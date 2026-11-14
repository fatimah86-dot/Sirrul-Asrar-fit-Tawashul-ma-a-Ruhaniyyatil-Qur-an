#!/usr/bin/env python3
"""Bangun Sirrul-Asrar-Bab2-Hal-239-516.docx dari transkripsi/bab2.md.

Aturan yang ditegakkan skrip ini:
  - isi AR/LAT/ID disalin apa adanya (tidak diringkas, tidak ditambah)
  - tanda [TIDAK JELAS] / [TEKS ASLI DIJAGA] dipertahankan
  - font Arab = Amiri (ascii/hAnsi/cs/eastAsia)
  - per halaman mulai di halaman baru; AR (RTL) -> LAT (miring) -> ID
  - tabel markdown -> tabel Word
  - gambar memakai crop KETAT (assets/rajah/sirrul-asrar-tight) bila ada
  - rentang halaman pada sampul/Daftar Isi/footer diambil dari data, bukan dikarang
"""
import re
import os
import glob
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'transkripsi/bab2.md')
OUT = os.path.join(ROOT, 'Sirrul-Asrar-Bab2-Hal-239-516.docx')
TIGHT = os.path.join(ROOT, 'assets/rajah/sirrul-asrar-tight')
RAJAH = os.path.join(ROOT, 'assets/rajah/sirrul-asrar')

md = open(SRC, encoding='utf-8').read()
parts = re.split(r'(?m)^## HALAMAN (\d+)\s*[—\-–]?\s*(.*)$', md)
pages, order = {}, []
for i in range(1, len(parts), 3):
    n = int(parts[i])
    pages[n] = (parts[i + 1].strip(), parts[i + 2])
    order.append(n)
order.sort()
FIRST, LAST = order[0], order[-1]
gaps = [p for p in range(FIRST, LAST + 1) if p not in pages]
wafak_pages = [n for n in order if '![' in pages[n][1]]

doc = Document()
st = doc.styles['Normal']
st.font.name = 'Calibri'
st.font.size = Pt(10.5)
st.paragraph_format.space_after = Pt(4)
st.paragraph_format.line_spacing = 1.15


