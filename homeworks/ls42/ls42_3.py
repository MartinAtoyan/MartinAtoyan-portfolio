
class Temperature:
    def __init__(self, cel):
        self._cel = cel

    @property
    def cel(self):
        return self._cel

    @cel.setter
    def cel(self, cel):
        if isinstance(cel, int) and isinstance(cel, float):
            self._cel = cel
        else:
            ValueError()

    @property
    def fahrenheit(self):
        return (self.cel * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.cel = (value - 32) * 5/9


tmp = Temperature(25)
print(tmp.fahrenheit)

tmp.fahrenheit = 32
print(tmp.cel)

