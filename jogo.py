# importa as bibliotecas
import random  # responsável por escolher aleatoriamente uma opção
import time  # responsável por 'dar um tempo' para o usuário ler os valores imprimidos
import os  # responsável por limpar o console

# escolhe o modo de jogo
print("Digite (1) - Jogar humano contra humano")
print("Digite (2) - Jogar humano contra computador")
print("Digite (3) - Jogar computador contra computador")
escolherModo = input("")

# limpa o console
os.system("cls")

# direciona o código para certo caminho se o modo for 1
if escolherModo == "1":
    # certifica-se que o modo escolhido foi o correto
    print("Modo escolhido: humano x humano. Caso deseje continuar, digite (1)")
    print("Caso deseje mudar o modo de jogo, digite (2) para encerrar o programa!")
    garantirModo = input("")
    
    if garantirModo == "1":
        # pega os nomes dos jogadores, limpando o console antes
        os.system("cls")
        primeiroJogador = input("Digite o nome do primeiro jogador: ")
        os.system("cls")
        segundoJogador = input("Digite o nome do segundo jogador: ")
        
        # estabelece as variáveis iniciais
        vitoriasPrimeiroJogador = 0
        vitoriasSegundoJogador = 0
        empates = 0
        
        while garantirModo == "1":
            # começa o jogo pelo primeiroJogador, que escolhe entre as opções abaixo.
            os.system("cls")
            print("Excelente! Agora, se preparem para jogar!")
            time.sleep(3)
            os.system("cls")
            print(f"{primeiroJogador}, escolha: (1) - Pedra, (2) - Papel, (3) - Tesoura")
            escolhaJogadorUm = input("")
            time.sleep(3)
            os.system("cls")
            print(f"{segundoJogador}, escolha: (1) - Pedra, (2) - Papel, (3) - Tesoura")
            escolhaJogadorDois = input("")
            time.sleep(3)
            os.system("cls")
            
            # estabelece as lógicas entre cada opção e atualiza os status de vitórias
            if escolhaJogadorUm == "1" and escolhaJogadorDois == "3":
                vitoriasPrimeiroJogador += 1
                print(f"Vitória de {primeiroJogador}! Ele(a) escolheu Pedra! {segundoJogador} escolheu Tesoura!")
            elif escolhaJogadorUm == "2" and escolhaJogadorDois == "1":
                vitoriasPrimeiroJogador += 1
                print(f"Vitória de {primeiroJogador}! Ele(a) escolheu Papel! {segundoJogador} escolheu Pedra!")
            elif escolhaJogadorUm == "3" and escolhaJogadorDois == "2":
                vitoriasPrimeiroJogador += 1
                print(f"Vitória de {primeiroJogador}! Ele(a) escolheu Tesoura! {segundoJogador} escolheu Papel!")
            elif escolhaJogadorDois == "1" and escolhaJogadorUm == "3":
                vitoriasSegundoJogador += 1
                print(f"Vitória de {segundoJogador}! Ele(a) escolheu Pedra! {primeiroJogador} escolheu Tesoura!")
            elif escolhaJogadorDois == "2" and escolhaJogadorUm == "1":
                vitoriasSegundoJogador += 1
                print(f"Vitória de {segundoJogador}! Ele(a) escolheu Papel! {primeiroJogador} escolheu Pedra!")
            elif escolhaJogadorDois == "3" and escolhaJogadorUm == "2":
                vitoriasSegundoJogador += 1
                print(f"Vitória de {segundoJogador}! Ele(a) escolheu Tesoura! {primeiroJogador} escolheu Papel!")
            else:
                print("Empate! Ambos escolheram a mesma opção!")
                empates += 1
            
            time.sleep(3)
            # mostra o placar geral após cada partida
            os.system("cls")
            print("--- PLACAR GERAL ---")
            print(f"\nVitórias de {primeiroJogador}: {vitoriasPrimeiroJogador}")
            print(f"Vitórias de {segundoJogador}: {vitoriasSegundoJogador}")
            print("\n--------------------")
            time.sleep(3)
            
            # pergunta se os jogadores desejam continuar a jogar
            os.system("cls")
            print("A partida terminou. Deseja continuar? Digite (1 ) - Sim, (2) - Não")
            terminarJogo = input("")
            # se sim, o loop continua
            if terminarJogo == "1":
                garantirModo = "1"
            # se não, o loop para e os valores são imprimidos
            else:
                garantirModo = "2"
                time.sleep(3)
                os.system("cls")
                print("--- RESULTADO FINAL ---")
                print(f"\nEmpates: {empates}")
                print(f"Vitórias de {primeiroJogador}: {vitoriasPrimeiroJogador}")
                print(f"Vitórias de {segundoJogador}: {vitoriasSegundoJogador}")
                print("\n-----------------------")
                print(f"\nObrigado por jogarem, {primeiroJogador} e {segundoJogador}!")
    elif garantirModo == "2":
        os.system("cls")
        print("Programa encerrado!")
    else:
        os.system("cls")
        print("Programa encerrado! Digite algo válido da próxima vez!")
