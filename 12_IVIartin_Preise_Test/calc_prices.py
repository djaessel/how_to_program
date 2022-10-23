#!/bin/python


def strToFloatFix(fStr):
    return float(fStr.replace(',', '.'))


def floatToStrFix(fStr):
    return str(fStr).replace('.', ',')


def calc(csv_data):
    length = len(csv_data)
    for i in range(1, length):
        data = csv_data[i]
        ek = strToFloatFix(data[1])
        new_vk = ek * 3

        uvp = strToFloatFix(data[3])
        if (uvp > new_vk):
            new_vk = uvp

        data[2] = floatToStrFix(new_vk)
        csv_data[i] = data

    return csv_data


def readCsvData(filepath):
    dataLen = 123
    csv_data = []
    with open(filepath, "r") as fcsv:
        while dataLen > 1:
            data = fcsv.readline().split(';')
            dataLen = len(data)
            if dataLen > 1:
                csv_data.append(data)

    return csv_data


def writeCsvData(filepath, csv_data):
    with open(filepath.split('.')[0] + "_new.csv", "w") as fout:
        for data in csv_data:
            fout.write(data[0] + ";" + data[1] + ";" + data[2] + ";" + data[3])


import sys

file_path = "test.csv"

argc = len(sys.argv)
if argc > 1:
    file_path = sys.argv[1]


csv = readCsvData(file_path)
csv = calc(csv)
writeCsvData(file_path, csv)

