---
status: Pendientes
proyecto: kaipetpoint
fase: fase-2
criticidad: media
esfuerzo: M
---
_Objetivo: leer el peso directo de la balanza al POS en ventas a granel._

- [ ] Lectura de peso desde balanza USB/serial (WebSerial/WebUSB) al input de kg del POS.
    
- [ ] Fallback manual con validación siempre disponible.
    
- [ ] Depende de: [[KPP - Venta de alimentos a granel]].

**RIESGO** — protocolos de balanza variados; requiere hardware de prueba real antes de comprometer la integración.

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/balanza-granel
```
