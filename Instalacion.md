
# Proyecto Databricks: Configuración de Entorno e Instalación de Requisitos

## Pasos para la instalación

### 1. Crear un entorno virtual
Primero, asegúrate de tener Python instalado en tu máquina (se recomienda Python 3.10). Luego, crea un entorno virtual para aislar las dependencias del proyecto:

```bash
python3 -m venv .env
```

Activa el entorno virtual:

- En Linux/Mac:
  ```bash
  source .env/bin/activate
  ```

- En Windows:
  ```bash
  .env\Scripts\activate
  ```

---

### 2. Instalación de `requirements.txt` mediante script

```bash
python3 install_requirements.py
```

Pasos que se realizan en el script:

- Actualizar herramientas básicas

    Se comprueba antes de instalar los requisitos, tener las últimas versiones de `pip`, `setuptools` y `wheel`.

- Instalar los requisitos
Instala las dependencias necesarias para el proyecto desde el archivo `requirements.txt`.


    **Si ocurre algún error durante la instalación, revisa los mensajes en la terminal y ajusta según sea necesario (consulta la documentación para soluciones comunes).**

    **Se listarán los paquetes que no se pudieron instalar al final del proceso, deberías revisarlos y solucionarlos.**

---

`Nota`: Pyspark necesita Java instalado en tu máquina.
```bash
# Linux
sudo apt update
sudo apt install openjdk-11-jdk
```

---

### 3. Verificar la instalación

Ejecuta los scripts de verificación de instalación:

```bash
python3 test_pyspark.py
```

```bash
# Salida:
...
...
Versión de Spark: 3.5.3
+---+-----+
| id| name|
+---+-----+
|  1|Alice|
|  2|  Bob|
|  3|Cathy|
+---+-----+
``` 

---

```bash
python3 test_delta_spark.py
```

```bash	
    ...
    ...
        confs: [default]
        found io.delta#delta-spark_2.12;3.2.1 in central
        found io.delta#delta-storage;3.2.1 in central
        found org.antlr#antlr4-runtime;4.9.3 in central
:: resolution report :: resolve 97ms :: artifacts dl 3ms
        :: modules in use:
        io.delta#delta-spark_2.12;3.2.1 from central in [default]
        io.delta#delta-storage;3.2.1 from central in [default]
        org.antlr#antlr4-runtime;4.9.3 from central in [default]
        ---------------------------------------------------------------------
        |                  |            modules            ||   artifacts   |
        |       conf       | number| search|dwnlded|evicted|| number|dwnlded|
        ---------------------------------------------------------------------
        |      default     |   3   |   0   |   0   |   0   ||   3   |   0   |
        ---------------------------------------------------------------------
:: retrieving :: org.apache.spark#spark-submit-parent-bd65a8a3-a8b5-4b03-84f7-0c6ccd64ef44
        confs: [default]
        0 artifacts copied, 3 already retrieved (0kB/2ms)
24/12/03 17:35:46 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
24/12/03 17:35:51 WARN SparkStringUtils: Truncated the string representation of a plan since it was too large. This behavior can be adjusted by setting 'spark.sql.debug.maxToStringFields'.
+---+-----+                                                                     
| id| name|
+---+-----+
|  1|Alice|
|  3|Cathy|
|  2|  Bob|
+---+-----+
```

Si todo está correcto, deberías ver un mensaje indicando la versión de Spark y los datos de ejemplo en la terminal.