elif escolherModo == "2":
    # certifica-se que o modo escolhido foi o correto
    os.system("cls")
    print("Modo escolhido: humano x computador. Caso deseje continuar, digite (1)")
    print("Caso deseje mudar o modo de jogo, digite (2) para encerrar o programa!")
    garantirModo = input("")
    
    if garantirModo == "1":
        os.system("cls")
        # pega o nome do jogador
        nomeJogador = input("Digite o seu nome: ")
        # estabelece as variáveis iniciais
        vitoriasJogador = 0
        vitoriasComputador = 0
        empates = 0
        
        while garantirModo == "1":
            # começa o jogo pelo jogador, que escolhe entre as opções abaixo. Depois, vai para o computador
            os.system("cls")
            print("Excelente! Agora, se prepare para jogar!")
            time.sleep(3)
            os.system("cls")
            print(f"{nomeJogador} escolha: (1) - Pedra, (2) - Papel, (3) - Tesoura")
            escolhaJogador = input("")
            time.sleep(3)
            os.system("cls")
            print("Agora, o computador vai escolher: (1) - Pedra, (2) - Papel, (3) - Tesoura")
            time.sleep(3)
            # opções: 1 - Pedra, 2 - Papel, 3 - Tesoura
            opcoes = ["1", "2", "3"]
            # escolhe aleatoriamente, caso for computador, as opções acima
            opcaoAleatoria = random.choice(opcoes)
            os.system("cls")
            # estabelece as lógicas entre cada opção e atualiza os status de vitórias
            if escolhaJogador == "1" and opcaoAleatoria == "3":
                vitoriasJogador += 1
                print(f"Vitória de {nomeJogador}! Ele(a) escolheu Pedra. O computador escolheu Tesoura!")
            elif escolhaJogador == "2" and opcaoAleatoria == "1":
                vitoriasJogador += 1
                print(f"Vitória de {nomeJogador}! Ele(a) escolheu Papel. O computador escolheu Pedra!")
            elif escolhaJogador == "3" and opcaoAleatoria == "2":
                vitoriasJogador += 1
                print(f"Vitória de {nomeJogador}! Ele(a) escolheu Tesoura. O computador escolheu Papel!")
            elif opcaoAleatoria == "1" and escolhaJogador == "3":
                vitoriasComputador += 1
                print(f"Vitória do computador! Ele escolheu Pedra. {nomeJogador} escolheu Tesoura!")
            elif opcaoAleatoria == "2" and escolhaJogador == "1":
                vitoriasComputador += 1
                print(f"Vitória do computador! Ele escolheu Papel. {nomeJogador} escolheu Pedra!")
            elif opcaoAleatoria == "3" and escolhaJogador == "2":
                vitoriasComputador += 1
                print(f"Vitória do computador! Ele escolheu Tesoura. {nomeJogador} escolheu Papel!")
            elif opcaoAleatoria == escolhaJogador:
                if opcaoAleatoria == "1":
                    opcaoAleatoria = "Pedra"
                elif opcaoAleatoria == "2":
                    opcaoAleatoria = "Papel"
                else:
                    opcaoAleatoria = "Tesoura"
                print(f"Empate! Ambos escolheram {opcaoAleatoria}!")
                empates += 1
            
            # mostra o placar geral após cada partida
            time.sleep(3)
            os.system("cls")
            print("--- PLACAR GERAL ---")
            print(f"\nVitórias de {nomeJogador}: {vitoriasJogador}")
            print(f"Vitórias do computador: {vitoriasComputador}")
            print("\n--------------------")
            
            # pergunta se o jogador deseja continuar a jogar
            time.sleep(3)
            os.system("cls")
            print("A partida terminou. Deseja continuar? Digite (1) - Sim, (2) - Não")
            terminarJogo = input("")
            # se sim, o loop continua
            if terminarJogo == "1":
                garantirModo = "1"
            else:
                garantirModo = "2"
                time.sleep(3)
                os.system("cls")
                print("--- RESULTADO FINAL ---")
                print(f"\nEmpates: {empates}")
                print(f"Vitórias de {nomeJogador}: {vitoriasJogador}")
                print(f"Vitórias do computador: {vitoriasComputador}")
                print("\n-----------------------")
                print(f"\nObrigado por jogar, {nomeJogador}!")
    elif garantirModo == "2":
        os.system("cls")
        print("Programa encerrado!")
    else:
        os.system("cls")
        print("Programa encerrado! Digite algo válido da próxima vez!")
