import os
os.system("cls")

n_arquivo = ""

def menu() -> None:
    print('''
    1 - Nomear arquivo
    2 - Sobescrever o aruivo (w)
    3  - Editar o arquivo (a)
    4 - Criar um novo arquivo (x)
    5 - Exibir o conteúdo do arquivo (r)
    0 - Sair
          ''')
    escolha = input("Escolha uma opção: ")
    while escolha != 0:
        match escolha:
            case "0":
                break
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case _:
                print("Resposta inválida!")

def nomear_arquivo() -> None:
    n_arquivo = input("Digite o nome para o arquivo: ")
    arquivo = open(n_arquivo + ".txt", "w", encoding="utf-8")
    arquivo.close()
    print("Arquivo criado com sucesso!")

def sobrescrever() -> None:
    s_arquivo = input("Sobrescrever: ")
    arquivo = open(n_arquivo + ".txt", "w", encoding="utf-8")
    arquivo.write(s_arquivo)
    arquivo.close()
    print("Arquivo criado com sucesso!")
