import argparse


def read_data(filepath):
    with open(filepath) as in_file:
        return list(map(int, in_file.readlines()))


def part1(is_sample):
    lines = read_data(
        'data/part1/sample.txt' if is_sample else 'data/part1/input.txt')
    return calculate_increases(lines)


def part2(is_sample):
    lines = read_data(
        'data/part2/sample.txt' if is_sample else 'data/part2/input.txt')
    return calculate_increases(make_windows(lines, 3))


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
