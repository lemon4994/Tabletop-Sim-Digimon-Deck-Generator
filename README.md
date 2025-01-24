# Deck Generator Tool for Digimon TCG Tabletop Simulator games

## Instructions

Go to digimoncard.dev<br>
Create your deck in the deck editor, then export to TTS.<br>
![The export menu of digimoncard.dev](carddev.png)<br>
Any other deckbuilder that exports in the same format is also a valid alternative.

Copy and paste the export text as written into the program when prompted to.<br>
Optional: You can use alt arts by manually adding "_P1", "_P2", etc after the appropriate card IDs.

Then copy and paste the outputted file directly into your TTS saved objects folder (On Windows this is located at Documents/My Games/Tabletop Simulator/Saves/Saved Objects).<br>
Load it into a lobby as you would any other item.<br>
![The saved object as seen in the ingame menu](object.png)

Optional: You can use any image you want as the in game thumbnail for your deck, by placing a .png into the Saved Objects folder with the same name as your .json file

## TODO

- Unreleased cards<br>
    The images are taken from the official Digimon TCG website and thus can only use cards currently hosted on the site.<br>
- Parallel Arts<br>
    Due to how digimoncard.dev exports cards, another method is needed to automatically identify parallel arts for cards