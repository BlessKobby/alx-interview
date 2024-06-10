#!/usr/bin/python3
"Module for 0-minoperations"


def minOperations(n):
    """
    Gets fewest # of operations needed to result in exactly n H characters
    """
    # All outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    ops, rot = 0, 2
    while rot <= n:
        # If n evenly divides by rot
        if n % rot == 0:
            # Total even-divisions by rot = total operations
            ops += rot
            # set n to the remainder
            n = n / rot
            # reduce rot to find remaining smaller vals that evenly-divide n
            rot -= 1
        # increment rot until it evenly-divides n
        rot += 1
    return ops
