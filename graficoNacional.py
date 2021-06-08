import pymysql
import matplotlib.pyplot as plt
import numpy as np

def graficoNacional():
    conn = pymysql.connect(host="aulasegunda.mysql.uhserver.com",
                           user="convidado",
                           passwd="@FiCs2021",
                           db="aulasegunda")
    conexao = conn.cursor()
    conexao.execute("SELECT SUM(`infectados`) ,SUM(`mortos`), SUM( `curados`) FROM `base_grupo06`;")

    labels =['Total Nacional']
    infected_means = []
    deads_means = []
    recovered_means =[]

    for linha in (conexao.fetchall()):
        infected_means.append(int(linha[0]))
        deads_means.append(int(linha[1]))
        recovered_means.append(int(linha[2]))

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 1, infected_means, width, label='Infectados', color = 'blue')
    rects2 = ax.bar(x  , deads_means, width, label='Mortos', color = 'orange')
    rects3 = ax.bar(x + width / 1, recovered_means, width, label='Recuperados', color = 'green')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Quantdade')
    ax.set_title('Quantidade de Infectados, Mortos e Recuperados por COVID-19:')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=1)
    ax.bar_label(rects2, padding=1)
    ax.bar_label(rects3, padding=1)



    fig.tight_layout()

    plt.show()

    conn.close()