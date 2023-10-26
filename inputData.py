from cryptography.fernet import Fernet
from excelReader import ExcelReader
from rwExcel import SenhaInformationExporter, ExcelExporter

from readWriter import rwExcel


def menu(senhaCripto):
    password = rwExcel()

    senha = password
    # encriptografa a mensagem
    chave = Fernet.generate_key()
    fernet = Fernet(chave)

    encSenha = fernet.encrypt(senha.encode())

    print('')
    print("*****************************************************")
    print("=     DIGITE A SENHA DE ACESSO A PLATAFORMA         =")
    print("*                                                   *")
    print("=     CUIDADO, SOMENTE 3 TENTATIVAS!!!!!!           =")
    print('*****************************************************')
    print('')
    print('')

    senha_infos = SenhaInformationExporter(ExcelExporter(), encSenha)
    senha_infos.export_senha_information("Minhasenha.xlsx")

    senhasCriptos = ExcelReader().read_file('C:/Users/pedro/OneDrive/Área de Trabalho/projetos python/APS '
                                            'Base/Minhasenha.xlsx')

    # senha descript.
    decSenha = fernet.decrypt(senhasCriptos).decode()

    return decSenha
