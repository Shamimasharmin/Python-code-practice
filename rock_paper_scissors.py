activate = True
user_choices=['Yes', 'y', 'No', 'n']
while activate:
    words=['Rock', 'ROCK', 'rock', 'Paper', 'PAPER', 'paper', 'Scissors', 'SCISSORS', 'scissors']
    player1 = input('player1- Choose one: Rock, Paper or Scissors : ')
    if player1 in words:
        for word in words:
            if player1==word:
                pass
                player2 = input('player2- Choose one: Rock, Paper or Scissors : ')
                if player2 in words:
                    for word1 in words:
                        if player2==word1:
                            pass
                            if player1=='rock' and player2=='scissors':
                                print('Congrats, player1 win the game')
                            if player2=='rock' and player1=='scissors':
                                print('Congrats, player2 win the game')
                            if player1=='scissors' and player2=='paper':
                                print('Congrats, player1 win the game')
                            if player2=='scissors' and player2=='paper':
                                print('Congrats, player2 win the game')
                            if player1=='paper' and player2=='rock':
                                print('Congrats, player1 win the game')
                            if player1=='rock' and player2=='paper':
                                print('Congrats, player2 win the game')

    user_input=input('Do you want to continue? ')

    if user_input.lower() == user_choices[0].lower() or user_input.lower==user_choices[1].lower():
        continue
    else:
        print('Thanks for playing')
        activate=False
                            
                            
                            
                            
