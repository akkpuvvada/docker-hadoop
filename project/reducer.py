#!/usr/bin/python
import sys

age_group = {}
total_cases = 0

for row in sys.stdin:
  row = row.strip()
  # Get total number of cases
  total_cases += 1
  # splitting
  county, age = row.split('\t')
  try:
      age_group[age] += 1
  except KeyError:
      age_group[age] = 1

print('{0}:{1}'.format("total_cases", total_cases))
print('{0}:{1}'.format("0 - 17 years", age_group["0 - 17 years"]))
print('{0}:{1}'.format("18 to 49 years", age_group["18 to 49 years"]))
print('{0}:{1}'.format("50 to 64 years", age_group["50 to 64 years"]))
print('{0}:{1}'.format("65+ years", age_group["65+ years"]))
print('{0}:{1}'.format("Missing", int(age_group["Missing"])+int(age_group["NA"])))
