#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',') # split line into parts

    county = columns[3]
    age_group = columns[5]

    print('{0}\t{1}'.format(county, age_group))