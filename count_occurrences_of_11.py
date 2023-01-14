def count11(seq):
    y = 0

    seq_len = len(seq)

    for index, value in enumerate(seq):
        next_index = index + 1

        if next_index >= seq_len:
            break

        current_int = value
        next_int = seq[next_index]

        joined_string = str(current_int) + str(next_int)

        if joined_string == "11":
            y += 1

    return y


print(count11([0, 0, 1, 1, 1, 0]))
