'''
    줄 뒤집기
'''


def reverse_lines(infilename, outfilename):
    with open(infilename) as infile, open(outfilename, 'w') as outfile:
        for one_line in infile:
            outfile.write(f'{one_line.rstrip()[::-1]}\n')


if __name__ == '__main__':
    reverse_lines('line_reverse', 'line_reverse_output')
