/**
 * Vanilla JavaScript Utilities & Interactive Components - Oke Consulting
 * Zero Node.js / Zero compilation requirements
 */
document.addEventListener('DOMContentLoaded', () => {
  // 1. Auto-close mobile navbar when a link is clicked
  const navLinks = document.querySelectorAll('.navbar-nav .nav-link:not(.dropdown-toggle)');
  const navbarCollapse = document.getElementById('navbarSupportedContent');
  
  if (navbarCollapse && window.bootstrap) {
    const bsCollapse = new bootstrap.Collapse(navbarCollapse, { toggle: false });
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        if (navbarCollapse.classList.contains('show')) {
          bsCollapse.hide();
        }
      });
    });
  }

  // 2. Interactive Contact Form Handler with Feedback
  const contactForm = document.getElementById('okeContactForm');
  const formSuccessAlert = document.getElementById('okeFormSuccessAlert');

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const nombreInput = document.getElementById('nombre');
      const nombre = nombreInput ? nombreInput.value : 'amigo/a';

      if (formSuccessAlert) {
        const clientNamePlaceholder = document.getElementById('clientNamePlaceholder');
        if (clientNamePlaceholder) {
          clientNamePlaceholder.textContent = nombre;
        }
        formSuccessAlert.classList.remove('d-none');
        contactForm.classList.add('d-none');
      } else {
        alert(`¡Gracias ${nombre} por comunicarte con Oke Consulting! Responderemos a la brevedad.`);
        contactForm.reset();
      }
    });
  }

  // 3. Reset Contact Form button
  const resetFormBtn = document.getElementById('resetFormBtn');
  if (resetFormBtn && contactForm && formSuccessAlert) {
    resetFormBtn.addEventListener('click', () => {
      contactForm.reset();
      formSuccessAlert.classList.add('d-none');
      contactForm.classList.remove('d-none');
    });
  }

  // 4. Client-side Search on 404 Page
  const searchForm = document.getElementById('okeSearchForm');
  const searchInput = document.getElementById('okeSearchInput');

  if (searchForm && searchInput) {
    searchForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const query = searchInput.value.trim().toLowerCase();
      if (!query) return;

      const routes = [
        { terms: ['nosotros', 'quienes', 'mision', 'vision', 'equipo', 'historia'], url: 'nosotros.html' },
        { terms: ['analitica', 'datos', 'bi', 'dashboards', 'tableros', 'kpi', 'analitica de datos'], url: 'analitics.html' },
        { terms: ['tecnologia', 'software', 'libre', 'infraestructura', 'nube', 'cloud', 'soporte'], url: 'tecnologia.html' },
        { terms: ['consultoria', 'servicios', 'asesoria'], url: 'consultoria.html' },
        { terms: ['liderazgo', 'lean', 'oratoria', 'comunicacion', 'cadena de valor'], url: 'liderazgo.html' },
        { terms: ['tecnicos', 'google sheets', 'sheets', 'excel', 'curso', 'capacitacion', 'automatizacion'], url: 'tecnicos.html' },
        { terms: ['entrenamientos', 'cursos', 'talleres'], url: 'entrenamientos.html' },
        { terms: ['faq', 'preguntas', 'frecuentes', 'dudas', 'costos', 'precios'], url: 'faq.html' },
        { terms: ['terminos', 'privacidad', 'nda', 'condiciones', 'legal'], url: 'terminos.html' },
        { terms: ['contacto', 'contactos', 'mensaje', 'telefono', 'email', 'correo'], url: 'contactos.html' }
      ];

      let match = routes.find(r => r.terms.some(t => query.includes(t)));
      if (match) {
        window.location.href = match.url;
      } else {
        window.location.href = 'index.html';
      }
    });
  }

  // 5. Work In Progress (WIP) Newsletter Subscription Form
  const wipForm = document.getElementById('okeWipForm');
  const wipSuccess = document.getElementById('okeWipSuccess');

  if (wipForm) {
    wipForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const emailInput = document.getElementById('wipEmail');
      const email = emailInput ? emailInput.value : '';

      if (wipSuccess) {
        const emailPlaceholder = document.getElementById('wipEmailPlaceholder');
        if (emailPlaceholder) emailPlaceholder.textContent = email;
        wipSuccess.classList.remove('d-none');
        wipForm.classList.add('d-none');
      } else {
        alert(`¡Gracias! Te notificaremos a ${email} en cuanto esta sección esté disponible.`);
        wipForm.reset();
      }
    });
  }
});
