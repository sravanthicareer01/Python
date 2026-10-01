
#Simple Explanation: Use a loop and build the reversed string by adding each character to the beginning of a new string.
#Remember: Read the original string from left to right, but place every new character at the front.

#Reverse a string without using [::-1].
OriginalString ="python"
reversed_String =""
for char in OriginalString: # Read each character
    reversed_String = char + reversed_String # Add at the beginning of the empty string
print(reversed_String)

#Reverse String with using [::-1]

OriginalString ="GenAI"
Reversed_String =""
Reversed_String = OriginalString[::-1]
print(Reversed_String)
