from cmpt328.logic.lines import *
from cmpt328.logic.bits import *
from adders import FullAdder


def main():
    adder = FullAdder()

    def test(A, B, Cin, expectedSum, expectedCout):
        adder.A.connect(A)
        adder.B.connect(B)
        adder.Cin.connect(Cin)

        SUM = adder.SUM.getState()
        Cout = adder.Cout.getState()

        print("{} + {} + C {} = {} C {}     {}".format(A.getState(), B.getState(), Cin.getState(), SUM, Cout,
                                                "PASS" if (SUM == expectedSum and Cout == expectedCout) else "FAIL"))

    GROUND, CURRENT = Ground(), Current()
    ZERO, ONE = Bit.ZERO, Bit.ONE
    test(GROUND, GROUND, GROUND,  ZERO, ZERO)
    test(GROUND, GROUND, CURRENT,  ONE, ZERO)
    test(GROUND, CURRENT, GROUND,  ONE, ZERO)
    test(GROUND, CURRENT, CURRENT, ZERO, ONE)
    test(CURRENT, GROUND, GROUND,  ONE, ZERO)
    test(CURRENT, GROUND, CURRENT,  ZERO, ONE)
    test(CURRENT, CURRENT, GROUND,  ZERO, ONE)
    test(CURRENT, CURRENT, CURRENT, ONE, ONE)


if __name__ == "__main__":
    main()
