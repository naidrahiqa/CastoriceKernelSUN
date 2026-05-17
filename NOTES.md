# 📝 Kernel Stabilization Notes (Redmi 12 - fire)

## 🚀 Status Terakhir (Mei 2026)
- **v70 (Bazel)**: **BOOTING** ✅. Masalah: WiFi/Hotspot mati, GPU lag (limiter error), RAM usage tinggi (~3.9GB).
- **v71 (ZyClang)**: **BOOTLOOP** ❌. Penyebab: Antara toolchain ZyClang atau config `DEBUG_INFO_NONE` (matiin BPF A15).
- **v72 (Next)**: Fokus fix Hotspot (NAT) + Branding. **WAJIB PAKE BAZEL** buat baseline.

## ⚠️ Golden Rules (Jangan Dilanggar!)
1. **Page Size**: Harus **4K (CONFIG_ARM64_4K_PAGES=y)**. Kalau 16K/64K pasti bootloop karena vendor modules stock pake 4K.
2. **Local Version**: Branding pake `CONFIG_LOCALVERSION="-Epitaph"`. Jangan biarin kosong biar gampang cek di "About Phone".
3. **Debug Symbols**: Untuk Android 15, **JANGAN** set `CONFIG_DEBUG_INFO_NONE=y` dulu. Android 15 butuh BTF info buat networking (WiFi/Data).
4. **Toolchain**: GKI 6.6 paling stabil di **Bazel/Kleaf**. Toolchain lain (ZyClang, etc) cuma buat eksperimen kalau Bazel udah sempurna.

## 🛠️ Fixes yang Sedang Diterapkan (v72+)
- **Hotspot**: Penambahan `CONFIG_NF_NAT`, `CONFIG_IP_NF_NAT`, dan `CONFIG_NETFILTER_XT_TARGET_MASQUERADE`.
- **Branding**: Nama kernel diset ke `-Epitaph`.
- **Azure**: Sudah dihapus dari workflow karena nggak kepake.

## 🔍 Cara Debugging
- Kalau bootloop, tarik log pake: `adb pull /sdcard/last_kmsg.log` (lewat Recovery) atau cek `dmesg` lewat ADB kalau sempat masuk homescreen.
- Cek error GPU: `dmesg | grep "limiter"`.
- Cek status WiFi: `dmesg | grep "WIFI"`.

---
*Last Updated: 2026-05-17 13:00*