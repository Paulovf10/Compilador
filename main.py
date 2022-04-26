import re
from estados import Estados

tipos = ['char', 'int', 'const', 'double', 'float', 'void', 'long', 'short', 'main']
tipos_declara = ['%d', '%s']
condicionais = ['if', 'else']
repeticoes = ['for', 'while', 'do']
interacao = ['break', 'continue', 'return', 'goto']
funcoes = ['printf', '++', '--', '#include']
bibliotecas = ['<stdio.h>', '<conio.h>']
delimitador_inicio = ['(', '[', '{']
delimitador_fim = [')', ']', '}', ',']
operadores_aritimetico = ['-', '+', '/', '*']
operadores_logico = ['&&', '||', '!']
operadores_relacional = ['<', '>', '<=', '>=', '==', '!=']
operadores_relacional2 = ['++', '--']
jump = ['\n']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

a1 = [{'Indetificador': 'printf('}, {'String': '"'}, {'String': '"'}, {'Indetificador': 'contador'},
      {'Delimitador - Fim': ')'}, {'Separador': ';'}]
cd = [{'Palavra reservada - Repetição': 'for'}, {'Delimitador - Inicio': '('}, {'Indetificador': 'contador'},
     {'Operador atribuição': '='}, {'Numero': '10'}, {'Separador': ';'}, {'Indetificador': 'contador'},
     {'Operador relacional': '>='}, {'Numero': '1'}, {'Separador': ';'}, {'Indetificador': 'contador'},
     {'Palavra reservada - Função': '--'}, {'Delimitador - Fim': ')'}, {'Delimitador - Inicio': '{'}]

a = [{'Palavra reservada - Tipo': 'int'}, {'Palavra reservada - Tipo': 'main'}, {'Delimitador - Inicio': '('},
     {'Palavra reservada - Tipo': 'void'}, {'Delimitador - Fim': ')'}]

cont = 0



def literal_numero(num):
    flag = True
    for i in num:
        if i in numeros:
            continue
        else:
            return False
    return flag


def palavra_reservada(reserved):
    if reserved in tipos:
        pr = 'Palavra reservada - Tipo'
        return True, pr
    elif reserved in condicionais:
        pr = 'Palavra reservada - Condicional'
        return True, pr
    elif reserved in repeticoes:
        pr = 'Palavra reservada - Repetição'
        return True, pr
    elif reserved in interacao:
        pr = 'Palavra reservada - Interação'
        return True, pr
    elif reserved in funcoes:
        pr = 'Palavra reservada - Função'
        return True, pr
    elif reserved in bibliotecas:
        pr = 'Palavra reservada - Biblioteca'
        return True, pr
    else:
        return False


def indentificador(char):
    cadeia = re.compile(r'[a-zA-z]')
    busca = re.search(cadeia, char[0])
    if busca:
        return True
    else:
        return False


def cadeia_caracter(cac):
    if cac[0] == "\"" and cac[len(cac) - 1] == "\"":
        return True
    else:
        return False

def declara_tip(tip):
    if tip in tipos_declara:
        return True
    else:
        return False

def jlinha(lin):
    if lin in jump:
        return True
    else:
        return False

def operador_logico(logic):
    if logic in operadores_logico:
        return True
    else:
        return False


def operador_relacional(relational):
    if relational in operadores_relacional:
        return True
    else:
        return False


def operador_relacional2(relational):
    if relational in operadores_relacional2:
        return True
    else:
        return False


def operador_aritimetico(arithmetic):
    if arithmetic in operadores_aritimetico:
        return True
    else:
        return False


def operador_atribuicao(atrib):
    if atrib == '=':
        return True
    else:
        return False


def delimitador(limit):
    if limit in delimitador_inicio:
        a = 'Delimitador - Inicio'
        return True, a
    if limit in delimitador_fim:
        a = 'Delimitador - Fim'
        return True, a
    else:
        return False


def comentario(comment):
    if comment == '//':
        return True


def separador(separator):
    if separator == ';':
        return True
    else:
        return False


entrada = 1
Dic = { }
indice = 0
linha = 1
with open("entrada.txt") as file:
    for line in file:
        indice = indice + 1
        entrada = line
        entrada_token = str(entrada.split())
        lis = []
        list(entrada_token)
        i = 0

        for elem in eval(entrada_token):

            tokens = {}
            if palavra_reservada(elem):
                a, b = palavra_reservada(elem)
                tokens[b] = elem
                a = tokens.copy()
                lis.append(a)
            elif literal_numero(elem):
                tokens['Numero'] = elem
                a = tokens.copy()
                lis.append(a)
            elif cadeia_caracter(elem):
                tokens["String"] = elem
                a = tokens.copy()
                lis.append(a)
            elif operador_atribuicao(elem):
                tokens['Operador atribuição'] = elem
                a = tokens.copy()
                lis.append(a)
            elif operador_relacional(elem):
                tokens['Operador relacional'] = elem
                a = tokens.copy()
                lis.append(a)
            elif operador_relacional2(elem):
                tokens['Operador relacional2'] = elem
                a = tokens.copy()
                lis.append(a)
            elif jlinha(elem):
                tokens['Saltar Linha'] = elem
                a = tokens.copy()
                lis.append(a)
            elif operador_logico(elem):
                tokens['Operador logico'] = elem
                a = tokens.copy()
                lis.append(a)
            elif operador_aritimetico(elem):
                tokens['Operador aritimetico'] = elem
                a = tokens.copy()
                lis.append(a)
            elif separador(elem):
                tokens['Separador'] = elem
                a = tokens.copy()
                lis.append(a)
            elif delimitador(elem):
                b, a = delimitador(elem)
                tokens[a] = elem
                a = tokens.copy()
                lis.append(a)
            elif comentario(elem):
                tokens['comentario'] = elem
                a = tokens.copy()
                lis.append(a)
            elif indentificador(elem):
                tokens['Indetificador'] = elem
                a = tokens.copy()
                lis.append(a)
            elif declara_tip(elem):
                tokens['Tipo-Declaracão'] = elem
                a = tokens.copy()
                lis.append(a)
            else:
                print("Caractere não reconhecido", elem)
        #print(f"Tokens de entrada linha {linha}: {lis}\n")
        linha += 1
        h = lis.copy()
        Dic[indice] = h

for elem in Dic:
    print(Dic[elem])
for ele in Dic:
    erro = 1
    cont = 0
    while cont < len(Dic[ele]):
        Estados.condicioal(Dic[ele], cont, erro)
        Estados.ponto_vir(Dic[ele], cont , erro)
        Estados.tipos(Dic[ele], cont, erro)
        Estados.operadores_logico(Dic[ele], cont, erro)
        Estados.colchetes(Dic[ele], cont, erro)
        Estados.declaracao(Dic[ele], cont, erro)
        Estados.loop_for(Dic[ele], cont, erro)
        Estados.mais_menos(Dic[ele], cont, erro)
        Estados.operadores_aritimetico(Dic[ele], cont, erro)
        Estados.operadores_atribuicao(Dic[ele], cont, erro)
        Estados.operadores_relacional(Dic[ele], cont, erro)
        Estados.parenteses(Dic[ele], cont, erro)
        cont += 1
    erro +=1
