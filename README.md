link repositorio: https://github.com/lidia-veli/POO-Pokemon  
# Parcial POO Pokemon

## EJERCICIO 1 (5 puntos) 

En este ejercicio, vamos a hacer una versión programada en Python para que dos jugadores puedan jugar a este juego. Los jugadores se encontrarán representados por los entrenadores de cada uno de los equipos.   

En base a estas especificaciones se solicita que programe la clase Pokémon. Cada criatura Pokémon va a estar caracterizado por:     
- ID del Pokémon. Número entero y único que identifica a la criatura Pokémon.
- Nombre del Pokémon. Nombre de la critarua Pokémon.
- Tipo de arma que lleva a cabo el Pokémon. En esta primera versión del juego, solamente 4 tipos de arma van a existir: Puñetazo, Patada, Codazo, Cabezazo.
- Puntos de salud que tiene el Pokémon. Deben de estar entre 1 y 100.
- Índice de ataque del Pokémon. Deben de estar entre 1 y 10.
- Índice de defensa del Pokémon. Deben de estar entre 1 y 10.

Nota: Es obligatorio el uso de enumerados para el atributo del tipo de arma. El índice de ataque del Pokémon se recomienda que contenga el valor del tipo de arma. Se recuerda que el enumerado en Python tiene el formato 'Clave / Valor'.

Se pide:

1. Incluya los atributos de esta clase y establezca la visibilidad adecuada (público, privado, protegido). Añada cualquier atributo y/o método que considere necesario.

2. Programe un método constructor que reciba los datos necesarios para crear un Pokémon. El método debe verificar el tipo y valor de cada uno de los parámetros y lanzar la excepción correspondiente cuando no se cumplan los requisitos. El método constructor debe asegurarse de que el atributo ID es una identificación nueva no tomada por otros Pokémons. Así mismo, programe también un método destructor que se encarge de eliminar la instancia de Pokemon de la variable lista de IDs global.

3. Programe un método que mejor corresponda para imprimir objetos de tipo Pokemon según el siguiente ejemplo: “Pokemon ID 8 with name Bulbasaur has as weapon PUNCH and health 87.”

4. Programe los métodos setters y getters para la clase en función de lo que necesite. Si no necesita algún o ningún getter y/o setter, argumente por qué en un comentario dentro del módulo.

5. Programe el método is_alive(self) de la clase Pokémon. Este método sirve para saber si el Pokemon está vivo.

6. Programe el método fight_attack(self, Pokémon pokemon_to_attack). Método que implementa el ataque del Pokémon usando un golpe sobre otro Pokémon. Este método se basa en el método fight_defense(self, int points_of_damage) del Pokémon atacado. Se aplicará el índice de ataque del Pokémon atacante como representación del golpe dado. Este método devolverá un booleano True si se ha podido atacar a la criatura Pokémon.

7. Programe el método fight_defense(self, int points_of_damage). Este método implementa la defensa del Pokémon de un golpe de otro Pokémon. Este método actualiza el atributo de puntos de salud que tiene el Pokémon en base a los puntos de daño recibidos menos el índice de defensa del propio Pokémon. Si el índice de defensa es mayor que los puntos de ataque recibidos, el método devolverá false y el Pokémon no sufrirá ningún daño. Este método devolverá un booleano True si se ha sufrido un ataque por parte de otra criatura Pokémon.

8. Pruebe los objetos de la clase Pokémon con los casos de prueba que se le han pasado.


Para ayudar en el desarrollo de este ejercicio, se le hace entrega de un UML parcialmente completo de la posible implementación de este juego. Se puede modificar o realizar un UML completamente distinto, el cuál es necesario explicar brevemente en un documento de texto o en los comentarios de un fichero .py. En caso de realizar un UML diferente, no se aplicarán los criterios en base a los casos de prueba facilitados, que es probable que no funcionen sin una adaptación previa.  

Se facilitan también los archivos vacíos dónde deberán estar implementadas las clases que se piden y que tienen que ser completadas por el alumno. En dichas clases, están ya añadidos los casos de prueba de cada una de ellas.
