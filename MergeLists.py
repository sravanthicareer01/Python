# 1.merge two lists -take list1 and list2
# 2.use concatenation list1+list2 or we can simply extends list1.extends(list2) and print the result.
List1=[10,20,32,13,24]
List2=[30,20,10,43,12]
Result = List1+List2
print(Result)
List1.extend(List2)# Extends list1
print(List1) # List1 after extends
# Remove duplicates from the resultant list
withoutDuplicates = list(set(Result))
print(withoutDuplicates)
#Sort list
withoutDuplicates.sort()
print(withoutDuplicates)



