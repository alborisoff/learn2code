# -*- coding: utf-8 -*-

import json
import os

def jsontogeojson(filename):
    geojson_crashes = []  # Объявляем массив для данных GeoJSON
    json_crashes = json.loads(open(filename).read())  # Переменная для исходного JSON-файла
    newfilename, extension = os.path.splitext(filename)  # Берём имя исходного файла...
    geojsonfilename = newfilename + '.geojson'  # ...и прибавляем к нему новое расширение.
    summary = {}  # Словарь для итогового GeoJSON-файла
    for onecrash in json_crashes:  # Идём по исходному JSON-файлу, от происшествия к происшествию...
        onegeocrash = {}  # Заводим словарь для одного GeoJSON-описания ДТП
        properties = {}  # Заводим словарь для семантики
        # Массив полей семантики, которые есть в исходном JSON и будут переведены в GeoJSON.
        # Переведены будут не все поля.
        items = [
            "region_name",         # Субъект РФ
            "place_path",          # Место происшествия
            "em_moment_date",      # Дата происшествия
            "em_moment_time",      # Время происшествия
            "tr_area_state_name",  # Характер дорожного покрытия
            "type",                # Тип ДТП
            "light_type_name",     # Время суток
            "num_of_vehicle",      # Количество транспортных средств
            "num_of_victim",       # Суммарное количество пострадавших, если я правильно понимаю
            "num_of_fatalities"    # Количество погибших
                 ]
        onegeocrash["type"] = "Feature"
        # Переводим координаты из JSON в GeoJSON
        onegeocrash["geometry"] = {"type": "Point",
                                   "coordinates": [onecrash["geo_code"]["longitude"], onecrash["geo_code"]["latitude"]]}
        # Переводим семантику в GeoJSON
        for oneitem in items:
            if oneitem in onecrash:  # Если это поле имеется в исходном JSON...
                properties[oneitem] = onecrash[oneitem]  # ..., то добавляем его в наш GeoJSON с имеющимся значением...
            else:
                properties[oneitem] = ""  # ...иначе оставляем это поле незаполненным.
        onegeocrash["properties"] = properties  # Заполняем ключ-значение для семантики
        geojson_crashes.append(onegeocrash)  # Добавляем итоговое конвертированное происшествие в массив происшествий
        # Формируем необходимые ключи-значения для итогового файла
        summary["type"] = "FeatureCollection"
        summary["features"] = geojson_crashes
    # Сохраняем итоговый GeoJSON в файл
    with open(geojsonfilename, "w") as ready_geojson:
        json.dump(summary, ready_geojson)
    return geojsonfilename

filename = "crash_region_code_1124.json"
print jsontogeojson(filename)
