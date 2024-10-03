import random
from databaseconnection import connection
import functions_game
from functions_game import insert_data_disease_table

list_first_countries = ["Finland", "Cambodia", "Canada", "Peru", "Croatia", "South Africa", "Dubai"]
first_country = random.choice(list_first_countries)


game_rules = ("On Vaccine Voyage you are a researcher trying to find ingredients for a vaccine "
              "before the whole world is infected. You will do that by travelling around the world "
              "to find those ingredients. First name the disease you want to treat, then use the "
              "trivia tips to rightly guess the country where the ingredients are. You will start "
              "with 300 points, every mistake and new hint you ask will be debited from points. "
              "Good luck! We'll start now! Let's save the world together!\n")

print(game_rules)

print(f"The first infected country is {first_country}.\n")

disease_name = input("What disease are you going to treat? \n")

print(f"Now we start our journey to fight {disease_name}...\n")

names = disease_name
points = 300
guess_count = 1
greetings = "Congratulations! You found this ingredient! Let's move on!"


#randomize 7 countries, and assign 7 variables accordingly
from functions_game import ingredient_country
final_country_list = ingredient_country()


#for loop that will loop for 7 times, representing 7 levels

from functions_game import retrieve_hints

from functions_game import point_per_level

game_movement = ""
countries_guessed = []
game_over = "No"

for game_level in range(0,8):
        #generate randomly 6 hints for the country for the current level
        #enter into the function: the country after being randomly picked and game level
        #example: in the 1st level final_country_list[0] - which is the 1st country, and enter into the current level parameter as 1 (0+1),
        #print(game_level)
        #print(final_country_list[game_level])
    hint_list = retrieve_hints(final_country_list[game_level],game_level+1)
    print(game_level +1)
    for hint_number in range(0,7):
        print(hint_list[hint_number])
        print('Your current points:', points)
        game_movement = input("What do you want to do: guess, new hint or quit?\n").upper()
        while game_movement not in ["QUIT", "GUESS", "NEW HINT"]:
            game_movement = input("What do you want to do: guess, new hint or quit?\n").upper()

        #if commands to decide if they want to guess, new hint or quit; they said guess, then provide with a hint
        if game_movement == "GUESS":
            guess = input(f"This ingredient is in: \n")
            if guess == final_country_list[game_level]:
                print(f"Superb! You found the ingredient number {hint_number}, let's move on\n")
                countries_guessed.append(final_country_list[game_level])
                if guess_count == 1:
                    points += int(point_per_level(game_level +1))
                    break
                else:
                    guess_count = 1
            elif guess != final_country_list[game_level]:
                if points >= 0:
                    if hint_number in [0,1,2,3,4,5,6]:
                        points = points - int(point_per_level(game_level +1))
                        guess_count += 1
                        print('Your guess was wrong, please view the next hint and try again\n')
                        current_country = final_country_list[game_level] game_movement = input("What do you want to do: guess, new hint or quit?\n").upper()
                        while game_movement not in ["QUIT", "GUESS", "NEW HINT"]:
                            game_movement = input("What do you want to do: guess, new hint or quit?\n").upper()
                    if hint_number not in [0,1,2,3,4,5,6]:
                        while guess != final_country_list[game_level]:
                            print('You have used up all hints of this level, please pick your guess:')
                            from functions_game import multiple_choice
                            multiple_choice(final_country_list[game_level])
                            while game_movement not in ["QUIT", "GUESS", "NEW HINT"]:
                                game_movement = input("What do you want to do: guess, new hint or quit?\")
                   #run function
                    #input('what is the country you choose?')
                    #while guess != final_country_list[game_level]
                    ##input('what is the country you choose?') - 3 to 4 options
                else:
                    game_over = "Yes"
                    break
        elif game_movement == "NEW HINT":
            points = points - int(point_per_level(game_level +1))
        elif game_movement == "QUIT":
            game_over = "Yes"
            print('Sorry to see you go. Come back soon!')
            print('Your current records is', points, countries_guessed) #need to improve the code to show countries guess and insert record into the session table
            break





    if game_over == "Yes":
        break
if points > 0:
    print('Congratulation, you have found all ingredients')
else:
    print('You failed to find all ingredients within the points given\n')

#need to improve the finishing lines
decision = input('Do you want to retry or quit?').upper()
if decision == "RETRY":
    game_over = False
    points = 300
    guess_count = 1
elif decision == "QUIT":
    print("Thank you for playing! You're welcomed to try again")






    """

    for movement in hint_level:
        game_movement = input("What do you want to do: guess, new hint or quit?").upper
        if game_movement == "GUESS":
            guess = input("This ingredient is in: ")
            if guess == hints:
                if guess == :
                    points += 10
                hint_level += 1
                print(greetings)
                insert_data_disease_table(names, country)
                else guess != hint:
                    points = point_counter()
                    print("Not this time, try again...")
        elif game_movement == "NEW HINT":
            hints = retrieve_hints(country, level)
        else game_movement == "QUIT":
            break()
        game_movement = input("What do you want to do: guess, new hint or quit?").upper

    for hint in hints:
        if hint <= 6:
            hint = hints
            points = point_counter()
        elif hint > 6:
            hint = muliple_choice
            points = point_counter()

"""








