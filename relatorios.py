def relatorio_do_dia(maquinas, partidas, hoje):
    partidas_de_hoje = [partida for partida in partidas if partida["data"] == hoje]
    ligadas = sum(1 for maquina in maquinas if maquina["ligada"])
    print(f"\nRelatório de {hoje.strftime('%d/%m/%Y')}")
    print(f"Máquinas cadastradas: {len(maquinas)}")
    print(f"Máquinas ligadas: {ligadas}")
    print(f"Partidas registradas hoje: {len(partidas_de_hoje)}")
    if partidas_de_hoje:
        pontuacao_total = sum(partida["pontuacao"] for partida in partidas_de_hoje)
        print(f"Pontuação somada: {pontuacao_total}")
