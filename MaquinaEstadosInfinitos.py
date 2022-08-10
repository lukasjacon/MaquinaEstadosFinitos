# Lukas Jacon Barboza
"""
ENUNCIADO
    Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a
linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  determinar  se  uma  string de
entrada  faz  parte  da  linguagem  𝐿    definida  por  𝐿 = {𝑥 | 𝑥 ∈
 {𝑎,𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏} segundo o alfabeto  Σ={𝑎,𝑏,𝑐}.
O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt)
contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de
entrada. As linhas subsequentes contém uma string por linha.  A seguir está um exemplo das linhas que
podem existir em um arquivo de testes para o programa que você irá desenvolver:
        3
        abbaba
        abababb
        bbabbaaab
    Neste  exemplo  temos  3  strings  de  entrada.  O  número  de  strings em  cada  arquivo  será
representado  por  um  número  inteiro  positivo.  A  resposta  do  seu  programa  deverá  conter  uma, e
somente uma linha de saída para cada string. Estas linhas conterão a string de entrada e o resultado
da validação conforme o formato indicado a seguir:
        abbaba: não pertence.
    A  saída  poderá  ser  enviada  para  um  arquivo  de  textos,  ou  para  o  terminal  padrão  e  será
composta de uma linha de saída por string de entrada. No caso do exemplo, teremos 3 linhas de saída.
Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada
contendo um número diferente de strings diferentes. Os arquivos de entrada criados para os seus testes
devem estar disponíveis tanto no ambiente repl.it quanto no ambiente Github. Observe que o professor
irá  testar  seu  programa  com  os  arquivos  de  testes  que  você  criar  e  com,  no  mínimo  um  arquivo  de
testes criado pelo próprio professor.
"""

import os


def validaSimbolo(Simbolos):
    listaSimbolos = ['a', 'b', 'c']
    tamanhoSimbolo = len(Simbolos)
    resultado = True

    for i in range(0, tamanhoSimbolo):
        Simbolo = Simbolos[i]
        if Simbolo not in listaSimbolos:
            return False
        elif Simbolo == "a":
            if i == tamanhoSimbolo - 1 or i == tamanhoSimbolo - 2:
                return False
            if Simbolos[i + 1] == "b" and Simbolos[i + 2] == "b":
                resultado = True
            else:
                return False
    return resultado


arquivos = os.listdir('texto')
for arquivo in arquivos: # Loop que passa por cada arquivo, seguido por um comando que retornará a extensão do arquivo, para validação.
    extensao = os.path.splitext(arquivo)[1]
    if extensao == ".txt":
        # Caso o arquivo seja um '.txt', ele é aberto e lido.
        # A estrutura 'with' efetua o fechamento automático do arquivo após seu uso.
        with open("texto/%s" % arquivo) as dados:
            nomes = dados.readlines()
            quantidadeSimbolos = int(nomes[0])
            contador = 1

            while contador <= quantidadeSimbolos:
                Simbolo = nomes[contador].strip('\n')
                resposta = validaSimbolo(Simbolo)
                if resposta:
                    print("%s: pertence." % Simbolo)
                else:
                    print("%s: não pertence." % Simbolo)
                contador += 1
