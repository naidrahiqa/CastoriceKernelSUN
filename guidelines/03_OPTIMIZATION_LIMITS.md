# Aturan 3: Optimasi & Pengurangan Beban (Lightweight)

> **⚠️ ATURAN INI DIBUAT AGAR KERNEL TIDAK BERAT / LAG / RAM HABIS SEPERTI SEBELUMNYA**

## 1. Hapus Debugging (Wajib)
- **Kenapa?** Ukuran kernel membengkak 30-50% dan CPU terkuras untuk logging yang tidak dipakai oleh user biasa.
- **Implementasi:**
  ```ini
  CONFIG_DEBUG_INFO_NONE=y
  CONFIG_SLUB_DEBUG=n
  CONFIG_FUNCTION_TRACER=n
  ```

## 2. Pertahankan KPROBES (Jangan Dihapus!)
- **Kenapa?** KernelSU-Next bergantung penuh pada fungsi Kprobes untuk melakukan intercept system calls.
- **Apa yang terjadi kalau dihapus?** KernelSU tidak akan berfungsi / modul root gagal berjalan.
- **Implementasi:** Biarkan `CONFIG_KPROBES=y` (bawaan GKI).

## 3. LTO (Link-Time Optimization)
- **Kenapa?** LTO bikin binary kernel lebih kecil dan cepat. Tapi kalau pakai `full`, GitHub Actions akan **OOM (Out Of Memory)** karena limit RAM cuma 7GB.
- **Implementasi:** Gunakan `--lto=thin` pada command `tools/bazel run`.
  **DILARANG** menggunakan `--lto=full` atau `--lto=none`.

## 4. Baterai & RAM Android
- **Implementasi:**
  - Timer: `CONFIG_HZ=300` (Standar Android, jangan dinaikkan ke 1000 karena boros baterai G88).
  - RAM: `CONFIG_LRU_GEN=y` (Wajib, lebih efisien mengatur memori).
  - THP: `CONFIG_TRANSPARENT_HUGEPAGE=n` (Wajib dimatikan, makan terlalu banyak RAM di HP budget).
