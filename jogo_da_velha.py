import random


def jogar_teste():
    linha_1 = [" + "] * 3
    linha_2 = [" + "] * 3
    linha_3 = [" + "] * 3
    linhas = [linha_1, linha_2, linha_3]

    xis = " x "
    circ = " o "

    for i in range(3):
        # isso add xis
        numero_aleatorio_xis = random.randint(0, 2)
        numero_aleatorio_linha = random.randint(0, 2)

        while True:

            if linhas[numero_aleatorio_linha][numero_aleatorio_xis] == " + ":

                linhas[numero_aleatorio_linha][numero_aleatorio_xis] = xis
                break

            else:

                # chance 50% de escolher outra linha. Arrumar dps
                if random.randint(0, 10) <= 5:
                    numero_aleatorio_linha = random.randint(0, 2)

                numero_aleatorio_xis = random.randint(0, 2)


        # isso add circ
        numero_aleatorio_xis = random.randint(0, 2)
        numero_aleatorio_linha = random.randint(0, 2)

        while True:

            if linhas[numero_aleatorio_linha][numero_aleatorio_xis] == " + ":

                linhas[numero_aleatorio_linha][numero_aleatorio_xis] = circ
                break

            else:

                # chance 50% de escolher outra linha. Arrumar dps
                if random.randint(0, 10) <= 5:
                    numero_aleatorio_linha = random.randint(0, 2)

                numero_aleatorio_xis = random.randint(0, 2)



    print("".join(linha_1))
    print("".join(linha_2))
    print("".join(linha_3))

    xis_diagonal_1 = linha_2[1] == xis and linha_1[0] == xis and linha_3[2] == xis
    xis_diagonal_2 = linha_2[1] == xis and linha_3[0] == xis and linha_1[2] == xis

    circulo_diagonal_1 = linha_2[1] == circ and linha_1[0] == circ and linha_3[2] == circ
    circulo_diagonal_2 = linha_2[1] == circ and linha_3[0] == circ and linha_1[2] == circ


    ganhou_em_diagonal = xis_diagonal_1 or xis_diagonal_2 or circulo_diagonal_1 or circulo_diagonal_2

    contador = 0

    while contador < 3:

        if linhas[contador].count(xis) == 3 or linhas[contador].count(circ) == 3:
            ganhou_em_horizontal = True
        else:
            ganhou_em_horizontal = False

        vertical_xis = "x" in linha_1[contador] and "x" in linha_2[contador] and "x" in linha_3[contador]
        vertical_circ = "o" in linha_1[contador] and "o" in linha_2[contador] and "o" in linha_3[contador]

        ganhou_em_vertical = vertical_xis or vertical_circ
        if ganhou_em_vertical:
            print("Ganhou vertical", ganhou_em_vertical)
            break

        elif ganhou_em_horizontal:
            print("Ganhou horizontal", ganhou_em_horizontal)
            break

        elif ganhou_em_diagonal:
            print("Ganhou diagonal", ganhou_em_diagonal)
            break

        else:
            contador += 1

    print()

for i in range(5):
    jogar_teste()
