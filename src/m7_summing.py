"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Colin Balitewicz.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math as math
def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_cosines()
    run_test_sum_square_roots()


def run_test_sum_cosines():
    """ Tests the   sum_cosines   function. """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function.
    #   It TESTS the  sum_cosines  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # -------------------------------------------------------------------------
    expected_1=1.5403023058681398
    expected_2=1.1241554693209973
    expected_3=-.5194806481430600
    answer_1=sum_cosines(1)
    answer_2=sum_cosines(2)
    answer_3=sum_cosines(4)
    print('Test 1 expected',expected_1)
    print('Test 1 answer',answer_1)
    print('Test 2 expected',expected_2)
    print('Test 2 actual',answer_2)
    print('Test 3 expected',expected_3)
    print('Test 3 actual',answer_3)


def sum_cosines(n):
    total=0
    for k in range(n+1):
        total=total+math.cos(k)
    return total

    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the cosines of the integers
       0, 1, 2, 3, ... n, inclusive, for the given n.
    Side effects:   None.
    Example:
      If n is 3, this function returns
        cos(0) + cos(1) + cos(2) + cos(3)   which is about 0.13416.
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_cosines  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # -------------------------------------------------------------------------


def run_test_sum_square_roots():
    """ Tests the   sum_square_roots   function. """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement this function.
    #   It TESTS the  sum_square_roots  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # -------------------------------------------------------------------------
    expected_1=1.4142135623730950488
    expected_2=3.4142135623730950488
    expected_3=5.8637033051562731470
    answer_1=sum_square_roots(1)
    answer_2=sum_square_roots(2)
    answer_3=sum_square_roots(3)
    print('Test 1 expected',expected_1)
    print('Test 1 actual',answer_1)
    print('Test 2 expected',expected_2)
    print('Test 2 actual',answer_2)
    print('Test 3 expected',expected_3)
    print('Test 3 actual',answer_3)



def sum_square_roots(n):
    total=0
    for k in range(n+1):
        total=total+math.sqrt(2*k)
        print(k)
    return total
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the square roots of the integers
       2, 4, 6, 8, ... 2n    inclusive, for the given n.
           So if n is 7, the last term of the sum is
           the square root of 14 (not 7).
    Side effects:   None.
    Example:
      If n is 5, this function returns
         sqrt(2) + sqrt(4) + sqrt(6) + sqrt(8) + sqrt(10),
      which is about 11.854408.
    """
    # -------------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_square_roots  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
