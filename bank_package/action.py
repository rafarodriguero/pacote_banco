def sacar (valor, saldo):
    if valor <= saldo:
        saldo -= valor
        return f'Saque Realizado, novo saldo: {saldo}'
    else:
        return 'Saque NÃO Permitido'

def depositar (valor, saldo):
    if valor > 0:
        saldo += valor
        return f'Deposito Realizado, novo saldo: {saldo}'
    else:
        return 'Deposito NÃO Permitido'

def exibir_saldo(saldo):
    return f'Seu Saldo Atual: {saldo}'
