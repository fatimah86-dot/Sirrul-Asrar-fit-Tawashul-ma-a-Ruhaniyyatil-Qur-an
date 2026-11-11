# LAPORAN TRANSKRIPSI BAB 2 — BATCH 1–9 (Halaman 239–328)

Buku: *Sirrul Asrar fi at-Tawashul ma'a Ruhaniyyatil Qur'an*  
Sumber: `sirrul asror ruhani.pdf`  
Output: `transkripsi/bab2.md`  
Branch: `arena/02ad7a12-sirrul-asrar-fit-tawashul-ma-a`  
Format: AR | LAT | ID; angka wafaq dan rajah dicocokkan dari gambar scan PDF.

## Status halaman dan verifikasi

| Halaman | Isi | Status | Rajah/wafaq | Verifikasi: Gambar Scan PDF (bukan hanya raw_extract) |
|---|---|---|---|---|
| 239–248 | Batch 1; 27 tabel wafaq dari Al-Baqarah sampai Al-‘Ankabut | Selesai; utang audit visual dilunasi | 27 crop tabel asli | Setiap grid 4×4 diperiksa langsung dari render scan 200 DPI; 393 angka lama dikoreksi, tabel Al-Qasas dan Al-‘Ankabut ditambahkan, dan letak tabel dipindahkan ke halaman fisik yang benar |
| 249 | Ar-Rum, Luqman, As-Sajdah | Selesai; semua tabel dicocokkan | Tiga tabel diverifikasi | Scan p.249 dibuka dan angka Ar-Rum, Luqman, As-Sajdah diperiksa langsung; penanda perbaikan/konfirmasi ada di transkripsi |
| 250–258 | Batch 2; wafaq dan teks surah | Selesai; audit angka terdahulu dipertahankan | Angka ditranskripsi | Gambar scan PDF halaman terkait; tidak menggunakan raw_extract sebagai bukti angka |
| 259 | Al-Hashr, Al-Mumtahanah, As-Saff | Selesai; satu bagian tetap tidak terbaca | 3 crop tabel | Scan 200 DPI dan zoom halaman 259; tanda `؟؟؟` setelah «يكتبها في» tidak mengungkap kata/bahan yang hilang |
| 260–268 | Batch 3; wafaq dan teks surah | Selesai | 27 crop tabel | Gambar scan PDF halaman terkait pada 200 DPI; crop berasal dari PDF asli |
| 269–276 | Batch 4; surah-surah pendek dan tabel wafaq | Selesai | 24 crop tabel | Setiap halaman dirender 200 DPI terlebih dahulu; tabel dan angka diperiksa langsung dari gambar scan |
| 277–278 | Lembar judul penutup, mukadimah, nama doa, metode, dan doa | Selesai | Tidak ada rajah amalan | Kedua scan halaman dibuka dan diperiksa; tidak ada wafaq pada halaman 277–278 |
| 279–288 | Batch 5; rangkaian doa/ayat Ya-Sin, petunjuk alternatif, rajah lafaz, dan wafaq angka | Selesai; setiap halaman 279–288 dicocokkan baris demi baris dengan scan 200 DPI | 7 crop rajah; 1 wafaq 4×4 (16 angka); satu angka diperbaiki | Scan tiap halaman ditinjau langsung; 14 pada baris kedua kolom pertama p.284 dibaca dari scan; 5 area ketidakjelasan rajah pp.284–286 dicatat dengan konteks dan alasan |
| 289–298 | Batch 6; kelanjutan doa Ya-Sin, tata cara, kutipan ayat, dua doa baru | Selesai; setiap halaman 289–298 dicocokkan baris demi baris dengan scan 200 DPI | Tidak ada rajah/wafaq; ketiadaan diverifikasi per halaman | Urutan teks dan batas halaman dibetulkan; p.295 memuat 11 pengulangan salam dan p.297 memuat 12 pengulangan «كن فيكون» sesuai scan |
| 299–308 | Batch 7; kelanjutan Ya-Sin, ‘iddiyyah Ya-Sin, petunjuk amalan dan awal doa Ayat Kursi | Transkripsi AR/LAT/ID ditambahkan dan pp.299–300 dibandingkan kembali dengan scan; kutipan p.308 bersambung pada p.309 | 1 crop rajah p.305; tidak ada grid wafaq angka; 0 koreksi angka wafaq; 1 bagian tulisan tangan rajah tidak jelas | Sepuluh scan dibuka pada 200 DPI; teks, jumlah pengulangan dan rajah diperiksa visual. Angka metode disalin dari scan, bukan raw_extract |

**Status keseluruhan:** Batch 5 dan 6 (halaman 279–298) telah selesai diaudit ulang dari scan 200 DPI; Batch 7 (halaman 299–308) tetap selesai ditambahkan. Rincian halaman, koreksi, jumlah baris, crop dan penanda ketidakjelasan hasil audit akhir tercatat pada bagian “Audit Ulang Batch 5 & 6 - LUNAS” di bawah.

