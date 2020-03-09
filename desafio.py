# -*- coding: utf-8 -*-
N, M = [int(x) for x in input().split()]                    #N quantidade de baldes, M quantidades de operacoes

baldes = []                                                 #Lista que contem os baldes
bolas_iniciais = input().split()                            #Bolas iniciais de cada balde

for i in range(0, N):                                       #Loop na qnt de baldes
    lista_com_bola = [int(bolas_iniciais[i])]               #Cria uma lista com só o valor da bola inicial
    baldes.append(lista_com_bola)                           #Adiciona a lista com a bola inicial aos baldes

for i in range(0, M):                                       #Loop na qnt de operacoes
    operacao = [int(x) for x in input().split()]            #Pega os valores da operacao

    if operacao[0] == 1:                                    #Operação de inserção de bola, primeiro tipo                     
        P = operacao[1]                                     #Peso da bola
        I = operacao[2] - 1                                 #Id do balde, -1 já que o index da lista começa em 0

        baldes[I].append(P)                                 #Adiciona a bola de peso P no balde I
        baldes[I].sort()                                    #organizar balde, maior ultimo, menor primeiro

    elif operacao[0] == 2:                                  #Operação de imprimir a maior diferença absoluta, segundo tipo
        A = operacao[1] - 1                                 #Intervalo inferior, considerando que o index da lista começa em 0
        B = operacao[2] - 1                                 #Intervalo superior, considerando que o index da lista começa em 0

        diff = 0                                            #Diferença inicial
        for j in range(A, B):
            for k in range(j + 1, B + 1):                   #Loop pra comparar todos os bales entre A e B
                if baldes[j][-1] - baldes[k][0] > diff:     #Testa a diff entre maior bola do balde j e menor do k, indice -1 representa ultimo e indice 0 o primeiro
                    diff = baldes[j][-1] - baldes[k][0]
                if baldes[k][-1] - baldes[j][0] > diff:     #Testa a diff entre menor bola do balde j e maior do k, indice -1 representa ultimo e indice 0 o primeiro
                    diff = baldes[k][-1] - baldes[j][0]

        print(diff)