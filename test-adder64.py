from cmpt328.logic import number_format
from cmpt328.logic.ic import *
from adders import Adder64


def main():
    adder = Adder64()

    # Use 2s complement format this time for parity with the Java version
    format = number_format.twosComplement(64)
    sourceA, sourceB = NumberSource(format), NumberSource(format)
    adder.A.connectAll(sourceA)
    adder.B.connectAll(sourceB)

    displaySUM = NumberDisplay(format)
    displaySUM.IN.connectAll(adder.SUM)

    FMT_WIDTH = format.maximumValue() + 1

    unsigned = lambda x: x if x >= 0 else (x & (2**64 - 1))

    # There are now 2^129 ≈ 6.8×10^38 possible combinations of inputs so we'll just content ourselves with running a
    # bunch of tests!
    import random
    random.seed(0)  # seed is fixed so always generates same "random" test cases
    # If the test passes, consider replacing the above line with this and running another time or two:
    # random.seed() # seed is system clock so generates different "random" test cases every time

    TEST_COUNT = 10000

    print("Running {} test cases selected at random...".format(TEST_COUNT))
    passes, failures = 0, 0
    for i in range(TEST_COUNT):
        A, B = random.randint(format.minimumValue(), format.maximumValue()), \
               random.randint(format.minimumValue(), format.maximumValue())
        Cin = random.randint(0, 1)
        sourceA.setValue(A)
        sourceB.setValue(B)
        adder.Cin.connect((Ground(), Current())[Cin])

        expectedSum = (A + B + Cin + FMT_WIDTH) % (2 * FMT_WIDTH) - FMT_WIDTH
        expectedCout = Bit((unsigned(A) + unsigned(B) + Cin) > 2 * FMT_WIDTH)
        sum = displaySUM.getValue()
        Cout = adder.Cout.getState()

        testPassed = (sum == expectedSum and Cout == expectedCout)
        if testPassed:
            passes += 1
        else:
            failures += 1

        if not testPassed:
            print("Case {:5}/{:5}: {:28,} + {:28,} + C {} = {:28,} C {}     FAIL: expected {:28,} C {}"
                  .format(i, TEST_COUNT,
                          A, B, Cin, sum, Cout,
                          expectedSum, expectedCout))
        if failures >= 50:
            print("50 test cases have failed — bailing out")
            break

    if passes + failures == TEST_COUNT:
        print("{} of {} cases passed!".format(passes, passes + failures))
    if failures == 0:
        print("\nGood job! You may wish to run again with a different random seed (see code).\n")
    else:
        print("\nMake sure you fix it before moving on!")


if __name__ == "__main__":
    main()
