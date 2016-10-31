def handle_menu_choice(choice):
    '''
        does whatever choice means to do in the menu. Choice must be a valid menu choice otherwise behavior is unspecified'''

    if choice == AREA_OF_CIRCLE:
        area_of_circle()

    elif choice == CIRCUMFERENCE_OF_CIRCLE:
        circumference_of_circle()

    elif choice == AREA_OF_RECTANGLE:
        area_of_rectangle()

    elif choice == CIRCUMFERENCE_OF_RECTANGLE:
        perimeter_of_rectangle()

    elif choice == QUIT
