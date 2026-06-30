# Plan de presentación: Máquinas de Boltzmann y el puente entre física e inteligencia artificial

Duración estricta: **10 minutos**  
Integrantes: **2 personas**  
Objetivo: explicar de forma conceptual cómo la mecánica estadística aparece en modelos probabilísticos de aprendizaje automático, usando como eje las Máquinas de Boltzmann.

## Idea central

La charla no debe intentar cubrir todos los detalles técnicos de los 11 papers. La narrativa debe ser:

> Una Máquina de Boltzmann toma la idea física de que los estados de baja energía son más probables, la convierte en un modelo probabilístico y usa herramientas de mecánica estadística —distribución de Boltzmann, función de partición, ensembles, correlaciones y muestreo— para aprender patrones en datos.

## Reparto general

| Bloque | Tiempo | Expositor | Función |
|---|---:|---|---|
| 1. Motivación: energía y probabilidad | 1:00 | Persona 1 | Abrir con intuición física |
| 2. Distribución de Boltzmann y máxima entropía | 2:00 | Persona 1 | Conectar con Jaynes y el curso |
| 3. Máquina de Boltzmann: energía, pesos y aprendizaje | 2:00 | Persona 1 | Presentar el modelo central |
| 4. Función de partición y problema computacional | 2:00 | Persona 2 | Explicar por qué aparece el problema de $Z$ |
| 5. Métodos modernos y extensiones | 2:00 | Persona 2 | AIS, EBM, variables latentes, RG |
| 6. Cierre: diccionario física ↔ IA | 1:00 | Ambos | Resumir la conexión explícita |

Cada persona habla aproximadamente **5 minutos**.

## Diapositivas recomendadas

Usar **6 diapositivas máximo**. Las diapositivas deben mostrar ecuaciones, esquemas y palabras clave, no texto para leer.

### Diapositiva 1 — Pregunta de la charla

**Título:** ¿Cómo aprende una máquina usando ideas de la física estadística?

**Contenido visual:**

- Paisaje de energía: valles = estados probables, montañas = estados improbables
- Frase breve: “baja energía ↔ alta probabilidad”

**Guion Persona 1, 1:00:**

“La idea de partida es muy física: un sistema tiende a ocupar estados de baja energía, pero la temperatura permite fluctuaciones. Las Máquinas de Boltzmann trasladan esa idea a datos: una imagen, un patrón o una configuración recibe una energía. Si se parece a los datos reales, el modelo aprende a asignarle baja energía.”

**Papers detrás:**

- LeCun et al. (2006): marco general de Energy-Based Models.
- Carbone (2025): revisión moderna del vínculo entre EBM, muestreo y física estadística.

## Diapositiva 2 — De máxima entropía a Boltzmann

**Título:** La distribución de Boltzmann como inferencia

**Ecuación central:**

$$P(s)=\frac{e^{-\beta E(s)}}{Z}, \qquad Z=\sum_s e^{-\beta E(s)}$$

**Ideas clave:**

- Jaynes: maximizar entropía con energía media fija produce Boltzmann.
- $\beta$ aparece como multiplicador de Lagrange asociado a la restricción energética.
- La mecánica estadística puede leerse como inferencia bajo información incompleta.

**Guion Persona 1, 2:00:**

“Esto no es solo una fórmula física: Jaynes muestra que si conocemos solo la energía media y queremos no introducir información extra, la distribución correcta es la de máxima entropía. Esa distribución es precisamente Boltzmann. Por eso la conexión con IA es natural: un modelo probabilístico también intenta asignar probabilidades con información incompleta.”

**Conexión explícita con el curso:**

- Ensamble canónico.
- Entropía de Shannon/Gibbs.
- Función de partición como normalizador.

**Papers detrás:**

- Jaynes (1957a): base conceptual central.
- Jaynes (1957b): extensión a matriz de densidad y lectura predictiva de la mecánica estadística.

## Diapositiva 3 — Máquina de Boltzmann: un Ising que aprende

**Título:** Pesos como acoplamientos aprendibles

**Ecuaciones centrales:**

$$E(\mathbf{s})=-\sum_{i<j} w_{ij}s_i s_j-\sum_i b_i s_i$$

$$\Delta w_{ij}=\eta\left(\langle s_i s_j\rangle_{datos}-\langle s_i s_j\rangle_{modelo}\right)$$

