# Pedoman 1: KMI & Versi Kernel (CRITICAL)

> [!IMPORTANT]
> Pedoman ini merupakan aturan dasar yang bersifat krusial untuk menjaga stabilitas kompilasi dan mencegah kegagalan booting pada perangkat Xiaomi Redmi 12 (fire). Jangan mengubah aturan di bawah ini tanpa pengujian menyeluruh.

---

## 1. Gunakan Posisi HEAD Terbaru (Tip of Branch)
* **Aturan Utama**: Gunakan posisi HEAD terbaru dari cabang `common-android15-6.6`. Jangan pernah mengunci versi kernel ke commit spesifik (seperti commit lama 6.6.58).
* **Rasionalisasi**: Berdasarkan hasil pengujian rilis v70 (versi 6.6.129) yang sukses melakukan booting, kernel memerlukan pembaharuan terkini dari upstream cabang Android. Mengunci versi kernel ke commit lama `33c1ba9ffede` (6.6.58) terbukti memicu **bootloop** pada semua build yang dilakukan sejak bulan Mei 2026.
* **Implementasi**: Biarkan proses `repo sync` mengambil HEAD terbaru dari cabang utama. Hindari penambahan perintah `git fetch` atau `git checkout` ke commit lama secara manual pada berkas workflow.

---

## 2. Format Kompresi Kernel Utama
* **Aturan Utama**: Gunakan konfigurasi kompresi kernel bawaan dari arsitektur Generic Kernel Image (GKI).
* **Rasionalisasi**: Sistem pemuatan modul dan kompresi ramdisk Android 15 telah dioptimalkan secara spesifik oleh Google untuk format kompresi tertentu. Memaksa kompresi ke format lain (seperti memaksakan GZIP secara absolut dan menghapus LZ4) dapat menyebabkan bootloader MediaTek gagal mendekode kernel dengan benar.
* **Implementasi**: Jangan memaksakan flag `CONFIG_KERNEL_GZIP=y` secara agresif atau menghapus dukungan `CONFIG_KERNEL_LZ4=y`. Biarkan parameter kompresi berjalan sesuai konfigurasi default GKI.

---

## 3. Prioritas Format Citra Kernel pada AnyKernel3
* **Aturan Utama**: Utamakan ekstraksi dan pengemasan citra terkompresi `Image.gz` dalam paket AnyKernel3.
* **Rasionalisasi**: Chipset MediaTek Helio G88 pada Redmi 12 memiliki struktur bootloader vendor yang sangat sensitif terhadap format citra kernel. Format raw `Image` tanpa kompresi seringkali ditolak secara langsung oleh bootloader, menyebabkan perangkat langsung terlempar ke mode Fastboot.
* **Implementasi**: Proses pengemasan AnyKernel3 harus memindai dan memilih citra kernel dengan urutan prioritas sebagai berikut:
  1. `Image.gz` (Prioritas Utama / Kompatibilitas Terbaik)
  2. `Image.lz4` (Cadangan Pertama)
  3. `Image` (Cadangan Terakhir / Fallback)

---

## 4. Penambahan Optimasi Secara Bertahap
* **Aturan Utama**: Jangan menambahkan bendera (flags) optimasi kompilasi secara masif tanpa pengujian booting individu.
* **Rasionalisasi**: Konfigurasi optimasi ekstrem seperti `CONFIG_DEBUG_KERNEL=n` atau `CONFIG_FUNCTION_TRACER=n` yang terkesan meningkatkan performa, secara faktual merusak dependensi subsistem pelacakan BPF pada Android 15, memicu kegagalan inisialisasi jaringan dan berujung pada bootloop.
* **Implementasi**: Setiap perubahan konfigurasi optimasi harus diuji secara terpisah dengan siklus: *Kompilasi* → *Pemasangan* → *Verifikasi Booting* → *Commit*. Jika terdapat keraguan, biarkan optimasi tersebut dinonaktifkan.
