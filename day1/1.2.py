with open('1.1.input') as f:
    lines = f.readlines()
    prev = None
    inc_counter = 0
    windows = []
    for idx in range(0, len(lines) - 2):
        windows.append(int(lines[idx]) + int(lines[idx + 1]) + int(lines[idx + 2]))

    for idx in range(1, len(windows)):
        if windows[idx - 1] < windows[idx]:
            inc_counter += 1

    print(inc_counter)