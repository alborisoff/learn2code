# -*- coding: utf-8 -*-

polygon = [[3, 2],
           [8, 7],
           [12, 8],
           [8, 12],
           [3, 10],
           [6, 7],
           [3, 2]]
point = [8, 10]


def bbox(poly):  # Получаем баунд-бокс обрезающего полигона
    xs, ys = [], []
    for poi in poly:
        xs.append(poi[0])
        ys.append(poi[1])
    return [min(xs), max(xs), min(ys), max(ys)]


def intersectwithnormal(normal, edge):  # Здесь частный случай: ребро полигона пересекается с перпендикуляром к оси OX.
    xe1, ye1, xe2, ye2 = edge[0][0], edge[0][1], edge[1][0], edge[1][1]
    xn1, yn1, xn2, yn2 = normal[0][0], normal[0][1], normal[1][0], normal[1][1]
    xintersect = xn1  # Очевидно, что точка пересечения с перпендикуляром к оси OX будет иметь абсциссу перпендикуляра.
    # Остаётся только найти ординату точки пересечения.
    k = (ye2 - ye1) / (xe2 - xe1)
    b = ye1 - k*xe1
    yintersect = k*xintersect + b
    return [xintersect, yintersect]


def intersects(poly, poi):
    ints = []
    normal = [[poi[0], bbox(poly)[2]], [poi[0], bbox(poly)[3]]]
    for i in range(len(poly) - 1):
        edge = [poly[i], poly[i + 1]]
        xe1, ye1, xe2, ye2 = edge[0][0], edge[0][1], edge[1][0], edge[1][1]
        xn1, yn1, xn2, yn2 = normal[0][0], normal[0][1], normal[1][0], normal[1][1]
        if min(xe1, xe2) <= xn1 <= max(xe1, xe2):
            ints.append(intersectwithnormal(normal, edge))
    return ints


print "Intersects:"
print intersects(polygon, point)
