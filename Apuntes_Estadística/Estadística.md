# Glosario de Estadística para Data Science e Inteligencia Artificial

## **1. Media (Promedio)**
- **Definición**: Es el valor promedio de un conjunto de datos, calculado como la suma de todos los valores dividida por la cantidad de valores.
- **Explicación**: Ayuda a resumir los datos en un solo número representativo. Por ejemplo, si tus datos son [2, 4, 6], la media sería \( (2+4+6)/3 = 4 \).
- **Interpretación**: Indica el valor típico en un conjunto de datos.
- **Cuándo usarla**: Es útil cuando los datos no tienen valores extremos significativos (outliers), ya que estos pueden distorsionar el promedio.


---

## **2. Mediana**
- **Definición**: Es el valor central de un conjunto de datos ordenados.
- **Explicación**: Divide los datos en dos mitades. Si hay un número impar de valores, la mediana es el del medio; si es par, es el promedio de los dos del centro. Útil cuando los datos tienen valores extremos (outliers).
- **Interpretación**: Refleja el valor central y no se ve afectada por outliers.
- **Cuándo usarla**: Ideal para distribuciones sesgadas o con outliers significativos.

---

## **3. Moda**
- **Definición**: Es el valor o valores que aparecen con más frecuencia en un conjunto de datos.
- **Explicación**: Ideal para datos categóricos. Por ejemplo, en ["rojo", "azul", "rojo"], la moda es "rojo".
- **Interpretación**: Representa la opción más común en los datos.
- **Cuándo usarla**: Útil en análisis de frecuencia o para entender la categoría más prevalente.

---

## **4. Varianza**
- **Definición**: Mide cuánto varían los datos con respecto a la media.
- **Explicación**: Una varianza alta significa que los datos están más dispersos; una varianza baja indica que están más cerca de la media. Fórmula: \( \sigma^2 = \frac{\sum (x_i - \mu)^2}{N} \).
- **Interpretación**: Indica la variabilidad de los datos, pero está en unidades al cuadrado.
- **Cuándo usarla**: Para comparar dispersión entre conjuntos de datos con la misma escala.

    ![Boxplot Varianza](/img/boxplot_varianza.png)

---

## **5. Desviación estándar**
- **Definición**: Es la raíz cuadrada de la varianza.
- **Explicación**: Indica cuánto se desvían los datos, en promedio, de la media. Más fácil de interpretar que la varianza porque está en las mismas unidades que los datos.
- **Interpretación**: Un valor alto indica mayor dispersión; uno bajo, mayor concentración cerca de la media.
- **Cuándo usarla**: Útil para evaluar la consistencia de los datos o el rendimiento de un modelo.

---

## **6. Correlación**
- **Definición**: Mide la relación entre dos variables.
- **Explicación**: Va de -1 a 1. Un valor cercano a 1 indica una relación positiva fuerte; -1, una negativa fuerte; 0, ninguna relación.
- **Interpretación**: Indica la dirección y fuerza de la relación lineal.
- **Cuándo usarla**: Ideal para explorar relaciones entre variables continuas. Evitar interpretarla como causalidad.

    ![Scatter Correlación](/img/scatter_correlacion.png)

---

## **7. Regresión**
- **Definición**: Es una técnica para modelar la relación entre una variable dependiente y una o más independientes.
- **Explicación**: Se utiliza para hacer predicciones. Por ejemplo, predecir las ventas en función del gasto publicitario.
- **Interpretación**: Los coeficientes indican cómo afecta cada variable independiente a la dependiente.
- **Cuándo usarla**: Útil cuando las variables tienen una relación causal o predictiva clara.

---

## **8. Distribución normal**
- **Definición**: Es una distribución de datos en forma de campana simétrica alrededor de la media.
- **Explicación**: Muchos fenómenos naturales siguen esta distribución, lo que la hace fundamental en estadísticas e IA.
- **Interpretación**: La mayoría de los valores se concentran cerca de la media.
- **Cuándo usarla**: Es base para muchos modelos estadísticos. No adecuada si los datos están sesgados.

    ![Distribución Normal](/img/distribucion_normal.png)

---

## **9. P-valor**
- **Definición**: Es la probabilidad de obtener resultados al menos tan extremos como los observados, asumiendo que la hipótesis nula es verdadera.
- **Explicación**: Si el p-valor es bajo (por ejemplo, < 0.05), se rechaza la hipótesis nula. Ayuda a validar hipótesis en experimentos.
- **Interpretación**: Un p-valor bajo sugiere evidencia contra la hipótesis nula.
- **Cuándo usarla**: En pruebas de hipótesis. No debe ser el único criterio de decisión.

