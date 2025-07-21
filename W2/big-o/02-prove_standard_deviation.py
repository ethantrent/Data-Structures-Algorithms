def standard_deviation_1(numbers):
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    avg = total / count
    sum_squared_differences = 0
    for number in numbers:
        sum_squared_differences += (number - avg) ** 2
    variance = sum_squared_differences / count
    return variance ** 0.5


def standard_deviation_2(numbers):
    sum_squared_differences = 0
    count_numbers = 0
    for number in numbers:
        total = 0
        count = 0
        for value in numbers:
            total += value
            count += 1
        avg = total / count
        sum_squared_differences += (number - avg) ** 2
        count_numbers += 1
    variance = sum_squared_differences / count_numbers
    return variance ** 0.5


def standard_deviation_3(numbers):
    count = len(numbers)
    avg = sum(numbers) / count
    sum_squared_differences = 0
    for number in numbers:
        sum_squared_differences += (number - avg) ** 2
    variance = sum_squared_differences / count
    return variance ** 0.5

numbers = [600, 470, 170, 430, 300]
print(standard_deviation_1(numbers))  # Should be 147.322 
print(standard_deviation_2(numbers))  # Should be 147.322 
print(standard_deviation_3(numbers))  # Should be 147.322 