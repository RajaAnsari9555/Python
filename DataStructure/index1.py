#List
#Ordered Collection
#changable
#allowed Duplicates

number = [10 ,20 ,30 ,40 , 60]
number.append(70)
number.remove(20)
print(number[3])
 
sum = 0 

for i in number:
   sum += i
   print(sum)


#Tuple
# ordered
# unmutable
#faster than list

data = (1 ,2 ,3)
print(data[1])


#Set
#unordered
#don,t allowed duplicate
#fast operation

s = {1,2,3,5,2}
s.add(6)
s.remove(3)
print(s)


#dictionary
#stored key value pair
student = {
   "name":"raja",
   "age":12
}

#access
print(student["name"])

#add/update
student["age"] = 21

print(student)

#loop
for key , value in student.items():
   print(key , value)