# Study Anything Spec v1.0
### Created: 17/07/2025
### Last Updated: 17/07/2025
### Author: Michael Shults

## Description
Study Anything is a simple Flask web app that allows users to review study material using flashcards.


## Features - using UI
- View decks
- View all cards in a deck
- Add deck
- Delete deck
- Create a new flashcard and add it to an existing deck
- Delete a flashcard
- Review all the cards in a deck

## Features - using API
- Get all decks (without the cards)
- Get all the cards in the database
- Get all the cards of a deck
- Add deck
- Delete deck
- Create a new flashcard and add it to an existing deck
- Delete a flashcard

## UI

### Main Menu
A horizontal menu, includes rectangular buttons with black text.
Menu items are (left to right): 'Home', Study', 'Add Decks', 'Add Cards', 'Browse'
<br>
<br>

### Home Page
The page contents are centered.  
From top  to bottom:
- Main Menu
- Large title: 'Study Anything'. Text color blue (`#017a9d` or similar)
- App description: a few paragraphs of text describing the app. Black text.
- Statistic section:
    - Small title - 'Statistics'
    - Total number of decks ('Decks: #')
    - Total number of cards ('Cards: #')
    - Total number of reviews ('Reviews: #')

### Study Page

### Add Decks Page
### Add Cards Page
### Browse Page


---

## API

see `spec/study-anything.openapi.yaml`.






