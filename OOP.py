class Square:
    def __init__(self):
      self.__height = 2
      self.__width = 2

square = Square()
#square.height = 3 # not a square anymore
print(vars(square))
print(square._Square__height)
square.__height = 4
print(vars(square))
print(square.__height)
print(square._Square__height)