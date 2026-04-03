# Ensambla páginas legales del prototipo Fenómeno a partir de HTML extraído (presentación de marca Fenómeno).
import re
from pathlib import Path

DIR = Path(__file__).resolve().parent
# Raíz del repo: ahí vive el sitio estático (index.html, assets/, legales).
OUT = DIR.parent.parent

FENOMENO_MAIL = "hola@fenomeno.bar"
FENOMENO_URL = "https://fenomeno.bar"
OG_IMAGE_PATH = "/assets/og/og-default.jpg"


def fenomeno_legales_html(html: str) -> str:
    """Sustituye dominios, marca comercial ajena en pantalla y correos genéricos por Fenómeno."""
    s = html
    s = re.sub(r"reservations@mandalaticket\.com", FENOMENO_MAIL, s, flags=re.I)
    s = re.sub(r"https?://www\.mandalatickets\.com/?", FENOMENO_URL + "/", s, flags=re.I)
    s = re.sub(r"www\.mandalatickets\.com", "fenomeno.bar", s, flags=re.I)
    s = re.sub(r"MANDALATICKETS\.COM", "FENÓMENO", s)
    s = re.sub(r"Mandalatickets\.com", "Fenómeno", s, flags=re.I)
    s = re.sub(r"MandalaTickets\.com", "Fenómeno", s)
    s = re.sub(r"\bMANDALATICKETS\b", "FENÓMENO", s)
    s = re.sub(r"MandalaTickets", "Fenómeno", s)
    s = re.sub(r"Mandala Tickets", "Fenómeno", s)
    s = re.sub(r"Mandala Group", "Fenómeno", s)
    s = re.sub(r"Grupo Mandala", "Fenómeno", s)
    s = re.sub(r"sitio web oficial de Mandala", "sitio web oficial de Fenómeno", s)
    s = s.replace(
        'Los términos "FENÓMENO", "FENÓMENO", "nosotros"',
        'Los términos "Fenómeno", "nosotros"',
    )
    return s

NAV = r"""
<header class="fixed top-0 w-full z-50 glass-nav border-b border-white/5">
<nav class="flex flex-wrap justify-between items-center gap-4 px-6 sm:px-8 py-6 w-full max-w-7xl mx-auto" aria-label="Principal">
<a href="index.html" class="inline-flex items-center shrink-0 h-8 max-h-8 focus-visible:outline-offset-4" aria-label="Fenómeno — inicio">
<img src="assets/SVG/Logo.svg" alt="Fenómeno" width="200" height="60" class="h-8 w-auto max-w-[min(11rem,46vw)] object-contain object-left" decoding="async"/>
</a>
<div class="hidden md:flex items-center gap-8 font-headline font-bold text-sm">
<a class="text-[#e2dcc6] hover:text-[#E63912] transition-colors" href="index.html#inicio">Inicio</a>
<a class="text-[#e2dcc6] hover:text-[#E63912] transition-colors" href="index.html#manifiesto">Manifiesto</a>
<a class="text-[#e2dcc6] hover:text-[#E63912] transition-colors" href="index.html#curaduria">Curaduría</a>
<a class="text-[#e2dcc6] hover:text-[#E63912] transition-colors" href="contacto.html">Contacto</a>
</div>
<a href="index.html#inicio" class="bg-[#E63912] text-white px-6 py-2 rounded-full font-headline font-bold text-sm hover:opacity-90 shrink-0">Reservar mesa</a>
</nav>
</header>
"""

FOOT = r"""
<footer class="bg-[#1e1b1d] w-full py-10 px-8 border-t border-white/5">
<div class="max-w-7xl mx-auto flex flex-col gap-6">
<div class="flex flex-wrap gap-x-6 gap-y-2 justify-center md:justify-start font-headline font-bold text-xs uppercase tracking-widest">
<a class="text-[#e2dcc6]/70 hover:text-[#F5C412] transition-colors" href="https://www.instagram.com/fenomeno.es/" rel="noopener noreferrer" target="_blank">Instagram</a>
<a class="text-[#e2dcc6]/70 hover:text-[#F5C412] transition-colors" href="contacto.html">Contacto</a>
<a class="text-[#e2dcc6]/70 hover:text-[#F5C412] transition-colors" href="privacidad.html">Privacidad</a>
<a class="text-[#e2dcc6]/70 hover:text-[#F5C412] transition-colors" href="faqs.html">FAQs</a>
<a class="text-[#e2dcc6]/70 hover:text-[#F5C412] transition-colors" href="terminos.html">Términos y Condiciones</a>
<a class="text-[#e2dcc6]/70 hover:text-[#F5C412] transition-colors" href="cumplimiento-rgpd.html">Cumplimiento del RGPD</a>
</div>
<p class="font-body text-[10px] text-[#e2dcc6]/40 uppercase tracking-[0.3em] text-center md:text-left">© <span class="js-ano-legal">2026</span> Fenómeno</p>
</div>
</footer>
"""

