import tkinter as tk


# def quit_app():
#     my_window.destroy()

def red_colour():
    my_window['bg'] = 'red'


def blue_colour():
    my_window['bg'] = 'blue'


def green_colour():
    my_window['bg'] = 'green'


my_window = tk.Tk()
# my_menu = tk.Menu(my_window)
# my_menu.add_command(label='Red', command=red_colour)
# # my_menu.add_command(label='Quit', command=quit_app)
# my_menu.add_command(label='Blue', command=blue_colour)
# my_menu.add_command(label='Green', command=green_colour)

my_menubar = tk.Menu(my_window)
my_dropdown_menu = tk.Menu(my_menubar, tearoff=False)
my_dropdown_menu.add_command(label='Red', command=red_colour)
my_dropdown_menu.add_command(label='Blue', command=blue_colour)
my_dropdown_menu.add_command(label='Green', command=green_colour)
my_menubar.add_cascade(label='Colour', menu=my_dropdown_menu)
my_window.config(menu=my_menubar)


my_window.mainloop()
