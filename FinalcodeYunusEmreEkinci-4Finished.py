import pandas as pd

# Veriler
data = {
    'xi': [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65],
    'c1': [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16],
    'c2': [22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22]
}

# DataFrame oluşturma
df = pd.DataFrame(data)

# Başlangıç küme merkez değerleri
c1 = 16
c2 = 22

# Mesafe hesaplama fonksiyonu


def manhattan_distance(x, y):
    return abs(x - y)


# İterasyonlar
for iteration in range(4):
    # Uzaklıkları hesapla ve kümeye atama
    df['Distance1'] = df['xi'].apply(lambda x: manhattan_distance(x, c1))
    df['Distance2'] = df['xi'].apply(lambda x: manhattan_distance(x, c2))
    df['Cluster'] = df[['Distance1', 'Distance2']].idxmin(
        axis=1).apply(lambda x: x[-1])

    # Yeni küme merkezlerini güncelle
    c1 = df[df['Cluster'] == '1']['xi'].mean()
    c2 = df[df['Cluster'] == '2']['xi'].mean()

    # Sonuçları yazdır
    print(f"{iteration+1}. iterasyon sonucu:")
    print("c1 =", c1)
    print("c2 =", c2)

    df['Centroid'] = df['Cluster'].map({'1': c1, '2': c2})
    df = df[['xi', 'c1', 'c2', 'Cluster', 'Centroid']]
    print(df)
    print("")
