import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

directory = "/content/drive/MyDrive/Special_folder/Для студентов/Проект_инсульт/ColorStroop/9003_stroop_2023-03-07_14h10.10.726.csv"
df = pd.read_csv(directory)

mas = df['response.rt']

plt.hist(mas, bins=50, edgecolor='black')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.title('Гистограмма данных до обработки')
plt.grid(True)
plt.show()
