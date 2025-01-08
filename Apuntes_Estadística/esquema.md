┌─────────────────────────────────────────────────────────────┐
│            Análisis Exploratorio de Datos (EDA)             │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        v
            ┌────────────────────────────────────────┐
            │    Calidad y Preparación de Datos       │
            └─────────────────┬──────────────────────┘
                              │
                              v
   - Limpieza y Validación: Tratamiento de valores faltantes (imputar/eliminar),
     corrección de errores, eliminación o codificación de datos atípicos no justificados.
   - Dominio: Conocer qué representan las variables, qué rangos son esperables.
   - Herramientas: pandas (Python), dplyr (R)

   Iterar este paso hasta asegurar datos suficientemente consistentes.

────────────────────────────────────────────────────────────────

                                ┌─────────────────────┐
                                │   Distribución de    │
                                │        Datos         │
                                └───────┬────────────┘
                                        │
                                        v
                           ┌──────────────────────────┐
         Simetría ←──────▶│    Distribución Simétrica │◀─────→ Asimetría
                           └───────┬─────────────────┘
                                   │
                         ┌─────────┴─────────┐
                         │                   │
                         v                   v
               ┌─────────────────────┐  ┌────────────────────────────┐
       Medidas de Tendencia Central   │  │   Medidas de Dispersión     │
     (Media, Mediana, Moda)          │  │ (Rango, Varianza, STD, IQR, MAD)
               └─┬────────────────────┘  └───────┬─────────────────┘
                 │                                 │
                 v                                 v
      Influencia de valores extremos          Sensibilidad a valores extremos
      - Si hay outliers: Mediana > Media      - Varianza & STD ↑ si outliers
      - IQR o MAD en vez de Varianza/STD       - IQR/MAD más robustos

      **Interpretación:**
      - Media ~ Mediana ~ Moda → distribución simétrica.
      - Diferencias grandes → posible asimetría o outliers.

────────────────────────────────────────────────────────────────

   ┌────────────────────────────────────────────────────────────────┐
   │                Distribución Asimétrica (Skew)                   │
   └───────┬────────────────────────────────────────────────────────┘
           │
           v
   Asimetría Positiva (derecha):          Asimetría Negativa (izquierda):
   - Media > Mediana > Moda               - Media < Mediana < Moda
   - Cola larga a la derecha              - Cola larga a la izquierda

   **Skewness (coef. de asimetría):**
   - Skewness ≈ 0 → simétrica
   - Skewness > 0 → asimetría positiva
   - Skewness < 0 → asimetría negativa
   **Cuidado:** Un valor pequeño no siempre implica simetría perfecta; considerar el tamaño muestral.

   **Curtosis:**
   - Mide “apuntamiento” o colas pesadas.
   - Curtosis > 3 (mesocúrtica estándar): colas más pesadas que una normal.
   - Curtosis < 3: colas menos pesadas.
   **Cuidado:** Altas curtosis pueden indicar más riesgo de valores extremos, no necesariamente “picos” estrechos.

   Si fuerte asimetría:
   - Transformaciones (log, Box-Cox).
   - Usar estadísticas robustas (Mediana, IQR).
   - Visualizar: Histogramas, Boxplots, Q–Q plots.
   **Cuidado:** Transformar datos puede complicar la interpretación original de las variables (unidades, escala).

────────────────────────────────────────────────────────────────

                      ┌────────────────────────┐
                      │       Normalidad        │
                      └───┬────────────────────┘
                          │
                          v
    Pruebas: Shapiro-Wilk, Kolmogorov-Smirnov
    - p-valor alto → no se rechaza normalidad (no es garantía de ser normal perfecta).
    - p-valor bajo → datos se alejan de la normal.

    **Cuidado:** Pruebas sensibles al tamaño de muestra. Con muestras grandes, pequeñas desviaciones se detectan fácilmente.

    Si no normal:
    - Medidas robustas
    - Correlaciones no paramétricas (Spearman/Kendall)

────────────────────────────────────────────────────────────────

   ┌─────────────────────┐
   │   Correlaciones      │
   └───────┬─────────────┘
           │
           v
   Coeficientes de Correlación:
   - Pearson: mide relación lineal.
     Rango: -1 a 1
     Valores cercanos a ±1 → fuerte correlación lineal
     0 → sin relación lineal
     **Cuidado:** Sensible a outliers; un solo valor extremo puede distorsionar la correlación.

   - Spearman: basado en rangos, capta relaciones monotónicas.
     También de -1 a 1.
     Menos sensible a outliers que Pearson.
     **Cuidado:** No diferencia entre lineal y no lineal, sólo monotonicidad.

   - Kendall: similar a Spearman, pero más robusto frente a empates y a muestras pequeñas.
     Rango: -1 a 1.

   **Interpretación:**
   - Correlación alta no implica causalidad.
   - Dato con outliers puede inflar o reducir la correlación.
   - Considerar el contexto: ¿tiene sentido la relación?

────────────────────────────────────────────────────────────────

   ┌─────────────────────────────────────────┐
   │    Posición (Cuartiles, Percentiles)     │
   └─────────────────┬──────────────────────┘
                     │
                     v
   - Cuartiles (Q1, Q2=Mediana, Q3):
     IQR = Q3 - Q1
     IQR alto → datos dispersos en el rango medio.
     IQR bajo → datos más concentrados.
   - Percentiles: ubican puntos específicos (p.ej. P90).
   
   **Cuidado:** Un percentile aislado no da el panorama completo. Combinarlos con dispersión y asimetría para entender la distribución.

────────────────────────────────────────────────────────────────

   ┌────────────────────────────────────┐
   │      Visualización y Herramientas   │
   └─────────────────┬─────────────────┘
                     │
                     v
   Visualizaciones:
   - Histogramas: forma general, asimetría, modas.
   - Boxplots: outliers, IQR, mediana.
   - Q–Q plots: desviaciones respecto a la normal.
   - Matrices de correlación y Heatmaps: relaciones entre variables.

   Herramientas de Software:
   - Python: pandas, numpy, scipy, matplotlib, seaborn
   - R: dplyr, ggplot2, stats
   **Cuidado:** Escalas de ejes, bins en histogramas, y elección apropiada del gráfico influyen en la interpretación.

────────────────────────────────────────────────────────────────

   ┌──────────────────────────────────────────┐
   │       Contexto, Interpretación y Ciclo    │
   └─────────────────┬────────────────────────┘
                     │
                     v
   Considerar el Dominio:
   - Un outlier en datos financieros puede ser un valor real (un millonario), mientras que en datos biomédicos podría ser error de medición.
   - Skewness leve en un dataset pequeño puede no ser importante, en dataset masivo sí.

   Ciclo Iterativo:
   1. Preparar datos (limpieza, tratamiento de faltantes).
   2. Analizar distribución, tendencia central, dispersión, asimetría, normalidad.
   3. Seleccionar métricas (Media/Mediana, Varianza/IQR) según contexto.
   4. Ver correlaciones, elegir Pearson/Spearman/Kendall según tipo de relación y robustez necesaria.
   5. Visualizar para validar hallazgos.
   6. Ajustar (transformaciones, remover o imputar outliers) y repetir.

   **Cuidado:** 
   - Interpretar siempre con conocimiento del dominio.
   - Métricas no son absolutos, sino guías.  
   - Valorar las consecuencias de modificar los datos (transformaciones, filtrados).

