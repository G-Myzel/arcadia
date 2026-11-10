from datetime import date

import maquinas
import partidas
import relatorios
import util


def main():
    lista_maquinas = []
    lista_partidas = []

    while True:
        util.menu()
        opcao = util.user_choice()

        if opcao == "1":
            maquinas.cadastrar(lista_maquinas)
        elif opcao == "2":
            maquinas.listar(lista_maquinas)
        elif opcao == "3":
            maquinas.alternar_status(lista_maquinas)
        elif opcao == "4":
            partidas.registrar(lista_partidas, lista_maquinas)
        elif opcao == "5":
            jogo = input("Nome do jogo: ").strip()
            partidas.mostrar_ranking(lista_partidas, jogo)
        elif opcao == "6":
            relatorios.relatorio_do_dia(lista_maquinas, lista_partidas, date.today())
        elif opcao == "7":
            print("Até logo!")
            break
        else:
            print("Escolha uma opção de 1 a 7.")


if __name__ == "__main__":
    main()
