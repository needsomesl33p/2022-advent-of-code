def load_input():
    with open('inputs.txt', mode='r') as file:
        content = file.read()
        return content


def eval(signal):
    block_size = 4
    counter = 0
    signal_length = len(signal)

    for bit in range(signal_length):
        sector = signal[bit:block_size + bit]
        set_of_sec = set(sector)
        if len(set_of_sec) == block_size:
            break
        counter += 1

    return counter + block_size


def main():
    print(eval(load_input()))


if __name__ == '__main__':
    main()
