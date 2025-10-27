Rutas Involucradas:
- resources\views\Aplicadores\ProductosEspecies\Index.blade.php -> (para mostrar tabla Productos quimicos)
- resources\views\Aplicadores\ProductosEspecies\Datos.blade.php -> (para mostrar las especies relacionadas a los quimicos)
### Descripción:
En *"productos químicos por especie"* Los rangos en los productos químicos deben indicar la ==dosis inicial== de acuerdo al **volumen del pozo** y según el **relleno de agua** en los estanques, anotar los litros y que se calcule automáticamente el volumen de producto que deben aplicar. En productos químicos por especie, dejar rangos y agregar columna con la dosificación por producto para posterior calculo de dosis inicial o relleno.

En Productos químicos por especie, dejar rangos y agregar columna con dosificación por producto para posterior calculo de dosis inicial o relleno 

### 🧩 **Terminología del módulo “Químicos en Pozo”**

**Pozo** 🧱  
→ Recipiente o estanque donde se mezcla **agua** con **productos químicos** para el tratamiento de frutas.  
Cada pozo tiene una **capacidad total (Lt)** definida.

---

**Capacidad del Pozo** ⚖️  
→ Volumen máximo de agua (en litros) que puede contener el pozo cuando está lleno.  
Ejemplo: 30.000 L.

---

**Cant. Agua en Pozo** 💧  
→ Litros de agua **actuales** en el pozo al momento de iniciar la inspección.  
Usado para calcular la **dosis inicial** si el pozo no está completamente lleno.

---

**Relleno (Agua)** 🚰  
→ Cantidad de agua (en litros) que se **agrega** al pozo durante el proceso, cuando el nivel baja.  
El sistema calcula automáticamente la **dosis adicional de producto químico** que debe aplicarse según ese relleno.

---

**Producto Químico** ⚗️  
→ Sustancia utilizada en el tratamiento del agua de los pozos (ej. fungicidas, ácidos, hipoclorito).  
Cada producto está asociado a una **unidad de medida (LT, KG, GRS)** y puede tener diferentes dosis por especie.

---

**Dosis Inicial** 🎯  
→ Cantidad de producto químico que se aplica cuando el pozo está lleno.  
Se define por **producto y especie** y sirve de base para calcular dosis proporcionales.

---

**Dosis Aplicada** 🧪  
→ Cantidad **real** de producto que el aplicador añadió (puede coincidir o no con la dosis sugerida).  
Se registra manualmente y se valida frente a la dosis calculada.

---

**Dosis Sugerida** 📐  
→ Valor calculado automáticamente por el sistema en base a:  
`(relleno × dosis_inicial) / capacidad_pozo`  
Indica cuánto químico se debería aplicar según los litros reales de agua.

---

**Unidad de Medida (U/M)** ⚖️  
→ Expresa la forma en que se cuantifica el producto químico:

- **LT** = litros
    
- **KG** = kilogramos
    
- **GRS** = gramos
    

---

**Rango Mín / Máx** 📊  
→ Límites permitidos para la dosis de cada producto.  
El sistema los usa para validar si la dosis aplicada está dentro del rango aceptable.

---

**Calificación** ✅  
→ Resultado automático que compara la dosis aplicada con la dosis sugerida.

- **DOSIS ACEPTADA** → dentro del margen de tolerancia (±5%).
    
- **REVISAR** → fuera del rango o inconsistente.
    

---

**Acción Correctiva** 🛠️  
→ Observación que explica por qué la dosis aplicada difiere de la sugerida o está fuera de rango.  
Ejemplo: “Relleno parcial con producto concentrado” o “Corrección manual por baja temperatura”.

---
### 🧩 1️⃣ Qué tienes hasta ahora

Tienes **tres entidades principales:**

| Entidad                               | Qué representa                                                                     | Ejemplo en tus pantallas                     |
| ------------------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------- |
| 🧱 **Pozos**                          | Recipientes donde se mezcla agua con productos químicos para tratar fruta          | “Pozo Niko”, “Pozo Fungicida (Unitec)”       |
| ⚗️ **Productos Químicos**             | Sustancias como “Fungicidas”, “Ácido Clorhídrico” o “Hipoclorito Sódico”           | Cada uno tiene su unidad (LT, KG, GRS, etc.) |
| 🍒 **Productos Químicos por Especie** | Define qué productos se aplican a qué especie (Cerezas, Uvas, etc.) y en qué dosis | Dosis inicial, unidad, rango min/máx.        |

Luego tienes el módulo **"Químicos en Pozo"**, donde registras la **aplicación real** (fecha, pozo, máquina, dosis, etc.).

---

### ⚗️ 2️⃣ Qué pide el requerimiento realmente

> "Los rangos en los productos químicos deben indicar la dosis inicial de acuerdo al volumen del pozo y según el relleno de agua en los estanques. Anotar los litros y que se calcule automáticamente el volumen de producto que deben aplicar."

Vamos a traducirlo a un lenguaje más claro 👇

#### Significa:

Quieren que **la dosis inicial (o cantidad de químico a aplicar)** **no sea fija**, sino que **se calcule dinámicamente** según:

- El **volumen del pozo** (litros totales de agua que puede contener).
    
