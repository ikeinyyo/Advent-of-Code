import argparse


def read_data(filepath):
    with open(filepath) as in_file:
        return in_file.readlines()


def part1(is_sample):
    lines = read_data(
        'data/sample.txt' if is_sample else 'data/input.txt')
    up = list(map(lambda up_line: int(up_line.split(' ')[1]), filter(lambda line: line.startswith('up'), lines)))
    down = list(map(lambda up_line: int(up_line.split(' ')[1]), filter(lambda line: line.startswith('down'), lines)))
    forward = list(map(lambda up_line: int(up_line.split(' ')[1]), filter(lambda line: line.startswith('forward'), lines)))
    return sum(forward) * (sum(down) - sum(up))


def part2(is_sample):
    lines = read_data(
        'data/sample.txt' if is_sample else 'data/input.txt')
    
    aim = 0
    depth = 0
    horizontal = 0
    for line in lines:
        number = int(line.split(' ')[1])
        if line.startswith('up'):
            aim -= number
        elif line.startswith('down'):
            aim += number
        else:
            horizontal += number
            depth += number*aim

    return horizontal * depth


def calculate_increases(data):
    displazed_list = data[:1] + data[:-1]
    result_list = map(int.__sub__, data, displazed_list)
    return len(list(filter(lambda item: item > 0, result_list)))


def make_windows(data, window_size):
    windows_list = data.copy()
    for i in range(1, window_size):
        windows_list = list(map(int.__add__, windows_list, data[i:]))
    return windows_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sample', action='store_true')
    args = parser.parse_args()

    part1_result = part1(args.sample)
    print("Part1:", part1_result)

    part2_result = part2(args.sample)
    print("Part2:", part2_result)