---

## **10. Intervalo de confianza**
- **Definición**: Rango de valores dentro del cual se espera que esté un parámetro poblacional con cierto nivel de confianza.
- **Explicación**: Un intervalo de confianza del 95% significa que estamos 95% seguros de que el valor verdadero está dentro de ese rango.
- **Interpretación**: Proporciona una estimación del parámetro poblacional.
- **Cuándo usarla**: Para comunicar la precisión de una estimación.

---

## **11. Test de hipótesis**
- **Definición**: Es un procedimiento para decidir si aceptar o rechazar una hipótesis basada en datos muestrales.
- **Explicación**: Se utiliza para validar suposiciones, como si un medicamento es efectivo o no.
- **Interpretación**: Rechazar o aceptar la hipótesis con base en el p-valor.
- **Cuándo usarla**: Para validar hipótesis en investigación. Requiere buen diseño experimental.

---

## **12. Outliers (Valores atípicos)**
- **Definición**: Son datos que se alejan significativamente del resto.
- **Explicación**: Pueden ser errores o datos interesantes que requieren análisis adicional.
- **Interpretación**: Indican posibles errores o fenómenos inusuales.
- **Cuándo usarla**: Analizar su causa antes de eliminarlos. Útiles en ciertos contextos.

---

## **13. Muestreo**
- **Definición**: Es el proceso de seleccionar un subconjunto de datos de una población para análisis.
- **Explicación**: Permite trabajar con menos datos sin analizar toda la población, ahorrando tiempo y recursos.
- **Interpretación**: La representatividad del muestreo es clave.
- **Cuándo usarla**: Cuando no es posible analizar toda la población. Evitar sesgos.

---

## **14. Overfitting (Sobreajuste)**
- **Definición**: Ocurre cuando un modelo se ajusta demasiado bien a los datos de entrenamiento y falla en generalizar a datos nuevos.
- **Explicación**: Es como memorizar en lugar de aprender.
- **Interpretación**: El modelo funciona bien en entrenamiento pero mal en datos reales.
- **Cuándo usarla**: Evitarlo con técnicas como validación cruzada.

---

## **15. Underfitting (Subajuste)**
- **Definición**: Ocurre cuando un modelo es demasiado simple y no captura las tendencias de los datos.
- **Explicación**: Es como tratar de resumir un libro completo en una frase y perder detalles clave.
- **Interpretación**: El modelo tiene un rendimiento deficiente en entrenamiento y prueba.
- **Cuándo usarla**: Asegurar suficiente complejidad del modelo.

---

## **16. Tipos de Variables**
- **Definición**: Características o propiedades que se pueden medir, observar o categorizar.
- **Explicación**: 
  - **Categóricas**: Representan categorías o grupos. Ejemplo: género, estado civil.
    - **Nominales**: Sin orden natural. Ejemplo: país de origen.
    - **Ordinales**: Con orden natural. Ejemplo: niveles de tabaquismo.
  - **Numéricas**: Representan cantidades.
    - **Discretas**: Valores contables. Ejemplo: número de hijos.
    - **Continuas**: Valores medibles. Ejemplo: peso, altura.
- **Interpretación**: Determina el tipo de análisis estadístico aplicable.

---

## **17. Transformaciones de Variables**
- **Definición**: Procesos que ajustan los datos para facilitar su análisis.
- **Explicación**: 
  - **Escalado Min-Max**: Normaliza los valores entre 0 y 1. Útil para algoritmos sensibles a la escala.
  - **Estandarización (Z-score)**: Ajusta los datos a media 0 y desviación estándar 1. Ideal para datos normales.
  - **Logarítmica**: Reduce el impacto de valores extremos.
- **Interpretación**: Mejora la compatibilidad con ciertos algoritmos.
- **Cuándo usarla**: Elegir la técnica según la distribución de los datos.

---

## **18. Aprendizaje Supervisado**
- **Definición**: Tipo de aprendizaje automático donde los datos incluyen etiquetas.
- **Explicación**: 
  - **Clasificación**: Predice categorías. Ejemplo: spam/no spam.
  - **Regresión**: Predice valores continuos. Ejemplo: precio de una casa.
- **Interpretación**: Depende de la métrica de evaluación utilizada.
- **Cuándo usarla**: Cuando los datos están etiquetados.

---

## **19. Aprendizaje No Supervisado**
- **Definición**: Tipo de aprendizaje automático donde los datos no tienen etiquetas.
- **Explicación**: Se enfoca en encontrar patrones. Ejemplo: agrupamiento (clustering).
- **Interpretación**: Los resultados necesitan validación interpretativa.
- **Cuándo usarla**: Para explorar datos desconocidos o sin etiquetar.

