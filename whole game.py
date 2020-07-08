class Game:
############################################################
#create_the_main_class_for_the_whole_game
    def __init__(self):
##############################################################
    #print_all_the_following_statments_after_running_directly
        print('welcome in the full game...^_^')
        print('this game contains many small games')
        print('choose number to play your game')
        print('press [1] to play even and odd guess game')
        print('press [2] to play sum of numbers game')
        print('press[3] to play multiplication table game')
        print('if you want exit the game press x')
        print('------------------------------------------')
        self.choice()
    def choice(self):
    ################################################################
    #build_function_that_let_user_chose_the-game
        while True:
            user_choice = input('enter your choice:')
            try:
                user_choice = int(user_choice)
                if user_choice == 1:
                    print('------------------------------------------')
                    self.even_odd_game()
                elif user_choice == 2:
                    print('------------------------------------------')
                    self.summ_game()
                elif user_choice == 3:
                    print('------------------------------------------')
                    self.multiply_game()
                elif user_choice == 'x':
                    break
                    exit()
                else:
                    print('choose value between 1, 2 and 3')
            except ValueError:
                print('please enter valid input')
    ##########################################################################
    #even_odd_guessing_code
    def even_odd_game(self):
        print('this game takes number and tell you if it is even or odd')
        print('follow this instructions to be able to play')
        print('if you want exit the game press x')
        print('-----------------------------------------------------------')
        while True:
            number = input('enter the number:')
            if number == 'x':
                print('closing the game')
                print('------------------------------------------')
                break
            if number == 'h':
                print('this game does not take any of decimal nor letters so please do not enter them')
            try:
                number = int(number)
                if number % 2 == 0:
                    print('accumulating.....')
                    print('this number is even')
                else:
                    print('accumulating.....')
                    print('this number is odd')
            except ValueError:
                print('enter valid input')
                print('for more instructions and inf enter h')
            print('------------------------------------------------------------------------')
    ########################################################################################################
    #addation_game_code
    def summ_game(self):
        print('welcome on this game')
        print('this game takes two or more numbers and print the sum of them')
        print('if you want exit press x')
        print('-----------------------------------------------------------------')
        while True:
            first_number = input('how many numbers do you want to count:')
            if first_number == 'x':
                print('closing the game')
                print('------------------------------------------------------')
                break
            try:
                first_number = int(first_number)
                count_number = 0
                total = 0
                while count_number < first_number:
                    insert_number = float(input('enter a number:'))
                    count_number += 1
                    total = total + insert_number
                print(total)
            except ValueError:
                print('please enter valid number')
            print('-----------------------------------------------------')
    ################################################################################################################
    #multiplication_table_code
    def multiply_game(self):
        print('this game print you multiplication table for any number')
        print('if you want to exit the game enter x')
        print('if you want some instructions enter h')
        print('------------------------------------------------------------------')
        while True:
            number = input('what is the number you want to find its multiplication table:')
            if number == 'x':
                print('closing game.....')
                print('------------------------------------------')
                break
            if number == 'h':
                print('do not enter any letters')
                number = input('what is the number you want to find its multiplication table:')
            end = input('how far you want it to go:')
            if end == 'x':
                print('closing game.....')
                break
            if end == 'h':
                print('do not enter any letters because this game takes only numbers')
                end = input('how far you want it to go:')
            try:
                number = float(number)
                end = int(end)
                for i in range(0, end + 1):
                    print(i, '*', number, '=', i * number)
            except ValueError:
                print('please enter a valid number')
                print('for further information enter h')
            print('-----------------------------------------------------------------------------')
#######################################################################################################################
#take_object_from_main_class_and_start-the_game
game1 = Game()
#########################################################################
#building_steps
#1_create_a_class_that_contain_all_the_games_as_functions_and_this_class_called_Game
#2_create_a_constructor_that_print_instructions_and_choices_directly_after_taking_an_object_from_the_main_class
#3_create_another_function_that_let_the_user_choose_the_program
#4_build_a_function_for_each_game
#5_take_an_object_from_the_class
