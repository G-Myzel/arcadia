from datetime import date


def registrar(partidas, maquinas):
    nome_jogador = input("Nome do jogador: ").strip()
    jogo = input("Nome do jogo: ").strip()
    if not nome_jogador or not jogo:
        print("Informe o nome do jogador e do jogo.")
        return

    elegiveis = [
        (indice, maquina)
        for indice, maquina in enumerate(maquinas, start=1)
        if maquina["ligada"] and maquina["jogo"].casefold() == jogo.casefold()
    ]
    if maquinas and not elegiveis:
        print("Não há máquina ligada com esse jogo.")
        return

    if elegiveis:
        print("Máquinas disponíveis:")
        for indice, maquina in elegiveis:
            print(f"{indice}. {maquina['nome']}")
        escolha = input("Número da máquina: ").strip()
        try:
            maquina_indice = int(escolha)
        except ValueError:
            print("Digite um número válido.")
            return
        if not any(indice == maquina_indice for indice, _ in elegiveis):
            print("Máquina não encontrada.")
            return
        maquina = maquinas[maquina_indice - 1]["nome"]
    else:
        maquina = "Não informada"

    entrada = input("Pontuação: ").strip()
    try:
        pontuacao = int(entrada)
    except ValueError:
        print("A pontuação deve ser um número inteiro.")
        return
    if pontuacao < 0:
        print("A pontuação não pode ser negativa.")
        return

    partidas.append({
        "jogador": nome_jogador,
        "jogo": jogo,
        "maquina": maquina,
        "pontuacao": pontuacao,
        "data": date.today(),
    })
    print("Partida registrada.")


def mostrar_ranking(partidas, jogo):
    if not jogo:
        print("Informe o nome do jogo.")
        return
    ranking = [
        partida for partida in partidas
        if partida["jogo"].casefold() == jogo.casefold()
    ]
    if not ranking:
        print("Ainda não há partidas para esse jogo.")
        return
    ranking.sort(key=lambda partida: (-partida["pontuacao"], partida["jogador"].casefold()))
    print(f"Ranking de {jogo}:")
    for posicao, partida in enumerate(ranking, start=1):
        print(f"{posicao}. {partida['jogador']} — {partida['pontuacao']} pontos")
