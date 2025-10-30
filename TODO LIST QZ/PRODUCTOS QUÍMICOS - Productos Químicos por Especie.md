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

## 🧮 1. Variables base

| Variable | Significado                                           | Unidad         |
| -------- | ----------------------------------------------------- | -------------- |
| `Cp`     | Capacidad del pozo                                    | **L** (litros) |
| `Ra`     | Relleno de agua actual (lo que se agregará)           | **L**          |
| `Dv`     | Valor de dosificación del producto (ej. 30 mL)        | **UM_orig**    |
| `Db`     | Base de dosificación (ej. por cada 100 L de agua)     | **L**          |
| `Eum/l`  | Equivalente por litro del producto                    | **UM_orig/L**  |
| `FaB`    | Factor de conversión a unidad base interna (mL o mg)  | —              |
| `Fdb`    | Factor de conversión desde base interna a UM original | —              |

> Las unidades originales (`UM_orig`) pueden ser **mL**, **mg**, **g**, **kg**, etc., según el producto químico.

---

## ⚗️ 2. Equivalente por litro (E)

### Si viene del backend:

$$
E_{UM/L} = \text{valor recibido (UM por litro)}
$$

### Si se calcula desde la ficha del producto:

$$
E_{UM/L} = \frac{D_V}{D_B}
$$

**Ejemplo:**

Si el producto indica “30 mL por 100 L”, entonces:

$$
E_{UM/L} = \frac{30}{100} = 0.3 \text{ mL/L}
$$

---

## 🧪 3. Conversión a unidad base interna

Esto se usa para mantener coherencia si el producto está en mg, g, kg, o mL, L.

$$
E_{BASE/L} = E_{UM/L} \times F_{aB}
$$

| Unidad original | Base interna | `FaB` |
| ---------------- | ------------- | ------ |
| mL → mL | 1 |
| L → mL | 1000 |
| mg → mg | 1 |
| g → mg | 1000 |
| kg → mg | 1 000 000 |

---

## 💧 4. Dosis inicial (pozo lleno)

$$
Dosis_{inicial\_BASE} = C_P \times E_{BASE/L}
$$

$$
Dosis_{inicial\_UM} = Dosis_{inicial\_BASE} \times F_{dB}
$$

Donde \( F_{dB} \) es el inverso de \( F_{aB} \):

| Unidad original | `FdB` |
| ---------------- | ------ |
| mL | 1 |
| L | 1/1000 |
| mg | 1 |
| g | 1/1000 |
| kg | 1/1 000 000 |

🔹 **Ejemplo:**

Pozo de **50 000 L**, producto **0.3 mL/L**:

$$
Dosis_{inicial} = 50\,000 \times 0.3 = 15\,000 \text{ mL}
$$

---

## 🧴 5. Dosis a aplicar (relleno)

$$
Dosis_{aplicada\_BASE} = R_A \times E_{BASE/L}
$$

$$
Dosis_{aplicada\_UM} = Dosis_{aplicada\_BASE} \times F_{dB}
$$

**Ejemplo:** con el mismo producto (0.3 mL/L) y relleno de **10 000 L**:

$$
Dosis_{aplicada} = 10\,000 \times 0.3 = 3\,000 \text{ mL}
$$

---

## 📊 6. Concentración aplicada (para calificación)

$$
Conc_{UM/L} = \frac{Dosis_{aplicada\_UM}}{R_A}
$$

**Ejemplo:**

$$
Conc_{UM/L} = \frac{3\,000}{10\,000} = 0.3 \text{ mL/L}
$$

---

## ✅ 7. Calificación de la dosis

Comparación de la concentración real con los **rangos definidos del producto**:

$$
\text{Si } Conc_{UM/L} < Rango_{min} \Rightarrow \text{“DOSIS BAJA AL MÍNIMO”}
$$

$$
\text{Si } Conc_{UM/L} > Rango_{max} \Rightarrow \text{“DOSIS SOBRE EL MÁXIMO”}
$$

$$
\text{Si } Rango_{min} \le Conc_{UM/L} \le Rango_{max} \Rightarrow \text{“DOSIS ACEPTADA”}
$$

💡 **Resumen visual:**

| Condición | Resultado |
| ---------- | ---------- |
| `Conc < Rango_min` | ⚠️ Dosis baja al mínimo |
| `Conc > Rango_max` | 🚫 Dosis sobre el máximo |
| `Rango_min ≤ Conc ≤ Rango_max` | ✅ Dosis aceptada |

---

## ⚙️ 8. Ejemplo completo

| Concepto | Valor | Unidad |
| --------- | ------ | ------- |
| Capacidad pozo `C_P` | 50 000 | L |
| Relleno `R_A` | 10 000 | L |
| Dosificación `D_V / D_B` | 30 mL / 100 L | — |
| `E_{UM/L}` | 0.3 | mL/L |

**Cálculos:**

$$
\begin{align*}
Dosis_{inicial} &= 50\,000 \times 0.3 = 15\,000 \text{ mL} \\
Dosis_{aplicada} &= 10\,000 \times 0.3 = 3\,000 \text{ mL} \\
Conc_{UM/L} &= \frac{3\,000}{10\,000} = 0.3 \text{ mL/L}
\end{align*}
$$

Si el rango permitido es **0.25–0.35 mL/L** → ✅ **DOSIS ACEPTADA**

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

- [x] Al seleccionar **Producto** → pintar Unidad, Dosis Inicial, Rangos (ya lo haces).
    
- [ ] Input **Relleno (L)** → al escribir:
    
    - [x] Calcular y mostrar (readonly) **Dosis por Relleno Calculada**.
        
    - [x] Pre-cargar **Dosis Aplicada** con ese valor (el aplicador puede ajustar).
        
    - [x] Si queda **fuera de rango**, marcar el input y mostrar aviso; **habilitar** Acción Correctiva.
        

## D) **Editar Inspección / Muestras**

- [x] Mostrar también las dosis **calculadas** (si decides guardarlas) para auditoría.
    
- [x] Mantener la validación visual de rangos.





_IDEAS O SUGERENCIAS:
	. las docis inicales podría  colocarse al momento de crear el químico y no en la asignación de la docis al fruto: 

