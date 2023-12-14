def highest_consonant_value(s):
    consonants = "bcdfghjklmnpqrstvwxyz"  # defining a string holding the consonants
    max_value = 0  # putting the maximum consonant value to 0
    current_value = 0  # putting the current consonant value to 0
    
    for char in s:  # iterating through each character in the input string s
        if char in consonants:  # Check if the character is a consonant
            # calculation of the value of the consonant based on its position in the alphabet
            current_value += ord(char) - ord('a') + 1
        else:
            # if the character is not a consonant, update the maximum value encountered
            max_value = max(max_value, current_value)
            # reset the current value to 0 as consecutive consonants have ended
            current_value = 0
    
    # return the maximum value encountered 
    return max(max_value, current_value)

# testing the function with the input "king"
print(highest_consonant_value("king"))
