# Esqueleto de diapositivas

## 1. ¿Cómo aprende una máquina usando ideas de la física?

Imagen: `ploteos/01_paisaje_energia.png`

Mensaje oral: los estados de baja energía son más probables. En IA, una configuración de datos también puede recibir una energía.

## 2. Distribución de Boltzmann

Imagen: `ploteos/02_boltzmann_temperatura.png`

Ecuación:

$$P(s)=\frac{e^{-\beta E(s)}}{Z}$$

Mensaje oral: Jaynes permite leer esta distribución como máxima entropía bajo restricción de energía media.

## 3. Máquina de Boltzmann / RBM

Imagen: `ploteos/03_rbm_arquitectura.png`

Ecuación:

$$E(v,h)=-v^TWh-a^Tv-b^Th$$

Mensaje oral: los pesos son acoplamientos aprendibles, análogos al modelo de Ising.

## 4. Función de partición

Imagen: `ploteos/04_crecimiento_configuraciones.png`

Ecuación:

$$Z=\sum_s e^{-E(s)}$$

Mensaje oral: calcular `Z` requiere sumar sobre todas las configuraciones; crece como $2^N$.

## 5. Aprendizaje por correlaciones

Imagen: `ploteos/05_regla_aprendizaje.png`

Ecuación:

$$\Delta w_{ij}=\eta\left(\langle v_i h_j\rangle_{datos}-\langle v_i h_j\rangle_{modelo}\right)$$

Mensaje oral: el modelo ajusta pesos para reproducir las correlaciones observadas en los datos.

## 6. Cierre: diccionario física ↔ IA

Imagen: `ploteos/06_diccionario_fisica_ia.png`

Mensaje oral: energía, temperatura, función de partición, correlaciones y ensembles son el puente entre mecánica estadística e inteligencia artificial.
