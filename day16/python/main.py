import re

def read_data(file_name='../input.txt'):
    registers = {}
    program = []
    
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            if line.startswith('Register'):
                reg, val = line.split(': ')
                reg = reg.split()[1]  # Extract register letter
                registers[reg.lower()] = int(val)
            elif line.startswith('Program:'):
                program = [int(x) for x in line.split(': ')[1].split(',')]
    
    return {'program': program, **registers}

def part1(data):
    a, b, c = data['a'], data['b'], data['c']
    program = data['program']
    #
    i, R = 0, []

    while i in range(len(program)):
        C = {0:0,1:1,2:2,3:3,4:a,5:b,6:c}

        match program[i], program[i+1]:
            case 0, op: a = a >> C[op]
            case 1, op: b = b ^ op
            case 2, op: b = 7 & C[op]
            case 3, op: i = op-2 if a else i
            case 4, __: b = b ^ c
            case 5, op: R = R + [C[op] & 7]
            case 6, op: b = a >> C[op]
            case 7, op: c = a >> C[op]
        i += 2
    return R

def part2(data):

    a, b, c = data['a'], data['b'], data['c']
    program = data['program']

    minimum = float('inf')
    todo = [(1, 0)]
    for i, a in todo:
        for a in range(a, a+8):
            if part1({'a': a, 'b': 0, 'c': 0, 'program': program}) == program[-i:]:
                todo += [(i+1, a*8)]
                if i == len(program): minimum = min(minimum, a)

    return minimum

if __name__ == '__main__':
    data = read_data('../input.txt')
    print('PART 1 : SOLUTION', )
    print(part1(data), sep=',')
    data = read_data('../input.txt')
    print('PART 2 : SOLUTION', part2(data))
