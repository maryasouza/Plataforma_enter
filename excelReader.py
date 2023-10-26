import pandas as pad


class ExcelReader:
    def _init_(self):
        # TODO document why this method is empty
        pass

    def read_file(self, file_name):
        excel_file = (file_name)
        senha_id = 'senha'

        # Leitura do Excel
        df = pad.read_excel(excel_file)
        senha = df[senha_id].tolist()

        return senha[0]
