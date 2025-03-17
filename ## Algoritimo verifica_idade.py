## Algoritimo verifica_idade

# Função para verificar idade
def verificar_maior_idade(idade):    
    if idade >= 18:        
        return "Você é maior de idade."    
    else:        
        return "Você é menor de idade."

# Solicita ao usuário a idade dele
idade = int(input('Digite a sua idade: '))

# Mostra o resultado
resultado = verificar_maior_idade(idade)
print(resultado)