elif escolherModo == "3":
    # certifica-se que o modo escolhido foi o correto
    os.system("cls")
    print("Modo escolhido: computador x computador. Caso deseje continuar, digite (1).")
    print("Caso deseje mudar o modo de jogo, digite (2)")
    garantirModo = input("")
    
    if garantirModo == "1":
        # estabelece as variáveis iniciais
        vitoriasComputadorUm = 0
        vitoriasComputadorDois = 0
        empates = 0
        
        while garantirModo == "1":
            # começa o jogo pelo computadorUm, que escolhe entre as opções abaixo.
            # depois, vai para o computadorDois
            os.system("cls")
            print("Excelente! Agora, se prepare para assistir!")
            time.sleep(3)
            os.system("cls")
            print("O COMPUTADOR UM irá escolher entre: (1) - Pedra, (2) - Papel, (3) - Tesoura")
            # opções: 1 - Pedra, 2 - Papel, 3 - Tesoura
            opcoes = ["1", "2", "3"]
            opcaoAleatoriaComputadorUm = random.choice(opcoes)
            time.sleep(3)
            if opcaoAleatoriaComputadorUm == "1":
                opcaoEscolhidaUm = "Pedra"
            elif opcaoAleatoriaComputadorUm == "2":
                opcaoEscolhidaUm = "Papel"
            else:
                opcaoEscolhidaUm = "Tesoura"
            os.system("cls")
            print(f"O COMPUTADOR UM escolheu: {opcaoEscolhidaUm}")
            time.sleep(3)
            os.system("cls")
            print("Agora, o COMPUTADOR DOIS vai escolher: (1) - Pedra, (2) - Papel, (3) - Tesoura")
            opcaoAleatoriaComputadorDois = random.choice(opcoes)
            time.sleep(3)
            if opcaoAleatoriaComputadorDois == "1":
                opcaoEscolhidaDois = "Pedra"
            elif opcaoAleatoriaComputadorDois == "2":
                opcaoEscolhidaDois = "Papel"
            else:
                opcaoEscolhidaDois = "Tesoura"
            os.system("cls")
            print(f"O COMPUTADOR DOIS escolheu: {opcaoEscolhidaDois}")
            time.sleep(3)
            os.system("cls")
            # estabelece as lógicas entre cada opção e atualiza os status de vitórias
            if opcaoAleatoriaComputadorUm == "1" and opcaoAleatoriaComputadorDois == "3":
                vitoriasComputadorUm += 1
                print("Vitória do COMPUTADOR UM! Ele escolheu Pedra. O COMPUTADOR DOIS escolheu Tesoura!")
            elif opcaoAleatoriaComputadorUm == "2" and opcaoAleatoriaComputadorDois == "1":
                vitoriasComputadorUm += 1
                print("Vitória do COMPUTADOR UM! Ele escolheu Papel. O COMPUTADOR DOIS escolheu Pedra!")
            elif opcaoAleatoriaComputadorUm == "3" and opcaoAleatoriaComputadorDois == "2":
                vitoriasComputadorUm += 1
                print(" Vitória do COMPUTADOR UM! Ele escolheu Tesoura. O COMPUTADOR DOIS escolheu Papel!")
            elif opcaoAleatoriaComputadorDois == "1" and opcaoAleatoriaComputadorUm == "3":
                vitoriasComputadorDois += 1
                print("Vitória do COMPUTADOR DOIS! Ele escolheu Pedra! O COMPUTADOR UM escolheu Tesoura!")
            elif opcaoAleatoriaComputadorDois == "2" and opcaoAleatoriaComputadorUm == "1":
                vitoriasComputadorDois += 1
                print("Vitória do COMPUTADOR DOIS! Ele escolheu Papel! O COMPUTADOR UM escolheu Pedra!")
            elif opcaoAleatoriaComputadorDois == "3" and opcaoAleatoriaComputadorUm == "2":
                vitoriasComputadorDois += 1
                print("Vitória do COMPUTADOR DOIS! Ele escolheu Tesoura! O COMPUTADOR UM escolheu Papel!")
            elif opcaoAleatoriaComputadorDois == opcaoAleatoriaComputadorUm:
                print("Empate! Ambos os computadores escolheram a mesma jogada!")
                empates += 1
            
            time.sleep(3)
            # mostra o placar geral após cada partida
            os.system("cls")
            print("--- PLACAR GERAL ---")
            print(f"\nVitórias do COMPUTADOR UM: {vitoriasComputadorUm}")
            print(f"Vitórias do COMPUTADOR DOIS: {vitoriasComputadorDois}")
            print("\n--------------------")
            time.sleep(3)
            # pergunta se o jogador deseja continuar a assistir
            os.system("cls")
            print("A partida terminou. Deseja continuar a assistir? Digite (1) - Sim, (2) - Não")
            terminarJogo = input("")
            # se sim, o loop continua
            if terminarJogo == "1":
                garantirModo = "1"
            # se não, o loop para e os valores finais são imprimidos
            else:
                garantirModo = "2"
                time.sleep(3)
                os.system("cls")
                print("--- RESULTADO FINAL ---")
                print(f"\nEmpates: {empates}")
                print(f"Vitórias do COMPUTADOR UM: {vitoriasComputadorUm}")
                print(f"Vitórias do COMPUTADOR DOIS: {vitoriasComputadorDois}")
                print("\n-----------------------")
                print("\nObrigado por assistir os computadores jogarem!")
    elif garantirModo == "2":
        os.system("cls")
        print("Programa encerrado!")
    else:
        os.system("cls")
        print("Programa encerrado! Digite algo válido da próxima vez!")
else:
    os.system("cls")
    print("Programa encerrado! Digite uma das opções acima quando inicializar novamente o programa!")