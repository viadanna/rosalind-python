from .sequences import DNA


def parse_fasta(lines, _type):
    name = None
    sequence = ''
    for line in lines:
        if line.startswith('>'):
            if name:
                yield DNA(sequence, name)
                sequence = ''
            name = line[1:]
        else:
            sequence += line
    yield _type(sequence, name)


def read_fasta(string, _type=DNA):
    return parse_fasta(string.split('\n'), _type)
