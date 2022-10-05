def validar_cliente(nome, cpf, cidade):
    dados_cliente ={'cliente1':{'nome':'Rafael Souza', 'cpf':'12345678901', 'cidade':'SAO PAULO'},
                    'cliente2':{'nome':'Renata Souza', 'cpf':'10987654321', 'cidade':'NOVA EUROPA'}}
    cliente_valido = False

    for chave, valor in dados_cliente.items():
        if ((nome == dados_cliente[chave]['nome']) and (cpf  == dados_cliente[chave]['cpf'])  and (cidade.upper() == dados_cliente[chave]['cidade'])):
            cliente_valido = True

    return cliente_valido

def valor_permitido(valor_financ, quant_parcelas, cliente_valido = False):
    if cliente_valido:

        if (valor_financ > 1000 and valor_financ <= 5000):

            if (valor_financ > 999.99 and valor_financ <= 2000) and (quant_parcelas > 1 and quant_parcelas < 5):
                return f'Financiamento de {valor_financ} concedido em {quant_parcelas} parcelas'

            elif (valor_financ > 2000 and valor_financ <= 4000) and (quant_parcelas > 1 and quant_parcelas < 8):
                return f'Financiamento de {valor_financ} concedido em {quant_parcelas} parcelas'
            
            elif (valor_financ > 4000 and valor_financ <= 5000) and (quant_parcelas > 1 and quant_parcelas < 10):
                return f'Financiamento de {valor_financ} concedido em {quant_parcelas} parcelas'

            else:
                return f'Quantidade de parcelas solicitada não atende os requisitos do Financiamento'
    
        else:
            return f'Valor solicitado não permitido para financiamentos'

    else:
        return f'Cliente não validado'
        
