import numpy as np
from sklearn.linear_model import LinearRegression

# Veriler
X = np.array([[5.1, 3.5, 1.4, 0.2],
              [4.9, 3.0, 1.4, 0.2],
              [7.0, 3.2, 4.7, 1.4],
              [6.4, 3.2, 4.5, 1.5],
              [6.3, 3.3, 6.0, 2.5],
              [5.8, 2.7, 5.1, 1.9]])

Y = np.array([[1, 0, 0],
              [1, 0, 0],
              [0, 1, 0],
              [0, 1, 0],
              [0, 0, 1],
              [0, 0, 1]])

# Doğrusal regresyon modelini oluştur
regression_model = LinearRegression()

# Modeli eğit
regression_model.fit(X, Y)

# Katsayılar
coef = regression_model.coef_

# Yeni örneği tahmin et
new_ex = np.array([5, 3.4, 1.5, 0.2]).reshape(1, -1)
predicted_class = regression_model.predict(new_ex)

# Katsayıları ve tahmin edilen sınıfı yazdır
print("Doğrusal Regresyon Katsayıları:")
print(coef)
print("-----------------------")
print("Yeni Örneğin Tahmin Edilen Sınıfı:")
print(predicted_class)
