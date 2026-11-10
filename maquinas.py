def cadastrar(maquinas):
    nome = input("Nome da máquina: ").strip()
    jogo = input("Jogo disponível: ").strip()
    if not nome or not jogo:
        print("Informe o nome da máquina e o jogo.")
        return
    maquinas.append({"nome": nome, "jogo": jogo, "ligada": False})
    print(f"Máquina {nome} cadastrada.")


def listar(maquinas):
    if not maquinas:
        print("Nenhuma máquina cadastrada.")
        return
    for indice, maquina in enumerate(maquinas, start=1):
        status = "Ligada" if maquina["ligada"] else "Desligada"
        print(f"{indice}. {maquina['nome']} | {maquina['jogo']} | {status}")


def alternar_status(maquinas):
    listar(maquinas)
    if not maquinas:
        return
    escolha = input("Número da máquina para alternar (ENTER para voltar): ").strip()
    if not escolha:
        return
    try:
        indice = int(escolha) - 1
    except ValueError:
        print("Digite um número válido.")
        return
    if not 0 <= indice < len(maquinas):
        print("Máquina não encontrada.")
        return
    maquina = maquinas[indice]
    maquina["ligada"] = not maquina["ligada"]
    print(f"{maquina['nome']}: {'ligada' if maquina['ligada'] else 'desligada'}.")
