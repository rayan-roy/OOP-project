## Last version: 24 September 2019

## Classes implementing different types of nodes for linked data structures

class Single:
    """
    Fields: _value stores any value
            _next stores the next node or None, if none
   """

    ## Single(value, next) produces a newly constructed singly-linked 
    ##     node storing value with a link to next, where next has the
    ##     default value None.
    ## __init__: Any (anyof Single None) -> Single
    def __init__(self, value, next = None):
        self._value = value
        self._next = next

    ## repr(self) produces a string with the information in self.
    ## __repr__: Single -> Str
    def __repr__(self):
        if self._value == None:
            return "Empty node"
        else:
            return str("Node containing " + str(self._value))

    ## self.access() produces the value stored in self.
    ## access: Single -> Any
    def access(self):
        return self._value

    ## self.next() produces the node to which self is linked
    ##    or None if none exists.
    ## next: Single -> (anyof Single None)
    def next(self):
        return self._next

    ## self.store(value) stores value in self.
    ## Effects: Mutates self by storing value in self.
    ## store: Single, Any -> None
    def store(self, value):
        self._value = value

    ## self.link(node) links node using the next pointer.
    ## Effects: Mutates self by linking node using the next pointer.    
    ## link: Single (anyof Single None) -> None
    def link(self, node):
        self._next = node

class Double:
    """
    Fields: _value stores any value
            _next points to the next node in the list
            _prev points to the previous node in the list
    """

    ## Double(value, next, prev) produces a newly constructed
    ##     doubly-linked node storing value with a next pointer
    ##     to next and a prev pointer to prev, where next and prev
    ##     have the default values of None.
    ## __init__: Any (anyof Double None) (anyof Double None) -> Double
    def __init__(self, value, next = None, prev = None):
        self._value = value
        self._next = next
        self._prev = prev

    ## repr(self) produces a string with the information in self.
    ## __repr__: Double -> Str
    def __repr__(self):
        if self._value == None:
            return "Empty node"
        else:
            return str("Node containing " + str(self._value))

    ## self.access() produces the value stored in self.
    ## access: Double -> Any
    def access(self):
        return self._value

    ## self.next() produces the node to which self is linked
    ##    using next or None if none exists.
    ## next: Double -> (anyof Double None)
    def next(self):
        return self._next

    ## self.prev() produces the node to which self is linked
    ##    using prev or None if none exists.
    ## prev: Double -> (anyof Double None)
    def prev(self):
        return self._prev

    ## self.store(value) stores value in self.
    ## Effects: Mutates self by storing value in self.
    ## store: Double, Any -> None
    def store(self, value):
        self._value = value

    ## self.link_next(node) links node using the next pointer.
    ## Effects: Mutates self by linking node using the next pointer.    
    ## link_next: Double (anyof Double None) -> None
    def link_next(self, node):
        self._next = node

    ## self.link_prev(node) links node using the prev pointer.
    ## Effects: Mutates self by linking node using the prev pointer.
    ## link_prev: Double (anyof Double None) -> None
    def link_prev(self, node):
        self._prev = node
        
