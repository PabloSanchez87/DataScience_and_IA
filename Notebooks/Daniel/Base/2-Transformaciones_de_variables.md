## Transformaciones de variables

### Escalado y normalización
Se llevan las variables a la misma escala, para que sean comparables.

- `Min-max scalling`
    - Escala de 0 a 1
    - Ventajas:
        - Facilita la comparabilidad entre variables de diferentes escalas
        - La proporcionalidad entre los valores se mantiene
        - Es muy simple
    - Desventajas:
        - Es muy sensible a outliers
        - Si aparecen nuevos datos fuera del rango Xmin - Xmax deja de funcionar

- `Estandarización (z-score)`
    - Deka los valores con media cero y desviación estándar 1

    - Ventajas:
        - Adecuado para un distribución normal
    
    - Desventajas:
        - No es sensible a outliers
        - Si los datos tienen distribuiciones muy sesgadas no los convierte a distribuciones normales

- `Normalización(vectorial)`
    - Escala vectores para que tengan norma 1

    - Ventajas:
        - Mantiene la dirección de los vectores, únicamente escala su magnitud
        - Es útil en algoritmos basados en distancias como k-NN o algoritmos de clustering

    - Desventajas:
        - Se pueden eliminar relaciones entre variables. Si se utiliza el clustering para luego aplicar modelos por cluústers hay que tener esto en cuenta
        
- `Estandarización robusta`
    - Técnica de estandarización menos afectada por outliers

    - Ventajas:
        - Menor sensibilidad a outliers
        - Mejor rendimiento en datos normales

    - Desventajas:
        - No es muy eficiente en datos con distribuciones sesgadas
        - Se puede que no funcione en todos los casos

### Trasformación logaritmica
- Ventajas
    - Manejo de sesgos
    - Convierte relaciones no lineales en lineas
- Desventajas
    - Hace que los valores cercanos a cero se acerquen mucho.
    - Datos transformados menos intuitivos.

### Tratamiento de variables categóricas
- Convertir variables categóricas en formato numérico porque hay variables que no pueden tratar valores categóricos

- `One-hot encoding`
    - Por cada categoria de la varibale categórica crea un flag de pertenencia a ese grupo.

    - Ventajas:
        - Al ser un flag evita sesgos de magnitud.
        - Intuitivo
        - Compatible con algoritmos basados en distancias
        - Funciona bien con métodos de importancia de variables.

    - Desventajas:
        Si hay muchas categorias aumenta mucho la dimensionalidad del problema.
        - Si hay muchas categorías puede ser poco interpretable.

- `Ordinal encoding`
    - Añadir un contador a cada categoría.
    - Ventajas:
        - No aumenta la dimensionalidad del problema.
        - Se puede interpretar mejor.
        - Da flexibilidad al poder meter una métrica personalizada.
    - Desventajas:
        - Se puede que no funcione en todos los casos.
        - Depende de la calidad de la variable.
        - No es muy eficiente en grandes conjuntos de datos.

- `Target encoding`
    - A cada categoría se le asigna algún estadístico de la variable objetivo, normalmente la media o mediana.
    - Ventajas:
        - Simple y no aumenta la dimensionalidad del problema.
        - Captura mucha información sobre la categoría
        - Adecuado para modelos basados en distancias.
        - Da flexibilidad al poder meter una métrica personalizada.
    - Desventajas:
        - Riesgo de fuga de datos (data leakage)
        - Dependencia de la caldiad del objetivo
        - Menor interpretabilidad

- `Embedding`
    - Consisten en aplicar un modelo, para crear vectores de características que representen la variable/categorias.
    - Ventajas:
        - Muy eficiente en grandes conjuntos de datos.
        - Util para aplicar modelos basados en distancias.
    - Desventajas:
        - No es muy intuitivo.
        - Muy complejo.
        - Muy costoso computacionalmente.





