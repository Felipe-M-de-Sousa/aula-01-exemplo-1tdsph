n1 = float(input('Escolha o primeiro número: '))
n2 = float(input('Escolha o segundo número: '))
print('\nEscolha uma operação:')
print('1. Somar')
print('2. Subtrair')
print('3. Dividir')
print('4. Mutiplicar')
opcao = input('Digite a opção (1/2/3/4): ')
if opcao == '1':
    print(f'O resultado da soma é: {n1 + n2}')
elif opcao == '2':
    print(f'O resultado da subtração é: {n1 - n2}')
elif opcao == '3':
    print(f'O resultado da divisão é: {n1 / n2}')
elif opcao == '4':
    print(f'O resultado da multiplicação é: {n1 * n2}')
else:
    print('Saindo da calculadora!')