- El **relleno de agua actual** (litros reales de agua en ese momento, ingresados en el formulario).
    

Esto es importante porque:

> No es lo mismo aplicar producto en un pozo lleno (30.000 L) que en uno con solo 2.500 L.

---

### 💧 3️⃣ Ejemplo matemático del cálculo

Supongamos que:

- El pozo tiene **capacidad total = 30.000 L**
    
- El relleno actual es **2.500 L**
    
- El producto químico tiene **dosis inicial de 30 L por pozo lleno (30.000 L)**
    

Entonces, para calcular la cantidad proporcional de producto a aplicar según el agua actual:

### 💧 Cálculo de Dosis Real (según relleno)

La **dosis real** se ajusta proporcionalmente según el volumen de agua que se haya rellenado en el pozo.

#### 📘 Fórmula general

$$
\text{Dosis real} = \frac{\text{Relleno actual}}{\text{Capacidad total}} \times \text{Dosis inicial}
$$

#### 📊 Ejemplo práctico

- Capacidad total del pozo: **30 000 L**  
- Relleno actual: **2 500 L**  
- Dosis inicial: **30 L**

$$
\text{Dosis real} = \frac{2500}{30000} \times 30 = 2.5\,L
$$

➡️ Por lo tanto, la **dosis real a aplicar** es **2.5 L**.


---

### 🧮 4️⃣ Cómo se aplicaría en tu sistema

|Etapa|Qué pasa|Qué datos intervienen|
|---|---|---|
|1️⃣ Crear inspección|El usuario elige pozo → el sistema ya sabe la **capacidad total** (por ejemplo 30.000 L).|`pozos.capacidad_lt`|
|2️⃣ Usuario ingresa **relleno actual (L)** en el formulario|Por ejemplo, 2.500 L.|Campo input “relleno”|
|3️⃣ El sistema busca el producto químico seleccionado|Y su **dosis inicial** asignada a la especie (ej. 30 L).|`producto_especie.dosis_inicial`|
|4️⃣ El sistema calcula automáticamente la **dosis proporcional a aplicar**|Fórmula anterior: `(relleno / capacidad_pozo) * dosis_inicial`||
|5️⃣ En la vista de inspección o muestra, se muestra la dosis calculada|Por ejemplo, “Debe aplicar: 2.5 L de Fungicida”||

---

### 🧭 5️⃣ El objetivo general del requerimiento

El objetivo final de todo esto es que el sistema:

- 💧 **tome en cuenta el agua real (relleno)**
    
- 📏 **use la capacidad del pozo**
    
- ⚗️ **y calcule la cantidad exacta de químico (dosis real) que se debe aplicar**  
    en lugar de mostrar solo la dosis inicial “fija”.
    

---

### 🧠 6️⃣ Qué debes preparar conceptualmente

- [x] 1. **Agregar campo "dosis_inicial"** a la relación _producto_especie_ (ya lo hiciste ✔️).
    
- [ ] 2. **Obtener capacidad del pozo** cuando se seleccione en la inspección.
    
- [x] 3. **Pedir relleno actual** (ya tienes ese input en la vista).
    
- [ ] 4. **Calcular automáticamente la dosis proporcional** en el frontend (JS) o backend (controller).
    
- [ ] 5. **Guardar ese valor como "dosis aplicada"** en la tabla de muestras.
    

---

# 🧭 Cambios de UI (pantallas y campos)

## A) **Productos por Especie**

- [x] Confirmar que la tabla muestre: **Dosis Inicial**, **Rango Min**, **Rango Máx**, **Unidad**.
    
- [x] Tooltip corto explicando que **dosis_inicial** está pensada para pozo **lleno** (capacidad total), y que el sistema **proporciona** según litros reales.
    

## B) **Crear inspección (químicos en pozo)**

- [x] Al elegir **Pozo** → mostrar **Capacidad** (readonly).
    
- [x] Campo **Cant. Agua en Pozo (L)** (obligatorio si vas a calcular dosis inicial en esta etapa).
    
- [x] Campo **Producto** → al seleccionar:
    
    -  Pintar **Unidad**, **Dosis Inicial**, **Rangos**.
        
    -  Calcular y mostrar (readonly) **Dosis Inicial Calculada** con la fórmula.
        
- [x] Si no hay **cant_agua_pozo**, ocultar/inhabilitar dosis inicial calculada.
    

## C) **Agregar Muestra** (modal)

-  Al seleccionar **Producto** → pintar Unidad, Dosis Inicial, Rangos (ya lo haces).
    
-  Input **Relleno (L)** → al escribir:
    
    -  Calcular y mostrar (readonly) **Dosis por Relleno Calculada**.
        
    -  Pre-cargar **Dosis Aplicada** con ese valor (el aplicador puede ajustar).
        
    -  Si queda **fuera de rango**, marcar el input y mostrar aviso; **habilitar** Acción Correctiva.
        

## D) **Editar Inspección / Muestras**

-  Mostrar también las dosis **calculadas** (si decides guardarlas) para auditoría.
    
-  Mantener la validación visual de rangos.





_IDEAS O SUGERENCIAS:
	. las docis inicales podría  colocarse al momento de crear el químico y no en la asignación de la docis al fruto: 

