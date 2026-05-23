print("Bem-vindo a Loja de Gelados do Luidy") 

print("-------------------Cardápio-------------------") 

print("Tamanho | Cupuaçu (CP) | Açaí (AC)") 

print("   P    | R$  9.00      | R$ 11.00") 

print("   M    | R$ 14.00      | R$ 16.00") 

print("   G    | R$ 18.00      | R$ 20.00") 

print("---------------------------------------------") 

def calcular_valor(sabor, tamanho): 

    if sabor == "CP": 

        if tamanho == "P": 

            return 9.00 

        elif tamanho == "M": 

            return 14.00 

        elif tamanho == "G": 

            return 18.00 

    elif sabor == "AC": 

        if tamanho == "P": 

            return 11.00 

        elif tamanho == "M": 

            return 16.00 

        elif tamanho == "G": 

            return 20.00 

total = 0   

while True: 

    while True: 

        sabor = input("Entre com o sabor desejado (CP/AC): ").upper() 

        if sabor != "CP" and sabor != "AC": 

            print("Sabor inválido. Tente novamente.") 

        else: 

            break 

    while True: 

        tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper() 

        if tamanho != "P" and tamanho != "M" and tamanho != "G": 

            print("Tamanho inválido. Tente novamente.") 

        else: 

            break 

    valor = calcular_valor(sabor, tamanho)    

    if sabor == "CP": 

        print(f'Você pediu um Cupuaçu no tamanho {tamanho}: R$ {valor:.2f}') 

    elif sabor == "AC": 

        print(f'Você pediu um Açaí no tamanho {tamanho}: R$ {valor:.2f}') 

    total += valor  # Soma ao total 

    mais = input('Deseja mais alguma coisa? (S/N): ').upper() 

    if mais != "S": 

        break 

print(f'\nO valor total a ser pago: R$ {total:.2f}') 

print('Obrigado por comprar na Loja de Gelados do Luidy! Volte sempre!')