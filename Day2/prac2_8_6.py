blocks = int(input("Enter the number of blocks: "))
height = 0
blocks_used = 0

# blocks_used + height + 1 == total blocks used it another layer is added
while (blocks_used + height + 1 <= blocks):
    height += 1  # adds another layer
    blocks_used += height  # updates blocks used to account for another layer added

print(f"Blocks used: {blocks_used}")
print(f"The height of the pyramind is {height} layers")
