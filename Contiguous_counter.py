from contiguous import *

## A class implementing Counter using a contiguous list implementation

class Counter:
    '''
    Fields: _data containing Contiguous array
    
    '''
    ## Counter(cap) produces a newly constructed empty counter with
    ##     capacity cap.
    ## __init__:  -> Counter
    def __init__(self, cap):
        self._data = Contiguous(cap)

    ## repr(self) produces a string of values stored in self.
    ## __repr__: Counter -> Str
    def __repr__(self):
        return repr(self._data)   

    ## value in self produces True if value is a data item in self.
    ## __contains__: Counter Any -> Bool
    ## Requires: 0 <= value <= cap - 1
    def __contains__(self, value):
        if (self._data.access(value) == None):
            return False
        else:
            return True
            

    ## self.count(value) produces the number of copies of value
    ##     stored in self.
    ## count: Counter Any -> Int
    ## Requires: 0 <= value <= cap - 1
    def count(self, value):
        if (self._data.access(value) == None):
            return 0
        else:
            return self._data.access(value)        
        
        
    ## self.all() produces a list of all distinct values in self.
    ## all: Counter -> (listof Any)
    def all(self):
        dist_list = []
        for value in range(self._data._size):
            if self._data.access(value) != None:
                dist_list.append(value)
        return dist_list
                
    
    ## self.add(value) adds a copy of value to self.
    ## Effects: Mutates self by adding value to self.
    ## add: Counter Any -> None
    ## Requires: 0 <= value <= cap - 1
    def add(self, value):
        if self._data.access(value) == None:
            self._data.store(value, 1)  
        else:
            self._data.store(value, self._data.access(value) + 1)
                
   
    ## self.delete(value) removes a copy of value from self.
    ## Effects: Mutates self by removing a copy of value from self.
    ## delete: Counter Any -> None
    ## Requires: self contains an item with value value
    ##           0 <= value <= cap - 1
    def delete(self, value):
        if self._data.access(value) > 1 :
            self._data.store(value, self._data.access(value)-1)
        else:
            self._data.store(value, None)