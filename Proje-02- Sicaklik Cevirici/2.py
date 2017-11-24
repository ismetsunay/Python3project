print("-" * 30)
print("1- Celsius to fahrenheit")
print("2- Fahrenheit to celsius")
print("-" * 30)
seçim = input("Ikisinden birini seç (1/2):")

if seçim == "1":
    print("\n Celsius to Fahrenheit")
    celsius = float(input("Dönüşüm derecesi: "))
    fahrenhayt = (celsius * 1.8) + 32
    print("{} derece fahrenheit eşittir {} derece fahrenheit.".format(celsius, fahrenhayt))
elif seçim == "2":
    print("\n Fahrenheit to Celsius")
    fahrenhayt = float(input("Dönüşüm derecesi: "))
    celsius = (fahrenhayt - 32) / 1.8
    print("{} derece fahrenheit eşittir {} derece celsius.".format(fahrenhayt, celsius))
else:
    print("Geçersiz işlem.")