## Rekap pelunasan utang verifikasi 1–3

1. **Hal. 259 — Al-Mumtahanah:** Scan menunjukkan tepat tiga tanda tanya (`؟؟؟`) sesudah «يكتبها في». Bagian yang tidak dapat dipastikan ialah apa/bahan/tempat yang dimaksud untuk menulis surah. Konteks terbaca: sebelumnya «من بلي بالطحال» dan «وعسر عليه برؤه»; sesudahnya «ويشربها ثلاثة أيام متوالية» dan «يزول عنه الطحال بإذن الله تعالى». Kalimat tetangga pada scan menyebut khasiat Al-Hashr sebelum entri itu dan Al-Saff setelahnya, tetapi konteks tersebut tidak mengungkap bacaan yang hilang. Tag `[TIDAK JELAS]` dipertahankan dan tidak ada dugaan yang ditambahkan.
2. **Hal. 249 — Ar-Rum, Luqman, As-Sajdah:** Semua tiga tabel diverifikasi dari scan. Deret Luqman dan As-Sajdah diperbarui/ditandai sebagai hasil pemeriksaan gambar; tabel Ar-Rum dan catatan teks Ar-Rum juga dibetulkan dari scan. Angka ada di `transkripsi/bab2.md`.
3. **Hal. 239–248 — audit Batch 1:** Semua 27 grid wafaq fisik diperiksa satu per satu pada render 200 DPI. Sebanyak **393 angka pada daftar lama dikoreksi**; tabel Al-Qasas dan Al-‘Ankabut yang belum tercantum ditambahkan, fragmen/duplikasi Al-A‘raf dibereskan, dan grid dipasangkan dengan halaman scan yang benar. Dua puluh tujuh crop tabel PDF asli disimpan di `assets/rajah/sirrul-asrar/hal-239-rajah-*.jpg` sampai `hal-248-rajah-*.jpg` dan ditautkan di bawah keterangan halaman. Daftar angka tidak diambil dari `raw_extract.txt`.

## Batch 4 — halaman 269–278

- Halaman 269–276: seluruh tabel wafaq yang tampak (24 grid) disalin kanan-ke-kiri, baris demi baris, dari scan. Angka yang tampak ganjil pada sumber—misalnya 514, 565, 1197, 1895, 284, dan 6175—dipertahankan sebagaimana cetakan, tidak dinormalkan menjadi pola yang diasumsikan. Dua puluh empat crop tabel asli ditautkan di transkripsi.
- Halaman 277: judul dekoratif “دعوات روحانية لا غنى عنها”; tidak ada rajah/wafaq amalan.
- Halaman 278: mukadimah, nama-nama doa, cara yang disebutkan, dan petikan doa ditranskripsikan; lafaz khusus ditandai `[TEKS ASLI DIJAGA]`. Angka metode yang tampak pada scan (21 kali/21 hari, 7 kali/36 hari, atau 3 kali/41 hari) disalin dari gambar, bukan dari ekstraksi teks.
- Catatan Batch 4 tersebut hanya meliputi halaman 269–278; Batch 5 halaman 279–288 dicatat terpisah di bawah.

## Rajah dan crop

| Halaman | Crop tabel/rajah |
|---|---|
| 239–248 | 27 crop tabel wafaq dari PDF asli |
| 249–258 | Tidak ada crop terpisah pada batch terdahulu; status ini dicatat apa adanya |
| 259–268 | 30 crop tabel wafaq |
| 269–276 | 24 crop tabel wafaq |
| 277–278 | Tidak ada rajah/wafaq amalan; diverifikasi dari scan |
| 283–286 | 7 crop rajah/tabel dari PDF asli; empat halaman lainnya tidak memiliki rajah |
| 279–282, 287–288 | Tidak ada rajah; diverifikasi dari scan |

Tidak ada scan halaman penuh yang disimpan di `assets/rajah/`; semua berkas di sana merupakan crop tabel.

## Kepatuhan 7 kaidah

| Hukum | Penerapan |
|---|---|
| 1. Rasm dijaga | Bacaan yang tidak jelas tidak ditebak; bagian tak terbaca diberi keterangan sesuai scan. |
| 2. Huruf muqatta‘ah | Lafaz muqatta‘ah dipertahankan bila muncul. |
| 3. Hifẓ al-a‘dād | Angka wafaq di Batch 1, 4, dan 5 dicocokkan dengan gambar scan, bukan raw_extract; anomali cetak dipertahankan. |
| 4. Asma’ Suryani/thilasm | Lafaz khusus dipertahankan dengan tag `[TEKS ASLI DIJAGA]` bila relevan. |
| 5. Istilah falak/hikmah | Istilah khusus tidak diterjemahkan bebas; istilah yang kurang pasti tidak dikarang. |
| 6. Ayat | Rujukan QS dicantumkan apabila teks ayat dikutip. |
| 7. Peringatan syar‘i | Peringatan diterjemahkan utuh; klaim khasiat disajikan sebagai isi sumber, bukan anjuran atau nasihat medis. |

