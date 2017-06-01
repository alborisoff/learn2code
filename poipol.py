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

def intersect(segment1, segment2):  # Координаты пересечения двух прямых, проходящих через две точки каждая

    x11 = segment1[0][0]
    y11 = segment1[0][1]
    x12 = segment1[1][0]
    y12 = segment1[1][1]

    x21 = segment2[0][0]
    y21 = segment2[0][1]
    x22 = segment2[1][0]
    y22 = segment2[1][1]

    a1 = y11 - y12
    b1 = x12 - x11
    c1 = x11*y12 - x12*y11

    a2 = y21 - y22
    b2 = x22 - x21
    c2 = x21*y22 - x22*y21

    y = (a2*c1 - a1*c2) / (a1*b2 - a2*b1)
    x = (-c1 - b1*y) / a1

    return x, y

arra = [[0, 0],
        [10, 2],
        [1, 1],
        [100, 0],
        [50, 1000]]

print gabarits(arra)
