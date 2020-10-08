import random

# Establish movie variety sets

action = {'Jaws', 'Fast and Furious', 'Marvel Cinematic Universe', 'Mission Impossible', 'Jumanji', 
         'Expendables', 'James Bond', 'Star Wars', 'John Wick', 'X-men', 'Oblivion'
         }
romance = {'Crazy, Stupid Love', 'Definitely, Maybe', 'Love Actually', '500 Days of Summer', 'The Longest Ride', 
         'Her', 'Blue Valentine', 'Call Me by Your Name', 'The Proposal', 'When Harry Met Sally', 'No Strings Attached'
         }
artistic = {'Phantom Thread', 'Once Upon a Time in Hollywood', 'Inherent Vice', 'No Country for Old Men', 'Fargo', 
         'Good Fellas', 'Schindler\'s List', 'The Revenant', 'American Beauty', 'Black Swan', 'Ford v Ferrari'
         }

def movie_displayer():
    print("Select 3 movies from each selection.\nYou will need to enter the number for each one of your choices 1 at a time then hit enter.\nIf you choose the wrong selection, you can redo your selection.")

    rom_movies = list(random.sample(romance,6))
    act_movies = list(random.sample(action,6))
    art_movies = list(random.sample(artistic,6))

    card_1 = rom_movies[:3] + act_movies[:3] + art_movies[:3]
    card_2 = rom_movies[3:] + act_movies[3:] + art_movies[3:]

    print("\nCard 1:\n")

    for i in card_1:
        print(card_1.index(i),i,'\n')

    user_selections = list() ## Error, not saving user input accurately
    for i in range(0,3,1):
        user_selections.append(input())

    return 0

movie_displayer()