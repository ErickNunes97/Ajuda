from cadastro import cadastro
from Atualizar import atualizar
from visualizar import visualizacao
from grafico import grafico
from deletar import deletar
from totalNacional import total
from graficoNacional import graficoNacional

print("===================== Sistema de Notas =======================")
print("Seja bem-vindo ao sistema de pesquisa nacional sobre a COVID-19 para continuar "
      "\nbasta acessar o menu abaixo digitando uma das opções.")
print("Digite 1 para iniciar o programa: ")
print("==============================================================")

digito = int(input("Escreva o digito pro favor.... \n"))

while digito != 0:
    print("======================= Menu Principal =======================")
    print("+ 1 - Cadastrar                                              +")
    print("+ 2 - Atualizar Cadastro                                     +")
    print("+ 3 - Visualizar Cadastros                                   +")
    print("+ 4 - Visualizar gráfico com a quantidade de pessoas         +")
    print("+ 5 - Deletar Estado do Sistema                              +")
    print("+ 6 - Total Nacional (Infectados, Mortos e Recuperados)      +")
    print("+ 7 - Se deseja ver o gráfico o total nacional de infectados,+"
          "\n+     mortos e recuperados                                   +")
    print("+ 0 - Para Sair                                              +")
    print("==============================================================")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        cadastro()

    if opcao == 2:
        atualizar()

    if opcao == 3:
        visualizacao()
    if opcao ==4:
        grafico()

    if opcao == 5:
        deletar()

    if opcao == 6:
        total()

    if opcao == 7:
        graficoNacional()

    if opcao ==0:
        break;