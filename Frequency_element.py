#Count frequency of elements in a list.
# 1.create a list
# 2.Simple Explanation: Use a dictionary where the element is the key and its count is the value. Each time an element
# appears, increase its count by one.

# List1=[1,2,3,1,2,3,5,6,2]
# Frequency ={}
# for number in List1:
#     Frequency[number] = Frequency.get(number,0)+1 # number is not showing give 0 or increase count by 1
# print(Frequency)

#Find the first non-repeated character.
# 1.find the frequency of characters in text through for loop iteration
# 2.create variable name with Non_Repeated_Character and initialize to None
# 3.again traverse through all the characters in text and compare count using if
# 4.print "Non_repeated_Character"

# text="aabbccdeee"
# frequency ={}
# for char in text:
#     frequency[char]=frequency.get(char,0)+1
    
   
# non_repeat = None
# for char in text:
#     if frequency[char]==1:
#         non_repeat = char
#         break;
# print(non_repeat)
#  # Find duplicates using functions

def find_duplicate(s):
    seen=set()
    duplicate=set()
    for char in s:
        if char in seen:
           duplicate.add(char)
        else:
           seen.add(char)
    return duplicate
print(find_duplicate("programming"))






