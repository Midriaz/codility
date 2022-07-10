def solution(R):
    speed = {"foot": {"A": 20, "S": 30}, "scooter": {"A": 5, "S": 40}}

    # We start a ride on a scooter, and one time per travel can change to foot.
    # So we need to know if and when do this switch.
    #
    # The idea of the algorithm is to calculate the time of travel by scooter on every road segment.
    # Simultaneously, the algorithm calculates the time of travel by foot on every reverse road segment.
    #
    # Then in every segment, we compare how long it will take to continue traveling by scooter
    # and to continue traveling by foot.
    #
    # The algorithm has optimal O(N) complexity and scores 100%.

    # sets the first segment value, other segment values will be incremented by the previous segment's value
    # to compare the time of travel just by foot and just by scooter we add leading zero
    # because on a start we don't spend any time yet
    scooter = [0, speed['scooter'][R[0]]]
    foot = [speed['foot'][R[-1]]]

    for i in range(1, len(R)):
        scooter.append(scooter[i] + speed['scooter'][R[i]])
        foot.append(foot[i-1] + speed['foot'][R[-i-1]])

    # reverse list of travel by foot time to simplify further actions
    foot = foot[::-1]

    # travel just by scooter or by foot?
    min_distance = min(scooter[-1], foot[0])

    # calculates on every segment how long it takes to complete the road by scooter and by foot
    for i in range(1, len(scooter) - 1):
        s = scooter[-1] - scooter[i]
        f = scooter[i] + foot[i]

        if foot[i] < s and f < min_distance:
            min_distance = f

    return min_distance


# performing tests, not a part of the solution
tests = [
    ['ASAASS', 116],
    ['SSA', 80],
    ['SSSSAAA', 175],
    ['AAAAAA', 30],
    ['SSSSSS', 180],
    ['AAAAS', 50],
    ['S', 30],
    ['A', 5]
]
tests = [[test[0], test[1], solution(test[0])] for test in tests]
[print(f'{test[0]}: expected {test[1]} got {test[2]}') for test in tests if test[2] != test[1]]