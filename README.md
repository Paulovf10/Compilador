# Compilador 
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

Paulo Victor Fernandes Sousa
192050108

# Checklist

- [ x ] Analisador lexico
- [ ] Analisador sintatico
- [ ] Analisador semantico


# Analisador lexico
- Atualmente o programa consegue identificar as entradas transformando as em tokens e indentificando a qual grupo pertence.
- Caso não pertença a nenhum grupo é retornado um erro lexico.
- Após isso o sistema faz uma verificação de estados para cada tipo de token verificando se existe algum erro lexico.
- O programa retorna a linha e o token que contem o problema.

# Particularidades do sistema
- Devido ao fato da separação de tokens ser feita atraves da função split(), é necessario dar um espaço a cada token e informação digitada.
- O codigo é dividido em duas partes:
  1) A main onde a entrada é trasformada em token e feita as checagens.
  2) A classe estados onde é feita a verificação dos estados possiveis de cada token.

# Execução
- O programa retorna os erros caso existam.
- Um dicionario contendo todos os tokens e seus valores.
  
# Tokens
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

# Entrada
#include <stdio.h>
#include <conio.h>
int main ( void ) {
  int = 2 ;

  for ( i = 1 ; i <= 9 ; i++ ) {
    printf ( " Aprendendo Linguagem C \n " ) ;
  }

  getch ( ) ;
  return ( 0 ) ;
}

# Saida
[{'Palavra reservada - Função': '#include'}, {'Palavra reservada - Biblioteca': '<stdio.h>'}]
[{'Palavra reservada - Função': '#include'}, {'Palavra reservada - Biblioteca': '<conio.h>'}]
[{'Palavra reservada - Tipo': 'int'}, {'Palavra reservada - Tipo': 'main'}, {'Delimitador - Inicio': '('}, {'Palavra reservada - Tipo': 'void'}, {'Delimitador - Fim': ')'}, {'Delimitador - Inicio': '{'}]
[{'Palavra reservada - Tipo': 'int'}, {'Operador atribuição': '='}, {'Numero': '2'}, {'Separador': ';'}]
[]
[{'Palavra reservada - Repetição': 'for'}, {'Delimitador - Inicio': '('}, {'Indetificador': 'i'}, {'Operador atribuição': '='}, {'Numero': '1'}, {'Separador': ';'}, {'Indetificador': 'i'}, {'Operador relacional': '<='}, {'Numero': '9'}, {'Separador': ';'}, {'Indetificador': 'i++'}, {'Delimitador - Fim': ')'}, {'Delimitador - Inicio': '{'}]
[{'Palavra reservada - Função': 'printf'}, {'Delimitador - Inicio': '('}, {'String': '"'}, {'Indetificador': 'Aprendendo'}, {'Indetificador': 'Linguagem'}, {'Indetificador': 'C'}, {'Indetificador': '\\n'}, {'String': '"'}, {'Delimitador - Fim': ')'}, {'Separador': ';'}]
[{'Delimitador - Fim': '}'}]
[]
[{'Indetificador': 'getch'}, {'Delimitador - Inicio': '('}, {'Delimitador - Fim': ')'}, {'Separador': ';'}]
[{'Palavra reservada - Interação': 'return'}, {'Delimitador - Inicio': '('}, {'Numero': '0'}, {'Delimitador - Fim': ')'}, {'Separador': ';'}]
[{'Delimitador - Fim': '}'}]
