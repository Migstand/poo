from datetime import datetime, timedelta

x = datetime.strptime("10/10/2025 9:00", "%d/%m/%Y %H:%M")
y = timedelta(hours=1, minutes=30)
z = x + y

print(x)
print(y)
print(z)

a = datetime.strptime(input("Informe a data de nascimento: "), "%d/%m/%Y")
b = datetime.now()

print(a)
print(b)