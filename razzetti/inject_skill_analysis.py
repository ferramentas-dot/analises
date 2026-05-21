"""Injeta a seção 'Análise completa (skill)' nos 16 cards YT alvo dentro
de analises/razzetti/index.html, sem regenerar o arquivo todo.

Usa markdown lib pra renderizar os .md da skill em HTML, depois encontra
cada card pelo data-id e insere o bloco após a copy-section.
"""
import re
from pathlib import Path

import markdown as _md

INDEX_PATH = Path(r"C:\Users\luana\Downloads\analises\razzetti\index.html")
ANALISES_IA_DIR = Path(r"C:\Users\luana\Downloads\Swipeoffers\swipe-kit\spy\ofertas-black\razzetti\5 - Analises IA")

YT_ANALISE_SKILL = {
    "zW3V0q0Fyd4": "Sistemas vs Metas",
    "qknqc_o5P9I": "Hormozi 50k 1 dia",
    "n7NjfUyMH00": "Mentalidad Imparable",
    "WebeLebbPtc": "Productividad",
    "RAv4QSHp8OM": "ClickUp Gestiono Equipo",
    "th-F7ghtQWQ": "Captar Clientes Agencia",
    "n7OBUjL9E3Q": "Setter Guia Definitiva",
    "WFE7mxPlO9U": "5min Aumentar Facturacion",
    "KIyucNH99Zg": "Negocio Funcione Sin Mi",
    "3oitOfg1mbM": "Productivo Organizado Empresario",
    "bZ8R-2dzfDA": "De 0 a 10k",
    "mgZn-bFI82M": "Cobra 2k por Cliente",
    "5CTI3t_in7s": "5 Pasos VSL Funnel",
    "CdE9VGv95MI": "Guion Closer de Venta",
    "M5E_9xitlqU": "Convierte Conversaciones en Ventas",
    "pNA13yIx7tI": "Razzetti Vende Humo",
}

CSS_BLOCK = """
  /* Análise completa da skill — injetado por inject_skill_analysis.py */
  .skill-analysis-section details {
    background: var(--bg);
    border: 1px solid #ef4444;
    border-radius: 6px;
    padding: 0;
  }
  .skill-analysis-section summary {
    cursor: pointer;
    padding: 10px 12px;
    font-size: 12.5px;
    color: #fca5a5;
    font-weight: 600;
    user-select: none;
    list-style: none;
  }
  .skill-analysis-section summary::-webkit-details-marker { display: none; }
  .skill-analysis-section summary::before {
    content: "▸ "; display: inline-block; transition: transform 0.15s ease; color: #ef4444;
  }
  .skill-analysis-section details[open] summary::before { transform: rotate(90deg); }
  .skill-analysis-section summary:hover { color: #fecaca; }
  .skill-analysis-section summary code {
    background: rgba(239,68,68,0.12); padding: 1px 6px; border-radius: 3px;
    font-size: 11px; color: #fca5a5;
  }
  .skill-analysis-content {
    padding: 14px 16px; border-top: 1px solid #ef4444;
    font-size: 13px; line-height: 1.65; color: var(--text);
    max-height: 600px; overflow-y: auto;
  }
  .skill-analysis-content h1 {
    font-size: 17px; margin: 0 0 12px; padding-bottom: 8px;
    border-bottom: 1px solid var(--border); color: var(--text);
  }
  .skill-analysis-content h2 {
    font-size: 14px; margin: 18px 0 8px;
    padding: 6px 10px; background: var(--surface-2);
    border-left: 3px solid #ef4444; border-radius: 4px; color: var(--text);
  }
  .skill-analysis-content h3 { font-size: 13.5px; margin: 12px 0 6px; color: var(--text); }
  .skill-analysis-content h4 {
    font-size: 12px; margin: 10px 0 4px; color: var(--muted);
    text-transform: uppercase; letter-spacing: 0.6px;
  }
  .skill-analysis-content p { margin: 0 0 10px; color: var(--text); }
  .skill-analysis-content ul, .skill-analysis-content ol { margin: 0 0 12px; padding-left: 20px; }
  .skill-analysis-content li { margin-bottom: 4px; }
  .skill-analysis-content strong { color: var(--text); font-weight: 700; }
  .skill-analysis-content code {
    background: var(--surface-2); padding: 1px 5px; border-radius: 3px;
    font-size: 12px; color: #fbbf24;
  }
  .skill-analysis-content blockquote {
    margin: 10px 0; padding: 8px 14px;
    background: var(--surface-2); border-left: 3px solid var(--muted);
    border-radius: 4px; color: var(--text); font-size: 12.5px;
  }
  .skill-analysis-content table {
    width: 100%; border-collapse: collapse; margin: 12px 0;
    font-size: 12.5px; background: var(--surface-2);
    border: 1px solid var(--border); border-radius: 6px; overflow: hidden;
  }
  .skill-analysis-content th, .skill-analysis-content td {
    padding: 6px 10px; border-bottom: 1px solid var(--border); text-align: left;
  }
  .skill-analysis-content th {
    background: var(--bg); color: var(--muted);
    text-transform: uppercase; font-size: 10.5px; letter-spacing: 0.4px;
  }
  .skill-analysis-content tr:last-child td { border-bottom: none; }
  .skill-analysis-content hr { border: none; height: 1px; background: var(--border); margin: 16px 0; }
  .skill-analysis-content a { color: var(--accent); text-decoration: none; }
  .skill-analysis-content a:hover { text-decoration: underline; }
"""

