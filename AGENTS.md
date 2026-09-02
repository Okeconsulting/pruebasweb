# Reglas e Identidad del Proyecto - Oke Consulting

Este documento define la estructura técnica, componentes, identidad visual y reglas de desarrollo para el sitio web de **Oke Consulting**.

---

## 1. Información General del Proyecto

- **Nombre:** Oke Consulting Web
- **Propósito:** Sitio web corporativo para servicios de consultoría (Analítica, Tecnología) y programas de entrenamiento (Liderazgo, Habilidades Técnicas).
- **Entorno:** Sitio web estático puro basado en **HTML5 semántico / CSS3 modular (Variables) / JavaScript (Vanilla)** con Bootstrap 5.3 vía CDN + Automatización en Python (.venv).
- **Criterio de Arquitectura:** 100% libre de dependencias de Node.js o herramientas de compilación complejas. Ejecutable directamente abriendo los archivos en cualquier navegador o servidor web estándar.

---

## 2. Pila Tecnológica & Dependencias

- **Frontend UI Framework:** [Bootstrap 5.3.6 (CDN)](https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/css/bootstrap.min.css)
- **Componentes Interactivos:** Bootstrap 5.3.6 Bundle JS (CDN) + js/main.js (Vanilla JS)
- **Iconos:** FontAwesome 6 (CDN)
- **Estilos Modulares:** css/variables.css, css/components.css, css/style.css
- **Automatización:** Python 3.x (.venv) para script de despliegue FTP (deployftp.py).

---

## 3. Identidad Visual & Tokens de Diseño

- **Logo & Favicon:**
  - Favicon: /img/logo_ed3.ico
  - Logo de Marca: /img/logo_ed3.jpeg (dimensiones estándar en Navbar: 120x120 px)
- **Paleta de Colores (Definida en css/variables.css):**
  - Fondo corporativo característico: --oke-bg: #e2f9eb; (verde menta suave)
  - Color primario de marca: --oke-primary: #198754;
  - Hover primario: --oke-primary-hover: #157347;
  - Color oscuro de texto: --oke-dark: #212529;
  - Texto atenuado: --oke-text-muted: #6c757d;
- **Componentes UI Clave (css/components.css):**
  - .site-wrapper, .site-header, .site-main, .site-footer (Layout wrapper)
  - .oke-navbar, .navbar-brand-logo, .navbar-brand-text (Navbar)
  - .oke-breadcrumb-bar (Migas de pan con separador estilizado)
  - .oke-card, .oke-feature-box (Tarjetas con elevación suave en hover)
  - .oke-accordion (Acordeones interactivos para FAQ)
  - .oke-legal-card (Tarjetas de términos y condiciones)
  - .oke-form-card, .oke-form-control (Formularios y validación)
  - .oke-status-card, .oke-search-box (Componentes para estados y 404)
  - .oke-wip-badge, .oke-newsletter-box (Componentes para secciones WIP)

---

## 4. Mapa del Sitio y Estructura de Archivos

| Archivo | Sección | Descripción |
| :--- | :--- | :--- |
| index.html | **Inicio** | Página principal de presentación de Oke Consulting |
| 
osotros.html | **Nosotros** | Misión, visión, valores, historia y metodología de trabajo |
| consultoria.html | **Consultoría (Hub)** | Visión general y tarjetas de los servicios de consultoría |
| nalitics.html | **Consultoría > Analítica** | Servicios de analítica de datos e inteligencia de negocios |
| 	ecnologia.html | **Consultoría > Tecnología** | Soluciones tecnológicas, software libre e infraestructura |
| ntrenamientos.html | **Entrenamientos (Hub)** | Visión general de programas y capacitaciones |
| liderazgo.html | **Entrenamientos > Liderazgo** | Capacitaciones en liderazgo, Lean Management y comunicación |
| 	ecnicos.html | **Entrenamientos > Técnicos** | Formación técnica aplicada y curso de Google Sheets |
| contactos.html | **Contacto** | Formulario de contacto y canales de atención |
| aq.html | **Preguntas Frecuentes** | Acordeón interactivo con 16 dudas frecuentes sobre consultoría y cursos |
| 	erminos.html | **Términos & Privacidad** | Cláusulas claras de confidencialidad, propiedad de datos y garantías |
| 404.html | **Error 404 (NotFound)** | Manejador de página no encontrada con buscador y accesos directos |
| 500.html | **Error 500 (ServerError)** | Aviso de soporte técnico con botón para recargar la vista |
| wip.html | **Work In Progress (WIP)** | Plantilla para secciones en desarrollo con captura de newsletter |

---

## 5. Despliegue y Operaciones

- **Script:** deployftp.py
- **Variables requeridas:** FTP_SERVER, FTP_USERNAME, FTP_PASSWORD, FTP_REMOTE_PATH
- **Exclusiones obligatorias:** .git/, .github/, .venv/, .agents/, __pycache__/, *.pyc, .env, deployftp.py
