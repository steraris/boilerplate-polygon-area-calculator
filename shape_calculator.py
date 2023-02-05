class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def __str__(self):
        return f'''Rectangle(width={self.width}, height={self.height})'''
    def set_width(self,width):
        self.width = width
    def set_height(self,horn):
        self.height = horn
    def get_area(self):
        self.area = self.width * self.height
        return self.area
    def get_perimeter(self):
        self.perimeter = (2 * self.width) + (2 * self.height)
        return self.perimeter
    def get_diagonal(self):
        self.diagonal = ((self.width ** 2) + (self.height ** 2)) ** .5
        return self.diagonal
    def get_picture(self):
        self.stringee = ''
        if self.width > 50 or self.height > 50:
            self.stringee += 'Too big for picture.'
        else:
            for i in range(0,self.height):
                for a in range(0,self.width):
                    self.stringee += '*'
                self.stringee += '\n'
        return self.stringee
    def get_amount_inside(self,rectangle):
        self.fits_width = self.width // rectangle.width
        self.fits_height = self.height // rectangle.height
        self.fits = self.fits_height * self.fits_width
        return self.fits

class Square(Rectangle):
    def __init__(self,side):
        self.side = side
        self.height = side
        self.width = side
    def __str__(self):
        return f'''Square(side={self.side})'''
    def set_side(self,side):
        self.side = side
        self.height = side
        self.width = side
        return self.side
    def set_height(self,new_height):
        return self.set_side(new_height)
    def set_width(self,new_width):
        return self.set_side(new_width)
