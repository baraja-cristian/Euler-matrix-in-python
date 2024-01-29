import numpy as np
import matplotlib.pyplot as plt

# MATRIZ DE EULER
# SOLICITAR AL USUARIO INGRESAR LA ECUACIÓN DIFERENCIAL COMO UNA CADENA DE CARACTERES

equation_str = input('INGRESE LA ECUACIÓN DIFERENCIAL dy/dx = ')

# Definir la ecuación diferencial como una función
equation = lambda x, y: eval(equation_str)

 
# INGRESAR LOS VALORES INICIALES Y LOS PARÁMETROS POR CONSOLA

x0 = float(input('INGRESE EL VALOR INICIAL DE x: '))

y0 = float(input('INGRESE EL VALOR INICIAL DE y: '))

h = float(input('INGRESE EL TAMAÑO DEL PASO h: '))

xf = float(input('INGRESE EL VALOR FINAL DE x: '))


# INICIALIZACIÓN DE VECTORES PARA ALMACENAR LOS RESULTADOS
x_values = np.arange(x0, xf + h, h)
y_values = np.zeros_like(x_values)

# CONDICIONALES INICIALES
y_values[0] = y0

# IMPLEMENTACIÓN DEL MÉTODO DE EULER
print('ITERACIÓN\t x\t\t y')

for i in range(len(x_values)-1):
    x = x_values[i]
    y = y_values[i]

    # ECUACION DIFERENCIAL
    dy_dx = equation(x, y)

    # MÉTODO DE EULER
    y_new = y + h * dy_dx

    # ALMACENAR EL NUEVO VALOR DE y EN EL VECTOR DE RESULTADOS
    y_values[i+1] = y_new

    # MOSTRAR VALORES EN CONSOLA
    print(f'{i+1}\t\t {x:.4f}\t {y:.6f}')

# MOSTRAR EL VALOR FINAL DE y EN CONSOLA

print(f'VALOR FINAL DE y: {y_values[-1]:.6f}')


# VISUALIZACIÓN DE LOS RESULTADOS
plt.plot(x_values, y_values, '-o')
plt.title(f'MÉTODO DE EULER PARA {equation_str}')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
