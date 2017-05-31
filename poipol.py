# -*- coding: utf-8 -*-

def  gabarits(arrofpoints):

    # Получив на входе массив углов многоугольника, выдаём координаты габаритного прямоугольника,
    # в который вписан входной многоугольник.
    # Массив точек имеет вид [[x1, y1], [x2, y2], ...,  [[xn, yn]]]
    # Очевидно, что нам нужно найти как минимальные, так и максимальные x и y.
    minx = 0
    maxx = arrofpoints[0][0]
    miny = 0
    maxy = arrofpoints[0][1]
    for i in range(0, len(arrofpoints)):
        for j in range(i, len(arrofpoints)):
            if minx > arrofpoints[j][0]:
                minx = arrofpoints[j][0]
            if maxx < arrofpoints[j][0]:
                maxx = arrofpoints[j][0]
            if miny > arrofpoints[j][1]:
                miny = arrofpoints[j][1]
            if maxy < arrofpoints[j][1]:
                maxy = arrofpoints[j][1]
    return minx, maxx, miny, maxy

arra = [[0, 0],
        [10, 2],
        [1, 1],
        [100, 0],
        [50, 1000]]

print gabarits(arra)
