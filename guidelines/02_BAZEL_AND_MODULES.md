# Pedoman 2: Bazel Build & Konfigurasi Modul

> [!WARNING]
> Kegagalan dalam mematuhi pedoman ini dapat menyebabkan kegagalan kompilasi total pada alur kerja CI/CD (Kleaf Bazel Sandbox) atau memicu kegagalan pemuatan driver perangkat keras setelah kernel terpasang.

---

## 1. Kompilasi ZRAM & ZSMALLOC Sebagai Modul
* **Aturan Utama**: Modul ZRAM dan ZSMALLOC wajib dikompilasi sebagai modul dinamis (`=m`), bukan statis (`=y`), dan tidak boleh dinonaktifkan (`=n`).
* **Rasionalisasi**: Kleaf (sistem kompilasi Bazel bawaan Google untuk GKI 6.6) memiliki konfigurasi pelacakan deklaratif yang mewajibkan berkas driver `zram.ko` dan `zsmalloc.ko` terdaftar di dalam atribut `module_outs`. Jika Anda memaksa kedua fitur ini menjadi *built-in* atau menonaktifkannya, Bazel akan mendeteksi hilangnya berkas modul tersebut dan menghentikan proses kompilasi dengan status **Build Failure**.
* **Implementasi**: Pastikan baris konfigurasi berikut tertulis secara tepat di dalam defconfig Anda:
  ```ini
  CONFIG_ZSMALLOC=m
  CONFIG_ZRAM=m
  CONFIG_ZRAM_DEF_COMP_LZ4=y
  CONFIG_CRYPTO_LZ4=y
  ```
* **Larangan Keras**: Jangan pernah memanipulasi berkas `BUILD.bazel` menggunakan skrip otomatis untuk menghapus paksa referensi modul-modul ini dari sistem pelacakan Bazel.

---

## 2. Pemeliharaan Modul Vendor (MODVERSIONS)
* **Aturan Utama**: Pertahankan konfigurasi pemeriksaan versi simbol modul bawaan GKI. Jangan mematikan fitur ini secara sembarangan pada konfigurasi produksi HP.
* **Rasionalisasi**: Sistem operasi HyperOS pada Xiaomi Redmi 12 mengandalkan arsitektur DLKM (Dynamically Loadable Kernel Modules). Driver untuk sensor penting seperti kamera, modul layar, pengisian daya, dan sensor sidik jari dikompilasi secara terpisah oleh pihak vendor. Driver vendor ini memerlukan pemeriksaan tanda tangan CRC untuk mencocokkan kompatibilitas dengan kernel utama. Menonaktifkan pemeriksaan ini secara serampangan akan memicu kegagalan sistem saat memuat driver krusial tersebut, yang berdampak langsung pada **bootloop** perangkat.
* **Implementasi**: Jangan menambahkan opsi `CONFIG_MODVERSIONS=n` pada defconfig utama Anda kecuali untuk pengujian isolasi terbatas yang spesifik. Biarkan sistem mengikuti kebijakan penanganan modul bawaan GKI.
