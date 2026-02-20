import matplotlib.pyplot as plt

categorias = ["Aluguel", "Comida", "Transporte", "Lazer"]
valores = [1200, 800, 300, 400]

plt.pie(valores, labels=categorias, autopct="%1.1f%%")

#cores = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]
#plt.pie(valores, labels=categorias, autopct="%1.1f%%", colors=cores)
    
plt.title("Distribuição de Gastos")

plt.show()