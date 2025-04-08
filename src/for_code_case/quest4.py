import random
def quest4 ():
    while True:
        player = input("Pedra, papel ou tesoura?").lower()
        npc = random.choice(["pedra", "papel", "tesoura"])

        if player not in ["pedra", "papel", "tesoura"]:
            print("Insira um valor válido!")
            continue

        match player, npc:
            case player, npc if player == npc:
                print(f"Player: {player} \nNPC: {npc}")
                print("Empate!\n\n")
                continue

            case "pedra", "tesoura":
                print(f"Player: {player} \nNPC: {npc}")
                print("Ganhou!\n")

            case "pedra", "papel":
                print(f"Player: {player} \nNPC: {npc}")
                print("Perdeu!\n")

            case "papel", "tesoura":
                print(f"Player: {player} \nNPC: {npc}")
                print("Perdeu!\n")

            case "papel", "pedra":
                print(f"Player: {player} \nNPC: {npc}")
                print("Ganhou!\n")

            case "tesoura", "papel":
                print(f"Player: {player} \nNPC: {npc}")
                print("Ganhou!\n")

            case "tesoura", "pedra":
                print(f"Player: {player} \nNPC: {npc}")
                print("Perdeu!\n")
        break
quest4()