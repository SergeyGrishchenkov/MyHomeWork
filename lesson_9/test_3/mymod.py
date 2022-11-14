def count_lines(name):
    with open(name) as our_file:
        line_count = len(our_file.readlines())
    return line_count


def count_chars(name):
    with open(name) as our_file:
        line_char_count = len(our_file.read())
    return line_char_count


def test(name):
    string_count = count_lines(name)
    char_count = count_chars(name)
    print(
        f'Your file \'{name}\' has:\n{string_count} - the number of lines,\n{char_count} - the number of characters, including service symbols')


if __name__ == '__main__':
    test('D:/test.txt')
