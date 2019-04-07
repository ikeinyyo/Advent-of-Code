import numpy as np

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
    return m if h == 0 else 61

def parse_id(tokens):
    return tokens[3][1:] if tokens[3][0] == '#' else None

def parse_status(tokens):
    return 1 if tokens[2] == 'falls' else 0

def create_guards(logs):
    guards = []
    for log in logs:
        if not any(guard['id'] == log['id'] for guard in guards):
            guards.append({'id': log['id'], 'status': 0, 'last_time': 0, 'times': np.zeros(60)})
    return guards

def get_guard_by_id(guards, id):
    return next((guard for guard in guards if guard['id'] == id), None)

def create_report(logs, guards):
    id = 0
    for log in logs:
        if log['id']:
            id = log['id']

        guard = get_guard_by_id(guards, id)

        if log['id']:
            guard['last_time'] = 0

        if guard['last_time'] > log['time']:
            range = guard['times'][guard['last_time']: 59]
            range[:] = range + 1
            guard['last_time'] = 0

        if log['status'] == 1 and guard['status'] == 0:
            guard['last_time'] = log['time']
        elif log['status'] == 0 and guard['status'] == 1:
            range = guard['times'][guard['last_time']: log['time']]
            range[:] = range + 1
        guard['status'] = log['status']

def part_one():
    logs = []
    for line in open(part_one_input):
        logs.append(parse(line))
    logs.sort(key=lambda log: (log['date'], log['time']))

    guards = create_guards(logs)

    create_report(logs, guards)
    guards.sort(key=lambda guard: guard['times'].sum(), reverse=True)
    print("{} x {} = {}".format(guards[0]['id'], np.argmax(guards[0]['times']), (int(guards[0]['id']) * np.argmax(guards[0]['times']))))

def main():
    part_one()

if __name__ == "__main__":
    main()
