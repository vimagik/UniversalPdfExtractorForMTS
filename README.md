# UniversalPdfExtractorForMTS

## Экспорт данных из платежек МТС банка

Если в 21 веке банк тебе не предоставляет выписку с которой можно будет в дальнейшем работать, например анализируя расходы и доходы за месяц, приходится писать вот такие сприты для получения необходимых данных в редактируемом виде. Текущая версия может обрабатывать PDF выписки из интернет-банка МТС на 09.03.2023. Если поменяется формат и скрипт перестанер работать, пишите, возможно поправлю. А может и нет =)

### Установка

1. Скачиваем содержимое из репозитория в папку
2. Запускаем Командную строку (консоль) и через команду cd "имя_папки", переходим в папку из пункта 1.
3. Создаем виртуальное окружение командой
```
python -m venv .venv
```
**ВНИМАНИЕ!** Предварительно у вас должен быть установлен Python 3.11.0 Может и на других версиях будет работать. Не проверял.

4. В Комндной строке запускаем виртуальное окружение 
```
.\.venv\Scripts\activate
```
5. Устанавливаем все необходимые библиотеки командой
```
pip install -r .\requirements.txt
```
6. Кладем сюда же все необходимые для анализа выписки из МТС банка в формате PDF, далее запускаем скрипт
```
python main.py
```

Вуаля, после работы скрипта в папке рядом с каждым PDF файло появится CSV файл содержащий операции из выписок в формате: дата операции, описание, сумма