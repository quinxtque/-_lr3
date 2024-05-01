
n = 4
m = 4
p = 1

def Mul(matrix1, matrix2):
    result = []

    for i in range(n):
        result.append([])
        for j in range(p):
            summ = 0
            for k in range(m):
                summ += matrix1[i][k] * matrix2[k]
            result[i].append(summ)

    return result


def Add(matrix1, matrix2):
    result = []
    for i in range(n):

        for j in range(p):
            result.append(matrix1[i][j] + matrix2[i])

    return result


def show_x(x):
    print("  ", end=' ')
    for i in range(len(x)):
        print(f"{i:>11}", end=' ')
    print()

    for i in range(len(x[0])):
        print(f"x{i + 1}", end=' ')
        for j in range(len(x)):
            #round(x[j][i], rounder)
            print(f"{x[j][i]:>11.8f}".replace('.', ','), end=' ')
        print()


def show_delta(d):
    print("d ", end=' ')
    for i in range(len(d)):
        #round(d[i], rounder)
        print(f"{d[i]:>11.8f}".replace('.', ','), end=' ')
    print()

'''
петрушкин вариант

    x1 - x2 + 4x3 = 2
    0.5x1 + 2x2 - x3 = 1
    5x1 - x2 + x3 = 4

    next:
    4x3 = -x1 + x2 + 2
    2x2 = -0.5x1 + x3 + 1
    5x1 = x2 - x3 + 4

    next:
    x1 = 0.2x2 - 0.2x3 + 0.8
    x2 = -0.25x1 + 0.5x3 + 0.5
    x3 = -0.25x1 + 0.25x2 + 0.5
    
это из моего варианта

    -0.77x1 - 0.04x2 + 0.21x3 - 18x4 = -1.24
    0.25x1 - 1.23x2 + 0.16x3 - 0.09x4 = 1.12
    -0.21x1 + 0.16x2 + 0.8x3 - 0.13x4 = 2.56
    15x1 - 0.31x2 + 0.06x3 + 1.12x4 = -0.77
    
    next:
    18x4 = 1.24 - 0.77x1 - 0.04x2 + 0.21x3
    -1.23x2 = 1.12 - 0.25x1 - 0.16x3 + 0.09x4
    0.8x3 = 2.56 + 0.21x1 - 0.16x2 + 0.13x4
    15x1 = -0.77 + 0.31x2 - 0.06x3 - 1.12x4
    
    next:
    x1 = -0.046667 + 0.020667x2 -0.004x3 -0.074667x4
    x2 = -0.910569 + 0.203252x1 + 0.130081x3 -0.07317x4
    x3 = 3.2 + 0.2625x1 -0.2x2 + 0.1625x4
    x4 = 0.068889 -0.042778x1 -0.002222x2 + 0.011667x3
        
e = 0,0005
'''

m_size = 4

C = [
    [0, 0.020667, -0.004, -0.074667],
    [0.203252, 0, 0.130081, -0.07317],
    [0.2625, -0.2, 0, 0.1625],
    [-0.042778, -0.002222, 0.011667, 0]
]

d = [-0.051333, -0.910569, 3.2, 0.068889]

idk = []

for i in range(len(C)):
    summ = 0
    for j in range(len(C[i])):
        #print(f"{C[i][j]:>6.3f}", end=' ')
        summ += abs(C[i][j])
    #print()
    idk.append(summ)
    #round(summ, rounder)

#print(idk)

q = max(idk)
print(q)

x = [d]
delta = [1]

e = 0.0005

x.append(Add(Mul(C, x[0]), d))

k = 1

#deltaPart = q / (1 - q) * max([abs(x[1][i] - x[0][i]) for i in range(3)])
#print(q)

while True:
    delta.append(pow(q, k) / (1 - q) * max([abs(x[1][i] - x[0][i]) for i in range(m_size)]))

    if delta[k] <= e:
        break

    x.append(Add(Mul(C, x[k]), d))

    #deltaPart *= q

    k += 1


show_x(x)
show_delta(delta)