**Ideas clave:**

- $s_i$ son unidades binarias, análogas a espines.
- $w_{ij}$ juega el papel de acoplamiento tipo Ising.
- Aprender significa ajustar los acoplamientos para que las correlaciones del modelo se parezcan a las de los datos.

**Guion Persona 1, 2:00:**

“La Máquina de Boltzmann es prácticamente un modelo de Ising con parámetros ajustables. Los pesos $w_{ij}$ no son solo números de una red neuronal: funcionan como constantes de acoplamiento. El aprendizaje compara dos correlaciones: las que aparecen cuando fijamos los datos y las que genera el modelo en equilibrio. Si difieren, se corrigen los pesos.”

**Conexión explícita con el curso:**

- Modelo de Ising.
- Correlaciones térmicas.
- Equilibrio estadístico.

**Papers detrás:**

- Ackley, Hinton & Sejnowski (1985): paper fundacional de las Máquinas de Boltzmann.
- Hohm (2026): puente pedagógico entre Ising, RBM y redes neuronales.

## Diapositiva 4 — El problema de la función de partición

**Título:** El obstáculo: normalizar cuesta exponencialmente

**Ecuación central:**

$$Z=\sum_{\mathbf{s}\in\{0,1\}^N}e^{-E(\mathbf{s})}$$

**Ideas clave:**

- Para $N$ unidades binarias hay $2^N$ configuraciones.
- $Z$ es necesaria para probabilidades exactas.
- En la práctica, se evita o se estima mediante muestreo.

**Guion Persona 2, 2:00:**

“Aquí aparece el problema computacional central. Para normalizar la distribución hay que sumar sobre todas las configuraciones posibles. Eso es manejable para pocos espines, pero crece como $2^N$. Este mismo problema aparece en física cuando calculamos cantidades termodinámicas y en machine learning cuando queremos entrenar modelos generativos.”

**Conexión explícita con el curso:**

- $Z$ genera magnitudes termodinámicas.
- $F=-k_BT\ln Z$.
- La dificultad de calcular $Z$ motiva aproximaciones estadísticas.

**Papers detrás:**

- Mazzanti & Romero (2020): estimación eficiente de $Z$ en RBM con AIS.
- Merhav (2026): muestreo de importancia inversa agrupado para estimar $Z$.

## Diapositiva 5 — Cómo se evita calcular todo

**Título:** Muestreo, energía libre y modelos modernos

**Contenido visual:** tabla breve

| Idea física | Uso en IA |
|---|---|
| Muestreo térmico | Gibbs sampling / MCMC |
| Recocido | Annealed Importance Sampling |
| Energía libre | Variables latentes / ELBO |
| Integrar grados de libertad | Neuronas ocultas / RG |

**Guion Persona 2, 2:00:**

“La solución no es enumerar todos los estados, sino muestrear los más relevantes. Esto conecta directamente con métodos como Gibbs sampling, Contrastive Divergence y Annealed Importance Sampling. Además, en modelos modernos con variables latentes, la idea de marginalizar variables ocultas es análoga a integrar grados de libertad, como en física estadística y grupo de renormalización.”

**Papers detrás:**

- LeCun et al. (2006): EBM como marco general.
- Dawid & LeCun (2023): EBM con variables latentes y energía libre.
- Carbone (2025): conexión con MCMC, Langevin y modelos generativos modernos.
- Hohm (2026): analogía entre integrar neuronas ocultas y grupo de renormalización.

## Diapositiva 6 — Mapa conceptual final

**Título:** Diccionario física estadística ↔ inteligencia artificial

| Mecánica estadística | Machine learning |
|---|---|
| Energía $E(s)$ | Costo o incompatibilidad de un dato |
| Distribución de Boltzmann | Modelo probabilístico sobre configuraciones |
| Temperatura $T$ | Control de exploración / suavidad |
| Función de partición $Z$ | Normalización / evidencia |
| Acoplamientos $J_{ij}$ | Pesos aprendibles $w_{ij}$ |
| Correlaciones térmicas | Estadísticas aprendidas de los datos |
| Energía libre | Objetivos variacionales / variables latentes |
| Ensemble | Inferencia bajo incertidumbre |

**Guion ambos, 1:00:**

