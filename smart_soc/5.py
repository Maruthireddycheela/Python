# write a programm for finding second largest number in list

#1st method

def second_largest(numbers):
    # Remove duplicates and sort the list in descending order
    numbers = list(set(numbers))  # Remove duplicates
    
    if len(numbers) < 2:
        return None  # If there are fewer than 2 unique numbers, no second largest exists
    
    numbers.sort(reverse=True)  # Sort the list in descending order
    return numbers[1]  # The second element is the second largest

# Example usage
numbers = [12, 45, 23, 45, 67, 34, 12]
result = second_largest(numbers)

if result is not None:
    print(f"The second largest number is {result}")
else:
    print("There is no second largest number")


#2nd method


def second_largest(numbers):
    # Initialize the largest and second largest variables
    largest = second = float('-inf')  # `-inf` is the smallest possible number to start with

    for number in numbers:
        if number > largest:
            second = largest  # If a new largest is found, the old largest becomes the second largest
            largest = number  # Update the largest number
        elif number > second and number != largest:
            second = number  # Update the second largest number, but only if it's different from largest

    return second  # After the loop, return the second largest value

numbers = [1, 2, 12, 5, 234]
print("second_largest:", second_largest(numbers))


# 3rd method

def second_largest(number):
    # Remove duplicates by converting the list to a set, then back to a list
    number = list(set(number))

    # Sort the list in descending order
    number.sort(reverse=True)

    # If the list has more than 1 element, return the second largest number, otherwise return None
    return number[1] if len(number) > 1 else None

number = [1, 2, 332, 23]
print("second-largest number:", second_largest(number))

