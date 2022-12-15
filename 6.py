# ----- input handling -----
with open('input_day6.txt') as fin:
    buffer = fin.read()

def check_marker(marker):
    for c in marker:
        if marker.count(c) != 1:
            return False
    return True

def main():
    cnt = []

    for idx in range(len(buffer) - 1):
        marker = buffer[idx:idx+4]
        message = buffer[idx:idx+14]
        
        # --- Part 1 --- 
        # if (check_marker(marker) == True):
        #     print(idx+4)
        #     return
        
        # --- Part 2 --- 
        if (check_marker(message) == True):
            print(idx+14)
            return

if __name__ == '__main__':
    main()