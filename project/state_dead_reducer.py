#!/usr/bin/python
import sys

states = {}

count = 0

for row in sys.stdin:
  row = row.strip()

  state, is_dead = row.split(':')

  if is_dead.lower().strip() == "yes":
    try:
      states[state] += 1
    except KeyError:
      states[state] = 1

print(states)
