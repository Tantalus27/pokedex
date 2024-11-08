PokeAPI Pokedex

A command-line Pokédex built with Python that uses the PokeAPI to retrieve and display information about Pokémon. This program provides basic details about Pokémon, including their types, weight, height, locations, cry, and sprite.

Features

Fetch and Display Pokémon Information: Shows basic data such as type(s), weight, height, and games the Pokémon has appeared in.
Location Data: Retrieves where to find the Pokémon in the game world.
Pokémon Cry: Plays the Pokémon's latest or legacy cry sound.
Sprite Display: Shows the Pokémon's sprite image in a separate window.

Requirements
Python 3.x

Required Python Libraries:
requests
pygame (for playing the Pokémon cry and displaying sprites)
textwrap (for game name formatting)

Installation
Clone the repository:

git clone https://github.com/tantalus88/pokedex.git

cd PokeAPI_Pokedex
Install the required packages:

pip install -r requirements.txt

Usage
Run the program:
python main.py

Follow the prompts to enter a Pokémon's name. If the Pokémon name is misspelled, you will be prompted to re-enter it.

After the Pokémon details are displayed, you will be asked if you’d like to search for another Pokémon.

Code Structure
main.py: Contains all functions to retrieve, display, and handle data related to Pokémon: 

get_pokemon_name(): Takes Pokémon name input.

get_pokemon_info(name): Fetches Pokémon information from the PokeAPI.

show_pokemon_info(pokemon_info): Displays Pokémon's basic details.

get_location(pokemon_info): Retrieves location areas where the Pokémon can be found.

pokemon_cry(pokemon_info): Plays the Pokémon's cry.

pokemon_sprite(pokemon_info): Displays the Pokémon's sprite in a pygame window.

repeat_lookup(): Prompts user to look up another Pokémon or exit.

Notes

To avoid errors if a Pokémon name is entered incorrectly, the program will prompt you to re-enter the name. Upon a successful API response, the program will then retrieve and display all relevant data.

Troubleshooting

AttributeError: If the Pokémon name is entered incorrectly, ensure it’s spelled correctly upon retry.

Pygame Window Freezes: Press the close button on the Pygame window if it remains open after viewing a Pokémon sprite.
