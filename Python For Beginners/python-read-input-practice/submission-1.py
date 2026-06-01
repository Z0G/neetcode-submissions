def add_two_numbers() -> int:
    numbers = input()
    strings = numbers.split(",")

    new_list = []
    total = 0

    for s in strings:
        total += int(s)

    return total    



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
