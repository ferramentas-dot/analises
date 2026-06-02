#!/usr/bin/env python3
"""
Regenera os 2 textareas (framework + analise geral) em cada card de Meta-Ads
a partir dos .md atualizados.
"""
import re, sys, html
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

ROOT_MD = Path(r"c:/Users/luana/Downloads/Swipeoffers/swipe-kit/spy/ofertas-black/razzetti/ads_transcripts/analises")
INDEX = Path(r"C:/Users/luana/Downloads/analises/razzetti/index.html")

MAPPING = {
    "20DATV-ENGAJ-Razetti-Multiplos-ads": "Aquecimento_perfil_e_engajamento/20DATV - ENGAJ - Razetti - Multiplos ads.md",
    "37DATV-ENGAJ-Razetti-Multiplos-ads": "Aquecimento_perfil_e_engajamento/37DATV - ENGAJ - Razetti - Multiplos ads.md",
    "37DATV-ENGAJ-Razetti-Multiplos-ads-2": "Aquecimento_perfil_e_engajamento/37DATV - ENGAJ - Razetti - Multiplos ads (2).md",
    "37DATV-ENGAJ-Razetti-Multiplos-ads-3": "Aquecimento_perfil_e_engajamento/37DATV - ENGAJ - Razetti - Multiplos ads (3).md",
    "73DATV-ENGAJ-Razzeti-Multiplos-ads": "Aquecimento_perfil_e_engajamento/73DATV - ENGAJ - Razzeti - Multiplos ads.md",
    "73DATV-ENGAJ": "Aquecimento_perfil_e_engajamento/73DATV - ENGAJ.md",
    "79DATV-ENGAJ": "Aquecimento_perfil_e_engajamento/79DATV - ENGAJ.md",
    "45DATV-TRIP-FREE": "Bluehackers_biblio_-_Trip_Free/45DATV - TRIP FREE.md",
    "55DATV-TRIP-FREE": "Bluehackers_biblio_-_Trip_Free/55DATV - TRIP FREE.md",
    "55DATV-TRIP-FREE-BIB-BLUE-1": "Bluehackers_biblio_-_Trip_Free/55DATV - TRIP FREE - BIB BLUE (1).md",
    "55DATV-TRIP-FREE-BIB-BLUE-2": "Bluehackers_biblio_-_Trip_Free/55DATV - TRIP FREE - BIB BLUE (2).md",
    "AD55DATV-BLUEHACKERS-BIBLIO": "Bluehackers_biblio_-_Trip_Free/AD55DATV - BLUEHACKERS BIBLIO.md",
    "48DATV-COMERCIAL-VSL-4DUP": "Funil_comercial_com_vsl/48DATV - COMERCIAL VSL - 4DUP.md",
    "48DATV-COMERCIAL-VSL": "Funil_comercial_com_vsl/48DATV - COMERCIAL VSL.md",
    "52DATV-COMERCIAL-VSL": "Funil_comercial_com_vsl/52DATV - COMERCIAL VSL.md",
    "64DATV-COMERCIAL-VSL": "Funil_comercial_com_vsl/64DATV - COMERCIAL VSL.md",
    "65DATV-COMERCIAL-VSL": "Funil_comercial_com_vsl/65DATV - COMERCIAL VSL.md",
    "66DATV-COMERCIAL-VSL": "Funil_comercial_com_vsl/66DATV - COMERCIAL VSL.md",
    "59DATV-Trip-27-USD": "Funil_tripware/59DATV - Trip 27$.md",
    "59DATV-Trip-27": "Funil_tripware/59DATV - Trip 27.md",
    "69DATV-TRIP-27-USD": "Funil_tripware/69DATV - TRIP 27$.md",
    "69DATV-TRIP-27": "Funil_tripware/69DATV - TRIP 27$,.md",
}

