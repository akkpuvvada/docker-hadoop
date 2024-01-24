#!/usr/bin/python
import sys

age_group = {
  "no_of_deaths": 0,
  "18 to 49 years":0,
  "65+ years":0,
  "0 - 17 years":0
}

total_cases = 0
county = ""
count = 0

for row in sys.stdin:
  row = row.strip()

  age_range, is_dead = row.split(':')

  # Get total number of dead people
  if is_dead.lower().strip() == "yes":
    age_group["no_of_deaths"] += 1
    try:
        age_group[age_range] += 1
    except KeyError:
        age_group[age_range] = 1

print("Total number of deaths", age_group["no_of_deaths"])
print("deaths of people between 0 - 17 years", age_group["0 - 17 years"])
print("deaths of people between 18 to 49 years", age_group["18 to 49 years"])
print("deaths of people between 50 to 64 years", age_group["50 to 64 years"])
print("deaths of people between 65+ years", age_group["65+ years"])
print("missing data", int(age_group["Missing"]) + int(age_group["NA"]))
