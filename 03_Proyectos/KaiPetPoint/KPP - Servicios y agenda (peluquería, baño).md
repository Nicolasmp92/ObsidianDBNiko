---
status: Pendientes
proyecto: kaipetpoint
fase: fase-2
criticidad: media
esfuerzo: M
---
_Objetivo: vender y agendar servicios (baño, peluquería) además de productos._

- [ ] Ítems tipo servicio en catálogo: sin stock, con duración estimada.
    
- [ ] Agenda de horas: servicio + cliente/mascota + fecha/hora + estado (agendada/completada).
    
- [ ] Cobro del servicio por el mismo POS con comprobante.
    
- [ ] Depende de: [[KPP - Clientes y cuenta corriente (fiado)]]; mascotas opcionales ([[KPP - Ficha de mascota y recordatorio de recompra]]).

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/servicios-agenda
```
