# adders.py
    
from cmpt328.logic import *
from cmpt328.logic.gates import *
    
class HalfAdder:

    def __init__(self):
        # Inputs to the circuit: InputLines
        self.A = InputLine()
        self.B = InputLine()

        sum = XorGate(self.A, self.B)
        c = AndGate(self.A, self.B)
        # Sum is xor of A and B
        # Carry is and of A and B
        
        # Your code should finish with definitions of the outputs:
        self.SUM = sum  # one of the gates you created above
        self.C = c   # one of the gates you created above

class FullAdder:
    def __init__(self):
        # Inputs to the circuit: InputLines
        self.A = InputLine()
        self.B = InputLine()
        self.Cin = InputLine()

        adder1 = HalfAdder()
        adder2 = HalfAdder()
        adder1.A.connect(self.A)
        adder1.B.connect(self.B)
        adder2.A.connect(adder1.SUM)
        adder2.B.connect(self.Cin)

        cout = OrGate(adder1.C, adder2.C)

        self.SUM = adder2.SUM  # one of the gates you created above
        self.Cout = cout  # one of the gates you created above

class Adder4:
    def __init__(self):
        # Inputs to the circuit: InputLines
        self.A = InputMultiLine(4)
        self.B = InputMultiLine(4)
        self.Cin = InputLine()
        self.Cout = Line()

        adder1 = FullAdder()
        adder1.Cin.connect(self.Cin)
        adder1.A.connect(self.A.getLine(0))
        adder1.B.connect(self.B.getLine(0))

        adder2 = FullAdder()
        adder2.Cin.connect(adder1.Cout)
        adder2.A.connect(self.A.getLine(1))
        adder2.B.connect(self.B.getLine(1))


        adder3 = FullAdder()
        adder3.Cin.connect(adder2.Cout)
        adder3.A.connect(self.A.getLine(2))
        adder3.B.connect(self.B.getLine(2))

        adder4 = FullAdder()
        adder4.Cin.connect(adder3.Cout)
        adder4.A.connect(self.A.getLine(3))
        adder4.B.connect(self.B.getLine(3))

        cout = adder4.Cout

        self.SUM = MultiLine.of(adder1.SUM, adder2.SUM, adder3.SUM, adder4.SUM)  # one of the gates you created above
        self.Cout = cout  # one of the gates you created above


class Adder16:
    def __init__(self):
        # Inputs to the circuit: InputLines
        self.A = InputMultiLine(16)
        self.B = InputMultiLine(16)
        self.Cin = InputLine()
        self.Cout = InputMultiLine(16)

        adder1 = Adder4()
        adder1.Cin.connect(self.Cin)
        adder1.A.connectAll((self.A.lineRange(0,4)))
        adder1.B.connectAll((self.B.lineRange(0,4)))

        adder2 = Adder4()
        adder2.Cin.connect(adder1.Cout)
        adder2.A.connectAll((self.A.lineRange(4,8)))
        adder2.B.connectAll((self.B.lineRange(4,8)))


        adder3 = Adder4()
        adder3.Cin.connect(adder2.Cout)
        adder3.A.connectAll((self.A.lineRange(8,12)))
        adder3.B.connectAll((self.B.lineRange(8,12)))

        adder4 = Adder4()
        adder4.Cin.connect(adder3.Cout)
        adder4.A.connectAll((self.A.lineRange(12,16)))
        adder4.B.connectAll((self.B.lineRange(12,16)))

        cout = adder4.Cout

        self.SUM = MultiLine.join(adder1.SUM, adder2.SUM, adder3.SUM, adder4.SUM)  # one of the gates you created above
        self.Cout = cout  # one of the gates you created above

class Adder64:
    def __init__(self):
        # Inputs to the circuit: InputLines
        self.A = InputMultiLine(64)
        self.B = InputMultiLine(64)
        self.Cin = InputLine()
        self.Cout = InputMultiLine(16)

        adder1 = Adder16()
        adder1.Cin.connect(self.Cin)
        adder1.A.connectAll((self.A.lineRange(0,16)))
        adder1.B.connectAll((self.B.lineRange(0,16)))

        adder2 = Adder16()
        adder2.Cin.connect(adder1.Cout)
        adder2.A.connectAll((self.A.lineRange(16,32)))
        adder2.B.connectAll((self.B.lineRange(16,32)))


        adder3 = Adder16()
        adder3.Cin.connect(adder2.Cout)
        adder3.A.connectAll((self.A.lineRange(32,48)))
        adder3.B.connectAll((self.B.lineRange(32,48)))

        adder4 = Adder16()
        adder4.Cin.connect(adder3.Cout)
        adder4.A.connectAll((self.A.lineRange(48,64)))
        adder4.B.connectAll((self.B.lineRange(48,64)))

        cout = adder4.Cout

        self.SUM = MultiLine.join(adder1.SUM, adder2.SUM, adder3.SUM, adder4.SUM)  # one of the gates you created above
        self.Cout = cout  # one of the gates you created above