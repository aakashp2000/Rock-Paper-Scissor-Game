import random
import math
def play():
    user= input("What is your choice? 'r' for rock, 's' for scissors, p for paper\n")
    user=user.lower()
    computer=random.choice(['r','p','s'])
    if user==computer:
        return (0,user,computer)
    if is_win(user,computer):
        return (1,user,computer)
    return (-1,user,computer)
def is_win(player,opponent):
    if(player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True
    return False
def best_of(n):
    player_w=0
    computer_w=0
    wins_nec=math.ceil(n/2)
    while player_w<wins_nec and computer_w<wins_nec:
        result,user,computer=play()
        if(result==0):
            print('You and the computer both chose {}. It is a tie'.format(user))
        elif(result==1):
            player_w+=1 
            print('You chose {} and computer chose {}. You won!'.format(user,computer))
        else:
            computer_w+=1
            print('You chose {} and computer chose {}. You lost!'.format(user,computer))
        print('\n')
    if player_w>computer_w:
        print('You have won the best of {}. What a champ'.format(n))
    else:
        print('You have lost the best of {}. Better luck next time'.format(n))
        
if __name__ == "__main__":
    best_of(3)
