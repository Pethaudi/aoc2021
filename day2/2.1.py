dict = {
    "down": 1,
    "up": -1,
    "forward": 0
}
with open('2.1.input') as f:
    lines = f.readlines()
    parsed: list[[int, int]] = map(
        lambda split: [dict[split[0]], int(split[1])],
        map(
            lambda line: line.split(" "),
            lines
        )
    )

    x = 0
    y = 0
    for step in parsed:
        if step[0] == 0:
            x += step[1]
        else:
            y += step[1] * step[0]

    print(x * y)