# code to check vowel
count = 0
a = "arif"
for vow in a:
    if vow == "a" or vow == "e" or vow == "i" or vow == "o" or vow == "u":
         count += 1

print(f"{a} has {count} vowel")  

# code to find the number x
x = 25
indx = 0
numbers =[1,2,25,35,70,18,74,25]
for num in numbers :
    if num == x:
        print(f"the number at indx no {indx}")
        break
    indx += 1
                