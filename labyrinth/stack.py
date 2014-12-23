
from linkedlist import LinkedList


class Stack:

    def __init__( self ):
        self.stack = LinkedList()


    def push( self, item ):
        self.stack.addFirst(item)


    def pop( self ):
        removed = self.top()
        self.stack.removePosition(0)
        return removed.data


    def top( self ):
        return self.stack.getFirst()
        #return self.stack.getPosition(self.stack.getSize()-1)


    def isEmpty( self ):
        size = self.stack.getSize()
        if size<=0:
            return True
        else:
            return False


