import os;os.system("cls")

print("Arquivos texto")

nome_arquivo = "dados3.txt"

arquivo = open(nome_arquivo + ".txt", "w", encoding="utf-8")
arquivo.write("Linha1\n")
arquivo.write("Linha2\n")
arquivo.write("Linha3\n")
arquivo.close()

arquivo = open(nome_arquivo, "r", encoding="utf-8")
conteudo = arquivo.read()
arquivo.close()
print(conteudo)

'''try:
    os.mkdir("d:\edson2")
except FileExistsError:
    print("O arquivo já existe!")
else:    
    arquivo = open(nome_arquivo + ".txt", "w", encoding="utf-8")
    arquivo.write("Linha1\n")
    arquivo.write("Linha2\n")
    arquivo.write("Linha3\n")
    arquivo.close()
    print("Arquivo gravado com sucesso!")
'''


import os
os.system("cls" if os.name == "nt" else "clear")

print("Arquivos texto")
# Podemos abrir, ler, gravar e escrever em arquivos texto
# Formas de abertura
'''
'w' - write / escrita
'r' - read / leitura
'a' - append / edição
'x' - gravação exclusiva
'+' - ?????
'''
arquivo = open('dados.txt','w',encoding="utf-8") #open () -> abre um arquivo 
# enconding="utf-8" deixa em pt-br
arquivo.write('Salário do João -> 452.78\n')
arquivo.close()
print("Arquivo gravado com sucesso!")
 
arquivo = open('dados.txt','r',encoding="utf-8") #open() -> abre um arquivo
conteudo = arquivo.read()
print("Conteudo do arquivo: ")
print(conteudo)
arquivo.close()
 
arquivo = open('dados.txt','a',encoding="utf-8") #open() -> abre um arquivo
arquivo.write("Nova linha")
arquivo.close()
print("Arquivo gravado com sucesso!")
 
arquivo = open('dados.txt','a',encoding="utf-8") #open() -> abre um arquivo
msg = input("Digite o conteudo do arquivo:")
arquivo.write(msg + "\n")
arquivo.close()
print("Arquivo gravado com sucesso!")

