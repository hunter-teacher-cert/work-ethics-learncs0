
#create list of students in 701
students_701 = ["Giana", "Giana", "Giana", "Nia", "Nia", "Efrain", "Emely", "Joseph", "Samantha", "Leynin", "Kasey", "Elder", "Kevin", "Carlos", "Kennedi"]

#create scores
scores = [4, 4, 3, 3, 2, 2, 1, 1, 4, 4]

#-----------
#print length of list
print ("length of 701 student list")
print (len(students_701))
#output:  15
#-----------
#print list of students in 701
print ('names of students in original 701 class')
print(students_701)

#output:
#['Giana', 'Giana', 'Giana', 'Nia', 'Nia', 'Efrain', 'Emely', 'Joseph', 'Samantha', 'Leynin', 'Kasey', 'Elder', 'Kevin', 'Carlos', 'Kennedi']

#-----------
#count 
print("number of times Giana appears on roster")
print(students_701.count("Giana"))

#-----------
#access elements of list
print(students_701[-1])
print(students_701[0])
print(students_701[7:]) #element 7 and on
print(students_701[6:8]) #element range 6-7 not 8
#output
#Kennedi
#Efrain
#['Kevin', 'Carlos', 'Kennedi']
#['Elder', 'Kevin']

#-----------
#changing index value
students_701[0]="Sarai"
print(students_701[0]) 


#----------
#add item to end of the list
students_701.append("Jamyrie")
print(students_701)
#-----------
#insert new element at a specific location
students_701.insert(1, "Najm")
print('insert new element at a specific location index 1 Najm')
print(students_701)
#-----------
#remove an element
students_701.remove("Samantha")
print("student list with Samantha removed")
print(students_701)
#-----------
#check membership boolean
print ("Kennedi" in students_701)
print ("Wendi" in students_701)
#output 
#True
#False

#repetition
print (students_701 * 2)
#output
#['Efrain', 'Emely', 'Joseph', 'Samantha', 'Leynin', 'Kasey', 'Elder', 'Kevin', 'Carlos', 'Kennedi', 'Efrain', 'Emely', 'Joseph', 'Samantha', 'Leynin', 'Kasey', 'Elder', 'Kevin', 'Carlos', 'Kennedi', 'Efrain', 'Emely', 'Joseph', 'Samantha', 'Leynin', 'Kasey', 'Elder', 'Kevin', 'Carlos', 'Kennedi']'
#-----------
#concatenation
print(students_701 + [4,4,3,3,2,2,1,1,0,0]) 


#-----------
#add two lists together 
students_701.extend(scores)
print (students_701)
#output['Sarai', 'Emely', 'Joseph', 'Samantha', 'Leynin', 'Kasey', 'Elder', 'Kevin', 'Carlos', 'Kennedi', 4, 4, 3, 3, 2, 2, 1, 1, 4, 4]

#-----------
#locate index of an element
print('index for Leynin')
print(students_701.index("Leynin"))

print('index for score 4')
print(students_701.index(4))


#-----------
#remove last element with pop
#students_701.pop()
#-----------
#clear a list
students_701.clear()
print(students_701)
#output []