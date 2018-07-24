number = 0
while number<=10:
    print("The Numbers are ",number)
    number+=1

while number>10 and number<=20:
    print(number)
    number+=1

for characters in "Python":
    print(characters)

for names in ["King","Dan","Brio","Lesson"]:
    print(names)

fruits = ["Mango","Orange","Avocado","Pineapple","Juice"]
for fruit in fruits:
    if len(fruit) == 5:
        print(fruit)
