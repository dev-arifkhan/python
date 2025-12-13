# code to check vowel
count = 0
a = input("Enter a text: ").lower()
for vow in a:
    if vow == "a" or vow == "e" or vow == "i" or vow == "o" or vow == "u":
         count += 1

print(f"{a} has {count} vowel")  

# hi.
     