class Countpair:
    """
    Fields: _value stores any value
            _count stores an integer
    """

    ## Countpair(value, count) produces a newly constructed Countpair
    ##     storing value and count.
    ## __init__: Any Int -> Countpair
    def __init__(self, value, count=0):
        self._value = value
        self._count = count

    ## repr(self) produces a string with the information in self.
    ## __repr__: Countpair -> Str
    def __repr__(self):
        return str(self._value) + ": " + str(self._count)

    ## self.value() produces the value stored in self.
    ## value: Countpair -> Any
    def value(self):
        return self._value

    ## self.count() produces the count stored in self.
    ## count: Countpair -> Int
    def count(self):
        return self._count
    
    ## self.set_value(new) sets the value stored in self to new
    ## Effects: Mutates self by storing new as value in self.
    ## set_value: Countpair Any -> None
    def set_value(self, new):
        self._value = new

    ## self.set_count(new) sets the count stored in self to new
    ## Effects: Mutates self by storing new as count in self.
    ## set_count: Countpair Int -> None
    def set_count(self, new):
        self._count = new

        
