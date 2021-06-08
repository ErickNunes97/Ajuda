import pymysql
import time


def visualizacao():
    conn = pymysql.connect(host="aulasegunda.mysql.uhserver.com",
                           user="convidado",
                           passwd="@FiCs2021",
                           db="aulasegunda")
    connection = conn.cursor()
    connection.execute("SELECT `estado`, `infectados`, `mortos`, `curados`, `id` FROM `base_grupo06` ORDER BY id ASC;")

    print("============================Visualização===============================")
    print("+ Aqui é mostrado os estados cadastrados, assim como os dados do mesmo+")
    print("=======================================================================")

    for line in (connection.fetchall()):
        stringText = "| estado: {} | infectados: {} | mortos: {}| curados: {} | id:{}|"
        estado = line[0]
        infectados = line[1]
        mortos = line[2]
        curados = line[3]
        id = line[4]

        stringText = stringText.format(estado, infectados, mortos, curados, id)
        print(stringText)
        time.sleep(2.0)

    connection.close()
