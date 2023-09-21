beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(beatles)

for i in range(2):
    member_name = input("Enter name: ")
    beatles.append(member_name)

print(beatles)

del beatles[4], beatles[3]


print(beatles)

beatles.insert(0, "Ringo Starr")
print(beatles)
