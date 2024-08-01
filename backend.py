import random
#selects random word afive letter word

GAMEROUND=1

winner_word=[]

def word():
    global winner_word
    wordsPTR=open("WORDS.txt")

    randmword=random.choice(wordsPTR.read().split())
    winner_word=list(randmword)
    wordsPTR.close()
    print(winner_word)
word()

getscore=open("Gamestreak.txt").read()

def iswords(user_input):
    with open("WORDS.txt", "r") as words:
        for word in words:
            if user_input in word:
                return True



#states of a letter
# a letter can be:
# not in the word=-1 
#in the word(not correct place)=0
# in the correct place in the word=1
game_state=[-1,-1,-1,-1,-1]

def state(winner_word, user_guess):
    global game_state
    #user_position=0
    #winner_position=0
     #defaults all the states to not in the word

    for user_position, user_guess[user_position] in enumerate(user_guess):
        print(user_position,user_guess[user_position])
        for winner_position, winner_word[winner_position] in enumerate(winner_word):
            if user_guess[user_position]==winner_word[user_position]:
                game_state[user_position]=1
            elif (user_guess[user_position]==winner_word[winner_position]) or (winner_word).count(user_guess[user_position]) >=1:
                game_state[user_position]=0
            else:
                game_state[user_position]=-1
    #user_position+=1
    #print(game_state, "gamestate")
        
def highscore(round_num,score):
    if int(round_num)>int(score):
        with open('Gamestreak.txt', 'w') as file:
            file.write(str(round_num)) 

def winner(round_num, score):
    
    if game_state==[1,1,1,1,1]:
        highscore(round_num,score)