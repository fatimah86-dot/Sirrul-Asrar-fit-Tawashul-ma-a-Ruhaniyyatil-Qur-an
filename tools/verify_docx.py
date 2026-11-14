#!/usr/bin/env python3
"""Verifikasi dokumen Word: 3 lapis sejajar, tanda dipertahankan, cakupan jujur, gambar tertanam."""
import re, sys, zipfile, difflib
from docx import Document

F = sys.argv[1] if len(sys.argv) > 1 else 'Sirrul-Asrar-Bab2-Hal-239-516.docx'
SRC = 'transkripsi/bab2.md'

d = Document(F)
src = open(SRC, encoding='utf-8').read()

def norm(t):
    t = re.sub(r'\*\*', '', t); t = re.sub(r'`', '', t); t = re.sub(r'\*(?!\*)', '', t)
    return re.sub(r'\s+', ' ', t).strip()

ar = [p.text[:-4].rstrip() for p in d.paragraphs if p.text.rstrip().endswith('  AR')]
lat = [p.text[5:] for p in d.paragraphs if p.text.startswith('LAT  ')]
idn = [p.text[4:] for p in d.paragraphs if p.text.startswith('ID  ')]
s_ar = [m.group(1).rstrip() for m in re.finditer(r'(?m)^\*\*AR:\*\*\s?(.*)$', src)]
s_lat = [m.group(1) for m in re.finditer(r'(?m)^\*\*LAT:\*\*\s?(.*)$', src)]
s_id = [m.group(1) for m in re.finditer(r'(?m)^\*\*ID:\*\*\s?(.*)$', src)]

print('blok AR / LAT / ID  :', len(ar), len(lat), len(idn))
print('sumber AR/LAT/ID    :', len(s_ar), len(s_lat), len(s_id))
print('AR identik          :', sum(1 for a, b in zip(ar, s_ar) if a == b), '/', len(s_ar))
print('LAT identik (norm)  :', sum(1 for a, b in zip(lat, s_lat) if norm(a) == norm(b)), '/', len(s_lat))
print('ID  identik (norm)  :', sum(1 for a, b in zip(idn, s_id) if norm(a) == norm(b)), '/', len(s_id))

alltxt = '\n'.join(p.text for p in d.paragraphs) + '\n' + '\n'.join(
    c.text for t in d.tables for r in t.rows for c in r.cells)
for tag in ('[TIDAK JELAS', '[TEKS ASLI DIJAGA]'):
    print('%-20s doc=%d src=%d %s' % (tag, alltxt.count(tag), src.count(tag),
                                      'OK' if alltxt.count(tag) == src.count(tag) else 'BEDA'))

z = zipfile.ZipFile(F)
media = [n for n in z.namelist() if n.startswith('word/media/')]
rels = z.read('word/_rels/document.xml.rels').decode()
docxml = z.read('word/document.xml').decode()
print('media tertanam      :', len(media), '| relasi External:', 'External' in rels)
print('gambar inline       :', docxml.count('<w:drawing>'))
print('font Amiri          :', docxml.count('Amiri'), 'rujukan')
print('judul "Halaman n"   :', len(re.findall(r'(?m)^Halaman \d+', '\n'.join(p.text for p in d.paragraphs))))
sampul = [p.text for p in d.paragraphs[:14] if p.text.strip()]
print('sampul              :', sampul[3:5])
print('klaim "Hal. 1–516"  :', alltxt.count('Hal. 1–516'), '(harus 0)')
