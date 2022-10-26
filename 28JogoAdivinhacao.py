from time import sleep
import random
print('\033[33;1m-=' * 35)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[33;1m-=\033[m' * 35)

com = random.randint(0, 5)
num = int(input('Em que número eu pensei? '))
print('\033[36mPROCESSANDO...')
sleep(1)

if com == num:
    print(f'\033[33;1mPARABÉNS! VOCÊ GANHOU! Eu realmente pensei no número {num}!')
else:
    print(f'\033[31;1mGANHEI! Eu pensei no número {com} e não no {num}!')
