user_balance = 0
DAILY_AMOUNT_LIMIT = 500
daily_withdraw_limit = 3
operation_account = -1
users_bank = []
all_current_accounts = []
cont_number_account = 1
statement = '----------------- EXTRATO -----------------\n'

def withdraw_cash(cash_for_out: float, user_balance):
    global statement, daily_withdraw_limit
    if user_balance != 0:
        if daily_withdraw_limit == 0:
            print("Limite diário excedido para saque.")
            return user_balance
        elif cash_for_out > DAILY_AMOUNT_LIMIT:
            print("O Valor informado é maior que o limite diário")
        elif cash_for_out <= user_balance:
            user_balance -= cash_for_out
            statement += f'Tipo de operação: Saque\nValor retirado: R$ {cash_for_out:.2f}\nSaldo Atual: R$ {user_balance:.2f}\n-------------------------------------------\n'
            daily_withdraw_limit -= 1
            return user_balance
    print("Saldo insuficiente para saque.")
    return user_balance

def cash_deposit(cash_for_deposit, user_balance):
    global statement
    user_balance += cash_for_deposit
    statement += f'Tipo de operação: Depósito\nValor depositado: R$ {cash_for_deposit:.2f}\nSaldo Atual: R$ {user_balance:.2f}\n-------------------------------------------\n'
    return user_balance

def bank_statement(statement):
    print(f"\n{statement}")

def create_user_account(users_bank, name, birth_date, cpf, address):
    user = {
        "name": name,
        "birth_date": birth_date,
        "cpf": cpf,
        "address": address,
        "number_current_accounts": []
    }
    users_bank.append(user)
    print("Usuário criado com sucesso!")
    return user
def is_valid_cpf_length(cpf):
    return len(cpf) == 11 and cpf.isdigit()

def user_account_inputs():
    address_label = ["Logradouro", "Bairro", "Cidade", "Estado[Ex: BA]"]
    address_infos = []
    birth_day_label = ["Dia", "Mês", "Ano"]
    birth_day_infos = []

    name = input("Digite o nome: ")
    while True:
        cpf = input("Digite seu CPF: ")
        is_valid_cpf= is_valid_cpf_length(cpf)
        if (is_valid_cpf):
            break
        print("CPF inválido")
    
    for info in address_label:
        question_address = input(f'Digite o {info}: ')
        address_infos.append(question_address)
    address = f'{address_infos[0]} - {address_infos[1]} - {address_infos[2]} - {address_infos[3]}'
    for info in birth_day_label:
        question_birth_day = input(f'Digite o {info}: ')
        birth_day_infos.append(question_birth_day)
    birth_date = f'{birth_day_infos[0]}/{birth_day_infos[1]}/{birth_day_infos[2]}'
    
    create_user_account(users_bank, name, birth_date, cpf, address)
    
def create_current_account(cpf: str, users_bank, all_current_accounts):
    global cont_number_account
    current_account = {
        "agency_number": '0001',
        "number_account_user": cont_number_account,
        "user": cpf
    }
    for user in users_bank:
        if user["cpf"] == cpf:
            user["number_current_accounts"].append(current_account["number_account_user"])
            all_current_accounts.append(current_account)
            print("Conta corrente criada com sucesso!")
            
            return True
    print("Usuário não encontrado")
    return False

def list_users():
    if users_bank:
        for user in users_bank:
            print(f"Nome: {user['name']}\nData de Nascimento: {user['birth_date']}\nEndereço: {user['address']}\nCPF: {user['cpf']}")
            print('-' * 20)
    else:
        print("Não existem usuários cadastrados")

def list_user_accounts(cpf):
    print()
    user_accounts = [account for account in all_current_accounts if account["user"] == cpf]
    if user_accounts:
        for account in user_accounts:
            print(f"Agência: {account['agency_number']}\nNúmero da Conta: {account['number_account_user']}\nCPF do Usuário: {account['user']}")
            print('-' * 20)
    else:
        print("Nenhuma conta encontrada para o CPF fornecido")

def list_users_with_cpf():
    if users_bank:
        for user in users_bank:
            print(f"Nome: {user['name']} - CPF: {user['cpf']}")
    print()

while True: 
    operation = input(
        """
---------Menu---------
[0] Criar Conta
[1] Criar Usuário
[2] Operações
[3] Listar Usuários
[4] Listar Contas de um Usuário
[5] Sair
Selecione sua opção: """
    )

    if not operation.isdigit():
        print("Digite um número correspondente à opção.")
        continue

    operation = int(operation)
    if operation == 0:
        list_users_with_cpf
        cpf = input("Informe seu CPF: ")
        create_current_account(cpf, users_bank, all_current_accounts, cont_number_account)
    elif operation == 1:
        user_account_inputs()
    elif operation == 2:
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
                break
    elif operation == 3:
        list_users()
    elif operation == 4:
        cpf = input("Informe o CPF do usuário: ")
        list_user_accounts(cpf)
    elif operation == 5:
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")
