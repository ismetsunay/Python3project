import random

print(("-" * 30) + "\nTaş,Kağıt,Makas\n" + ("-" * 30))

kullanıcı_puanı, bilgisayar_puanı = 0, 0

while True:

    print("\n1 - Taş\n2 - Kağıt\n3 - Makas")
    kullanıcı_seçimi = input("Senin seçimin: ")
    bilgisayar_seçimi = random.choice(["1", "2", "3"])

    if kullanıcı_seçimi == "1":

        if bilgisayar_seçimi == "1":
            print("Bilgisayarın tercihi: Taş\nKaya kayaya eşit.Berabere!")

        elif bilgisayar_seçimi == "2":
            print("Bilgisayarın tercihi: Kağıt\nKağıt taşı sarar.Kaybettin!")
            bilgisayar_puanı += 100

        elif bilgisayar_seçimi == "3":
            print("Bilgisayarın tercihi: Makas\nKaya makası kırıyor.Sen kazandın!")
            kullanıcı_puanı += 100



    elif kullanıcı_seçimi == "2":

        if bilgisayar_seçimi == "1":
            print("Bilgisayarın tercihi: Taş\nKağıt taşı sarar.Sen kazandın!")
            kullanıcı_puanı += 100

        elif bilgisayar_seçimi == "2":
            print("Bilgisayarın tercihi: Kağıt\nKağıt kağıda eşit.Berabere!")

        elif bilgisayar_seçimi == "3":
            print("Bilgisayarın tercihi: Makas\nMakas kağıtı keser.Kaybettin!")
            bilgisayar_puanı += 100


    elif kullanıcı_seçimi == "3":

        if bilgisayar_seçimi == "1":
            print("Bilgisayarın tercihi: Taş\nKaya makası kırıyor.Kaybettin!")
            bilgisayar_puanı += 100


        elif bilgisayar_seçimi == "2":
            print("Bilgisayarın tercihi: Kağıt\nMakas kağıtı keser.Sen kazandın!")
            kullanıcı_puanı += 100

        elif bilgisayar_seçimi == "3":
            print("Bilgisayarın tercihi: Makas\nMakas makasa eşit.Berabere!")

    else:
        break

print("\nKullanıcı puanı: {}\nBilgisayarın skoru: {}".format(kullanıcı_puanı, bilgisayar_puanı))
