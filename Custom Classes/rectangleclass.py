# RECTANGLE CLASS
class rectangle:
    # CONSTRUCTOR , FOR REQUIRING  THE LENGTH AND WIDTH
    def __init__(self, length, width: int):
        self.length = int(length)
        self.width = int(width)
    
    # ITERATOR, FOR  MAKING THE INSTANCE ITERABLE
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}




#  MAKE AN INSTANCE OF REACTANGLE CLASS
length=float(input('Enter the length of rectangle: '))
width=float(input('Enter the width of rectangle: '))
rectangle1=rectangle(length,width)


# ITERATE OVER THE RECTANGLE INSTANCE
for side in rectangle1:
    print(side)