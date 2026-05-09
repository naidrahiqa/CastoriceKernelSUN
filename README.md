<div align="center">

# ⚡ Castorice Kernel
### Gaming-Optimized GKI 6.6 Kernel for Redmi 12 (fire)

[![GitHub Release](https://img.shields.io/github/v/release/naidrahiqa/CastoriceKernelSUN?style=for-the-badge&logo=github&color=success)](https://github.com/naidrahiqa/CastoriceKernelSUN/releases/latest)
[![GitHub Downloads](https://img.shields.io/github/downloads/naidrahiqa/CastoriceKernelSUN/total?style=for-the-badge&logo=github&color=blue)](https://github.com/naidrahiqa/CastoriceKernelSUN/releases)
[![GitHub Stars](https://img.shields.io/github/stars/naidrahiqa/CastoriceKernelSUN?style=for-the-badge&logo=github&color=yellow)](https://github.com/naidrahiqa/CastoriceKernelSUN/stargazers)

![Android](https://img.shields.io/badge/Android-15-3DDC84?style=flat-square&logo=android)
![Xiaomi](https://img.shields.io/badge/Device-Redmi%2012%20(fire)-FF6900?style=flat-square&logo=xiaomi)
![Chipset](https://img.shields.io/badge/Chipset-MT6768-orange?style=flat-square)

</div>

---

## 👋 Halo!

Ini adalah **Castorice Kernel** - kernel custom GKI 6.6 yang gw bikin khusus buat Redmi 12 (fire) dengan fokus ke **gaming performance**, **stabilitas**, dan **root flexibility**. 

Kenapa bikin ini? Karena gw pengen kernel yang:
- ⚡ **Cepet** buat gaming (HZ_1000, full preempt)
- 🎮 **Smooth** tanpa lag (optimized scheduler & TCP BBR)
- 🛡️ **Flexible** root options (4 KernelSU variants!)
- 🔒 **Aman** dari deteksi (SUSFS optional)
- 🔧 **Customizable** (ganti governor on-the-fly)

> ⚠️ **PERHATIAN:** Kernel ini **HANYA MENDUKUNG HyperOS 2 (Android 15)** dengan arsitektur GKI 6.6. Jangan di-flash di MIUI 14 atau HyperOS 1 (Android 13/14) karena akan menyebabkan Bootloop!

---

## 🎯 Pilih Kernel yang Cocok Buat Lo

### 🛡️ Step 1: Butuh SUSFS Ga?

**SUSFS** itu buat nge-hide root dari app yang detect root (banking apps, game anti-cheat, dll).

- ✅ **Pake SUSFS** kalo lo main game competitive atau pake banking apps
- ❌ **Skip SUSFS** kalo cuma buat daily driver biasa

### 🔑 Step 2: Pilih Root Method

Gw support 4 root method, pilih sesuai kebutuhan:

| Root Method | Cocok Buat | Status |
|:------------|:-----------|:-------|
| **KernelSU-Next** | Pengguna umum (paling stabil) | ⭐ Recommended |

### ⚙️ Step 3: Pilih CPU Governor

Governor itu ngatur gimana CPU lo kerja:

| Governor | Kapan Pake | Battery | Performance |
|:---------|:-----------|:--------|:------------|
| **schedutil** | Daily driver | ⚡⚡⚡ | 🎮🎮🎮 |
| **performance** | Gaming hardcore | ⚡ | 🎮🎮🎮🎮🎮 |
| **ondemand** | Balanced | ⚡⚡⚡⚡ | 🎮🎮 |
| **conservative** | Battery saver | ⚡⚡⚡⚡⚡ | 🎮 |

> 💡 **Pro Tip:** Lo bisa ganti governor kapan aja pake kernel tuner app!

---

## 📥 Cara Install (Gampang Kok!)

### 🔽 Download Dulu

1. Ke [**Releases Page**](../../releases/latest)
2. Download file zip AnyKernel3 yang sesuai, contoh nama file:
   ```
   Castorice-Gaming-v45-GKI66-KSUNext-SUSFS-Performance-balanced-stable-Bazel-Redmi12.zip
   ```
   
### 📲 Flash Kernel (Wajib Unlock Bootloader)

**Persiapan VBMeta (Hanya dilakukan sekali untuk bypass proteksi):**
Boot ke mode Fastboot, lalu jalankan:
```bash
fastboot --disable-verity --disable-verification flash vbmeta vbmeta.img
fastboot --disable-verity --disable-verification flash vbmeta_system vbmeta_system.img
fastboot --disable-verity --disable-verification flash vbmeta_vendor vbmeta_vendor.img
```
*(File img di atas diekstrak dari ROM HyperOS 2 Fastboot).*

**Cara Flash (Pake Kernel Flasher App):**
1. Install [Kernel Flasher](https://github.com/capntrips/KernelFlasher/releases) dari GitHub.
2. Buka app, pilih file zip kernel yang udah lo download.
3. Flash → Reboot.
4. Done! ✅

> ⚠️ **Note:** Redmi 12 (fire) saat ini sulit menggunakan custom recovery untuk HyperOS 2 karena masalah kompatibilitas layar. Gunakan Kernel Flasher!

### 📱 Install Manager App

Setelah flash kernel, install manager app sesuai root method lo:

- **KernelSU-Next:** [Download Manager](https://github.com/KernelSU-Next/KernelSU-Next/releases)

---

## 🎮 Fitur Gaming

### ⚡ Low Latency
- **HZ_1000:** Timer 1000Hz buat input lag minimal.
- **Full PREEMPT:** Kernel bisa di-interrupt kapan aja = smoother.
- **HRTIMER:** High-resolution timer buat frame timing presisi.

### 🧠 Memory Management
- **LRU-Gen:** Multi-generational LRU (Native GKI).
- **LZ4/ZSTD ZRAM:** Kompresi RAM super cepat.
- **KSM:** Merge memory yang sama buat hemat RAM.

### 🌐 Network & I/O
- **TCP BBR:** Congestion control modern dari Google untuk ping stabil.
- **BFQ I/O Scheduler:** Optimized I/O untuk memori eMMC/UFS.

---

## 🛠️ Build Sendiri (Advanced)

Kini jauh lebih gampang dengan **🎛️ GKI Control Center**! Lo ga perlu lagi jalanin workflow satu-satu. Cukup pake satu "Manager" buat bikin semua varian sekaligus.

1. **Fork** repo ini.
2. Masuk ke tab **Actions**.
3. Pilih workflow: **🎛️ GKI Control Center**.
4. Klik **Run workflow**.
5. Pilih kombinasi yang lo mau (Matrix Build):
   - **Root Methods:** Checkbox KernelSU-Next.
   - **SUSFS Variant:** Pilih mau yang murni atau +SUSFS.
   - **Toolchains:** Pilih satu atau **semua sekaligus** (Bazel, ZyClang, WeebX, Neutron, Azure, AOSP).
   - **Governors:** Masukin list (e.g. `schedutil,performance`).

### 🔨 Toolchain Options

Sekarang mendukung lebih banyak toolchain dengan sistem **Smart Extraction** (Otomatis deteksi struktur archive):

| Toolchain | Keterangan | Status |
|:----------|:-----------|:-------|
| **Bazel** | Google's official GKI toolchain | 💎 Ultra Stable |
| **ZyClang** | Balanced gaming performance | 🚀 Fast |
| **WeebX Clang**| Aggressive optimization | 🔥 Hot |
| **Neutron Clang**| Stability & LLVM focus | 🛡️ Modern |
| **Azure Clang** | Extreme compatibility (RELR fix) | 🛠️ Updated |
| **AOSP Latest** | Cleanest build environment | 📎 Stock |

---

## 🚀 Technical Improvements (Terbaru!)

Gw udah benerin beberapa isu krusial biar build-nya makin solid:
- 🧠 **Smart Toolchain Extract:** Build script sekarang pinter, bisa bedain archive "flat" (ZyClang) vs "nested" otomatis. No more "Clang not found" error!
- 🔗 **RELR / .relr.dyn Fix:** Host tools sekarang dipaksa pake system linker (`/usr/bin/ld`) biar ga bentrok sama glibc Ubuntu terbaru.
- 🧱 **Bazel Symlink Fix:** Driver KernelSU sekarang di-copy (bukan symlink) saat build Bazel biar semua symbol (`ksu_handle_*`) ke-compile sempurna.
- 🛡️ **Hunk Detection:** Verifikasi otomatis buat SUSFS patch, kalo ada yang gagal (hunk rejected) langsung ketauan di logs.

---

## 📊 Build Status

| Workflow | Status |
|:---------|:-------|
| **🎛️ GKI Control Center** | [![GKI Control Center](https://github.com/naidrahiqa/CastoriceKernelSUN/actions/workflows/build_manager_gki.yml/badge.svg)](https://github.com/naidrahiqa/CastoriceKernelSUN/actions/workflows/build_manager_gki.yml) |
| **⚙️ Core Build Engine** | [![Core Build](https://github.com/naidrahiqa/CastoriceKernelSUN/actions/workflows/_build_kernel_core.yml/badge.svg)](https://github.com/naidrahiqa/CastoriceKernelSUN/actions/workflows/_build_kernel_core.yml) |

---

## 📋 Compatibility & Features

| Feature | GKI 6.6 | Notes |
|:--------|:-------:|:------|
| **OS Support** |
| HyperOS 2 (A15) | ✅ | Mendukung Penuh |
| HyperOS 1 (A14) | ❌ | Tidak Didukung |
| MIUI 14 (A13) | ❌ | Tidak Didukung |
| **Root Methods** |
| KernelSU-Next | ✅ | Recommended |
| **Tech Specs** |
| Bypass KMI Strict | ✅ | Kompatibel dengan modul vendor bawaan |
| OEM Hash Locked | ✅ | Anti bootloop karena mismatch base version |
| SUSFS | ✅ | Optional Toggle |

---

## 🐛 Known Issues & Solutions

### ❌ Bootloop setelah flash
**Penyebab:** Belum unlock vbmeta atau beda versi Android.
**Solusi:** Pastikan kamu di HyperOS 2 dan sudah flash vbmeta ori dengan perintah `--disable-verity`.

### ❌ Banking app detect root
**Penyebab:** SUSFS belum dikonfigurasi.
**Solusi:** 
1. Flash varian kernel yang ada SUSFS-nya.
2. Gunakan Manager App untuk mengaktifkan hide root.

---

## 💖 Credits

Kernel ini ga mungkin ada tanpa bantuan dari:
- **[KernelSU-Next Team](https://github.com/KernelSU-Next/KernelSU-Next)** - Next-gen kernel root
- **[simonpunk](https://gitlab.com/simonpunk/susfs4ksu)** - SUSFS magic
- **[osm0sis](https://github.com/osm0sis/AnyKernel3)** - AnyKernel3 flasher
- **[Google](https://android.googlesource.com/kernel/manifest)** - Android Common Kernel Source

<div align="center">

### 🎮 Built for Gamers, by Gamers
**Kalo lo suka kernel ini, kasih ⭐ dong!**
Made with ❤️ and ☕ for Redmi 12 (fire) Community

</div>
