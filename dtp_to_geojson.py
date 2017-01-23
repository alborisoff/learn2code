# -*- coding: utf-8 -*-

import json
import os


def one_crash_to_pre_geojson(onecrash):
    semantics = {}  # Заводим пустой словарь для семантики
    # onegeocrash --- это описание одного объекта в формате GeoJSON. В дальнейшем эти описания будут собраны в массив.
    onegeocrash = {"type": "Feature",
                   "geometry": {"type": "Point",
                                "coordinates": [onecrash["geo_code"]["longitude"],
                                                onecrash["geo_code"]["latitude"]]}}
    # Поля исходного JSON-файла, которые потом будут добавлены в семантику (features) объекта.
    semantic_items = [
                        "region_name",  # Субъект РФ
                        "place_path",  # Место происшествия
                        "em_moment_date",  # Дата происшествия
                        "em_moment_time",  # Время происшествия
                        "tr_area_state_name",  # Характер дорожного покрытия
                        "type",  # Тип ДТП
                        "light_type_name",  # Время суток
                        "num_of_vehicle",  # Количество транспортных средств
                        "num_of_victim",  # Суммарное количество пострадавших, если я правильно понимаю
                        "num_of_fatalities"  # Количество погибших
                     ]
    # Добавляем семантику в GeoJSON.
    for oneitem in semantic_items:  # Идём от одного поля исходного GeoJSON к другому.
        if oneitem in onecrash:  # Если это поле есть в исходном файле...
            semantics[oneitem] = onecrash[oneitem]  # ..., то добавляем его в GeoJSON.
        else:
            semantics[oneitem] = ''  # Иначе записываем в это поле пустое значение.
    onegeocrash["properties"] = semantics   # Записываем сформированную семантику в поле features.
    return onegeocrash  # Возвращаем готовое описание объекта в формате GeoJSON


def iterjson_to_geojson(filename):
    newfilename, extension = os.path.splitext(filename)  # Берём имя исходного JSON-файла...
    geojsonfilename = newfilename + '.geojson'  # ...и прибавляем к нему новое расширение.
    geojson_data = []  # Массив для данных GeoJSON (описаний отдельно взятых объектов).
    ready_geojson = {"type": "FeatureCollection"}  # Заводим словарь для итогового GeoJSON.
    with open(filename, 'r') as json_file:  # Открываем исходный файл.
        for onecrash in json_file:  # Идём по строкам.
            one_json_line = json.loads(onecrash)  # Каждую строку записываем как JSON-файл.
            one_geojson_line = one_crash_to_pre_geojson(one_json_line)  # Переводим этот JSON в формат GeoJSON.
            geojson_data.append(one_geojson_line)  # Добавляем в массив описаний объектов.
    ready_geojson["features"] = geojson_data  # Записываем полученный массив в поле features готового GeoJSON.
    with open(geojsonfilename, "w") as ready_file:
        json.dump(ready_geojson, ready_file)  # Сохраняем готовый GeoJSON в файл.
    return geojsonfilename  # Возвращаем имя готового GeoJSON.


# Пусть данный скрипт переводит в GeoJSON все JSON-файлы, которые находятся в той же папке, что и он сам.
for onejsonfile in os.listdir('.'):
    filename, extension = os.path.splitext(onejsonfile)
    if extension == '.json':
        try:
            iterjson_to_geojson(onejsonfile)
            print filename, 'конвертирован в', iterjson_to_geojson(onejsonfile)
        except:
            print 'Ой, что-то пошло не так...'
