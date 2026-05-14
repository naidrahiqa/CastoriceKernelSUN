# Aturan 2: Bazel Build & Konfigurasi Module

> **⚠️ MENGABAIKAN ATURAN INI AKAN MEMBUAT BUILD CI/CD GAGAL (COMPILE ERROR)**

## 1. Modul ZRAM & ZSMALLOC
- **Kenapa?** Kleaf (sistem build Bazel bawaan GKI) secara eksplisit mencari file output `zram.ko` dan `zsmalloc.ko`.
- **Apa yang terjadi kalau diubah?** Kalau modul ini di-disable atau dijadikan built-in (`=y`), Bazel tidak akan menemukan file `.ko` dan build akan **FAIL**.
- **Implementasi:** Wajib di-set sebagai module (`=m`) di defconfig.
  ```ini
  CONFIG_ZSMALLOC=m
  CONFIG_ZRAM=m
  CONFIG_ZRAM_DEF_COMP_LZ4=y
  CONFIG_CRYPTO_LZ4=y
  ```
- **DILARANG:** Menghapus daftar modul menggunakan `sed -i` di `BUILD.bazel`.

## 2. Modul Vendor (MODVERSIONS)
- **Kenapa?** Xiaomi menggunakan DLKM (Dynamically Loadable Kernel Modules). Modul ini butuh ngecek versi ABI kernel.
- **Apa yang terjadi kalau di-disable?** Driver HP (kamera, layar, dll) menolak untuk di-load. HP bootloop.
- **Implementasi:** 
  **DILARANG** menambahkan `CONFIG_MODVERSIONS=n`. Biarkan default dari GKI.
