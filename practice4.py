cricketers=["Virat","Rahul","Yuzi","Dravid","Bhumrah"]
            #0        1       2

            #-3         -2        -1
print(cricketers[0])
print(cricketers[-2])
print(cricketers[1:3])

cricketers[2] ="rohit"
print(cricketers)

heroes=["Raj","sudeep","rakshith","rishab","vijay","Roopesh"]
#       0       1        2            3

heroes.append("RAJ b")
print(heroes)

heroes.insert(2,"vinod")
print(heroes)

heroes.remove("Raj")
print(heroes)

#heroes.clear()
#print(heroes)

heroes.pop()  # removes last element
heroes.pop()
print(heroes)


print(heroes.index("vinod"))

print("BVC" in heroes)

print(heroes.count("vinod"))

heroes.sort()
print(heroes)

numbers=[3,6,1,2,7,8,4,5,]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers_copy=numbers.copy
print(numbers_copy)

heroes.extend(numbers)
print(heroes)