import random

def isimler():
    isim = ["Albert", "Charles", "Nicolas", "Michael", "Anders", "Isaac", "Stephen", "Marie", "Richard"]
    soyadı = ["Einstein", "Darwin", "Copernicus", "Faraday", "Celsius", "Newton", "Hawking", "Curie","Dawkins"]
    return "{} {}".format(random.choice(isim), random.choice(soyadı))
for i in range(5):
    print(isimler())
