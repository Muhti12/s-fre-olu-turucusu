import random
degıskenler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
parola_uzunlugu = int(input("Parolanın uzunluğu ne kadar olmalı?"))
sıfre = ""
for i in range(parola_uzunlugu):
    sıfre = random.choice(degıskenler) + sıfre
print(sıfre)
