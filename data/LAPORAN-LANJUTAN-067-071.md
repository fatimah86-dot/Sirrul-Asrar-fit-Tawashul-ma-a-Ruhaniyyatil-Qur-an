# LAPORAN LANJUTAN — PDF hal. 67–71 (Bab 2: al-Istisyarah bil-Qur'an)

Tanggal: 2026-11-11 · Branch: `arena/02ad7a12-sirrul-asrar-fit-tawashul-ma-a`
Sumber naskah: `sirrul asror ruhani.pdf` (516 hlm) · Sumber pola: `data/final/asror-tawashul-quran-USER-hal-02-66.txt`

---

## 1. Titik mulai & pemetaan halaman (diuji, bukan ditebak)

Perintah pemilik naskah: *"lanjutkan halaman 67 di pdf aslinya … halaman terakhir yang dikerjakan adalah halaman 60 [pdf aslinya Hal 67]"*.

Hasil uji silang berkas kiriman ↔ PDF:

| Berkas kiriman | Halaman cetak/PDF | Catatan |
|---|---|---|
| `HALAMAN 59` | hal. 64 | akhir Istikharah bi-r-Riqa' |
| `HALAMAN 60` (1 judul) | **hal. 65 + 66** | daftar karya 39 judul + nomor kontak; **dua** halaman cetak |
| — | **hal. 67** | `الْبَابُ الثَّانِي — الِاسْتِشَارَةُ بِالْقُرْآنِ الْكَرِيمِ` ← mulai di sini |
| — | hal. 68–71 | lanjutan, baru dikerjakan sekarang |

**Selisih penomoran = 5 halaman.** Lima halaman yang **tidak ada** di berkas kiriman: `HALAMAN 18, 26, 38, 43, 46` = **cetak hal. 23, 31, 43, 48, 51** (semuanya halaman bergambar/rajah dengan lapisan teks hampir kosong). Ini yang perlu dikirim menyusul.

**Bukti bahwa PDF hal. 67 = `الباب الثاني`** (bukan 68/69): render 200 dpi + pembacaan mata menunjukkan judul itu di **idx 66 = halaman 67**, dan teks yang bergantung padanya (`ويفتح القرآن بيده…`) ada di hal. 68, dan seterusnya sampai hal. 71.

## 2. Hasil kerja

Berkas baru: **`transkripsi/bab2-lanjutan-067-071.md`**

| Halaman | Judul | AR | LAT | ID |
|---|---|---|---|---|
| 67 | Awal Bab Kedua: al-Istisyarah bil-Qur'an al-Karim | 11 | 11 | 11 |
| 68 | Kelanjutan: Fathu al-Mushaf & Adab al-Musyawarah | 15 | 15 | 15 |
| 69 | Tanda Huruful-Fa'l (1): Sehat–Sakit, Kaya–Miskin | 13 | 13 | 13 |
| 70 | Tanda Huruful-Fa'l (2): Tempat, Negeri, & Tempat Orang | 19 | 19 | 19 |
| 71 | Tanda Huruful-Fa'l (3): Keadaan Orang Sakit & Arah | 16 | 16 | 16 |
| **Total** | | **74** | **74** | **74** |

- **Seimbang 74 = 74 = 74** (tidak ada lapis yang lebih panjang → tidak ada blok yang hilang).
- `[TIDAK JELAS]` = **0** (tidak ada dipakai untuk menutupi potongan).
- `[Bersambung ke Hal. X]` = **6** (3 blok hal. 67→68 dan 3 blok hal. 68→69, sesuai tanda sambung cetak `=`).
- Huruf-huruf fa'l ditulis **apa adanya** dari naskah (mis. `اف ك ط ظ ذ ر ز وت ث ه ش غ`) lalu diberi baris LAT & ID yang mengeja huruf yang sama — tidak diterjemahkan, tidak diurutkan ulang.
- Wafaq/rajah: **tidak ada** di hal. 67–71 → **Daftar Wafak tidak bertambah**.
- Tanda `ﷺ` dan `عليه السلام` = ornamen cetak; dicatat di konvensi, tidak diubah.

## 3. Yang BELUM (jujur)

1. Hal. 72 dan seterusnya belum dikerjakan.
2. Halaman cetak **23, 31, 43, 48, 51** belum ada di berkas kiriman → belum bisa disusun berurutan sempurna.
3. Dokumen Word untuk 67–71 belum dibuat; menunggu pemilik naskah menyetujui hasil teks ini dulu (sesuai aturan "jangan lanjut sebelum user cek").
4. PR **#1 tetap DRAFT** — belum merge.

## 4. Cara verifikasi mandiri

```bash
grep -c '^\*\*AR:\*\*'  transkripsi/bab2-lanjutan-067-071.md   # 74
grep -c '^\*\*LAT:\*\*' transkripsi/bab2-lanjutan-067-071.md   # 74
grep -c '^\*\*ID:\*\*'  transkripsi/bab2-lanjutan-067-071.md   # 74
grep -n '^## HALAMAN'   transkripsi/bab2-lanjutan-067-071.md   # 67,68,69,70,71
```
