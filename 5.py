# ----- input handling -----
with open('input_day5.txt') as fin:
    crates = fin.read().split('\n\n')
    crates = [elem.split('\n') for elem in crates]

    stacks = crates[0][:-1]
    stacks = [elem[1::4] for elem in stacks]
    stacks = list(map(list, zip(*stacks)))
    stacks = [[elem for elem in col if elem != ' '] for col in stacks]

    instructions = crates[1]
    instructions = [elem.split(" ") for elem in instructions]

def main():
    for instruction in instructions:
        amount = int(instruction[1])
        src = int(instruction[3]) - 1
        dest = int(instruction[5]) - 1

        # --- Part 1 --- 
        # for _ in range(amount):
            # stacks[dest].insert(0, stacks[src].pop(0))

        # --- Part 2 --- 
        lifted_crates = stacks[src][:amount]
        del stacks[src][:amount]
        stacks[dest] = lifted_crates + stacks[dest]

    message = [elem[0] for elem in stacks]
    print(''.join(message))


if __name__ == '__main__':
    main()