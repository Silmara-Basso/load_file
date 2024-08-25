import csv

path_to_file: str = "files/products.csv"

file_csv: list = []

with open(file=path_to_file, mode="r", encoding='utf-8') as mfile:
    dfile = csv.DictReader(mfile)

    for row in dfile:
        file_csv.append(row)

print(file_csv)

