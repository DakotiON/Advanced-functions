import math

def filter_palindromes(x):
    is_palindrome = lambda s: s == s[::-1]
    return list(filter(is_palindrome, x))

# Example usage:
words = ["racecar", "level", "deified", "python", "madam"]
palindromes = filter_palindromes(words)
print("Palindromes:", palindromes)
print('-------------------------------------------------------')
def collatz(number):
    current_number = number

    def next_collatz():
        nonlocal current_number
        if current_number == 1:
            raise StopIteration
        if current_number % 2 == 0:
            current_number //= 2
        else:
            current_number = current_number * 3 + 1
        return current_number

    while True:
        yield current_number
        try:
            current_number = next_collatz()
        except StopIteration:
            break


sequence = collatz(6)
for number in sequence:
    print(number)
print('-------------------------------------------------------')
def round_numbers(numbers, direction='down'):
    rounded_numbers = []
    for num in numbers:
        if direction == 'down':
            rounded_numbers.append(math.floor(math.sqrt(num)))
        elif direction == 'up':
            rounded_numbers.append(math.ceil(math.sqrt(num)))
        else:
            raise ValueError("Invalid direction")
    return rounded_numbers

# Example usage:
numbers = [1, 2, 3, 4, 5]
rounded_down = round_numbers(numbers, direction='down')
print("Rounded down:", rounded_down)

rounded_up = round_numbers(numbers, direction='up')
print("Rounded up:", rounded_up)
print('-------------------------------------------------------')
