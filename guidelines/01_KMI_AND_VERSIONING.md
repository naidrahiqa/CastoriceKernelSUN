# Aturan 1: KMI & Versi Kernel (CRITICAL)

> **⚠️ JANGAN PERNAH MENGUBAH ATURAN DI BAWAH INI TANPA ALASAN YANG JELAS!**

## 1. Gunakan Tip of Branch (JANGAN Lock Versi)
- **Kenapa?** Build 30 April 2026 (versi 6.6.129) yang **BOOTING** pakai tip of branch `common-android15-6.6`.
- **Apa yang terjadi kalau di-lock?** Semua build Mei 2026 yang di-lock ke commit `33c1ba9ffede` (6.6.58) **BOOTLOOP**.
- **Implementasi:** Biarkan `repo sync` ambil HEAD. JANGAN tambahkan `git fetch` + `git checkout` ke commit spesifik.

## 2. Kompresi Kernel — Ikuti Default GKI
- **Kenapa?** Build yang booting tidak mengubah format kompresi dari default GKI.
- **Implementasi:** JANGAN paksa `CONFIG_KERNEL_GZIP=y` atau hapus `CONFIG_KERNEL_LZ4=y`. Biarkan default.

## 3. AnyKernel3 Packaging (Image.gz Priority)
- **Kenapa?** Bootloader Mediatek Redmi 12 (fire) lebih stabil dengan `Image.gz` daripada raw `Image`.
- **Implementasi:** Urutan pencarian file di AnyKernel3:
  1. `Image.gz` (Prioritas Utama)
  2. `Image.lz4`
  3. `Image` (Terakhir/Fallback)
- **Status:** Sudah diperbaiki per 15 Mei 2026. JANGAN ditukar lagi urutannya.

## 4. JANGAN Tambah Optimisasi Tanpa Test Booting
- **Kenapa?** Config seperti `CONFIG_DEBUG_KERNEL=n`, `CONFIG_FUNCTION_TRACER=n` terbukti bikin bootloop.
- **Implementasi:** Tambah optimisasi SATU PER SATU. Setiap config harus di-test flash → boot → confirm sebelum commit.
- **Referensi:** Lihat blok "OPTIMIZATIONS DISABLED" di `_build_kernel_core.yml` untuk daftar lengkap.
