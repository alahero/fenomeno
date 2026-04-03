# Script puntual: extrae cuerpo legal desde HTML descargado de mandalatickets.com
import re
from pathlib import Path

base = Path(r"C:\Users\a_her\AppData\Local\Temp")
out_dir = Path(__file__).resolve().parent

def main():
    html = (base / "mt-priv.html").read_text(encoding="utf-8", errors="replace")
    m = re.search(
        r'privacypolicy-titulo[^>]*>([^<]+)</h2>\s*<p[^>]*>(.+?)</p>\s*</div>\s*</div>\s*</div>',
        html,
        re.DOTALL,
    )
    if m:
        inner = m.group(2)
        inner = re.sub(r"^<p>", "", inner, count=1)
        inner = re.sub(r"</p>\s*$", "", inner)
        (out_dir / "_extracted_privacidad_inner.html").write_text(inner, encoding="utf-8")
        print("privacidad", len(inner))

    faq_html = (base / "mt-faq.html").read_text(encoding="utf-8", errors="replace")
    m2 = re.search(r'<ul class="faq">(.*?)</ul>', faq_html, re.DOTALL)
    if m2:
        (out_dir / "_extracted_faq_inner.html").write_text(m2.group(1), encoding="utf-8")
        print("faq", len(m2.group(1)))

    th = (base / "mt-terminos.html").read_text(encoding="utf-8", errors="replace")
    m3 = re.search(r'termscondittions-texto">\s*<p[^>]*>(.+)', th, re.DOTALL)
    if m3:
        tinner = m3.group(1)
        end = tinner.find("</div>")
        if end > 0:
            tinner = tinner[:end]
        (out_dir / "_extracted_terminos_inner.html").write_text(tinner, encoding="utf-8")
        print("terminos", len(tinner))

if __name__ == "__main__":
    main()
