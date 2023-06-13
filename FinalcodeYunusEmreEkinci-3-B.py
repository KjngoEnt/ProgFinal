import pandas as pd
import numpy as np

data = {
    'X': [1, 2, 2, 3, 4, 5, 6, 8, 10, 11],
    'Y': [3, 5, 3, 9, 7, 2, 8, 6, 6, 1],
    'Z': ['Negatif', 'Pozitif', 'Pozitif', 'Negatif', 'Negatif', 'Pozitif', 'Pozitif', 'Negatif', 'Negatif', 'Negatif']
}
new_x = 7
new_y = 3

df = pd.DataFrame(data)


def euclidean_distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)


df['Distance'] = df.apply(lambda row: euclidean_distance(
    row['X'], row['Y'], new_x, new_y), axis=1)

df['YakinlikSirasi'] = df['Distance'].rank(ascending=True)

print("Tablo:")
print(df)