## Verifikasi dan build

Catatan ini merekam keadaan sebelum audit ulang final: pada saat itu kelengkapan Batch 5 dan Batch 6 masih terbuka. Batch 7 (299–308) telah diperiksa terpisah sesuai catatan di bawah. Untuk Batch 5: satu wafaq angka 4×4 berisi 16 angka dan tujuh crop rajah ditautkan. Repo ini tidak menyediakan perintah build otomatis; status akhir pp.279–298 ada pada bagian “Audit Ulang Batch 5 & 6 - LUNAS”.

**Kesimpulan terdahulu (sebelum audit ulang final):** Batch 7 telah ditambahkan hingga p.308. Saat catatan historis ini ditulis, Batch 5–6 masih memerlukan audit ulang; hasil finalnya kini dicatat pada bagian “Audit Ulang Batch 5 & 6 - LUNAS”.

## Perbaikan Batch 5: dari ringkasan menjadi transkripsi penuh

- **Cakupan scan:** pp.279–288 dirender pada 200 DPI sebelum penyalinan; scan menjadi sumber utama. Untuk rajah pp.284–286 juga dilakukan pemeriksaan crop beresolusi lebih tinggi. Ekstraksi teks PDF tidak dipakai sebagai bukti angka.
- **Perubahan terukur:** patch perbaikan menambahkan **202 baris teks** pada transkripsi, termasuk **123 baris berlabel AR/LAT/ID (41 set)**. Baris Indonesia baru memiliki **276 tanda akhir kalimat/segmen** menurut hitungan mekanis tanda titik, tanda tanya, dan tanda seru; hitungan ini mekanis dan segmen dalam tabel bukan kalimat prosa.
- **Halaman dengan omisi terbanyak:** **hal. 286**, yang pada versi sebelumnya hanya diberi deskripsi ringkas untuk dua kisi besar (7×7 dan 8×8). Perbaikan kini mencatat unsur lafaz yang dapat dibaca dan menyebut secara eksplisit bagian sel yang tetap tidak dapat dipastikan; crop asli tetap berada tepat di bawah uraian masing-masing kisi. Halaman 285 juga memuat kisi bertulisan buram dan diberi perlakuan sama.
- **Hal. 279–283:** uraian diperluas dengan doa, bacaan Ya-Sin dan seruan sesuai bagian yang dapat dibaca. Kelanjutan lintas halaman dan lafaz khusus dipertahankan; titik pemisah hanya dinyatakan sebagai cetakan apabila memang terlihat pada scan.
- **Hal. 284:** lafaz yang dapat dikenali pada rajah pertama dicatat; bentuk lain yang tidak dapat dipisahkan ditandai `[TIDAK JELAS - LIHAT PDF HALAMAN 284]` dengan sebab dan konteks. Wafaq angka diperiksa ulang pada scan: **1 13 11 8 / 12 7 2 13 / 6 9 16 3 / 15 4 5 10**, dibaca kanan-ke-kiri per baris. Pola 16 angka, pengulangan 13 pada baris kedua, serta penanda `[ANGKA SEPERTI DI SCAN]` tetap dipertahankan—tidak dinormalkan.
- **Hal. 285–286:** tiap kisi dicatat sebagai unit visual terpisah, unsur yang cukup terbaca ditulis, dan kelompok lafaz yang tidak dapat dibaca diberi penanda dengan alasan (huruf berhimpitan, tinta/cetakan kabur) serta konteks letaknya pada halaman. Rajah bukan prosa berjalan; halaman tidak mempunyai kalimat asli pengantar/penutup yang mengapit sel-sel, sehingga catatan konteks membedakan keterangan editor dari bacaan scan. Crop menjaga semua isi visual yang belum dapat ditransliterasi.
- **Rajah dipertahankan:** tujuh crop lama tetap ditautkan dan ditempatkan di bawah uraian terkait: p.283 satu; p.284 dua; p.285 dua; p.286 dua. Tidak ada crop yang dipindah atau dihapus.
- **Catatan batas:** tulisan yang masih tidak terbaca pada sel-sel rajah pp.284–286 belum dapat ditranskripsi lengkap; semuanya ditandai, tidak diganti “dst” atau ringkasan seolah-olah sebagai transkripsi. Penanda ketidakjelasan ditempatkan dekat materi dan menyebut halaman serta alasan/konteks.

**Validasi historis:** tujuh tautan crop diperiksa keberadaan berkasnya; wafaq p.284 dibandingkan dengan render scan; `git diff --check` dijalankan setelah perubahan. Pemeriksaan final setelah tahap historis ini dirangkum di bagian “Audit Ulang Batch 5 & 6 - LUNAS”.

---

## Bab 2 — Batch 6: halaman 289–298

