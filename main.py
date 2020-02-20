input_filename = "b_read_on.txt"


def library_weight(lib_singup_time, lib_books_per_day, lib_books_indexs, book_scores):
    total_score = 0

    for b in lib_books_indexs:
        total_score += book_scores[b]

    return total_score / (0.5 * lib_singup_time) + lib_books_per_day


def main():
    input_file = open(input_filename)

    fl = next(input_file).split()
    num_dif_books = int(fl[0])
    num_libraries = int(fl[1])
    num_days = int(fl[2])

    sl = next(input_file).split()

    book_scores = list(map(lambda x: int(x), sl))

    lib_index = 0

    library_weights = []

    for lib in input_file:
        lib_info = lib.split()
        if not lib_info:
            break
        # lib_num_books = int(lib_info[0])
        lib_singup_time = int(lib_info[1])
        lib_books_per_day = int(lib_info[2])

        lib_books_indexs = next(input_file).split()
        lib_books_indexs = map(lambda x: int(x), lib_books_indexs)

        lib_weight = library_weight(lib_singup_time, lib_books_per_day, lib_books_indexs, book_scores)

        library_weights.append((lib_index, lib_weight))

        lib_index += 1

    library_order = sorted(library_weights, key=lambda x: x[1])

    print(map(library_order[::-1]))

    input_file.close()

    output_filename = input_filename[:-4] + '-out.txt'

    output_file = open(output_filename, 'w+')

    # output_file.write()

    output_file.close()


if __name__ == '__main__':
    main()
