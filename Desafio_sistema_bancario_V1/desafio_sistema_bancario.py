user_balance = 0
DAILY_AMOUNT_LIMIT = 500
daily_withdraw_limit = 3
operation_account = -1
statement = '----------------- EXTRATO -----------------\n'

def withdraw_cash(cash_for_out: float, user_balance):
    global statement
    if user_balance != 0:
        if daily_withdraw_limit == 0:
            print("Limite diário excedido para saque.")
            return -1
        elif(cash_for_out > DAILY_AMOUNT_LIMIT):
            print("O Valor informado é maior que o limite diário")
        elif cash_for_out <= user_balance:
            user_balance -= cash_for_out
            statement += f'Tipo de operação: Saque\nValor retirado: R$ {cash_for_out:.2f}\nSaldo Atual: R$ {user_balance:.2f}\n-------------------------------------------n'
            daily_withdraw_limit -= 1 
            return user_balance
    print("Saldo insuficiente para saque.")
    return -1

def cash_deposit(cash_for_deposit, user_balance):
    global statement
    user_balance += cash_for_deposit
    statement += f'Tipo de operação: Depósito\nValor depositado: R$ {cash_for_deposit:.2f}\nSaldo Atual: R$ {user_balance:.2f}\n-------------------------------------------n'
    return user_balance

def bank_statement(statement):
    print(f"\n{statement}")



while operation_account != 3:
    operation_account = input(
    """
---------Menu---------
[0] Depósito
[1] Saque
[2] Extrato
[3] Encerrar operação
Selecione sua opção: """
    )

    if not operation_account.isdigit():
        print('Digite um número correspondente à opção.')
        continue

    operation_account = int(operation_account)

    if operation_account == 0:
        control_deposit = 0
        while control_deposit != 1:
            cash_for_deposit = input("\nDigite o valor do depósito (R$): ")
            if cash_for_deposit.replace('.', '').isdigit():
                cash_for_deposit = float(cash_for_deposit)
                user_balance = cash_deposit(cash_for_deposit, user_balance)
                control_deposit = 1
            else:
                print("Digite um valor válido.")
    elif operation_account == 1:
        control_cashout = 0
        while control_cashout != 1:
            cash_for_out = input("\nDigite o valor do saque (R$): ")
            if cash_for_out.replace('.', '').isdigit():
                cash_for_out = float(cash_for_out)
                user_balance = withdraw_cash(cash_for_out, user_balance)
                control_cashout = 1
            else:
                print("Digite um valor válido.")
    elif operation_account == 2:
        bank_statement(statement)
    elif operation_account == 3:
        daily_withdraw_limit = 3
        print('Encerrando operação')
