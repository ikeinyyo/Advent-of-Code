# Thanks for solution: https://www.reddit.com/r/adventofcode/comments/a2lesz/2018_day_3_solutions/eazjans/
import numpy as np

part_one_input = "data/input.txt"
part_two_input = "data/input.txt"

def part_one():
    matrix = np.zeros((1000, 1000), dtype=np.int)
    for line in open(part_one_input, "r"):
        r = parse(line)
        claim = matrix[r['left']:r['left']+r['width'],r['top']:r['top']+r['height']]
        claim[:] = claim + 1

    print(np.sum(np.where(matrix > 1, 1, 0)))

    for line in open(part_one_input, "r"):
        r = parse(line)
        claim = matrix[r['left']:r['left']+r['width'],r['top']:r['top']+r['height']]
        if claim.max() == 1:
            print(r['id'])

def get_padding(tokens):
    padding = tokens[2].replace(':', '').split(',')
    return int(padding[0]), int(padding[1])

def get_shape(tokens):
    shape = tokens[3].split('x')
    return int(shape[0]), int(shape[1])

def get_id(tokens):
    return int(tokens[0][1:])

def parse(line):
    tokens = line.split(' ')
    l, t = get_padding(tokens)
    w, h = get_shape(tokens)
    square = {}
    square['top'] = t
    square['left'] = l
    square['height'] = h
    square['width'] = w
    square['id'] = get_id(tokens)
    return square

def main():
    part_one()

if __name__ == "__main__":
    main()
