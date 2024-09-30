import random
from databaseconnection import connnection




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
country = ingredients
ingredients = ingredient_country()
hints = retrieve_hints(current_country, current_level)
points = 300
hint_level = 1
greetings = "Congratulations! You found this ingredient! Let's move on!"


while points > 0 and hint_level < 7:
    for movement in hint_levels:
        game_movement = input("What do you want to do: guess, new hint or quit?").upper
        if game_movement == "GUESS":
            guess = input("This ingredient is in: ")
            if guess == hint:
                if guess == 1:
                    points += 10
                    hint_level += 1
                    print(greetings)
                else guess != hint:
                    points = point_counter()
                    print("Not this time, try again...")
        elif game_movement == "NEW HINT":
            hints = retrieve_hints(country, level)
        else game_movement == "QUIT":
            break()

    for hint in hints:
        if hint <= 6:
            hint = hints
            points = point_counter()
        elif hint > 6:
            hint = muliple_choice
            points = point_counter()
    game_movement = input("What do you want to do: guess, new hint or quit?").upper









