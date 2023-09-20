temperatures_day1_day30 = [25, 20, 21, 26, 23, 22, 18,
                           27, 28, 30, 31, 33, 34, 36, 36, 37, 38, 40, 39, 37, 35,
                           34, 32, 31, 30, 28, 26, 21, 23, 24]

temp_first7 = temperatures_day1_day30[0:7]

max = temp_first7[0]
for i in temp_first7:
    if i > max:
        max = i

print(f"WEEK 1 TEMPS: {temp_first7}")
print(f"WEEK 1 max: {max}")

temp_last5 = temperatures_day1_day30[25:30]
print(temp_last5)

min = temp_last5[0]
for i in temp_last5:
    if i < min:
        min = i

print(f"WEEK last TEMPS: {temp_first7}")
print(f"WEEK last min: {min}")

temp_alt = temperatures_day1_day30[::2]

sum = 0

for i in temp_alt:
    sum += i

average = sum / len(temp_alt)

print(f"ALTERNATE AVG TEMP: {average:.2f}")
