# Aturan 3: Optimasi & Pengurangan Beban (Lightweight)

> **⚠️ ATURAN INI DIBUAT AGAR KERNEL TIDAK BERAT / LAG / RAM HABIS SEPERTI SEBELUMNYA**

## 1. Hapus Debugging — Hati-hati dengan A15 BTF!
- **Kenapa?** Ukuran kernel membengkak 30-50% dan CPU terkuras untuk logging yang tidak dipakai user biasa.
- **⚠️ PERINGATAN:** Untuk Android 15, **JANGAN set `CONFIG_DEBUG_INFO_NONE=y`** dulu! A15 butuh **BTF info** untuk networking (WiFi/Data). Kalau dipaksa, WiFi dan data seluler mati. Biarkan default GKI.
- **Implementasi (aman untuk A15):**
  ```ini
  # CONFIG_DEBUG_INFO_NONE=y    ← JANGAN di A15! Bikin BTF error → WiFi mati
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
  **DILARANG** menggunakan `--lto=full` (OOM) atau `--lto=none` (kernel gede, cuma buat deep debugging).
- **Status Workflow:** ✅ `_build_kernel_core.yml` sudah pakai `--lto=thin`.

## 4. Baterai & RAM Android
- **Implementasi:**
  - Timer: `CONFIG_HZ=300` (Standar Android. HZ=1000 bikin respon lebih cepat tapi boros baterai di MT6768 — khusus gaming build bisa dicoba, tapi jangan default).
  - RAM: `CONFIG_LRU_GEN=y` (Wajib, lebih efisien mengatur memori).
  - THP: `CONFIG_TRANSPARENT_HUGEPAGE=n` (Wajib dimatikan, makan terlalu banyak RAM di HP budget).
