#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',')

    state = columns[1]
    is_dead = columns[17]

    print('{0}:{1}'.format(state, is_dead))