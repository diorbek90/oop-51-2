import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

"""
    Библиотека matplotlib используется для визуализации данных двухмерной и трехмерной графикой, с помощью
    него можно строить графики функции такие как парабола гипербола и т.д. Вот базовый пример использование.
"""


x_value = [i for i in range(-8, 8+1) if i != 0]
y_values = []

for i in x_value:
    if i != 0:
        y_values.append(4/i)

plt.figure(figsize=(4, 4))

plt.plot(x_value, y_values, color='g')
plt.title("График гиперболы")
plt.grid()
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.show()

print(x_value)
print(y_values)