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
# check palindrome
n = "aia"
rev_n =""
for pal in n:
    rev_n = pal+rev_n
print(rev_n)
if rev_n == n:
    print(f"{n} was a palindrome")

# average of list numbers
num = [10,20,30,40]
total = 0
for n in num:
    total = total + n
avg = total / len(num)
print(int(avg))

# Merg & Short list 
list1 = [1,2,3,10,4,5]
list2 = [5,6,7,8,9]
list3 = list1 + list2
list3.sort()
print(list3)

