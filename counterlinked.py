from linked import *

## A class implementing Counter using a singly linked list implementation

class Counter:
    """
    Fields: _first points to the first node (if any) in a singly-linked list
    """
    
    ## Counter(cap) produces a newly constructed empty counter with
    ##     capacity cap.
    ## __init__:  -> Counter
    def __init__(self, cap):
        self._first = None

    ## repr(self) produces a string of values stored in self.
    ## __repr__: Counter -> Str
    def __repr__(self):
        current = self._first
        to_return = "("
        while current != None:
            to_print = current.access()
            current = current.next()
            to_return = to_return + str(to_print) + ","
        return to_return[:-1] + ")"

    ## value in self produces True if value is a data item in self.
    ## __contains__: Counter Any -> Bool
    ## Requires: 0 <= value <= cap - 1
    def __contains__(self, value):    
        current = self._first
        while current != None:
            if value == current.access():
                return True
            current = current.next()
        return False        

    ## self.count(value) produces the number of copies of value
    ##     stored in self.                      
    ## count: Counter Any -> Int
    ## Requires: 0 <= value <= cap - 1
    def count(self, value):
        current = self._first
        count = 0
        while current != None:
            if current.access() == value:   
                count = count + 1
                current = current.next()
            else:
                current = current.next()
        return count 
        
    ## self.all() produces a list of all distinct values in self.
    ## all: Counter -> (listof Any)
    def all(self): 
        dist_list = []
        current = self._first
        while current != None:
            if current.access() not in dist_list:
                dist_list.append(current.access())
                current = current.next()
            else:
                current = current.next()
        return dist_list
    
    ## self.add(value) adds a copy of value to self.
    ## Effects: Mutates self by adding value to self.
    ## add: Counter Any -> None   
    ## Requires: 0 <= value <= cap - 1
    def add(self, value):     
        current = self._first   
        if self._first == None:
            newest_node = Single(value)
            self._first = newest_node        
        while current != None:
            next_node = current.next()
            if current.access() <= value and next_node == None:
                new_node = Single(value, next_node)
                current.link(new_node)
                break
            elif current.access() >= value:
                new_node = Single(value, current)
                self._first = new_node                  
                break
            elif current.access() <= value and value <= next_node.access(): 
                new_node = Single(value, next_node)
                current.link(new_node)                
                break
            else:
                current = current.next()        
    
    ## self.delete(value) removes a copy of value from self.
    ## Effects: Mutates self by removing a copy of value from self.
    ## delete: Counter Any -> None
    ## Requires: self contains an item with value value  
    ##           0 <= value <= cap - 1
    def delete(self, value):                                    
        current = self._first
        while current != None:
            next_node = current.next()
            if current.access() == value: 
                self._first = next_node
                break
            elif next_node.access() == value:  
                current.link(next_node.next())  
                next_node.link("None") 
                break
            else:
                current = current.next()   
    
        