---

## **20. Métricas de Evaluación**
- **Definición**: Indicadores que miden el rendimiento de un modelo.
- **Explicación**: 
  - **Precisión**: Proporción de predicciones correctas.
  - **Recall (Sensibilidad)**: Capacidad de identificar correctamente casos positivos.
  - **F1 Score**: Promedio armónico de precisión y recall.
- **Interpretación**: Ayudan a comparar modelos y elegir el más adecuado.
- **Cuándo usarla**: Elegir la métrica según el contexto del problema.

---

## **21. Distribuciones de Probabilidad**
- **Definición**: Modelos matemáticos que describen cómo se distribuyen los datos.
- **Explicación**:
  - **Distribución binomial**: Modela eventos con dos resultados posibles, como lanzar una moneda.  
    Ejemplo: Si lanzas una moneda 10 veces, la distribución binomial puede predecir la probabilidad de obtener 6 caras.
  - **Distribución de Poisson**: Utilizada para eventos raros en un intervalo de tiempo.  
    Ejemplo: Número de llamadas en una central telefónica por minuto.
- **Interpretación**: Ayudan a modelar incertidumbre en problemas reales.
- **Cuándo usarla**: Elegir según el fenómeno que se modela (binomial para eventos discretos, normal para fenómenos continuos, etc.).

---

## **22. Matriz de Confusión**
- **Definición**: Herramienta para evaluar el rendimiento de un modelo de clasificación.
- **Explicación**: Contiene cuatro métricas clave:
  - **Verdaderos positivos (TP)**: Predicciones correctas de casos positivos.
  - **Falsos positivos (FP)**: Predicciones incorrectas de casos positivos.
  - **Verdaderos negativos (TN)**: Predicciones correctas de casos negativos.
  - **Falsos negativos (FN)**: Predicciones incorrectas de casos negativos.
- **Ejemplo**: En un modelo para detectar spam:
  - TP: Correos spam detectados correctamente.
  - FN: Correos spam no detectados.
- **Interpretación**: Proporciona una visión completa de errores y aciertos.
- **Cuándo usarla**: Para analizar el rendimiento de clasificadores binarios o multiclase.

---

## **23. Regularización**
- **Definición**: Técnica para prevenir el sobreajuste en modelos de aprendizaje automático.
- **Explicación**:
  - **L1 (Lasso)**: Penaliza los coeficientes absolutos grandes, promoviendo soluciones dispersas.  
    Ejemplo: Útil para selección de variables.
  - **L2 (Ridge)**: Penaliza los coeficientes al cuadrado, manteniendo valores pequeños.  
    Ejemplo: Útil cuando todas las variables aportan información.
- **Interpretación**: Introduce un sesgo para reducir la varianza.
- **Cuándo usarla**: Para mejorar la generalización de modelos lineales.

---

## **24. Validación Cruzada**
- **Definición**: Técnica para evaluar el rendimiento de un modelo dividiendo los datos en conjuntos de entrenamiento y prueba.
- **Explicación**:
  - Divide los datos en "k" subconjuntos (folds).
  - Entrena el modelo en \(k-1\) conjuntos y prueba en el restante.
  - Repite \(k\) veces y promedia los resultados.
- **Interpretación**: Reduce el riesgo de sobreajuste y proporciona una evaluación robusta.
- **Cuándo usarla**: Siempre que se evalúe un modelo, especialmente con conjuntos de datos pequeños.

---

## **25. Reducción de Dimensionalidad**
- **Definición**: Técnicas para simplificar datos de alta dimensionalidad preservando su esencia.
- **Explicación**:
  - **PCA (Análisis de Componentes Principales)**: Encuentra combinaciones lineales de variables que maximizan la varianza.
  - **t-SNE**: Representa datos en 2D o 3D para visualización.  
    Ejemplo: Visualizar agrupaciones en un dataset de imágenes.
- **Interpretación**: Mejora la interpretabilidad y rendimiento de modelos.
- **Cuándo usarla**: Para reducir ruido o acelerar cálculos en datasets grandes.

---

## **26. Algoritmos de Clustering**
- **Definición**: Agrupan datos en base a similitudes.
- **Explicación**:
  - **K-Means**: Divide los datos en \(k\) grupos mediante centroides.
  - **DBSCAN**: Detecta grupos densos y puntos atípicos.
- **Ejemplo**: Segmentación de clientes en función de sus hábitos de compra.
- **Interpretación**: Los grupos representan patrones o segmentos en los datos.
- **Cuándo usarla**: Cuando no se tienen etiquetas y se busca descubrir patrones.
