scores = [85, 92, 78, 90, 88, 76, 94, 89]

print("Original scores:", scores)

for i in range(0, len(scores)):
    for j in range(i, len(scores)):
        if scores[i] >= scores[j]:
            scores[i], scores[j] = scores[j], scores[i]

print("Sorted scores (ascending order):", scores)
