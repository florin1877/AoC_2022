# ----- input handling -----
with open('input_day4.txt') as fin:
    assignments = fin.read().split('\n')
    assignments = [elem.split(',') for elem in assignments]
    assignments = [[pair.split('-') for pair in elem] for elem in assignments]
    assignments = [[set(range(int(pair[0]), int(pair[1]) + 1)) for pair in elem] for elem in assignments]

def main():
    count = 0

    # --- Part 1 ---
    # if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]):

    # --- Part 2 ---
    for pair in assignments:
        if pair[0].isdisjoint(pair[1]):
            continue
        count = count + 1

    print(count) 

if __name__ == '__main__':
    main()