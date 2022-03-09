import csv
import numpy as np
d = []
dia = 0
mes = 0
ano = 0
prec = []
precipitacao = 0
count = 0
V1 = 0
V2 = 0
V3 = 0
V4 = 0
V5 = 0
V6 = 0
i = 0
with open('C:\\Users\\josiv\\Documents\\programas_python\\60-independencia1.txt') as f:
    csv_reader = csv.reader(f, delimiter=';')
    cabecalho = next(csv_reader, None)
    prec = []
    for row in csv_reader:
        ano = int(row[4])
        mes = int(row[5])
        prec.append(mes)
        prec.append(row[7:])

    for z in range(0, len(prec), 2):
        # print(prec[z]) #printa o mes
        # print(prec[z+1]) #printa a precipitacao
        for j in prec[z+1]:
            precipitacao = float(j)
            if np.isnan(precipitacao) == True:
                pass
            else:

                if prec[z] <= 5 and precipitacao < 2.0:

                    print(mes, ano, precipitacao)
                    count += 1
                    print(count)

                    if 5 == count:
                        V1 += 1
                        print('V1 =', V1, 'V2 =', V2, 'V3 =', V3, 'V4 =', V4, 'V5 =', V5, 'V6 =', V6)

                    elif 11 == count:
                        V2 += 1
                        print('V1 =', V1, 'V2 =', V2, 'V3 =', V3, 'V4 =', V4, 'V5 =', V5, 'V6 =', V6)

                    elif 16 == count:
                        V3 += 1
                        print('V1 =', V1, 'V2 =', V2, 'V3 =', V3, 'V4 =', V4, 'V5 =', V5, 'V6 =', V6)

                    elif 21 == count:
                        V4 += 1
                        print('V1 =', V1, 'V2 =', V2, 'V3 =', V3, 'V4 =', V4, 'V5 =', V5, 'V6 =', V6)

                    elif 26 == count:
                        V5 += 1
                        print('V1 =', V1, 'V2 =', V2, 'V3 =', V3, 'V4 =', V4, 'V5 =', V5, 'V6 =', V6)

                    elif count == 31:
                        V6 += 1
                        print('V1 =', V1, 'V2 =', V2, 'V3 =', V3, 'V4 =', V4, 'V5 =', V5, 'V6 =', V6)

                else:
                    count = 0

if V2 >= 1:
    V1 = V1 - V2
if V3 >= 1:
    V2 = V2 - V3
if V4 >= 1:
    V3 = V3 - V4
if V5 >= 1:
    V4 = V4 - V5
if V6 >= 1:
    V5 = V5 - V6

print('V1 =', V1, 'V2 =', V2, 'V3 =', V3, 'V4 =', V4, 'V5 =', V5, 'V6 =', V6)
