---
title: "Una guía de talles que casi empeora el problema que quería resolver"
date: 2026-07-20
---

# Una guía de talles que casi empeora el problema que quería resolver

## Contexto

Este proyecto es la auditoría de experiencia de cliente (CX) de **Peke Nik &
Mami** (Oncativo, Córdoba), la tienda de ropa para bebés y niños que maneja mi
hermana Vane, que vengo trabajando como caso real a lo largo de la
diplomatura. Del diagnóstico salieron tres Pain Points y tres propuestas de
mejora. Esta entrada documenta la implementación de la primera: una **guía
visual de talles** para compartir por WhatsApp e Instagram, pensada para
reducir las consultas repetitivas y los cambios por talle incorrecto.

## Problema

El Pain Point 1 del diagnóstico es la dificultad para determinar el talle
correcto, sobre todo en compras para bebés y regalos. Armé una primera
versión de la guía con una escala estándar: edad del bebé → rango de peso →
talle. Es la convención más común en indumentaria infantil y, en el papel,
resolvía el pain point.

El problema apareció al chequearla con Vane. En la entrevista original ya
estaba la pista, solo que no la había tomado en cuenta al diseñar la v1:

> "Cuando me dicen el talle, siempre pregunto la edad porque a veces las
> escalas son diferentes entre las marcas."

Vane nunca se guía solo por la edad. Cruza edad y peso, y ajusta según la
marca puntual que está ofreciendo, porque un talle "6 meses" de un
proveedor no equivale al de otro. Una guía que dice "edad → talle" como
escala fija no solo es incompleta: puede generar *más* cambios por talle
incorrecto que los que evita, que es exactamente lo que la guía debía
reducir.

## Acciones (post-mortem constructivo)

1. **Documenté el feedback tal cual lo dijo Vane**, en vez de resumirlo o
   suavizarlo, para no perder el matiz de "a veces las escalas son
   diferentes entre las marcas" (`docs/feedback_vane.md`).
2. **Rehice la guía (v2)**: el peso pasa a tener el mismo peso visual y
   funcional que la edad — no es un dato secundario — y se agrega una nota
   explícita de que la escala es orientativa y puede variar según la marca.
3. **Actualicé el mensaje rápido de WhatsApp** que acompaña la guía: en vez
   de "consultá la guía y contame edad y peso", ahora pide edad *y* peso
   siempre, antes de confirmar el talle, para que nadie compre guiándose
   solo por la imagen.
4. **Até el fix a un KPI real del plan de medición** del CX audit
   (`docs/kpi_talle.md`): % de cambios por talle incorrecto. La v1 probablemente
   no lo hubiera movido, porque no atacaba la causa real (variación entre
   marcas); la v2 sí tiene una hipótesis de impacto directa.

## Aprendizajes

- El dato que invalidó la v1 ya estaba en la investigación original. El
  error no fue de research, fue de no volver a leer la entrevista completa
  antes de diseñar la solución — diseñé desde una convención genérica en vez
  de desde lo que Vane realmente dijo que hace.
- Una guía "linda" no es lo mismo que una guía que funciona para el negocio
  real. Lo visual estaba bien en la v1; lo que fallaba era la lógica de
  fondo.
- Atar cada fix a un KPI del plan de medición (no solo "mejoré la guía")
  obliga a preguntarse si el cambio realmente ataca la causa del problema o
  solo lo maquilla.

## Reflexión sobre feedback radicalmente sincero

Lo más incómodo de este proceso no fue rehacer el script del gráfico: fue
admitir que la v1, con la que estaba conforme, no le servía a Vane tal cual
estaba. Fue tentador pensar "es una guía orientativa, ya está bien así" y
dejarla pasar. Aplicar feedback radicalmente sincero acá significó tomar en
serio una frase que parecía un detalle menor de la entrevista ("a veces las
escalas son diferentes entre las marcas") y usarla para invalidar un trabajo
ya terminado, en vez de defenderlo. Prefiero una guía que tarde un día más
en salir pero refleje cómo Vane realmente asesora, a una que se vea prolija
y termine generando más cambios de los que evita.

## Control de versiones — evidencia

Historial de commits de este repositorio (orden cronológico):

1. `f4d9f19` — Agrega v1 de la guía visual de talles (por edad)
2. `d364b57` — docs: registra feedback de Vane sobre la guía v1 (escala única no sirve)
3. `b562786` — fix: v2 de la guía con peso como dato clave y aviso de variación por marca
4. `81bb13f` — docs: liga el fix al KPI 3 del plan de medición (% cambios por talle incorrecto)

Repositorio completo: https://github.com/rocioloyeau/pekenik-guia-talles/commits/main
