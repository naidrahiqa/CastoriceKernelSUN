# Aturan 1: KMI & Versi Kernel (CRITICAL)

> **⚠️ JANGAN PERNAH MENGUBAH ATURAN DI BAWAH INI TANPA ALASAN YANG JELAS!**

## 1. Versi Kernel Harus Persis `6.6.58`
- **Kenapa?** Vendor module bawaan Redmi 12 (terutama driver layar/LCM `0c 0d`, touchscreen, wifi) dikompilasi khusus untuk versi ini.
- **Apa yang terjadi kalau diubah?** Bootloop (Stuck logo Xiaomi lalu reboot) karena system gagal ngeload driver layar (SurfaceFlinger crash).
- **Implementasi:** Di workflow, kita **wajib** nge-fetch commit AOSP spesifik:
  ```bash
  git fetch https://android.googlesource.com/kernel/common 33c1ba9ffede --depth=1
  git checkout 33c1ba9ffede
  ```

## 2. Kompresi Kernel Wajib GZIP
- **Kenapa?** Bootloader Xiaomi sangat sensitif terhadap format kompresi image. Bawaan pabrik menggunakan GZIP.
- **Apa yang terjadi kalau diubah (misal ke LZ4/ZSTD)?** Kernel mungkin tidak bisa di-decompress oleh bootloader, berujung mati total saat booting atau stuck.
- **Implementasi:** 
  ```ini
  CONFIG_KERNEL_GZIP=y
  # DILARANG MENGGUNAKAN CONFIG_KERNEL_LZ4=y
  ```

## 3. AnyKernel3 Packaging (Image.gz Priority)
- **Kenapa?** Meskipun build ngasilin file `Image` (raw) dan `Image.gz`, AnyKernel3 **HARUS** memprioritaskan `Image.gz` untuk Redmi 12 (fire). File `Image` mentah seringkali ditolak bootloader Mediatek atau bikin "bad image" error.
- **Implementasi:** Pastikan di workflow CI/CD, urutan loop pencarian file adalah:
  1. `Image.gz` (Prioritas Utama)
  2. `Image.lz4`
  3. `Image` (Terakhir/Fallback)
- **Status:** Sudah diperbaiki di workflow per 15 Mei 2026. JANGAN ditukar lagi urutannya.
