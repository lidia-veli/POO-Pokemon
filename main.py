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


# IMPORTACIONES
import csv
import sys
from random import randint
from pokemon import (Pokemon, conj_active_ids)
from weapon_type import WeaponType

dict_weapon_type = {'punch':WeaponType.PUNCH, 'PUNCH':WeaponType.PUNCH,
                    'kick':WeaponType.KICK, 'KICK':WeaponType.KICK,
                    'headbutt':WeaponType.HEADBUTT, 'HEADBUTT':WeaponType.HEADBUTT,
                    'elbow':WeaponType.ELBOW, 'ELBOW':WeaponType.ELBOW}


# FUNCIONES

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
    
    # COMPROBAMOS QUE LOS PARÁMETROS SON CORRECTOS
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
    list_pokemon_obj = []  # lista donde vamos a ir guardando los objetos tipo Pokemon 

    for att_list in list_pokemon_att:  # para cada lista de atributos de un pokemon
        ident = int(att_list[0])  # int
        name = att_list[1]  # str
        weapon_type = dict_weapon_type[att_list[2]]  # WeaponType
        health = int(att_list[3])  # int
        attack = int(att_list[4])  # int
        defense = int(att_list[5])  # int
        # creamos el objeto tipo Pokemon
        pokemon = Pokemon(ident, name, weapon_type, health, attack, defense)

        # nos aseguramos de que realmente es un elemento de tipo Pokemon
        description = f"Pokemon ID {ident} with name {name} has as weapon {att_list[2].upper()} and health {health}"
        if bool(str(pokemon) == description) is False:  # si imprimir el objeto no coincide con esta descripción, es que no es un objeto tipo Pokemon
            raise TypeError("The parameter list_of_pokemons must be a list of Pokemon-type elements.")
        else:
            # es verdaderamente un objeto tipo Pokemon del formato deseado
            list_pokemon_obj.append(pokemon)  # añadimos el objeto a ls lista de objetos Pokemon
            

    # DEVOLVEMOS LA LISTA DE OBJETOS POKEMON
    return list_pokemon_obj


