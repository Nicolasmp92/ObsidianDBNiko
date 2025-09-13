## 📂 Estructura de Perfiles y Roles de Usuario - BeanFlow

### 🔒 Base del sistema de permisos

- Se utilizará el paquete **Spatie Laravel-Permission**.
    
- Cada funcionalidad será **modular y controlable por el Administrador**, quien podrá activar o desactivar permisos específicos para cada rol.
    
- Todos los roles tendrán su propio panel con vistas personalizadas adaptadas a sus funciones.
    
- Los permisos estarán separados de los roles, permitiendo mayor flexibilidad para crear roles híbridos si es necesario.
    

---

### 🛠️ ADMINISTRADOR

**Acceso total a todas las funcionalidades**, incluyendo:

- Estadísticas generales del local.
    
- Gestión completa del menú (creación, edición, ocultar/activar items).
    
- Gestión de usuarios y sus roles.
    
- Activación o desactivación de módulos (por ejemplo: permitir que Ventas edite el menú diario, o habilitar QR para clientes).
    
- Visualización completa del estado de mesas, pedidos y ventas.
    
- Panel separado con sus herramientas de administración, **diferenciado visualmente** del resto (para evitar confusión).
    

---

### 🧾 GARZÓN

**Funciones principales:**

- Tomar pedidos desde formulario.
    
- Visualizar estado de mesas: ocupadas, disponibles, pendientes de atención.
    
- Ver y editar comandas activas de sus mesas.
    
- Confirmar o ajustar pedidos hechos por cliente vía QR.
    
- Notificar cierre de mesa o que el cliente pidió la cuenta.
    

**Flujo de trabajo (actual):**

- 1. Escoge mesa.
        
- 2. Abre pedido.
        
- 3. Agrega productos.
        
- 4. Envía a cocina.
        
- 5. Monitorea estado hasta cierre.
        

**Futuro:**

- Al cliente ordenar por QR, el garzón solo valida y entrega.
    

---

### 🍳 COCINA

**Vista táctil optimizada para cocina**:

- Comandas en tiempo real.
    
- Clasificación por:
    
    - Hora de recepción (orden natural).
        
    - Complejidad o tiempo estimado.
        
- Posibilidad de **reordenar prioridad** según carga de trabajo.
    
- Cambiar estado: recibido, en preparación, listo, entregado.
    

**Otras funciones:**

- Vista clara, con botones grandes y contraste alto.
    
- Puede marcar productos como "agotados" (opcional, configurable por admin).
    

---

### 💵 VENTAS

**Enfocado en la gestión de mesón y caja:**

- Ver ventas en tiempo real (por mesa o directo al mesón).
    
- Generar boletas, facturas, tickets provisorios.
    
- Registrar ventas en efectivo, tarjeta, transferencia, etc.
    
- Historial de ventas del día y filtros por forma de pago.
    
- Ver mesas activas, con opción de cerrar cuentas.
    

**Opcional según configuración del administrador:**

- Acceso a edición de menú diario (ej. activar menú colación).
    
- Gestión de delivery o pedidos telefónicos.
    
- Integración futura con SII para emisión de documentos tributarios.
    

---

### 👤 CLIENTE (futuro)

**Acceso desde escaneo de QR en la mesa:**

- Ver menú en tiempo real.
    
- Realizar pedido desde su celular.
    
- Ver estado del pedido en tiempo real (ej. "en cocina", "listo").
    
- Opción de registrarse como "cliente frecuente".
    
- Pagar desde el celular (futuro).