import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

directory = "/content/drive/MyDrive/Special_folder/Для студентов/Проект_инсульт/ColorStroop/9003_stroop_2023-03-07_14h10.10.726.csv"
df = pd.read_csv(directory)
df = pd.read_csv(directory)

if 'feedback.started' in df.columns:
    fname = 'feedback.started'
else:
    fname = 'feedback_image.started'

df_filtered = df[(df[fname].isna()) & (df['response.rt'] > 0.150)]
arr = df_filtered['response.rt']

arr_new = np.log(arr)

Sample_average = np.mean(arr_new)

Var = np.sqrt(np.mean((arr_new - Sample_average) ** 2))


def func(x):
    return (np.log(x) - Sample_average) / Var

df_f = df_filtered[df_filtered['response.rt'].apply(func) < 3]
df_f1 = df_f[df_f['response.rt'].apply(func) > -3]
df_res = df_f1[['word', 'cor', 'dir', 'congr', 'response.keys', 'response.corr', 'response.rt']]

mas = df_res['response.rt']

plt.hist(mas, bins=15, edgecolor='black')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.title('Гистограмма данных после обработки')
plt.grid(True)
plt.show()