- Seluruh scan pp.289–298 dirender 200 DPI dan ditinjau sebelum penyalinan. Transkripsi ditambahkan dalam format AR | LAT | ID untuk tata cara, doa dan ayat Surah Ya-Sin yang tercetak pada halaman.
- Batch ini **tidak memuat rajah atau tabel wafaq**; tiap halaman diperiksa langsung dan diberi keterangan tidak ada rajah. Tautan crop terdahulu tetap ada dan tervalidasi.
- Pada scan halaman 295, «سلام قولًا من رب رحيم» muncul 11 kali; pada halaman 297 ayat «إنما أمره إذا أراد شيئًا أن يقول له كن فيكون» muncul berulang. Pengulangan dicatat dalam transkripsi sebagaimana terbaca pada scan; angka hitungan ini bukan wafaq.
- Penanda halaman 298 memperkenalkan doa lain untuk ru’yat al-Nabi, tetapi tidak menandai awal bab baru (tidak tampak judul «باب» atau «فصل» pada scan), sehingga halaman tetap berada di `transkripsi/bab2.md`.
- Pemeriksaan akhir batch: render scan 200 DPI; seluruh tautan crop dalam dokumen ada; `git diff --check` bersih.

## Bab 2 — Batch 7: halaman 299–308

- Semua halaman 299–308 dirender dari PDF pada 200 DPI sebelum penyalinan dan ditinjau kembali sebagai gambar. pp.299–300 dibandingkan ulang dengan scan: doa salawat di p.299 disalin pada dua tempat sebagaimana cetakannya; kutipan Ya-Sin p.300 mencakup ayat 25–54, termasuk pengulangan salawat dan ayat 48–54 di bagian bawah.
- Halaman 301–303 memuat kelanjutan Ya-Sin dan rangkaian pengulangan. «سلام قولًا من رب رحيم» pada p.301 ditulis 12 baris sesuai scan; «إنما أمره إذا أراد شيئًا أن يقول له كن فيكون» pada p.303 ditulis 12 baris. Pengulangan juga dieja lengkap pada LAT dan ID, tidak diganti “dst/dll”.
- Halaman 304–308 ditranskripsikan dalam urutan AR | LAT | ID. Teks pada p.304 berlanjut di p.305; kutipan di akhir p.308 berlanjut ke p.309, tanpa melengkapi bagian yang belum tampak. Tidak ada nomor wafaq/grid angka pada batch ini: **0 koreksi angka wafaq**. Bilangan amalan yang tampak, termasuk 7, 12, 14, 35, dan 102, disalin dari scan.
- **Rajah:** satu crop rajah p.305 dibuat langsung dari PDF pada `assets/rajah/sirrul-asrar/hal-305-rajah-01.jpg`, ditautkan langsung di bawah keterangan halaman. Sebagian tulisan tangan kecil di dalam rajah tidak dapat dipastikan karena goresan bertumpuk/buram; dicatat dengan `[TIDAK JELAS - HALAMAN 305]`. Hal. 299–304 dan 306–308 diperiksa dan tidak memuat rajah/tabel; absence markers ada per halaman. **Jumlah crop Batch 7: 1; jumlah bagian tidak jelas: 1 (tulisan rajah p.305).**
- Tidak ada angka wafaq yang dikoreksi. `git diff --check` dan keberadaan semua tautan crop diperiksa sebelum commit.

## Audit Ulang Batch 5 & 6 - LUNAS

Semua halaman 279–298 dibandingkan langsung, baris demi baris, dengan scan PDF yang dirender pada 200 DPI. `raw_extract.txt` tidak digunakan sebagai bukti untuk angka wafaq. Kutipan dan pengulangan dipertahankan sesuai urutan serta batas halaman; bagian yang benar-benar tidak dapat dibaca diberi alasan, konteks, dan tautan crop apabila berupa rajah.

### Rekap hasil

- **Transkripsi penuh:** 579 baris Markdown ditambahkan pada bagian halaman 279–298 dibandingkan dengan baseline sebelum Batch 5 (`f62536f^`); hitungan dilakukan pada bagian per halaman, bukan pada catatan laporan.
- **Koreksi angka wafaq:** 1 angka. Pada p.284, sel baris kedua kolom pertama dibaca **14** dari scan (bukan 12 pada versi awal) dan diberi tag `[DIPERBAIKI DARI GAMBAR SCAN]`. Wafaq 4×4 berisi 16 angka; nilai lain tidak dinormalkan.
- **Ketidakjelasan:** 11 kemunculan tag lama dihapus atau dikonsolidasikan dibanding snapshot sebelum audit final (`e12277e`): dua bagian pada pp.281–282 dapat dibaca dari scan; delapan tag berulang pada uraian AR/LAT untuk kisi pp.285–286 digabungkan menjadi satu catatan per kisi; satu tag literal pada catatan verifikasi lama dibersihkan. **Lima area isi yang tetap tidak terbaca** dipertahankan: satu bagian rajah p.284, dua kisi p.285, dan dua kisi p.286; masing-masing menyebut alasan dan konteks halaman.
- **Rajah/crop:** tujuh crop asli tetap ada dan tertaut tepat di bawah keterangan rajah: p.283 (1), p.284 (2), p.285 (2), p.286 (2). Semua tautan diperiksa keberadaan filenya. Tidak ada rajah pada pp.279–282 dan 287–298; ketiadaan dicek dari scan per halaman.
- **Pengulangan terukur dari scan:** p.295 memuat 11 baris «سلام قولًا من رب رحيم»; p.297 memuat 12 baris «إنما أمره إذا أراد شيئًا أن يقول له كن فيكون».

