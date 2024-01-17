import random



print(f"{'#'*20} Welcome to rock paper scissor game {'#'*20}\n\n")
print('Rules:')
print('* Rock crushes scissor (rock wins against scissor)')
print('* Scissor cut paper (scissor win against paper)')
print('* Paper covers rock (paper wins against rock)')
print("* If both Players choose the same shape, the round is a tie, and no points are awarded.\n")
print('Scoring:')
print('* Each Player starts with 0 points.')
print('* After each round, the winner of that round gets 1 point.')
print('* If the round is a tie, no points are awarded to either Player.\n')
print('After three rounds, the Player with the most points is declared the overall winner.')

#Player
i =1
pl_points = 0
cm_points = 0
print('\nComputer:Write any one choice from scissor,paper and rock')
while(i<=3):
    che = random.choice(['paper','scissor','rock'])
    ply_chs = input('You:').replace(" ","")
    print(f'Computer:{che}')
    if ply_chs.lower() == che:
        print(f'Computer:Round{i} is tie')
        print(f'You:score={pl_points}')
        print(f'Computer:Score={cm_points}')
    elif ply_chs.lower() == 'rock' :
        if che == 'paper':
            pl_points +=1
            print(f'You:score={pl_points}')
            print(f'Computer:Score={cm_points}')
        else:
            cm_points +=1
            print(f'You:score={pl_points}')
            print(f'Computer:Score={cm_points}')
        
    elif ply_chs.lower() == 'paper':
        if che == 'rock':
            pl_points +=1
            print(f'You:score={pl_points}')
            print(f'Computer:Score={cm_points}')
        else:
            cm_points +=1
            print(f'You:score={pl_points}')
            print(f'Computer:Score={cm_points}')
    elif ply_chs.lower() == 'scissor':
        if che == 'paper':
            pl_points +=1
            print(f'You:score={pl_points}')
            print(f'Computer:Score={cm_points}')
        else:
            cm_points +=1
            print(f'You:score={pl_points}')
            print(f'Computer:Score={cm_points}')
    else:
        print('Computer:plese write the correct choice')
        i-=1
    i +=1


if cm_points == pl_points:
    print('\nComputer:Match tie')
elif cm_points < pl_points:
    print('\nComputer:Congratulation! You win.')
else:
    print('\nComputer:You Loss')