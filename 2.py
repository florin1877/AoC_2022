# ----- input handling -----
with open('input_day2.txt') as fin:
    guide = fin.read().split('\n')
    guide = [elem.split(' ') for elem in guide]

elf_hands = ['A', 'B', 'C']
my_hands = ['X', 'Y', 'Z']

# --- Part 1 ---
outcomes = [[4, 1, 7], [8, 5, 2], [3, 9, 6]]

# --- Part 2 --- 
outcomes2 = [[3, 1, 2], [4, 5, 6], [8, 9, 7]]

def round_score(round):
    i = elf_hands.index(round[0])
    j = my_hands.index(round[1])
    return outcomes2[j][i]

def main():
    scores = [round_score(round) for round in guide]

    print(sum(scores))

if __name__ == '__main__':
    main()