import random

# build collection of test movies

action = {'Jaws', 'Fast and Furious', 'Marvel Cinematic Universe', 'Mission Impossible', 'Jumanji',
          'Expendables', 'James Bond', 'Star Wars', 'John Wick', 'X-men', 'Oblivion'
          }
romance = {'Crazy, Stupid Love', 'Definitely, Maybe', 'Love Actually', '500 Days of Summer', 'The Longest Ride',
           'Her', 'Blue Valentine', 'Call Me by Your Name', 'The Proposal', 'When Harry Met Sally',
           'No Strings Attached'
           }
artistic = {'Phantom Thread', 'Once Upon a Time in Hollywood', 'Inherent Vice', 'No Country for Old Men', 'Fargo',
            'Good Fellas', 'Schindler\'s List', 'The Revenant', 'American Beauty', 'Black Swan', 'Ford v Ferrari'
            }


# Display selection of movies, and get feedback


def display_movies():
    print(
        "Select 3 movies from each selection.\n"
        "You will need to enter the number for each one of your choices 1 at a time then hit enter.\n"
        "If you choose the wrong selection, you can redo your selection.")

    # Get list of movies
    def make_card():
        movie_list = list(random.sample(romance, 3))
        movie_list.extend(random.sample(action, 3))
        movie_list.extend(random.sample(artistic, 3))

        card = list(movie_list)

        return card

    # build card
    def show_card(card):
        print("\nCard 1:\n")

        for i in card:
            print(card.index(i), i, '\n')

    card_1 = make_card()
    show_card(card_1)
    # Get user selections

    def get_user_preference():
        user_selections = list()
        for i in range(0, 3, 1):
            user_selections.append(card_1[int(input())])

        return user_selections

    return get_user_preference()

# Compare selections with movie list to determine set.


def determine_taste(set_movies):

    taste_profile = {
        'romance_fan': False,
        'action_fan': False,
        'art_fan': False
    }

    def choose_genres(set_movies, taste_profile):

        if set_movies.isdisjoint(action) is False:
            taste_profile['action_fan'] = True
        if set_movies.isdisjoint(romance) is False:
            taste_profile['romance_fan'] = True
        if set_movies.isdisjoint(artistic) is False:
            taste_profile['art_fan'] = True

    choose_genres(set_movies, taste_profile)

    user_taste_profile = list()

    print("You are a fan of:")

    for genre, v in taste_profile.items():
        if v:
            print(genre)

selected_movies = display_movies()
determine_taste(set(selected_movies))
