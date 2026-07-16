def menu():
    print("""
╔══════════════════════════════════════════╗
║          ARCADIA — Fliperama             ║
╠══════════════════════════════════════════╣
║  1 - Cadastrar máquina                   ║
║  2 - Listar máquinas                     ║
║  3 - Ligar / desligar máquina            ║
║  4 - Registrar partida                   ║
║  5 - Ver ranking de um jogo              ║
║  6 - Relatório do dia                    ║
║  7 - Sair                                ║
╚══════════════════════════════════════════╝
""")

def user_choice():
    return input("Escolha uma opção: ")

def input_validation(user_selection):
    try:
        user_selection_processed = int(user_selection)
        executes_user_choice(user_selection_processed)
    except:
        message('Seleção Invalida! Tente novamente')

def message(msg):
    print(msg)


def executes_user_choice(user_selection_processed):
    match user_selection_processed:
        case 1:
            message(f"Você escolheu a opção {user_selection_processed}")
        case 2:
            message(f"Você escolheu a opção {user_selection_processed}")
        case 3:
            message(f"Você escolheu a opção {user_selection_processed}")
        case 4: 
            message(f"Você escolheu a opção {user_selection_processed}")
        case 5: 
            message(f"Você escolheu a opção {user_selection_processed}")
        case 5:
            message(f"Você escolheu a opção {user_selection_processed}")
        case 6: 
            message(f"Você escolheu a opção {user_selection_processed}")
        case 7:
            message(f"Você escolheu a opção {user_selection_processed}")

