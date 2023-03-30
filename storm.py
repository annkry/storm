'''The variable domains (storm fields) are 0 or 1.
Declaration of constraints:
for every three fields (lying next to each other, horizontally or vertically) the condition must be satisfied: a+2b+3c != 2
for every 2 x 2 squares the condition must be satisfied: there can be no arrangement [1,0,1,0] or [0,1,0,1] or any triplet of painted fields
the sum of colored fields in rows and columns must equal the numbers given as input.'''

def B(i, j):
    return 'B_%d_%d' % (i, j)


def domains(Vs):
    return [q + ' in 0..1' for q in Vs]


def suma(QS, k):
    return ' sum([' + ', '.join(QS) + '], #= , %d)' % k


def get_column(j, c):
    return [B(i, j) for i in range(c)]


def get_raw(i, c):
    return [B(i, j) for j in range(c)]


def horizontal(c, r, rows):
    return [suma(get_raw(i, c), rows[i]) for i in range(r)]


def vertical(c, r, cols):
    return [suma(get_column(i, r), cols[i]) for i in range(c)]


def tri(a, b, c):
    return '%s + 2*%s +3*%s #\\= 2' % (a, b, c)


def all_tri(r):
    return [tri(B(i, j), B(i, j+1), B(i, j+2)) for i in range(r) for j in range(0, r-2)]


def all_tri_c(c):
    return [tri(B(j, i), B(j+1, i), B(j+2, i)) for i in range(c) for j in range(0, c-2)]


def square(a, b, c, d):
    return 'tuples_in([[%s,%s,%s,%s]] , [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1], [1,1,0,0], [0,0,1,1], [0,1,0,1], [1,0,1,0], [1,1,1,1], [0,0,0,0]] )' % (a, b, c, d)


def sq_gen(r, c):
    return [square(B(i, j), B(i, j+1), B(i+1, j), B(i+1, j+1)) for i in range(0, r-2) for j in range(0, c-2)]


def print_constraints(Cs, indent, d):
    position = indent
    writeln(indent * ' ')
    for c in Cs:
        writeln(c + ',')
        position += len(c)
        if position > d:
            position = indent
            writeln('')
            writeln(indent * ' ')


def storms(rows, cols, triples):
    writeln(':- use_module(library(clpfd)).')

    R = len(rows)
    C = len(cols)

    bs = [B(i, j) for i in range(R) for j in range(C)]

    writeln('solve([' + ', '.join(bs) + ']) :- ')

    cs = domains(bs) + vertical(C, R, cols) + horizontal(C, R, rows) + \
        all_tri_c(C) + all_tri(R) + sq_gen(R, C)
    for i, j, val in triples:
        cs.append('%s #= %d' % (B(i, j), val))
    print_constraints(cs, 4, 70),
    print()
    writeln('    labeling([ff], [' + ', '.join(bs) + ']).')
    writeln('')
    writeln(":- tell('prolog_result.txt'), solve(X), write(X), nl, told.")


def writeln(s):
    output.write(s + '\n')


txt = open('zad_input.txt').readlines()
output = open('solution.txt', 'w')

rows = list(map(int, txt[0].split()))
cols = list(map(int, txt[1].split()))
triples = []

for i in range(2, len(txt)):
    if txt[i].strip():
        triples.append(tuple(map(int, txt[i].split())))

storms(rows, cols, triples)