def load_html_analyses():
    result = {}
    for vid, slug in YT_ANALISE_SKILL.items():
        matches = list(ANALISES_IA_DIR.glob(f"*analise copy YT - {slug}.md"))
        if not matches:
            matches = [
                p for p in ANALISES_IA_DIR.glob("*.md")
                if slug.lower() in p.name.lower() and "analise copy YT" in p.name and " BH " not in p.name
            ]
        if not matches:
            print(f"[warn] não encontrei {vid} ({slug})")
            continue
        md = matches[0].read_text(encoding="utf-8")
        result[vid] = _md.markdown(md, extensions=["extra", "sane_lists", "tables"])
    return result


def inject_skill_section(html: str, analyses: dict) -> str:
    """Pra cada video alvo, encontra o fim da copy-section dentro do article
    e insere o bloco da skill-analysis-section depois."""
    new_html = html
    injected = 0
    for vid, analysis_html in analyses.items():
        # Padrão: <article data-id="VID"> ... <section class="copy-section"> ... </section>
        # Achar o article inteiro
        article_pattern = re.compile(
            rf'(<article class="card"[^>]*data-id="{re.escape(vid)}"[^>]*>.*?</article>)',
            re.DOTALL
        )
        m = article_pattern.search(new_html)
        if not m:
            print(f"[warn] card {vid} não encontrado no HTML")
            continue
        original_article = m.group(1)  # preservar pra .replace()
        article = original_article
        # Se já tem skill-analysis-section, remove pra re-inserir com conteúdo atualizado
        if 'class="skill-analysis-section"' in article:
            article = re.sub(
                r'\s*<section class="skill-analysis-section">.*?</section>',
                '',
                article,
                flags=re.DOTALL,
                count=1,
            )
        # Achar o fim da copy-section: </section> que fecha a primeira <section class="copy-section">
        # Vamos procurar por '<p class="caption-quote">' (que está dentro da copy-section, perto do fim)
        # ou se não houver caption, procurar por '<div class="save-state" data-for="copy::VID"...>não editado</div>'
        new_block = f'''
        <section class="skill-analysis-section">
          <details>
            <summary>📺 Ver análise completa (9 blocos · skill <code>analise-copy-youtube</code>)</summary>
            <div class="skill-analysis-content">{analysis_html}</div>
          </details>
        </section>'''
        # Inserir após o </section> da copy-section
        # Padrão: </section>\n        {transcript-section ou outro}
        # Vou achar a copy-section dentro do article e inserir após ela
        copy_end_pattern = re.compile(
            r'(<section class="copy-section">.*?</section>)',
            re.DOTALL
        )
        new_article = copy_end_pattern.sub(lambda x: x.group(1) + new_block, article, count=1)
        if new_article == article:
            print(f"[warn] {vid} não conseguiu inserir (copy-section não casou)")
            continue
        new_html = new_html.replace(original_article, new_article, 1)
        injected += 1
    print(f"Injetadas {injected} análises da skill")
    return new_html


def inject_css(html: str) -> str:
    if "skill-analysis-section details" in html:
        print("[skip] CSS da skill já presente")
        return html
    # Inserir antes de </style> (primeiro fechamento)
    return html.replace("</style>", CSS_BLOCK + "\n</style>", 1)


def main():
    html = INDEX_PATH.read_text(encoding="utf-8")
    analyses = load_html_analyses()
    print(f"Carreguei {len(analyses)}/16 análises")
    html = inject_css(html)
    html = inject_skill_section(html, analyses)
    INDEX_PATH.write_text(html, encoding="utf-8")
    print(f"WROTE: {INDEX_PATH}")


if __name__ == "__main__":
    main()
