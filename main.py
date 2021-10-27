import time
from numpy import linalg as LA
from math import sqrt


tv = []
klass_o = []
klass_g = []
klass_t = []
klass_r = []
tvec = []
with open("klass_o.txt") as t:
    tv = t.readlines()
for i in tv:
    ip = i.split()
    isp = []
    for k in ip:
        isp.append(int(k))
    klass_o.append(isp)
tv = []
with open("klass_g.txt") as t:
    tv = t.readlines()
for i in tv:
    ip = i.split()
    isp = []
    for k in ip:
        isp.append(int(k))
    klass_g.append(isp)
tv = []
with open("klass_t.txt") as t:
    tv = t.readlines()
for i in tv:
    ip = i.split()
    isp = []
    for k in ip:
        isp.append(int(k))
    klass_t.append(isp)
tv = []
with open("klass_r.txt") as t:
    tv = t.readlines()
for i in tv:
    ip = i.split()
    isp = []
    for k in ip:
        isp.append(int(k))
    klass_r.append(isp)
tv = []
with open("vvod.txt") as t:
    tv = t.readlines()
for i in tv:
    ip = i.split()
    isp = []
    for k in ip:
        isp.append(int(k))
    tvec.append(isp)


def yadro(el):
    y = []
    for i in range(len(el[0])):
        t = 0
        for j in el:
            t += j[i]
        t = t/len(el)
        y.append(t)
    return y


def prib_odin(ma):
    for i in range(len(ma)):
        ma[i][i] += 1
    return ma


def matriza_kovariazii(el):
    ya = yadro(el)
    m = []
    for i in range(len(el[0])):
        mm = []
        for k in range(len(el[0])):
            t = 0
            for j in el:
                t += (j[i] - ya[i])*(j[k] - ya[k])
            # ts = f"{t}/{(len(el) - 1)}"
            ts = t / (len(el) - 1)
            mm.append(ts)
        m.append(mm)
    return m


def matrix_umn(m1, m2):
    str1 = len(m1)
    stol1 = len(m1[0])
    str2 = len(m2)
    stol2 = len(m2[0])
    if stol1 != str2:
        print("Матрицы нельзя перемножить.")
        return
    mm = []
    for i in range(str1):
        m = []
        for j in range(stol2):
            s = 0
            for t in range(stol1):
                s += m1[i][t] * m2[t][j]
            m.append(s)
        mm.append(m)
    if str1 != len(mm) or stol2 != len(mm[0]):
        return "Что-то пошло не так."
    return mm


def transponirovaniye(ma):
    str1 = len(ma)
    stol1 = len(ma[0])
    mm = []
    for i in range(stol1):
        m = []
        for j in range(str1):
            m.append(ma[j][i])
        mm.append(m)
    return mm


def obratnaya_matriza(ma):
    return LA.inv(ma)


def evklid_mahalanobis(ya, makov, v):
    mkovo  = prib_odin(makov)
    obrmk = LA.inv(mkovo)
    for i in range(len(v[0])):
        v[0][i] = v[0][i] - ya[i]
    vtrans = transponirovaniye(v)
    proms = matrix_umn(v, obrmk)
    s = matrix_umn(proms, vtrans)
    otvet = s[0][0]
    otvet = sqrt(otvet)
    return otvet


def cicl_s_odnim_obrazom(obr):
    yao = yadro(klass_o)
    yag = yadro(klass_g)
    yat = yadro(klass_t)
    yar = yadro(klass_r)
    mk_o = matriza_kovariazii(klass_o)
    mk_g = matriza_kovariazii(klass_g)
    mk_t = matriza_kovariazii(klass_t)
    mk_r = matriza_kovariazii(klass_r)
    e_m = []
    e_m.append(evklid_mahalanobis(yao, mk_o, obr))
    e_m.append(evklid_mahalanobis(yag, mk_g, obr))
    e_m.append(evklid_mahalanobis(yat, mk_t, obr))
    e_m.append(evklid_mahalanobis(yar, mk_r, obr))
    print(e_m)
    if e_m[0] < 2:
        return "Это класс O"
    if e_m[1] < 7:
        return "Это класс Г)"
    if e_m[3] < 14.2:
        return "Это клас Р"
    if 9.8 < e_m[2] < 11:
        return "Это класс Т"
    return