# Compilador - Analisador lexico
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

Paulo Victor Fernandes Sousa
192050108

# Checklist

- [ x ] Analisador lexico
- [ ] Analisador sintatico
- [ ] Analisador semantico


# Particularidades do sistema
- Atualmente o programa consegue identificar as entradas transformando as em tokens e indentificando a qual grupo pertence.
- Caso não pertença a nenhum grupo é retornado um erro lexico.
- Após isso o sistema faz uma verificação de estados para cada tipo de token verificando se existe algum erro lexico.
- O programa retorna a linha e o token que contem o problema.
