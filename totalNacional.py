import pymysql
import time
from graficoNacional import graficoNacional

def total():
    conn = pymysql.connect(host="aulasegunda.mysql.uhserver.com",
                           user="convidado",
                           passwd="@FiCs2021",
                           db="aulasegunda")
    connection = conn.cursor()
    connection.execute("SELECT SUM(`infectados`) ,SUM(`mortos`), SUM( `curados`) FROM `base_grupo06`;")


    print("============================Total Nacional de Casos===============================")


    for line in (connection.fetchall()):
        stringText = "| infectados: {} | mortos: {}| curados: {} |"
        infectados = line[0]
        mortos = line[1]
        curados = line[2]


        stringText = stringText.format(infectados, mortos, curados)
        print("Total Nacional :" + stringText)
        print("\n===============================================================================")

        print("Deseja visualizar um gráfico sobre tais dados:")

        opcao = input("Digite 'S' para Sim e 'N' para não:")

        if opcao == 's' or 'S':
            graficoNacional()

        else:
            print("Tudo bem, até a próxima!")

        time.sleep(2.0)

    connection.close()
