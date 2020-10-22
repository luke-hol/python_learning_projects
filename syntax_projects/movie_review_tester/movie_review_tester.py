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

def make_card():
    movie_list = list(random.sample(romance, 3))
    movie_list.extend(random.sample(action, 3))
    movie_list.extend(random.sample(artistic, 3))

    card = list(movie_list)

    return card


def show_card(card):
    print("\nCard 1:\n")

    for i in card:
        print(card.index(i), i, '\n')


def display_movies():
    print(
        "Select 3 movies from each selection.\n"
        "You will need to enter the number for each one of your choices 1 at a time then hit enter.\n"
        "If you choose the wrong selection, you can redo your selection."
    )

    card_1 = make_card()
    show_card(card_1)
    return card_1

# Get user selections


def get_user_preference(card):
    user_selections = list()
    for i in range(0, 3, 1):
        user_selections.append(card[int(input())])

    return user_selections

# Compare selections with movie list to determine set.


def determine_taste(set_movies):

    taste_profile = {
        'romance': False,
        'action': False,
        'artistic': False
    }

    def choose_genres(set_movies, taste_profile):

        if set_movies.isdisjoint(action) is False:
            taste_profile['action'] = True
        if set_movies.isdisjoint(romance) is False:
            taste_profile['romance'] = True
        if set_movies.isdisjoint(artistic) is False:
            taste_profile['artistic'] = True

    choose_genres(set_movies, taste_profile)

    print("You are a fan of:")

    for genre, v in taste_profile.items():
        if v:
            print(genre)
    return taste_profile


def recommend_movies(taste_profile):
    genres = []
    card = set()
    for k, v in taste_profile.items():
        if v:
            genres.append(k)

    for i in genres:
        if i == 'romance':
            card.update(romance.difference(selected_movies))
        if i == 'action':
            card.update(action.difference(selected_movies))
        if i == 'artistic':
            card.update(artistic.difference(selected_movies))

    return card


selected_movies = get_user_preference(display_movies())
taste_profile = determine_taste(set(selected_movies))
recommendation_card = recommend_movies(taste_profile)
show_card(list(recommendation_card))
