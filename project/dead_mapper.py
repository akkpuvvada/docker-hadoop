#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',') # split line into parts

    age_group = columns[5]
    # 17
    dead = columns[17]

    print('{0}:{1}'.format(age_group, dead))
    