# PROGRAMMER: Terrence Chung

# IMPORT STATEMENTS

class Inside_Geometric_Shape: #Rectangle

    # CONSTRUCTOR
    def __init__(self, length, height, line_color, fill_color):


        # LENGTH EXCEPTIONS
        if not isinstance(length, int) and not isinstance(length, float):
            raise TypeError("Inside_Geometric_Shape.py __init__ length - length must be a valid integer or float.")
        if length <= 0:
            raise ValueError("Inside_Geometric_Shape.py __init__ length - length must be greater than zero.")


        # HEIGHT EXCEPTIONS
        if not isinstance(height, int) and not isinstance(height, float):
            raise TypeError("Inside_Geometric_Shape.py __init__ height - height must be a valid integer or float.")
        if height <= 0:
            raise ValueError("Inside_Geometric_Shape.py __init__ height - height must be greater than zero.")


        valid_colors = ("red", "white", "blue", "orange", "white", "black", "green", "yellow", "purple")
        # LINE_COLOR EXCEPTIONS
        if not isinstance(line_color, str):
            raise TypeError("Inside_Geometric_Shape.py __init__ line_color - line color must be a valid string.")
        if line_color.lower() not in valid_colors:
            raise ValueError("Inside_Geometric_Shape.py __init__ line_color - line color must be a valid color (Red, White, Blue, Orange, White, Black, Green, Yellow, Purple)")


        # FILL_COLOR EXCEPTIONS
        if not isinstance(fill_color, str):
            raise TypeError("Inside_Geometric_Shape.py __init__ fill_color - fill color must be a valid string.")
        if fill_color.lower() not in valid_colors:
            raise ValueError("Inside_Geometric_Shape.py __init__ fill_color - fill color must be a valid color (Red, White, Blue, Orange, White, Black, Green, Yellow, Purple)")


        # INSTANCE VARIABLES
        self.__length = length
        self.__height = height
        self.__line_color = line_color
        self.__fill_color = fill_color


    # INSTANCE METHODS
    def get_length(self):
        return self.__length

    def get_height(self):
        return self.__height

    def get_line_color(self):
        return self.__line_color

    def get_fill_color(self):
        return self.__fill_color

    def set_length(self, length):
        pass

    def set_height(self, height):
        pass

    def set_line_color(self, line_color):
        pass

    def set_fill_color(self, fill_color):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass