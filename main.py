import requests
import json
import time
import io
import pygame
import textwrap as tw
import os

#PokeAPI url
base_url = "https://pokeapi.co/api/v2/pokemon/" 

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
# Display the program name and author
def intro():
    print("""PokeAPI Pokedex
Created by Marcus Martinez""")

# get the pokemon name 
def get_pokemon_name():
    name = input("Enter a Pokemon name: ").lower()
    clear_screen()
    return name

# insert the pokemon name into the API and verify the pokemon data can be found     
def get_pokemon_info(name):
    while True:
        url = f"{base_url}{name}"
        response = requests.get(url)

        if response.status_code == 200:
            pokemon_data = response.json()
            return pokemon_data
        else:
            print(f"Failed to get data error {response.status_code}")
            print("Please check the Pokemon name and try again.")
            name = get_pokemon_name()

# print the pokemon information the screen 
def show_pokemon_info(pokemon_info):
    if pokemon_info:

        #retreive the game list
        game_indices = pokemon_info.get("game_indices", []) 

        # reteieve height data and convert to meters
        height_data = pokemon_info.get("height")
        height = height_data / 10

        # reteive the weight data and convert to kilo grams
        weight_data = pokemon_info.get("weight")
        weight = weight_data / 10

        # retreive pokemon type(s)
        pokemon_type_data = pokemon_info.get("types",[])
        pokemon_type = ' '.join([poke_type["type"]["name"].capitalize() for poke_type in pokemon_type_data])

        # format pokemon name and game names
        pokemon_name = pokemon_info['name'].capitalize()
        game_name = [game["version"]["name"].capitalize() for game in game_indices]
        wrapped_game_names = tw.fill(' • '.join(game_name), width=40)

        # Display pokemon information
        print("=== Pokémon Information ===\n")
        print(f"Name: {pokemon_name}")
        print(f"Type(s): {pokemon_type}")
        print(f"Height: {height:.1f} meters")
        print(f"Weight: {weight:.1f} kilograms")
        print("\nAppeared in Games:")
        print(wrapped_game_names)  
        print("==========================\n")

# retreive Pokemon location data
def get_location(pokemon_info):
    location_url = pokemon_info.get("location_area_encounters")
    if location_url:
        location_response = requests.get(location_url)
            # verify location data
        if location_response.status_code == 200:
            location_data = location_response.json()
                # If Pokemon has locaton information display locations
            if location_data:
                    # Format location data
                pokemon_location = [local["location_area"]["name"].replace("-"," ").capitalize() for local in location_data]
                print("this pokemon can be found at:")
                for location in pokemon_location:
                    print(location)
            else:
                print("Location data not found")
        else:
            print("Location data not found")

# Get Pokemon cry information
def pokemon_cry(pokemon_info):

    # Get cry url from list starting with latest cry
    cries = pokemon_info.get("cries", {})
    cry = cries.get("latest")
    response = requests.get(cry)

    if cry:
        # if latest cry exist play cry
        if response.status_code == 200:
            pygame.mixer.init()
            cry_data = io.BytesIO(response.content)
            pygame.mixer.music.load(cry_data, "ogg")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        # If latest cry does not exist play legacy cry 
        else:
            cry = cries.get("legacy")
            response = requests.get(cry)
            pygame.mixer.init()
            cry_data = io.BytesIO(response.content)
            pygame.mixer.music.load(cry_data, "ogg")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

# Get Pokemon sprite image
def pokemon_sprite(pokemon_info,):

    # Get Pokemon sprite image url
    sprite_info = pokemon_info.get("sprites", {})
    sprite = sprite_info.get("front_default")
    response = requests.get(sprite)

    if sprite:
        # Verify Pokemon sprite image exists then displays
        if response.status_code == 200:
            sprite_img_data = io.BytesIO(response.content)
            sprite_img = pygame.image.load(sprite_img_data)
            pygame.init()
            screen = pygame.display.set_mode(sprite_img.get_rect().size)
            screen.blit(sprite_img, (0,0))
            pygame.display.flip() 
            #pygame.quit()
        # Display error message if image is not available
        else:
            print("Pokemon sprite image not found.")

# Repeat Pokemon look up
def repeat_lookup():
    # get input selection from user 
    answer = input("\nWhould you like to search for another Pokemon? Y/N: ").lower()
    # Y selection loops the program
    if answer == "y":
        pygame.quit()
        clear_screen()
        main()
        return answer

    # N selection closes the program
    elif answer == "n":
        print("\nClosing Pokedex")
        time.sleep(.5)
        clear_screen()

    # repeat the repeat_lookup function if neither Y or N is selected
    else:
        print("please select Y for yes or N for no")
        time.sleep(1)
        clear_screen()
        repeat_lookup()
        

def main():
    p_name = get_pokemon_name()                    
    pokemon_info = get_pokemon_info(p_name)
    pokemon_info
    show_pokemon_info(pokemon_info)
    get_location(pokemon_info)
    pokemon_cry(pokemon_info)
    pokemon_sprite(pokemon_info)
    repeat_lookup()

clear_screen()
intro()    
main()