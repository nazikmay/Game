import random
import os
import re
os.system('cls' if os.name=='nt' else 'clear')

while True:
    print('Rock,Paper,Scissors-Shoot!')
    userChois = input(" tanda [R]ock, [P]aper or [S]cissors [E]xit:").upper()
    if not re.match('[SsRrPpEe]', userChois):
            print("pleas chois a latters")
            print('[R]ock, [P]aper or [S]cissors')
            continue
    print('yor chois: '+ userChois)
    choices= ['R','P','S']
    rand = random.choice(choices)
    print('I chois '+ rand)
    if rand ==str.upper(userChois):
        print('Tei!')
    elif rand == 'R' and userChois.upper()=='S':
        print('таш кайчыга кирет ! мен уттум')
    elif rand =='S' and userChois.upper()== 'P':
        print('кайчы кагазды кести. мен уттум')
    elif rand == 'P' and userChois.upper()=='R':
        print('кагаз ташты жабат.мен уттум')

    elif userChois== 'E':
        print('Exit')
        break

    else:
        print("сен уттун!")