YEAR_SCRIPT = """
<script>(function(){var n=document.querySelectorAll(".js-ano-legal"),y=String(new Date().getFullYear()),i;for(i=0;i<n.length;i++){n[i].textContent=y;}})();</script>
"""

HEAD = """<!DOCTYPE html>
<html class="dark" lang="es">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<link rel="icon" href="assets/SVG/Favicon-light.svg" type="image/svg+xml" media="(prefers-color-scheme: light)"/>
<link rel="icon" href="assets/SVG/Favicon.svg" type="image/svg+xml" media="(prefers-color-scheme: dark)"/>
<link rel="icon" href="assets/SVG/Favicon.svg" type="image/svg+xml"/>
<title>{title}</title>
<meta name="description" content="{description}"/>
<link rel="canonical" href="{canonical_url}"/>
<meta property="og:title" content="{og_title}"/>
<meta property="og:description" content="{description}"/>
<meta property="og:type" content="website"/>
<meta property="og:url" content="{canonical_url}"/>
<meta property="og:image" content="{og_image}"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta property="og:locale" content="es_ES"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{og_title}"/>
<meta name="twitter:description" content="{description}"/>
<meta name="twitter:image" content="{og_image}"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Epilogue:wght@700;800;900&amp;family=Newsreader:ital,wght@0,400;1,400&amp;family=Work+Sans:wght@400;500&amp;display=swap" rel="stylesheet"/>
<script>
      tailwind.config = {{ darkMode: "class", theme: {{ extend: {{ fontFamily: {{ headline: ["Epilogue"], body: ["Work Sans"], label: ["Newsreader"] }} }} }} }};
    </script>
<style type="text/tailwindcss">
        body {{ background-color: #131012; color: #e2dcc6; font-family: "Work Sans", sans-serif; background-image: radial-gradient(circle at center, #1c181a 0%, #131012 100%); background-attachment: fixed; }}
        .glass-nav {{ background: rgba(19, 16, 18, 0.8); backdrop-filter: blur(12px); }}
        a:focus-visible, button:focus-visible {{ outline: 2px solid #F5C412; outline-offset: 3px; }}
        .skip-link {{ position: absolute; left: 1rem; top: 1rem; z-index: 100; padding: 0.5rem 1rem; background: #E63912; color: #fff; font-weight: 700; font-size: 0.875rem; text-transform: uppercase; border-radius: 9999px; transform: translateY(-200%); transition: transform 0.2s ease; }}
        .skip-link:focus {{ transform: translateY(0); }}
        .legal-body h2 {{ font-family: Epilogue, sans-serif; font-weight: 800; font-size: 1rem; color: #F5C412; text-transform: uppercase; letter-spacing: 0.04em; margin-top: 1.75rem; margin-bottom: 0.5rem; }}
        .legal-body p, .legal-body li {{ font-size: 0.875rem; line-height: 1.65; color: rgba(226, 220, 198, 0.88); margin-bottom: 0.75rem; }}
        .legal-body a {{ color: #F5C412; text-decoration: underline; text-underline-offset: 2px; }}
        .legal-body b, .legal-body strong {{ color: #e2dcc6; font-weight: 700; }}
    </style>
</head>
<body class="antialiased">
<a class="skip-link font-headline" href="#contenido-principal">Saltar al contenido</a>
"""


def wrap_page(title: str, description: str, canonical_path: str, main_inner: str) -> str:
    base = FENOMENO_URL.rstrip("/")
    canonical_url = f"{base}/{canonical_path.lstrip('/')}"
    og_image = f"{base}{OG_IMAGE_PATH}"
    head_html = HEAD.format(
        title=title,
        description=description,
        canonical_url=canonical_url,
        og_title=title,
        og_image=og_image,
    )
    return (
        head_html
        + NAV
        + f'<main id="contenido-principal" class="pt-28 pb-20 px-6 sm:px-8 max-w-4xl mx-auto" tabindex="-1">\n{main_inner}\n</main>\n'
        + FOOT
        + YEAR_SCRIPT
        + "</body></html>"
    )


