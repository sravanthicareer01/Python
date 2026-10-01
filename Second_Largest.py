#Find the second-largest number.
# 1.Create a list of items with the duplicates
# 2.Remove the duplicates from the list by applying set ,since set won't allow duplicates
# 3.Sort the list then we foundout order of elements.
# 4.based on reverse index we can findout - -1=last,-2=second largest

List1=[10,20,30,20,50,10,40]
Unique_numbers = list(set(List1))
print(Unique_numbers) #Before sort
Unique_numbers.sort()
print(Unique_numbers) #After Sort
second_largest = Unique_numbers[-2] # index from the right to left
print(second_largest)



