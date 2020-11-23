## Last version: 13 June 2019

## A class implementing contiguous memory

class Contiguous:
    """    
    Fields: _items is a list of items
            _size is number of items that can be stored
    """

    ## Contiguous(s) produces contiguous memory of size s
    ##     and initializes all entries to None.
    ## __init__: Int -> Contiguous
    ## Requires: s is positive
    def __init__(self, s):
        self._items = []
        self._size = s
        for index in range(self._size):
            self._items.append(None)

    ## repr(self) produces a string with the sequence of values.
    ## __repr__: Contiguous -> Str
    def __repr__(self):
        to_return = "("
        for index in range(self._size - 1):
            if self.access(index) == None:
                to_print = "None"
            else:
                to_print = self.access(index)
            to_return = to_return + str(to_print) + ","
        if self.access(self._size - 1) == None:
            to_print = "None"
        else:
            to_print = self.access(self._size - 1)
        return to_return + str(to_print) +")"

    ## self.size() produces the size of self.
    ## size: Contiguous -> Int
    def size(self):
        return self._size

    ## self == other produces True if self and other have the same
    ##     size and store the same values at each index.
    ## __eq__: Contiguous Contiguous -> Bool
    def __eq__(self, other):
        if self.size() != other.size():
            return False
        else:
            for pos in range(self.size()):
                if self.access(pos) != other.access(pos):
                    return False
            return True
        
    ## self.access(index) produces the value at the given index.
    ## access: Contiguous Int -> Any
    ## Requires: 0 <= index < self._size
    def access(self, index):
        return self._items[index]

    ## self.store(index, value) stores value at the given index.
    ## Effects: Mutates self by storing value at the given index.
    ## store: Contiguous Int Any -> None
    ## Requires: 0 <= index < self._size
    def store(self, index, value):
        self._items[index] = value






        





