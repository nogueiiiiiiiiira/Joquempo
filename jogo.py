# importa as bibliotecas
import random  # responsável por escolher aleatoriamente uma opção
import time  # responsável por 'dar um tempo' para o usuário ler os valores imprimidos
import os  # responsável por limpar o console

# escolhe o modo de jogo
print("Digite (1) - Jogar humano contra humano")
print("Digite (2) - Jogar humano contra computador")
print("Digite (3) - Jogar computador contra computador")
escolher_modo = input("")

# limpa o console
os.system("cls")

# direciona o código para certo caminho se o modo for 1
if escolher_modo == "1":
    # certifica-se que o modo escolhido foi o correto
    print("Modo escolhido: humano x humano. Caso deseje continuar, digite (1)")
    print("Caso deseje mudar o modo de jogo, digite (2) para encerrar o programa!")
    garantir_modo = input("")
    
    if garantir_modo == "1":
        # pega os nomes dos jogadores, limpando o console antes
        os.system("cls")
        primeiro_jogador = input("Digite o nome do primeiro jogador: ")
        os.system("cls")
        segundo_jogador = input("Digite o nome do segundo jogador: ")
        
        # estabelece as variáveis iniciais
        vitorias_primeiro_jogador = 0
        vitorias_segundo_jogador = 0
        empates = 0
        
        while garantir_modo == "1":
            # começa o jogo pelo primeiro_jogador, que escolhe entre as opções abaixo.
            os.system("cls")
            print("Excelente! Agora, se preparem para jogar!")
            time.sleep(3)
            os.system("cls")
            print(f"{primeiro_jogador}, escolha: (1) - Pedra, (2) - Papel, (3) - Tesoura")
            escolha_jogador_um = input("")
            time.sleep(3)
            os.system("cls")
            print(f"{segundo_jogador}, escolha: (1) - Pedra, (2) - Papel, (3) - Tesoura")
            escolha_jogador_dois = input("")
            time.sleep(3)
            os.system("cls")
            
            # estabelece as lógicas entre cada opção e atualiza os status de vitórias
            if escolha_jogador_um == "1" and escolha_jogador_dois == "3":
                vitorias_primeiro_jogador += 1
                print(f"Vitória de {primeiro_jogador}! Ele(a) escolheu Pedra! {segundo_jogador} escolheu Tesoura!")
            elif escolha_jogador_um == "2" and escolha_jogador_dois == "1":
                vitorias_primeiro_jogador += 1
                print(f"Vitória de {primeiro_jogador}! Ele(a) escolheu Papel! {segundo_jogador} escolheu Pedra!")
            elif escolha_jogador_um == "3" and escolha_jogador_dois == "2":
                vitorias_primeiro_jogador += 1
                print(f"Vitória de {primeiro_jogador}! Ele(a) escolheu Tesoura! {segundo_jogador} escolheu Papel!")
            elif escolha_jogador_dois == "1" and escolha_jogador_um == "3":
                vitorias_segundo_jogador += 1
                print(f"Vitória de {segundo_jogador}! Ele(a) escolheu Pedra! {primeiro_jogador} escolheu Tesoura!")
            elif escolha_jogador_dois == "2" and escolha_jogador_um == "1":
                vitorias_segundo_jogador += 1
                print(f"Vitória de {segundo_jogador}! Ele(a) escolheu Papel! {primeiro_jogador} escolheu Pedra!")
            elif escolha_jogador_dois == "3" and escolha_jogador_um == "2":
                vitorias_segundo_jogador += 1
                print(f"Vitória de {segundo_jogador}! Ele(a) escolheu Tesoura! {primeiro_jogador} escolheu Papel!")
            else:
                print("Empate! Ambos escolheram a mesma opção!")
                empates += 1
            
            time.sleep(3)
            # mostra o placar geral após cada partida
            os.system("cls")
            print("--- PLACAR GERAL ---")
            print(f"\nVitórias de {primeiro_jogador}: {vitorias_primeiro_jogador}")
            print(f"Vitórias de {segundo_jogador}: {vitorias_segundo_jogador}")
            print("\n--------------------")
            time.sleep(3)
            
            # pergunta se os jogadores desejam continuar a jogar
            os.system("cls")
            print("A partida terminou. Deseja continuar? Digite (1 ) - Sim, (2) - Não")
            terminar_jogo = input("")
            # se sim, o loop continua
            if terminar_jogo == "1":
                garantir_modo = "1"
            # se não, o loop para e os valores são imprimidos
            else:
                garantir_modo = "2"
                time.sleep(3)
                os.system("cls")
                print("--- RESULTADO FINAL ---")
                print(f"\nEmpates: {empates}")
                print(f"Vitórias de {primeiro_jogador}: {vitorias_primeiro_jogador}")
                print(f"Vitórias de {segundo_jogador}: {vitorias_segundo_jogador}")
                print("\n-----------------------")
                print(f"\nObrigado por jogarem, {primeiro_jogador} e {segundo_jogador}!")
    elif garantir_modo == "2":
        os.system("cls")
        print("Programa encerrado!")
    else:
        os.system("cls")
        print("Programa encerrado! Digite algo válido da próxima vez!")
