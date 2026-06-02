---
oferta: Thiago Reis / Growth Machine
funil: Desafio "5 a 50 Clientes em 20 Dias"
tipo: origem de tráfego — confirmação de campanha paga
data: 2026-06-02
fonte: Biblioteca de Anúncios da Meta + código da LP + criativos coletados
status: ATIVO (confirmado 02/06/2026)
relacionados:
  - "[[recon-ecossistema]]"
  - "[[razzetti-template-canonico]]"
---

# Origem do tráfego — Funil "Desafio: 5 a 50 Clientes em 20 Dias"

## TL;DR
A **origem principal do tráfego pago** do Thiago Reis **não** é o domínio institucional `growthmachine.com.br` (0% pago, tráfego orgânico em queda). É um **domínio dedicado** — `lp.desafio1a10milhoes.com.br/v2` — montado só pra rodar **Meta Ads**. **Está ativo** (confirmado em 02/06/2026).

## Origem principal: META ADS (Facebook + Instagram)
- **Página anunciante:** *Thiago Reis - Growth Machine*
- **Status:** 🔴 **ATIVO** — Biblioteca de Anúncios da Meta retorna dezenas de anúncios com status "Ativo" (20+ criativos só no primeiro carregamento da busca).
- **Longevidade dos criativos:** vídeos coletados estão nomeados **"AD 30 a 65 dias ativos"** → campanha **escalada e sustentada há 1–2 meses**. Anúncio que sobrevive 30–65 dias é sinal clássico de **funil vencedor** (ROI positivo segurando o investimento).
- **Formato dominante:** **vídeo** (13 criativos de vídeo coletados vs. 1 print de imagem) — VSL-style/depoimento.
- **Copy padrão do anúncio:** *"Conquiste de 5 a 50 clientes em 20 dias com um método prático, scripts prontos e uma estratégia clara para aplicar no seu comercial."*
- **Prova:** print em `1 - Ads/meta-ad-library-desafio.png`; criativos em `2 - Paginas/desafio 50 clientes - meta ads/`.

## Fluxo do funil
```
Meta Ads (FB/IG, vídeo)  →  LP lp.desafio1a10milhoes.com.br/v2  →  VSL  →  quiz de qualificação  →  checkout HOTMART (pay.hotmart.com)  →  R$97  →  garantia 7 dias
```

## Evidências técnicas na LP (/v2)
- **Google Tag Manager:** `GTM-NW8KJ3PR` (orquestra os pixels)
- **Facebook Pixel:** `connect.facebook.net` presente (rastreamento de conversão Meta)
- **Checkout:** `launcher.hotmart.com` → produto na **Hotmart**
- **Sem footprint de SEO** (LP é shell JS de ~5KB renderizado no client) → confirma que a LP **não** vive de orgânico; é destino de mídia paga.
- `<title>`: "Desafio: 5 a 50 Clientes em 20 Dias | Growth Machine"

## Por que isso importa pro spy
- O domínio institucional engana: SimilarWeb mostra 0% pago e tráfego caindo -23,6%. **A aquisição real roda neste domínio paralelo**, invisível pro SimilarWeb da home.
- Esse é o **front-end pago** (R$97 tripwire) que alimenta a escada de valor Growth Machine (Growth Play, imersões, Growth Way high-ticket via diagnóstico).
- Funil-irmão coletado no mesmo padrão: **Scanner de Vendas + Desafio** (ver `2 - Paginas/funil scanner de vendas + desafio 50 clientes - meta ads/`).

## Método de verificação (replicável)
1. Biblioteca de Anúncios Meta: busca por "desafio 5 a 50 clientes" / "growth machine", país BR, status Ativo.
2. Grep no HTML da LP por `connect.facebook.net`, `GTM-`, `hotmart` → confirma pixel + checkout.
3. Nome dos arquivos de criativo ("X dias ativos") → estima longevidade da campanha.