def  get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):
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
        [in] list_of_pokemons List of the Pokemons that are associated to the coach.

    Returns
    -------
        List List of the Pokemons associaated to the coach that are undefeated.

    Example
    -------
        >>> get_pokemon_in_a_list_of_pokemons(1, list_of_pokemons)
    """

    # COMPROBAMOS QUE LOS PARÁMETROS SON CORRECTOS
    # nos aseguramos de que el parámetro coach_to_ask es un entero
    if isinstance(coach_to_ask, int) is False:
        raise TypeError("The parameter coach_to_ask must be an integer.")

    # nos aseguramos de que el parámetro list_of_pokemons es una lista de elementos de tipo Pokemon
    for i in range(len(list_of_pokemons)):
        if isinstance(list_of_pokemons[i], Pokemon) is False:
            raise TypeError("The parameter list_of_pokemons must be a list of Pokemon-type elements.")


   # QUITAMOS LOS POKEMONS QUE SE HAN QUEDADO SIN VIDA
    for poke in list_of_pokemons:
        if poke.get_health_points() <= 0:  # si el pokemon no tiene vida
            list_of_pokemons.remove(poke)  # quitamos el pokemon de la lista
        else:
            pass

    # imprimir por pantalla la lista de pokemons para que el usuario pueda elegir
    #print(f"Coach {coach_to_ask} has {len(list_of_pokemons)} pokemons:")
    #for poke in list_of_pokemons:
    #  print(f'Pokemon: {poke.get_pokemon_id()}. Name: {poke.get_pokemon_name()}. Weapon: {poke.get_weapon_type().name}. Health: {poke.get_health_points()}. Attack: {poke.get_attack_rating()}. Defense: {poke.get_defense_rating()}.')


    # DEVOLVEMOS LA LISTA DE POKEMONS ACTUALIZADA
    return list_of_pokemons


def coach_is_defeated(list_of_pokemons):
    """Function to know if the Coach has been defeated.

    This function is used in order to know if the Coach is still undefeated.

    Syntax
    ------
       [ ] = coach_is_defeated(list_of_pokemons)

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
       >>> coach_is_defeated(list_of_pokemons)
    """

    if len(list_of_pokemons) == 0:
        return True
    else:
        return False



#--------------------------------------------------------------------------------
# FUNCIONES EXTERNALIZADAS de la función main()
#--------------------------------------------------------------------------------

def  elegir_pokemon(coach_to_ask, list_of_pokemons):
    '''Funcion para elegir un pokemon de la lista de pokemons de un entrenador.
    RETURN: pokemon seleccionado'''

    # COMPROBAMOS QUE LOS PARÁMETROS SON CORRECTOS
    # nos aseguramos de que el parámetro coach_to_ask es un entero
    if isinstance(coach_to_ask, int) is False:
        raise TypeError("The parameter coach_to_ask must be an integer.")
    
    # nos aseguramos de que el parámetro list_of_pokemons es una lista de elementos de tipo Pokemon
    for i in range(len(list_of_pokemons)):
        if isinstance(list_of_pokemons[i], Pokemon) is False:
            raise TypeError("The parameter list_of_pokemons must be a list of Pokemon-type elements.")


    # EL USUARIO ELIGE EL SIGUIENTE POKEMON QUE QUIERE USAR
    # bucle para repetir la elección del pokemon hasta que se elija uno válido
    while True:

        # imprimir por pantalla la lista de pokemons para que el usuario pueda elegir
        print()
        print(f"Coach {coach_to_ask} has {len(list_of_pokemons)} pokemons:")
        for poke in list_of_pokemons:
            print(f'Pokemon: {poke.get_pokemon_id()}. Name: {poke.get_pokemon_name()}. Weapon: {poke.get_weapon_type().name}. Health: {poke.get_health_points()}. Attack: {poke.get_attack_rating()}. Defense: {poke.get_defense_rating()}.')

        # pedimos al usuario que elija un pokemon
        entrada = input("Introduce the ID of the Pokemon you want to select: ")
        try:  # nos aseguramos de que es un entero
            poke_id = int(entrada)
        except:
            print()
            print("Pokemon ID must be an integer.")
            continue  # volvemos a pedir que elija un pokemon

        # y comprobamos que el ID está en el conjunto de IDs activos
        if poke_id not in conj_active_ids:
            print()
            print("This ID doesn't belong to any active pokemon. Choose another one.")
            continue  # volvemos a pedir que elija un pokemon
        else:
            pass
        
        # recorremos la lista de pokemons hasta encontrar el pokemon con el ID introducido por el usuario
        for poke in list_of_pokemons:
            if poke.get_pokemon_id() == poke_id:
                selected_pokemon = poke
                print(f'Selected pokemon: {selected_pokemon.get_pokemon_name()}.')
                return selected_pokemon
            else:
                pass  


def ronda_ataque_inicial(poke1, poke2):
    '''Función que modeliza la 1º ronda de ataque de un combate entre dos pokemons.
    RETURN: atacante en esa ronda (1 o 2).'''
    # elegimos aleatoriamente quien ataca primero
    if randint(0, 1) == 0:
        #poke1.fight_attack(poke2)  # ataca primero poke1
        print(f'Pokemon {poke1.get_pokemon_name()} attacked first.')
        return 1
    else:
        #poke2.fight_attack(poke1)  # ataca primero poke2
        print(f'Pokemon {poke2.get_pokemon_name()} attacked first.')
        return 2


def ronda_ataque(poke1, poke2, ataque_anterior):
    '''Función que modeliza las rondas de ataque (no iniciales) de un combate entre dos pokemons.
    RETURN: atacante en esa ronda (1 o 2).'''
    if ataque_anterior == 1:  # ha atacado antes el pokemon 1
        poke2.fight_attack(poke1)  # ahora ataca el pokemon 2
        print(f'Pokemon {poke2.get_pokemon_name()} attacked.')
        return 2
    
    else:  # ha atacado antes el pokemon 2
        poke1.fight_attack(poke2)  # ahora ataca el pokemon 1
        print(f'Pokemon {poke1.get_pokemon_name()} attacked.')
        return 1


def batalla(poke1, poke2):
    '''Funcion que modeliza una batalla entre dos pokemons.'''
    
    #si tienen las mismas características de ataque y defensa automáticamente hay EMPATE
    if poke1.get_attack_rating() == poke2.get_attack_rating() and poke1.get_defense_rating() == poke2.get_defense_rating():
        print('Both pokemons have the same attack and defense ratings.')
        print("It's a tie.")
        return None

    ronda = 1  # contador de rondas
    print(f'Round {ronda}:')
    atacante = ronda_ataque_inicial(poke1, poke2)  # en la 1º ronda se alige aleatoriamente el atacante

    while poke1.is_alive() and poke2.is_alive():  # mientras ambos pokemons estén vivos
        ronda += 1
        print(f'Round {ronda}:')
        atacante = ronda_ataque(poke1, poke2, atacante)  # depende de quien haya atacado antes

    # fuera del bucle, uno de los dos pokemons ha muerto
    if poke1.get_health_points() > 0:  # si al final poke1 está vivo
        print(f'Pokemon {poke1.get_pokemon_name()} won the battle.')
        return poke1
    
    # hemos salido del bucle, por lo que uno de los dos pokemons ha muerto
    # si poke1 no está vivo, entonces poke2 está vivo
    else:
        print(f'Pokemon {poke2.get_pokemon_name()} won the battle.')
        return poke2


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

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

    puntos_vida_team_1 = []  # lista de puntos de vida del equipo 1
    puntos_vida_team_2 = []  # lista de puntos de vida del equipo 2

    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")

    # Get configuration for Game User 1.
    pokemons_coach_1 = get_data_from_user('data/coach_1_pokemons.csv')
    puntos_vida_team_1.append( sum([poke.get_health_points() for poke in pokemons_coach_1]) )  # puntos de vida iniciales del equipo 1


    # Get configuration for Game User 2.
    pokemons_coach_2 = get_data_from_user('data/coach_2_pokemons.csv')
    puntos_vida_team_2.append( sum([poke.get_health_points() for poke in pokemons_coach_2]) )  # puntos de vida iniciales del equipo 2

    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of pokemons:
    list_active_ids = list(conj_active_ids)
    copy_pokemons_coach_1 = pokemons_coach_1.copy()
    copy_pokemons_coach_2 = pokemons_coach_2.copy()

    # Choose first pokemons
    poke_team_1 = elegir_pokemon(1, pokemons_coach_1)  # 1º pokemon del entrenador 1
    poke_team_2 = elegir_pokemon(2, pokemons_coach_2)  # 1º pokemon del entrenador 2
     

    # Main loop.
    
    # mientras los entrenadores tengan pokemons vivos
    while True:
        print('------------------------------------------------------------------')
        print(f"BATTLE between Team 1's: {poke_team_1.get_pokemon_name()} and Team 2's: {poke_team_2.get_pokemon_name()}")
        print('------------------------------------------------------------------')

        ganador_batalla = batalla(poke_team_1, poke_team_2)  # batalla entre los dos pokemons elegidos

        #actualizamos los puntos de vida de los equipos
        puntos_vida_team_1.append( sum([poke.get_health_points() for poke in pokemons_coach_1]) )  # puntos de vida del equipo 1 tras la batalla
        puntos_vida_team_2.append( sum([poke.get_health_points() for poke in pokemons_coach_2]) )  # puntos de vida del equipo 2 tras la batalla
        

        # actualizamos las listas de pokemons de los entrenadores, según quien haya sido el ganador de la batalla
        if ganador_batalla == poke_team_1:  # si el ganador es el pokemon 1
            pokemons_coach_2 = get_pokemon_in_a_list_of_pokemons(2, pokemons_coach_2)  # actualizamos la lista de pokemons del entrenador 2
            if coach_is_defeated(pokemons_coach_1) or coach_is_defeated(pokemons_coach_2):
                break
            else:
                poke_team_2 = elegir_pokemon(2, pokemons_coach_2)  # el entrenador 2 elige otro pokemon
                continue

        elif ganador_batalla == poke_team_2:  #  si el ganador es el pokemon 2
            pokemons_coach_1 = get_pokemon_in_a_list_of_pokemons(1, pokemons_coach_1)  # actualizamos la lista de pokemons del entrenador 1
            if coach_is_defeated(pokemons_coach_1) or coach_is_defeated(pokemons_coach_2):
                break
            else:
                poke_team_1 = elegir_pokemon(1, pokemons_coach_1)  # el entrenador 1 elige otro pokemon
                continue
        
        else: # ganador_batalla == None, EMPATE
            # ninguno de los dos pokemons han sufrido daños
            # cada entrenador elige un nuevo pokemon
            poke_team_1 = elegir_pokemon(1, pokemons_coach_1)
            poke_team_2 = elegir_pokemon(2, pokemons_coach_2)
            continue
            

    # fuera del bucle
    if not coach_is_defeated(pokemons_coach_1):  # si el entrenador 1 no ha sido derrotado
        print("------------------------------------------------------------------")
        print("Game User 1 has won the Game.")
        print("------------------------------------------------------------------")
    
    else:  # si el entrenador 2 no ha sido derrotado
        print("------------------------------------------------------------------")
        print("Game User 2 has won the Game.")
        print("------------------------------------------------------------------")



    print("------------------------------------------------------------------")
    print("The Game has ended")
    print("------------------------------------------------------------------")

    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")
    for ronda in range(len(puntos_vida_team_1)):
        if ronda == 0:
            print(f'Initial health points: {puntos_vida_team_1[ronda]}')
        elif ronda == len(puntos_vida_team_1)-1:
            print(f'Final health points: {puntos_vida_team_1[ronda]}')
        else:
            print(f'Health points in Round {ronda}: {puntos_vida_team_1[ronda]}')


    print('\n')
    print("Game User 2:")
    for ronda in range(len(puntos_vida_team_2)):
        if ronda == 0:
            print(f'Initial health points: {puntos_vida_team_2[ronda]}')
        elif ronda == len(puntos_vida_team_2)-1:
            print(f'Final health points: {puntos_vida_team_2[ronda]}')
        else:
            print(f'Health points in Round {ronda}: {puntos_vida_team_2[ronda]}')




# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
