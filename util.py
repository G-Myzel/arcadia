def menu():
    print("""
ARCADIA — Fliperama

1. Cadastrar máquina
2. Listar máquinas
3. Ligar ou desligar máquina
4. Registrar partida
5. Ver ranking de um jogo
6. Relatório do dia
7. Sair
""")


def user_choice():
    return input("Escolha uma opção: ").strip()
