def litres_100km_to_miles_gallon(litres):
    litres = 235.215 / litres
    return litres


def miles_gallon_to_litres_100km(miles):
    miles = 235.215 / miles
    return miles

print(litres_100km_to_miles_gallon(3.9))
print(litres_100km_to_miles_gallon(7.5))
print(litres_100km_to_miles_gallon(10.0))
print(miles_gallon_to_litres_100km(60.3))
print(miles_gallon_to_litres_100km(31.4))
print(miles_gallon_to_litres_100km(23.5))
