part_one_input = "data/input.txt"
part_two_input = "data/input.txt"

def part_one():
    twice = 0
    three_times = 0
    f = open(part_one_input, "r")
    for line in f:
        has_twice = False
        has_three_times = False
        for number in line:
            if line.count(number) == 2 and not has_twice:
                has_twice = True
                twice += 1
            elif line.count(number) == 3 and not has_three_times:
                has_three_times = True
                three_times += 1
    print("{0} * {1} = {2}".format(twice, three_times, twice * three_times))

def diff_by_one_character(text1, text2):
    diff_count = 0
    for index in range(0, len(text1)):
        if text1[index] != text2[index]:
            if diff_count > 1:
                return False
            else:
                diff_count += 1
    return diff_count == 1

def clear_character(text1, text2):
    for index in range(0, len(text1)):
        if text1[index] != text2[index]:
            return text1[:index] + text1[index+1:]


def part_two():
    f = open(part_two_input, "r")
    lines = f.read().splitlines()
    for first in lines:
        for second in lines:
            if diff_by_one_character(first, second):
                print("{} - {}: {}".format(first, second, clear_character(first, second)))
                return
                
def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()
