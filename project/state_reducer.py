#!/usr/bin/python
import sys

states = {}

count = 0

for row in sys.stdin:
  row = row.strip()

  state, is_dead = row.split(':')

  try:
      states[state] += 1
  except KeyError:
      states[state] = 1

# print('{0}:{1}'.format("total_cases", total_cases))
print(states)
