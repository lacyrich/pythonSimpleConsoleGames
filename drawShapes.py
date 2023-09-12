# -*- coding: utf-8 -*-

#asks user for inputs then creates triangle
def draw_inverted_right_triangle() :
    triangle_size = input("Enter the size of your triangle as an integer >= 2, example 6: ")
    while not triangle_size.isdigit() or not int(triangle_size) >= 2:
        triangle_size = input("Invalid input. Enter the size of your triangle as an integer >= 2, example 6: ")
    triangle_size = int(triangle_size)
    character = input("Enter a single character you want to make the shape with: ")
    while len(character) > 1 or len(character) < 0:
        character = input("Invalid input. Enter a single character you want to make the shape with: ")
    for i in range(1,triangle_size+1): 
        for j in range((triangle_size+1)-i):
            print(character, end=' ') 
        print()
#asks user for inputs then creates rectangle
def draw_rectangle() :
    length = input("Enter the length of your rectangle as an integer >= 2: ")
    while not length.isdigit() or not int(length) >= 2:
        length = input("Invalid input. Enter the length of your rectangle as an integer >= 2: ")
    length = int(length)
    width = input("Enter the width of your rectangle as an integer >= 2: ")
    while not width.isdigit() or not int(width) >= 2:
        width = input("Invalid input. Enter the width of your rectangle as an integer >= 2: ")
    width = int(width)
    character = input("Enter a single character you want to make the shape with: ")
    while len(character) > 1 or len(character) < 0:
        character = input("Invalid input. Enter a single character you want to make the shape with: ")       
    for i in range(width): 
        for j in range(length):
            print(character, end=' ') 
        print()
 #gives user choice between triangle and rectangle, allowing for only rectangle and triangle to be entered. Then calls whichever the user chose
def draw_shapes() : 
    shape_selection = input("Enter 1 to draw an inverted right 'triangle' or 'rectangle' to draw a rectangle: ").lower()
    while shape_selection != "triangle" and shape_selection !="rectangle":
        shape_selection = input("Invalid Input. Enter 'triangle' to draw an inverted right triangle or 'rectangle' to draw a rectangle: ").lower()
    if shape_selection == "triangle":
        draw_inverted_right_triangle()
    else: 
        draw_rectangle() 
    input("Press enter to continue...")