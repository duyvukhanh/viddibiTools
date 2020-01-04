from fuzzywuzzy import fuzz


a = fuzz.ratio("bloodline","blood line")

print(type(a))