elif escolher_modo == "2":
    # certifica-se que o modo escolhido foi o correto
    os.system("cls")
    print("Modo escolhido: humano x computador. Caso deseje continuar, digite (1)")
    print("Caso deseje mudar o modo de jogo, digite (2) para encerrar o programa!")
    garantir_modo = input("")
    
    if garantir_modo == "1":
        os.system("cls")
        # pega o nome do jogador
        nome_jogador = input("Digite o seu nome: ")
        # estabelece as variáveis iniciais
        vitorias_jogador = 0
        vitorias_computador = 0
        empates = 0
        
        while garantir_modo == "1":
            # começa o jogo pelo jogador, que escolhe entre as opções abaixo. Depois, vai para o computador
            os.system("cls")
            print("Excelente! Agora, se prepare para jogar!")
            time.sleep(3)
            os.system("cls")
            print(f"{nome_jogador} escolha: (1) - Pedra, (2) - Papel, (3) - Tesoura")
            escolha_jogador = input("")
            time.sleep(3)
            os.system("cls")
            print("Agora, o computador vai escolher: (1) - Pedra, (2) - Papel, (3) - Tesoura")
            time.sleep(3)
            # opções: 1 - Pedra, 2 - Papel, 3 - Tesoura
            opcoes = ["1", "2", "3"]
            # escolhe aleatoriamente, caso for computador, as opções acima
            opcao_aleatoria = random.choice(opcoes)
            os.system("cls")
            # estabelece as lógicas entre cada opção e atualiza os status de vitórias
            if escolha_jogador == "1" and opcao_aleatoria == "3":
                vitorias_jogador += 1
                print(f"Vitória de {nome_jogador}! Ele(a) escolheu Pedra. O computador escolheu Tesoura!")
            elif escolha_jogador == "2" and opcao_aleatoria == "1":
                vitorias_jogador += 1
                print(f"Vitória de {nome_jogador}! Ele(a) escolheu Papel. O computador escolheu Pedra!")
            elif escolha_jogador == "3" and opcao_aleatoria == "2":
                vitorias_jogador += 1
                print(f"Vitória de {nome_jogador}! Ele(a) escolheu Tesoura. O computador escolheu Papel!")
            elif opcao_aleatoria == "1" and escolha_jogador == "3":
                vitorias_computador += 1
                print(f"Vitória do computador! Ele escolheu Pedra. {nome_jogador} escolheu Tesoura!")
            elif opcao_aleatoria == "2" and escolha_jogador == "1":
                vitorias_computador += 1
                print(f"Vitória do computador! Ele escolheu Papel. {nome_jogador} escolheu Pedra!")
            elif opcao_aleatoria == "3" and escolha_jogador == "2":
                vitorias_computador += 1
                print(f"Vitória do computador! Ele escolheu Tesoura. {nome_jogador} escolheu Papel!")
            elif opcao_aleatoria == escolha_jogador:
                if opcao_aleatoria == "1":
                    opcao_aleatoria = "Pedra"
                elif opcao_aleatoria == "2":
                    opcao_aleatoria = "Papel"
                else:
                    opcao_aleatoria = "Tesoura"
                print(f"Empate! Ambos escolheram {opcao_aleatoria}!")
                empates += 1
            
            # mostra o placar geral após cada partida
            time.sleep(3)
            os.system("cls")
            print("--- PLACAR GERAL ---")
            print(f"\nVitórias de {nome_jogador}: {vitorias_jogador}")
            print(f"Vitórias do computador: {vitorias_computador}")
            print("\n--------------------")
            
            # pergunta se o jogador deseja continuar a jogar
            time.sleep(3)
            os.system("cls")
            print("A partida terminou. Deseja continuar? Digite (1) - Sim, (2) - Não")
            terminar_jogo = input("")
            # se sim, o loop continua
            if terminar_jogo == "1":
                garantir_modo = "1"
            else:
                garantir_modo = "2"
                time.sleep(3)
                os.system("cls")
                print("--- RESULTADO FINAL ---")
                print(f"\nEmpates: {empates}")
                print(f"Vitórias de {nome_jogador}: {vitorias_jogador}")
                print(f"Vitórias do computador: {vitorias_computador}")
                print("\n-----------------------")
                print(f"\nObrigado por jogar, {nome_jogador}!")
    elif garantir_modo == "2":
        os.system("cls")
        print("Programa encerrado!")
    else:
        os.system("cls")
        print("Programa encerrado! Digite algo válido da próxima vez!")
