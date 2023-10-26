import sys
import openpyxl


def rwExcel():
    if len(sys.argv) != 2:
        print("use um arquivo excel <xlsx_file>")
        return
    xlsx_file = sys.argv[1]
    senha = ""

    try:
        workbook = openpyxl.load_workbook(xlsx_file)
        sheet = workbook.worksheets[0]
        data = [str(cell[0].value) for cell in sheet.iter_rows(min_col=1, max_col=1)]
        data.pop(0)
        formatted_data = "','".join(data)
        senha = f"{formatted_data}"
        return senha
    except Exception as e:
        print(f"ocorreu um erro: {e}")
