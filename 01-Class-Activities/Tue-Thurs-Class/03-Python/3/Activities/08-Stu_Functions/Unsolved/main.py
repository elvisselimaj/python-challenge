# @TODO: Write a function that returns the arithmetic average for a list of numbers

def average(numbers):
    length = len(numbers)
    total = float(0)
    
    for num in numbers:
        total += num

    avg = total / length
    
    return avg
    

# Test your function with the following:
print(average([100, 50, 75.5]))
print(average(range(11)))