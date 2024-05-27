list1 = ["zzz","2","sss"]
list2 =["vasu"]
print("test lists")
print (list1+list2)
print (list2)
list1[1]='inserted 3'
print (list1)

# adding Element 
list1.append('apend 44')
print(list1)

# remove element

list1.remove('sss')
print(list1)

#sort
list1.sort()
print (list1)

#reverse

list1.reverse()
print (list1)

print(len(list1))

#nested lists

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3]
lists = [fruits, numbers]
print('nested lists ')
print(lists)

#extend list




numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
more_numbers = [11, 12, 13, 14, 15]
numbers1.extend(more_numbers)
print("Extending list ")
print(numbers1)

print(numbers1.index(5))
numbers1.clear()
print(numbers1)

# SUB selection /slicing

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("sub selection  ")

print(numbers[2:7]) 

print(numbers[-2:-1])


# count
numbers1 = [1,2,2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers1.count(2))


number1copy= numbers1.copy()
print(number1copy)

list1.append(number1copy)
print(list1)