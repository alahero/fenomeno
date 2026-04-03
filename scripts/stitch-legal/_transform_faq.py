# Convierte el <ul class="faq"> de Mandala a secciones semánticas para Fenómeno
import re
from pathlib import Path

def main():
    raw = Path(__file__).parent.joinpath("_extracted_faq_inner.html").read_text(encoding="utf-8")
    blocks = re.findall(
        r'<h6 class="question">(.*?)</h6>\s*<div class="answer">(.*?)</div>',
        raw,
        re.DOTALL,
    )
    parts = []
    for q, a in blocks:
        q = re.sub(r"\s+", " ", q.strip())
        a = a.strip()
        parts.append(
            f'<section class="faq-item border-b border-[#3a322f]/50 pb-8 mb-8 last:border-0">\n'
            f'<h2 class="font-headline font-bold text-[#E63912] text-sm uppercase tracking-wide mb-3">{q}</h2>\n'
            f'<div class="font-body text-[#e2dcc6]/80 text-sm leading-relaxed [&_a]:text-[#F5C412] [&_a]:underline [&_b]:text-[#e2dcc6]">{a}</div>\n'
            f"</section>"
        )
    Path(__file__).parent.joinpath("_faq_sections.html").write_text("\n".join(parts), encoding="utf-8")
    print("items", len(blocks))

if __name__ == "__main__":
    main()