### Catatan audit per halaman

| Halaman | Hasil pencocokan scan 200 DPI dan perbaikan | Rajah/wafaq | Baris baru* |
|---:|---|---|---:|
| 279 | Doa, Ya-Sin 1–21, seruan dan kelanjutan yang terpotong di batas halaman dicocokkan; penomoran terjemahan mengikuti penanda ayat pada scan. | Tidak ada rajah. | 28 |
| 280 | Sambungan doa, Ya-Sin 22–45, seruan, dan titik sambung ke p.281 dicocokkan; frasa pembuka «يا جميع» dipertahankan sesuai scan. | Tidak ada rajah. | 45 |
| 281 | Ya-Sin 45–64, Ayat Kursi, seruan dan rangkaian nama di bagian bawah dicocokkan; rangkaian yang sebelumnya diragukan terbaca dan penanda ketidakjelasan dihapus. | Tidak ada rajah. | 29 |
| 282 | Lafaz khusus, seruan, dan Ya-Sin 65–83 ditranskripsikan sesuai urutan halaman; tidak tersisa marker untuk bagian cetak yang dapat dibaca. | Tidak ada rajah. | 20 |
| 283 | Seruan dan kisi 6×6 dicocokkan; urutan lafaz ditulis kanan-ke-kiri dan crop disertakan. | 1 crop; bukan wafaq angka. | 32 |
| 284 | Dua rajah diperiksa; lafaz yang terbaca dicatat dan teks yang bertumpuk tetap ditandai. Wafaq 4×4 dicek dari scan dan angka 12 diperbaiki menjadi 14. | 2 crop; 1 wafaq (16 angka); 1 koreksi angka. | 20 |
| 285 | Dua kisi (6 baris dan 8 baris) diperiksa; bacaan sel yang bertumpuk tidak ditebak, konteks dan alasan ketidakjelasan disertakan. | 2 crop; 2 area tak terbaca. | 20 |
| 286 | Kisi 7 baris dan 8 baris diperiksa; lafaz yang cukup jelas dicatat, bagian kabur tidak direkonstruksi, konteks dan alasan disertakan. | 2 crop; 2 area tak terbaca. | 22 |
| 287 | Metode Ya-Sin, doa, bilangan dan jadwal latihan dicocokkan; angka amalan dan petunjuk akhir halaman dipertahankan. | Tidak ada rajah. | 24 |
| 288 | Kelanjutan petunjuk, perlindungan, doa dan angka amalan dicocokkan; elipsis/garis yang memang tercetak dipertahankan, bagian terpotong ditautkan ke p.289. | Tidak ada rajah. | 41 |
| 289 | Hitungan 16 huruf, cara 409/818, dan uraian tentang latihan dicocokkan baris demi baris. | Tidak ada rajah/wafaq. | 23 |
| 290 | Tata cara dan bacaan lengkap dicocokkan; paragraf nasihat penutup yang sebelumnya terlewat ditambahkan dari scan. | Tidak ada rajah/wafaq. | 29 |
| 291 | Doa metode lain, pembukaan, Ya-Sin 1–12 dan awal tasbih dicocokkan; akhir halaman dibiarkan bersambung. | Tidak ada rajah/wafaq. | 19 |
| 292 | Kelanjutan tasbih dan doa, Ya-Sin 13–17 serta pengulangan di bagian bawah halaman dilengkapi dan diurutkan sesuai scan. | Tidak ada rajah/wafaq. | 31 |
| 293 | Doa lintas halaman, Ya-Sin 18–24, pengulangan tasbih/doa, serta Ya-Sin 25–35 dan awal ayat 36 dipisahkan menurut batas scan. | Tidak ada rajah/wafaq. | 32 |
| 294 | Sisa ayat 36 hingga Ya-Sin 58, tasbih dan doa dicocokkan; awal halaman melanjutkan ayat 36 dari p.293. | Tidak ada rajah/wafaq. | 26 |
| 295 | Sebelas pengulangan salam, Ya-Sin 59–64, tasbih dan doa dicocokkan dari scan. | Tidak ada rajah/wafaq. | 47 |
| 296 | Ya-Sin 65–76 dan dua rangkaian tasbih pada halaman dicocokkan; tajuk rentang ayat dibatasi ke 65–76 dan doa kedua dibiarkan bersambung ke p.297. | Tidak ada rajah/wafaq. | 35 |
| 297 | Kelanjutan tasbih/doa, Ya-Sin 77–83 dan 12 pengulangan «كن فيكون» dicocokkan; duplikasi berlebih dihapus. | Tidak ada rajah/wafaq. | 33 |
| 298 | Judul, mukadimah, Ya-Sin 1–12, selawat panjang dan kutipan Ya-Sin 13–17 dicocokkan; ayat 15–17 yang tertinggal ditambahkan. | Tidak ada rajah/wafaq. | 23 |
| **Total** | **Semua pp.279–298 diaudit langsung terhadap scan.** | **7 crop; 1 wafaq; 1 koreksi angka.** | **579** |

