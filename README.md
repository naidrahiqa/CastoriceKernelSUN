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
   
   Kernel Type: both              # Pilih: gki-6.6, legacy-4.19, atau both
   Root Method: kernelsu-next     # KSU variant
   Enable SUSFS: ✅               # Centang kalo mau SUSFS
   CPU Governor: performance      # Governor default
   
   # Toolchain Selection (Separate untuk GKI & Legacy!)
   Clang Toolchain (GKI): bazel           # Bazel/ZyClang/Proton/Neutron
   Clang Toolchain (Legacy): zyc-latest   # ZyClang/Proton/Neutron
   ```
6. Tunggu ~20-30 menit
7. Semua build masuk ke **1 release** dengan tag yang sama!

**Keuntungan:**
- ✅ Semua variant dalam 1 release
- ✅ Pilih toolchain **berbeda** untuk GKI & Legacy
- ✅ Toggle SUSFS on/off
- ✅ Build GKI + Legacy sekaligus
- ✅ Nama file otomatis include toolchain info

**Contoh hasil di 1 release:**
```
v1.0/
├── Castorice-Gaming-v45-GKI66-KSUNext-SUSFS-Performance-Bazel-Redmi12.zip
└── Castorice-Gaming-v45-Leg419-KSUNext-SUSFS-Performance-ZyClang19-Redmi12.zip
```

### 🔧 Cara 2: Individual Workflows

Buat yang mau kontrol lebih detail per workflow:

1. **Fork** repo ini
2. Ke tab **Actions**
3. Pilih workflow spesifik:
   - 🟢 `GKI 6.6 — KernelSU (No SUSFS)` - Toolchain: Bazel/ZyClang/Proton/Neutron
   - 🟣 `GKI 6.6 — KernelSU + SUSFS` - Toolchain: Bazel/ZyClang/Proton/Neutron
   - 🟠 `Legacy 4.19 — KernelSU (No SUSFS)` - Toolchain: ZyClang/Proton/Neutron
   - 🔴 `Legacy 4.19 — KernelSU + SUSFS` - Toolchain: ZyClang/Proton/Neutron
4. Klik **Run workflow**
5. Isi form:
   ```
   Custom Name: Gaming
   Author Name: YourName
   Root Method: kernelsu-next
   CPU Governor: performance
   Clang Toolchain: bazel         # GKI: bazel/zyc-latest/proton-latest/neutron-latest
                                  # Legacy: zyc-latest/proton-latest/neutron-latest
   Release Tag: v1.0              # (Optional) Pake tag yang sama biar masuk 1 release
   ```
6. Tunggu build selesai

**Keuntungan:**
- ✅ Kontrol penuh per workflow
- ✅ Pilih toolchain spesifik per build
- ✅ Bisa build cuma 1 variant aja (hemat waktu)
- ✅ Cocok buat testing toolchain comparison

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

### 🔨 Toolchain Options

Sekarang **GKI dan Legacy** bisa pilih toolchain!

| Toolchain | Best For | GKI | Legacy | Version |
|:----------|:---------|:---:|:------:|:--------|
| **Bazel** | Google's official (recommended) | ✅ | ❌ | Auto |
| **ZyClang** | Balanced performance | ✅ | ✅ | Auto-latest |
| **Proton Clang** | Maximum performance | ✅ | ✅ | Auto-latest |
| **Neutron Clang** | Stability focused | ✅ | ✅ | Auto-latest |

#### 📊 Toolchain Comparison

| Feature | Bazel | ZyClang | Proton Clang | Neutron Clang |
|:--------|:-----:|:-------:|:------------:|:-------------:|
| **Stability** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Performance** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Build Speed** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Compatibility** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **GKI Support** | ✅ Official | ✅ | ✅ | ✅ |
| **Legacy Support** | ❌ | ✅ | ✅ | ✅ |
| **Optimization Level** | Standard | Balanced | Aggressive | Conservative |
| **LLVM Version** | Google's | Latest | Latest | Latest |
| **Recommended For** | Daily driver | All-rounder | Gaming/Benchmark | Production |

#### 🎯 Which Toolchain Should You Choose?

**For GKI 6.6:**
- 🟢 **Bazel** (Default) - Paling stabil karena official Google toolchain
- 🔵 **ZyClang** - Kalo mau balance antara performa & stabilitas
- 🔴 **Proton Clang** - Buat max gaming performance (tapi bisa kurang stabil)
- 🟣 **Neutron Clang** - Buat yang prioritas stabilitas over performa

**For Legacy 4.19:**
- 🟢 **ZyClang** (Default) - Best balance, recommended!
- 🔴 **Proton Clang** - Kalo mau squeeze max performance
- 🟣 **Neutron Clang** - Kalo device lo sering crash/unstable

**Contoh hasil:**
```
GKI dengan Bazel (default):
Castorice-Gaming-v45-GKI66-KSUNext-NoSUSFS-Performance-Bazel-Redmi12.zip

