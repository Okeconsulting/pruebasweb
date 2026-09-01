# Reglas e Identidad del Proyecto - Oke Consulting

Este documento define la estructura técnica, componentes, identidad visual y reglas de desarrollo para el sitio web de **Oke Consulting**.

---

## 1. Información General del Proyecto

- **Nombre:** Oke Consulting Web
- **Propósito:** Sitio web corporativo para servicios de consultoría (Analítica, Tecnología) y programas de entrenamiento (Liderazgo, Habilidades Técnicas).
- **Entorno:** HTML5 / CSS3 / JavaScript (Vanilla) + Automatización en Python.

---

## 2. Pila Tecnológica & Dependencias

- **Frontend UI Framework:** [Bootstrap 5.3.6](https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/css/bootstrap.min.css)
- **Iconos:** FontAwesome (CDN)
- **Automatización:** Python 3.x (.venv) para scripts de utilidades y despliegue.

---

## 3. Identidad Visual & Diseño

- **Logo & Favicon:**
  - Favicon: /img/logo_ed3.ico
  - Logo de Marca: /img/logo_ed3.jpeg (dimensiones estándar en Navbar: 120x120 px)
- **Paleta de Colores:**
  - Color de fondo característico: #e2f9eb (verde suave corporativo)
  - Clases estándar de Bootstrap (g-body-tertiary, tn-primary, tn-outline-*)
- **Estilos Globales de Botones e Iconos:**
  `css
  .btn .fa-solid, .btn .fa-brands {
      margin-right: .5rem;
  }
  .fa-2x {
      font-size: 2em;
  }
  `

---

## 4. Mapa del Sitio y Estructura de Páginas

| Archivo | Sección | Descripción |
| :--- | :--- | :--- |
| index.html | **Home** | Página principal de presentación de Oke Consulting |
| 
osotros.html | **Nosotros** | Misión, visión, propuesta de valor y equipo |
| consultoria.html | **Consultoría (Hub)** | Visión general de los servicios de consultoría |
| nalitics.html | **Consultoría > Analítica** | Servicios de analítica de datos e inteligencia de negocios |
| 	ecnologia.html | **Consultoría > Tecnología** | Soluciones tecnológicas e infraestructura |
| ntrenamientos.html | **Entrenamientos (Hub)** | Visión general de programas y capacitaciones |
| liderazgo.html | **Entrenamientos > Liderazgo** | Capacitaciones y talleres de liderazgo |
| 	ecnicos.html | **Entrenamientos > Técnicos** | Formación en habilidades técnicas especializadas |
| contactos.html | **Contactos** | Formulario y canales de contacto |

---

## 5. Estándar de Componentes

### A. Barra de Navegación (Navbar)
- Ubicación: Fija superior (
avbar navbar-expand-lg bg-body-tertiary sticky-top)
- Estructura:
  - Marca con Logo + Texto Oke Consulting con enlace a index.html
  - Menú:
    1. *Home* (index.html)
    2. *Nosotros* (
osotros.html)
    3. *Consultoría* (Dropdown y Hub: consultoria.html, nalitics.html, 	ecnologia.html)
    4. *Entrenamientos* (Dropdown y Hub: ntrenamientos.html, liderazgo.html, 	ecnicos.html)
    5. *Contactos* (contactos.html)
- Debe mantenerse consistente en todas las páginas, marcando la clase ctive en la página correspondiente.

---

## 6. Despliegue y Operaciones

- **Script:** deployftp.py
- **Variables requeridas:** FTP_SERVER, FTP_USERNAME, FTP_PASSWORD, FTP_REMOTE_PATH
- **Exclusiones obligatorias:** .git/, .github/, .venv/, .agents/, __pycache__/, *.pyc, .env, deployftp.py
