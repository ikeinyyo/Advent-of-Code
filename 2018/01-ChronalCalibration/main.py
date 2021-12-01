def part_one():
    f = open("data/input.txt", "r")
    total = 0
    for number in f:
      total += int(number)
    print(total)

def part_two():
    f = open("data/input.txt", "r")
    lines = f.read().splitlines()
    total = 0
    values = [0]
    found = False
    while not found:
        for number in lines:
            total += int(number)
            if total in values:
                found = True
                break
            values.append(total)
    print(total)

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()
