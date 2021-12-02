with open('1.1.input') as f:
    lines = f.readlines()
    prev = None
    inc_counter = 0
    for line in lines:
        if prev is not None and prev < int(line):
            inc_counter += 1

        prev = int(line)

    print(inc_counter)