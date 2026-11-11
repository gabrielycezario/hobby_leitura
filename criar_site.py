from pathlib import Path
from html import escape

PASTA = Path(__file__).resolve().parent
NOME = 'Gabriely Cezário' 

sites = [
    {
        'nome': 'Kindle',
        'categoria': 'Leitura digital',
        'descricao': 'No Kindle, posso levar vários livros para qualquer lugar e ler pelo aplicativo ou pelo dispositivo.',
        'link': 'https://www.amazon.com.br/kindle',
        'link_texto': 'Conhecer o Kindle',
        'imagem': 'kindle.svg',
        'fundo': '#dcece5', 'tinta': "#5e1b5e", 'icone': 'kindle',
    },
    {
        'nome': 'Amazon Livros',
        'categoria': 'Descobrir novos livros',
        'descricao': 'Na Amazon, pesquiso títulos, autores, sinopses e avaliações de leitores antes de escolher a próxima leitura.',
        'link': 'https://www.amazon.com.br/livros',
        'link_texto': 'Explorar livros na Amazon',
        'imagem': 'amazon.svg',
        'fundo': '#fff0d8', 'tinta': '#8f5019', 'icone': 'amazon',
    },
    {
        'nome': 'TikTok (BookTok)',
        'categoria': 'Resenhas e recomendações',
        'descricao': 'No BookTok, acompanho resenhas, opiniões e indicações de leitores que me ajudam a descobrir histórias.',
        'link': 'https://www.tiktok.com/tag/booktok',
        'link_texto': 'Ver resenhas no BookTok',
        'imagem': 'tiktok.svg',
        'fundo': '#e8e3f5', 'tinta': '#504085', 'icone': 'tiktok',
    },
]


