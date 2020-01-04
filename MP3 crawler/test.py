from fuzzywuzzy import fuzz


a = "Bandera - topic"
b = "Bandera"

c = fuzz.ratio(b,a)
print(c)