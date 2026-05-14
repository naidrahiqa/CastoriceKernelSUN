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
