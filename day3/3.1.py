import numpy as np

with open("3.1.input") as file:
    lines = np.array(
        list(
            map(
                lambda line: list(line.replace("\n", "")),
                file.readlines()
            )
        ),
        dtype=int
    )
    gamma = np.where(np.sum(lines, axis=0) > lines.shape[0] / 2, 1, 0)
    epsilon = np.abs(gamma - 1)
    to_dec = lambda bin: int(np.array2string(bin, separator="").replace("[", "").replace("]", ""), 2)
    print(to_dec(gamma) * to_dec(epsilon))
