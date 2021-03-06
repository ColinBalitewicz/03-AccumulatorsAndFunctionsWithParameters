"""
This module demonstrates and practices:
  -- using ARGUMENTs in function CALLs,
  -- having PARAMETERs in function DEFINITIONs, and
  -- RETURNING a value from a function,
        possibly CAPTURING the RETURNED VALUE in a VARIABLE.
  -- UNIT TESTING.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Colin Balitewicz.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import m4t_tester
import math as math

def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_of_digits()
    run_test_digits_in_cube()
    run_test_digits_in_power()
    run_test_fancy_sums_of_digits()

    # -------------------------------------------------------------------------
    # DONE: 9. DO THIS LAST!
    #    -- Uncomment the line of code below to run the main function
    #         in m4t_tester.py (do not make changes to it).
    #         It runs OUR tests on your code.
    #    -- Check to see whether all test cases indicate they
    #          "COMPLETED SUCCESSFULLY!"
    #    -- If your code fails any of OUR tests but passes YOUR tests,
    #         then you are likely not TESTING the methods correctly.
    #       ** Ask a TA or your professor for help in that case. **
    # -------------------------------------------------------------------------

    m4t_tester.main()


def run_test_sum_of_digits():
    """ Tests the  sum_of_digits   function. """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this TEST function, as follows:
    #
    #  Step 1:  This TEST function tests the  sum_of_digits  function.
    #    So read the doc-string of the  sum_of_digits  function
    #    defined below.  Be sure that you understand from the
    #    doc-string what the  sum_of_digits  function SHOULD return.
    #
    #  Step 2:  Pick a test case:  a number that you could send as
    #    an actual argument to the  sum_of_digits  function.
    #      - For example, you could pick the test case  826.
    #
    #  Step 3: Figure out the CORRECT (EXPECTED) answer for your
    #    test case.  In the example of  826  the correct answer
    #    for the sum of its digits is  8 + 2 + 6, which is 16.
    #
    #  Step 4: Write code that prints both the EXPECTED answer
    #    and the ACTUAL answer returned when you call the function.
    #    See the example below.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_of_digits   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 16
    answer = sum_of_digits(826)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    # -------------------------------------------------------------------------
    # TO DO: 2 (continued).
    # Below this comment, add 3 more test cases of your own choosing.
    # -------------------------------------------------------------------------
    expected_2=14
    expected_3=21
    expected_4=19
    answer_2=sum_of_digits(9230)
    answer_3=sum_of_digits(3189)
    answer_4=sum_of_digits(7921)
    print('Test 2 expected',expected_2)
    print('actual 2',answer_2)
    print('Test 3 expected',expected_3)
    print('actual 3',answer_3)
    print('Test 4 expected',expected_4)
    print('actual 4',answer_4)
def sum_of_digits(number):
    """
    What comes in:  An integer.
    What goes out:  The sum of the digits in the given integer.
    Side effects:   None.
    Example:
      If the integer is 83135,
      this function returns (8 + 3 + 1 + 3 + 5), which is 20.
    """
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch this function - it has no TO DO in it.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the other problems.
    #
    # Ask for help if you are unsure what it means to CALL a function.
    # The ONLY part of this function that you need to understand is
    # the doc-string above.  Treat this function as a black box.
    # -------------------------------------------------------------------------
    if number < 0:
        number = -number

    digit_sum = 0
    while True:
        if number == 0:
            break
        digit_sum = digit_sum + (number % 10)
        number = number // 10

    return digit_sum


def run_test_digits_in_cube():
    """ Tests the   digits_in_cube   function. """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function.
    #   It TESTS the  digits_in_cube  function defined below.
    #   Include at least **   3   ** tests.
    #
    # To implement this TEST function, use the same 4 steps as above:
    #
    #   Step 1: Read the doc-string of  digits_in_cube  below.
    #     Understand what that function SHOULD return.
    #
    #   Step 2:  Pick a test case:  a number(s) that you could send as
    #     actual argument(s) to the  digits_in_cube  function.
    #
    #  Step 3: Figure out the CORRECT (EXPECTED) answer for your test case.
    #
    #  Step 4: Write code that prints both the EXPECTED answer
    #    and the ACTUAL answer returned when you call the function.
    #    Follow the same form as in previous examples.
    #
    #   Include at least **   3   ** tests.
    # -------------------------------------------------------------------------
    expected_5=9
    expected_6=10
    expected_7=8
    answer_5=digits_in_cube(6)
    answer_6=digits_in_cube(7)
    answer_7=digits_in_cube(8)

    print('Test 5 expected',expected_5)
    print('Test 5 actual',answer_5)
    print('Test 6 expected',expected_6)
    print('Test 6 answer',answer_6)
    print('Test 7 expected',expected_7)
    print('Test 7 actual',answer_7)



def digits_in_cube(n):
    answer=n**3
    return sum_of_digits(answer)
    """
    What comes in:  A positive integer.
    What goes out:  The sum of the digits in the CUBE of the integer.
    Side effects:   None.
    Example:
      If the integer (n) is 5    (so n cubed is 125),
      this function returns (1 + 2 + 5), which is 8.
    """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    ###########################################################################
    # IMPORTANT: CALL, as many times as needed,
    #    the    sum_of_digits    function that is DEFINED ABOVE.
    ###########################################################################
    # -------------------------------------------------------------------------


def run_test_digits_in_power():
    """ Tests the   digits_in_power   function. """
    # -------------------------------------------------------------------------
    # DONE: 5. Implement this function.
    #   It TESTS the  digits_in_power  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous TEST functions.
    # -------------------------------------------------------------------------
    expected_1=1
    expected_2=10
    expected_3=9
    answer_1=digits_in_power(1,1)
    answer_2=digits_in_power(2,6)
    answer_3=digits_in_power(3,4)
    print('Test 1 answer expected',expected_1)
    print('Test 1 actual answer',answer_1)
    print('Test 2 expected answer',expected_2)
    print('Test 2 actual answer',answer_2)
    print('Test 3 expected answer',expected_3)
    print('Test 3 actual answer',answer_3)



def digits_in_power(n, k):
    x=n**k
    sum_of_digits(x)
    return sum_of_digits(x)
    """
    What comes in:  Two positive integers, n and k.
    What goes out:
      The sum of the digits in x, where x is n raised to the kth power.
    Side effects:   None.
    Example:
      If the arguments are 12 and 3, respectively,
      this function returns 18
      since 12 to the 3rd power is 1728 (whose digits sum to 18).
    """
    # -------------------------------------------------------------------------
    # DONE: 6. Implement and test this function.
    #
    ###########################################################################
    # IMPORTANT: CALL, as many times as needed,
    #    the    sum_of_digits    function that is DEFINED ABOVE.
    ###########################################################################
    # -------------------------------------------------------------------------


def run_test_fancy_sums_of_digits():
    """ Tests the   fancy_sums_of_digits   function. """
    # -------------------------------------------------------------------------
    # DONE: 7. Implement this function.
    #   It TESTS the  fancy_sums_of_digits  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing the previous
    # TEST functions.
    # -------------------------------------------------------------------------
    expected_1=1
    expected_2=1
    expected_3=1
    answer_1=fancy_sums_of_digits(1)
    answer_2=fancy_sums_of_digits(10)
    answer_3=fancy_sums_of_digits(100)
    print('Test 1 expected',expected_1)
    print('Test 1 actual',answer_1)
    print('Test 2 expected',expected_2)
    print('Test 2 actual',answer_2)
    print('Test 3 expected',expected_3)
    print('Test 3 actual',answer_3)

    # -------------------------------------------------------------------------
    # HINT:  For your 1st test, consider  n=10.  Figure out BY HAND
    # the correct (expected) answer for that test case.  (It's easy.)
    # The doc-string below gives test cases you can use for
    # your 2nd and 3rd tests but READ THOSE TEST CASES CAREFULLY
    # in the doc-string to be sure that you understand the specification.
    # -------------------------------------------------------------------------


def fancy_sums_of_digits(n):
    x=sum_of_digits(n**1000)
    y=sum_of_digits(n**999)
    return sum_of_digits(x**y)

    """
    What comes in:  A positive integer n.
    What goes out:
      -- Let X denote the   sum   of the digits in (n ** 1000).
      -- Let Y denote the   sum   of the digits in (n ** 999).
      This function RETURNs the sum of the digits in (X ** Y).
    Side effects:   None.
    Examples:
      -- If n is 2, then:
            -- the   sum   of the digits in n ** 1000 is 1366 (trust me!).
            -- the   sum   of the digits in n ** 999 is 1367 (trust me!).
            -- so X ** Y is VERY LARGE in this case
                     (don't try to print it!)
            -- the   sum   of the digits in (X ** Y) is 19084 (trust me!)
            -- so this function returns 19084.
      -- If n is 35, then:
            -- the sum of the digits in n ** 1000 is 7021 (trust me!).
            -- the sum of the digits in n ** 999 is 7145 (trust me!).
            -- so X ** Y is VERY LARGE in this case
                     (don't try to print it!)
            -- the sum of the digits in (X ** Y) is 124309 (trust me!)
            -- so this function returns 124309.
    """
    # -------------------------------------------------------------------------
    # DONE: 8. Implement and test this function.
    #
    ###########################################################################
    # IMPORTANT: CALL, as many times as needed,
    #    the    sum_of_digits    function that is DEFINED ABOVE.
    ###########################################################################
    # -------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# This unusual form is necessary for the special testing we provided.
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
