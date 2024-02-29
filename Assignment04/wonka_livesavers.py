# William Romine
# 00103649
# Dr. Lewis CS472
# https://www.geeksforgeeks.org/rearrange-a-string-in-sorted-order-followed-by-the-integer-sum/

def rearrange_candies(input_string):
    red_count = input_string.count('r')
    white_count = input_string.count('w')
    blue_count = input_string.count('b')
    
    output_string = 'r' * red_count + 'w' * white_count + 'b' * blue_count
    
    red_pointer = 0
    white_pointer = red_count
    blue_pointer = red_count + white_count
    
    for candy in input_string:
        if candy == 'r':
            output_string = output_string[:red_pointer] + candy + output_string[red_pointer + 1:]
            red_pointer += 1
        elif candy == 'w':
            output_string = output_string[:white_pointer] + candy + output_string[white_pointer + 1:]
            white_pointer += 1
        elif candy == 'b':
            output_string = output_string[:blue_pointer] + candy + output_string[blue_pointer + 1:]
            blue_pointer += 1
    
    return output_string

input_string = input("Order of Candies 'r', 'w', 'b': ")

output_string = rearrange_candies(input_string)

print("Rearranged Candies:", output_string)