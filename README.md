cbecs-eui-ranking

Ranks U.S. commercial building types by Energy Use Intensity using 2018 EIA CBECS data

What it does

Reads the EIA's 2018 Commercial Buildings Energy Consumption Survey (CBECS) Table C12, extracts Energy Use Intensity (EUI) values for 14 main commercial building categories, and produces a ranked report comparing each category to the national benchmark of 70.4 kBtu/sq ft.

Input

Table C12 from the 2018 CBECS, exported as CSV from the EIA website. Contains aggregated EUI data across thousands of real U.S. commercial buildings.

Output

A ranked report showing all 14 building categories from most to least energy intensive, with categories exceeding the national average flagged with ***.

Concepts demonstrated

csv module, flag variables for header navigation, dictionary duplicate guarding, try/except for withheld data (Q values), sorting by value with lambda, f-string formatting, enumerate for rank numbering

Data source

U.S. Energy Information Administration — 2018 Commercial Buildings Energy Consumption Survey
https://www.eia.gov/consumption/commercial/data/2018/
