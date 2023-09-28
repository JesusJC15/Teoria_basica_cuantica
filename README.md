# TEORÍA CUÁNTICA BÁSICA, OBSERVABLES Y MEDIDAS
## SISTEMA CUÁNTICO DE UNA LINEA
El sistema consiste en una partícula confinada a un conjunto discreto de posiciones en una línea. El simulador debe permitir especificar el número de posiciones y un vector ket de estado asignando las amplitudes.
1. El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.
2. El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
### Funciones
#### Requisitos
- Interprete de python
- Libreria numpy
1. normalizar(vect)
   Normaliza un vector dado.
   
   ![image](https://github.com/JesusJC15/observables_y_medidas/assets/93460550/1d8f655b-7342-4948-ade8-70bc50e91621)

3. part_una_linea(vect, pos)
    El sistema debe calcula la probabilidad de encontrarlo en una posición en particular.

   ![image](https://github.com/JesusJC15/observables_y_medidas/assets/93460550/dd57c414-45f2-4236-9c84-5a4d03d61e34)

5. transitar(vect1, vect2)
   El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.

   ![image](https://github.com/JesusJC15/observables_y_medidas/assets/93460550/099196ff-ccd3-4059-96b4-57191029cb76)
