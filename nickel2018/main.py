def solution(p: list) -> int:
    # the first step: calculate the number of elements in the triangle
    total_square = sum([len(p)-i for i in range(0, len(p)+1)])

    # the next step: find the lengths of all sequences of False elements
    blank = False  # indicates if a current sequence is of False elements
    seq = 0  # a length of a sequence of False elements
    zeros = []  # store the lengths of the sequences
    for i in range(len(p)):
        if not p[i]:
            if blank:
                seq += 1
            else:
                # the first element of a sequence of False elements
                blank = True
                seq = 1
        else:
            blank = False
            zeros.append(seq)
            seq = 0
    # don't forget to save the length of the last sequence
    zeros.append(seq)

    # the final step: subtract the number of elements in "ZERO Triangles"
    for x in zeros:
        total_square -= sum([x-i for i in range(0, x)])

    # checking the constraints set in the task
    if total_square >= 1000000000:
        return 1000000000
    return total_square