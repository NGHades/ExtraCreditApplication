# PROGRAMMER

# IMPORT STATEMENTS
import tkinter
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.ttk

class ApplicationView:
    # CONSTRUCTOR
    def __init__(self):
        self.__application_window = tkinter.Tk()
        self.__application_window.title("Application View")
        self.__application_window.geometry("800x600")


        self.__application_frame = tkinter.ttk.Frame(self.__application_window, title = "Application Frame")

    """
    Application Frame will contain a Canvas
    Outside Geometric Shape graphic will be centered in the Canvas
    Inside Geometric Shape graphic will be centered in the Canvas
    All File Menu selections will display an appropriate Tkinter Popup
    All Edit Menu selections will display an appropriate Tkinter Popup
    All View Menu selections will display an appropriate Tkinter Popup
    The Help Menu selections will display an appropriate Tkinter Popup
    All Exception messages will be displayed using an appropriate Tkinter Popup
    Canvas graphics will update every time that an Outside Geometric Shape value is modified
    Canvas graphics will update every time that an Inside Geometric Shape value is modified
    """
    # INSTANCE METHODS

    # File Menu
    # def edit_outside_shape_radius(self):
    #     outside_radius = tkinter.simpledialog.askfloat("Edit Outside Radius", "Enter New Outside Radius:")
    #     return outside_radius
    # def edit_outside_shape_line_color(self):
    #     outside_line_color = tkinter.simpledialog.askstring("Edit Outside Line Color","Enter New Outside Line Color:")
    #     return outside_line_color
    # def edit_outside_shape_fill_color(self):
    #     outside_fill_color = tkinter.simpledialog.askstring("Edit Outside Fill Color", "Enter New Outside Fill Color")
    #     return outside_fill_color
    # def edit_inside_shape_length(self):
    #     inside_length = tkinter.simpledialog.askfloat("Edit Inside Shape Length", "Enter New Insidem Length:")
    #     return inside_length
    # def edit_inside_shape_height(self):
    #     inside_length = tkinter.simpledialog.askfloat("Edit Inside Shape Length", "Enter New Insidem Length:")
    #     return inside_length
    # def edit_inside_shape_line_color(self):
    #     inside_line_color = tkinter.simpledialog.askstring("Edit Inside Line Color", "Enter New Inside Line Color:")
    #     return inside_line_color
    # def edit_inside_shape_fill_color(self):
    #     inside_fill_color = tkinter.simpledialog.askstring("Edit Inside Fill Color", "Enter New Inside Fill Color:")
    #     return inside_fill_color

    # # Pickle File Editing
    # def edit_pickle_outside_shape_radius(self):
    #     outside_radius = tkinter.simpledialog.askfloat("Edit Outside Radius", "Enter New Outside Radius:")
    #     return outside_radius
    # def edit_pickle_outside_shape_line_color(self):
    #     outside_line_color = tkinter.simpledialog.askstring("Edit Outside Line Color","Enter New Outside Line Color:")
    #     return outside_line_color
    # def edit_pickle_outside_shape_fill_color(self):
    #     outside_fill_color = tkinter.simpledialog.askstring("Edit Outside Fill Color", "Enter New Outside Fill Color")
    #     return outside_fill_color
    # def edit_pickle_inside_shape_length(self):
    #     inside_length = tkinter.simpledialog.askfloat("Edit Inside Shape Length", "Enter New Inside Length:")
    #     return inside_length
    # def edit_pickle_inside_shape_height(self):
    #     inside_height = tkinter.simpledialog.askfloat("Edit Inside Shape Height", "Enter New Inside Height:")
    #     return inside_height
    # def edit_pickle_inside_shape_line_color(self):
    #     inside_line_color = tkinter.simpledialog.askstring("Edit Inside Line Color", "Enter New Inside Line Color:")
    #     return inside_line_color
    # def edit_pickle_inside_shape_fill_color(self):
    #     inside_fill_color = tkinter.simpledialog.askstring("Edit Inside Fill Color", "Enter New Inside Fill Color:")
    #     return inside_fill_color