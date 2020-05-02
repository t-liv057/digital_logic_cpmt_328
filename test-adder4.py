from cmpt328.logic import number_format
from cmpt328.logic.ic import *
from adders import Adder4


def main():
    adder = Adder4()

    format = number_format.unsigned(4)
    sourceA, sourceB = NumberSource(format), NumberSource(format)
    adder.A.connectAll(sourceA)
    adder.B.connectAll(sourceB)

    displaySUM = NumberDisplay(format)
    displaySUM.IN.connectAll(adder.SUM)

    # Exhaustively test every possible combination of inputs
    passes, failures = 0, 0

    for A in range(format.maximumValue() + 1):
        sourceA.setValue(A)
        for B in range(format.maximumValue() + 1):
            sourceB.setValue(B)
            for Cin in range(2):
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

                print("{:2} + {:2} + C {} = {:2} C {}    {}".format(A, B, Cin, sum, Cout,
                                                                    "PASS" if testPassed else "FAIL"))

    print("{} out of {} tests passed!".format(passes, passes + failures))
    if failures == 0:
        print("\nGood job! Move on to the next step.")
    else:
        print("\nMake sure you fix it before moving on!")


if __name__ == "__main__":
    main()
