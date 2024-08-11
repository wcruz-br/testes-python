print()
print('*************')
print('Exercício 3.1')
print('*************')
print()
# Escreva uma função chamada right_justify, que receba uma string chamada s como parâmetro
# e exiba a string com espaços suficientes à frente para que a última letra da string esteja na coluna 70 da tela

def right_justify(s):
    if len(s) < 70:
        print(" " * (70 - len(s)) + s)
    else:
        print(s)

for i in ('monty',
          'teste de alinhamento',
          'um texto um pouco maior para ver o que acontece',
          '70certinho' + '-' * 60,
          'passei dos 70 com essa: ' + '=' * 75):
    right_justify(i)

print()
print("-" * 100)

print()
print('*************')
print('Exercício 3.2')
print('*************')
print()
# Um objeto de função é um valor que pode ser atribuído a uma variável ou passado como argumento.
# Por exemplo, do_twice é uma função que toma um objeto de função como argumento e o chama duas vezes:
def do_twice(f):
    f()
    f()

# Aqui está um exemplo que usa do_twice para chamar uma função chamada print_spam duas vezes:
def print_spam():
    print('spam')
do_twice(print_spam)
print()

# 1) Digite este exemplo em um script e teste-o.
# 2) Altere do_twice para que receba dois argumentos, um objeto de função e um valor,
#    e chame a função duas vezes, passando o valor como um argumento.
def do_twice_2(f, val):
    f(val)
    f(val)

# 3) Copie a definição de print_twice que aparece anteriormente neste capítulo no seu script.
def print_twice(bruce):
    print(bruce)
    print(bruce)

# 4) Use a versão alterada de do_twice para chamar print_twice duas vezes, passando 'spam' como um argumento.
do_twice_2(print_twice, 'spam')
print()

# 5) Defina uma função nova chamada do_four que receba um objeto de função e um valor
#    e chame a função quatro vezes, passando o valor como um parâmetro.
#    Deve haver só duas afirmações no corpo desta função, não quatro.
def do_four(f, val):
    do_twice_2(f, val)
    do_twice_2(f, val)

do_four(print_twice, 'spam')

print()
print("-" * 100)

print()
print('*************')
print('Exercício 3.3')
print('*************')
print()
# 1) Escreva uma função que desenhe uma grade como a seguinte:
        # + - - - - + - - - - +
        # |         |         |
        # |         |         |
        # |         |         |
        # |         |         |
        # + - - - - + - - - - +
        # |         |         |
        # |         |         |
        # |         |         |
        # |         |         |
        # + - - - - + - - - - +

def do_twice_33_0(f):
    f()
    f()

def do_twice_33_1(f, val):
    f(val)
    f(val)

def do_four_33_1(f, val):
    do_twice_33_1(f, val)

def do_twice_33_2(f, val1, val2):
    f(val1, val2)
    f(val1, val2)

def do_four_33_2(f, val1, val2):
    do_twice_33_2(f, val1, val2)

def linha(val1, val2):
    do_twice_33_2(meia_linha, val1, val2)
    print(val1)

def meia_linha(val1, val2):
    char_and_space(val1)
    do_four_33_1(char_and_space, val2)

def char_and_space(val):
    print(val, end=' ')

def grade():
    do_twice_33_0(meia_grade)
    linha('+', '-')

def meia_grade():
    linha('+', '-')
    do_four_33_2(linha, '|', ' ')

grade()

# Obs.: tem jeito melhor de fazer, mas quis seguir o padrão das respostas dos exercícios anteriores
