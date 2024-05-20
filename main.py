import random
elementi = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ù"

lunghezza = int(input("scegli la lunghezza della password:"))

password = ""
for i in range(lunghezza):
    password += random.choice(elementi)
print(password)
