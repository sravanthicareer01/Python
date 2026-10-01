#Largest and smallest numbers from the list
#1.create list and measure length of the list
#2.iterate through the length using indices
#3.Before this findout max and min values
List1=[10,20,5,6,25,34]
length=len(List1)
print(length)
List1.sort()
print(List1)
max_value = List1[0]
min_value = List1[0]
for i in range(length):
    if List1[i]>max_value:
        max_value=List1[i]
    if List1[i]<min_value:
        min_value=List[i]
print(max_value)   
print(min_value)  
# irrespective of length
print(max(List1))
print(min(List1))

