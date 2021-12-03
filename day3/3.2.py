import numpy as np

with open("3.1.input") as file:
    lines = list(
        map(
            lambda line: list(line.replace("\n", "")),
            file.readlines()
        )
    )

    def removeFollowing(inp: list[list[str]], idx: int, most = True) -> int:
        sum = 0
        for line in inp:
            sum += int(line[idx])

        if sum == len(inp):
            return "0"
        elif sum == 0:
            return "1"

        if most:
            if sum >= len(inp) / 2:
                return "0"
            return "1"
        else:
            if sum < len(inp) / 2:
                return "0"
            return "1"

    def filterOut(inp: list[list[str]], idx: int, to_remove: str) -> list[list[str]]:
        new_list = []
        for line in inp:
            if line[idx] != to_remove:
                new_list.append(line)
        return new_list

    oxygen_lines = lines
    co2_lines = lines
    curr_idx = 0
    while len(oxygen_lines) > 1:
        remove = removeFollowing(oxygen_lines, curr_idx)
        oxygen_lines = filterOut(oxygen_lines, curr_idx, remove)
        curr_idx += 1

    curr_idx = 0
    while len(co2_lines) > 1:
        remove = removeFollowing(co2_lines, curr_idx, False)
        co2_lines = filterOut(co2_lines, curr_idx, remove)
        curr_idx += 1

    to_dec = lambda bin: int(np.array2string(bin, separator="").replace("[", "").replace("]", ""), 2)
    print(to_dec(np.array(oxygen_lines[0], dtype=int)) * to_dec(np.array(co2_lines, dtype=int)))
    """
    wrong answers:
    2034902
    6347574
    """
