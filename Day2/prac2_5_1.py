"""
x = float(input("Enter value for x: "))

y = 1/(x+(1/(x+1/(x+1/x))))

print("y =", y)
"""

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

""""
use floor division, modulo, 
"""
# convert everything to mins
total_mins = hour * 60 + mins + dura
hour_end = (total_mins // 60) % 12
mins_end = total_mins % 60

# display in 12 hour format
end_time = (f"{hour_end:02d}:{mins_end:02d}")
print(end_time)
