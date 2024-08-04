# pt1
a = "This is  question 1"
print (a)

# pt2
b = "This is  question 2"
print (b)
c =  "This is  question 2 but changed"
print(c)

# pt3
name: str = "Wasay"
print("Hello" + " " + name + " would you like to learn some Python today?")

# pt4
lowercase_name = name.lower()
print(lowercase_name)
uppercase_name = name.upper()
print(uppercase_name)
titlecase_name = name.title()
print(titlecase_name)

# pt5
quote : str = "When you pray for rain you gotta deal with the mud too."
author : str = "Robert McCall"
print(author + " once said, " + quote )

# pt6
message : str = "Those people who show no mercy will receive no mercy from Allah."
famous_person : str = "Prophet(PBUH)"
print(message + " " + famous_person )

# pt7
person_name : str = "!John-"
stripped_name = person_name.strip("!")
print(stripped_name, end=" ")
lstripped_name = person_name.lstrip("\t")
print(lstripped_name, end=" ")
rstripped_name = person_name.rstrip("-")
print(rstripped_name)

# pt8
num1 = 5
num2 = 10
num3 = 15
print(num1 + num2 + num3)

# pt9
num4 = 2
num5 = 6
temp = None
print ("Before Swap")
print("num4 = " + str(num4) + "\tnum5 = " +str(num5))
temp = num4
num4 = num5
num5 = temp

print("After Swap")
print("num4 = " + str(num4) + "\tnum5 = " + str(num5))

# pt10
fav_color : str = "Yellow"
newfav_color = fav_color
del fav_color
print(newfav_color)

# pt11
pet_name : str = "Buddy"
# pet_name : str = "Max"
print(pet_name)

# pt12
var1 : str = "Sunshine"
print(var1)
# print(sunsine)

# pt13
score = 100 
print(score, end=" ")
score = 87
print(score)

# pt14
city : str = "New-York"
print(city)

# pt15
text : str = "pyThon proGramming"
titlecase_text = text.title()
print(titlecase_text)

# pt16
lowercase_text = text.lower()
print(lowercase_text)

# pt17
uppercase_text = text.upper()
print(uppercase_text)

# pt18
temperature = 25
print("The current temperature is " + str(temperature)+ " degrees")

# pt19
poem : str = '"Two roads diverged in a yellow wood, \nAnd sorry I could not travel both \nAnd be one traveler, long I stood \nAnd looked down one as far as I could \nTo where it bent in the undergrowth"'
print(poem)