lista_contas = {}
n_contas = 0

LIMITE_SAQUES = 3
LIMITE_POR_SAQUE = 500


def criar_conta():
    global n_contas

    n_contas += 1
    return n_contas


def criar_usuario():
    nome_usuario = input("Digite o nome do usuário: ").strip()

    if not nome_usuario:
        print("Nome de usuário inválido.")
        return

    if nome_usuario in lista_contas:
        print("Já existe um usuário com esse nome.")
        return

    numero_conta = criar_conta()

    lista_contas[nome_usuario] = {
        "numero_conta": numero_conta,
        "saldo": 0,
        "depositos": [],
        "saques": [],
        "transferencias": [],
        "quantidade_saques": 0
    }

    print(
        f"Usuário {nome_usuario} criado com sucesso. "
        f"Conta número: {numero_conta}"
    )


def listar_contas():
    if not lista_contas:
        print("\nNenhuma conta cadastrada.")
        return

    print("\n========== CONTAS ==========")

    for usuario, dados in lista_contas.items():
        print(f"Usuário: {usuario}")
        print(f"Conta: {dados['numero_conta']}")
        print(f"Saldo: R$ {dados['saldo']:.2f}")
        print("----------------------------")

    print("============================")


def buscar_usuario():
    nome_usuario = input("Digite o nome do usuário: ").strip()

    if nome_usuario not in lista_contas:
        print("Usuário não encontrado.")
        return None

    return nome_usuario


def saque(usuario, valor):
    conta = lista_contas[usuario]

    if valor <= 0:
        return "Valor de saque inválido."

    if conta["quantidade_saques"] >= LIMITE_SAQUES:
        return "Limite de saques diários atingido."

    if valor > LIMITE_POR_SAQUE:
        return "Não é possível sacar valores acima de R$ 500,00."

    if valor > conta["saldo"]:
        return "Saldo insuficiente para realizar o saque."

    conta["saldo"] -= valor
    conta["saques"].append(valor)
    conta["quantidade_saques"] += 1

    return (
        f"Saque realizado com sucesso. "
        f"Saldo atual: R$ {conta['saldo']:.2f}"
    )


def deposito(usuario, valor):
    conta = lista_contas[usuario]

    if valor <= 0:
        return "Valor de depósito inválido. O valor deve ser positivo."

    conta["saldo"] += valor
    conta["depositos"].append(valor)

    return (
        f"Depósito realizado com sucesso. "
        f"Saldo atual: R$ {conta['saldo']:.2f}"
    )


def extrato(usuario):
    conta = lista_contas[usuario]

    texto_extrato = "\n========== EXTRATO ==========\n"
    texto_extrato += f"Usuário: {usuario}\n"
    texto_extrato += f"Conta: {conta['numero_conta']}\n"

    if (
        not conta["depositos"]
        and not conta["saques"]
        and not conta["transferencias"]
    ):
        texto_extrato += "\nNão foram realizadas movimentações.\n"

    else:
        texto_extrato += "\nDepósitos:\n"

        if conta["depositos"]:
            for valor in conta["depositos"]:
                texto_extrato += f"+ R$ {valor:.2f}\n"
        else:
            texto_extrato += "Nenhum depósito realizado.\n"

        texto_extrato += "\nSaques:\n"

        if conta["saques"]:
            for valor in conta["saques"]:
                texto_extrato += f"- R$ {valor:.2f}\n"
        else:
            texto_extrato += "Nenhum saque realizado.\n"

        texto_extrato += "\nTransferências:\n"

        if conta["transferencias"]:
            for transferencia in conta["transferencias"]:
                tipo = transferencia["tipo"]
                valor = transferencia["valor"]
                outro_usuario = transferencia["usuario"]

                if tipo == "enviada":
                    texto_extrato += (
                        f"- R$ {valor:.2f} para {outro_usuario}\n"
                    )
                else:
                    texto_extrato += (
                        f"+ R$ {valor:.2f} de {outro_usuario}\n"
                    )

        else:
            texto_extrato += "Nenhuma transferência realizada.\n"

    texto_extrato += f"\nSaldo atual: R$ {conta['saldo']:.2f}"
    texto_extrato += "\n============================="

    return texto_extrato


def transferir(usuario_origem, valor, usuario_destino):
    conta_origem = lista_contas[usuario_origem]

    if valor <= 0:
        return "Valor de transferência inválido."

    if usuario_destino not in lista_contas:
        return "Conta de destino não encontrada."

    if usuario_destino == usuario_origem:
        return "Não é possível transferir para a própria conta."

    if valor > conta_origem["saldo"]:
        return "Saldo insuficiente para realizar a transferência."

    conta_destino = lista_contas[usuario_destino]

    conta_origem["saldo"] -= valor
    conta_destino["saldo"] += valor

    conta_origem["transferencias"].append(
        {
            "tipo": "enviada",
            "usuario": usuario_destino,
            "valor": valor
        }
    )

    conta_destino["transferencias"].append(
        {
            "tipo": "recebida",
            "usuario": usuario_origem,
            "valor": valor
        }
    )

    return (
        f"Transferência de R$ {valor:.2f} para "
        f"{usuario_destino} realizada com sucesso.\n"
        f"Saldo atual: R$ {conta_origem['saldo']:.2f}"
    )


while True:
    print("\n========== SISTEMA BANCÁRIO ==========")
    print("1. Criar usuário e conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Extrato")
    print("5. Listar contas")
    print("6. Transferir")
    print("7. Sair")
    print("======================================")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        criar_usuario()

    elif opcao == "2":
        usuario = buscar_usuario()

        if usuario:
            try:
                valor = float(
                    input("Digite o valor do depósito: R$ ")
                )

                print(deposito(usuario, valor))

            except ValueError:
                print("Digite um valor numérico válido.")

    elif opcao == "3":
        usuario = buscar_usuario()

        if usuario:
            try:
                valor = float(
                    input("Digite o valor do saque: R$ ")
                )

                print(saque(usuario, valor))

            except ValueError:
                print("Digite um valor numérico válido.")

    elif opcao == "4":
        usuario = buscar_usuario()

        if usuario:
            print(extrato(usuario))

    elif opcao == "5":
        listar_contas()

    elif opcao == "6":
        usuario_origem = buscar_usuario()

        if usuario_origem:
            usuario_destino = input(
                "Digite o nome do usuário da conta de destino: "
            ).strip()

            try:
                valor = float(
                    input("Digite o valor da transferência: R$ ")
                )

                print(
                    transferir(
                        usuario_origem,
                        valor,
                        usuario_destino
                    )
                )

            except ValueError:
                print("Digite um valor numérico válido.")

    elif opcao == "7":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")