#Mark Larrenz C. Bathan
#BAET 2102
#CHANGE CALCULATOR

name = (input("Mark Larrenz C. Bathan:"))
print("Hello," +name)

amount = int(input("Enter the amount you want to peso: "))

pesos100 = amount // 100
remaining = amount % 100

pesos20 = remaining // 20
remaining = remaining % 20

pesos30 = remaining // 30
remaining = remaining % 30

pesos5 = remaining // 5
remaining = remaining % 5

pesos1 = remaining // 1

print("100 pesos:", pesos100)
print("20 pesos:", pesos20)
print("5 pesos:", pesos5)
print("1 peso:", pesos1)

