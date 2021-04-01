# TDD Intro: Command-line To Do Application #

## Purpose ##

The purpose of this project is to create a To Do application that runs at the command prompt.

Core behaviors include:

1. Accepting user input
2. Creating new to-do items
3. Displaying all active to-do items
4. Marking to-do items as complete
5. Displaying all completed to-do items
6. Deleting active to-do items
7. Deleting all completed to-do items

## Prerequisites ##

1. Python V3 (3.8 or above preferred)
    - Download installer here: https://www.python.org/downloads/
2. Pipenv
    - install with `pip3 install pipenv`

## Project Setup ##

**1. Fork this project**

Click on the fork button in the upper right hand corner of the page. Github will do the rest.

**2. Clone the project to your local computer:**

Option A: From the command line

1. Open a command prompt and navigate to the folder where you typically store projects
    - Note: I typically keep my projects in `~/Documents/projects` (`~` is your user home directory)
2. Clone the project repository
    - command: `git clone <project_url>`
    - replace `<project_url>` with the URL from Github for your project

Option B: From the Github Desktop client

1. Choose the repository from the list of remote repositories
2. Press clone, and select a location on your computer to store the files

**3. Set up the project**

This is how you will actually set up the project to run on your local computer.

1. Open a command prompt at the root directory of this project.
    - You'll know you have it right if you are in the same directory as the file called `Pipfile`
2. Install all required packages and dependencies:
    - In the command window, run the command `pipenv install --dev`
    - The install process could take a little bit. You'll probably see a fair amount of program output.

That's it!

**4. Running the tests**

To run all the tests, run the following command:

`pipenv run test`

**5. Committing code**

Make sure, when you have a passing test, COMMIT YOUR CODE! The more often you commit, the less work you'll lose if you make a mistake. Also, we all make mistakes.

To commit your code run the following command from the command prompt:

`git commit -am "In 50 characters, describe what you did"`

OR

Commit from Github Desktop.

**6. Pushing code**

To push your code, run the following command from the command prompt:

`git push` or `git push origin master`

OR

Push from Github Desktop