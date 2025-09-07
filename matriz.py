import numpy as np 

class Matriz:
    def __init__(self, m):
        ma = []
        for i in m:
            mc = []
            for j in i:
                mc.append(j)
            ma.append(mc)
        self.val = ma
    
    def ToString(self):
        ms, c = "", 1
        for i in self.val:
            for j in i:
                ms += str(j)
                ms += " "
            if(c < len(self.val)):
                ms += '\n'
            c+=1
        return ms
    
    def __add__(self, m):
        a, m, ans = self.val, m.val, []

        for i in range(len(a)):
            pa = []
            for j in range(len(a[i])):
                pa.append(a[i][j] + m[i][j])
            ans.append(pa)
        
        return Matriz(ans)
    
    def __sub__(self, m):
        a, m, ans = self.val, m.val, []

        for i in range(len(a)):
            pa = []
            for j in range(len(a[i])):
                pa.append(a[i][j] - m[i][j])
            ans.append(pa)
        
        return Matriz(ans)

    def __mul__(self, m):
        a, m, ans = self.val, m.val, []
        aLen, mLen = len(a), len(m)

        for i in range(aLen):
            pa = []
            for j in range(len(a[i])):
                t = 0
                for k in range(mLen):
                    t += a[i][k] * m[k][j]
                pa.append(t)
            ans.append(pa)

        return Matriz(ans)

    def Comparar(self, m):
        a, b, ans = self.val, m.val, 0
        ma, mb = np.array(a), np.array(b)
        da, db = np.linalg.det(ma), np.linalg.det(mb)

        if abs(da) < 1e-10: da = 0
        if abs(db) < 1e-10: db = 0

        if da == db: ans = "Igual"
        elif da > db: ans = "Mayor"
        else: ans = "Menor"
    
        return ans

    def Traza(self):
        m, ans = self.val, 0

        for i in range(len(m)):
            ans += m[i][i]

        return ans

    def Transpuesta(self):
        m = self.val
        a = []

        for i in range(len(m)):
            pa = []
            for j in range(len(m[i])):
                pa.append(m[j][i])
            a.append(pa)

        return Matriz(a)

    def esSimetrica(self):
        m = self.val
        mt = self.Transpuesta()

        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] != mt.val[i][j]:
                    return False

        return True
    
    def Ceros(self):
        m = self.val
        a = []

        for i in m:
            a.append(i.copy())

        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == 0:
                    for k in range(len(m)):
                        a[k][j] = 0
                    for l in range(len(m[i])):
                        a[i][l] = 0

        return Matriz(a)
    
    

m1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

m2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

mt1 = Matriz(m1)
mt2 = Matriz(m2)

#1
print(mt1.ToString())
#2
mt3 = mt1 + mt2
print(mt3.ToString())
#3
mt4 = mt1 - mt2
print(mt4.ToString())
#4
mt5 = mt1 * mt2
print(mt5.ToString())
#5 (Este tipo de comparacion se realiza bajo el determinante de la matriz, no elemento a elemento)
print(mt1.Comparar(mt2))
#6
print(mt1.Traza())
#7
mt6 = mt1.Transpuesta()
print(mt6.ToString())
#8
print(mt1.esSimetrica())
#9
mt7 = Matriz([[1, 2, 0],
              [4, 5, 6],
              [7, 0, 9]])
mt8 = mt7.Ceros()
print(mt8.ToString())