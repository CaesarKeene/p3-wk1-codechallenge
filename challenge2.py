def check_two_positive(a,b,c):
    # count the number of positive numbers amongst a, b, and c
    positive_count = sum(1 for num in [a,b,c] if num > 0)
    return positive_count == 2  # check if the two numbers are positive

# different cases
print (check_two_positive(2,4,-3))
print (check_two_positive(-4,6,0))
print (check_two_positive(-14,-3,-4))
print (check_two_positive(9,0,2))
