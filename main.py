#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python method contains the application of the Game.

@contents :  This module contains the complete implementation of the application
             of the Game.
@project :  N/A
@program :  N/A
@file :  main.py
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

import csv
from classes.pokemon import Pokemon
from classes.weapon_type import WeaponType

dict_weapon_type = {'punch':WeaponType.PUNCH, 'PUNCH':WeaponType.PUNCH,
                    'kick':WeaponType.KICK, 'KICK':WeaponType.KICK,
                    'headbutt':WeaponType.HEADBUTT, 'HEADBUTT':WeaponType.HEADBUTT,
                    'elbow':WeaponType.ELBOW, 'ELBOW':WeaponType.ELBOW
                    }


def get_data_from_user(name_file):
    """Function to obtain data from each user.

    This function obtains data from each user in order to set the configuration
    of the Game.

    Syntax
    ------
      [ ] = get_data_from_user(name_file)

    Parameters
    ----------
      name_file str Name of the CSV file.

    Returns
    -------
      list_pokemons List of Pokemons obtained from CSV .

    Example
    -------
      >>> list_pokemons = get_data_from_user("file.csv")
    """

    # nos aseguramos de que el parametro name_file es un string
    if isinstance(name_file, str) is False:
        raise TypeError("The name of the file must be a string.")

    else:
        # y nos aseguramos de que el fichero existe
        try:
            list_pokemon_att = []  # lista de listas de atributos que definen un pokemon
            with open(name_file, 'r', encoding="utf-8") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    list_pokemon_att.append(row)
       
        except FileNotFoundError:
            print("The file does not exist.")


    # TRANSFORMAR CADA LISTA DE ATRIBUTOS POKEMON EN UN OBJETO TIPO POKEMON
    list_pokemon_obj = []  # lista de objetos tipo Pokemon
    for i in range(len(list_pokemon_att)):
        pokemon = Pokemon( int(list_pokemon_att[i][0]), list_pokemon_att[i][1], dict_weapon_type[list_pokemon_att[i][2]], int(list_pokemon_att[i][3]), int(list_pokemon_att[i][4]), int(list_pokemon_att[i][5]) )
        #                    identifyer                  name                    weapon_type                                health                       attack                       defense

        # nos aseguramos de que el parámetro list_of_pokemons debe ser una lista de elementos de tipo Pokemon
        description = f"Pokemon ID {list_pokemon_att[i][0]} with name {list_pokemon_att[i][1]} has as weapon {list_pokemon_att[i][2].upper()} and health {list_pokemon_att[i][3]}"
        if bool(str(pokemon) == description) == False:
            raise TypeError("The parameter list_of_pokemons must be a list of Pokemon-type elements.")
        else:
            # es verdaderamente un objeto tipo Pokemon del formato deseado
            list_pokemon_obj.append(pokemon)

    # DEVOLVEMOS LA LISTA DE OBJETOS POKEMON
    return list_pokemon_obj



def get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):
    """Function to know the list of Pokemons that are associated to the Coach.

    This function is used in order to know the list of Pokemos that are
    associated to the coach. This function prints the result of this list, so
    the user can select a Pokemon.

    Syntax
    ------
       [ ] = get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):

    Parameters
    ----------
       [in] coach_to_ask Coach to ask for her/his list of Pokemons.
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       List List of the Pokemons associaated to the coach that are undefeated.

    Example
    -------
       >>> get_pokemon_in_a_list_of_pokemons(1, list_of_pokemons)
    """





def coach_is_undefeated(list_of_pokemons):
    """Function to know if the Coach is still undefeated.

    This function is used in order to know if the Coach is still undefeated.

    Syntax
    ------
       [ ] = coach_is_undefeated(list_of_pokemons)

    Parameters
    ----------
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       Boolean True if the coach has all her/his Pokemons defeated.
               False if the coach has any Pokemon that is undefeated.

    Example
    -------
       >>> coach_is_undefeated(list_of_pokemons)
    """


def main():
    """Function main of the module.

    The function main of this module is used to perform the Game.

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

    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")

    # Get configuration for Game User 1.


    # Get configuration for Game User 2.


    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of pokemons:


    # Choose first pokemons
 

    # Main loop.



    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")


    print("Game User 2:")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
