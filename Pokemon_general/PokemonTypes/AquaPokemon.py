from Pokemon_general.Pokemon import Pokemon
from Pokemon_general.PokeType import PokemonType


class AquaPokemon(Pokemon):

    def __init__(self, pokemon_name, pokemon_id, current_hp, max_hp):

        # basic info about pokemon
        super().__init__(pokemon_name, pokemon_id, current_hp, max_hp)

        # additional info about pokemon
        self.primary_type = PokemonType(0)
        self.alive = True
        self.experience_points = 0
        self.fight_status = False
        
