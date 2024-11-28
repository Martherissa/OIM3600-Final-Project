import requests
import pprint
import json
import pprint
import urllib.request
import random
from cardimg import taroCards


api_url = "https://tarotapi.dev/api/v1/cards"

up_down = [" Upright", " Reversed"]


def random_card(number):
    """
    Get a random tarot card
    """
    response = requests.get(api_url + "/random" + f"?n={number}")
    result = response.json()
    return result


def random_card_name(result):
    """
    Input a number
    Get the specified number of random tarot card
    """

    return [(card["name"] + random.choice(up_down)) for card in result["cards"]]


# # pprint.pprint(random_card(3))
# result = random_card(3)
# pprint.pprint(random_card_name(result))


def card_description(result, cards):
    """
    Get the description of a card
    """
    newname = {}
    descriptions = []
    for names in cards:
        newname[" ".join(names.split(" ")[:-1])] = names.split(" ")[-1]

    for elements in newname:
        for card in result["cards"]:
            if elements == card["name"]:
                descriptions.append(card["desc"])

    return descriptions


def card_meaning(result, cards):
    """
    Get the meaning of a card
    """
    newname = {}
    meanings = []
    for names in cards:
        newname[" ".join(names.split(" ")[:-1])] = names.split(" ")[-1]

    for elements in newname:
        for card in result["cards"]:
            if elements == card["name"]:
                if newname[elements] == "Upright":
                    meanings.append(card["meaning_up"])
                else:
                    meanings.append(card["meaning_rev"])
    return meanings


def get_card_image(cards):

    newname = {}
    images = []
    for names in cards:
        newname[" ".join(names.split(" ")[:-1])] = names.split(" ")[-1]

    for i in range(len(taroCards)):
        for elements in newname:
            if elements == taroCards[i]["name"]:
                images.append(str(taroCards[i]["image"]))

    return images


def main():
    result = random_card(3)
    cards = random_card_name(result)
    pprint.pprint(result)
    print(cards)
    pprint.pprint(card_meaning(result, cards))
    pprint.pprint(card_description(result, cards))
    pprint.pprint(get_card_image(cards))


if __name__ == "__main__":
    main()
