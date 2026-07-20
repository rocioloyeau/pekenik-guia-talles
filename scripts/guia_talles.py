"""
Genera la guia visual de talles (Propuesta 1 del CX audit de Peke Nik & Mami)
para compartir por WhatsApp e Instagram.

v2 (fix por feedback de Vane, ver docs/feedback_vane.md): se agrega el peso
como columna igual de importante que la edad -no secundaria- y una nota
explicita de que la escala varia segun la marca, para que quien reciba la
guia sepa que igual puede haber que confirmar con Vane.
"""
import matplotlib.pyplot as plt

filas = [
    ("RN (0-1 mes)", "Hasta 4 kg aprox."),
    ("0-3 meses", "4 - 6 kg aprox."),
    ("3-6 meses", "6 - 8 kg aprox."),
    ("6-9 meses", "8 - 9 kg aprox."),
    ("9-12 meses", "9 - 10 kg aprox."),
    ("12-18 meses", "10 - 11.5 kg aprox."),
    ("18-24 meses", "11.5 - 13 kg aprox."),
]

fig, ax = plt.subplots(figsize=(6, 4.6))
ax.axis("off")
tabla = ax.table(
    cellText=filas,
    colLabels=["Edad", "Peso (dato clave, no opcional)"],
    loc="upper center",
    cellLoc="center",
)
tabla.scale(1, 1.5)
ax.set_title("Guia de talles Peke Nik & Mami - orientativa", pad=20)
ax.text(
    0.5, 0.02,
    "Esta guia es orientativa: la escala real puede variar segun la marca.\n"
    "Contanos edad Y peso del bebe para confirmar el talle exacto.",
    ha="center", va="bottom", fontsize=8, style="italic", transform=ax.transAxes,
)
fig.tight_layout()
fig.savefig("assets/guia_talles.png", dpi=150)
print("Guia generada en assets/guia_talles.png")