Persona 1: “La conclusión es que la Máquina de Boltzmann no solo toma inspiración estética de la física: usa directamente la distribución de Boltzmann, la función de partición y las correlaciones de equilibrio.”

Persona 2: “Y desde el lado de IA, eso permite construir modelos que aprenden distribuciones de datos. La dificultad central —calcular $Z$— es la misma que en física estadística, por eso aparecen métodos de muestreo, energía libre y aproximaciones.”

**Frase final sugerida:**

“Los modelos probabilísticos modernos no inventaron una nueva forma de tratar la incertidumbre: heredaron de la mecánica estadística la idea de describir lo probable mediante energía, entropía y ensembles.”

## Uso de todos los papers en la charla

No conviene explicar los 11 papers uno por uno. La forma correcta de usarlos es como base bibliográfica de cada idea:

| Paper | Rol en la presentación | Prioridad oral |
|---|---|---|
| Jaynes (1957a) | Justifica Boltzmann desde máxima entropía | Alta |
| Jaynes (1957b) | Refuerza la lectura predictiva/inferencial | Mención breve |
| Ackley, Hinton & Sejnowski (1985) | Introduce la Máquina de Boltzmann y la regla de aprendizaje | Alta |
| LeCun et al. (2006) | Generaliza a Energy-Based Models | Alta |
| Cheng, Chen & Wang (2018) | Comparación con Born Machines y teoría de información | Solo respaldo si preguntan |
| Puškarov & Cortés Cubero (2018) | Generalized Gibbs Ensembles como extensión avanzada | Mención opcional |
| Mazzanti & Romero (2020) | AIS para estimar $Z$ en RBM | Alta |
| Dawid & LeCun (2023) | EBMs con variables latentes y energía libre moderna | Alta |
| Carbone (2025) | Revisión moderna: EBM, MCMC, Langevin, física no equilibrio | Mención breve |
| Hohm (2026) | Puente pedagógico con Ising, RG y redes neuronales | Alta |
| Merhav (2026) | Método reciente para estimar función de partición | Cierre o respaldo |

## Qué NO incluir por tiempo

- No explicar Born Machines en detalle.
- No desarrollar matriz de densidad ni formalismo cuántico.
- No entrar en JEPA salvo una frase como ejemplo moderno.
- No derivar matemáticamente Contrastive Divergence.
- No listar todos los métodos de estimación de $Z$; basta decir AIS/MCMC como ejemplos.

## Cronómetro recomendado

| Tiempo | Acción |
|---:|---|
| 0:00-1:00 | Motivación: energía baja = alta probabilidad |
| 1:00-3:00 | Jaynes, máxima entropía y Boltzmann |
| 3:00-5:00 | Máquina de Boltzmann como Ising que aprende |
| 5:00-7:00 | Función de partición e intratabilidad |
| 7:00-9:00 | Muestreo, energía libre y modelos modernos |
| 9:00-10:00 | Diccionario final y cierre |

## Preguntas probables del profesor

**¿Dónde aparece explícitamente la mecánica estadística?**  
En la distribución de Boltzmann, la función de partición, las correlaciones de equilibrio, el modelo de Ising, la energía libre y el uso de ensembles.

**¿Qué aprende realmente la Máquina de Boltzmann?**  
Aprende los pesos/acoplamientos $w_{ij}$ para que las correlaciones generadas por el modelo se parezcan a las correlaciones observadas en los datos.

**¿Por qué es difícil entrenarla?**  
Porque calcular la función de partición requiere sumar sobre un número exponencial de configuraciones.

**¿Cuál es la conexión con IA moderna?**  
Los Energy-Based Models, variables latentes, métodos de muestreo y objetivos variacionales usan la misma estructura conceptual: energía, probabilidad, normalización y aproximación.

## Recomendación final

La charla debe sonar como una explicación conceptual, no como revisión bibliográfica. Los papers deben aparecer como soporte de autoridad, pero la línea narrativa debe ser simple:

1. La física asigna probabilidades a partir de energía.
2. Las Máquinas de Boltzmann usan esa idea para modelar datos.
3. Los pesos son acoplamientos aprendibles.
4. La función de partición es el gran problema computacional.
5. La IA moderna reutiliza métodos de mecánica estadística para aproximar ese problema.
