# Materiales para la presentación

Esta carpeta contiene código y figuras para armar la presentación de 10 minutos sobre **Máquinas de Boltzmann y el puente entre física e inteligencia artificial**.

## Estructura

- `generar_figuras.py`: script que genera todos los ploteos.
- `requirements.txt`: dependencias mínimas.
- `ploteos/`: carpeta de salida con las figuras en `.png` y `.svg`.

## Cómo generar las figuras

Desde la raíz del repositorio:

```powershell
python .\presentacion_materiales\generar_figuras.py
```

Si falta alguna dependencia:

```powershell
pip install -r .\presentacion_materiales\requirements.txt
```

## Figuras sugeridas por diapositiva

| Diapositiva | Figura | Uso |
|---|---|---|
| 1. Motivación | `01_paisaje_energia.*` | Explicar que baja energía implica alta probabilidad. |
| 2. Boltzmann | `02_boltzmann_temperatura.*` | Mostrar cómo la temperatura cambia la concentración de probabilidad. |
| 3. Máquina de Boltzmann | `03_rbm_arquitectura.*` | Mostrar visibles, ocultas y pesos como acoplamientos. |
| 4. Función de partición | `04_crecimiento_configuraciones.*` | Mostrar por qué sumar todas las configuraciones es intratable. |
| 5. Aprendizaje | `05_regla_aprendizaje.*` | Mostrar fase positiva menos fase negativa. |
| 6. Cierre | `06_diccionario_fisica_ia.*` | Resumir el puente conceptual física ↔ IA. |

## Recomendación

Usar las figuras como apoyo visual, no como texto para leer. La charla debe mantener una línea simple: energía → probabilidad → pesos como acoplamientos → función de partición → aproximaciones por muestreo.
