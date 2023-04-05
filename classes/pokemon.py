#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the class Pokemon, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  pokemon.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Francisco Hernando Gallego (francisco.hernandogallego@ceu.es)
           Ruben Juarez Cadiz (ruben.juarezcadiz@ceu.es)

@version :  0.0.1, 08 November 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""


# Source packages.

from classes.weapon_type import WeaponType
conj_active_ids = {''}  # conjunto vacío de ids activos
    # lo hacemso conjunto porque simplemente lo vamos a usar para comprobar si un ID está activo o no,
    # realmente no vamos a tener que acceder a los elementos del conjunto (en cuyo caso usaríamos una lista).

class Pokemon():
    """Python class to implement a basic version of a Pokemon of the game.

    This Python class implements the basic version of a Pokemon of the game.

    Syntax
    ------
      obj = Pokemon(id, pokemon_name, weapon_type, health_points,
                   attack_rating, defense_rating)

    Parameters
    ----------
      [in] id ID of the Pokemon.
      [in] pokemon_name Name of the Pokemon.
      [in] weapon_type Type of weapon that carries out the Pokemon.
      [in] health_points Points of health that the Pokemon has.
      [in] attack_rating Attack rating of the Pokemon.
      [in] defense_rating Defense rating of the Pokemon.

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class Pokemon.

    Attributes
    ----------

    Example
    -------
      >>> from pokemon import Pokemon
      >>> from weapon_type import WeaponType
      >>> obj_Pokemon = Pokemon(1, "Bulbasaur", WeaponType.PUNCH, 100, 7, 10)
    """


    #atributos de instancia, los ponemos todos privados
    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points, attack_rating, defense_rating):
        self.__pokemon_id = pokemon_id  # int
        conj_active_ids.add(int(pokemon_id))  # asegurándonos de que lo ahcemos en formato de numero entero
            # al instanciar un objeto de la clase Pokemon, añadimos su id al conjunto de ids activos
        self.__pokemon_name = pokemon_name  # str
        self.__weapon_type = weapon_type  # WeaponType
        self.__health_points = health_points  # int in [1,100]
        self.__attack_rating = attack_rating  # int in [1,10]
        self.__defense_rating = defense_rating  # int in [1,10]

        # verificamos que los parámetros de entrada son del tipo correcto y son válidos
        if not isinstance(self.__pokemon_id, int) and self.__pokemon_id not in conj_active_ids:
            # ID debe ser un entero y no haber sido usado previamente
            raise TypeError("The parameter pokemon_id must be a valid integer.")
        if not isinstance(self.__pokemon_name, str):
            raise TypeError("The parameter pokemon_name must be a string.")
        if not isinstance(self.__weapon_type, WeaponType):
            raise TypeError("The parameter weapon_type must be a WeaponType.")
        if not isinstance(self.__health_points, int) and self.__health_points not in range(1, 101):
            raise TypeError("The parameter health_points must be an integer between 1 and 100.")
        if not isinstance(self.__attack_rating, int) and self.__attack_rating not in range(1, 11):
            raise TypeError("The parameter attack_rating must be an integer between 1 and 10.")
        if not isinstance(self.__defense_rating, int) and self.__defense_rating not in range(1, 11):
            raise TypeError("The parameter defense_rating must be an integer between 1 and 10.")

    def __str__(self):
        return "Pokemon ID " + str(self.__pokemon_id) + " with name " + self.__pokemon_name + " has as weapon " + self.__weapon_type._name_ + " and health " + str(self.__health_points)
    #    return f"Pokemon ID {self.__pokemon_id} with name {self.__pokemon_name} has as weapon {self.__weapon_type._name_} and health {self.__health_points}"
    
    #def __del__(self):
    #    print("Pokemon deleted")
    #    Pokemon.conj_active_ids.remove(self.__pokemon_id) # quitamos el id del pokemon eliminado de la lista de ids activos


    # GETTERS y SETTERS
    def get_pokemon_id(self): 
        return self.__pokemon_id
    def get_pokemon_name(self):
        return self.__pokemon_name
    def get_weapon_type(self):
        return self.__weapon_type
    def get_health_points(self):
        return self.__health_points
    def get_attack_rating(self):
        return self.__attack_rating
    def get_defense_rating(self):
        return self.__defense_rating
    
    def set_health_points(self, new_health_points):
        # los puntos de salud no pueden superar los 100 puntos
        # sí permitimos que sean negativos, ya que eso indica que el pokemon está muerto
        if new_health_points <= 100:  
            self.__health_points = new_health_points
        else:
            raise ValueError("The parameter new_health_points must be a valid integer.")
    
    def set_attack_rating(self, new_attack_rating):
        self.__attack_rating = new_attack_rating
    def set_defense_rating(self, new_defense_rating):
        self.__defense_rating = new_defense_rating
    

    def is_alive(self): # devuelve True si el pokemon sique vivo, esto es, tiene puntos de salud > 0
        '''Método para saber si el Pokemon está vivo o no'''
        if self.get_health_points() > 0:  # está vivo, si todavia tiene health_points
            return True
        else:  # si se ha quedado sin vida
            conj_active_ids.remove(self.get_pokemon_id())  # quitamos su id del conjunto de ids activos
            return False

    def fight_defense(self, damage_points):
        '''Método que implementa la defensa del Pokémon a un golpe de otro Pokémon'''
        if damage_points >= self.get_defense_rating():  # si los puntos de daño superan a nuestros puntos de defensa, nuestra salud se ve afectada
            damage = damage_points - self.get_defense_rating()  # calculamos el daño que recibiremos en base a sus puntos de defensa
            self.set_health_points( self.get_health_points() - damage )  # actualizamos la salud del pokemon con el daño recibido
            return True  # nos han hecho daño
        else:
            return False  # no nos han hecho daño
    
    def fight_attack(self, enemy):
        '''Método que implementa el ataque del Pokémon usando un golpe sobre otro Pokémon.
            Basado en el fight_defense del pokemon enemigo'''
        if not isinstance(enemy, Pokemon):  # nos aseguramos de que el enemigo es un objeto de la clase Pokemon
            raise TypeError("The parameter enemy must be a Pokemon.")
        else:
            if self.get_attack_rating() >= enemy.get_defense_rating(): # si nuestro ataque es mayor que su defensa, hacemos daño al enemigo
                enemy.fight_defense( self.get_attack_rating() ) # el enemigo se defiende de nuestro ataque
                return True # hemos podido atacar
            else:
                return False # no hemos podido atacar





def main():
    """Function main of the module.

    The function main of this module is used to test the Class that is described
    in this module.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = Pokemon(1, "Ivysaur", WeaponType.HEADBUTT, 100, 8, 9)

    if pokemon_1.get_pokemon_name() == "Ivysaur":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 9:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = Pokemon(2, "Charmander", WeaponType.HEADBUTT, 100, 7, 10)

    if str(pokemon_2) == "Pokemon ID 2 with name Charmander has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = Pokemon(3, "Wartortle", WeaponType.KICK, 97, 8, 9)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = Pokemon(4, "Squirtle", WeaponType.ELBOW, 93, 9, 6)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = Pokemon(5, "Venusaur", WeaponType.PUNCH, 99, 10, 7)
    pokemon_6 = Pokemon(6, "Charmeleon", WeaponType.PUNCH, 99, 9, 8)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 97:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