def set_cs(run, font='Amiri'):
    rPr = run._element.get_or_add_rPr()
    rf = rPr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts')
        rPr.append(rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
        rf.set(qn(a), font)


def rtl(par):
    pPr = par._p.get_or_add_pPr()
    pPr.append(OxmlElement('w:bidi'))


def field(par, instr):
    r = par.add_run()
    f1 = OxmlElement('w:fldChar'); f1.set(qn('w:fldCharType'), 'begin')
    it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = instr
    f2 = OxmlElement('w:fldChar'); f2.set(qn('w:fldCharType'), 'end')
    r._r.append(f1); r._r.append(it); r._r.append(f2)


INLINE = re.compile(r'(\*\*.+?\*\*|\*[^*\n]+?\*|`[^`]+?`)')


def rich(par, text, italic=False, size=10.5):
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith('**') and part.endswith('**') and len(part) > 4:
            r = par.add_run(part[2:-2]); r.bold = True
        elif part.startswith('*') and part.endswith('*') and len(part) > 2:
            r = par.add_run(part[1:-1]); r.italic = True
        elif part.startswith('`') and part.endswith('`') and len(part) > 2:
            r = par.add_run(part[1:-1]); r.font.name = 'Consolas'; r.font.size = Pt(size - 1)
            continue
        else:
            r = par.add_run(part); r.italic = italic
        r.font.size = Pt(size)


def plain(text):
    return re.sub(r'\*\*', '', text)


def clean_body(body):
    out, lines, i = [], body.split('\n'), 0
    while i < len(lines):
        l = lines[i]
        if l.startswith('|'):
            blk = []
            while i < len(lines) and lines[i].startswith('|'):
                blk.append(lines[i]); i += 1
            out.append(('table', blk)); continue
        if '![' in l:
            out.append(('img', None)); i += 1; continue
        if l.startswith('**[ADA RAJAH]**') or l.startswith('**[TIDAK ADA RAJAH'):
            i += 1; continue
        if l.strip() in ('', '---'):
            i += 1; continue
        out.append(('line', l)); i += 1
    return out


def images_for(n):
    tight = sorted(glob.glob(os.path.join(TIGHT, 'hal-%d-rajah-*.png' % n)))
    if tight:
        return [(p, True) for p in tight]
    return [(p, False) for p in sorted(glob.glob(os.path.join(RAJAH, 'hal-%d-rajah-*' % n)))]


# ---------------- SAMPUL ----------------
for _ in range(3):
    doc.add_paragraph()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('سِرُّ الْأَسْرَارِ فِي التَّوَاصُلِ مَعَ رُوحَانِيَّاتِ الْقُرْآن')
r.bold = True; r.font.size = Pt(28); set_cs(r); rtl(p)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('Sirrul Asrar fi at-Tawashul ma‘a Ruhaniyyatil Qur’an'); r.bold = True; r.font.size = Pt(18)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('Syaikh al-Ruhaniyyin Syaikh Atiyah Abdul Hamid'); r.italic = True; r.font.size = Pt(12)
doc.add_paragraph()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('Bab 2 — Transliterasi AR | LAT | ID'); r.bold = True; r.font.size = Pt(20)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('Hal. %d–%d' % (FIRST, LAST)); r.bold = True; r.font.size = Pt(22)
r.font.color.rgb = RGBColor(0x1F, 0x3B, 0x63)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('(%d halaman · %d halaman berwafak · font Arab Amiri)' % (len(order), len(wafak_pages)))
r.font.size = Pt(11)
doc.add_paragraph()
for txt in ['Naskah koreksi manual — format saja, isi tidak diubah',
            'Sumber: transkripsi/bab2.md + data/LAPORAN-BAB2.md']:
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(txt); r.font.size = Pt(9.5); r.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

# ---------------- CATATAN CAKUPAN ----------------
p = doc.add_paragraph()
r = p.add_run('CATATAN CAKUPAN'); r.bold = True; r.font.size = Pt(18)
r.font.color.rgb = RGBColor(0xB0, 0x30, 0x30)
for txt in [
    'Dokumen ini memuat halaman %d–%d saja — %d halaman, berurutan tanpa celah%s.'
    % (FIRST, LAST, len(order), '' if not gaps else ', kecuali celah: ' + ', '.join(map(str, gaps))),
    'Halaman 1–238 TIDAK ada di transkripsi/bab2.md dan TIDAK ditranskripsi di sini. Tidak ada isi yang dikarang.',
    'transkripsi/bab1.md (hal. 7–28) adalah dokumen TERPISAH — tidak digabungkan ke sini.',
    'Halaman 1–6 dan 29–238 belum pernah ditranskripsi; menunggu teks dari pemilik naskah.',
    'Judul sampul, Daftar Isi, dan footer memakai rentang yang benar-benar ada: hal. %d–%d.' % (FIRST, LAST),
    'Seluruh AR/LAT/ID disalin apa adanya. Tanda TIDAK JELAS dan TEKS ASLI DIJAGA dipertahankan persis di tempatnya, jumlahnya sama dengan sumber.',
    'Rajah disisipkan sebagai potongan ketat area wafaq; tidak ada halaman utuh yang disisipkan.',
]:
    pp = doc.add_paragraph(style='List Bullet'); rich(pp, txt, size=10)
doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

# ---------------- DAFTAR ISI ----------------
p = doc.add_paragraph(); r = p.add_run('DAFTAR ISI'); r.bold = True; r.font.size = Pt(18)
p = doc.add_paragraph()
r = p.add_run('Isi per halaman %d–%d (satu judul satu baris, nomor sejajar)' % (FIRST, LAST))
r.italic = True; r.font.size = Pt(10)
for n in order:
    title = plain(pages[n][0])
    pp = doc.add_paragraph(); pp.paragraph_format.space_after = Pt(1)
    r = pp.add_run('Halaman %d' % n); r.bold = True; r.font.size = Pt(9.5)
    if title:
        r2 = pp.add_run(' — ' + title); r2.font.size = Pt(9.5)
doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

# ---------------- ISI ----------------
for idx, n in enumerate(order):
    title = plain(pages[n][0])
    if idx > 0:
        doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    h = doc.add_heading(level=1)
    r = h.add_run('Halaman %d' % n + (' — ' + title if title else ''))
    r.font.size = Pt(15); r.font.color.rgb = RGBColor(0x1F, 0x3B, 0x63)

    img_done = set()
    for kind, payload in clean_body(pages[n][1]):
        if kind == 'table':
            rows = [[c.strip() for c in r_.strip().strip('|').split('|')] for r_ in payload
                    if not re.match(r'^\|[\s\-:|]+\|$', r_.strip())]
            if not rows:
                continue
            ncol = max(len(r_) for r_ in rows)
            t = doc.add_table(rows=0, cols=ncol)
            t.style = 'Table Grid'; t.alignment = WD_TABLE_ALIGNMENT.CENTER
            for ri, row in enumerate(rows):
                cells = t.add_row().cells
                for ci in range(ncol):
                    par = cells[ci].paragraphs[0]
                    rich(par, row[ci] if ci < len(row) else '', size=9)
                    if ri == 0:
                        for rr in par.runs:
                            rr.bold = True
            doc.add_paragraph()
            continue
        if kind == 'img':
            if n in img_done:   # satu halaman = satu set gambar (hindari gambar ganda)
                continue
            img_done.add(n)
            ptr = doc.add_paragraph()
            r = ptr.add_run('[Wafak Hal. %d] — Lihat gambar wafak pada naskah asli halaman %d' % (n, n))
            r.bold = True; r.font.size = Pt(9.5)
            for path, tight in images_for(n):
                pp = doc.add_paragraph(); pp.alignment = WD_ALIGN_PARAGRAPH.CENTER
                try:
                    pp.add_run().add_picture(path, width=Inches(4.4 if tight else 4.8))
                except Exception:
                    pp.add_run('[gagal menyisipkan %s]' % os.path.basename(path))
                cap = doc.add_paragraph(); cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                rr = cap.add_run('[Wafak Hal. %d] — Gambar wafak dari naskah asli halaman %d' % (n, n))
                rr.italic = True; rr.font.size = Pt(8.5); rr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
            continue

        l = payload
        m = re.match(r'^\*\*(AR|LAT|ID):\*\*\s?(.*)$', l)
        if m:
            lab_kind, txt = m.group(1), m.group(2).rstrip()
            pp = doc.add_paragraph(); pp.paragraph_format.space_after = Pt(5)
            if lab_kind == 'AR':
                pp.alignment = WD_ALIGN_PARAGRAPH.RIGHT; rtl(pp)
                r = pp.add_run(txt); r.font.size = Pt(15); set_cs(r, 'Amiri')
                lab = pp.add_run('  AR'); lab.font.size = Pt(7)
                lab.font.color.rgb = RGBColor(0x99, 0x99, 0x99)
            elif lab_kind == 'LAT':
                r = pp.add_run('LAT  '); r.bold = True; r.font.size = Pt(7.5)
                r.font.color.rgb = RGBColor(0x99, 0x99, 0x99)
                rich(pp, txt, italic=True, size=10.5)
            else:
                r = pp.add_run('ID  '); r.bold = True; r.font.size = Pt(7.5)
                r.font.color.rgb = RGBColor(0x99, 0x99, 0x99)
                rich(pp, txt, size=10.5)
            continue
        if l.startswith('- '):
            pp = doc.add_paragraph(style='List Bullet'); rich(pp, l[2:].strip(), size=10); continue
        txt = l.strip(); pp = doc.add_paragraph()
        if txt.startswith('*(') and txt.endswith(')*'):
            rich(pp, txt, italic=True, size=9)
        elif txt.startswith('**[TIDAK JELAS') or txt.startswith('**[TIDAK ADA RAJAH'):
            r = pp.add_run(plain(txt)); r.font.size = Pt(9); r.font.color.rgb = RGBColor(0x8A, 0x3B, 0x00)
        else:
            rich(pp, txt, size=10)

# ---------------- DAFTAR WAFAK ----------------
doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
p = doc.add_paragraph(); r = p.add_run('DAFTAR WAFAK'); r.bold = True; r.font.size = Pt(18)
p = doc.add_paragraph()
r = p.add_run('%d halaman berisi rajah/wafak (hal. %d–%d). Setiap gambar = potongan ketat area wafaq.'
              % (len(wafak_pages), FIRST, LAST))
r.italic = True; r.font.size = Pt(9.5)
for n in wafak_pages:
    pp = doc.add_paragraph(); r = pp.add_run('[Wafak Hal. %d]' % n); r.bold = True; r.font.size = Pt(10)
    for path, tight in images_for(n):
        ip = doc.add_paragraph(); ip.alignment = WD_ALIGN_PARAGRAPH.CENTER
        try:
            ip.add_run().add_picture(path, width=Inches(2.0))
        except Exception:
            ip.add_run('[gagal]')
        cap = doc.add_paragraph(); cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        rr = cap.add_run('[Wafak Hal. %d] — Gambar wafak dari naskah asli halaman %d' % (n, n))
        rr.italic = True; rr.font.size = Pt(8)
        rr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

# ---------------- FOOTER ----------------
sec = doc.sections[0]
fp = sec.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = fp.add_run('Sirrul Asrar — Bab 2 (AR | LAT | ID) · Hal. %d–%d · ' % (FIRST, LAST)); r.font.size = Pt(8)
field(fp, 'PAGE')
r = fp.add_run(' / '); r.font.size = Pt(8)
field(fp, 'NUMPAGES')
for rr in fp.runs:
    rr.font.size = Pt(8)

doc.core_properties.title = 'Sirrul Asrar — Bab 2 Transliterasi AR | LAT | ID hal. %d–%d' % (FIRST, LAST)
doc.core_properties.subject = 'Naskah koreksi manual (format-only), font Amiri'
doc.save(OUT)

print('halaman:', len(order), '| rentang:', FIRST, '-', LAST, '| celah:', gaps)
print('halaman berwafak:', len(wafak_pages), '| ukuran MB:', round(os.path.getsize(OUT) / 1048576, 2))