\* Hitungan baris baru adalah selisih penambahan pada bagian halaman masing-masing terhadap baseline sebelum Batch 5; bukan hitungan kalimat atau baris cetak pada scan.

**Validasi final Batch 5–6:** `git diff --check` bersih; ketujuh tautan crop pp.283–286 diperiksa dan berkasnya ada. Commit titik aman untuk p.290 dan p.292–298 tersimpan sebagai `82b5cd1`; audit final ini dicatat terpisah. Batch 8 mulai dikerjakan pada pp.309–311; audit dan commit final Batch 8 belum selesai.

## Bab 2 — Batch 8 (SELESAI): halaman 309–318

- Cakupan pp.308–318 dirender pada 200 DPI sebelum penyalinan. Sambungan ayat QS al-Mujādilah 58:21 dari p.308 ke p.309 dipertahankan. pp.309–311 memakai hasil pemeriksaan scan terdahulu dan tidak diulang sesuai instruksi; pp.312–315 dicocokkan lagi dengan scan 200 DPI; pp.316–318 dibaca dari scan yang tersimpan dan bagian yang samar diberi konteks, tanpa melengkapi kata yang tidak tampak.
- Semua halaman 309–318 memiliki AR | LAT | ID. Penambahan/koreksi khusus Batch 8 mencakup pelengkapan instruksi rajah di akhir p.314 yang merujuk pada p.315, uraian batas halaman dan bagian tak terbaca, serta pembetulan alur sambungan p.317–318 tanpa menyisipkan kata yang tidak terbaca.
- **Rajah/crop: 2.** Kisi 3×3 tulisan tangan p.309 (`hal-309-rajah-01.jpg`) dan khatam lingkaran/persegi «حجاب القفل الكبير» p.315 (`hal-315-rajah-01.jpg`) dicrop dari PDF asli dan disisipkan langsung di bawah keterangannya. pp.310–314 dan 316–318 diperiksa dari scan dan diberi penanda tidak ada rajah. Crop p.315 diperiksa ulang: dua petak segitiga berhadapan menunjukkan tiga guratan tegak, dicatat «111» **[ANGKA SEPERTI DI SCAN]** tanpa normalisasi; tulisan lain pada rajah tidak cukup jelas.
- **Koreksi angka wafaq: 0.** Tidak ditemukan grid wafaq numerik pada pp.309–318; tidak ada angka wafaq yang dikoreksi. Bilangan dalam instruksi dan tanda «111» pada rajah disalin sebagaimana terlihat, bukan dipaksakan menjadi pola numerik.
- **[TIDAK JELAS]: 10 penanda.** Mencakup kisi tulisan tangan p.309; satu bagian rusak p.312; objek yang hilang pada baris-baris seruan p.313; tiga objek/seruan kabur p.314; dua aspek keterbacaan rajah p.315; rangkaian nama kabur p.316; satu frasa rusak p.317; serta dua bagian/batas halaman p.318. Semua diberi konteks; tidak ada bagian kosong yang ditebak.
- **Validasi:** 91 tautan crop dalam dokumen semuanya menunjuk ke berkas yang ada; setiap halaman p.309–318 mempunyai heading tunggal dan AR/LAT/ID; `git diff --check` bersih. Render sementara dibersihkan setelah audit final.
- Commit titik aman Batch 8: `Bab 2 Batch 8: hal. 309–318`.

## Bab 2 — Batch 9 (SELESAI): halaman 319–328