elif escolher_modo == "3":
    # certifica-se que o modo escolhido foi o correto
    os.system("cls")
    print("Modo escolhido: computador x computador. Caso deseje continuar, digite (1).")
    print("Caso deseje mudar o modo de jogo, digite (2)")
    garantir_modo = input("")
    
    if garantir_modo == "1":
        # estabelece as variáveis iniciais
        vitorias_computador_um = 0
        vitorias_computador_dois = 0
        empates = 0
        
        while garantir_modo == "1":
            # começa o jogo pelo computadorUm, que escolhe entre as opções abaixo.
            # depois, vai para o computadorDois
            os.system("cls")
            print("Excelente! Agora, se prepare para assistir!")
            time.sleep(3)
            os.system("cls")
            print("O COMPUTADOR UM irá escolher entre: (1) - Pedra, (2) - Papel, (3) - Tesoura")
            # opções: 1 - Pedra, 2 - Papel, 3 - Tesoura
            opcoes = ["1", "2", "3"]
            opcao_aleatoria_computador_um = random.choice(opcoes)
            time.sleep(3)
            if opcao_aleatoria_computador_um == "1":
                opcao_escolhida_um = "Pedra"
            elif opcao_aleatoria_computador_um == "2":
                opcao_escolhida_um = "Papel"
            else:
                opcao_escolhida_um = "Tesoura"
            os.system("cls")
            print(f"O COMPUTADOR UM escolheu: {opcao_escolhida_um}")
            time.sleep(3)
            os.system("cls")
            print("Agora, o COMPUTADOR DOIS vai escolher: (1) - Pedra, (2) - Papel, (3) - Tesoura")
            opcao_aleatoria_computador_dois = random.choice(opcoes)
            time.sleep(3)
            if opcao_aleatoria_computador_dois == "1":
                opcao_escolhida_dois = "Pedra"
            elif opcao_aleatoria_computador_dois == "2":
                opcao_escolhida_dois = "Papel"
            else:
                opcao_escolhida_dois = "Tesoura"
            os.system("cls")
            print(f"O COMPUTADOR DOIS escolheu: {opcao_escolhida_dois}")
            time.sleep(3)
            os.system("cls")
            # estabelece as lógicas entre cada opção e atualiza os status de vitórias
            if opcao_aleatoria_computador_um == "1" and opcao_aleatoria_computador_dois == "3":
                vitorias_computador_um += 1
                print("Vitória do COMPUTADOR UM! Ele escolheu Pedra. O COMPUTADOR DOIS escolheu Tesoura!")
            elif opcao_aleatoria_computador_um == "2" and opcao_aleatoria_computador_dois == "1":
                vitorias_computador_um += 1
                print("Vitória do COMPUTADOR UM! Ele escolheu Papel. O COMPUTADOR DOIS escolheu Pedra!")
            elif opcao_aleatoria_computador_um == "3" and opcao_aleatoria_computador_dois == "2":
                vitorias_computador_um += 1
                print(" Vitória do COMPUTADOR UM! Ele escolheu Tesoura. O COMPUTADOR DOIS escolheu Papel!")
            elif opcao_aleatoria_computador_dois == "1" and opcao_aleatoria_computador_um == "3":
                vitorias_computador_dois += 1
                print("Vitória do COMPUTADOR DOIS! Ele escolheu Pedra! O COMPUTADOR UM escolheu Tesoura!")
            elif opcao_aleatoria_computador_dois == "2" and opcao_aleatoria_computador_um == "1":
                vitorias_computador_dois += 1
                print("Vitória do COMPUTADOR DOIS! Ele escolheu Papel! O COMPUTADOR UM escolheu Pedra!")
            elif opcao_aleatoria_computador_dois == "3" and opcao_aleatoria_computador_um == "2":
                vitorias_computador_dois += 1
                print("Vitória do COMPUTADOR DOIS! Ele escolheu Tesoura! O COMPUTADOR UM escolheu Papel!")
            elif opcao_aleatoria_computador_dois == opcao_aleatoria_computador_um:
                print("Empate! Ambos os computadores escolheram a mesma jogada!")
                empates += 1
            
            time.sleep(3)
            # mostra o placar geral após cada partida
            os.system("cls")
            print("--- PLACAR GERAL ---")
            print(f"\nVitórias do COMPUTADOR UM: {vitorias_computador_um}")
            print(f"Vitórias do COMPUTADOR DOIS: {vitorias_computador_dois}")
            print("\n--------------------")
            time.sleep(3)
            # pergunta se o jogador deseja continuar a assistir
            os.system("cls")
            print("A partida terminou. Deseja continuar a assistir? Digite (1) - Sim, (2) - Não")
            terminar_jogo = input("")
            # se sim, o loop continua
            if terminar_jogo == "1":
                garantir_modo = "1"
            # se não, o loop para e os valores finais são imprimidos
            else:
                garantir_modo = "2"
                time.sleep(3)
                os.system("cls")
                print("--- RESULTADO FINAL ---")
                print(f"\nEmpates: {empates}")
                print(f"Vitórias do COMPUTADOR UM: {vitorias_computador_um}")
                print(f"Vitórias do COMPUTADOR DOIS: {vitorias_computador_dois}")
                print("\n-----------------------")
                print("\nObrigado por assistir os computadores jogarem!")
                
    elif garantir_modo == "2":
        os.system("cls")
        print("Programa encerrado!")
    else:
        os.system("cls")
        print("Programa encerrado! Digite algo válido da próxima vez!")
else:
    os.system("cls")
    print("Programa encerrado! Digite uma das opções acima quando inicializar novamente o programa!")
