# Find duplicate elements in a list.
#Simple Explanation: Keep track of elements that have already appeared. If an element is seen again, add it to a duplicate
#collection.
#Remember: first time = store it; second time = duplicate.
# list1=[10,20,30,10,20]
# seen=set()
# duplicate=set()
# #Iterate through the list
# for number in list1:
#     if number in seen:    #Number already seen one time its a duplicate, so we have to add it to duplicate set
#         duplicate.add(number)
#     else:
#         seen.add(number)  # else need to add to seen set
# print(duplicate)
# print(seen)


#remove duplicate while maintaining order
# 1.create a list
# 2.traverse through the list using for loop, add unique one's to the set
# 3.add same to then list to maintain order
List1=[2,3,1,5,6,8,1,3,4,4]
seen =set()
result =[]
for number in List1:
    if number not in seen:
         seen.add(number)
         result.append(number)
print(seen)
print(result)
