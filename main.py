import arcade
from mpmath import mp
import time

def draw_axes():
    for x in range(0, 601, 15):
        arcade.draw_line(x, 0, x, 600, arcade.color.BLACK, 1)
    for y in range(0, 601, 15):
        arcade.draw_line(0, y, 800, y, arcade.color.BLACK, 1)

def draw_function(a: int, b: int):
    x1 = 0
    y1 = (float(a) * x1 - (float(a) * 300 - 300)) + (float(b) * 15)
    x2 = 600
    y2 = (float(a) * x2 - (float(a) * 300 - 300)) + (float(b) * 15)
    arcade.draw_line(0, 300, 600, 300, arcade.color.BLACK, 3)
    arcade.draw_text('x', 580, 272, arcade.color.BLACK, 24)
    arcade.draw_line(300, 0, 300, 600, arcade.color.BLACK, 3)
    arcade.draw_text('y', 280, 575, arcade.color.BLACK, 24)
    arcade.draw_line(x1, y1, x2, y2, arcade.color.RED, 3)

def menu():
    print('A program that solves the type of calculation given by the user.')
    print('Author: Wiktor Wasinski')
    print('')
    print('1 - drawing a linear function')
    print('2 - are linear functions perpendicular?')
    print('3 - are the linear functions parallel?')
    print('4 - is the linear function constant, increasing or decreasing?')
    print('5 - print π')
    option = int(input('Choose the type of calculation: '))
    print('')
    match option:
        case 1: option1()
        case 2: option2()
        case 3: option3()
        case 4: option4()
        case 5: option5()
        case _: invalid_option()

def option1(): # Drawing a linear function
    # Input of coefficients
    a = input('Enter "a": ')
    b = input('Enter "b": ')
    function = 'y=' + a + 'x+' + b
    print(function)
    # Drawing function
    arcade.open_window(600, 600, 'Graph of the function ' + function)
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()
    draw_axes()
    draw_function(a,b)
    arcade.finish_render()
    arcade.run()

def option2():  # Are linear functions perpendicular?
    # Input of coefficients
    a1 = input('Enter "a1": ')
    b1 = input('Enter "b1": ')
    a2 = input('Enter "a2": ')
    b2 = input('Enter "b2": ')
    function1 = 'y=' + a1 + 'x+' + b1
    print(function1)
    function2 = 'y=' + a2 + 'x+' + b2
    print(function2)
    # Are linear functions perpendicular?
    if float(a1) * float(a2) == -1:
        print('The functions are perpendicular.')
    else:
        print('The functions are not perpendicular.')
    input('Press any key to finish.')

def option3():  # Are the linear functions parallel?
    # Input of coefficients
    a1 = input('Enter "a1": ')
    b1 = input('Enter "b1": ')
    a2 = input('Enter "a2": ')
    b2 = input('Enter "b2": ')
    function1 = 'y=' + a1 + 'x+' + b1
    print(function1)
    function2 = 'y=' + a2 + 'x+' + b2
    print(function2)
    # Are the linear functions parallel?
    if a1 == a2 and b1 == b2:
        print('The functions overlap.')
    elif a1 == a2:
        print('The functions are parallel.')
    else:
        print('The functions are not parallel.')
    input('Press any key to finish.')

def option4():  # Is the linear function constant, increasing or decreasing?
    # Input of coefficients
    a = input('Enter "a": ')
    b = input('Enter "b": ')
    function = 'y=' + a + 'x+' + b
    print(function)
    # Is the linear function constant, increasing or decreasing?
    if float(a) > 0:
        print('The function is increasing.')
    elif float(a) < 0:
        print('The function is decreasing.')
    else:
        print('The function is constant.')
    input('Press any key to finish.')

def option5():  # Print π
    accuracy = input('Enter the number of digits to be displayed: ')
    mp.dps = int(accuracy)
    tik = time.perf_counter()
    print('π=' + str(mp.pi))
    tok = time.perf_counter()
    print(f'Finished in {tok - tik:0.4f} second(s).')
    input('Press any key to finish.')

def invalid_option():
    input('Invalid value. Try again.')

menu() # <--- Here start program
