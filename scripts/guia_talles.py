"""
Genera la guia visual de talles (Propuesta 1 del CX audit de Peke Nik & Mami)
para compartir por WhatsApp e Instagram.

v1: escala de referencia general por edad, tomada de convenciones estandar
de indumentaria infantil. Pendiente de validar con Vane si aplica igual
a las marcas que vende (ver docs/feedback_vane.md).
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

fig, ax = plt.subplots(figsize=(6, 4))
ax.axis("off")
tabla = ax.table(
    cellText=filas,
    colLabels=["Edad", "Peso de referencia"],
    loc="center",
    cellLoc="center",
)
tabla.scale(1, 1.5)
ax.set_title("Guia de talles Peke Nik & Mami - por edad", pad=20)
fig.tight_layout()
fig.savefig("assets/guia_talles.png", dpi=150)
print("Guia generada en assets/guia_talles.png")
