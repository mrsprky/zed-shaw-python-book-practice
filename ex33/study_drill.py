from sys import argv

script, start_point, ending_point = argv

starting = int(start_point)
ending = int(ending_point) + 1


def append_to_list(from_num, to_num):
    i = from_num
    numbers = []

    while i < to_num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
    return numbers

print("The numbers: ")

numbers = append_to_list(starting, ending)

for num in numbers:
    print(num)