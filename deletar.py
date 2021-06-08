import pymysql


def deletar() -> object:
    conn = pymysql.connect(host="aulasegunda.mysql.uhserver.com",
                           user="convidado",
                           passwd="@FiCs2021",
                           db="aulasegunda")
    connection = conn.cursor()

    print("=========================Deletar=============================")
    print("+ Aqui você poderá deletar o estado cadastrado              +")
    print("+ Assim que o novo cadastro é feito, será gerado um novo id +")
    print("+ Deseja mesmo deletar?                                     +")
    print("=============================================================")

    opcao = input("Se deseja deletar, digite 'S' para Sim e 'N' para Não....")

    if opcao == "Sim":
        id = int(input("Digite o ID do estado: "))
        print("O estado de ID:" + str(id) + "foi deletado da sua base.")
    else:
        print("Seu registro permanecerá na base de Dados, boa pesquisa! ")

    connection.execute("DELETE FROM `base_grupo06` WHERE `base_grupo06`.`id` =" + str(id) + ";")
    connection.execute("COMMIT;")
    connection.close()
