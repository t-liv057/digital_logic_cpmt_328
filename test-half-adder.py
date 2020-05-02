from cmpt328.logic.lines import *
from cmpt328.logic.bits import *
from adders import HalfAdder


def main():
    adder = HalfAdder()

    def test(A, B, expectedSum, expectedC):
        adder.A.connect(A)
        adder.B.connect(B)

        SUM = adder.SUM.getState()
        C = adder.C.getState()

        print("{} + {} = {} C {}     {}".format(A.getState(), B.getState(), SUM, C,
                                                "PASS" if (SUM == expectedSum and C == expectedC) else "FAIL"))

    GROUND, CURRENT = Ground(), Current()
    ZERO, ONE = Bit.ZERO, Bit.ONE
    test(GROUND, GROUND,  ZERO, ZERO)
    test(GROUND, CURRENT,  ONE, ZERO)
    test(CURRENT, GROUND,  ONE, ZERO)
    test(CURRENT, CURRENT, ZERO, ONE)


if __name__ == "__main__":
    main()
