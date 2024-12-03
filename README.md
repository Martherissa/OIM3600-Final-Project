# OIM3600 Final Project: Tarot Card Reading
## Team Members
- Marissa Yang
- Doris Dai

## Project Overview
Our project is a tarot card reading program that allows users to draw a card from a deck of 78 cards that can be either
upward direction or downward direction like traditional tarot card reading and receive a reading based on the card they drew.
The program will provide the user with:
- the name of the card
- the card's image
- brief description of the card's image
- breif explanantion of the meaning of the card.
The user will also have the option to draw another card or change logout of their current username and log in as a different user.

All session data will be stored in the user_data folder under session.json file:
- past_questions: a list of dictionaries containing the user's information, past questions, and the cards they drew each time
- everything outside the past_questions list will be the current user's information and the current question and results they are drawing


## Usage Guidelines
1. Run the "app.py" file
2. "Ctr+Click" on the link that appears in the terminal
3. The user will be redirected to the home page
4. Input username, your question, and an integer number from 1 to 6 resembling the number of cards you want to pick
5. Click "Submit" are user will be redirected to the result page
6. Click on each of the card images to see the card's description and meaning
7. Reclick the card image to hide the card's description and meaning
8. Click "Draw Another Card" to draw another card
9. Click "Logout" to logout of the current user and log in as a different user

## Dependencies
1. [Flask Api Documentation](https://flask.palletsprojects.com/en/stable/api/)
2. [Tarot Api](https://tarotapi.dev/api/v1/cards)
3. Past Web Tech Projects and Course Materials
4. ChatGPT

## Project Structure

#### Python Files
- function.py:
    - contains all the predefined functions that are used in the app.py file
    - functions are built off of the tarot Api
    - Key functions:
        - random_card: Input a number and return specified number of random tarot cards from tarot Api
        - random_card_name: Input the result from random_card and return the list of card names
        - card_description: Input he result from random_card and the card names list and return the list of cards descriptions
        - card_meaning: Input the result from random_card and the card names list and return the list of the cards meanings
        - get_card_image: Input the result from random_card and the card names list and return the list of cards images urls
- app.py:
    - this is the main code for the app and it's built on the Flask framework
        - to run the app, run the app.py file
        - "Ctr+Click" on the link that appears in the terminal to access the page
    - contains definations of routes for the home page, result page, and logout page
        - home page: contains the form for the user to input their username, question, and number of cards they want to draw
        - result page: contains the result of the user's question and the cards they drew
        - another card page: redirect user back to homepage to draw another card with same username
        - logout page: allow user to change user name and draw another card
    - contrains specification for data storage:
        - The session data will be stored in the user_data folder
        - The session data will be stored in a file called session.json
        - The session is permanent, meaning that all past data will be stored even after the browser is closed
        - The session data will be signed (encrypted) for security
        - The session key prefix is session: (not necessary but added for clarity)
-cardimg.py:
    - contains a list item called tarotCards:
        - each element of the list is a dictionary containing the card's name, description, and image url

#### Folders
- templates folder:
    - index.html: contains the form for the user to input their username, question, and number of cards they want to draw
    - result.html: contains the result of the user's question and the cards they drew
- user_data folder:
    - session.json: contains all the session data for the webpage
    - the session data is permanent meaning that the data will be stored even after the user closes the app
        - past_questions: a list of dictionaries containing the user's information, past questions, and the cards they drew each time
        - everything outside the past_questions list will be the current user's information and the current question and results they are drawing

## Collaboration information

#### Collaboration Members
- Marissa Yang
- Doris Dai

#### Collaboration Plan
We discussioned the project idea and structure together and worked together online to build the code together
For any modifications or changes, we will text each other the places we made changes and the reasons why it is imperative
If there are any issues, we will text each other and do our best to explain the issue and the solution we came up with 
and choose the best course of action

## Aknowledgements
- Flask Api
- Tarot Api
- Web Tech Course Materials from Professor Shankar
- ChatGPT

## Reflection
Having learned from past projects from problem solving class, we started out with a clear structure for the webpage
with the desired functionalities we wish to include and decided that we wanted to do a simply webpage that would allow users 
to draw tarot cards and provide with simply readings. Marissa initially wished to do more indepth analysis of the readings using 
text mineing and adding more advanced features but due to the limited time we had, we decided to keep the project simple yet challenging.

Building functions off of the tarot Api was a challenge as we had to figure out how to extract the information we needed from the Api
especially as the Api did not specify the direction of the cards and we had to build another list to randomly assign directions to the cards.
Then, since the tarot Api did not provide images, we had to manually input the image urls for each card which was time consuming. Since we changed
the names for each card, we need to split the names to extract information from the api.

Building the app.py, the main problem we had was regarding the route as we need to understand what data we need to obtain and plug
into the page or store in session for easier reference to the next page. Data storage is another stressful part as we need to figure out
how to keep past data seperated from current data and how to prevent data from being overwritten. We realized that when user log into a webpage,
the webpage usually remember the username. We wanted to replicate the feature while giving the user the option to logout and 
change to another username. Since the time is limited, we were not able to implement more advanced features like passward login and creating 
different databases for different users. However, to explore the topic further, we decided to proceed the project even after the semester ends to 
enhacen our understanding of full stack development.

While ChatGPT helped us alot with exploring new apis and understanding the logistics of Flask api, sometimes it failed to understand the problem, and 
would provide codes with bugs that will taper latter code implementation. A simply example is how ChatGPT generated HTML code always has the styles
inside html rather than in the style section which created major difficulty if not cautioned for when styling the code or adding javascript functions to
change the style when clicked or so on.

Overall, the project was a great learning experience as we not only explored python but also CSS, HTML, Javascript, and even data storage and security
It enabled us to replicated some baisc freatures of a formal webpage and we wished to spend more time advancing it in the future.
