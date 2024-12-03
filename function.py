import requests
import pprint
import json
import pprint
import urllib.request
import random
from cardimg import taroCards

# API URL
api_url = "https://tarotapi.dev/api/v1/cards"

# Upright or reversed
# Predefined list of upright and reversed positions for the cards
# Since the API does not provide this information, we will randomly assign it
up_down = [" Upright", " Reversed"]


def random_card(number):
    """
    Get specified number of random tarot cards randomly

    Input: number of random cards to get
    result is the whole list from the api
    """
    response = requests.get(api_url + "/random" + f"?n={number}")
    result = response.json()
    return result


def random_card_name(result):
    """
    Input the result from random_card function with specified number of cards
    Get the name of the list of tarot cards

    Input: whole list from the api
    result is a list of card names
    """

    # each element of the list is a card name:
    # "name" + "Upright" or "Reversed" for all the results in the list
    return [(card["name"] + random.choice(up_down)) for card in result["cards"]]


# # pprint.pprint(random_card(3))
# result = random_card(3)
# pprint.pprint(random_card_name(result))


def card_description(result, cards):
    """
    Get the description of a set of cards

    Input: whole list from the api, the list of card names
    result is a list of description
    """
    newname = {}
    descriptions = []

    # Make a dictionary of the card names:
    # key is the card name, value is the position (upright or reversed)
    for names in cards:
        newname[" ".join(names.split(" ")[:-1])] = names.split(" ")[-1]

    # Get the description of the cards based on the keys in the dictionary
    # append the description to the list
    for elements in newname:
        for card in result["cards"]:
            if elements == card["name"]:
                descriptions.append(card["desc"])

    return descriptions


def card_meaning(result, cards):
    """
    Get the meaning of a set of cards

    Input: whole list from the api, list of card names
    result is a list of meanings
    """
    newname = {}
    meanings = []

    # Same operation as before:
    # Make a dictionary of the card names:
    # key is the card name, value is the position (upright or reversed)
    for names in cards:
        newname[" ".join(names.split(" ")[:-1])] = names.split(" ")[-1]

    # Get the meaning of the cards based on the keys in the dictionary
    # Then evaluate if the card is upright or reversed
    # append the meaning to the list based on the card name and the position
    for elements in newname:
        for card in result["cards"]:
            if elements == card["name"]:
                if newname[elements] == "Upright":
                    meanings.append(card["meaning_up"])
                else:
                    meanings.append(card["meaning_rev"])
    return meanings


def get_card_image(cards):
    """
    Get the image url of a set of cards

    Input: list of card names
    result is a list of images urls of the cards
    """

    newname = {}
    images = []

    # Same operation as before:
    # Make a dictionary of the card names:
    # key is the card name, value is the position (upright or reversed)
    for names in cards:
        newname[" ".join(names.split(" ")[:-1])] = names.split(" ")[-1]

    # Get the image of the cards based on the keys in the dictionary
    # append the image to the list
    # Note that the image file is actually created and modified by ourselves
    # each image file is an url
    for i in range(len(taroCards)):
        for elements in newname:
            if elements == taroCards[i]["name"]:
                images.append(str(taroCards[i]["image"]))

    return images


def main():
    # This is the test set
    result = random_card(3)
    cards = random_card_name(result)
    pprint.pprint(result)
    print(cards)
    pprint.pprint(card_meaning(result, cards))
    pprint.pprint(card_description(result, cards))
    pprint.pprint(get_card_image(cards))


if __name__ == "__main__":
    main()
