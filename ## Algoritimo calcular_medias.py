## Algoritmo calcular_medias

# Solicita ao usuário que insira as notas
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

# Calcula a média das notas
media = (n1 + n2) / 2

# Verifica se a média é suficiente para aprovação
if media >= 7:    
    print(f'A média das notas é: {media:.2f}. Você foi aprovado!')
else:    
    print(f'A média das notas é: {media:.2f}. Você foi reprovado!')