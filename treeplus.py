## ==================================================================
## Rayan Roy (20764233)
## CS 234 Fall 2020
## Assignment 03, Problem 1
## ==================================================================

## An implementation of a tree in which each node has pointers prev (to
## previous sibling or parent), first (to first child), and next (to next
## sibling) and stores a countpair.  The countpair stores the value at the
## node and an integer that indicates the position of the node in the
## ordering of the children of its parent, starting at 0 for the first child,
## and with a value of -1 for the root.

from treenode import *
from countpair import *

class Treeplus:
    """
    Fields: _root is the root treenode or None if the tree is empty
    """

    ## Treeplus() produces an empty ordered tree.
    ## __init__: -> Treeplus
    def __init__(self):
        self._root = None   
        
    ## self.is_empty() produces True if the tree is empty and False
    ##     otherwise.
    ## is_empty: Treeplus -> Bool
    def is_empty(self):
        return (self._root == None)      

    ## self.root() produces the root of self.
    ## root: Treeplus -> Treenode
    ## Requires: self is not empty
    def root(self):
        return self._root  

    ## self.parent(node) produces the treenode that is the parent
    ##     of node, if any, and otherwise None.
    ## parent: Treeplus Treenode -> (anyof Treenode None)
    ## Requires: node is a treenode in self
    def parent(self, node):
        if node.prev() == None:                                            
            return None
        else:
            current = node                                               
            previous = node.prev()
            while previous.first() != current:
                current = previous
                previous = current.prev()
            return previous
            
        
    ## self.child(node, pos) produces the child of node in
    ##     position pos.
    ## child: Treeplus Treenode Int -> Treenode
    ## Requires: node is a treenode in self that is not a leaf
    ##           pos is in the range from 0 to the
    ##               number of children of node - 1
    def child(self, node, pos):                 
        temp_node = node.first()
        temp = 0
        for value in range(pos+1):
            if temp == pos:
                return temp_node
            else:
                temp = temp + 1
                temp_node = temp_node.next()  
        

    ## self.order(node) produces the position of node
    ##     in the ordering of the children of its parent,
    ##     where the first child is at position 0,
    ##     or -1 if node is the root.
    ## order: Treeplus Treenode -> Int
    ## Requires: node is a treenode in self
    def order(self, node):
        if node.prev() == None:
            return -1
        else:
            cur_node = node
            prev_node = node.prev()
            count = 0    #we want 0 becuse the first child is index 0
            while (prev_node.first() != cur_node):
                cur_node = prev_node
                prev_node = cur_node.prev()
                count = count + 1
            return count
        
        
    ## self._increase_all(node, offset) increases the position of
    ##     the node and all siblings after it in the order
    ##     by offset.
    ## _increase_all: Treeplus Treenode Int -> None
    ## Requires: node is a node in self
    ##           0 < offset
    def _increase_all(self, node, offset):
        if node == None:
            return
        else:
            node.value()._count = node.value()._count + offset
            curr_node = node._next
            while curr_node != None:
                curr_node.value()._count = curr_node.value()._count + offset
                curr_node = curr_node.next()
            

    ## self._decrease_all(node, offset) decreases the position of
    ##     the node and all siblings after it in the order
    ##     by offset.
    ## _decrease_all: Treeplus Treenode Int -> None
    ## Requires: node is a node in self
    ##           0 < offset
    def _decrease_all(self, node, offset):
        if node == None:
            return
        else:
            node.value()._count = node.value()._count - offset
            curr_node = node._next
            while curr_node != None:
                curr_node.value()._count = curr_node.value()._count - offset
                curr_node = curr_node.next()       
                
    ## self.add_leaf(parent, pos, value) adds a new leaf storing
    ##     value as a child of parent in position pos, where the
    ##     first position is 0; if parent is None then the new node
    ##     is the root replacing the entire tree (if any).
    ## add_leaf: Treeplus (anyof Treenode None) Int Any -> Treenode
    ## Requires: parent is either none or a Treenode in self
    ##           pos <= the number of children of parent
    def add_leaf(self, parent, pos, value):
        if parent == None or self.is_empty():
            self._root = Treenode(Countpair(value,-1))
            return self._root
        elif parent._first == None:   
            newnode = Treenode(Countpair(value,pos))
            parent.set_first(newnode)
            newnode.set_prev(parent)
            newnode._next = None
            return newnode
        elif pos == 0:
            child = parent.first()
            newnode = Treenode(Countpair(value,pos))
            parent.set_first(newnode) 
            newnode.set_prev(parent) 
            newnode.set_next(child)
            self._increase_all(parent.first().next(),1) 
            return newnode
            
        else:
            child = parent.first()
            main_val = 0
            while main_val < pos-1:
                child = child.next()
                main_val=main_val+1
                
            nxt_sib = child.next()
            if nxt_sib is None:
                child._next = Treenode(Countpair(value,pos))
                child._next._prev = child
                return child._next
                
            else:
                child._next = Treenode(Countpair(value,pos))
                child._next._next = nxt_sib
                child._next._prev = child
                child._next._next =  child._next
                self._increase_all(nxt_sib,1)    
                return child._next
            
    ## self.add_internal(parent, start, end, value) adds a
    ##     new child of parent storing value, to become the parent 
    ##     of the children of parent in positions start through end
    ##     in order after any children before start and before
    ##     any children after end, and produces the new child.
    ## add_internal: Treeplus Treenode Int Int Any -> Treenode
    ## Requires: parent is a Treenode in self
    ##           0 <= start <= end <= number of children of parent-1
    def add_internal(self, parent, start, end, value):
        offset = end - start
        if start == 0:
            node_above = self.child(parent, start) 
            newnode = Treenode(Countpair(value,start))
            newnode.set_prev(parent)
            newnode.set_next(self.child(parent, end)._next)
            newnode.set_first(node_above) 
            node_above.set_prev(newnode)
            self.child(parent, end)._next = None
            parent.set_first(newnode)
            if self.child(parent,end) != None:
                self._decrease_all(self.child(parent,end).next(), offset) 
            return newnode
        else:
            temp_ch_a = self.child(parent, start)
            temp_ch_b = self.child(parent, end)
            newnode = Treenode(Countpair(value,start))
            
            if self.child(parent,end).next() != None:
                self._decrease_all(self.child(parent,end+1), offset)
                
            newnode.set_prev(self.child(parent, start-1))
            self.child(parent, start-1)._next = newnode
            newnode.set_next(temp_ch_b._next)

            if temp_ch_b._next != None:
                temp_ch_b._next._prev = newnode
            else:
                newnode.set_next(None)
            newnode.set_first(temp_ch_a)
            temp_ch_a.set_prev(newnode)
            temp_ch_b.set_next(None)
            
            #this code is for decrementing the order of the stuff inside
            if temp_ch_a != None:
                self._decrease_all(temp_ch_a, start) 
            return newnode
        
    ## self.delete_leaf(node) deletes node from self.
    ## delete_leaf: Treeplus Treenode -> None
    ## Requires: node is a leaf in self
    def delete_leaf(self, node):
        if self.root() == node:
            self._root = None
        elif node._next == None:
            if node._prev._first == node:
            #    print("ray")
                node._prev._first = None
                node.set_first(None)
            else:
                node._prev._next = node.next()
               # print("xd")
            node._prev = None
            node._next = None
          #  node.set_value(None)
                        
        else:
            if node._prev._first == node:
                node._prev._first = node.next()
                node._next._prev = node._prev
               # parent.set_first(node.next())
            else:
                node._prev._next = node.next()
                node._next._prev = node._prev
            self._decrease_all(node._next,1)
            node._prev = None
            node._next = None 
            node.set_value(None)
            node.set_first(None)             
            

    ## self.delete_internal(node) deletes node from self; if
    ##     node is the root, the tree becomes empty; otherwise,
    ##     the children of the node become children of the grandparent
    ##     in order starting at the position of the deleted node.
    ## delete_internal: Treeplus Treenode -> None
    ## Requires: node is an internal node
    def delete_internal(self, node):
        if self.root() == node:
            self._root = None
        elif node._first == None: #base case
           # print("ahlie")
            self.delete_leaf(node) 
        else:
            #we want to find total children, so we can decrease/increase stuff
            index = 0
            sibling = node._first                   
           # print(sibling)
           
            while sibling != None:
                sibling = sibling._next
                index = index+1
               # print(sibling)
                #no siblings but child of the nodes
            
            if index == 0:
               # print("joe")
                self.delete_leaf(node)
            
            #fixed 
            elif (node._prev == self.parent(node)) and (node.next() == None): 
                node._prev._first = node._first
               # print(node._first._prev.value())
              #  print(node._prev._first.value())
                node._first._prev = node._prev
                node.set_prev(None)
                node.set_next(None)
                node.set_value(None)
                node.set_first(None)           
             #last part of the node (fixed)
            elif (node._prev != self.parent(node)) and (index >= 1) and node.next() == None:
              #  print("hello")
                node._prev._next = node._first
                node._first._prev = node._prev
              #  print(index)
                #To get the previous index
                counter = node._prev._value._count
              #  print(counter)
                self._increase_all(node._prev._next, counter+1)       

                node.set_prev(None)
                node.set_first(None)
                node.set_next(None)
                node.set_value(None)               
            
            #causing trouble
            #first child with some indexes
            elif (node._prev == self.parent(node)) and (index >= 1) and node.next() != None:
                node._first._prev = node._prev
                self.parent(node)._first = node._first 
                self._increase_all(node._next,index-1)
                node._next._prev = self.child(node, index -1) #link the last offsring to parent
                self.child(node, index -1)._next = node._next
                node.set_prev(None)
                node.set_first(None)
                node.set_next(None)
                node.set_value(None)                                
            elif (node._prev != self.parent(node)) and (index >= 1) and node.next() != None:
                node._prev._next = node._first
                node._first._prev = node._prev
                self._increase_all(node._next,index-1)
                self.child(node, index -1)._next = node.next()
                node._next._prev = self.child(node, index -1)
                #changing the count of value
                counter = node._prev._value._count 
                
                new_val = 0
                while new_val < index:
                    self.child(node, counter)._value._count = counter + 1
                    counter = counter +1
                    new_val = new_val + 1
                node.set_prev(None)
                node.set_first(None)
                node.set_next(None)
                node.set_value(None)
                           
                