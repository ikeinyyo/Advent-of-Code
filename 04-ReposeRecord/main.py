part_one_input = "data/input.txt"
part_two_input = "data/input.txt"


def parse(line):
    tokens = line.split(' ')
    return {'date': parse_date(tokens), 'id': parse_id(tokens),
    'time': parse_time(tokens), 'status': parse_status(tokens)}

def parse_date(tokens):
    return tokens[0][1:].replace('-', '')

def parse_time(tokens):
    h = int(tokens[1][:2])
    m = int(tokens[1][3:5])
    return m if h == 0 else -1

def parse_id(tokens):
    return tokens[3][1:] if tokens[3][0] == '#' else ''

def parse_status(tokens):
    return 1 if tokens[2] == 'falls' else 0

def part_one():
    logs = []
    for line in open(part_one_input):
        logs.append(parse(line))
    logs.sort(key=lambda log: (log['date'], log['time']))
    print(logs)
    print("Day 4")

def main():
    part_one()

if __name__ == "__main__":
    main()
