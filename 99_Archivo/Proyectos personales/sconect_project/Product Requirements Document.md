
---

# PRD: Sconect - Plataforma de Gestión Clínica

## 1. Visión del Producto

Sconect es una plataforma SaaS diseñada para digitalizar la gestión de clínicas independientes (kinesiólogos, odontólogos, medicina alternativa, etc.). Su objetivo es centralizar la agenda, evolucionar pacientes y permitir una administración segura sin compartir contraseñas.

## 2. Gobernanza de Usuarios y Seguridad (RBAC Dinámico)

La seguridad es el pilar central. Se elimina la práctica de compartir credenciales mediante **permisos granulares**.

- **Super Admin:** Titular de la cuenta. Gestiona usuarios, asigna roles y delega permisos especiales.
    
- **Administrativo:** Gestiona agenda y pacientes. Puede realizar tareas extras (ej: generar reportes) solo si el Super Admin le otorga el permiso explícito.
    
- **Clínico:** Gestión de evoluciones y atenciones. Puede autogestionar su agenda.
    
- **Seguridad:**
    
    - **Trazabilidad:** `AuditLog` inmutable para toda acción (quién, qué, cuándo).
        
    - **Delegación:** Panel para activar funciones delegadas sin compartir acceso.
        
    - **Sesiones:** Registro de IP y dispositivo por cada acción realizada.
        

## 3. Funcionalidades Core (MVP)

- **Agenda Clínica:**
    
    - Visualización de agenda sincronizada.
        
    - **Notificaciones:** Envío automatizado de recordatorios vía correo electrónico (en fase 2: WhatsApp).
        
- **Ficha Clínica Digital:**
    
    - Registro de paciente (datos personales + historial).
        
    - Evoluciones: Sistema de notas con timestamp (no destructivo).
        
    - Gestión de archivos: Subida de imágenes/documentos.
        
- **Reportes:** Módulo para métricas de gestión (accesible bajo permiso delegado).
    

## 4. Stack Técnico

- **Backend:** Go (Clean Architecture: Domain, Use Cases, Adapters).
    
- **Frontend:** Flutter (Mobile-first, diseño responsivo, BloC).
    
- **Base de Datos:** PostgreSQL (Postgres).
    
- **Infraestructura:** VPS, contenedores Docker.
    

## 5. Estándares Técnicos

- **Clean Code:** Cumplimiento estricto de los principios SOLID.
    
- **Interoperabilidad:** Modelos de datos alineados al estándar **HL7 FHIR**.
    
- **UX/UI:** Atomic Design, accesibilidad WCAG 2.1 (contraste 4.5:1), touch targets mínimos de 48px.
    
- **Kaizen:** Aplicación de la "Regla del Boy Scout" en cada pull request.