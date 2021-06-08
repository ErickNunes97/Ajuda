import pymysql
import matplotlib.pyplot as plt
import numpy as np


def grafico():
    conn = pymysql.connect(host="aulasegunda.mysql.uhserver.com",
                           user="convidado",
                           passwd="@FiCs2021",
                           db="aulasegunda")
    conexao = conn.cursor()
    conexao.execute("SELECT `id`, `estado`, `infectados`, `mortos`, `curados` FROM `base_grupo06` ORDER BY estado ASC; ")

    labels = []
    infected_means = []
    deads_means = []
    recovered_means =[]



    for linha in (conexao.fetchall()):
        labels.append(linha[1])
        infected_means.append(linha[2])
        deads_means.append(linha[3])
        recovered_means.append(linha[4])

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, infected_means, width, label='Infectados', color='blue')
    rects2 = ax.bar(x + width / 4, deads_means, width, label='Mortos', color='orange')
    rects3 = ax.bar(x + width / 1, recovered_means, width, label='Recuperados', color='green')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Quantdade')
    ax.set_title('Quantidade de Infectados, Mortos e Recuperados por COVID-19:')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=2)
    ax.bar_label(rects2, padding=2)
    ax.bar_label(rects3, padding=2)



    fig.tight_layout()

    plt.show()

    conn.close()