def md_to_plain(md: str) -> str:
    lines = md.splitlines()
    out = []
    title = None
    skip_until_section = True

    for raw in lines:
        if skip_until_section:
            if raw.startswith("# ") and title is None:
                title = raw[2:].strip()
                continue
            if raw.startswith("## "):
                skip_until_section = False
            else:
                continue

        line = raw
        m = re.match(r"^## (.+)$", line)
        if m:
            header = m.group(1).strip()
            up = header.upper()
            if out and out[-1] != "":
                out.append("")
            out.append(up)
            out.append("─" * max(3, min(len(up), 60)))
            out.append("")
            continue
        m = re.match(r"^### (.+)$", line)
        if m:
            out.append("")
            out.append(m.group(1).strip().upper())
            out.append("")
            continue
        if re.match(r"^---\s*$", line):
            continue
        bm = re.match(r"^(\s*)([-*])\s+(.+)$", line)
        if bm:
            indent_level = len(bm.group(1)) // 2
            content = bm.group(3)
            prefix = "    " * indent_level + "• "
            line = prefix + content
        line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", line)
        line = re.sub(r"\*\*([^*]+)\*\*", r"\1", line)
        line = re.sub(r"\*([^*]+)\*", r"\1", line)
        line = re.sub(r"`([^`]+)`", r"\1", line)
        line = line.replace("**", "").replace("`", "")
        out.append(line)

    result = []
    blank_streak = 0
    for ln in out:
        if ln.strip() == "":
            blank_streak += 1
            if blank_streak <= 2:
                result.append(ln)
        else:
            blank_streak = 0
            result.append(ln)
    text = "\n".join(result).strip() + "\n"
    if title:
        text = f"{title}\n\n" + text
    return text


def split_analise_geral(md: str):
    pattern = re.compile(
        r'(\n## 9\. An[áa]lise geral[^\n]*\n)(.*?)(?=\n## \d+\.|\Z)',
        flags=re.DOTALL | re.IGNORECASE
    )
    m = pattern.search(md)
    if not m:
        return md, None
    analise_geral_full = m.group(1) + m.group(2)
    framework_md = md[:m.start()] + md[m.end():]
    return framework_md, analise_geral_full


html_text = INDEX.read_text(encoding='utf-8')
updated_main = 0
updated_ag = 0

for base_id, rel_md in MAPPING.items():
    md_path = ROOT_MD / rel_md
    if not md_path.exists():
        print(f"WARN missing: {md_path}", file=sys.stderr)
        continue
    md_text = md_path.read_text(encoding='utf-8')
    framework_md, analise_geral_md = split_analise_geral(md_text)

    framework_plain = md_to_plain(framework_md)
    framework_esc = html.escape(framework_plain, quote=True)
    storage_key_main = f"copy::ad-{base_id}"
    main_pat = re.compile(
        r'(data-storage-key="' + re.escape(storage_key_main) + r'"\s+data-default=")([^"]*)(")',
        flags=re.DOTALL
    )
    new_html, n = main_pat.subn(lambda m: m.group(1) + framework_esc + m.group(3), html_text)
    if n:
        html_text = new_html
        updated_main += 1

    if analise_geral_md is not None:
        ag_plain = md_to_plain(analise_geral_md)
        ag_esc = html.escape(ag_plain, quote=True)
        storage_key_ag = f"copy::ad-{base_id}-analise-geral"
        ag_pat = re.compile(
            r'(data-storage-key="' + re.escape(storage_key_ag) + r'"\s+data-default=")([^"]*)(")',
            flags=re.DOTALL
        )
        new_html, n = ag_pat.subn(lambda m: m.group(1) + ag_esc + m.group(3), html_text)
        if n:
            html_text = new_html
            updated_ag += 1
        else:
            print(f"WARN no AG textarea for: {base_id}", file=sys.stderr)

INDEX.write_text(html_text, encoding='utf-8')
print(f"OK {updated_main} textareas principais atualizados")
print(f"OK {updated_ag} textareas de Analise Geral atualizados")
