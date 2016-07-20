#Globals

import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

#Define the functions


def find_preference():
    preferences = {} 
    for taste, question in questions.items():
        print(question)
        preferences[taste] = input() in ["y", "yes"]
    return preferences    
    

def make_drink():
    drink = []
    for key, value in preferences.items():
        if value is True:
            drink.append(random.choice(ingredients[key]))
    return drink

def main()
    preference = find_preference()
    drink = make_drink()


#if __name__ == "__main__":
#   main()