README - Chess Application

This project is a board game tournament management software. It allows you to organize and monitor a tournament between
different players. The software lets you mix players, create matches and track game results.

Features
Create a new tournament with a name, location, start date, end date, and description.
Add participating players to the tournament by selecting them from an existing list.
Randomly shuffle players for the first round of the tournament.
Generate matches between players based on their scores (or randomly in case of score ties).
Record match results for each player.
Manage different rounds of the tournament with an automatic update of player rankings.
Save tournament information in a JSON file for later resumption.

Installation
Clone this repository to your local machine using the command:

git clone https://github.com/n4xe/P4_OC_Chess_Tournament_Application/tree/master/
Make sure you have Python 3.10.7 installed on your machine.

Install the required dependencies using the command:
pip install -r requirements.txt

Usage
Run the main file main.py to launch the application.

Follow the on-screen instructions to create a new tournament, add players, start rounds, and record match results.

Tournament information is automatically saved in the tournament_information/tournament_database.json file.

To start a flake 8 repport, please install flake 8 and flake8-html and paste in the terminal : 
"flake8 --max-line-length=119 my_app --format=html --htmldir=flake8_rapport"

Authors
Valentin Simioni
