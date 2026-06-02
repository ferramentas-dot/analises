#!/usr/bin/env python3
"""
Reescreve o bloco 9 (Analise geral) de 21 .md em PT plano - sem jargao.
Glossario: moderacao -> 'Facebook bloquear / regras do Facebook',
hook -> 'abertura', CTA -> 'pedido', lead -> 'pessoa que ve',
publico quente/frio -> 'quem ja conhece / quem nunca viu',
retarget -> 'mostrar de novo pra quem ja viu', etc.
"""
import re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(r"c:/Users/luana/Downloads/Swipeoffers/swipe-kit/spy/ofertas-black/razzetti/ads_transcripts/analises")

REWRITES = {
    "Aquecimento_perfil_e_engajamento/20DATV - ENGAJ - Razetti - Multiplos ads.md": """## 9. Análise geral

Anúncio curto, em formato de lista. Entrega seis dicas práticas em meio minuto.

A ideia é simples: **você está perdendo dinheiro porque fala as palavras erradas — o Razzetti tem as palavras certas**.

Funciona porque quem assiste sai com a sensação de "aprendi alguma coisa" sem ter pago nada. É exatamente o que um anúncio de engajamento precisa entregar pra fazer a pessoa querer seguir.

A lista resolve o problema de "como prender atenção sem contar uma história". Cada item da lista é um motivo novo pra continuar assistindo.

**O que dá pra repetir:** o formato "não diga X, diga Y" pode ser usado mil vezes. O próximo anúncio pode ser sobre liderança, gestão, contratação — sempre com o mesmo molde.

**O Facebook bloquearia esse anúncio?** Não. Não tem palavra arriscada — é só conteúdo de coaching.

O único risco é que o Razzetti **não pede pra pessoa seguir falando**. Ele depende 100% do botão de "seguir" na tela e do algoritmo do Instagram pra transformar atenção em novo seguidor.
""",

    "Aquecimento_perfil_e_engajamento/37DATV - ENGAJ - Razetti - Multiplos ads.md": """## 9. Análise geral

Esse é o **anúncio mais bem construído** dos 7 anúncios de engajamento, se a gente olhar pelo critério de venda.

A abertura bate numa dor que todo mundo tem (humilhação social). Logo depois, ele vira o jogo e coloca a responsabilidade na pessoa que tá assistindo. O corpo entrega o método + duas técnicas com nome + uma autoridade implícita ("comando biológico"). Fecha com uma frase forte que dá pra printar e com um pedido claro de seguir.

A ideia é simples: **presença social não é dom, é técnica — e o Razzetti tem o passo a passo**.

**O que dá pra repetir:** a estrutura "cena de dor social do dia a dia → vira o jogo → 2 técnicas práticas → frase de princípio" é um molde infinito pra coaching de habilidades comportamentais. Você troca só a cena de abertura e roda.

**O Facebook bloquearia esse anúncio?** Não. Está limpo.

O único risco é que o pedido de "me siga" aparece só no final. Se o vídeo for cortado antes do ponto típico em que 75% das pessoas largam, o seguidor se perde.
""",

    "Aquecimento_perfil_e_engajamento/37DATV - ENGAJ - Razetti - Multiplos ads (2).md": """## 9. Análise geral

O formato de encenação é o **mais diferente do grupo** de anúncios de engajamento. Em vez do Razzetti ensinar olhando pra câmera, ele atua a cena.

É uma aposta arriscada porque depende da audiência entender o jogo dos dois personagens sem narração explicando. Mas funciona: cada par "chefe ruim vs líder bom" é um motivo novo pra continuar assistindo.

A ideia é "**liderar não é mandar, é cuidar enquanto exige**" — entregue mostrando, não falando.

**O que dá pra repetir:** o formato de comparação atuada gera muito engajamento porque parece conteúdo, não anúncio.

**O Facebook bloquearia esse anúncio?** Não. Está ok.

O risco prático foi **resolvido pelo visual**: as etiquetas fixas **JEFE** e **LÍDER** acima da cabeça de cada personagem (com o Razzetti dobrado em tela dividida) eliminam qualquer dúvida. Quem tá vendo entende o jogo no primeiro segundo, sem precisar nem ouvir o áudio.

O peso da entrega vai todo pra produção: a edição que coloca os dois Razzetti na mesma cena + as etiquetas sempre na tela + a legenda amarela alinhada com quem está falando. É um anúncio caro de produzir — e essa é justamente a defesa contra cópias baratas.
""",

    "Aquecimento_perfil_e_engajamento/37DATV - ENGAJ - Razetti - Multiplos ads (3).md": """## 9. Análise geral

Anúncio de indicação de livros que faz duas coisas ao mesmo tempo: entrega valor real (3 livros bons) **E** posiciona o Razzetti como coach "sério" que ataca o coaching motivacional superficial.

A abertura combina três elementos: número (3 livros) + benefício comparativo (à frente de 99%) + prazo (fim do ano). É uma das construções mais ricas dos 7 anúncios de engajamento.

A ideia é "**leia o que importa e estará à frente**". E o truque de **falar o argumento antes de revelar o título** é o melhor recurso de escrita do grupo.

**O que dá pra repetir:** o molde pode ser usado pra indicação de qualquer coisa. E o ataque ao "superficial" filtra exatamente o tipo de pessoa que paga caro por mentoria — alguém que paga $10 mil dólares por mentoria não compra de coach motivacional.

**O Facebook bloquearia esse anúncio?** Não. Está limpo.

O único risco é que **sem ganchos no meio** entre um livro e outro, quem tá assistindo pode largar o vídeo antes dos 30 segundos.
""",

    "Aquecimento_perfil_e_engajamento/73DATV - ENGAJ - Razzeti - Multiplos ads.md": """## 9. Análise geral

Anúncio de pura ressonância emocional. **Sem pedido pra seguir, sem método com nome, sem prova externa**.

Funciona como ímã pra quem se identifica — e tem muita gente que se reconhece em pelo menos uma das 10 frases.

A ideia é "**ser extremo em virtudes te enfraquece — equilíbrio é maturidade**". Filosoficamente faz sentido, mas como peça de venda é raso. Não tem promessa, não tem técnica, não tem resultado.

**O que dá pra repetir:** o formato é muito bom pra screenshot e pra compartilhar — gera muitos salvamentos e compartilhamentos no Instagram.

**O Facebook bloquearia esse anúncio?** Não. Está limpo.

**Problema grave:** sem o Razzetti pedir nada (seguir, salvar, compartilhar), a identificação da pessoa não vira ação. O botão visual cobre uma parte, mas num coaching de produto caro o Razzetti deveria pedir o "seguir" falando.

É **o anúncio mais fraco do grupo** quando o critério é venda direta. Pode funcionar bem na métrica de salvamento e compartilhamento orgânico.
""",

    "Aquecimento_perfil_e_engajamento/73DATV - ENGAJ.md": """## 9. Análise geral

Anúncio de história do fundador que aposta **tudo** na proximidade afetiva entre o público e o Razzetti.

Quem já segue ele consome com prazer. Quem nunca viu o Razzetti larga o vídeo em segundos — porque não tem promessa, método, nada em jogo nem pedido pra seguir.

A ideia é "**vim do nada, segue minha jornada**" — história clássica de fundador. Funciona em remarketing (mostrar o anúncio de novo pra gente que já viu a marca) e pra quem já conhece. Falha pra quem ainda não conhece.

**O que dá pra repetir:** o uso de objetos físicos como prova (a lousa, o cheque, a tela preta de fundo) é genial. Torna a história concreta, palpável.

**O Facebook bloquearia esse anúncio?** Não, tá ok pelas regras do Facebook. Mas na prática o anúncio sangra porque **falta uma abertura forte, uma frase logo depois que segure e um pedido pra seguir falado**.

Numa conta de anúncios pagos, esse criativo só justifica orçamento pra **quem já conhece o Razzetti**. Pra quem nunca viu, é desperdício de dinheiro.
""",

    "Aquecimento_perfil_e_engajamento/79DATV - ENGAJ.md": """## 9. Análise geral

Anúncio curto e muito bem construído.

A abertura é uma afirmação que vai contra o que o mercado acredita — e isso faz a pessoa parar de rolar a tela, porque o cérebro estranha. Logo depois, ele filtra quem é o público certo. O corpo entrega o método com nome (filtragem) + comparação direta entre cliente barato e cliente premium. Fecha com uma frase forte e um pedido condicional que diz exatamente o que a pessoa ganha se seguir.

A ideia é "**preço alto não é arrogância, é seleção**" — manifesto típico de quem vende produto caro.

**O que dá pra repetir:** a estrutura "abertura contra o senso comum → como é o erro → método com nome → como é o jeito certo → frase forte → pedido com recompensa" é um molde de manifesto que pode ser usado em qualquer assunto.

**O Facebook bloquearia esse anúncio?** Não. Está limpo.

O pedido "me segue se quer aprender como" é a **melhor formulação dos 7 anúncios** de engajamento. Deveria virar o padrão pros próximos criativos do funil.
""",

    "Bluehackers_biblio_-_Trip_Free/45DATV - TRIP FREE.md": """## 9. Análise geral

É um anúncio que mira gente que JÁ tá na lista de email do Razzetti mas ainda não comprou nada caro. Ele usa a biblioteca gratuita como isca pra reaquecer essa pessoa.

A ideia é simples: **te entrego valor primeiro, você confia depois**.

Razzetti monta o anúncio em três tempos:
1. Identifica quem é ("estás en mi lista")
2. Tira a objeção da venda ("no te voy a vender nada")
3. Empilha o que você ganha, usando o preço de um produto dele mesmo como referência (mentoria de 25 mil dólares)

Isso funciona porque, em vez de usar uma referência cultural conhecida (coisa que produto caro dificilmente tem), ele usa **a própria autoridade dele + a lógica de "primeiro eu te dou, depois você me dá"**.

O que faz esse anúncio escalar:
- Abertura que já filtra no áudio (separa quem é da lista)
- Logo depois, ele tira a objeção da venda
- Três pedidos pra clicar espalhados sem cansar
- Deixa o motivo claro

**O que pode quebrar nas regras do Facebook:** ele cita muitos valores concretos de renda ("10.000", "100.000", "25.000"). Em conta de anúncios sem histórico, isso é sinal vermelho pro filtro que o Facebook usa pra travar promessas de "ganhar dinheiro".

Razzetti tem conta aquecida, então passa. Mas se for copiar em conta nova, precisa trocar os números por frase mais genérica (tipo "escalar tu negocio al próximo nivel" no lugar das cifras).
""",

    "Bluehackers_biblio_-_Trip_Free/55DATV - TRIP FREE.md": """## 9. Análise geral

Esse anúncio troca quem fala (sai Razzetti, entra Sol) mas mantém a mesma lógica de "te dou primeiro, você confia depois".

A jogada é fazer a Sol virar um **rosto conhecido** no feed da pessoa. Quanto mais ela vê a Sol, menos resistência tem pra clicar.

A ideia aqui é: **muito conteúdo de valor + sensação de fazer parte de um movimento maior** ("elevar la región").

Esse anúncio é diferente do 45DATV em dois pontos:
- Não usa um conceito-método com nome (tipo o "dominó" do outro)
- Troca isso por uma lista pura de coisas + uma causa coletiva

O que faz esse anúncio funcionar:
- Abertura que filtra logo no início ("Coaches Infoproductores")
- Reconhecimento de um rosto recorrente (Sol)
- Repete a palavra "gratis" várias vezes pra fixar

O que perde força:
- Não tem método com nome
- O primeiro pedido pra clicar demora pra aparecer
- Tem uma incongruência sutil ("mis directivos" na boca da Sol, sendo que ela não é diretora)

**Risco com as regras do Facebook:** é o mesmo do 45DATV — muitos números de renda concretos ("100.000 dólares al mes", "un millón de dólares al mes"). Passa em conta aquecida, quebra em conta nova porque o Facebook trava promessas explícitas de dinheiro.
""",

    "Bluehackers_biblio_-_Trip_Free/55DATV - TRIP FREE - BIB BLUE (1).md": """## 9. Análise geral

É um anúncio em formato de tour visual da biblioteca. O que ancora tudo é um verbo bizarro: **"subornarte épicamente"**. Essa palavra estranha é o que faz o anúncio se destacar no meio dos outros.

A ideia é: **eu preciso TANTO te ajudar que vou usar a palavra mais agressiva possível pra te entregar valor de graça**.

A escolha de "subornar" é arriscada mas inteligente. Ela transforma a pergunta "por que de graça?" em "ele tá tão desesperado pra provar que vai me dar tudo".

É uma inversão de poder: em vez da pessoa se sentir vendida, ela se sente quem decide.

O que faz esse anúncio funcionar:
- O verbo estranho ("subornarte épicamente")
- A escada de promessas (primeiro 10-20k, depois 100k)
- Detalhes específicos que dão sensação de realidade (tipo "2 horas y 22 minutos")

O que precisa cuidar:
- O anúncio só faz sentido com a gravação da tela por cima. Sem visual, ele perde uns 40% da força, porque palavras como "aquí" e "acá" ficam soltas
- Tem um único pedido pra clicar, no final. Isso só funciona se a gravação da tela segurar a atenção até lá

**Risco com as regras do Facebook:** dobrado. A palavra "subornar" (associada a corrupção em alguns filtros) mais os números de renda explícitos podem fazer o Facebook bloquear ou limitar a entrega do anúncio.
""",

    "Bluehackers_biblio_-_Trip_Free/AD55DATV - BLUEHACKERS BIBLIO.md": """## 9. Análise geral — Trade-off

**O que essa variante ganha:**
- **Alcance maior:** o AD55 não exclui quem já fatura 100k (esse pessoal ainda pode desconfiar do Razzetti). Pega desconfiança de qualquer pessoa, em qualquer faixa de faturamento.
- **Menor risco no Facebook:** tira uma menção de número de renda da abertura (deixa só no corpo do anúncio). O filtro do Facebook que trava promessas de "ganhar dinheiro" tem menos motivo pra bloquear logo na primeira varredura.

**O que essa variante perde:**
- **Menos peso emocional:** "no confías en mi" é uma coisa abstrata. "No consigues 100.000" é uma dor concreta, que dá pra medir, que a pessoa se identifica. Quem tá com a dor concreta clica com mais força.

**A emoção principal muda:**
- Original = sensação de não estar à altura ("ainda não cheguei lá").
- Variante = desconfiança ("não acredito nele").
- Essa emoção da variante é mais leve, mais defensiva. Funciona melhor pra quem nunca viu o Razzetti, que ainda não consumiu muito conteúdo dele.
""",

    "Funil_comercial_com_vsl/48DATV - COMERCIAL VSL.md": """## 9. Análise geral

Esse é o **anúncio principal** do funil. É praticamente um mini vídeo de vendas dentro de um anúncio pago.

O Razzetti aposta que quem aguenta os 2 minutos e 30 segundos de explicação do que ele entrega é exatamente quem vai agendar a call.

A ideia é forte: **"não te falta esforço, te falta o sistema completo — e eu tenho as 4 partes que cobrem 100% do que tá faltando"**.

Cada uma das 4 partes puxa a próxima. E cada caso real costura uma objeção com uma prova.

O que funciona bem é a **estrutura em pedaços** — dá pra cortar em 4 mini-anúncios, um por parte, e testar cada um separado.

O que NÃO funciona é o tamanho cru. Pra quem nunca te viu, 2 minutos e meio sai caro demais no custo do anúncio.

Esse anúncio funciona melhor pra mostrar de novo pra quem já viu o vídeo de venda ou a página do produto, e pra audiências parecidas com compradores reais.

**Risco com as regras do Facebook:** as promessas de dinheiro diretas ($10k-$100k por mês, $48k num mês só) são o ponto frágil. Passa hoje, mas é o tipo de anúncio que cai em revisão manual do Facebook de vez em quando.
""",

    "Funil_comercial_com_vsl/48DATV - COMERCIAL VSL - 4DUP.md": """## 9. Análise geral

Esse anúncio serve pra **tirar o medo** da pessoa, não pra atrair gente nova.

A ideia é uma só: quem já viu o Razzetti, já pensou em agendar, mas travou no "será que vão me forçar a comprar?" — esse anúncio responde direto: "não, nem precisa comprar. Vem só conhecer".

Tudo no texto aponta pra isso. A abertura é a voz interna da própria pessoa. Logo depois, ele desarma a objeção. No corpo, dá permissão pra pessoa dizer não. E o pedido pra agendar fica parecendo mais um convite pra um café do que uma venda.

Funciona porque coaching de preço alto é jogo de confiança. E a maior barreira pra agendar uma call é o medo de sofrer pressão.

O que funciona bem aqui é a **baixa pressão dentro de um funil onde a call faz o trabalho pesado**.

O que NÃO funciona é usar esse anúncio pra atrair gente que ainda não te conhece. Sem prova, vira só "agenda".

Provavelmente esse anúncio roda pra mostrar de novo pra quem já viu o vídeo de venda ou a página do produto e não comprou.

**Risco com as regras do Facebook:** baixo. Não tem promessa direta de dinheiro nem número de ganho nesse anúncio.
""",

    "Funil_comercial_com_vsl/52DATV - COMERCIAL VSL.md": """## 9. Análise geral

Esse anúncio serve pra **quebrar objeção com um tom diferente**.

O humor abre a pessoa desconfiada que já tá imune a guru sério. Depois ele vira a chave pro sério e entra com prova pesada. Fecha com "tira o risco" (*"¿qué tienes para perder?"*).

A ideia é: **"eu reconheço sua desconfiança e te dou o motivo lógico pra superar"**.

Funciona porque junta duas coisas: quebra de padrão (humor é raro nesse nicho) + muitos números reais.

O que funciona bem é a **média contando todo mundo** — é uma das frases mais fortes em prova social pra coaching. Porque já corta a desculpa "ah, vocês só mostram os melhores".

O que NÃO funciona tão bem é depender do humor. Se a edição erra o timing, vira vergonha alheia.

**Risco com as regras do Facebook:** baixo. Humor que ri de si mesmo não dispara alerta do Facebook pra conteúdo sensível.
""",

    "Funil_comercial_com_vsl/64DATV - COMERCIAL VSL.md": """## 9. Análise geral

Esse anúncio **ataca um jeito antigo de fazer as coisas**.

A ideia é: **"o que você faz não funciona mais, eu tenho o que funciona agora"**.

Funciona porque coach que faz lançamento vive a dor da roleta russa — não sabe se o próximo lançamento vai dar dinheiro ou não.

O Razzetti diz qual é a dor (estresse + não ter previsibilidade) e oferece o oposto (paz + dá pra prever) num arco curto.

E empilha prova ($300 milhões gerados + $10 milhões próprios + 8 anos de mercado + 300 casos) pra fechar.

O que funciona bem é a **abertura "X morreu, foi substituído por Y"**: simples, fácil de copiar, e ela mesma já segmenta o público sozinha.

O que NÃO funciona é a promessa de $300 milhões se rodar em escala maior — vai cair em revisão do Facebook cedo ou tarde.

**Risco com as regras do Facebook:** passa hoje, mas é o anúncio mais arriscado dos seis. As cifras altas de receita disparam o filtro que o Facebook usa pra travar promessas de "ganhar dinheiro".

A frase "ecosistema hiper orgánico de anuncios" tá mal escrita (mistura "orgânico" com "anúncios pagos", que NÃO é orgânico) e merece reescrita.
""",

    "Funil_comercial_com_vsl/65DATV - COMERCIAL VSL.md": """## 9. Análise geral

Esse anúncio é **prova social pura**.

A ideia é: **"não sou eu quem fala, é uma cliente que tava no mesmo lugar que você"**.

Funciona porque coaching de preço alto tem barreira de confiança altíssima. E nada quebra essa barreira como ouvir alguém igual a você falando.

O fato dela ser ESPECÍFICA nas ações que tomou (subiu o ticket de $1.500 pra $2.500) faz a pessoa sentir que dá pra fazer igual. Ela pensa: "eu posso fazer isso amanhã".

O que funciona bem é a **sensação de gravação real** — entra no meio da fala, sem polimento, com errinhos naturais ("ni acá al mes"). É o formato que CONSTRÓI confiança aos poucos.

O que NÃO funciona é depender 100% do depoimento sem ter um pedido falado pra agendar. A cliente não puxa a venda, só serve de prova.

**Risco com as regras do Facebook:** baixo. Depoimentos com cliente identificável são a categoria que menos dá problema com o Facebook.
""",

    "Funil_comercial_com_vsl/66DATV - COMERCIAL VSL.md": """## 9. Análise geral

Esse anúncio **muda a forma como a pessoa se enxerga**.

A ideia é: **"você tá brincando de tática, eu te ensino estratégia"**.

Funciona porque mexe com o orgulho de quem tem negócio — ninguém quer se ver como amador que só faz tática.

O Razzetti combina três coisas: autoridade emprestada (o visual militar), ataque com nome aos métodos comuns (stories e ManyChat), e argumento de contas básicas do negócio (LTV — o quanto cada cliente vale ao longo do tempo).

Resultado: um anúncio que filtra muito bem por nível de maturidade da pessoa.

O que funciona bem é a **frase que gruda na cabeça** (estratégia vs tática).

O que NÃO funciona tão bem é o pedido repetido duas vezes e o pulo abrupto entre "estratégia vs tática" e "subir LTV".

**Risco com as regras do Facebook:** baixo. Linguagem de negócio, sem termos sensíveis.
""",

    "Funil_tripware/59DATV - Trip 27$.md": """## 9. Análise geral

Esse é um **anúncio que lista o que vem na caixa, pra quem já tá quentinho** — não é pra quem nunca te viu. Serve pra impactar de novo quem viu o vídeo de venda ou a página de venda e ainda não comprou.

Ele ataca a dúvida "vale o que custa?" mostrando quanta coisa entrega. A abertura funciona porque junta três coisas em 2 segundos: curiosidade, preço e risco zero. Mas a frase logo depois quebra o ritmo.

A estrutura é mais "carta de venda em vídeo" do que "anúncio pra descobrir gente nova". Isso limita o alcance pra quem nunca te viu, mas ajuda a fechar quem já te conhece.

A ideia central de venda é: **"você não pode perder, e por $27 você leva muito mais do que o preço diz"**. Mostra muito entregável rápido (passa sensação de produto de $500+) e zera o risco com a garantia invertida. É a ideia certa pra um produto de entrada barato.

**O que NÃO funciona** pra quem nunca te viu: não tem gancho de dor ou identificação no início, não tem prova social de fora, e usa o termo "hiperorgánico de alto valor" sem explicar.

**O que funciona** pra quem já te conhece: muito entregável, garantia e nomes grudentos pra cada parte do produto.

**Risco com as regras do Facebook:** o problema é a promessa em dinheiro crua ("5 a 20 mil dólares extras al mes"). Em regiões onde o Facebook é mais rígido com promessas de "ganhar dinheiro", isso pode bloquear ou limitar a entrega do anúncio. O resto passa tranquilo.
""",

    "Funil_tripware/59DATV - Trip 27.md": """## 9. Análise geral

Esse é o anúncio mais bem mirado dos 4 do funil. Funciona porque sabe exatamente quem está do outro lado: alguém que CHEGOU na hora de pagar e travou. E vai direto na cabeça dessa pessoa.

A abertura (primeira frase) já filtra no primeiro segundo. Depois disso, o anúncio ataca a objeção lógica ("só provando pra saber"). E o corpo faz uma jogada rara: transforma o preço de $27 em **um selo de "estou comprometido"** em vez de barreira.

Isso não é texto tirado de livro — é texto de quem entende como a cabeça do comprador funciona.

A ideia é: **"o que te impede não é o produto, é a sua própria indecisão — e o jeito de quebrar a indecisão é entrar"**. É uma sacada muito boa. O "ficamos como amigos" repetido tira o peso de "estou vendendo pra você" e cria vínculo.

Pra mostrar de novo pra quem abandonou o carrinho, é fórmula. Escala naturalmente porque o público é pequeno mas muito qualificado.

**Risco com as regras do Facebook:** nenhum. Sem promessa em dinheiro explícita. Tom limpo. É o tipo de anúncio que roda 6 meses sem cansar a audiência (porque o público é renovado o tempo todo por novos abandonos de carrinho).
""",

    "Funil_tripware/69DATV - TRIP 27$.md": """## 9. Análise geral

Esse anúncio aposta tudo numa coisa só: a frase estranha "literalmente me puedes escapar". É a frase que faz a pessoa parar de rolar a tela.

O resto do anúncio é comum — garantia invertida repetida (igual aos outros) e pedido pra clicar. A força aqui está na abertura. O corpo não acompanha.

A ideia é: **"você é mais esperto que eu nesse acordo — leve vantagem"**. É uma sacada inteligente, porque passa a sensação de risco do comprador pro vendedor.

Mas o anúncio é curto demais pra sustentar a promessa de "te va a volar la cabeza" (vai te explodir a cabeça) — não mostra nenhuma prova concreta. Isso funciona pra audiência que já é muito quente (gente que já conhece o Razzetti e já viu o vídeo de venda), mas trava pra quem nunca te viu.

**Risco com as regras do Facebook:** baixo. Tom limpo. Pro tamanho que tem, é bom no custo por clique mas provavelmente fraco em conversão pra quem nunca viu.
""",

    "Funil_tripware/69DATV - TRIP 27$,.md": """## 9. Análise geral

Esse é a versão pior do anúncio pra quem abandonou o carrinho. Mesma ideia, mas mais raso.

A abertura funciona pra mirar o público que visitou a página. Mas o corpo é genérico — não usa as sacadas boas do outro (transformar o preço em sinal de compromisso, criar clima de amizade).

Parece uma variação feita só pra encher os dados de visitantes do site, não pra ganhar do outro em conversão.

A ideia é igual aos outros: **"risco zero, entra e vê"**. Mas sem a jogada esperta do anúncio de carrinho abandonado e sem a frase estranha do "me puedes escapar". É o anúncio mais comum dos 4.

Escala porque o anúncio "mostrar de novo pra quem já visitou" converte por inércia (o público já é qualificado), não porque o anúncio é forte.

**Risco com as regras do Facebook:** médio por causa da promessa em dinheiro no pedido. Em conta com histórico limpo, passa. Em conta que tá sob análise do Facebook, pode travar.
""",
}

