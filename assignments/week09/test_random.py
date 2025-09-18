import random

GA_Random = random.randint(0, 10)
p_layer=int(input('Enter number: '))
if p_layer == GA_Random:
    print('you win')

elif p_layer < GA_Random:
    print('low try again')

elif p_layer > GA_Random:
    print('high try again')