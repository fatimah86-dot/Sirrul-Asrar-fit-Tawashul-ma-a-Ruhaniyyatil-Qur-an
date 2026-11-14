#!/usr/bin/env python3
"""Impor transkripsi halaman SAMPUL–60 (= PDF hal. 1–66) ke format induk.

Sumber : data/final/asror-tawashul-quran-USER-renumber-PDF.md
Keluaran: transkripsi/bab0-sampul-001-066.md

Format sumber memakai judul '# 📖 HALAMAN 2 — PDF hal. 2'; induk memerlukan
'## HALAMAN <nomor> — <judul>'. Skrip ini hanya MENGAlih penanda judul —
isi AR/LAT/ID/TATACARA disalin apa adanya, tanpa diringkas atau ditambah.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'data/final/asror-tawashul-quran-USER-renumber-PDF.md')
OUT = os.path.join(ROOT, 'transkripsi/bab0-sampul-001-066.md')

HEAD = re.compile(r'^#\s*📖\s*HALAMAN\s*(SAMPUL|\d+)\s*[—–-]\s*(.*)$')

md = open(SRC, encoding='utf-8').read()
# buang komentar HTML di awal berkas (catatan peta), bukan isi kitab
md = re.sub(r'(?s)^\s*<!--.*?-->', '', md)

lines = md.split('\n')
out = []
buf_pre = []
current = None
for ln in lines:
    m = HEAD.match(ln.strip())
    if m:
        if current is not None:
            out.append(current)
        tag = m.group(1)
        num = 1 if tag == 'SAMPUL' else int(tag)
        sub = m.group(2).strip()
        current = ['## HALAMAN %d — %s' % (num, sub), '']
        buf_pre = []
        continue
    if current is None:
        continue
    current.append(ln)

if current is not None:
    out.append(current)

body = '\n'.join('\n'.join(b).strip('\n') for b in out)

header = """# TRANSKRIPSI HALAMAN SAMPUL – 60 (PDF hal. 1–66)

Bagian pembuka kitab **Sirrul Asrar fi at-Tawashul ma'a Ruhaniyyatil Qur'an**
(Syaikh 'Athiyyah 'Abdul Hamid): sampul, muqaddimah, wasiat, dan Bab 1
(keutamaan ayat & surah) sampai halaman daftar karya.

Sumber teks: `data/final/asror-tawashul-quran-USER-renumber-PDF.md` — penanda
judul diubah ke format induk (`## HALAMAN n`), isi 4 sub-header disalin apa
adanya. Nomor halaman = nomor halaman naskah (peta resmi lihat
`data/PETA-HALAMAN.md`).

"""

open(OUT, 'w', encoding='utf-8').write(header + body + '\n')

nums = [int(x) for x in re.findall(r'(?m)^## HALAMAN (\d+)', body)]
print('halaman:', len(nums), 'rentang', min(nums), '-', max(nums))
print('keluaran:', OUT)
