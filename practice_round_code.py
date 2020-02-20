
input_filename = "e_also_big.in"


def main():
    input_file = open(input_filename)
    fl = next(input_file).split()

    max_slices, av_types = int(fl[0]), int(fl[1])

    used_types = 0
    types = []

    pizzas = next(input_file).split()[::-1]

    remaining_slices = max_slices

    for pizza_type, num_slices in zip(reversed(range(av_types)), pizzas):
        num_slices = int(num_slices)

        if num_slices < remaining_slices:
            used_types += 1

            types.append(str(pizza_type))

            remaining_slices -= num_slices

        if remaining_slices == 0:
            break

    output_filename = input_filename[:-2] + 'out'

    output_file = open(output_filename, 'w+')

    output_file.write(str(used_types) + '\n')

    output_file.write(' '.join(types[::-1]))


if __name__ == '__main__':
    main()
