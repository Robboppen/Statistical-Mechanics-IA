# Máquinas de Boltzmann: El Puente entre Física e Inteligencia Artificial

> **Contexto:** Mecánica Estadística — Instituto de Física y Astronomía, Universidad de Valparaíso  
> **Foco:** Distribución de Boltzmann · Pesos probabilísticos · Función de partición · Ensembles como lenguaje de inferencia
.
---

## Índice

1. [La Distribución de Boltzmann](#1-la-distribución-de-boltzmann)
2. [Pesos Probabilísticos y Modelos Basados en Energía](#2-pesos-probabilísticos-y-modelos-basados-en-energía)
3. [La Función de Partición](#3-la-función-de-partición)
4. [Ensembles como Lenguaje de Inferencia](#4-ensembles-como-lenguaje-de-inferencia)
5. [La Máquina de Boltzmann](#5-la-máquina-de-boltzmann)
6. [Mapa Conceptual Unificado](#6-mapa-conceptual-unificado)
7. [Referencias](#7-referencias)

---

## 1. La Distribución de Boltzmann

### 1.1 Origen físico

Considera un sistema en contacto con un reservorio térmico a temperatura $T$. La probabilidad de que el sistema se encuentre en el microestado $s$ con energía $E(s)$ es:

$$\boxed{P(s) = \frac{1}{Z}\, e^{-\beta E(s)}, \qquad \beta = \frac{1}{k_B T}}$$

Esta distribución se **deriva** — no se postula — del principio de máxima entropía (Jaynes, 1957): es la distribución de probabilidad **menos informativa** consistente con el valor esperado de la energía $\langle E \rangle = U$.

### 1.2 Derivación por máxima entropía

Maximizar la entropía de Shannon $S = -\sum_s P(s)\ln P(s)$ sujeto a:

$$\sum_s P(s) = 1, \qquad \sum_s P(s)\,E(s) = \langle E \rangle$$

introduce multiplicadores de Lagrange $(\lambda_0,\, \beta)$ y produce:

$$P(s) = e^{-(1+\lambda_0)}\, e^{-\beta E(s)}$$

Identificando $e^{1+\lambda_0} = Z$ se recupera la distribución de Boltzmann. La temperatura inversa $\beta$ **es el multiplicador de Lagrange de la restricción energética** — no un parámetro físico externo.

### 1.3 Propiedades clave

| Límite | Comportamiento |
|---|---|
| $T \to 0$ | $P(s)$ se concentra en el estado fundamental (mínima energía) |
| $T \to \infty$ | $P(s)$ converge a distribución uniforme |
| $T$ intermedia | Balance entre energía y entropía |

La función softmax en redes neuronales es una distribución de Boltzmann discreta:

$$P(y = k \mid \mathbf{x}) = \frac{e^{f_k(\mathbf{x})/T}}{\sum_{k'} e^{f_{k'}(\mathbf{x})/T}}$$

---

## 2. Pesos Probabilísticos y Modelos Basados en Energía

### 2.1 Energy-Based Models (EBMs)

Los modelos basados en energía (LeCun et al., 2006) generalizan la distribución de Boltzmann al aprendizaje automático: se asocia una energía escalar $E_\theta(\mathbf{x})$ a cada configuración $\mathbf{x}$, parametrizada por $\theta$:

$$p_\theta(\mathbf{x}) = \frac{e^{-E_\theta(\mathbf{x})}}{Z(\theta)}, \qquad Z(\theta) = \int e^{-E_\theta(\mathbf{x})}\, d\mathbf{x}$$

**Inferencia:** encontrar configuraciones de mínima energía.  
**Aprendizaje:** ajustar $\theta$ para que las configuraciones observadas tengan menor energía que las no observadas.

### 2.2 La función de energía de la Máquina de Boltzmann

La Máquina de Boltzmann (Ackley, Hinton & Sejnowski, 1985) define:

$$E(\mathbf{s}) = -\sum_{i < j} w_{ij}\, s_i s_j \;-\; \sum_i b_i\, s_i$$

donde $s_i \in \{0,1\}$ son unidades binarias estocásticas. La analogía con el **modelo de Ising** es directa:

| Modelo de Ising | Máquina de Boltzmann |
|---|---|
| Constante de acoplamiento $J_{ij}$ | Peso aprendible $w_{ij}$ |
| Campo externo $h_i$ | Bias $b_i$ |
| Spin $\sigma_i \in \{-1,+1\}$ | Unidad $s_i \in \{0,1\}$ |
| Temperatura $T$ fija | $\beta$ absorbido en $w_{ij}$ |

Los **pesos $w_{ij}$ son constantes de acoplamiento ajustadas por gradiente**: la red "aprende" el Hamiltoniano de Ising que mejor describe los datos.

### 2.3 Interpretación probabilística de los pesos

La probabilidad de activación de la unidad $k$ dado el estado del resto es:

$$P(s_k = 1 \mid \mathbf{s}_{\backslash k}) = \sigma\!\left(\sum_j w_{kj}\, s_j + b_k\right), \qquad \sigma(x) = \frac{1}{1+e^{-x}}$$

Cada peso $w_{kj}$ cuantifica la **correlación probabilística** entre las unidades $k$ y $j$:
- $w_{kj} > 0$: activaciones correlacionadas (ferromagnético)
- $w_{kj} < 0$: activaciones anticorrelacionadas (antiferromagnético)
- $w_{kj} = 0$: independencia condicional

---

## 3. La Función de Partición

### 3.1 Definición y rol normalizador

$$Z = \sum_{\mathbf{s}} e^{-E(\mathbf{s})}$$

$Z$ aparece como **normalizador universal** en tres disciplinas:

| Disciplina | Rol de $Z$ |
|---|---|
| Física estadística | Normaliza $P(\mathbf{s})$, genera toda la termodinámica |
| Estadística bayesiana | Normaliza la distribución posterior $P(\theta \mid \text{datos})$ |
| Machine learning | Normaliza la distribución del modelo $p_\theta(\mathbf{x})$ |

### 3.2 Termodinámica contenida en $Z$

Toda la información termodinámica del sistema se obtiene derivando $\ln Z$:

$$F = -k_B T \ln Z \qquad \text{(Energía libre de Helmholtz)}$$

$$\langle E \rangle = -\frac{\partial \ln Z}{\partial \beta}, \qquad S = k_B\left(\ln Z + \beta\langle E\rangle\right), \qquad C_v = k_B \beta^2 \frac{\partial^2 \ln Z}{\partial \beta^2}$$

En ML: $-\ln Z(\theta)$ aparece directamente en la **log-verosimilitud negativa** (función de pérdida):

$$\ln p_\theta(\mathbf{x}) = -E_\theta(\mathbf{x}) - \ln Z(\theta)$$

### 3.3 El problema de la intratabilidad

Para $N$ unidades binarias, $Z$ es una suma de $2^N$ términos:

$$Z = \sum_{\mathbf{s} \in \{0,1\}^N} e^{-E(\mathbf{s})}$$

Para $N = 100$: $2^{100} \approx 10^{30}$ términos. **$Z$ es generalmente intratable** — este es el problema central compartido entre física computacional y ML generativo.

### 3.4 Estrategias de aproximación

| Método | Idea central | Contexto |
|---|---|---|
| **Contrastive Divergence (CD-$k$)** | $k$ pasos de Gibbs, evita calcular $Z$ explícitamente | ML — Hinton (2002) |
| **Persistent CD (PCD)** | Cadenas de Markov persistentes para mejor mezcla | ML — Tieleman (2008) |
| **Annealed Importance Sampling (AIS)** | Puente térmico entre distribución trivial y el modelo | Física & ML — Neal (2001) |
| **Campo medio (TAP)** | Aproximación de Bethe/Plefka-Georges-Yedidia | Física estadística |
| **ELBO variacional** | Cota inferior de $\ln p(\mathbf{x})$, minimiza $F$ variacional | VAEs — Kingma & Welling (2013) |

---

## 4. Ensembles como Lenguaje de Inferencia

### 4.1 La equivalencia fundamental (Jaynes, 1957)

El resultado profundo de Jaynes es que la mecánica estadística de equilibrio **es** inferencia bayesiana óptima bajo restricciones. El ensamble canónico surge de maximizar la entropía sujeto a conocer $\langle E \rangle$.

### 4.2 Diccionario completo

| Mecánica Estadística | Inferencia Bayesiana / ML |
|---|---|
| Ensamble canónico ($T$ fija) | Distribución a posteriori $P(\theta \mid \text{datos})$ |
| Energía $E(s)$ | Log-verosimilitud negativa $-\ln P(\text{datos} \mid \theta)$ |
| Temperatura $T = 1/\beta$ | Parámetro de regularización / temperatura softmax |
| Función de partición $Z$ | Evidencia marginal $P(\text{datos})$ |
| Energía libre $F = -kT\ln Z$ | Función de pérdida / $-$ELBO |
| Promedio térmico $\langle O \rangle$ | Valor esperado $\mathbb{E}[f(\mathbf{x})]$ |
| Fluctuaciones $\langle(\Delta E)^2\rangle = k_BT^2 C_v$ | Varianza del estimador |
| Calor específico $C_v = \partial\langle E\rangle/\partial T$ | Capacidad expresiva del modelo |
| Recocido simulado | *Learning rate annealing* / optimización global |
| Ruido térmico $\sim k_BT$ | Dropout / regularización estocástica |
| Transición de fase en $T_c$ | Cambio de régimen en el aprendizaje |

### 4.3 Energía libre variacional = ELBO

La conexión más profunda entre física e IA moderna: la **energía libre de Helmholtz variacional**

$$F[q] = \langle E \rangle_q - T\,S[q] = \langle E \rangle_q + k_BT\sum_s q(s)\ln q(s)$$

reaparece exactamente como el **Evidence Lower Bound (ELBO)** de los Autoencoders Variacionales (VAEs):

$$\ln P(\mathbf{x}) \geq \underbrace{\mathbb{E}_{q_\phi(\mathbf{z}|\mathbf{x})}[\ln P_\theta(\mathbf{x}|\mathbf{z})]}_{\text{energía media negativa}} \underbrace{-\, D_{\text{KL}}\!\left(q_\phi(\mathbf{z}|\mathbf{x}) \| P(\mathbf{z})\right)}_{\text{entropía del modelo}}$$

Minimizar $F$ variacional **≡** maximizar el ELBO. La inferencia variacional moderna **es** termodinámica.

### 4.4 La temperatura como hiperparámetro universal

$$T \to 0: \quad \text{softmax} \to \arg\max \quad \text{(decisión determinista)}$$
$$T \to \infty: \quad \text{softmax} \to \text{uniforme} \quad \text{(máxima incertidumbre)}$$

La temperatura controla el balance **exploración/explotación** en RL, la **nitidez de generación** en LLMs, y el **régimen de aprendizaje** en redes profundas.

---

## 5. La Máquina de Boltzmann

### 5.1 Arquitectura general

Red de $N$ unidades binarias $s_i \in \{0,1\}$ con conexiones simétricas $w_{ij} = w_{ji}$. Las unidades se dividen en:

- **Visibles** $\mathbf{v}$: observables, representan los datos
- **Ocultas** $\mathbf{h}$: latentes, aprenden representaciones internas

La distribución de equilibrio es exactamente la distribución de Boltzmann:

$$P(\mathbf{v}, \mathbf{h}) = \frac{e^{-E(\mathbf{v},\mathbf{h})}}{Z}$$

### 5.2 Máquina de Boltzmann Restringida (RBM)

La **restricción** (Smolensky, 1986): eliminar conexiones dentro de cada capa ($w_{ij}^{vv} = 0$, $w_{ij}^{hh} = 0$). La función de energía se simplifica:

$$E(\mathbf{v}, \mathbf{h}) = -\mathbf{v}^T W \mathbf{h} - \mathbf{a}^T\mathbf{v} - \mathbf{b}^T\mathbf{h}$$

**La restricción hace factorizable la inferencia:**

$$P(\mathbf{h} \mid \mathbf{v}) = \prod_j P(h_j \mid \mathbf{v}), \qquad P(\mathbf{v} \mid \mathbf{h}) = \prod_i P(v_i \mid \mathbf{h})$$

con activaciones sigmoideas individuales:

$$P(h_j = 1 \mid \mathbf{v}) = \sigma\!\left(b_j + \sum_i v_i W_{ij}\right)$$

### 5.3 Entrenamiento: Divergencia Contrastiva (CD-$k$)

El gradiente de la log-verosimilitud:

$$\frac{\partial \ln P(\mathbf{v})}{\partial W_{ij}} = \underbrace{\langle v_i h_j \rangle_{\text{datos}}}_{\text{fase positiva}} - \underbrace{\langle v_i h_j \rangle_{\text{modelo}}}_{\text{fase negativa}}$$

| | Fase positiva ("wake") | Fase negativa ("sleep") |
|---|---|---|
| **Proceso** | Sistema en contacto con los datos | Sistema en equilibrio interno |
| **Cálculo** | $\langle v_i h_j \rangle^{(0)}$: fijar $\mathbf{v}$, muestrear $\mathbf{h}$ | $\langle v_i h_j \rangle^{(k)}$: $k$ pasos de Gibbs |
| **Interpretación** | Correlaciones en los datos reales | Correlaciones del modelo generativo |

Regla de actualización **CD-$k$**:

$$\Delta W_{ij} = \eta\left(\langle v_i h_j \rangle^{(0)} - \langle v_i h_j \rangle^{(k)}\right)$$

---

## 6. Mapa Conceptual Unificado

```
FÍSICA ESTADÍSTICA                    MACHINE LEARNING
══════════════════                    ════════════════
                                      
P(s) = e^{-βE(s)} / Z     ←────→    p_θ(x) = e^{-E_θ(x)} / Z(θ)
         ↑                                      ↑
  distribución de                       modelo generativo
  Boltzmann (1877)                       aprendido de datos

Z = Σ_s e^{-βE(s)}        ←────→    Z(θ) = ∫ e^{-E_θ(x)} dx
    intratable                          intratable
    ↓ AIS, MCMC                         ↓ CD-k, MCMC, VAE

F = -kT ln Z               ←────→    Pérdida = -ln p_θ(x)
  energía libre                         = E_θ(x) + ln Z(θ)
  se minimiza en equilibrio             se minimiza en entrenamiento

Ensamble canónico          ←────→    Distribución a posteriori
  (Jaynes 1957)                        P(θ | datos)

Temperatura T = 1/β        ←────→    Temperatura softmax
  controla fluctuaciones               controla exploración/explotación

Pesos J_{ij} (Ising)       ←────→    Pesos W_{ij} aprendibles
  interacciones físicas                correlaciones en los datos

Recocido simulado          ←────→    Learning rate annealing
Ruido térmico ~kT          ←────→    Dropout / regularización
Transición de fase T_c     ←────→    Cambio de régimen
⟨ΔE²⟩ = kT²C_v            ←────→    Varianza del estimador
```

---

## 7. Referencias

### Fundamentos físicos e inferencia

1. **Jaynes, E.T.** (1957). *Information Theory and Statistical Mechanics*. Physical Review, **106**, 620–630. `DOI: 10.1103/PhysRev.106.620`

2. **Jaynes, E.T.** (1957). *Information Theory and Statistical Mechanics II*. Physical Review, **108**, 171–190. `DOI: 10.1103/PhysRev.108.171`

### Máquinas de Boltzmann

3. **Ackley, D.H., Hinton, G.E. & Sejnowski, T.J.** (1985). *A Learning Algorithm for Boltzmann Machines*. Cognitive Science, **9**(1), 147–169. `DOI: 10.1207/s15516709cog0901_7`

4. **Smolensky, P.** (1986). *Information Processing in Dynamical Systems: Foundations of Harmony Theory*. En: Parallel Distributed Processing, Vol. 1. MIT Press, pp. 194–281.

5. **Hinton, G.E.** (2002). *Training Products of Experts by Minimizing Contrastive Divergence*. Neural Computation, **14**(8), 1771–1800. `DOI: 10.1162/089976602760128018`

6. **Hinton, G.E., Osindero, S. & Teh, Y.W.** (2006). *A Fast Learning Algorithm for Deep Belief Nets*. Neural Computation, **18**(7), 1527–1554. `DOI: 10.1162/neco.2006.18.7.1527`

7. **Hinton, G.E. & Salakhutdinov, R.R.** (2006). *Reducing the Dimensionality of Data with Neural Networks*. Science, **313**(5786), 504–507. `DOI: 10.1126/science.1127647`

### Modelos basados en energía y función de partición

8. **LeCun, Y., Chopra, S., Hadsell, R., Ranzato, M. & Huang, F.** (2006). *A Tutorial on Energy-Based Learning*. En: Predicting Structured Data. MIT Press. [`PDF`](http://yann.lecun.com/exdb/publis/pdf/lecun-06.pdf)

9. **Mazzanti, F. & Romero, E.** (2020). *Efficient Evaluation of the Partition Function of RBMs with Annealed Importance Sampling*. arXiv: 2007.11926.

10. **Dawid, A. & LeCun, Y.** (2024). *Introduction to Latent Variable Energy-Based Models: a Path Toward Autonomous Machine Intelligence*. Journal of Statistical Mechanics. `DOI: 10.1088/1742-5468/ad292b`

### Ensembles como inferencia y conexiones modernas

11. **Puškarov, T. & Cortés Cubero, A.** (2018). *Machine Learning Algorithms Based on Generalized Gibbs Ensembles*. arXiv: 1804.03546.

12. **Carleo, G. & Troyer, M.** (2017). *Solving the Quantum Many-Body Problem with Artificial Neural Networks*. Science, **355**(6325), 602–606. `DOI: 10.1126/science.aag2302`

13. **Kingma, D.P. & Welling, M.** (2013). *Auto-Encoding Variational Bayes*. arXiv: 1312.6114.

---

*Preparado para el repositorio del curso de Mecánica Estadística — IFA, UV.*