# Caso especial: 55DATV - TRIP FREE - BIB BLUE (2) usa "## 7-9. CTAs, moderação, análise"
SPECIAL_55_2 = (
    "Bluehackers_biblio_-_Trip_Free/55DATV - TRIP FREE - BIB BLUE (2).md",
    """## 7-9. Pedidos, regras do Facebook, análise (igual ao original, com 1 diferença)

**Risco adicional com as regras do Facebook:** agora a faixa de renda aparece **NO PRIMEIRO SEGUNDO** do anúncio — antes vinha só no corpo. Aumenta o motivo pro Facebook bloquear como "promessa de ganhar dinheiro" logo na primeira varredura.

**Risco adicional VISUAL:** chuva de dólares + cifrões "$10.000 a $100.000 USD" estampados na tela DESDE O FRAME 1 = dobro de motivo pro filtro de imagem do Facebook (além do filtro de texto/áudio). O Facebook reconhece imagens de dólares caindo como sinal padrão de anúncio de "ganhar dinheiro". Em conta nova, esse visual sozinho derruba o anúncio mesmo antes do texto ser analisado. O original (sem dólares na abertura) é mais defensável visualmente.
"""
)

updated = 0

for rel, new_block in REWRITES.items():
    path = ROOT / rel
    if not path.exists():
        print(f"WARN missing: {path}", file=sys.stderr)
        continue
    text = path.read_text(encoding='utf-8')
    pattern = re.compile(r'## 9\. An[áa]lise geral.*?(?=\n## \d+\.|\Z)', flags=re.DOTALL | re.IGNORECASE)
    if not pattern.search(text):
        print(f"WARN no block 9: {rel}", file=sys.stderr)
        continue
    new_text = pattern.sub(new_block.rstrip() + "\n\n", text)
    path.write_text(new_text, encoding='utf-8')
    updated += 1

# Special case
rel2, new_block2 = SPECIAL_55_2
path2 = ROOT / rel2
if path2.exists():
    text2 = path2.read_text(encoding='utf-8')
    pattern2 = re.compile(r'## 7-9\..*?(?=\n## \d+\.|\Z)', flags=re.DOTALL)
    if pattern2.search(text2):
        new_text2 = pattern2.sub(new_block2.rstrip() + "\n\n", text2)
        path2.write_text(new_text2, encoding='utf-8')
        updated += 1
    else:
        print(f"WARN no ## 7-9 in: {rel2}", file=sys.stderr)

print(f"OK {updated} arquivos atualizados")
