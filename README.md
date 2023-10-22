# TEORÍA CUÁNTICA BÁSICA, OBSERVABLES Y MEDIDAS
Este repositorio contiene un conjunto de funciones para realizar operaciones en el contexto de mecánica cuántica, incluyendo normalización de vectores, cálculo de probabilidades, cálculo de valores esperados y varianza de observables, así como el cálculo de valores propios y probabilidades de transición. El código está implementado en Python y utiliza la biblioteca NumPy para realizar cálculos matriciales.
### Funciones
#### Requisitos
- Interprete de python
- Libreria numpy
  
1. normalizar(vect): Normaliza un vector dado, asegurando que su norma sea igual a 1 (en caso de que no sea un vector unitario).
   
   ![image](https://github.com/JesusJC15/observables_y_medidas/assets/93460550/1d8f655b-7342-4948-ade8-70bc50e91621)

2. part_una_linea(vect, pos): Calcula la probabilidad de encontrar una partícula en una posición específica de un sistema probabilístico de una línea.

   ![image](https://github.com/JesusJC15/observables_y_medidas/assets/93460550/dd57c414-45f2-4236-9c84-5a4d03d61e34)

3. ampli_tran(vect1, vect2): Calcula la probabilidad de amplitud de transición entre dos vectores.

   ![image](https://github.com/JesusJC15/Teoria_basica_cuantica/assets/93460550/085f0bc9-e1ac-4daa-806b-3be0f10d9eb2)

4. media_varianza(mat_obs, vect_est): Calcula la media y la varianza de un observable en un estado dado.

   ![image](https://github.com/JesusJC15/Teoria_basica_cuantica/assets/93460550/fbf5080e-a13b-466a-a2ba-c896844b04ea)

5. val_y_vect_prop(mat_obs, vect_est): Calcula los valores propios del observable y la probabilidad de que el sistema transite a uno de los vectores propios después de una observación.

   ![image](https://github.com/JesusJC15/Teoria_basica_cuantica/assets/93460550/02b9d854-0804-4ef6-a1a6-1cdcd3ba8ed4)
