print('Hello Word!')

nome = 'Gabi'
idade = 18
print('Olá, ',nome, ' vc tem, ',idade, ' correto?')

nome = input('Informe o nome!')
idade = input('Informe a idade!')
print('Olá, ',nome, ' vc tem, ',idade, ' correto?') #1 forma de concatenar
print('Olá, '+nome+ ' vc tem, '+idade+ ' correto?') #2 forma de concatenar

'''
EXERCICIO: Faça um formulario que pergunte
o nome, cpf, endereco, idade, altura e telefone
e imprima isso em um relatorio organizado
'''

nome = input('Escreva seu nome: ')
cpf = input('Escreva seu CPF: ')
endereco = input('Escreva seu Endereço: ')
idade = input('Escreva sua idade: ')
altura = input('Escreva sua altura: ')
telefone = input('Escreva seu telefone: ')

print('Nome:', nome)
print('CPF:', cpf)
print('Endereço:', endereco)
print('Idade:', idade, 'anos')
print('Altura:', altura, 'metros')
print('Telefone:', telefone)
