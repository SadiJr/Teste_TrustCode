# -*- coding: utf-8 -*-
import sys
import math

#class Testes:
 #   def __init__():
  #      pass

def primeiro_teste(lista, numero):
    maxVal = max(lista)
    minVal = min(lista)

    if numero > maxVal or numero < minVal:
        print("O número digitado não está na lista\n")
        main()
    else:
        calculo(lista, numero)

        
'''        if numero > maxVal and numero < minVal:
            print("O número digitado  não existe dentro da lista.\nPor favor, repense suas escolhas e digite um valor válido")
            main()
        else:
            calculo(lista, numero)
    #primeiro_teste(lista, numero)'''
                    
def calculo(lista, numero):
        tamanho = len(lista)
        achei = False
        acesso = int(tamanho/2)
        contador = 0
        while(not achei):
            contador = contador + 1
            if lista[acesso] > numero:
                acesso = int(acesso/2)
                continue
            elif numero > lista[acesso]:
                if(int(acesso + acesso /2) > tamanho - 1):
                    acesso = tamanho - 1
                else:
                    acesso = int(acesso + acesso/2)
                continue
            else:
                achei = True

        print("Foram necessárias",contador," operações\n")
            

def segundo_teste(lista_1, lista_2):
    lista_final = list(set(lista_1) & set(lista_2))
    print(lista_final)
    #segundo_teste(lista_1, lista_2)

def terceiro_teste(numero):
    lista_primos = []
    quantidade_primos = 0
    operacoes = 0
    if numero < 1:
        #print("O numero digitado eh invalido, pois nao possui nenhum numero primo antes dele e o mesmo nao eh primo.\n Retorne essa funcao quando souber matematica basica\n")
        print("O número digitado é inválido. Tente digitar apenas números positivos e acima de 1")
        main()
    else:
        A = list(range(2, numero+1))
        for i in range(2, int(math.sqrt(numero)+1)):
            if i in A:
                for j in range(i**2, numero+1, i):
                    if j in A: A.remove(j)
        print(A)


        '''Método antigo: apenas verificava se era primo e não fazia mais nada
        divisores = 1;
        for divisor in range(2, numero):
            for dividendo in range(2, numero):
                if divisor % dividendo ==0:
                    divisores = divisores +1
                if divisores >= 3:
                    #não é primo
                    break
                else:
                    lista_primos.append(divisor)
    print(lista_primos)'''
        
def quarto_teste():
        palavra = input("Digite a palavra\n")
        resultado = 0;
        for letra in palavra:
            if(letra.lower() == letra):
                #Significa que a letra é mínuscula;
                print(ord(letra) % 96)
                resultado += ord(letra) % 96
            else:
                print((ord(letra) % 64) + 26)
                resultado += (ord(letra) % 64) + 26
        #valor = self.converte(palavra)
        divisores = 0
        for divisor in range(1, resultado):
            if resultado % divisor == 0:
                divisores = divisores + 1
                if divisores > 2:
                    break
        if divisores > 2:
            print("A palavra ", palavra, " não é prima\n")
        else:
            print("A palavra ", palavra, " é prima\n")
    #quarto_teste()

def main():
        
        opcao = int(input("Digite uma das seguintes opções:\n1 - Primeiro Teste\n2 - Segundo Teste\n3 - Terceiro Teste\n4 - Quarto Teste\n0 - Encerrar Testes\n"))
        if opcao == 1:
            lista = eval((input("Digite a lista ordenada(ou use um comando para a criar\nExemplo [0,1,2,4,5,6] e não lista = [0,1,2,3,4,5,6])\n")))
            numero = int(input("Digite o número que deseja buscar\n"))
            primeiro_teste(lista, numero)
            main()
            pass
        elif opcao == 2:
            lista_1 = eval((input("Digite a primeira lista(ou use o comando [] para a criar)\n")))
            lista_2 = eval((input("Digite a segunda lista(ou use um comando [] para a criar)\n")))
            segundo_teste(lista_1, lista_2)
            main()
            pass
        elif opcao == 3:
            numero = int(input("Digite um número\n"))
            terceiro_teste(numero)
            main()
            pass
        elif opcao == 4:
            quarto_teste()
            main()
            pass
        else:
            print("Até logo")
            sys.exit()
