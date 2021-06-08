import pymysql


def cadastro():
    conn = pymysql.connect(host="aulasegunda.mysql.uhserver.com",
                           user="convidado",
                           passwd="@FiCs2021",
                           db="aulasegunda")
    connection = conn.cursor()

    print("=================Cadastramento===================")
    print("+ Digite os dados solicitados para o cadastro   +")
    print("=================================================")
    estado = input(str("Digita o seu Estado: ")).upper()
    infectados = int(input("Digite o numero de infectados: "))
    mortos = int(input("Digite o número de mortos: "))
    curados = int(input("Digite o número de recuperados:"))

    stringTexto = "('{}', '{}', '{}', '{}')"
    stringTexto = stringTexto.format(estado, infectados, mortos, curados)
    connection.execute(
        "INSERT INTO `base_grupo06`(`estado`, `infectados`, `mortos`, `curados`)" + "VALUES" + stringTexto
    )
    conn.commit()
    conn.close()
