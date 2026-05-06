<div align="center">

# ⚡ Castorice KernelSUN ⚡
**High-Performance Gaming Kernel for Redmi 12 (fire)**

![Android](https://img.shields.io/badge/Android-13%20%7C%2014%20%7C%2015-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![Xiaomi](https://img.shields.io/badge/Xiaomi-HyperOS%20%7C%20MIUI-FF6900?style=for-the-badge&logo=xiaomi&logoColor=white)
![KernelSU](https://img.shields.io/badge/KernelSU-Multi--Variant-12B9A1?style=for-the-badge)
![SUSFS](https://img.shields.io/badge/SUSFS-Optional-blueviolet?style=for-the-badge)

</div>

---

## 📌 Overview

**Castorice Kernel** is a gaming-focused custom kernel built for the **Xiaomi Redmi 12 (fire)** with MT6768 chipset. Optimized for maximum performance, low latency, and flexible root options with multiple KernelSU variants.

We provide **4 automated workflows** covering both GKI and Legacy kernels, with optional SUSFS integration for advanced root hiding.

---

## 🚀 Kernel Variants

### 📦 Available Workflows

| Workflow | Kernel | Root Options | SUSFS | Best For |
|:---------|:-------|:-------------|:------|:---------|
| **🟢 GKI 6.6 — KernelSU** | Linux 6.6 | KSU-Next, WildKSU, SukiSU, ReSukiSU | ❌ | HyperOS 2 (Android 15) - Daily Driver |
| **🟣 GKI 6.6 — KernelSU + SUSFS** | Linux 6.6 | KSU-Next, WildKSU, SukiSU, ReSukiSU | ✅ | HyperOS 2 - Banking Apps & Games |
| **🟠 Legacy 4.19 — KernelSU** | Linux 4.19 | KSU-Next, WildKSU, SukiSU, ReSukiSU | ❌ | MIUI 14 / HyperOS 1 - Daily Driver |
| **🔴 Legacy 4.19 — KernelSU + SUSFS** | Linux 4.19 | KSU-Next, WildKSU, SukiSU, ReSukiSU | ✅ | MIUI 14 / HyperOS 1 - Banking Apps |

### 🎮 Root Method Options

| Method | Description | Recommended For |
|:-------|:------------|:----------------|
| **KernelSU-Next** | Official next-gen KernelSU | Most users (stable) |
| **WildKSU** | Unofficial KernelSU fork with extra features | Advanced users |
| **SukiSU** | Alternative KSU implementation | Testing/Development |
| **ReSukiSU** | Rebuilt SukiSU variant | Experimental |

### ⚙️ CPU Governor Options

All workflows support custom CPU governors (switchable via kernel tuner apps):
- **schedutil** (default) - Balanced performance & battery
- **performance** - Maximum performance (gaming)
- **ondemand** - Dynamic scaling
- **conservative** - Battery saver

---

## ✨ Features

### 🎮 Gaming Optimizations
- **HZ_1000:** 1000Hz timer frequency for ultra-low latency
- **Full PREEMPT:** Preemptible kernel for smoother gaming
- **HRTIMER:** High-resolution timers for precise frame timing
- **All CPU Governors Built-in:** Switch governors on-the-fly

### 🛡️ Root & Security
- **Multiple KernelSU Variants:** Choose your preferred root method
- **SUSFS Integration (Optional):** Advanced root hiding
  - Path/mount hiding
  - kstat spoofing
  - uname spoofing
  - Symbol hiding from kallsyms
- **Module Compatibility:** MODVERSIONS enabled on GKI (vendor modules safe)

### 🧠 Memory & Performance
- **LRU-Gen:** Multi-Gen LRU for better memory management (GKI)
- **LZ4/ZSTD ZRAM:** Fast compression with writeback support
- **KSM:** Kernel Samepage Merging for memory deduplication
- **Transparent Hugepages:** Better memory performance

### 🌐 I/O & Networking
- **TCP BBR:** Google's BBR congestion control for faster networking
- **BFQ + Kyber I/O Schedulers:** Optimized disk I/O
- **IPSet Support:** Advanced firewall capabilities
- **FQ Qdisc:** Fair Queue packet scheduling

### 📱 Device-Specific Fixes
- **LCM 0c/0d Panel Fix:** Fixed touchscreen issues on both panel variants
- **Primary Display Fix:** Smoother 90Hz rendering
- **Focaltech Touchscreen Patch:** Better touch responsiveness

---

## 📥 Installation Guide

### ⚠️ Important: Choose the Correct Variant!

| Your OS | Kernel to Flash |
|:--------|:----------------|
| **HyperOS 2.x (Android 15)** | GKI 6.6 |
| **HyperOS 1.x (Android 14)** | Legacy 4.19 |
| **MIUI 14 (Android 13)** | Legacy 4.19 |

> [!WARNING]
> Flashing the wrong kernel version will cause a **bootloop**!

### 📲 Installation Steps

1. **Download** the latest `Castorice-XXX-AnyKernel3.zip` from [Releases](../../releases)
2. **Flash** using one of these methods:
   - **Kernel Flasher App** (recommended for Redmi 12 fire due to LCM issue)
   - Custom Recovery (TWRP/OrangeFox) if available
3. **Reboot** to system
4. **Install** [KernelSU Manager](https://github.com/KernelSU-Next/KernelSU-Next/releases) (for KSU-Next) or respective manager for your chosen root method
5. **Verify** installation: Check kernel version in Settings → About Phone

### 🔧 Post-Installation (Optional)

- Use kernel tuner apps (e.g., Franco Kernel Manager, EX Kernel Manager) to:
  - Switch CPU governors
  - Adjust I/O schedulers
  - Fine-tune performance profiles

---

## 🛠️ Build Your Own Kernel

This repository uses **GitHub Actions** for automated builds. You can build custom kernels yourself!

### 🚀 Quick Build

1. **Fork** this repository
2. Go to **Actions** tab
3. Select a workflow:
   - `🔥 GKI 6.6 — KernelSU (No SUSFS)`
   - `🔥 GKI 6.6 — KernelSU + SUSFS`
   - `🔥 Legacy 4.19 — KernelSU (No SUSFS)`
   - `🔥 Legacy 4.19 — KernelSU + SUSFS`
4. Click **Run workflow**
5. Configure build options:
   - **Custom Name:** Your kernel name (e.g., "Gaming")
   - **Author Name:** Your name
   - **Root Method:** kernelsu-next / wildksu / sukisu / rsukisu
   - **CPU Governor:** schedutil / performance / ondemand / conservative
6. Wait for build to complete (~20-30 minutes)
7. Download the flashable zip from **Artifacts**

### 📋 Build Output Naming

```
Castorice-<Name>-v<BuildNumber>-<GKI/Legacy>-<RootMethod>-<SUSFS?>-<Governor>-Redmi12-AnyKernel3.zip
```

Example: `Castorice-Gaming-v45-GKI-6.6-kernelsu-next-SUSFS-performance-Redmi12-AnyKernel3.zip`

---

## 🔍 Compatibility Matrix

| Feature | GKI 6.6 | Legacy 4.19 |
|:--------|:-------:|:-----------:|
| HyperOS 2 (Android 15) | ✅ | ❌ |
| HyperOS 1 (Android 14) | ❌ | ✅ |
| MIUI 14 (Android 13) | ❌ | ✅ |
| KernelSU-Next | ✅ | ✅ |
| WildKSU | ✅ | ✅ |
| SukiSU | ✅ | ✅ |
| ReSukiSU | ✅ | ✅ |
| SUSFS | ✅ | ✅ |
| LRU-Gen | ✅ | ❌ |
| MODVERSIONS | ✅ | ❌ |
| All CPU Governors | ✅ | ✅ |

---

## 🐛 Known Issues

- **Custom Recovery:** Not available for HyperOS 2 due to LCM 0c/0d panel issue → Use Kernel Flasher app
- **SUSFS on GKI:** May fail to integrate on some builds → Falls back to non-SUSFS build automatically

---

## 📊 Benchmark Results

> Coming soon! Will include AnTuTu, Geekbench, and gaming FPS comparisons.

---

## 💖 Credits & Acknowledgements

### 🙏 Special Thanks

- **[KernelSU-Next](https://github.com/KernelSU-Next/KernelSU-Next)** - Next-gen kernel-level root
- **[WildKernels](https://github.com/WildKernels/Wild_KSU)** - WildKSU variant
- **[SukiSU-Ultra](https://github.com/SukiSU-Ultra/SukiSU-Ultra)** - SukiSU implementation
- **[ReSukiSU](https://github.com/ReSukiSU/ReSukiSU)** - ReSukiSU variant
- **[simonpunk](https://gitlab.com/simonpunk/susfs4ksu)** - SUSFS for advanced root hiding
- **[osm0sis](https://github.com/osm0sis/AnyKernel3)** - AnyKernel3 flasher
- **[ZyCromerZ](https://github.com/ZyCromerZ/Clang)** - ZyClang toolchain
- **[MiCode](https://github.com/MiCode/Xiaomi_Kernel_OpenSource)** - Xiaomi kernel sources
- **[Google](https://android.googlesource.com/kernel/manifest)** - Android Common Kernel (GKI)

### 🌟 Community

- **[Alexjr2](https://github.com/Alexjr2/KernelSU_Next_SUSFS_fire)** - Reference patches and inspiration

---

## 📜 License

This project is licensed under **GPL-2.0** - see the kernel source repositories for details.

---

## 🔗 Links

- **Releases:** [GitHub Releases](../../releases)
- **Issues:** [Report Bugs](../../issues)
- **Discussions:** [GitHub Discussions](../../discussions)
- **Telegram:** Coming soon!

---

<div align="center">

**Made with ❤️ for Redmi 12 (fire) Community**

⭐ Star this repo if you find it useful!

</div>
