## Table of Contents
* [**Testing During Development**](#testing-during-development)
    * [*Manual Testing*](#manual-testing)
        * [*VS Code flake8](#vs-code-flake8)
    * [*Bugs and Fixes*](#bugs-and-fixes)
* [**Post Development Testing**](#post-development-testing)
  * [**Validators**](#validators)
      * [*CI Python Linter*](#ci-python-linter)

## **Testing During Development**
While developing, I've manually tested using the following methods:
1. During development, I repeatedly created test prints to check the values of the methods.
2. I have thoroughly tested all inputs and their validation.
3. I have played through the game several times to make sure that all the functions work as intended.
4. I asked family, friends and colleagues to test the game extensively. So far, nobody has managed to break the game.

***
### **Manual Testing**
***

#### **VS Code flake8**
During development in VS Code, I repeatedly analyzed the code with Flake8 to check for errors and ensure quality and conformity with the PEP8 style guide. The most common sources of errors during the project's implementation are listed below:

1.  * ***Issue:*** 
        * E501 line too long: Lines exceeding the recommended maximum length of 79 characters.
    * ***Solution:*** 
        * I broke the long lines into shorter ones using parentheses and reformatting.

2.  * ***Issue:*** 
        * W291 trailing whitespace: Whitespace characters at the end of a line.
    * ***Solution:*** 
        * Any extra spaces at the end of lines have been removed.

3.  * ***Issue:*** 
        * E303 too many blank lines: To many blank lines between lines of code
    * ***Solution:*** 
        * Whenever there was more than one empty line between two lines of code, these were removed.

4.  * ***Issue:*** 
        * E304 expected 2 blank lines, found 1: Must be two empty lines between each top-level methods or class.
    * ***Solution:*** 
        * I have ensured that there are always two free lines between each top-level method class.

5.  * ***Issue:*** 
        * E222 multiple spaces after operator: Too many whitespaces after operator.
    * ***Solution:*** 
        * Removed the double whitespace after the operator.

6.  * ***Issue:*** 
        * E221 multiple spaces before operator: Too many whitespaces before operator.
    * ***Solution:*** 
        * Similar to 5. Removed the double whitespace before the operator.

7.  * ***Issue:*** 
        * E201 whitespace after '(': Another unnecessary whitespace.
    * ***Solution:*** 
        * Removed the whitespace after '('.

8.  * ***Issue:*** 
        * F541 f-string is missing placeholders: Unnecessary f-string usage.
    * ***Solution:*** 
        * This occurred after the line break to avoid the E501. The f-string was no longer necessary after the break.

9.  * ***Issue:*** 
        * W292 no newline at end of file: Missing new empty line after last code line.
    * ***Solution:*** 
        * An empty line is added after the last line of code.

10. * ***Issue:*** 
        * W391 blank line at end of file: A blank line after the last empty line.
    * ***Solution:*** 
        * The opposite of 9. Unnecessary lines removed.

***
### **Bugs and Fixes**
***

1. * ***Issue:*** 
        * During development, an infinite loop occurred when the player ships were set manually. The game could then no longer be played.
    * ***Solution:*** 
        * The problem could be solved by adding the correct loop to the '_manually_place_ship' method.

2. * ***Issue:*** 
        * Towards the end of the development, it was noticeable that the row of numbers from 1 to 10 in the radar view was slightly shifted.
    * ***Solution:*** 
        * The problem was that I had tried to solve the alignment with ljust, which turned out to be inaccurate and cumbersome. After changing the method to display boards side by side, the problem was solved.

#### **Remaining Bugs**  
* There are no bugs remaining in the app.

***
## **Post Development Testing**

### **Validators**

#### **CI Python Linter**
I have checked all my modules with CI Python Linter and no problems have occurred due to the permanent checks with flake8 during development.

* run.py
[CP Python Linter - run.py Screenshot](docs/screenshots/cipl_run_py.png)

* ship.py
[CP Python Linter - ship.py Screenshot](docs/screenshots/cipl_ship_py.png)

* board.py
[CP Python Linter - board.py Screenshot](docs/screenshots/cipl_board_py.png)

* game.py
[CP Python Linter - game.py Screenshot](docs/screenshots/cipl_game_py.png)

***
[return to README.md](README.md)