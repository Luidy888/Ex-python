def escolha_servico(): 

    while True: 

        print('Entre com o tipo de serviço desejado') 

        print('DIG - Digitalização') 

        print('ICO - Impressão Colorida') 

        print('IPB - Impressão Preto e Branco') 

        print('FOT - Fotocópia') 

        servico = input('>>').upper() 

 

        if servico in ['DIG', 'ICO', 'IPB', 'FOT']: 

            return servico 

        else: 

            print('Escolha inválida, entre com o tipo de serviço novamente') 

 

def num_pagina(): 

    while True: 

        try: 

            paginas = int(input('Entre com o número de páginas: ')) 

            if paginas > 20000: 

                print('Não aceitamos tantas páginas de uma vez...') 

                print('Por favor, entre com um número de páginas novamente') 

                continue 

 

            if paginas < 20: 

                desconto = 0 

            elif 20 <= paginas < 200: 

                desconto = 0.15 

            elif 200 <= paginas < 2000: 

                desconto = 0.20 

            elif 2000 <= paginas <= 20000: 

                desconto = 0.25 

 

            return paginas, desconto 

        except ValueError: 

            print('Número inválido. Por favor, entre com um valor numérico inteiro.') 

 

def servico_extra(): 

    while True: 

        print('Deseja adicionar algum serviço?') 

        print('1 - Encadernação Simples - R$ 15.00') 

        print('2 - Encadernação Capa Dura - R$ 40.00') 

        print('0 - Não desejo mais nada') 

        try: 

            adicional = int(input('>>')) 

            if adicional in [0, 1, 2]: 

                if adicional == 1: 

                    return 15 

                elif adicional == 2: 

                    return 40 

                else: 

                    return 0 

            else: 

                print('Opção inválida, escolha 0, 1 ou 2.') 

        except ValueError: 

            print('Número inválido. Por favor, entre com um número válido.') 

 

def calcular_preco(servico, paginas, desconto, extra): 

    precos = { 

        'DIG': 1.02, 

        'ICO': 1.00, 

        'IPB': 0.40, 

        'FOT': 0.20 

    } 

    preco_base = precos[servico] 

    total_servico = preco_base * paginas 

    total_com_desconto = total_servico * (1 - desconto) 

    total_geral = total_com_desconto + extra 

    return total_geral, total_com_desconto, preco_base 

 

print('Bem vindo à Copiadora do Luidy Oliveira') 

 

servico = escolha_servico() 

paginas, desconto = num_pagina() 

extra = servico_extra() 

total, total_com_desconto, preco_unitario = calcular_preco(servico, paginas, desconto, extra) 

 

print(f'Total: R$ {total:.2f} (Serviço: {preco_unitario:.2f} * paginas: {paginas} + extra: {extra:.2f})') 