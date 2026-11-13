#!/usr/bin/env python3
"""Bangun dokumen induk (DOCX + PDF): Sirrul Asrar utuh — Sampul–60 + 67–87 + 239–516.

Aturan yang ditegakkan:
  - isi AR/LAT/ID disalin apa adanya dari transkripsi/*.md (tidak diringkas/ditambah)
  - font Arab = Amiri
  - satu halaman cetak = satu halaman baru; AR (RTL) -> LAT (miring) -> ID
  - Daftar Isi & Daftar Wafak dihitung dari data, bukan dikarang
  - DOCX memakai gambar crop KETAT bila tersedia
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_BAB0 = os.path.join(ROOT, 'transkripsi/bab0-sampul-001-066.md')
SRC_MAIN = os.path.join(ROOT, 'transkripsi/bab2.md')
SRC_EXT = os.path.join(ROOT, 'transkripsi/bab2-lanjutan-067-076.md')
SRC_NEW = os.path.join(ROOT, 'transkripsi/bab2-lanjutan-077-100.md')
TIGHT = os.path.join(ROOT, 'assets/rajah/sirrul-asrar-tight')
RAJAH = os.path.join(ROOT, 'assets/rajah/sirrul-asrar')
FONT_DIR = os.path.join(ROOT, 'assets/fonts')

OUT_DOCX = os.path.join(ROOT, 'Sirrul-Asrar-Kitab-Hal-01-516.docx')
OUT_PDF = os.path.join(ROOT, 'Sirrul-Asrar-Kitab-Hal-01-516.pdf')


def parse(path):
    md = open(path, encoding='utf-8').read()
    parts = re.split(r'(?m)^## HALAMAN (\d+)\s*[—\-–]?\s*(.*)$', md)
    out = []
    for i in range(1, len(parts), 3):
        out.append((int(parts[i]), parts[i + 1].strip(), parts[i + 2]))
    return out


pages = parse(SRC_BAB0) + parse(SRC_MAIN) + parse(SRC_EXT)
if os.path.exists(SRC_NEW):
    pages = pages + parse(SRC_NEW)
pages.sort(key=lambda x: x[0])
nums = [p[0] for p in pages]
assert len(nums) == len(set(nums)), 'nomor halaman duplikat: %s' % [
    n for n in nums if nums.count(n) > 1]

MARK = re.compile(r'^\*\*(AR|LAT|ID):\*\*[ \t]*(.*)$')


def groups(body):
    """Pecah body menjadi blok AR/LAT/ID + baris sisa, TANPA duplikasi.

    Blok = baris ber-marker + baris lanjutan sampai baris kosong.
    Blok tunggal (AR tanpa LAT/ID) tetap dipertahankan.
    """
    out = []
    lines = body.split('\n')
    i = 0
    n = len(lines)
    while i < n:
        m = MARK.match(lines[i])
        if not m:
            i += 1
            continue
        kind, first = m.group(1), m.group(2).rstrip()
        buf = [first] if first else []
        j = i + 1
        while j < n:
            ln = lines[j]
            if not ln.strip():
                break
            if MARK.match(ln) or ln.startswith('#') or ln.startswith('![') \
                    or ln.startswith('---'):
                break
            buf.append(ln.strip())
            j += 1
        out.append(('B', kind, ' '.join(buf).strip()))
        i = j
    return out


def paired(body):
    """Kelompokkan: tripel berurutan (AR,LAT,ID) atau blok tunggal."""
    b = groups(body)
    out, i = [], 0
    while i < len(b):
        if (i + 2 < len(b) and b[i][1] == 'AR' and b[i + 1][1] == 'LAT'
                and b[i + 2][1] == 'ID'):
            out.append(('T', b[i][2], b[i + 1][2], b[i + 2][2]))
            i += 3
        else:
            out.append(('S', b[i][1], b[i][2], None))
            i += 1
    return out


def extras(body):
    """Baris non-blok (catatan/keterangan) yang tetap harus dicetak."""
    keep = []
    for ln in body.split('\n'):
        t = ln.strip()
        if not t:
            continue
        if MARK.match(t) or t.startswith('![') or t.startswith('---'):
            continue
        keep.append(t)
    return keep


def images(body):
    res = []
    for m in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)', body):
        p = m.group(1)
        name = os.path.basename(p)
        for base in (TIGHT, RAJAH):
            cand = os.path.join(base, name)
            if os.path.exists(cand):
                res.append(cand)
                break
    return res


SEC_RE = re.compile(r'(?m)^###\s*([1-4])\.\s*(.+)$')
SEC_NAMES = {
    '1': 'TEKS ARAB BERHARAKAT',
    '2': 'TRANSLITERASI LATIN',
    '3': 'TERJEMAHAN INDONESIA',
    '4': 'TATACARA PRAKTIK LENGKAP',
}


def sections(body):
    """Halaman berformat 4 sub-header (aturan Ustadz Yoad).

    Mengembalikan list (nomor, nama, [baris]) atau None bila format lama.
    """
    hits = list(SEC_RE.finditer(body))
    if not hits:
        return None
    out = []
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(body)
        raw = body[m.end():end]
        lines = [ln.rstrip() for ln in raw.split('\n')]
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        lines = [ln for ln in lines if ln.strip() != '---']
        # buang penanda markdown (**tebal**) — di dokumen dicetak sebagai teks biasa
        lines = [re.sub(r'\*\*(.+?)\*\*', r'\1', ln) for ln in lines]
        lines = [re.sub(r'`(.+?)`', r'\1', ln) for ln in lines]
        # baris gambar (![...]) DIPERTAHANKAN: dicetak di posisinya
        out.append((m.group(1), SEC_NAMES.get(m.group(1), m.group(2).strip()),
                    lines))
    return out


def clean(body):
    body = re.sub(r'(?m)^\*\*(AR|LAT|ID):\*\*.*$', '', body)
    body = re.sub(r'(?m)^!\[.*$', '', body)
    body = re.sub(r'(?m)^\*\*Rajah.*$', '', body)
    return body.strip()


def _has_ar(text):
    """True bila baris memuat huruf Arab (>= 3 karakter)."""
    n = sum(1 for ch in text if 0x0600 <= ord(ch) <= 0x06FF)
    return n >= 3


# ---------------------------------------------------------------- DOCX
def build_docx():
    from docx import Document
    from docx.shared import Pt, Inches
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    doc = Document()
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(10.5)
    st.paragraph_format.space_after = Pt(4)
    st.paragraph_format.line_spacing = 1.15

    def set_font(run, font='Amiri'):
        rPr = run._element.get_or_add_rPr()
        rf = rPr.find(qn('w:rFonts'))
        if rf is None:
            rf = OxmlElement('w:rFonts')
            rPr.append(rf)
        for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
            rf.set(qn(a), font)

    def rtl(par):
        pPr = par._p.get_or_add_pPr()
        bidi = OxmlElement('w:bidi')
        pPr.append(bidi)
        par.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    def field(par, instr):
        fld = OxmlElement('w:fldSimple')
        fld.set(qn('w:instr'), instr)
        par._p.append(fld)

    first, last = nums[0], nums[-1]
    wafak = [n for n, t, b in pages if images(b)]

    # --- sampul
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run('Sirrul Asrar fi at-Tawashul ma\'a Ruhaniyyatil Qur\'an')
    r.bold = True
    r.font.size = Pt(20)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run('Kitab Utuh — Transliterasi AR | LAT | ID')
    r.bold = True
    r.font.size = Pt(16)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run('Halaman naskah %d–%d' % (first, last))
    r.bold = True
    r.font.size = Pt(14)
    doc.add_paragraph()

    # --- catatan cakupan
    doc.add_paragraph().add_run('CATATAN CAKUPAN').bold = True
    for line in [
        'Dokumen induk ini memuat %d halaman naskah yang sudah ditranskripsi: '
        'Sampul–60 (PDF 1–66), 67–137, dan 239–516.' % len(pages),
        'Nomor halaman mengikuti nomor halaman naskah (lihat data/PETA-HALAMAN.md);'
        ' halaman 138–238 BELUM dikerjakan dan TIDAK dikarang.',
        'Tanda [TIDAK JELAS] dan [TEKS ASLI DIJAGA] dipertahankan apa adanya; '
        'jumlahnya sama dengan sumber.',
    ]:
        doc.add_paragraph(line)

    # --- daftar isi
    doc.add_page_break()
    doc.add_paragraph().add_run('DAFTAR ISI (satu judul satu baris)').bold = True
    for i, (n, title, body) in enumerate(pages, 1):
        par = doc.add_paragraph()
        par.add_run('%d. Hal. %d — %s' % (i, n, title or '(tanpa judul)'))

    # --- isi
    for n, title, body in pages:
        doc.add_page_break()
        h = doc.add_paragraph()
        r = h.add_run('HALAMAN %d — %s' % (n, title))
        r.bold = True
        r.font.size = Pt(13)

        secs = sections(body)
        if not secs:
            for path in images(body):
                try:
                    doc.add_picture(path, width=Inches(4.2))
                except Exception:
                    pass

        if secs:
            for num, name, lines in secs:
                sh = doc.add_paragraph()
                sr = sh.add_run('### %s. %s' % (num, name))
                sr.bold = True
                sr.font.size = Pt(11.5)
                for line in lines:
                    if line.startswith('!['):
                        m = re.search(r'\(([^)]+)\)', line)
                        if m:
                            name = os.path.basename(m.group(1))
                            for base in (TIGHT, RAJAH):
                                cand = os.path.join(base, name)
                                if os.path.exists(cand):
                                    try:
                                        doc.add_picture(cand, width=Inches(4.0))
                                    except Exception:
                                        pass
                                    break
                        continue
                    par = doc.add_paragraph()
                    if num == '1' and _has_ar(line):
                        rtl(par)
                        r = par.add_run(line)
                        set_font(r)
                        r.font.size = Pt(15)
                    elif num == '4' and line.startswith('- '):
                        par.paragraph_format.left_indent = Inches(0.28)
                        par.add_run('• ' + line[2:])
                    else:
                        par.add_run(line)
        else:
            for g in paired(body):
                if g[0] == 'T':
                    _, ar, lat, idn = g
                    par = doc.add_paragraph()
                    rtl(par)
                    r = par.add_run(ar)
                    set_font(r)
                    r.font.size = Pt(15)
                    par = doc.add_paragraph()
                    r = par.add_run(lat)
                    r.italic = True
                    par = doc.add_paragraph()
                    par.add_run(idn)
                else:
                    _, kind, text, _ = g
                    par = doc.add_paragraph()
                    if kind == 'AR':
                        rtl(par)
                        r = par.add_run(text)
                        set_font(r)
                        r.font.size = Pt(15)
                    else:
                        r = par.add_run(text)
                        r.italic = (kind == 'LAT')

            for line in extras(body):
                doc.add_paragraph(line)

    # --- daftar wafak
    doc.add_page_break()
    doc.add_paragraph().add_run(
        'DAFTAR WAFAK (%d halaman berwafak)' % len(wafak)).bold = True
    for n in wafak:
        doc.add_paragraph('Hal. %d — Gambar wafak/rajah dari naskah asli halaman %d'
                          % (n, n))
        for path in images(dict((x[0], x[2]) for x in pages)[n]):
            try:
                doc.add_picture(path, width=Inches(3.6))
            except Exception:
                pass

    # --- footer
    sec = doc.sections[0]
    fp = sec.footer.paragraphs[0]
    fp.text = 'Sirrul Asrar — Kitab · Hal. %d–%d · ' % (first, last)
    field(fp, 'PAGE')
    fp.add_run(' / ')
    field(fp, 'NUMPAGES')

    doc.core_properties.title = 'Sirrul Asrar — Kitab (AR | LAT | ID)'
    doc.save(OUT_DOCX)
    return first, last, len(wafak)


# ---------------------------------------------------------------- PDF
def build_pdf():
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.utils import ImageReader
    import arabic_reshaper
    from bidi.algorithm import get_display

    pdfmetrics.registerFont(TTFont('Amiri', os.path.join(FONT_DIR, 'Amiri-Regular.ttf')))
    pdfmetrics.registerFont(TTFont('Amiri-Bold', os.path.join(FONT_DIR, 'Amiri-Bold.ttf')))
    # DejaVu: metrik Latin lengkap (diakritik ṣ ḥ ẓ ā ī ū, «» ‘ ’ —) —
    # Helvetica inti PDF tidak punya glif ini (tercetak sebagai kotak hitam).
    pdfmetrics.registerFont(TTFont('DejaVu', os.path.join(FONT_DIR, 'DejaVuSans.ttf')))
    pdfmetrics.registerFont(TTFont('DejaVu-Bold', os.path.join(FONT_DIR, 'DejaVuSans-Bold.ttf')))

    W, H = A4
    c = canvas.Canvas(OUT_PDF, pagesize=A4)
    M = 46
    first, last = nums[0], nums[-1]

    def ar(text):
        return get_display(arabic_reshaper.reshape(text))

    def wrap(text, font, size, width):
        words = text.split()
        lines, cur = [], ''
        for w in words:
            t = (cur + ' ' + w).strip()
            if pdfmetrics.stringWidth(t, font, size) <= width - 8:
                cur = t
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    from fontTools.ttLib import TTFont as _TT
    DEJA_CMAP = _TT(os.path.join(FONT_DIR, 'DejaVuSans.ttf')).getBestCmap()
    AMIRI_CMAP = _TT(os.path.join(FONT_DIR, 'Amiri-Regular.ttf')).getBestCmap()

    def arabic_segments(text):
        # Shape and bidi the entire logical line first, preserving Arabic joining.
        segs = []
        for ch in ar(text):
            font = 'DejaVu' if ord(ch) not in AMIRI_CMAP and ord(ch) in DEJA_CMAP else 'Amiri'
            if segs and segs[-1][0] == font:
                segs[-1] = (font, segs[-1][1] + ch)
            else:
                segs.append((font, ch))
        return segs

    def _is_ar(ch):
        o = ord(ch)
        return (0x0600 <= o <= 0x06FF or 0x0750 <= o <= 0x077F
                or 0xFB50 <= o <= 0xFDFF or 0xFE70 <= o <= 0xFEFF)

    def reshape_runs(text):
        """Reshape tiap rentang Arab; Latin dibiarkan."""
        out, buf, in_ar = [], '', False
        for ch in text:
            a = _is_ar(ch)
            if a != in_ar:
                out.append(arabic_reshaper.reshape(buf) if in_ar else buf)
                buf = ''
                in_ar = a
            buf += ch
        out.append(arabic_reshaper.reshape(buf) if in_ar else buf)
        return ''.join(out)

    def draw_mixed(text, x, y, font, size, align='left'):
        """Cetak baris campuran Latin+Arab dengan bidi benar.

        1) reshape rentang Arab, 2) bidi seluruh baris, 3) gambar per potongan
        font mengikuti urutan visual (Amiri untuk Arab, DejaVu untuk Latin).
        """
        vis = get_display(reshape_runs(text))
        segs = []
        buf, cur = '', None
        for ch in vis:
            kind = 'Amiri' if (_is_ar(ch) or (ch not in ' ' and ord(ch) >= 128
                                              and ord(ch) not in DEJA_CMAP)) else font
            if cur is None:
                cur = kind
            if kind != cur:
                segs.append((cur, buf))
                buf = ''
                cur = kind
            buf += ch
        if buf:
            segs.append((cur, buf))
        total = sum(pdfmetrics.stringWidth(t, f, size) for f, t in segs)
        sx = x - total if align == 'right' else x
        for f, t in segs:
            c.setFont(f, size)
            c.drawString(sx, y, t)
            sx += pdfmetrics.stringWidth(t, f, size)

    def _segments(vis, font, size):
        segs, buf, cur = [], '', None
        for ch in vis:
            kind = 'Amiri' if (_is_ar(ch) or (ch not in ' ' and ord(ch) >= 128
                                              and ord(ch) not in DEJA_CMAP)) else font
            if cur is None:
                cur = kind
            if kind != cur:
                segs.append((cur, buf))
                buf = ''
                cur = kind
            buf += ch
        if buf:
            segs.append((cur, buf))
        return segs

    def wrap_mixed(text, font, size, width):
        """Bungkus baris judul/teks campuran memakai lebar visual sebenarnya."""
        words = text.split()
        lines, cur = [], ''
        for w in words:
            t = (cur + ' ' + w).strip()
            vis = get_display(reshape_runs(t))
            wd = sum(pdfmetrics.stringWidth(x, f, size)
                     for f, x in _segments(vis, font, size))
            if wd <= width - 40 or not cur:
                cur = t
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    def wrap_ar(text, size, width):
        """Bungkus teks Arab pada urutan LOGIS, lalu balik per baris.

        Membungkus string yang sudah di-bidi merusak urutan baca.
        """
        words = text.split()
        lines, cur = [], ''
        for w in words:
            t = (cur + ' ' + w).strip()
            if sum(pdfmetrics.stringWidth(s, f, size) for f, s in arabic_segments(t)) <= width:
                cur = t
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    def new_page():
        c.setFont('DejaVu', 8)
        c.drawString(M, H - 26, 'Sirrul Asrar — Kitab (AR | LAT | ID)')
        c.drawRightString(W - M, H - 26, 'Hal. %d–%d' % (first, last))
        c.line(M, H - 30, W - M, H - 30)
        return H - 52

    def footer():
        c.setFont('DejaVu', 8)
        c.drawCentredString(W / 2, 26, str(c.getPageNumber()))

    # sampul
    y = H - 200
    c.setFont('DejaVu-Bold', 18)
    c.drawCentredString(W / 2, y + 24, 'Sirrul Asrar fi at-Tawashul')
    c.drawCentredString(W / 2, y, "ma'a Ruhaniyyatil Qur'an")
    c.setFont('DejaVu-Bold', 16)
    c.drawCentredString(W / 2, y - 34, 'Kitab Utuh — Transliterasi AR | LAT | ID')
    c.setFont('DejaVu-Bold', 13)
    c.drawCentredString(W / 2, y - 62, 'Halaman naskah %d–%d' % (first, last))
    footer()
    c.showPage()

    # catatan cakupan
    y = new_page()
    c.setFont('DejaVu-Bold', 12)
    c.drawString(M, y, 'CATATAN CAKUPAN')
    y -= 20
    c.setFont('DejaVu', 9)
    notes = [
        'Dokumen induk memuat %d halaman naskah yang sudah ditranskripsi:' % len(pages),
        'Sampul–60 (PDF 1–66), 67–137, dan 239–516.',
        'Halaman 138–238 BELUM dikerjakan dan TIDAK dikarang.',
        'Setiap judul menyebut nomor halaman naskah asli agar mudah dicocokkan dengan rajah.',
        'Tanda [TIDAK JELAS] / [TEKS ASLI DIJAGA] dipertahankan apa adanya.',
    ]
    for n in notes:
        c.drawString(M, y, n)
        y -= 14
    footer()
    c.showPage()

    # daftar isi
    y = new_page()
    c.setFont('DejaVu-Bold', 12)
    c.drawString(M, y, 'DAFTAR ISI (satu judul satu baris)')
    y -= 18
    c.setFont('DejaVu', 8.5)
    for i, (n, title, body) in enumerate(pages, 1):
        if y < 60:
            footer()
            c.showPage()
            y = new_page()
        draw_mixed('%d. Hal. %d — %s' % (i, n, (title or '')[:95]), M, y,
                   'DejaVu', 8.5)
        y -= 11
    footer()
    c.showPage()

    # isi
    for n, title, body in pages:
        y = new_page()
        c.setFont('DejaVu-Bold', 12)
        for hl in wrap_mixed('HALAMAN %d — %s' % (n, title), 'DejaVu-Bold',
                             12, W - 2 * M):
            draw_mixed(hl, M, y, 'DejaVu-Bold', 12)
            y -= 16
        y -= 6

        def draw_img(path):
            nonlocal y
            try:
                img = ImageReader(path)
                iw, ih = img.getSize()
                w = 300.0
                h = w * ih / iw
                if y - h < 60:
                    footer()
                    c.showPage()
                    y = new_page()
                c.drawImage(img, (W - w) / 2, y - h, width=w, height=h)
                y -= h + 10
            except Exception:
                pass

        _secs_probe = sections(body)
        if not _secs_probe:
            for path in images(body):
                draw_img(path)

        def emit(txt, kind, size, indent=0):
            nonlocal y
            if kind == 'AR':
                lines = wrap_ar(txt, size, W - 2 * M - 10)
                step = size + 11
            elif kind == 'H':
                lines = wrap_mixed(txt, 'DejaVu-Bold', size, W - 2 * M - 40)
                step = size + 7
            else:
                lines = wrap(txt, 'DejaVu', size, W - 2 * M - 30 - indent)
                step = size + 4
            for line in lines:
                if y < 60:
                    footer()
                    c.showPage()
                    y = new_page()
                if kind == 'AR':
                    segments = arabic_segments(line)
                    x = W - M - sum(pdfmetrics.stringWidth(s, f, size) for f, s in segments)
                    for f, s in segments:
                        c.setFont(f, size)
                        c.drawString(x, y, s)
                        x += pdfmetrics.stringWidth(s, f, size)
                elif kind == 'H':
                    draw_mixed(line, M, y, 'DejaVu-Bold', size)
                else:
                    draw_mixed(line, M + indent, y, 'DejaVu', size)
                y -= step

        secs = sections(body)
        if secs:
            for num, name, lines in secs:
                y -= 4
                emit('%s. %s' % (num, name), 'H', 10.5)
                for line in lines:
                    if line.startswith('!['):
                        m = re.search(r'\(([^)]+)\)', line)
                        if m:
                            name = os.path.basename(m.group(1))
                            for base in (TIGHT, RAJAH):
                                cand = os.path.join(base, name)
                                if os.path.exists(cand):
                                    draw_img(cand)
                                    break
                        continue
                    if num == '1' and _has_ar(line):
                        emit(line, 'AR', 15)
                    elif line.startswith('- '):
                        emit('• ' + line[2:], 'T', 9, indent=14)
                    else:
                        emit(line, 'T', 9)
                y -= 4
        else:
            for g in paired(body):
                if g[0] == 'T':
                    seq = ((g[1], 'AR', 15), (g[2], 'LAT', 9), (g[3], 'ID', 9))
                elif g[1] == 'AR':
                    seq = ((g[2], 'AR', 15),)
                elif g[1] == 'LAT':
                    seq = ((g[2], 'LAT', 9),)
                else:
                    seq = ((g[2], 'ID', 9),)
                for txt, kind, size in seq:
                    emit(txt, kind, size)
                y -= 8

            for line in extras(body):
                emit(line, 'T', 9)

        footer()
        c.showPage()

    # daftar wafak
    wafak = [(n, images(b)) for n, t, b in pages if images(b)]
    y = new_page()
    c.setFont('DejaVu-Bold', 12)
    c.drawString(M, y, 'DAFTAR WAFAK (%d halaman berwafak)' % len(wafak))
    y -= 22
    for n, imgs in wafak:
        if y < 120:
            footer()
            c.showPage()
            y = new_page()
        c.setFont('DejaVu', 9.5)
        c.drawString(M, y, 'Hal. %d — Gambar wafak/rajah dari naskah asli halaman %d' % (n, n))
        y -= 12
        for path in imgs:
            try:
                img = ImageReader(path)
                iw, ih = img.getSize()
                w = 240.0
                h = w * ih / iw
                if y - h < 60:
                    footer()
                    c.showPage()
                    y = new_page()
                c.drawImage(img, (W - w) / 2, y - h, width=w, height=h)
                y -= h + 8
            except Exception:
                pass
        y -= 6
    footer()
    c.showPage()
    c.save()
    return len(wafak)


if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if what in ('all', 'docx'):
        f, l, w = build_docx()
        print('DOCX ok:', OUT_DOCX, '| hal', f, '-', l, '| wafak', w,
              '| MB', round(os.path.getsize(OUT_DOCX) / 1048576, 2))
    if what in ('all', 'pdf'):
        w = build_pdf()
        print('PDF ok:', OUT_PDF, '| wafak', w,
              '| MB', round(os.path.getsize(OUT_PDF) / 1048576, 2))
