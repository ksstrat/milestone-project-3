## Table of Contents
* [**Testing During Development**](#testing-during-development)
    * [*Manual Testing*](#manual-testing)
    * [*Bugs and Fixes*](#bugs-and-fixes)
* [**Post Development Testing**](#post-development-testing)
  * [**Validators**](#validators)
      * [*Python Validation*](#)

## **Testing During Development**
While developing, I've manually tested using the following methods:

### **Manual Testing**

#### VS Code flake8
During development in VS Code, I repeatedly analysed the code with Flake8 to check for errors and ensure quality and conformity with the PEP8 style guide. The most common sources of errors during the project's implementation are listed below:

1.  * ***Issue:*** 
        * E501 line too long: Lines exceeding the recommended maximum length of 79 characters.
    * ***Solution:*** 
        * I broke the long lines into shorter ones using parentheses and reformatting.

2.  * ***Issue:*** 
        * W291 trailing whitespace: Whitespace characters at the end of a line.
    * ***Solution:*** 
        * Any extra spaces at the end of lines have been removed.

3.  * ***Issue:*** 
        * E303 too many blak lines: To many blank lines between lines of code
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
        * E201 whitespace after '(': Another unnecessary whitepsace.
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
        * W391 blankl line at end of file: A blank line after the last empty line.
    * ***Solution:*** 
        * The opposite of 9. Unnecessary lines removed.

CI Python Linter