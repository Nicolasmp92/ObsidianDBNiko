---
status: Pendientes
proyecto: kaipetpoint
fase: fase-2
criticidad: alta
esfuerzo: M
---
_Objetivo: diferenciador del nicho — mascotas ligadas al cliente y recordatorio de recompra de alimento._

- [ ] Tabla `mascotas` ligada a cliente: especie, raza, peso, fecha de nacimiento.
    
- [ ] Consumo estimado: kg/día por mascota → al comprar alimento se calcula fecha estimada de agotamiento.
    
- [ ] Lista/alerta "clientes por recomprar" para contacto proactivo (manual → WhatsApp en fase 3).
    
- [ ] Sugerencia de ración/productos según peso y especie en la ficha.
    
- [ ] Depende de: [[KPP - Clientes y cuenta corriente (fiado)]].

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/mascotas-recompra
```
