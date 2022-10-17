import objects.round as r

#Condition to play:
_play = True

while _play:
    #STARTING THE GAME:
    round = r.Round()
    round.start()

    #DECIDING WHETHER TO CONTINUE OR NOT:
    _continue = input("Quer continuar jogando? (S/N):").upper()
    _play = True if _continue == 'S' else False