- Scan pp.319–328 dirender pada 200 DPI dan ditinjau per halaman, dengan p.318/p.319 dan p.328/p.329 sebagai konteks sambungan. Halaman 319–320 menutup sumpah sebelumnya; p.321–324 menjelaskan penyiapan tinta dan seruan; pp.325–326 berisi khatam serta bahan dupa; pp.326–328 memulai «الدرة المكنونة» dan seruan «الطهاطيل الكبرى». Semua halaman batch memiliki AR | LAT | ID dan entri untuk gambar/ketiadaan rajah.
- **Rajah/crop: 2.** Khatam dengan tulisan pada dinding p.321 (`hal-321-rajah-01.jpg`) dan khatam enam lingkaran p.325 (`hal-325-rajah-01.jpg`) dicrop langsung dari halaman PDF asli dan disisipkan setelah caption masing-masing. Kedua gambar diperiksa agar bingkai rajah utuh dan teks caption halaman tidak ikut terpotong masuk ke crop. Rajah tulisan tangan mengandung lambang yang tak terbaca; tidak dinormalisasi sebagai angka.
- **Audit ulang setelah draf awal.** Seluruh pp.319–328 dibandingkan ulang baris demi baris dengan scan. Audit ini menemukan dan memperbaiki:
  1. **Satu bagian hilang di p.321.** Paragraf «شرح الطريقة المباركة» (mulai hari Kamis saat matahari terbenam, bahan dupa cendana/muql biru/daun ās/getah Maghribi, air mawar jūrī 250 gram) sebelumnya tidak ikut tertranskripsi; kini ditambahkan AR | LAT | ID.
  2. **Satu koreksi angka.** Hitungan pada aṣrāf p.328 terbaca «آية الكرسي ٣ مرات» (bukan ٧) pada scan; angka diperbaiki dan diteruskan ke terjemahan. Angka lain yang diperiksa (779 kali pada p.324, 33 kali pada p.323, 21 kali pada p.319–320, 12 kali pada p.320, 11/7/3 pada p.322, 3 hari pada p.326) sesuai cetakan.
  3. **Koreksi bacaan** pada rangkaian nama dan lafaz yang sebelumnya salah baca, antara lain «بإنجيل عيسى» (bukan «بالمسيح عيسى»), «بحق شلشليش», «يا شمخ نطيطيون», «صباوثون»، «دهميثا دهليلوا»، «مشلآمون مشمخ مشخيثا»، «بحول أقسمت»، «فإذا هم جميعا واحدة»، «بسم الله» pada p.319; «براهيا», «شداي»، «لمع البرق»، «لقسم عظيم»، «روقيائيل»، «طحيطمغيليائيل»، «شمخاباروخ»، «كفعيائيل»، «مهليع»، «هلطيموش»، «هلعيموش»، «طيوناش»، «بكهكهين»، «طعطعوش»، «ردوحا»، «أشمرال» pada p.320; «سيهَاب، سمخاروب، طيهانوب» dan «بتبدورة إسفنجية» pada p.322; «ديمانونخ»، «طزنماخ»، «نواطيخ»، «أينكم»، «شمارخون»، «بياموئيل»، «طحيطمغيليائيل» pada p.323; «خلوها»، «انطوت»، «الطغاة»، «حسوديا» pada p.324; «فانفجرت»، «ونزيرا» pada p.326; «ألا ما حضرتم دعوتي»، «بالمحاريق» pada p.327; serta «كسبرة ناشفة» pada p.328. Semua perbaikan mengikuti bentuk yang tampak pada scan 200 DPI dan lapisan teks PDF asli; tidak ada kata yang direka.
  4. **Sisa tanda yang tak terbaca** dipertahankan: rangkaian nama yang hurufnya bertumpuk tetap ditandai `[TIDAK JELAS]` dengan konteks, dan lafaz pada baris terakhir p.319 yang terpotong di batas halaman dibiarkan bersambung ke p.320.
- **Koreksi angka wafaq: 0.** Tidak ada grid wafaq numerik pada pp.319–328; angka yang dikoreksi di atas adalah hitungan amalan, bukan sel wafaq. Lambang di dalam rajah tidak dikonversi menjadi angka.
- **[TIDAK JELAS]: 7 penanda** pada pp.319–320, 323–325, 327–328 untuk rangkaian nama khusus yang sangat rapat, tulisan rajah, dan bagian seruan yang bentuk cetaknya tidak memungkinkan pembacaan pasti. Tiap penanda menyertakan konteks/alasan; lafaz nama khusus dipertahankan sebagai bunyi, bukan diterka maknanya. Batas akhir p.328 sengaja dibiarkan bersambung ke p.329.
- **Validasi final:** semua halaman pp.319–328 memiliki satu heading dan setidaknya satu set AR/LAT/ID (p.319 dan p.327 memang satu blok AR/LAT/ID panjang sesuai bentuk halaman); 93 tautan crop dalam keseluruhan dokumen mengarah ke berkas yang ada; `git diff --check` bersih. Render dan OCR sementara dibersihkan setelah audit batch. Commit: `Bab 2 Batch 9: hal. 319–328`.

## Bab 2 — Batch 10 (SELESAI): halaman 329–338

