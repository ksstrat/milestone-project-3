# Battleship
## Overview
Welcome to Battleship!
This is a adaptation of the naval strategy game, playable directly in the terminal. Engage in a tactical battle against a computer opponent, strategically deploying your fleet and hunting down enemy vessels. The game features a clean, text-based interface with colored output for an enhanced user experience.

![Start Screen Screenshot](docs/screenshots/start-screen.png)

Link to Heroku: [Battleship](https://msp3-battleship-a0f0482c2f33.herokuapp.com/)


## Table of contents:
1. [**Overview**](#overview)
2. [**Planning stage**](#planning-stage)
    * [***Target Audiences***](#target-audiences)
    * [***User Stories***](#user-stories)
    * [***How This will Be Accomplised***](#how-this-will-be-accomplished)
3. [**Features**](#features)
    * [***Welcome Screen***](#welcome-screen)
    * [***Rules***](#rules)
    * [***Gameplay***](#gameplay)
    * [***Game Over***](#game-over)
4. [**Future Improvements**](#future-improvements)
5. [**Testing Phase**](#testing-phase)
6. [**Libraries**](#libraries)
7. [**Deployment**](#deployment)
8. [**Credtis**](#credits)

***
## **Planning stage**

### **Target Audiences**
* Players who enjoy classic strategy board games.
* Users looking for a simple, text-based game to play in a terminal environment.
* Individuals interested in a demonstration of object-oriented programming principles in Python applied to game development.
* Casual gamers seeking a quick and engaging single-player experience.

### **User Stories**
* As a user, i want to start a new game of Battleship against the computer.
* As a user, i want to be able to view the game rules before play.
* As a user, i want to enter my name for a personalized experience.
* As a user, i want to choose to place my ships manually or have them placed randomly.
* As a user, i want to receive clear feedback on what is happening at every stage of the game.
* As a user, i just want to have a good time with Battleships!

### **How This Will Be Accomplished**
* This game is implemented entirely in Python, utilizing an object-oriented programming (OOP) paradigm
* All interactions and game display occur within the command-line terminal.
* Once the players have entered their names, they can choose whether to start the game immediately or read the rules first.
* Players can either place their ships on the board themselves or choose to have them distributed randomly.
* Players receive clear visual feedback at every stage of the game.
* If the player makes an input that is not intended, he receives clear feedback and can repeat the input.

***
## **Features**

### **Welcome Screen**
* Users are greeted with the start screen.
* From here, you can:
    * Start the game
    * Read the rules
    * Exit the game

![Start Screen Screenshot](docs/screenshots/start-screen.png)

### **Rules**
* Here, the player is given an overview of the rules.
* After reading, he can return to the home screen by pressing any button.

![Rules Screen Screenshot](docs/screenshots/rules.png)

### **Gameplay**
* When the game starts, the player is first asked for their name.

![Enter Name Screenshot](docs/screenshots/enter-name.png)

* The player is then given the option of either placing the ships manually or leaving the placement to chance.

![Ship Placement Question](docs/screenshots/ship-placement-question.png)

* If the player chooses manual placement, they can place the ships on the playing field one by one, as they wish.

![Ship Placement](docs/screenshots/placing-ships.png)

* Once the orientation has been selected (horizontal or vertical), the ship is placed according to the player's choice.

![Ship Placement Orientation](docs/screenshots/placing-ships-orientation.png)

* If a player makes an invalid entry — for example, by trying to leave the grid or put a second boat on the same field — they will see a relevant error message.

![Ship Placement Invalid](docs/screenshots/placing-ships-invalid.png)

### **Game Over**

***
## **Future Improvements**

***
## **Testing Phase**
I have documented the testing processes, both during and after development, in a separate file named [TESTING.md](TESTING.md).

***
## **Libraries**

***
## **Deployment**

***
## **Credits**
