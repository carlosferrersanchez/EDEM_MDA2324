
print(f"Hola. Bienvenido al sistema de cálculo de inversiones.")

dinero = float(input("Cuanto dinero tienes para invertir (€)? "))
interes = float(input("Cual es el interés anual? \nEscribelo en decimal, ej 5% = 0.05. "))
ano = int(input("Cuantos años quieres mantener la inversión? "))
profit = dinero*interes*ano

print(f"En {ano} años tendrás {profit}€ de interés")