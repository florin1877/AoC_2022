import numpy as np

# ----- input handling -----
with open('input_day1.txt') as fin:
    elfs = fin.read().split('\n\n')
    elfs = [elem.split("\n") for elem in elfs]
    elfs = [list(map(int, elem)) for elem in elfs]

def main():
    total_calories = np.array([sum(elem) for elem in elfs])
    sorted_indices = np.argsort(total_calories)
    sorted_calories = total_calories[sorted_indices]
    print(sum(sorted_calories[-3:])) 


if __name__ == "__main__":
    main()