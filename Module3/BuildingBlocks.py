blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
height = 0
blocks_used = 0

while blocks_used + height + 1 <= blocks:
    height += 1
    blocks_used += height

#

print("The height of the pyramid:", height)