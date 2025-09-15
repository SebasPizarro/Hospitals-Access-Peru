# Hospitals Access Peru Dashboard

Este proyecto implementa un **dashboard interactivo con Streamlit** para analizar el acceso a hospitales públicos en el Perú, utilizando datos del **MINSA – IPRESS** y los **Centros Poblados (CCPP)**.  

El panel incluye:  
- **Descripción de datos**: resumen de hospitales públicos operativos.  
- **Mapas estáticos**: coropletas departamentales, distritos sin hospitales y distritos con mayor concentración.  
- **Mapas dinámicos**: coropleta nacional interactiva y análisis de proximidad (ejemplo: Lima vs. Loreto).  

---

## Requisitos

- Python 3.9+  
- [Anaconda](https://www.anaconda.com/) o entorno virtual `venv`  
- Paquetes listados en `requirements.txt`  

---

## Ejecución local

1. Clonar este repositorio y entrar al directorio raíz:  
   ```bash
   git clone https://github.com/<tu_usuario>/Hospitals-Access-Peru.git
   cd Hospitals-Access-Peru


Para activar el enviroment virtual:

#### Windows

```
env/Scripts/activate
```

#### Linux/MacOS

```
source env/bin/activate
```

Now you must install the necessary dependencies to run the dashboard:

```
pip install -r requirements.txt
```

This should take a few minutes. Once it is done, you can run the streamlit application:

```
streamlit run src/streamlit_app.py
```

This should start a locally hosted server and automatically open a browser tab with the application




## Filtrado de hospitales por estado de funcionamiento

El dataset original del MINSA – IPRESS incluye todos los establecimientos de salud, sin importar su estado (cerrados, inactivos, en remodelación).

Para el análisis se consideraron únicamente los hospitales operativos, aplicando el siguiente filtro en la columna “Condición”:

hosp_op = hosp[(hosp["Condición"] == "EN FUNCIONAMIENTO")



## Estructura de nuestro proyeccto:
Hospitals-Access-Peru/
│
├── src/                  # Código fuente
│   ├── streamlit_app.py  # Aplicación principal de Streamlit
│   ├── plots.py          # Funciones de visualización
│   └── estimation.py     # Funciones de estimación y cálculos
│
├── output/               # Resultados exportados (mapas, shapefiles, tablas)
├── assets/               # Recursos adicionales
├── requirements.txt      # Dependencias
└── README.md             # Este archivo



## Referencias

MINSA – Registro Nacional de IPRESS

Instituto Nacional de Estadística e Informática (INEI) – Centros Poblados (CCPP)


