
#ODD  INDEX CHAR
name = "maharastra"
print(name[1:11:2])

#PRINT VOWEL
str="samiksha"
for i in str:
    if i=="a"or i=="e"or i=="i"or i=="o"or i=="u":
        print(i)

#EVEN,ODD  CHAR COUNT
name = "samiksha"

even_count = len(name[0::2])
odd_count = len(name[1::2])

print("Even position count =", even_count)
print("Odd position count =", odd_count)

#REVERSE WITHOUT SLICING
new="Arya"
rev=""
for i in new:
    rev=i+rev
print(rev)

#PALINDROM
new="level"
rev=""
for i in new:
    rev=i+rev
if rev==new:
    print("palindrom")
else:
    print("not palindrom")