- Scan pp.329–338 dirender pada 200 DPI dan dibaca satu per satu, dengan p.328/p.329 dan p.338/p.339 sebagai konteks sambungan. Isi batch: penutup «الطهاطيل السبعة» p.329–330 (nama malaikat, tujuh raja, syarat amal, bahan dupa); «الدعوة البهلولية» p.331 (taṣrīf, khādim «صيهوع», raja per hari); sumpah Yahudi–Nasrani–Muslim dan khatam doa p.332; awal «رياضة سورة يس» p.333–334; penutup doa serta khādim «لطيف» p.335; jadwal hurufiah «لطيف», «استخدام الجن المؤمن», dan «باب استحضار فرد من أفراد الجن» p.336; «قسم ابتداء العزائم» p.337; «دعاء الأنوار» p.338. Semua halaman memiliki AR | LAT | ID.
- **Sambungan antarhalaman.** «يا مبدئ يا» di akhir p.334 bersambung ke «معيد يا فعال لما يريد» di awal p.335 dan diberi penanda sambungan; sumpah ruh Muslim «وإن كنتم من أشباح أرواح المسلمين…» yang tercetak di baris pertama p.338 dipindahkan ke blok p.338 (bukan p.337) sesuai letak cetaknya; doa «دعاء الأنوار» p.338 berakhir di tengah «أجب أنت و…» dan sengaja dibiarkan bersambung ke p.339.
- **Rajah/crop: 2.** Khatam lingkaran dengan bintang di dalamnya p.330 (`hal-330-rajah-01.jpg`, clip Rect(75,318,507,710) @400 DPI) dan bintang lima bersudut tebal p.332 (`hal-332-rajah-01.jpg`, clip Rect(183,331,431,553) @500 DPI). Crop pertama sempat bergeser (memuat judul dan memotong lingkaran) lalu diulang memakai bbox `get_image_info()`; crop kedua sempat memuat sliver teks di atas lalu dipangkas. Kedua hasil diperiksa dengan mata sebelum disisipkan. pp.329, 331, 333–338 diperiksa dan diberi penanda tidak ada rajah.
- **Koreksi bacaan hasil audit ulang** (dibandingkan dengan lapisan teks PDF dan scan 200 DPI): «معيد» (bukan «مَعِيدُ» sebagai kata baru), «رُوقِيَائِيلُ»، «لطيف» pada khādim, «تُحِيطُهَا» (bukan «تُخَلِّطُهَا»)، «امْلَأِ الطَّاسَةَ» (bukan «أَمْدُدِ»)، «حَتَّى يَنْتَهِيَ غَلَيَانُهُ… وَانْظُرْ بِدَاخِلِهَا… مُلُوكَ السَّبْعَةِ… لَا يَنْتَظِرُ، بَلِ انْوِ غَرَضَكَ»، «التَّفْرِيجِ» (bukan «التَّعْرِيجِ») dan «التَّفْرِيقَةِ» pada judul penggunaan jin mukmin, «الرَّوَاحُ الرُّوحَانِيَّةُ تَجْلِبُ لِلْأَعْدَادِ»، «أُولَى لِلْخَدِيمِ»، «وَصُنْهُ جُهْدَكَ وَإِيَّاكَ وَإِفْشَاءَهُ»، serta daftar raja p.337: «مُرَّة بن الحارث» (Senin), «أبو عزر الأحمر» (Selasa), «برقان اليهودي» (Rabu), «شمهورش القاضي ابن الوليد» (Kamis), «أبو النور الأبيض زوبعة» (Jumat), «ميمون السحابي» (Sabtu) — bentuk-bentuk ini berbeda dari daftar raja pada halaman-halaman sebelumnya dan dicatat sebagaimana tercetak. Duplikasi «ومرة صاحب يوم الاثنين» yang muncul saat penambalan dihapus. Kata «أُقْسِمْتُ» dinormalkan menjadi «أَقْسَمْتُ» sesuai kaidah dan bentuk yang dipakai halaman lain; «تامة راضية» dan «كهيعص حمعسق» dirapikan.
- **Koreksi angka wafaq: 0.** Tidak ada grid wafaq numerik pada pp.329–338. Angka yang diperiksa dan sesuai cetakan: الوحا ٢/العجل ٢/الساعة ٢ (p.330), ٣ أيام dan ١١٢ kali (p.331), ٣/٧/٧/٧ pengulangan istiḥḍār (p.336), ١٠٠ istighfar dan ١٠٠ selawat (p.336), serta hitungan ٣/٧ pada p.335. Angka «١٢١» untuk Surah al-Kāfirūn p.336 disalin apa adanya dan diberi catatan (lazimnya ١٠٠), bukan diubah.
- **[TIDAK JELAS]: 10 penanda** (p.329, p.330, p.331, p.332, p.333, p.334, p.335, p.336, p.337, p.338) untuk rangkaian nama yang sangat rapat, kata rusak pada paragraf jadwal, lafaz «شمخيثا/كسفبائيل», bait «لطيف» yang tidak terbaca sebagai kosakata baku, dan batas halaman yang terpotong. Tiap penanda menyertakan alasan; tidak ada kata yang ditebak atau dilengkapi.
- **Validasi final:** 100 bagian halaman dalam `transkripsi/bab2.md`; setiap halaman pp.329–338 memiliki jumlah blok AR = LAT = ID; 95 tautan crop menunjuk ke berkas yang ada; tidak ada baris kosong ganda; `git diff --check` bersih. Commit: `Bab 2 Batch 10: hal. 329–338`.