svg_base = '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500">
<rect width="800" height="500" rx="28" fill="{fundo}"/>
<circle cx="660" cy="95" r="130" fill="white" opacity=".28"/>
<circle cx="110" cy="430" r="150" fill="white" opacity=".22"/>
{desenho}
<text x="46" y="439" font-family="Arial,Helvetica,sans-serif" font-size="26" font-weight="700" fill="{tinta}">{titulo}</text>
<text x="46" y="470" font-family="Arial,Helvetica,sans-serif" font-size="18" fill="{tinta}">{subtitulo}</text>
</svg>'''

desenhos = {
    'kindle': '''<rect x="278" y="55" width="244" height="333" rx="25" fill="#1c3833"/><rect x="294" y="75" width="212" height="282" rx="8" fill="#fffdf2"/><rect x="317" y="113" width="166" height="8" rx="4" fill="#c3cfc9"/><rect x="317" y="136" width="145" height="8" rx="4" fill="#c3cfc9"/><rect x="317" y="159" width="161" height="8" rx="4" fill="#c3cfc9"/><path d="M326 280 Q398 228 473 280 L473 320 Q398 281 326 320Z" fill="#81b2a2"/><circle cx="400" cy="371" r="7" fill="#739c8d"/>''',
    'amazon': '''<g transform="translate(165 66)"><path d="M40 77 Q156 24 270 77 L270 310 Q156 260 40 310Z" fill="#d2a56b" stroke="#88531e" stroke-width="9"/><path d="M270 77 Q379 26 490 77 L490 310 Q379 260 270 310Z" fill="#efc790" stroke="#88531e" stroke-width="9"/><path d="M270 78V310" stroke="#88531e" stroke-width="8"/><path d="M77 126 Q152 102 236 128 M77 157 Q152 133 236 159 M305 128 Q375 102 453 126 M305 159 Q375 133 453 157" fill="none" stroke="#9b744d" stroke-width="7" stroke-linecap="round"/></g>''',
    'tiktok': '''<g transform="translate(285 48)"><rect width="230" height="348" rx="31" fill="#242238"/><rect x="15" y="19" width="200" height="298" rx="17" fill="#504085"/><path d="M135 75 V188 C135 231 108 251 75 248 C28 244 20 182 64 160 C74 155 82 153 91 153 V195 C72 191 63 206 72 215 C88 232 104 215 104 195 V75Z" fill="#98e5dc"/><path d="M146 69 V182 C146 225 119 245 86 242 C39 238 31 176 75 154 C85 149 93 147 102 147 V189 C83 185 74 200 83 209 C99 226 115 209 115 189 V69Z" fill="#fff"/><circle cx="115" cy="332" r="8" fill="#d1cde1"/></g>''',
}

for site in sites:
    imagem = svg_base.format(
        fundo=site['fundo'], tinta=site['tinta'], desenho=desenhos[site['icone']],
        titulo=escape(site['nome']), subtitulo=escape(site['categoria'])
    )
    (PASTA / site['imagem']).write_text(imagem, encoding='utf-8')

cards = '\n'.join(f'''<article class="card">
    <h3>{escape(s['nome'])}</h3>
    <p class="category">{escape(s['categoria'])}</p>
    <a href="{escape(s['link'])}" target="_blank" rel="noopener noreferrer" aria-label="Abrir {escape(s['nome'])}">
      <img src="{escape(s['imagem'])}" alt="Ilustração sobre {escape(s['nome'])} relacionada à leitura" loading="lazy">
    </a>
    <p>{escape(s['descricao'])}</p>
    <a class="site-link" href="{escape(s['link'])}" target="_blank" rel="noopener noreferrer">{escape(s['link_texto'])} ↗</a>
    <p class="url">{escape(s['link'])}</p>
  </article>''' for s in sites)

html = '''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Página sobre o hobby da leitura, com sites para encontrar livros e resenhas.">
  <title>Meu Hobby Favorito: Leitura</title>
  <style>
    :root { --ink:#243b32; --muted:#64776e; --paper:#fbf8ef; --green:#2e6a54; --line:#dbe4da; }
    * { box-sizing: border-box; }
    body { margin:0; background:var(--paper); color:var(--ink); font-family:Arial,Helvetica,sans-serif; line-height:1.6; }
    header { background:linear-gradient(125deg,#173d32,#39745e); color:white; padding:70px 24px 75px; text-align:center; }
    .eyebrow { font-size:13px; text-transform:uppercase; letter-spacing:3px; color:#d1e6d8; font-weight:700; }
    h1 { font-family:Georgia,serif; font-size:clamp(30px,5.5vw,56px); line-height:1.17; margin:14px 0; }
    .subtitle { margin:0 auto; max-width:620px; color:#e7f0e9; font-size:18px; }
    main { max-width:1160px; padding:46px 22px 60px; margin:auto; }
    .intro { max-width:780px; margin:0 auto 45px; text-align:center; }
    h2 { font-family:Georgia,serif; font-size:30px; margin:0 0 12px; }
    .intro p { color:#53685c; margin:0; }
    .cards { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:22px; }
    .card { background:white; padding:24px; border:1px solid var(--line); border-radius:18px; box-shadow:0 10px 28px #173d3210; }
    .card h3 { font-family:Georgia,serif; font-size:25px; margin:0 0 0; }
    .category { color:var(--green); text-transform:uppercase; font-size:11px; font-weight:700; letter-spacing:1.5px; margin:3px 0 16px; }
    .card img { display:block; width:100%; height:auto; aspect-ratio:8/5; border-radius:12px; transition:transform .2s; }
    .card img:hover { transform:scale(1.025); }
    .card > p:not(.category):not(.url) { min-height:110px; color:#506359; }
    a.site-link { color:white; background:var(--green); padding:11px 14px; border-radius:9px; font-weight:700; display:inline-block; text-decoration:none; }
    a.site-link:hover { background:#214e3d; }
    .url { font-size:12px; overflow-wrap:anywhere; color:#687d70; }
    .quote { margin:52px auto 0; padding:28px; max-width:790px; border-left:5px solid #7aa98b; background:#eaf1e9; border-radius:0 14px 14px 0; font-family:Georgia,serif; font-size:22px; text-align:center; }
    footer { background:#18392e; color:#dbe9dd; text-align:center; padding:25px 15px; font-size:14px; }
    @media (max-width:850px) { .cards {grid-template-columns:1fr;} .card > p:not(.category):not(.url) {min-height:0;} .card {max-width:560px; width:100%; margin:auto;} }
  </style>
</head>
<body>
  <header>
    <div class="eyebrow">Livros • Histórias • Imaginação</div>
    <h1>Meu hobby favorito: Leitura — {nome}</h1>
    <p class="subtitle">Entre páginas e histórias, descubro novas ideias, personagens e mundos.</p>
  </header>
  <main>
    <section class="intro">
      <h2>Por que gosto de ler?</h2>
      <p>A leitura é um dos meus hobbies favoritos porque me permite aprender, relaxar e conhecer diferentes pontos de vista. Também gosto de descobrir livros novos e acompanhar resenhas de outros leitores. Abaixo estão três sites que fazem parte desse universo.</p>
    </section>
    <section class="cards" aria-label="Três sites relacionados à leitura">
      {cards}
    </section>
    <blockquote class="quote">“Cada livro é uma nova oportunidade de conhecer outro mundo.”</blockquote>
  </main>
  <footer>Atividade de desenvolvimento web • Hobby: Leitura • {nome}</footer>
</body>
</html>
'''.replace('{nome}', escape(NOME)).replace('{cards}', cards)

(PASTA / 'index.html').write_text(html, encoding='utf-8')
print('Site gerado em:', PASTA / 'index.html')
print('Abra index.html no navegador para visualizar.')
