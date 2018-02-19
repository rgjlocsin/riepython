print("iPhone X price: 50000 Pesos")
Money = input("Your account balance:")

Price = 50000

Quantity = Money/Price
Excess = Money%Price

print("You can avail a total of", Quantity, "iPhone X phone(s).")
print("With an excess of", Excess, "Pesos, you need", Price-Excess, "to avail another iPhone X.")

