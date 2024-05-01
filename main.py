R = [10, 20, 50, 100]
I = [100, 250, 500, 1000]


def read_AB():
    A = []
    B = []
    with open('rules.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            values = line.split()
            if (values[0][0] == 'A'):
                arr = []
                for i in range(1, len(values)):
                    arr.append(float(values[i]))
                A.append(arr)
            if (values[0][0] == 'B'):
                arr = []
                for i in range(1, len(values)):
                    arr.append(float(values[i]))
                B.append(arr)
    return [A, B]


def implication(A, B):
    R = []
    for a in A:
        row = []
        for b in B:
            if (b < a):
                row.append(b)
            else:
                row.append(a)
        R.append(row)
    return R


def minmax(A, R):
    m = len(A)
    n = len(R)
    k = len(R[0])
    c = [[None for __ in range(k)] for __ in range(m)]
    for i in range(m):
        for j in range(k):
            c[i][j] = max(min(A[i][kk], R[kk][j]) for kk in range(n))
    return c


def maxR(R):
    Rm = [[None for __ in range(4)] for __ in range(4)]
    for i in range(4):
        for u in range(4):
            Rm[i][u] = max([c[i] for c in [[j[u] for j in x] for x in R]])

    return Rm


Ai = [[float(a) for a in input("A': ").split()]]


def search_alpha(Ai, A):
    alpha_array = []
    for i in range(len(A)):
        alpha_array.append(min(Ai[i], A[i]))
    return max(alpha_array)


A = read_AB()[0]
B = read_AB()[1]

R = [implication(A[i], B[i]) for i in range(4)]

print()
for i in range(len(R)):
    print(f"R{i + 1}:")
    for j in R[i]:
        print(j)
    print()

Bi = [minmax(Ai, R[i])[0] for i in range(4)]
Br1 = [max([x[i] for x in Bi]) for i in range(4)]  # 1 метод

print("1 метод: ")
print("B' = " + ' + '.join([f"{I[i]}/{Br1[i]}" for i in range(len(Br1))]))
print()

Rm = maxR(R)
Br2 = minmax(Ai, Rm)  # 2 метод
print("2 метод: ")
print("B' = " + ' + '.join([f"{I[i]}/{Br2[0][i]}" for i in range(len(Br2[0]))]))
print()

alpha = []
for a in A:
    alpha.append(search_alpha(Ai[0], a))

Bi1 = []
for i in range(len(alpha)):
    Bi1.append([[min(k, alpha[i]) for k in b] for b in B][i])

Br3 = [max([x[i] for x in Bi1]) for i in range(4)]
print("3 метод: ")
print("B' = " + ' + '.join([f"{I[i]}/{Br3[i]}" for i in range(len(Br3))]))
print()
