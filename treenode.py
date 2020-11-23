class Treenode:
    """
    Fields: _prev is the parent if the first child and otherwise
                 the previous sibling
            _first is the first child, if any, otherwise None
            _next is the next sibling, if any, otherwise None
            _value is the value stored in the node
    """

    ## Treenode(value) produces a newly construction node storing
    ##    the given value, with all links set to None.
    ## __init__: Any -> Treenode
    def __init__(self, value):
        self._prev = None
        self._first = None
        self._next = None
        self._value = value

    ## self.prev() produces the node, if any, linked
    ##     from by prev or None otherwise.
    ## prev: Treenode -> (anyof Treenode None)
    def prev(self):
        return self._prev

    ## self.first() produces the node, if any, linked
    ##     from self by first or None otherwise.
    ## first: Treenode -> (anyof Treenode None)
    def first(self):
        return self._first

    ## self.next() produces the node, if any, linked
    ##     from self by next or None otherwise.
    ## next: Treenode -> (anyof Treenode None)
    def next(self):
        return self._next
        
    ## self.value() produces the value of self.
    ## value: Treenode -> Any
    def value(self):
        return self._value
    
    ## self.set_prev(new) sets the previous sibling
    ##     of self to be new.
    ## prev: Treenode (anyof Treenode None) -> None
    def set_prev(self, new):
        self._prev = new

    ## self.set_first(new) sets the first child
    ##     of self to be new.
    ## first: Treenode (anyof Treenode None) -> None
    def set_first(self, new):
        self._first = new

    ## self.set_next(new) sets the previous sibling
    ##     of self to be new.
    ## next: Treenode (anyof Treenode None) -> None
    def set_next(self, new):
        self._next = new
        
    ## self.set_value(new) sets the value of self to new.
    ## value: Treenode Any -> None
    def set_value(self, new):
        self._value = new

        
    
        

