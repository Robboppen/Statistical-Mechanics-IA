from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch


OUT = Path(__file__).resolve().parent / "ploteos"
OUT.mkdir(parents=True, exist_ok=True)


plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 12,
        "axes.titlesize": 16,
        "axes.labelsize": 13,
        "figure.dpi": 160,
        "savefig.dpi": 220,
        "axes.spines.top": False,
        "axes.spines.right": False,
    }
)


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / f"{name}.png", bbox_inches="tight")
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight")
    plt.close(fig)


def fig_paisaje_energia():
    x = np.linspace(-3.2, 3.2, 600)
    energy = 0.35 * x**4 - 1.8 * x**2 + 0.25 * x + 3.2
    prob = np.exp(-energy)
    prob = prob / prob.max()

    fig, ax1 = plt.subplots(figsize=(9, 5))
    ax1.plot(x, energy, color="#1f4e79", lw=3, label="Energía E(x)")
    ax1.fill_between(x, energy, energy.min() - 0.2, color="#1f4e79", alpha=0.08)
    ax1.set_xlabel("Configuración x")
    ax1.set_ylabel("Energía", color="#1f4e79")
    ax1.tick_params(axis="y", labelcolor="#1f4e79")
    ax1.set_title("Paisaje de energía: los valles son más probables")

    ax2 = ax1.twinx()
    ax2.plot(x, prob, color="#c0392b", lw=2.5, ls="--", label="Probabilidad ∝ exp[-E(x)]")
    ax2.set_ylabel("Probabilidad relativa", color="#c0392b")
    ax2.tick_params(axis="y", labelcolor="#c0392b")
    ax2.spines["top"].set_visible(False)

    minima = x[np.argsort(energy)[:2]]
    for xm in sorted(minima):
        ym = np.interp(xm, x, energy)
        ax1.scatter([xm], [ym], s=90, color="#f1c40f", edgecolor="black", zorder=5)
    ax1.text(-3.05, energy.max() - 0.5, "Baja energía\n→ alta probabilidad", color="#111111")

    lines = ax1.get_lines() + ax2.get_lines()
    ax1.legend(lines, [l.get_label() for l in lines], loc="upper center", frameon=False)
    save(fig, "01_paisaje_energia")


def fig_boltzmann_temperatura():
    states = np.arange(8)
    energies = np.array([0.0, 0.7, 1.1, 1.8, 2.4, 3.0, 3.8, 4.4])
    temperatures = [0.5, 1.0, 2.5]
    colors = ["#1f4e79", "#2ca25f", "#c0392b"]

    fig, ax = plt.subplots(figsize=(9, 5))
    width = 0.24
    for i, (temp, color) in enumerate(zip(temperatures, colors)):
        beta = 1 / temp
        p = np.exp(-beta * energies)
        p /= p.sum()
        ax.bar(states + (i - 1) * width, p, width=width, color=color, alpha=0.85, label=f"T = {temp}")

    ax.set_title("Distribución de Boltzmann para distintas temperaturas")
    ax.set_xlabel("Microestado s")
    ax.set_ylabel("P(s)")
    ax.set_xticks(states)
    ax.legend(frameon=False)
    ax.text(4.6, 0.43, "T baja: se concentra\nen mínima energía", color="#1f4e79")
    ax.text(4.6, 0.34, "T alta: distribución\nmás uniforme", color="#c0392b")
    save(fig, "02_boltzmann_temperatura")


def fig_rbm_arquitectura():
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.set_title("Máquina de Boltzmann Restringida (RBM)", pad=12)

    visibles = [(2, y) for y in [1.2, 2.4, 3.6, 4.8]]
    ocultas = [(7.5, y) for y in [1.5, 3.0, 4.5]]

    for vx, vy in visibles:
        for hx, hy in ocultas:
            ax.plot([vx, hx], [vy, hy], color="#9aa3ad", lw=1.2, alpha=0.9)

    for i, (x, y) in enumerate(visibles, start=1):
        ax.add_patch(Circle((x, y), 0.32, color="#2b6cb0", ec="black", lw=1.0))
        ax.text(x, y, f"v{i}", ha="center", va="center", color="white", weight="bold")

    for j, (x, y) in enumerate(ocultas, start=1):
        ax.add_patch(Circle((x, y), 0.32, color="#c0392b", ec="black", lw=1.0))
        ax.text(x, y, f"h{j}", ha="center", va="center", color="white", weight="bold")

    ax.text(2, 0.35, "Capa visible\n(datos)", ha="center")
    ax.text(7.5, 0.35, "Capa oculta\n(variables latentes)", ha="center")
    ax.text(4.75, 5.35, "$w_{ij}$ = acoplamientos aprendibles", ha="center", fontsize=14)
    ax.text(4.75, 0.95, "Restricción: sin conexiones visible-visible ni oculta-oculta", ha="center", color="#333333")
    save(fig, "03_rbm_arquitectura")


