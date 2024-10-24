integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sum_odd_even(numbers):
    sum_of_odd = 0
    sum_of_even = 0

    for num in numbers:
        if num % 2 == 0:
            sum_of_even += num
        else:
            sum_of_odd += num
    
    return (f"sum of odd number: {sum_of_odd}", f"sum of even number: {sum_of_even}")

print(sum_odd_even(integers))