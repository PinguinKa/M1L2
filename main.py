import random   

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length = int(input('Введите длину пароля: '))

password = ''

for i in range(length):
    password += random.choice(symbols)

print(password)