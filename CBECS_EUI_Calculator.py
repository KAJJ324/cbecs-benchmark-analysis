# EUI Rankings by Building Type — National Benchmark Analysis
# Source data: U.S. EIA Commercial Buildings Energy Consumption Survey (CBECS), 2018
# Table C12: Sum of major fuel consumption totals and gross energy intensities
# Reads C12 data exported as CSV, extracts 14 main building category EUI values,
# ranks categories from most to least energy intensive, and flags those exceeding
# the national average of 70.4 kBtu/sq ft.
# Demonstrates: csv module, flag variables, duplicate guarding, try/except, sorting by value

import csv

main_categories = [
    'All buildings',
    'Education',
    'Food sales',
    'Food service',
    'Health care',
    'Lodging',
    'Mercantile',
    'Office',
    'Public assembly',
    'Public order and safety',
    'Religious worship',
    'Service',
    'Warehouse and storage',
    'Other',
    'Vacant'
]

fname = input("Enter file name: ")
fh = open(fname)
reader = csv.reader(fh)
eui_data = dict()
data_started = False

for row in reader:
    if row[0].strip() == 'All buildings':
        data_started = True
    if not data_started:
        continue
    name = row[0].strip()
    if name not in main_categories:
        continue
    if name in eui_data:
        continue
    try:
        eui = float(row[6])
    except:
        continue
    eui_data[name] = eui

national_avg = eui_data.pop('All buildings')

sorted_results = sorted(eui_data.items(), key=lambda x: x[1], reverse=True)
#for name, eui in sorted_results:
    #print(name, eui)

print(f"{'Rank':<6} {'Building Type':<35} {'EUI (kBtu/sq ft)':>16}")
print("-" * 60)
for rank, (name, eui) in enumerate(sorted_results, 1):
    if eui > national_avg:
        print(f"{rank:<6} *** {name:<31} {round(eui, 1):>16}")
    else:
        print(f"{rank:<6}     {name:<31} {round(eui, 1):>16}")
print("-" * 60)
print(f"National benchmark (All buildings): {round(national_avg, 1)}")