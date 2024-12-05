
class ImagNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def asString(self):
        print(f"{self.real} {'- '+str(self.imag*(-1)) if self.imag < 0 else '+ '+str(self.imag) }i")

    def __add__(self, other):
        return ImagNumber(self.real + other.real, self.imag + self.imag)

    def __sub__(self, other):
        return ImagNumber(self.real - other.real, self.imag - self.imag)