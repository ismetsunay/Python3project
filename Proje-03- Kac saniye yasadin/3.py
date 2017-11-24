from datetime import *


birth = datetime.strptime(input("Doğum tarihin (d.m.Y): "), "%d.%m.%Y")

age = datetime.now() - birth


print("Hayatta {} saniye kaldın".format(age.total_seconds()))
