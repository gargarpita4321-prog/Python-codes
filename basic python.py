# Take a user's name and city as input, then print: `"Hello <name>, welcome from <city>!"

name=input("Enter your name: ")
city=input("Enter your city: ")
print(f"Hello {name}, welcome from {city}!"
)

# Take the radius of a circle as input (as a float) and print its area (`π × r²`). Use `3.14159` for π.

r=float(input("Enter radius: "))
π=3.14159
area=(π*(r**2))
print(area)


# Ask the user for their birth year and print their approximate current age (assume current year is 2026).

birth_year= int(input("enter your birth year: "))
age=2026-birth_year
print(age)

# Ask the user to enter three subject marks, convert them to integers, and print their total and average.
Sub_1=int(input("enter subject marks: "))
Sub_2=int(input("enter subject marks: "))
Sub_3=int(input("enter subject marks: "))
total= Sub_1+Sub_2+Sub_3
average= total/3
print(total,average)

# Take a number as input and print whether it is positive, negative, or zero (using `if-elif-else`).

number=float(input("enter number: "))

if(number>0):
    status="positive"
elif(number==0):
    status="zero"
else:
    status="negative"

print(status)

# Take a sentence as input and print it in uppercase, then in lowercase.
sentence=input("type sentence: ")
print(sentence.lower())
print(sentence.upper())

# Ask the user for a word and check (using `in`) whether the letter `"a"` appears in it.
word=input("enter word: ")
print("a" in word)

# Take a full name as input(e.g., `"Tony Stark"`) and replace the last name with `"Rogers"` using `.replace()`.

name="Tony Stark"

print(name.replace("Stark","Rogers"))
