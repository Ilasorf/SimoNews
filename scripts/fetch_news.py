import feedparser
import os

feeds = [
    ("ANSA", "https://www.ansa.it/web/ansait_web_rss_homepage.xml"),
    ("SVT", "https://www.svt.se/nyheter/inrikes/rss.xml"),
    ("Tom's Hardware", "https://www.tomshardware.com/feeds/rss2/all.xml")
]

html = """
<html>
<head>
<meta charset="UTF-8">
<title>SimoNews</title>
<style>
body {
    font-family: Arial;
    max-width: 900px;
    margin: auto;
    padding: 20px;
    background: #f5f5f5;
}
.card {
    background: white;
    padding: 15px;
    margin-bottom: 20px;
    border-radius: 10px;
}
</style>
</head>
<body>

<h1>SimoNews</h1>
"""

for source, url in feeds:
    feed = feedparser.parse(url)

    html += f"<h2>{source}</h2>"

    for entry in feed.entries[:5]:
        title = entry.title
        summary = entry.summary if "summary" in entry else ""
        link = entry.link

        html += f'''
        <div class="card">
            <h3>{title}</h3>
            <p>{summary[:250]}</p>
            <a href="{link}">Leggi</a>
        </div>
        '''

html += "</body></html>"

os.makedirs("output", exist_ok=True)

with open("output/index.html", "w", encoding="utf-8") as f:
    f.write(html)
