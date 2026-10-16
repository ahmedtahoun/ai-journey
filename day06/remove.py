list = ["red", "green", "Blue", "Yellow"]
print(list)
num = int(input("How many items you want to remove? "))
index = num - 1 
remove_item = list.pop(index)

print(f"removed: {remove_item}")
print(f"remaining: {list}")

