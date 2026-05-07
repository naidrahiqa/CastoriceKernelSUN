<div align="center">

# ⚡ Castorice Kernel
### Gaming-Optimized Kernel for Redmi 12 (fire)

[![GitHub Release](https://img.shields.io/github/v/release/naidrahiqa/CastoriceKernelSUN?style=for-the-badge&logo=github&color=success)](https://github.com/naidrahiqa/CastoriceKernelSUN/releases/latest)
[![GitHub Downloads](https://img.shields.io/github/downloads/naidrahiqa/CastoriceKernelSUN/total?style=for-the-badge&logo=github&color=blue)](https://github.com/naidrahiqa/CastoriceKernelSUN/releases)
[![GitHub Stars](https://img.shields.io/github/stars/naidrahiqa/CastoriceKernelSUN?style=for-the-badge&logo=github&color=yellow)](https://github.com/naidrahiqa/CastoriceKernelSUN/stargazers)

![Android](https://img.shields.io/badge/Android-13%20%7C%2014%20%7C%2015-3DDC84?style=flat-square&logo=android)
![Xiaomi](https://img.shields.io/badge/Device-Redmi%2012%20(fire)-FF6900?style=flat-square&logo=xiaomi)
![Chipset](https://img.shields.io/badge/Chipset-MT6768-orange?style=flat-square)

</div>

---

## 👋 Halo!

Ini adalah **Castorice Kernel** - kernel custom yang gw bikin khusus buat Redmi 12 (fire) dengan fokus ke **gaming performance** dan **root flexibility**. 

Kenapa bikin ini? Karena gw pengen kernel yang:
- ⚡ **Cepet** buat gaming (HZ_1000, full preempt)
- 🎮 **Smooth** tanpa lag (optimized scheduler)
- 🛡️ **Flexible** root options (4 KernelSU variants!)
- 🔒 **Aman** dari deteksi (SUSFS optional)
- 🔧 **Customizable** (ganti governor on-the-fly)

---

## 🎯 Pilih Kernel yang Cocok Buat Lo

### 📱 Step 1: Cek OS Lo

Buka **Settings → About Phone**, liat versi Android/HyperOS lo:

| Kalo Lo Pake | Kernel yang Harus Lo Flash |
|:-------------|:---------------------------|
| **HyperOS 2.x** (Android 15) | 🟢 **GKI 6.6** |
| **HyperOS 1.x** (Android 14) | 🟠 **Legacy 4.19** |
| **MIUI 14** (Android 13) | 🟠 **Legacy 4.19** |

> ⚠️ **PENTING:** Salah pilih = bootloop! Jangan asal flash!

### 🛡️ Step 2: Butuh SUSFS Ga?

**SUSFS** itu buat nge-hide root dari app yang detect root (banking apps, game anti-cheat, dll).

- ✅ **Pake SUSFS** kalo lo main game competitive atau pake banking apps
- ❌ **Skip SUSFS** kalo cuma buat daily driver biasa

### 🔑 Step 3: Pilih Root Method

Gw support 4 root method, pilih sesuai kebutuhan:

| Root Method | Cocok Buat | Status |
|:------------|:-----------|:-------|
| **KernelSU-Next** | Pengguna umum (paling stabil) | ⭐ Recommended |
| **WildKSU** | Advanced user (extra features) | 🔥 Popular |
| **SukiSU** | Testing/Development | 🧪 Experimental |
| **ReSukiSU** | Alternative variant | 🔬 Beta |

### ⚙️ Step 4: Pilih CPU Governor

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
2. Download file yang sesuai, contoh nama file:
   ```
   Castorice-Gaming-v45-GKI66-KSUNext-SUSFS-Performance-ZyC19-Redmi12.zip
   ```
   
   **Penjelasan nama file:**
   - `Gaming` = Custom name lo
   - `v45` = Build number
   - `GKI66` = GKI 6.6 (atau `Leg419` = Legacy 4.19)
   - `KSUNext` = Root method (KSUNext/WildKSU/SukiSU/ReSukiSU)
   - `SUSFS` = Ada SUSFS (atau `NoSUSFS`)
   - `Performance` = CPU Governor default
   - `ZyC19` = Toolchain (ZyClang 19)
   - `Redmi12` = Device codename

### 📲 Flash Kernel

**Cara 1: Pake Kernel Flasher App** (Recommended!)
1. Install [Kernel Flasher](https://github.com/capntrips/KernelFlasher/releases) dari GitHub
2. Buka app, pilih file zip yang udah lo download
3. Flash → Reboot
4. Done! ✅

**Cara 2: Pake Custom Recovery** (Kalo punya TWRP/OrangeFox)
1. Reboot ke recovery
2. Install → Pilih zip file
3. Swipe to flash
4. Reboot system
5. Done! ✅

> ⚠️ **Note:** Redmi 12 fire belum ada custom recovery buat HyperOS 2 karena masalah LCM 0c/0d panel. Pake Kernel Flasher aja!

### 📱 Install Manager App

Setelah flash kernel, install manager app sesuai root method lo:

- **KernelSU-Next:** [Download Manager](https://github.com/KernelSU-Next/KernelSU-Next/releases)
- **WildKSU:** [Download Manager](https://github.com/WildKernels/Wild_KSU/releases)
- **SukiSU:** [Download Manager](https://github.com/SukiSU-Ultra/SukiSU-Ultra/releases)
- **ReSukiSU:** [Download Manager](https://github.com/ReSukiSU/ReSukiSU/releases)

### ✅ Verifikasi

Cek kalo kernel udah ke-install:
1. Buka **Settings → About Phone**
2. Tap **Kernel Version** beberapa kali
3. Harusnya muncul `Castorice-XXX-vXX`

---

## 🎮 Fitur Gaming

### ⚡ Low Latency
- **HZ_1000:** Timer 1000Hz buat input lag minimal
- **Full PREEMPT:** Kernel bisa di-interrupt kapan aja = smoother
- **HRTIMER:** High-resolution timer buat frame timing presisi

### 🧠 Memory Management
- **LRU-Gen:** Multi-generational LRU (GKI only)
- **LZ4/ZSTD ZRAM:** Kompresi RAM cepet
- **KSM:** Merge memory yang sama buat hemat RAM
- **Transparent Hugepages:** Akses memory lebih cepet

### 🌐 Network & I/O
- **TCP BBR:** Congestion control dari Google (internet lebih cepet)
- **BFQ + Kyber:** I/O scheduler optimized
- **IPSet:** Advanced firewall support

### 🔧 Customization
- **All Governors Built-in:** Ganti governor kapan aja
- **Multiple Root Options:** Pilih root method favorit lo
- **SUSFS Optional:** Hide root kalo perlu

---

## 🛠️ Build Sendiri (Advanced)

Lo bisa build kernel sendiri dengan custom config! Sekarang ada **2 cara**:

### 🎯 Cara 1: Unified Builder (Recommended!)

Paling gampang - 1 workflow buat semua variant!

1. **Fork** repo ini
2. Ke tab **Actions**
3. Pilih **"🎯 Unified Kernel Builder"**
4. Klik **Run workflow**
5. Isi form:
   ```
   Release Tag: v1.0              # Semua build masuk ke release ini
   Kernel Name: Gaming            # Nama custom lo
   Author Name: YourName          # Nama lo
   
   Kernel Type: gki-6.6           # Pilih: gki-6.6, legacy-4.19, atau both
   Root Method: kernelsu-next     # KSU variant
   Enable SUSFS: ✅               # Centang kalo mau SUSFS
   CPU Governor: performance      # Governor default
   Clang Toolchain: zyc-latest    # Pilih toolchain (Legacy only)
   ```
6. Tunggu ~20-30 menit
7. Semua build masuk ke **1 release** dengan tag yang sama!

**Keuntungan:**
- ✅ Semua variant dalam 1 release
- ✅ Pilih toolchain (ZyClang, Proton, Neutron)
- ✅ Toggle SUSFS on/off
- ✅ Build GKI + Legacy sekaligus

### 🔧 Cara 2: Individual Workflows

Buat yang mau kontrol lebih detail:

1. **Fork** repo ini
2. Ke tab **Actions**
3. Pilih workflow spesifik:
   - 🟢 `GKI 6.6 — KernelSU (No SUSFS)`
   - 🟣 `GKI 6.6 — KernelSU + SUSFS`
   - 🟠 `Legacy 4.19 — KernelSU (No SUSFS)`
   - 🔴 `Legacy 4.19 — KernelSU + SUSFS`
4. Klik **Run workflow**
5. Isi form + **Release Tag** (pake tag yang sama biar masuk 1 release)
6. Tunggu build selesai

### 🚀 Cara 3: Multi-Variant Matrix (Power User!)

Build banyak kombinasi sekaligus:

1. Pilih **"🚀 Multi-Variant Build"**
2. Configure:
   ```
   Release Tag: v1.0
   Build GKI: ✅
   Build Legacy: ✅
   Build SUSFS: ✅
   Root Methods: kernelsu-next,wildksu
   Governors: schedutil,performance
   ```
3. Ini bakal build **semua kombinasi**:
   - GKI + KSU-Next + Schedutil
   - GKI + KSU-Next + Performance
   - GKI + WildKSU + Schedutil
   - GKI + WildKSU + Performance
   - ... dan seterusnya (termasuk SUSFS variants!)

### 🔨 Toolchain Options (Legacy Only)

| Toolchain | Best For | Version |
|:----------|:---------|:--------|
| **ZyClang** | Balanced (recommended) | Auto-latest |
| **Proton Clang** | Performance | Auto-latest |
| **Neutron Clang** | Stability | Auto-latest |

> 💡 **Note:** GKI builds always use Bazel (Google's official build system)

### 📊 Build Status

| Workflow | Status | Last Build |
|:---------|:-------|:-----------|
| GKI 6.6 (No SUSFS) | [![Build](https://github.com/naidrahiqa/CastoriceKernelSUN/actions/workflows/build_gki.yml/badge.svg)](https://github.com/naidrahiqa/CastoriceKernelSUN/actions/workflows/build_gki.yml) | ![Last Build](https://img.shields.io/github/last-commit/naidrahiqa/CastoriceKernelSUN?style=flat-square) |
| GKI 6.6 + SUSFS | [![Build](https://github.com/naidrahiqa/CastoriceKernelSUN/actions/workflows/build_gki_susfs.yml/badge.svg)](https://github.com/naidrahiqa/CastoriceKernelSUN/actions/workflows/build_gki_susfs.yml) | ![Last Build](https://img.shields.io/github/last-commit/naidrahiqa/CastoriceKernelSUN?style=flat-square) |
| Legacy 4.19 (No SUSFS) | [![Build](https://github.com/naidrahiqa/CastoriceKernelSUN/actions/workflows/build_legacy.yml/badge.svg)](https://github.com/naidrahiqa/CastoriceKernelSUN/actions/workflows/build_legacy.yml) | ![Last Build](https://img.shields.io/github/last-commit/naidrahiqa/CastoriceKernelSUN?style=flat-square) |
| Legacy 4.19 + SUSFS | [![Build](https://github.com/naidrahiqa/CastoriceKernelSUN/actions/workflows/build_legacy_susfs.yml/badge.svg)](https://github.com/naidrahiqa/CastoriceKernelSUN/actions/workflows/build_legacy_susfs.yml) | ![Last Build](https://img.shields.io/github/last-commit/naidrahiqa/CastoriceKernelSUN?style=flat-square) |

---

## 📋 Compatibility Table

| Feature | GKI 6.6 | Legacy 4.19 | Notes |
|:--------|:-------:|:-----------:|:------|
| **OS Support** |
| HyperOS 2 (A15) | ✅ | ❌ | GKI only |
| HyperOS 1 (A14) | ❌ | ✅ | Legacy only |
| MIUI 14 (A13) | ❌ | ✅ | Legacy only |
| **Root Methods** |
| KernelSU-Next | ✅ | ✅ | Recommended |
| WildKSU | ✅ | ✅ | Popular |
| SukiSU | ✅ | ✅ | Experimental |
| ReSukiSU | ✅ | ✅ | Beta |
| **Features** |
| SUSFS | ✅ | ✅ | Optional |
| LRU-Gen | ✅ | ❌ | GKI only |
| MODVERSIONS | ✅ | ❌ | Vendor modules safe |
| All CPU Governors | ✅ | ✅ | Switchable |
| HZ_1000 | ✅ | ✅ | Low latency |
| Full PREEMPT | ✅ | ✅ | Smooth gaming |
| TCP BBR | ✅ | ✅ | Fast network |
| BFQ/Kyber I/O | ✅ | ✅ | Optimized I/O |

---

## 🐛 Known Issues & Solutions

### ❌ Bootloop setelah flash
**Penyebab:** Salah pilih kernel (GKI di Legacy OS atau sebaliknya)  
**Solusi:** Flash kernel yang sesuai OS lo, atau restore backup

### ❌ Touchscreen ga respon
**Penyebab:** Panel LCM 0c/0d belum ke-patch  
**Solusi:** Kernel ini udah include patch, tapi kalo masih bermasalah coba wipe cache

### ❌ Banking app detect root
**Penyebab:** SUSFS belum dikonfigurasi atau ga pake SUSFS  
**Solusi:** 
1. Flash kernel yang ada SUSFS-nya
2. Configure SUSFS via manager app
3. Atau pake Shamiko/Zygisk Hide

### ❌ Custom recovery ga bisa install
**Penyebab:** HyperOS 2 belum support custom recovery karena LCM issue  
**Solusi:** Pake Kernel Flasher app aja

---

## 🎯 Roadmap

- [x] Multi-root method support
- [x] SUSFS integration
- [x] Gaming optimizations
- [x] Automated CI/CD builds
- [ ] Benchmark results & comparisons
- [ ] OC/UV profiles
- [ ] Custom scheduler tweaks
- [ ] Telegram channel/group
- [ ] Video installation guide

---

## 💬 Community & Support

### 🆘 Butuh Bantuan?

1. **Cek dulu** [Known Issues](#-known-issues--solutions)
2. **Search** di [Issues](../../issues) - mungkin udah ada yang nanya
3. **Buat issue baru** kalo belum ada solusinya
4. **Join discussion** di [Discussions](../../discussions)

### 📢 Stay Updated

- ⭐ **Star** repo ini buat dapet notif update
- 👀 **Watch** repo buat tau ada release baru
- 🔔 **Enable notifications** di GitHub

---

## 💖 Credits

Kernel ini ga mungkin ada tanpa bantuan dari:

### 🏆 Main Contributors
- **[KernelSU-Next Team](https://github.com/KernelSU-Next/KernelSU-Next)** - Next-gen kernel root
- **[WildKernels](https://github.com/WildKernels/Wild_KSU)** - WildKSU variant
- **[SukiSU-Ultra](https://github.com/SukiSU-Ultra/SukiSU-Ultra)** - SukiSU implementation
- **[ReSukiSU](https://github.com/ReSukiSU/ReSukiSU)** - ReSukiSU variant
- **[simonpunk](https://gitlab.com/simonpunk/susfs4ksu)** - SUSFS magic
- **[osm0sis](https://github.com/osm0sis/AnyKernel3)** - AnyKernel3 flasher
- **[ZyCromerZ](https://github.com/ZyCromerZ/Clang)** - ZyClang toolchain

### 🌟 Special Thanks
- **[MiCode](https://github.com/MiCode/Xiaomi_Kernel_OpenSource)** - Xiaomi kernel sources
- **[Google](https://android.googlesource.com/kernel/manifest)** - Android Common Kernel
- **[Alexjr2](https://github.com/Alexjr2/KernelSU_Next_SUSFS_fire)** - Reference patches

### 🙏 Community
- Semua yang udah testing & kasih feedback
- Contributors yang udah submit PR
- Lo yang udah star repo ini! ⭐

---

## 📜 License

GPL-2.0 - Kernel Linux license yang sama

---

## 🔗 Quick Links

- 📦 [**Download Latest Release**](../../releases/latest)
- 🐛 [**Report Bug**](../../issues/new)
- 💡 [**Request Feature**](../../issues/new)
- 💬 [**Discussions**](../../discussions)
- 📊 [**Build Status**](../../actions)

---

<div align="center">

### 🎮 Built for Gamers, by Gamers

**Kalo lo suka kernel ini, kasih ⭐ dong!**

Made with ❤️ and ☕ for Redmi 12 (fire) Community

---

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=naidrahiqa.CastoriceKernelSUN)
![GitHub repo size](https://img.shields.io/github/repo-size/naidrahiqa/CastoriceKernelSUN?style=flat-square)
![Lines of code](https://img.shields.io/tokei/lines/github/naidrahiqa/CastoriceKernelSUN?style=flat-square)

</div>
