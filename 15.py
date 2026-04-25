def sum_digits(num):
    # Use the absolute value to handle negative integers
    num = abs(num)
    total_sum = 0
    
    while num > 0:
        # Extract the last digit
        total_sum += num % 10
        # Remove the last digit
        num //= 10
        
    return total_sum
