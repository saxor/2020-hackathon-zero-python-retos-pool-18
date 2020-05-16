from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ia):
    player = player.lower()
    ia = ia.lower()
    
    plays = [
        { 'player': 'piedra', 'ia': 'tijeras', 'res': 'G' },
        { 'player': 'piedra', 'ia': 'papel', 'res': 'P' },
        { 'player': 'papel', 'ia': 'piedra', 'res': 'G' },
        { 'player': 'papel', 'ia': 'tijeras', 'res': 'P' },
        { 'player': 'tijeras', 'ia': 'papel', 'res': 'G' },
        { 'player': 'tijeras', 'ia': 'piedra', 'res': 'P' }]

    result = [item for item in plays if item["player"] == player and item["ia"] == ia]
    if player == ia:
        return 'Empate!'
    if result[0]['res'] == 'G':
        return 'Ganaste!'
    if result[0]['res'] == 'P':
        return 'Perdiste!'
    
    return "Error"

# Entry Point
def Game():
    #
    # Input para el jugador player
    player = input('Introduce con que vas a jugar (Piedra, Papel o Tijeras): ')
    player = player.lower()

    #
    # Random para la IA
    ai = options[randint(0,2)]
    print(ai)

    winner = quienGana(player, ai)

    print(winner)

if __name__ == '__main__':
    Game()