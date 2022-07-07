from random import randint


char = ''.join(chr(randint(65, 91)) for _ in range(100))

with open('/tmp/saida.txt', 'w') as f:
    f.write(f'JESUS TE AMA! {char}')