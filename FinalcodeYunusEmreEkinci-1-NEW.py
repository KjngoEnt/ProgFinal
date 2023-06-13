import pandas as pd
import numpy as np

data = {
    'PERSONEL': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'MAAS': ['NORMAL', 'YUKSEK', 'DUSUK', 'YUKSEK', 'DUSUK', 'YUKSEK', 'DUSUK', 'YUKSEK', 'DUSUK', 'YUKSEK', 'DUSUK'],
    'DENEYIM': ['ORTA', 'YOK', 'YOK', 'ORTA', 'ORTA', 'IYI', 'IYI', 'ORTA', 'ORTA', 'IYI', 'IYI'],
    'GOREV': ['UZMAN', 'UZMAN', 'YONETICI', 'YONETICI', 'YONETICI', 'YONETICI', 'YONETICI', 'UZMAN', 'UZMAN', 'UZMAN', 'UZMAN'],
    'MEMNUN': ['EVET', 'EVET', 'EVET', 'EVET', 'EVET', 'EVET', 'EVET', 'HAYIR', 'HAYIR', 'HAYIR', 'HAYIR'],
}

conditions = {
    'BOLUNME': [1, 2, 3, 4, 5, 6, 7, 8],
    'CON1': ['MAAS', 'MAAS', 'MAAS', 'DENEYIM', 'DENEYIM', 'DENEYIM', 'GOREV', 'GOREV'],
    'CON2': ['NORMAL', 'YUKSEK', 'DUSUK', 'YOK', 'ORTA', 'IYI', 'UZMAN', 'YONETICI']
}

MaddeB = {
    'BOLUNME': conditions['BOLUNME'],
    'SOL': [None] * len(conditions['BOLUNME']),
    'SAG': [None] * len(conditions['BOLUNME']),
    'MEMNUNsol': [None] * len(conditions['BOLUNME']),
    'MEMNUNsag': [None] * len(conditions['BOLUNME'])
}

df = pd.DataFrame(data)  # Madde A

print(df)

for i, x in enumerate(conditions['CON1']):
    solcounter = 0
    sagcounter = 0
    memnuncounter = 0
    memnuncounter2 = 0
    if x == 'MAAS':

        for b, a in enumerate(data['MAAS']):

            if a == conditions['CON2'][i]:
                solcounter = solcounter + 1
                MaddeB['SOL'][i] = solcounter
                if data['MEMNUN'][b] == 'EVET':
                    memnuncounter = memnuncounter + 1
                    MaddeB['MEMNUNsol'][i] = memnuncounter
            else:
                sagcounter = sagcounter + 1
                MaddeB['SAG'][i] = sagcounter
                if data['MEMNUN'][b] == 'EVET':
                    memnuncounter2 = memnuncounter2 + 1
                    MaddeB['MEMNUNsag'][i] = memnuncounter2

    elif x == 'DENEYIM':

        for b, a in enumerate(data['DENEYIM']):

            if a == conditions['CON2'][i]:
                solcounter = solcounter + 1
                MaddeB['SOL'][i] = solcounter
                if data['MEMNUN'][b] == 'EVET':
                    memnuncounter = memnuncounter + 1
                    MaddeB['MEMNUNsol'][i] = memnuncounter
            else:
                sagcounter = sagcounter + 1
                MaddeB['SAG'][i] = sagcounter
                if data['MEMNUN'][b] == 'EVET':
                    memnuncounter2 = memnuncounter2 + 1
                    MaddeB['MEMNUNsag'][i] = memnuncounter2

    elif x == 'GOREV':

        for b, a in enumerate(data['GOREV']):

            if a == conditions['CON2'][i]:
                solcounter = solcounter + 1
                MaddeB['SOL'][i] = solcounter
                if data['MEMNUN'][b] == 'EVET':
                    memnuncounter = memnuncounter + 1
                    MaddeB['MEMNUNsol'][i] = memnuncounter
            else:
                sagcounter = sagcounter + 1
                MaddeB['SAG'][i] = sagcounter
                if data['MEMNUN'][b] == 'EVET':
                    memnuncounter2 = memnuncounter2 + 1
                    MaddeB['MEMNUNsag'][i] = memnuncounter2


df = pd.DataFrame(MaddeB)  # Madde B

print(df)

MaddeCsol = {
    'BOLUNME': conditions['BOLUNME'],
    'Bsol': [None] * len(conditions['BOLUNME']),
    'Psol': [None] * len(conditions['BOLUNME']),
    'sinifEVET': [None] * len(conditions['BOLUNME']),
    'sinifHAYIR': [None] * len(conditions['BOLUNME']),
    'PsinifEVET': [None] * len(conditions['BOLUNME']),
    'PsinifHAYIR': [None] * len(conditions['BOLUNME'])
}

