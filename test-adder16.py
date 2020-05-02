from cmpt328.logic import number_format
from cmpt328.logic.ic import *
from adders import Adder16


def main():
    adder = Adder16()

    format = number_format.unsigned(16)
    sourceA, sourceB = NumberSource(format), NumberSource(format)
    adder.A.connectAll(sourceA)
    adder.B.connectAll(sourceB)

    displaySUM = NumberDisplay(format)
    displaySUM.IN.connectAll(adder.SUM)

    # There are now 2^33 ≈ 8.6 bn possible combinations of inputs so we'll just content ourselves with running a
    # bunch of tests!
    import random
    random.seed(9654263354)  # seed is fixed so always generates same "random" test cases
    # If the test passes, consider replacing the above line with this and running another time or two:
    # random.seed() # seed is system clock so generates different "random" test cases every time

    TEST_COUNT = 50000

    print("Running {} test cases selected at random...".format(TEST_COUNT))
    passes, failures = 0, 0
    for i in range(TEST_COUNT):
        A, B = random.randint(0, format.maximumValue()), random.randint(0, format.maximumValue())
        Cin = random.randint(0, 1)
        sourceA.setValue(A)
        sourceB.setValue(B)
        adder.Cin.connect((Ground(), Current())[Cin])

        expectedSum = (A + B + Cin) % (format.maximumValue() + 1)
        expectedCout = Bit((A + B + Cin) > format.maximumValue())
        sum = displaySUM.getValue()
        Cout = adder.Cout.getState()

        testPassed = (sum == expectedSum and Cout == expectedCout)
        if testPassed:
            passes += 1
        else:
            failures += 1

        if not testPassed:
            print("Case {:5}/{:5}: {:5} + {:5} + C {} = {:5} C {}     FAIL: expected {:5} C {}"
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
