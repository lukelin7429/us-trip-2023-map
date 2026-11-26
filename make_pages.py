"""page.html is the page body (the form claude.ai Artifacts expect).
This wraps it into docs/index.html, a full document for GitHub Pages.
Usage: python3 make_pages.py"""
head='''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="Three weeks on the US East Coast, August–September 2023, rebuilt from the time and GPS stamps in phone photos.">
<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
'''
body=open('page.html',encoding='utf-8').read()
open('docs/index.html','w',encoding='utf-8').write(head+body+'\n</body>\n</html>\n')
print('docs/index.html written')
