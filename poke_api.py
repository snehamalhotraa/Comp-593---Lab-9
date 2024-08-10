'''Authors: Mahenur Master, Nisharg Patel, Sneha Malhotra, Siddharth Patel'''
import requests

# Base URL for accessing Pokémon data
POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test the get_pokemon_info() function
    # Use breakpoints to inspect the returned dictionary
    poke_info = get_pokemon_info("Bulbasaur")
    return

def get_pokemon_info(pokemon):
    """Fetches information about a specified Pokémon from the PokeAPI.

    Args:
        pokemon (str): The name or Pokedex number of the Pokémon.

    Returns:
        dict: A dictionary with Pokémon data if the request is successful. Returns None if unsuccessful.
    """
    # Standardize the Pokémon name by:
    # - Ensuring it's a string,
    # - Removing any leading or trailing whitespace, and
    # - Converting it to lowercase
    pokemon = str(pokemon).strip().lower()

    # Validate the Pokémon name
    if pokemon == '':
        print('Error: No Pokémon name provided.')
        return None

    # Construct the URL to request Pokémon data
    request_url = POKE_API_URL + pokemon

    # Make the GET request to retrieve Pokémon data
    print(f'Retrieving information for {pokemon.capitalize()}...', end='')
    response = requests.get(request_url)

    # Check if the response was successful
    if response.status_code == requests.codes.ok:
        print('success')
        # Return the Pokémon data as a dictionary
        return response.json()
    else:
        print('failure')
        print(f'Response code: {response.status_code} ({response.reason})')
        return None

if __name__ == '__main__':
    main()
