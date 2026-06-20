import os
os.system('cls')


print ("==============Saber seu Imc==============")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura : "))

imc = peso / (altura ** 2)

print("Seu IMC é:", round(imc, 2))

if imc < 18.5:
        print("Abaixo do peso")
elif imc < 24.9:
        print ("peso normal")
elif imc < 29.9:
        print ("sobrepeso")
elif imc < 34.9:
        print ("obesidade grau I")
elif imc < 39.9:
        print ("Obesidade garu II")
else:
        print ("Obesidade grau III")   



