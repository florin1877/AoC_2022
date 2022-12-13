def set_priority(item):
    if item < 'a' or item > 'z':
        return ord(item) - 38
    return ord(item) - 96

# ----- input handling -----
with open('input_day3.txt') as fin:
    rucksacks = fin.read().split('\n')
    
    # --- Part 1 ---
    # rucksacks = [[elem[:len(elem)//2], elem[len(elem)//2:]] for elem in rucksacks]
    # rucksacks = [''.join(set(elem[0]).intersection(elem[1])) for elem in rucksacks]
    
    # --- Part 2 ---
    badges = [rucksacks[n:n+3] for n in range(0, len(rucksacks), 3)]
    badges = [''.join(set.intersection(*map(set,group))) for group in badges]

    items = [set_priority(item) for item in badges]


def main():
    print(sum(items))

if __name__ == '__main__':
    main()