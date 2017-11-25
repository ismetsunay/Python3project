from datetime import *

önce = datetime.now()
text = "Küçük arkadaşıma merhaba de."
print("Lütfen yazın: {}".format(text))

if text == input(": "):
    sonra = datetime.now()
    hız = sonra - önce
    saniye = hız.total_seconds()
    saniyede_mektup = round(len(text) / saniye, 1)

    print("Kazandın!!")

    print("Skorunuz: {} saniye.".format(saniye))

    print("{} saniyede harf.".format(saniyede_mektup))

else:
    print("Hata yaptın.")
