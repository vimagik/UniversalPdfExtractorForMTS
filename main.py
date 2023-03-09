import os
import re
import csv
from PyPDF2 import PdfReader


PATTERN = r"([A-Z]+[\s\w>\\\-\.\,()]+)([−|+][\d \,]+)\D+(\d{2}\.\d{2}\.\d{4})"


def extract_first_page(reader: PdfReader) -> str:
    """Read the first page of the pdf"""
    page = reader.pages[0]
    text = page.extract_text()
    start_table = text.find("Наименование операции Сумма Дата и время Статус") + \
        len("Наименование операции Сумма Дата и время Статус") + 1
    end_table = text.find("Последние операции по карте")
    main_data = text[start_table: end_table]
    clean_data = re.sub(r"^\s+|\n|\r|\s+$", " ", main_data)
    return clean_data


def extract_another_page(reader: PdfReader, page_number: int) -> str:
    """Reading the second and subsequent pages of the PDF"""
    page = reader.pages[page_number]
    text = page.extract_text()
    end_table = text.find(
        "МТС Деньги – удобный сервис для быстрых переводов и платежей"
        ) - 1
    main_data = text[:end_table]
    clean_data = re.sub(r"^\s+|\n|\r|\s+$", " ", main_data)
    return clean_data


def find_data(data: str) -> list:
    """Searching for information via regular expressions"""
    struct_data = []
    for row in re.findall(PATTERN, data):
        dict_row = {
            "desc": row[0],
            "amount": row[1].replace(" ", "").replace("−", "-"),
            "date": row[2]
        }
        struct_data.append(dict_row)
    return struct_data


def save_to_csv(data: list, output_name: str) -> None:
    output_name += ".csv"
    with open(output_name, 'w', newline='', encoding="utf-8") as csvfile:
        fieldnames = ['date', 'desc', 'amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def extract_data_from_pdf(file_name: str) -> None:
    """Basic function, we give a PDF file as input"""
    reader = PdfReader(file_name)
    csv_data = []
    data = extract_first_page(reader)
    csv_data = find_data(data)
    for page_number in range(1, len(reader.pages)):
        data = extract_another_page(reader, page_number)
        csv_data += find_data(data)
    output_name = file_name[:-4]
    save_to_csv(csv_data, output_name)


if __name__ == "__main__":
    for file in os.listdir():
        if file.endswith(".pdf"):
            extract_data_from_pdf(file)
    