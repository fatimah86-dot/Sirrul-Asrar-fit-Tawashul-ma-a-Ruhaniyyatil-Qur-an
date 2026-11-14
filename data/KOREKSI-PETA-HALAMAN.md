# KOREKSI PETA HALAMAN — hasil Langkah (a)

Tanggal: 2026-11-11 · Branch: `arena/02ad7a12-sirrul-asrar-fit-tawashul-ma-a`
Cakupan: 16 baris yang masih bertanda `±` + 1 baris yang ternyata bertanda `±` tetapi tidak terdeteksi sebelumnya.

## Ringkasan

| Jumlah | Status |
|---|---|
| Baris bertanda `±` di berkas (ternyata) | **16**, bukan 10 |
| Baris yang **nomornya salah** dan dibetulkan | **12** |
| Baris yang nomornya benar (hanya naik status) | 4 |
| Sisa baris `±` di seluruh peta | **0** |

Daftar 16: bagian **4, 5, 6, 24, 25, 27, 28, 29, 30, 31, 32, 33, 40, 41, 42, 44**.
(Bagian 4/5/6 terlewat dari hitungan awal karena `±`-nya menempel pada angka kecil.)

## Koreksi nomor (salah → benar) + sebabnya

| Bagian | Sebelum | Sesudah | Sebab |
|---|---|---|---|
| 24 | ±28 | **28–29** | Daftar karya itu **berlanjut** ke halaman cetak 29. Di PDF 28 belum habis, PDF 29 memuat sisa ("شفاء العليل …" dst.). Satu bagian = dua halaman cetak. |
| 25 | ±30 | **31** | Judul `الباب الأول — التفاؤل بالقرآن الكريم` + `طريقة العمل` terbaca di **PDF 31**. PDF 30 hanya hiasan ornamen pembuka. |
| 29 | ±34 | **35** | `الوجه الأول … وجعه يوم الاثنين … يكتب له آخر الحشر` terbaca di **PDF 35**; PDF 34 memuat `وأنزلنا هذا القرآن` milik bagian 28. |
| 30 | ±35 | **36** | `* إن كان حرف «ح» فيه أربعة وجوه` terbaca di **PDF 36** (posisi paling atas). |
| 31 | ±36 | **37** | `اكتب له الفاتحة والإخلاص والمعوذتين، ويحملهم على رأسه` terbaca di **PDF 37**. |
| 32 | ±37 | **38** | `اللهم أصلح أمة محمد …` + `ويكتب له حجاب من سورة الأنبياء` terbaca di **PDF 38**. |
| 33 | ±38 | **39** | `* إن كان حرف «س» فيه سبعة وجوه` terbaca di **PDF 39**. |
| 39 | ±46 | **45** | `* إن كان حرف «ق» فيه أربعة وجوه` terbaca di **PDF 45**. |
| 40 | ±47 | **46** | `الوجه الثالث … نام على وجهه فلحقه أذى — يكتب له: الصافات والفاتحة` terbaca di **PDF 46**. |
| 41 | ±48 | **47** | `يكتب له ﴿ارجع البصر كرتين ينقلب إليك البصر خاسئًا وهو حسير﴾` terbaca di **PDF 47**. |
| 42 | ±49 | **48** | `الوجه الثالث … مرضه من الله سبحانه وتعالى` terbaca di **PDF 48**. |
| 45 | ±50 | **50** | Dipastikan: `الاستشفاء بالقرآن` **satu halaman** dengan bagian 44 (PDF 50). Bagian 44 = potongan atas, bagian 45 = potongan bawah halaman yang sama. |

## Naik status saja (nomor sudah benar)

| Bagian | PDF | Bukti |
|---|---|---|
| 4 | 4 | `من إصدارات شيخ الروحانيين … في المكتبات` — 26 baris cocok di PDF 4, juga muncul di PDF 28/65/76 (pengulangan cetakan) |
| 5 | 5 | `كتاب الأوفاق وخواص كل وفق` — cocok di PDF 5 |
| 6 | 6 | Halaman scan: `الفصل الأول — فضل بعض الآيات والسور من القرآن الكريم` + `للمتابعة والتواصل 0020162022238` |
| 27 | 32 | `الوجه الثاني … لحقه مارد من الأرض يوم الجمعة` terbaca di PDF 32 |
| 28 | 33 | `الوجه الثاني … لحقه وسواس وبعض تفكر … فدخل عليه` terbaca di PDF 33 |
| 44 | 50 | `الوجه الثالث … غيظ وكمد كثر فيه صراعه` (4 baris) di PDF 50 |

## Metode (agar bisa diulang)

1. Halaman **berlapis teks** (PDF 1–29, 65–66): pecah tiap bagian menjadi baris Arab, normalkan (NFKC, buang harakat/tatwil, buang header berjalan), lalu cocokkan substring ke teks tiap halaman; ambil halaman yang cocok paling banyak dan tidak ambigu.
2. Halaman **scan tanpa lapisan teks** (PDF 30–64): render 200–300 dpi, potong **band atas** (~6–17 % tinggi) per halaman, gabung 5–6 halaman per lembar kontak, lalu dibaca dengan mata. Kata kunci yang terbaca dicocokkan ke baris pertama/terakhir bagian yang bersangkutan.
3. Kesimpulan hanya dipakai kalau kata kunci terlihat **persis**; kalau tidak, baris tetap ditandai `±` (kali ini tidak ada yang tersisa).

## Catatan

- **Isi teks tidak diubah** sama sekali — hanya nomor halaman pada judul dan status verifikasi.
- Halaman cetak yang **belum punya bagian**: **12, 14, 17, 20, 23, 30, 34, 44, 49, 51**.
- Bagian **60** tetap `65–66` (dua halaman cetak).
