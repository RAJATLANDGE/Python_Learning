# list define
# l1 = []
# l1 = list()
# l1 = ['element', 'element', 'element', 'element', 'element', 'element', 'element', 'element']

student_marks = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 85]


print("student marks =", student_marks)

# append = add something in the list at the end.
student_marks.append(95)
print("after append =", student_marks)

# extend = add entity or list which merge with existing
student_marks.extend(["hundred", "fifty", "sixty"])
print("extended list =", student_marks)
digital_marks = [789, 456, 123]
# student_marks = student_marks + digital_marks #----------- this is also method for adding element in list.
# student_marks[5] = 500 #--------- replace exiting no with  500 at 5th index.
# print(student_marks)
# print("+ operation--2 list", student_marks)
# length of list
print("length of list =", len(student_marks))

# element(index)--------
print("element at 10 =", student_marks[10])

# count(element) = give the count of given element
print("count of 45 =", student_marks.count(45))

# Index(element) = give the index of given element
print("index of 55 =", student_marks.index(55))

# insert(index, element) = insert the element at given Index.
student_marks.insert(0, 10)
print("after index 10=", student_marks)
student_marks[5] = 500     #--------- replace the exiting no. with  500 at 5th index.

# reverce () = revere the list
student_marks.reverse()
print("reverse list =", student_marks)
student_marks.reverse()
print("reverse list =", student_marks)

# pop = remove the last element of the list
student_marks.pop()
print ("after pop =", student_marks)

# remove() = remove the given the element
student_marks.remove("fifty")
student_marks.remove(95)
print("after remove=", student_marks)

print(len(student_marks))

# copy
marks_student = student_marks.copy()
print("copied list", marks_student)
marks_student.append("sixty")
print("after append copied list =", marks_student)

student_marks.pop()
print("list after pop", student_marks)

# sort = arrange the element in ascending order
student_marks.sort()
print("list after sort =", student_marks)
student_marks.sort(reverse=True)
print("list after sort reverse =", student_marks)

# clear
student_marks.clear()
print(student_marks)
student_marks.append('paypal')
print(student_marks)

# split
message = "today is holiday"
print("after the split=", message.split())


# ----------------
message1 = "today is monday"
s = message1.split()
print(s)
s.extend(["hallmark", "trademark"])
print(s)
a = " ".join(s)
print(a)