from termcolor import colored
import random

linha_1 = [" 1 ", " 2 ", " 3 "]
linha_2 = [" 4 ", " 5 ", " 6 "]
linha_3 = [" 7 ", " 8 ", " 9 "]
linhas = [linha_1, linha_2, linha_3]

xis = " x "
circ = " o "

jogar_primeiro = random.randint(0, 1)

ninguem_ganhou = False


def coloca_xis_ou_circ(xis_ou_circ):
    num_random_xis_circ = random.randint(0, 2)
    num_random_linha = random.randint(0, 2)

    while True:

        espaco_vazio_1 = linhas[num_random_linha][num_random_xis_circ] != xis
        espaco_vazio_2 = linhas[num_random_linha][num_random_xis_circ] != circ
        espaco_vazio = espaco_vazio_1 and espaco_vazio_2

        if espaco_vazio:

            linhas[num_random_linha][num_random_xis_circ] = xis_ou_circ
            break

        else:

            # chance 50% de escolher outra linha. Arrumar dps
            if random.randint(0, 10) <= 5:
                num_random_linha = random.randint(0, 2)

            num_random_xis_circ = random.randint(0, 2)


def imprime_linhas():
    global linha_1, linha_2, linha_3

    print("".join(linha_1))
    print("".join(linha_2))
    print("".join(linha_3))
    print()


def logica_perdeu_ganhou():
    global ninguem_ganhou

    diagonal_esq_e_dir = linha_1[0] == linha_2[1] == linha_3[2] or linha_1[2] == linha_2[1] == linha_3[0]

    ganhou_em_diagonal = linha_2[1] != " 5 " and diagonal_esq_e_dir

    contador = 0
    venceu = False

    while contador < 3:

        # print("teste", contador)

        ganhou_em_horizontal = len(set(linhas[contador])) == 1

        ganhou_em_vertical = linha_1[contador] == linha_2[contador] == linha_3[contador]

        ninguem_ganhou = ganhou_em_horizontal == ganhou_em_vertical == ganhou_em_diagonal

        if ganhou_em_horizontal or ganhou_em_vertical or ganhou_em_diagonal:
            colorir_caracteres_venceu(contador, ganhou_em_horizontal, ganhou_em_vertical, ganhou_em_diagonal)
            imprime_linhas()

        if ganhou_em_vertical:
            print("Ganhou vertical", ganhou_em_vertical)
            venceu = True
            break

        elif ganhou_em_horizontal:
            print("Ganhou horizontal", ganhou_em_horizontal)
            venceu = True
            break

        elif ganhou_em_diagonal:
            print("Ganhou diagonal", ganhou_em_diagonal)
            venceu = True
            break

        contador += 1
    return venceu


def colorir_caracteres_venceu(local_do_caractere, ganhou_horizontal, ganhou_vertical, ganhou_diagonal):
    if ganhou_horizontal:
        for i in range(3):
            linhas[local_do_caractere][i] = colored(linhas[local_do_caractere][i], 'green')

    if ganhou_vertical:
        for i in range(3):
            linhas[i][local_do_caractere] = colored(linhas[i][local_do_caractere], 'green')

    if ganhou_diagonal:
        if linha_1[0] == linha_2[1] == linha_3[2]:
            for i in range(3):
                linhas[i][i] = colored(linhas[i][i], 'blue')

        if linha_1[2] == linha_2[1] == linha_3[0]:
            contador_posicao = 0
            for i in range(2, -1, -1):
                linhas[i][contador_posicao] = colored(linhas[i][contador_posicao], 'red')
                contador_posicao += 1


def zerar_var_linha_e_linhas():
    global linha_1, linha_2, linha_3, linhas, jogar_primeiro

    linha_1 = [" 1 ", " 2 ", " 3 "]
    linha_2 = [" 4 ", " 5 ", " 6 "]
    linha_3 = [" 7 ", " 8 ", " 9 "]

    linhas = [linha_1, linha_2, linha_3]

    jogar_primeiro = random.randint(0, 1)


def jogar_testes():
    num_jogada = 0

    if jogar_primeiro == 1:
        parametro_xis_ou_circ_0 = xis
        parametro_xis_ou_circ_1 = circ
    else:
        parametro_xis_ou_circ_1 = circ
        parametro_xis_ou_circ_0 = xis

    while True:

        coloca_xis_ou_circ(parametro_xis_ou_circ_0)  # add X
        num_jogada += 1
        # print("colocou x")
        if num_jogada >= 5 and logica_perdeu_ganhou():
            print("X ganhou")
            break
        elif num_jogada >= 9 and ninguem_ganhou:
            imprime_linhas()
            print("Draw")
            break

        coloca_xis_ou_circ(parametro_xis_ou_circ_1)  # add O
        num_jogada += 1
        # print("colocou O")
        if num_jogada >= 5 and logica_perdeu_ganhou():
            print("O ganhou")
            break
        elif num_jogada >= 9 and ninguem_ganhou:
            imprime_linhas()
            print("Draw")
            break

    print("¨" * 20)

    zerar_var_linha_e_linhas()

    print()


for x in range(1):
    jogar_testes()
