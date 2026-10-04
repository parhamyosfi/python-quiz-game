# Pygame quiz game
![Static Badge](https://img.shields.io/badge/python-3.12-blue)

a simple quiz game built with python

## Table Of Contens



- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)


## Features
- quiz system
  - Asks the player multipul question
  - Check the answers automaticly
  - Calculate the final scores
- Resulte storeg
  - Saves quiz result in `result.txt`
- Admin Mode
  - ask for the admin password
  - check if the password is correct
  - keeps the private informattion outside is correct
  - loads the password from `env`

## Project Structure
```
python_quiz_game/
│   .env
│   .env.example
│   .gitignore
│   1.png
│   2.png
│   3.png
│   Animation.gif
│   app.log
│   debug.log
│   demo.gif
│   error.log
│   main.py
│   question.py
│   README.md
│   requirments.txt
│   results.txt

```
### File Discreption
| file|discrption|
|---|---|
| `main.py` | main file used to run quiz game|
| `question.py` | stores questions and answers|
| `enve example` | shows the envoirment variables needed by prroject|
| `gitignore` | tells git whitch files and folders|
| `requirments` | package lists|
| `1.png` |stores start game picture|
| `2.png` |stores quiz game picture|
| `3.png` |stores final output|
| `demo.gif` |stores the project outpot|
## Requirements
Before running the project, make sure you have:
- `python 3`
- `python-dotenve`

## Installation
1. open terminal in the project
2. check that python is installed

```bashe
python --version
```
3. install the python packages:
```bash
pip install -r requirments.txt
```
## Enviorment Setup
1. create a `.env` file from `.env.example`
```bash
cp .env.example .env
```
2. open the new .env file
3. replace the example value with own password
``` text
quiz_admin_password=your_password_here
```
4. save the file.
> do not commit your `.env` file because it may contain privet information
## Uasge
1. open a terminal in the project folder
2. run the quiz game
``` bash
python main.py
```
3. choose `yes` or `no`
4. if you choose `yes`, enter the password from your `env` file
5. enter your name
6. answer the question
7. see your final score and message
8. your result is saved in `result.txt`
## Example Output
```text
do you want to move to admin move y/n: no

what's your name? parham
welcome

what language are we using? g++
wrong

what command start git? git init
correct

what command show git status? git log --oneline --all
wrong

your score is:  1 out of 3
keep practing parham .
```
## Screenshot
### start game
![start game1](.\1.png)
### quiz
![quiz](.\2.png)
### final score
![final score](.\3.png)
## demo
![quiz game demo](.\demo.gif)
## Roadmap
- [x] add multiple quiz question
- [x] calculate the final score
- [x] save results to a file
- [x] add admin mode
- [ ] add more quiz question
- [ ] add difficultly levels
- [ ] add a timer
## Contributing

## Licence 

## Author

create by [mohammad javad]()