import openpyxl
import requests


def extract_excel():
    URL = "http://www.mizaniatouna.gov.tn/tunisia/template_fr/boost_fr.xlsx"
    FILE_NAME = "boost_db.xlsx"
    r = requests.get(URL)
    with open(FILE_NAME, "wb") as excel_f:
        excel_f.write(r.content)
    work_book = openpyxl.load_workbook(FILE_NAME, read_only=True)
    work_sheet = work_book.get_sheet_by_name("Sheet1")
    yield work_sheet
