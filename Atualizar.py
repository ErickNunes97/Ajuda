import pymysql


def atualizar():
    conn = pymysql.connect(host="aulasegunda.mysql.uhserver.com",
                           user="convidado",
                           passwd="@FiCs2021",
                           db="aulasegunda")
    connection = conn.cursor()

    print("==========================Atualizar============================")
    print("+ Digite os dados requisitados para a atualização da pesquisa +")
    print("===============================================================")

    estado = input(str("Digita o seu Estado: ")).upper()
    infectados = int(input("Digite o numero de infectados: "))
    mortos = int(input("Digite o número de mortos: "))
    curados = int(input("Digite o número de recuperados: "))
    id = int(input("Digite o ID do estado: "))

    stringTexto = "`estado` = '{}', `infectados`= {},`mortos`= {}, `curados`= {}  WHERE `id`= {};"
    stringTexto = stringTexto.format(estado, infectados, mortos, curados, id)
    connection.execute("UPDATE `base_grupo06` SET " + stringTexto)
    connection.execute("COMMIT;")
    connection.close()