MaddeCsag = {
    'BOLUNME': conditions['BOLUNME'],
    'Bsag': [None] * len(conditions['BOLUNME']),
    'Psag': [None] * len(conditions['BOLUNME']),
    'sinifEVET': [None] * len(conditions['BOLUNME']),
    'sinifHAYIR': [None] * len(conditions['BOLUNME']),
    'PsinifEVET': [None] * len(conditions['BOLUNME']),
    'PsinifHAYIR': [None] * len(conditions['BOLUNME'])
}

EVETcounter = 0
HAYIRcounter = 0

# MaddeCsol
for i, x in enumerate(conditions['CON1']):
    MaddeCsol['Bsol'][i] = MaddeB['SOL'][i]

    MaddeCsol['Psol'][i] = MaddeCsol['Bsol'][i] / \
        (MaddeB['SAG'][i] + MaddeB['SOL'][i])
    MaddeCsol['Psol'][i] = round(MaddeCsol['Psol'][i], 2)

for i, b in enumerate(conditions['CON2']):
    MaddeCsol['sinifEVET'][i] = MaddeB['MEMNUNsol'][i]
    MaddeCsol['sinifHAYIR'][i] = MaddeCsol['Bsol'][i] - \
        MaddeB['MEMNUNsol'][i]

for i, b in enumerate(conditions['CON2']):
    MaddeCsol['PsinifEVET'][i] = MaddeCsol['sinifEVET'][i] / \
        MaddeCsol['Bsol'][i]
    MaddeCsol['PsinifHAYIR'][i] = MaddeCsol['sinifHAYIR'][i] / \
        MaddeCsol['Bsol'][i]

# MaddeCsag
for i, x in enumerate(conditions['CON1']):
    MaddeCsag['Bsag'][i] = MaddeB['SAG'][i]

    MaddeCsag['Psag'][i] = MaddeCsag['Bsag'][i] / \
        (MaddeB['SAG'][i] + MaddeB['SOL'][i])
    MaddeCsag['Psag'][i] = round(MaddeCsag['Psag'][i], 2)

for i, b in enumerate(conditions['CON2']):
    MaddeCsag['sinifEVET'][i] = MaddeB['MEMNUNsag'][i]
    MaddeCsag['sinifHAYIR'][i] = MaddeCsag['Bsag'][i] - \
        MaddeB['MEMNUNsag'][i]

for i, b in enumerate(conditions['CON2']):
    MaddeCsag['PsinifEVET'][i] = MaddeCsag['sinifEVET'][i] / \
        MaddeCsag['Bsag'][i]
    MaddeCsag['PsinifHAYIR'][i] = MaddeCsag['sinifHAYIR'][i] / \
        MaddeCsag['Bsag'][i]

df = pd.DataFrame(MaddeCsol)  # Madde C

print(df)

df = pd.DataFrame(MaddeCsag)  # Madde C

print(df)

MaddeD = {
    'BOLUNME': conditions['BOLUNME'],
    'Psol': (MaddeCsol['Psol']),
    'Psag': (MaddeCsag['Psag']),
    '2PsolPsag': [None] * len(conditions['BOLUNME']),
    'B|d': [None] * len(conditions['BOLUNME']),
}
n = 8
tempp = 0
for i, x in enumerate(MaddeD['BOLUNME']):
    MaddeD['Psol'][i] = MaddeCsol['Psol'][i]
    MaddeD['Psag'][i] = MaddeCsag['Psag'][i]
    MaddeD['2PsolPsag'][i] = 2 * MaddeCsol['Psol'][i] * MaddeCsag['Psag'][i]
    MaddeD['2PsolPsag'][i] = round(MaddeD['2PsolPsag'][i], 2)

    tempp = abs(MaddeCsol['sinifEVET'][i]/MaddeCsol['Bsol'][i] -
                MaddeCsag['sinifEVET'][i]/MaddeCsag['Bsag'][i]) + abs(MaddeCsol['sinifHAYIR'][i]/MaddeCsol['Bsol'][i] -
                                                                      MaddeCsag['sinifHAYIR'][i]/MaddeCsag['Bsag'][i])

    MaddeD['B|d'][i] = round(MaddeD['2PsolPsag'][i] * tempp, 2)


df = pd.DataFrame(MaddeD)  # Madde D

print(df)
enuygun = 0
for i, x in enumerate(MaddeD['B|d']):
    if enuygun < x:
        enuygun = x

print('En yuksek uygunluk degerine sahip bolme: ' + str(enuygun))  # Madde E