def fig_crecimiento_configuraciones():
    n = np.arange(1, 31)
    configs = 2**n

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(n, configs, color="#1f4e79", lw=3)
    ax.set_yscale("log")
    ax.set_title("La función de partición exige sumar sobre $2^N$ configuraciones")
    ax.set_xlabel("Número de unidades binarias N")
    ax.set_ylabel("Número de configuraciones")
    ax.grid(True, which="both", alpha=0.25)
    for k in [10, 20, 30]:
        ax.scatter([k], [2**k], color="#c0392b", s=70, zorder=5)
        ax.text(k - 1.2, 2**k * 1.8, f"2^{k} ≈ {2**k:.1e}", color="#c0392b")
    ax.text(2, 2**26, "$Z=\\sum_s e^{-E(s)}$\ncrece exponencialmente", fontsize=14)
    save(fig, "04_crecimiento_configuraciones")


def fig_regla_aprendizaje():
    labels = ["⟨v₁h₁⟩", "⟨v₁h₂⟩", "⟨v₂h₁⟩", "⟨v₂h₂⟩", "⟨v₃h₁⟩"]
    data = np.array([0.82, 0.55, 0.64, 0.30, 0.72])
    model = np.array([0.62, 0.48, 0.70, 0.42, 0.50])
    delta = data - model
    x = np.arange(len(labels))

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.axhline(0, color="black", lw=1)
    ax.bar(x - 0.18, data, width=0.36, label="Fase positiva: datos", color="#2b6cb0", alpha=0.85)
    ax.bar(x + 0.18, model, width=0.36, label="Fase negativa: modelo", color="#c0392b", alpha=0.8)
    for xi, d in zip(x, delta):
        ax.annotate(
            "",
            xy=(xi, model[xi] + d),
            xytext=(xi, model[xi]),
            arrowprops=dict(arrowstyle="->", color="#111111", lw=1.4),
        )
    ax.set_title("Aprendizaje: correlaciones de datos menos correlaciones del modelo")
    ax.set_ylabel("Correlación")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 1.0)
    ax.legend(frameon=False, loc="upper right")
    ax.text(0.1, 0.08, "$\\Delta w_{ij}=\\eta(\\langle v_i h_j\\rangle_{datos}-\\langle v_i h_j\\rangle_{modelo})$", fontsize=14)
    save(fig, "05_regla_aprendizaje")


def fig_diccionario_fisica_ia():
    pairs = [
        ("Energía E(s)", "Costo / incompatibilidad"),
        ("Boltzmann", "Modelo probabilístico"),
        ("Temperatura T", "Exploración / suavidad"),
        ("Función Z", "Normalización / evidencia"),
        ("Acoplamientos Jᵢⱼ", "Pesos aprendibles wᵢⱼ"),
        ("Energía libre F", "Objetivo variacional"),
        ("Ensemble", "Inferencia bajo incertidumbre"),
    ]

    fig, ax = plt.subplots(figsize=(10, 5.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 9)
    ax.axis("off")
    ax.set_title("Diccionario conceptual: física estadística ↔ inteligencia artificial", pad=12)

    ax.text(2.2, 8.1, "Mecánica estadística", ha="center", fontsize=15, weight="bold", color="#1f4e79")
    ax.text(7.8, 8.1, "Machine learning", ha="center", fontsize=15, weight="bold", color="#c0392b")

    y0 = 7.2
    for i, (left, right) in enumerate(pairs):
        y = y0 - i * 0.9
        ax.text(2.2, y, left, ha="center", va="center", fontsize=12.5)
        ax.text(7.8, y, right, ha="center", va="center", fontsize=12.5)
        arrow = FancyArrowPatch((3.8, y), (6.2, y), arrowstyle="<->", mutation_scale=14, color="#555555", lw=1.2)
        ax.add_patch(arrow)

    ax.text(5.0, 0.55, "La IA hereda de la física la idea de modelar probabilidad mediante energía y entropía.", ha="center", fontsize=12.5)
    save(fig, "06_diccionario_fisica_ia")


def main():
    fig_paisaje_energia()
    fig_boltzmann_temperatura()
    fig_rbm_arquitectura()
    fig_crecimiento_configuraciones()
    fig_regla_aprendizaje()
    fig_diccionario_fisica_ia()
    print(f"Figuras generadas en: {OUT}")


if __name__ == "__main__":
    main()