def main():
    priv_inner = (DIR / "_extracted_privacidad_inner.html").read_text(encoding="utf-8")
    if not priv_inner.lstrip().startswith("<"):
        priv_inner = "<p>" + priv_inner
    # Ancla cookies para enlaces desde el prototipo principal
    # Ancla #cookies: si el fragmento ya trae id="cookies", no sustituir.
    if '<h2 id="cookies">' not in priv_inner:
        priv_inner = priv_inner.replace(
            "<h2>4. Política de Cookies</h2>",
            '<h2 id="cookies">4. Política de Cookies</h2>',
            1,
        )
    priv_inner = fenomeno_legales_html(priv_inner)
    priv_main = f"""
<p class="font-label italic text-[#F5C412] text-lg mb-2">Información legal</p>
<h1 class="font-headline font-black text-3xl sm:text-4xl text-[#e2dcc6] uppercase tracking-tighter mb-4">Aviso de privacidad</h1>
<p class="text-sm text-[#e2dcc6]/70 mb-8 border-l-2 border-[#1266AB]/40 pl-4 leading-relaxed">Consultas sobre protección de datos (Fenómeno, Madrid): <a class="text-[#F5C412] underline" href="mailto:{FENOMENO_MAIL}">{FENOMENO_MAIL}</a>.</p>
<div class="legal-body text-justify">
{priv_inner}
</div>
"""
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "privacidad.html").write_text(
        wrap_page(
            "Política de privacidad — Fenómeno",
            "Privacidad Fenómeno Madrid: tratamiento de datos, cookies, RGPD y derechos. Contacto hola@fenomeno.bar. Sitio informativo.",
            "privacidad.html",
            priv_main,
        ),
        encoding="utf-8",
    )

    faq_sections = fenomeno_legales_html((DIR / "_faq_sections.html").read_text(encoding="utf-8"))
    faq_main = f"""
<p class="font-label italic text-[#F5C412] text-lg mb-2">Preguntas frecuentes</p>
<h1 class="font-headline font-black text-3xl sm:text-4xl text-[#e2dcc6] uppercase tracking-tighter mb-4">F.A.Q.S</h1>
<p class="text-sm text-[#e2dcc6]/70 mb-10 border-l-2 border-[#1266AB]/40 pl-4 leading-relaxed">Si te queda alguna duda, escríbenos a <a class="text-[#F5C412] underline" href="mailto:{FENOMENO_MAIL}">{FENOMENO_MAIL}</a>.</p>
<div class="space-y-2">
{faq_sections}
</div>
"""
    (OUT / "faqs.html").write_text(
        wrap_page(
            "FAQs — Fenómeno",
            "Preguntas frecuentes Fenómeno: reservas, edad mínima, bar Hi-Fi en Recoletos, horarios y contacto en Madrid.",
            "faqs.html",
            faq_main,
        ),
        encoding="utf-8",
    )

    term_inner = fenomeno_legales_html((DIR / "_extracted_terminos_inner.html").read_text(encoding="utf-8"))
    term_main = f"""
<p class="font-label italic text-[#F5C412] text-lg mb-2">Información legal</p>
<h1 class="font-headline font-black text-2xl sm:text-3xl text-[#e2dcc6] uppercase tracking-tighter mb-4 text-center">Términos y condiciones generales</h1>
<p class="text-sm text-[#e2dcc6]/70 mb-10 border-l-2 border-[#1266AB]/40 pl-4 leading-relaxed">Rigen el uso de este sitio web y complementan las condiciones que acuerdes al reservar o al consumir en el local (Madrid). Contacto: <a class="text-[#F5C412] underline" href="mailto:{FENOMENO_MAIL}">{FENOMENO_MAIL}</a>.</p>
<div class="legal-body text-justify overflow-x-auto">
{term_inner}
</div>
"""
    (OUT / "terminos.html").write_text(
        wrap_page(
            "Términos y condiciones — Fenómeno",
            "Condiciones de uso de fenomeno.bar y del local Fenómeno (Madrid). Propiedad intelectual, responsabilidad y ley española.",
            "terminos.html",
            term_main,
        ),
        encoding="utf-8",
    )

    # contacto.html se edita a mano en la raíz del repo (canales teléfono, correo, Instagram).
    print("OK: privacidad.html, faqs.html, terminos.html -> raiz del repo")


if __name__ == "__main__":
    main()
