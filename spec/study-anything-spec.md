# Study Anything Spec v1.0
### Created: 17/07/2025
### Last Updated: 20/07/2025
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
- Route: `/`
- Template: `index.html`
- Description:  
    - The page contents are centered.  
    - Elements from top to bottom:
        - Main Menu
        - Large title: "Study Anything". Text color blue (`#017a9d` or similar)
        - App description: a few paragraphs of text describing the app. Black text.
        - Statistic section:
            - Small title - "Statistics"
            - Total number of decks ('Decks: #')
            - Total number of cards ('Cards: #')
            - Total number of reviews ('Reviews: #')

### Study - Choose Deck Page
- Route `/study`
- Template: `choose-deck.html`
- Description:
    - The page contents are centered.  
    - Elements from top to bottom:
        - Main Menu
        - Large title: "Study".
        - Smaller subtitle: "Choose Deck"
        - Text: "Please choose a deck to study"
        - Deck selection form:
            - A dropdown with the options being all the deck names
            - a button to the right of the dropdown with the text 'Study'

### Study - Study Deck Page
- Route: `/study?deck-id=#`
- Template: `study.html`
- Description:
    - The page contents are centered.  
    - Elements from top to bottom:
        - Main Menu
        - Large title: "Study"
        - Smaller subtitle: "Deck {deck.name}"
            - where deck.name is the name of the deck whose id=deck-id
        - Review Pane:
           - There are two possible states ("Review Pane State"):
                - First state - "Test":
                - Second state - "Feedback"
            - Large square box for the front and back of the current card
                - Front of the card occupies the top half, back occupies bottom half.
                - Back is is not visible (hidden) when the state is "Feedback"
            - Three button:
                - Left button is either "Show Answer" (when in "Test" state) or "Hide Answer" (when in "Feedback" state)
                - Middle button is "Previous"
                - Right button is "Next"
         
### Add Decks Page
- Route: `/add-decks`
- Template: `add-decks.html`
- Description:
    - The page contents are centered.  
    - Elements from top to bottom:
        - Main Menu

### Add Cards Page
- Route: `/add-cards`
- Template: `add-cards.html`
- Description:
    - The page contents are centered.  
    - Elements from top to bottom:
        - Main Menu

### Browse Page
- Route: `/browse`
- Template: `browse.html`
- Description:
    - The page contents are centered.  
    - Elements from top to bottom:
        - Main Menu


---

## API

see `spec/study-anything.openapi.yaml`.






