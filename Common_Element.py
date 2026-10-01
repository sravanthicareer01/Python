# Find common elements between two lists.
# 1.Take two lists and make sure there is no duplicates in both the lists
# 2.Here we have to findout common elements, so we have to add & operation on both lists
# 3.print the result
List1=[10,5,40,20,54]
List2=[5,40,67,56,32]
Result = list(set(List1)&set(List2))
print(Result)
