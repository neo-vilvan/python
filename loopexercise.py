#for loop

for i in range(1, 11):
    print(i)


#while loop

i = 0
while i <= 10:
    print(i)
    i += 2

#for loop
names = ['Alice', 'Bob', 'Charlie', 'Dave']
for name in names:
    print(f"Hello, {name}")

#while loop
num = 0
while num < 1 or num >10:
    num = int(input("Enter a number between 1 and 10: "))


string = "Hello World"
vowels = 0
for char in string:
    if char in "aeiouAEIOU":
        vowels += 1
print(f"There are {vowels} vowels in the string.")