GKI dengan ZyClang:
Castorice-Gaming-v45-GKI66-KSUNext-NoSUSFS-Performance-ZyClang19-Redmi12.zip

Legacy dengan Proton:
Castorice-Gaming-v45-Leg419-WildKSU-SUSFS-Schedutil-ProtonClang18-Redmi12.zip

Legacy dengan Neutron:
Castorice-Gaming-v45-Leg419-SukiSU-SUSFS-Performance-NeutronClang19-Redmi12.zip
```

> 💡 **Pro Tip:** Kalo lo ga tau mau pilih yang mana, pake default aja (Bazel buat GKI, ZyClang buat Legacy). Udah tested & proven stable!

> ⚠️ **Note:** Toolchain yang berbeda bisa ngasih hasil performa yang beda. Coba sendiri mana yang paling cocok buat device lo!

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

## 🧪 Toolchain Benchmarking Tips

Pengen tau toolchain mana yang paling cepet di device lo? Ikutin cara ini:

### 📊 How to Benchmark

1. **Build semua toolchain variant:**
   ```
   - Castorice-Test-v1-GKI66-KSUNext-NoSUSFS-Performance-Bazel-Redmi12.zip
   - Castorice-Test-v1-GKI66-KSUNext-NoSUSFS-Performance-ZyClang19-Redmi12.zip
   - Castorice-Test-v1-GKI66-KSUNext-NoSUSFS-Performance-ProtonClang18-Redmi12.zip
   - Castorice-Test-v1-GKI66-KSUNext-NoSUSFS-Performance-NeutronClang19-Redmi12.zip
   ```

2. **Flash satu-satu & test:**
   - Gaming: Genshin Impact, PUBG, ML, dll (cek FPS & frame drops)
   - Benchmark: Geekbench, AnTuTu, 3DMark
   - Battery: Cek screen-on time (SOT) setelah 1 hari pemakaian
   - Stability: Pake 3-7 hari, cek ada crash/reboot ga

3. **Catat hasilnya:**
   | Toolchain | FPS Avg | AnTuTu | SOT | Stability |
   |:----------|:--------|:-------|:----|:----------|
   | Bazel | 58 | 350k | 7h | ⭐⭐⭐⭐⭐ |
   | ZyClang | 59 | 355k | 6.5h | ⭐⭐⭐⭐ |
   | Proton | 61 | 360k | 6h | ⭐⭐⭐ |
   | Neutron | 58 | 348k | 7.5h | ⭐⭐⭐⭐⭐ |

4. **Pilih yang paling cocok buat lo!**

### 💡 Benchmark Apps

- **Gaming FPS:** [FPS Meter](https://play.google.com/store/apps/details?id=com.nll.fpsmeter)
- **CPU/GPU:** [Geekbench 6](https://play.google.com/store/apps/details?id=com.primatelabs.geekbench6)
- **Overall:** [AnTuTu Benchmark](https://play.google.com/store/apps/details?id=com.antutu.ABenchMark)
- **3D Graphics:** [3DMark](https://play.google.com/store/apps/details?id=com.futuremark.dmandroid.application)
- **Battery:** [AccuBattery](https://play.google.com/store/apps/details?id=com.digibites.accubattery)

### ⚠️ Important Notes

- **Same config:** Pastiin semua build pake config yang sama (root method, governor, SUSFS on/off)
- **Clean flash:** Wipe cache sebelum flash kernel baru
- **Consistent testing:** Test di kondisi yang sama (brightness, apps, dll)
- **Multiple runs:** Jalanin benchmark 3x, ambil rata-rata
- **Real-world usage:** Benchmark score ≠ real-world performance, test juga daily usage!

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

- [x] Multi-root method support (KSU-Next, WildKSU, SukiSU, ReSukiSU)
- [x] SUSFS integration (optional toggle)
- [x] Gaming optimizations (HZ_1000, PREEMPT, etc)
- [x] Automated CI/CD builds
- [x] Multi-toolchain support (Bazel, ZyClang, Proton, Neutron)
- [x] Unified build system (1 workflow for all variants)
- [x] Smart kernel naming (includes toolchain info)
- [ ] Benchmark results & toolchain comparison data
- [ ] OC/UV profiles (overclock/undervolt)
- [ ] Custom scheduler tweaks (EAS tuning)
- [ ] Telegram channel/group for community
- [ ] Video installation guide (Bahasa Indonesia)
- [ ] Per-app CPU governor profiles
- [ ] Thermal throttling optimization

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

### 🔨 Toolchain Maintainers
- **[ZyCromerZ](https://github.com/ZyCromerZ/Clang)** - ZyClang toolchain
- **[kdrag0n](https://github.com/kdrag0n/proton-clang)** - Proton Clang
- **[Neutron-Toolchains](https://github.com/Neutron-Toolchains/clang-build-catalogue)** - Neutron Clang
- **[Google](https://android.googlesource.com/)** - Bazel build system & AOSP toolchains

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
