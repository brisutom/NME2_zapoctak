# uloha 61
def p(x):
    return p0 + k*x**2


def solve_diag(a, b, c, f):
    n = len(f)

    for i in range(1, n):
        mm = a[i-1]/b[i-1]
        b[i] = b[i] - mm*c[i-1]
        f[i] = f[i] - mm*f[i-1]

    x = n*[0]
    x[-1] = f[-1]/b[-1]

    for j in range(n-2, -1, -1):
        x[j] = (f[j] - c[j]*x[j+1])/b[j]

    return x


def build_matrix():
    h = L/m
    b = (m+1)*[0]
    a = m*[0]
    c = m*[0]
    b[0] = 1
    b[m] = 1
    a[m-1] = 0
    c[0] = 0

    for i in range(1, m):
        b[i] = (p(i*h) + p((i+1)*h))/h**2
        c[i] = -p((i + 1) * h) / h ** 2

    for j in range(0, m-1):
        a[j] = -p((j+1)*h)/h**2

    return [a, b, c]


print("Uloha 61: (p(x)*y')' = 0")
print("y(0) = 0,\ty(L) = y0")
print("p(x) = p0 + k*x^2,\tp0, k > 0\n\n")

try:
    L = float(input("Zadejte prosim hodnotu L: "))
    y0 = float(input("Zadejte prosim hodnotu y0: "))
    p0 = float(input("Zadejte prosim hodnotu p0: "))
    assert(p0 > 0)
    k = float(input("Zadejte prosim hodnotu k: "))
    assert(k > 0)
    m = int(input("Zadejte prosim pocet kroku: "))
except Exception:
    print("Spatny vstup. Pouziji se vychozi hodnoty.")
    L = 1
    y0 = 1
    p0 = 1
    k = 1
    m = 100

[a, b, c] = build_matrix()

f = (m+1)*[0]
f[0] = 0
f[m] = y0

result = solve_diag(a, b, c, f)

with open('result.txt', 'w') as f:
    f.write("#x y\n")
    for i, value in enumerate(result):
        point = i*(L/m)
        f.write(str(point) + " " + str(value) + "\n")

print("\nVystup zapsan do souboru result.txt")
