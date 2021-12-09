def create_phone_number(numbers):
    firsts = ''.join(map(str, numbers[:3]))
    seconds = ''.join(map(str, numbers[3:6]))
    thirds = ''.join(map(str, numbers[6:10]))
    phone_number = f"({firsts}) {seconds}-{thirds}"
    return phone_number


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
