import os
import json
import requests
from bs4 import BeautifulSoup
import markdownify

if __name__ == '__main__':
    ith = []
    title = subtitle = ''
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    idx = 7045
    for i in range(706, 931):
        response = requests.get(f"https://www.uji.es/com/noticies/?%24F%3Atitulo_largo_sin_acentos%3ALIKE%3AA%40%24F%3Atitulo_sin_acentos%3ALIKE%3AA%40%24F%3Asubtitulo_sin_acentos%3ALIKE%3AA%40%24F%3Aresumen_sin_acentos%3ALIKE%3AA%40%24F%3Acontenido%3ACLOB%3AA=&%24C%3Afecha_vigencia%3AFECHA_MAYOR_IGUAL=&%24C%3Afecha_vigencia%3AFECHA_MENOR_IGUAL=&pageSearch={i}",
                                    headers=HEADERS)
        if response.status_code == 200:
            data = response.text
            bs = BeautifulSoup(data, "html.parser")
            if bs:
                noticias = bs.find_all('p', {'class': 'bellota h4-title'})
                for noticia in noticias:
                    idx += 1
                    href = noticia.find('a').get('href')
                    if href.startswith('http'):
                        url = href
                    else:
                        url = "https://www.uji.es" + href
                    url_clean = url
                    for y in range(1, 4):
                        if y == 2:
                            url = "https://www.uji.es/upo/rest/publicacion/idioma/es?urlRedirect=" + url_clean
                        if y == 3:
                            url = "https://www.uji.es/upo/rest/publicacion/idioma/en?urlRedirect=" + url_clean
                        response = requests.get(url, headers=HEADERS)
                        if response.status_code == 200:
                            data = response.text
                            bs = BeautifulSoup(data, "html.parser")
                            if bs:
                                title_tag = bs.find('h2')
                                if title_tag:
                                    # Subtítulo (si existe)
                                    subtitle_tag = title_tag.find('span')
                                    subtitle = subtitle_tag.text.strip() if subtitle_tag else ""

                                    # Título: texto directo, sin incluir el span
                                    title_text = title_tag.find(text=True, recursive=False)
                                    title = title_text.strip() if title_text else None

                                if title == "Not found in English":
                                    continue

                                date = bs.find('div', {'class': 'clockBarDate margin-right-1'})
                                if date:
                                    date = date.text.split("|")[0].strip()

                                content = bs.find('div', {'class': 'uji-editor'})
                                if content:
                                    content = content.text.strip()
                                else:
                                    continue

                                #filename = title.lower().replace(' ', '_').replace('/', '_')
                                #filename = re.sub(r'[\\/*?:"<>|¿\t\n]', '_', filename)
                                #base_filename = f"{filename}"
                                base_filename = "noticia" + str(idx)

                                # ❌ Si ya existe el HTML, no seguimos con esta noticia
                                #if os.path.exists(html_filename):
                                #    print(f"NOTICIA YA EXISTE: {html_filename}")
                                #    continue

                                if y == 1:
                                    html_filename = os.path.join("UJI", "html", "2025-07", "va", f"{base_filename}.html")
                                    md_filename = os.path.join("UJI", "md", "2025-07", "va", f"{base_filename}.md")
                                    txt_filename = os.path.join("UJI", "plain", "2025-07", "va", f"{base_filename}.txt")

                                    ith.append(
                                        {'source': url,
                                         'title': title,
                                         'subtitle': subtitle,
                                         'date': date,
                                         'path2html': './html/2025-07/va/' + base_filename + ".html",
                                         'path2txt': './plain/2025-07/va/' + base_filename + ".txt",
                                         'path2md': './md/2025-07/va/' + base_filename + ".md"})
                                elif y == 2:
                                    html_filename = os.path.join("UJI", "html", "2025-07", "es",
                                                                 f"{base_filename}.html")
                                    md_filename = os.path.join("UJI", "md", "2025-07", "es", f"{base_filename}.md")
                                    txt_filename = os.path.join("UJI", "plain", "2025-07", "es", f"{base_filename}.txt")

                                    ith.append(
                                        {'source': url,
                                         'title': title,
                                         'subtitle': subtitle,
                                         'date': date,
                                         'path2html': './html/2025-07/es/' + base_filename + ".html",
                                         'path2txt': './plain/2025-07/es/' + base_filename + ".txt",
                                         'path2md': './md/2025-07/es/' + base_filename + ".md"})
                                else:
                                    html_filename = os.path.join("UJI", "html", "2025-07", "en",
                                                                 f"{base_filename}.html")
                                    md_filename = os.path.join("UJI", "md", "2025-07", "en", f"{base_filename}.md")
                                    txt_filename = os.path.join("UJI", "plain", "2025-07", "en", f"{base_filename}.txt")

                                    ith.append(
                                        {'source': url,
                                         'title': title,
                                         'subtitle': subtitle,
                                         'date': date,
                                         'path2html': './html/2025-07/en/' + base_filename + ".html",
                                         'path2txt': './plain/2025-07/en/' + base_filename + ".txt",
                                         'path2md': './md/2025-07/en/' + base_filename + ".md"})

                                with open(html_filename, "wb") as f:
                                    f.write(response._content)  # data es el contenido HTML original

                                markdown = markdownify.markdownify(str(bs), heading_style="ATX")

                                with open(md_filename, "w", encoding="utf-8") as f:
                                    f.write(markdown)


                                with open(txt_filename, "w", encoding="utf-8") as f:
                                    f.write(content)


                                print("NOTICIA: " + url + " DESCARGADA. INDEX = " + str(idx))

                        ruta = os.path.join("UJI", "index.json")
                        f = open(os.getcwd() + "\\" + ruta, "w+", encoding='utf-8')
                        f.write(json.dumps(ith, indent=4, ensure_ascii=False))
                print("PÁGINA: " + str(i) + " DESCARGADA.")