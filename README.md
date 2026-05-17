<div align="center">

# 🌌 Epitaph Kernel
### A High-Performance, Gaming-Optimized GKI 6.6 Kernel for Redmi 12 (fire)

[![GitHub Release](https://img.shields.io/github/v/release/naidrahiqa/epitaph_kernel?style=for-the-badge&logo=github&color=6a0dad)](https://github.com/naidrahiqa/epitaph_kernel/releases/latest)
[![GitHub Downloads](https://img.shields.io/github/downloads/naidrahiqa/epitaph_kernel/total?style=for-the-badge&logo=github&color=3a0066)](https://github.com/naidrahiqa/epitaph_kernel/releases)
[![GitHub Stars](https://img.shields.io/github/stars/naidrahiqa/epitaph_kernel?style=for-the-badge&logo=github&color=ffd700)](https://github.com/naidrahiqa/epitaph_kernel/stargazers)

![Android Version](https://img.shields.io/badge/OS-Android%2015%20(HyperOS%202)-3DDC84?style=flat-square&logo=android&logoColor=white)
![Target Device](https://img.shields.io/badge/Device-Redmi%2012%20(fire)-FF6900?style=flat-square&logo=xiaomi&logoColor=white)
![Soc Chipset](https://img.shields.io/badge/Chipset-MediaTek%20MT6768%20(G88)-009688?style=flat-square&logo=cpu)
![Build Engine](https://img.shields.io/badge/Compiler-Kleaf%20/%20Bazel-blue?style=flat-square&logo=google)

</div>

---

## ⚡ Overview

Welcome to **Epitaph Kernel**, a meticulously engineered Generic Kernel Image (GKI 6.6) designed exclusively for the **Redmi 12 (fire)** running **HyperOS 2 (Android 15)**. 

Epitaph represents the pinnacle of MediaTek MT6768 performance tuning, striking a perfect equilibrium between extreme gaming capabilities, lightning-fast scheduling latency, modern memory architecture, and robust root/anti-detection features.

> [!WARNING]
> **COMPATIBILITY REQUIREMENT:** This kernel is built strictly for **HyperOS 2 based on Android 15 (GKI 6.6 architecture)**. Flashing this kernel on MIUI 14 or HyperOS 1 (Android 13/14) will result in an immediate bootloop!

---

## 🚀 Key Features

### 🎮 Gaming & Low-Latency Optimizations
*   **HZ_1000 Timer:** Minimal latency and maximum input accuracy with a 1000Hz tick rate.
*   **Full PREEMPT (Real-time Preemption):** Higher frame consistency and reduced micro-stutters by allowing execution preemption anywhere in the kernel.
*   **HRTIMER:** Precision high-resolution timing for smooth frame intervals.

### 🧠 Modern Memory Architecture
*   **LRU-Gen (MGLRU):** Highly optimized Multi-Generational Least Recently Used memory reclamation policy.
*   **LZ4 / ZSTD ZRAM:** Ultra-fast RAM compression engine providing instant decompression speeds.
*   **Kernel Samepage Merging (KSM):** Intelligently merges redundant memory pages to maximize free RAM.

### 🌐 Network & I/O Optimizations
*   **TCP BBR Congestion Control:** Developed by Google, ensuring minimal network ping fluctuations and ultra-smooth packet handling.
*   **FQ (Fair Queueing) Packet Scheduler:** Drastically reduces bufferbloat during intensive multiplayer gaming sessions.
*   **BFQ I/O Scheduler:** Tailored scheduler optimizations to improve read/write latency on eMMC/UFS storage.

---

## 🎯 Variant Matrix (Pilih Sesuai Kebutuhan)

### 🛡️ 1. Anti-Detection (SUSFS)
*   **With SUSFS:** Integrated kernel-level hooks to completely hide root, custom mounts, and system modifications from banking apps and aggressive anti-cheats (e.g. Google Play Integrity, major competitive games).
*   **No SUSFS:** Pure standard kernel layout for everyday tasks.

### 🔑 2. Advanced Root Solutions
*   **KernelSU-Next:** Next-generation kernel-integrated root solution with premium modules mounting, extreme stability, and active updates.

### ⚙️ 3. CPU Governors
*   **schedutil:** Power-aware default governor tailored for general daily usage with dynamic performance scaling.
*   **performance:** Hardcore gaming profile forcing CPU cores to remain at maximum frequencies.
*   **ondemand / conservative:** Balanced and battery-saving alternatives.

---

## 📥 Clean Installation Guide

### 1. Bypass Verification (Fastboot Mode)
Before flashing the custom kernel for the first time, you must unlock and disable verity checks on your partition layouts. 
Boot into **Fastboot Mode** and execute:
```bash
fastboot --disable-verity --disable-verification flash vbmeta vbmeta.img
fastboot --disable-verity --disable-verification flash vbmeta_system vbmeta_system.img
fastboot --disable-verity --disable-verification flash vbmeta_vendor vbmeta_vendor.img
```
> [!NOTE]
> You must extract the corresponding `.img` files from your device's exact stock HyperOS 2 Fastboot ROM.

### 2. Flashing the Kernel
> [!IMPORTANT]
> Because custom recovery (TWRP/OrangeFox) has hardware rendering limitations on Redmi 12 (fire) under Android 15, we strictly recommend using **Kernel Flasher**.

1.  Download the desired zip from our [**Releases Page**](../../releases/latest) (e.g., `Epitaph-Epitaph-v45-GKI66-KSUNext-SUSFS-Performance-balanced-stable-Bazel-Redmi12.zip`).
2.  Install [Kernel Flasher Manager](https://github.com/capntrips/KernelFlasher/releases) on your phone.
3.  Open the application, select the downloaded AnyKernel3 zip file.
4.  Tap **Flash**, wait for the success screen, and reboot.
5.  Install the [KernelSU-Next Manager App](https://github.com/KernelSU-Next/KernelSU-Next/releases) to manage root permissions.

---

## 🛠️ Build Custom Variants (GKI Control Center)

Epitaph Kernel features an automated compile pipeline called **🎛️ GKI Control Center**. You don't need to configure compile trees manually. You can trigger a multi-architecture matrix build directly from GitHub!

1.  **Fork** this repository.
2.  Navigate to your fork's **Actions** tab and select **🎛️ GKI Control Center**.
3.  Click **Run workflow** and choose your custom combinations:
    *   **Root Methods:** Select `KernelSU-Next`.
    *   **SUSFS Integration:** Choose whether to patch `SUSFS` or build vanilla GKI.
    *   **Toolchain Compilation:** Build with Bazel, ZyClang, WeebX, Neutron, Azure, or AOSP Clang.
    *   **Custom Name & Author:** Define your own branding tags (Defaults to `Epitaph` by `Naidrahiqa`).

### 🔨 Supported Toolchains
*   **Bazel (Kleaf):** Official Google GKI compilation standard. Extremely robust and reliable.
*   **ZyClang / WeebX:** Custom Clang setups optimized with aggressive performance flags for high-end CPU workloads.
*   **Neutron / Azure:** Modern LLVM compilers focusing on binary reduction, RELR relocations, and execution efficiency.

---

## 🦾 Technical Development & Bug Fixes

We have solved critical GKI constraints to guarantee full compatibility on Android 15 HyperOS 2:
*   **SELinux / LSM Signature Bypass:** Compiled with `CONFIG_MODULE_SIG_PROTECT=n` to allow successful manual and boot-time `insmod` execution of GKI modules (like `cfg80211.ko` and `mac80211.ko`) from system folders.
*   **Resolved Module Dependency Chains:** The startup sequence automatically handles the loading dependencies (`rfkill` $\rightarrow$ `libarc4` $\rightarrow$ `cfg80211` $\rightarrow$ `mac80211`) to prevent missing symbols.
*   **Smart Archive Extractor:** The build pipeline automatically detects and processes both "flat" and "nested" toolchain archives, avoiding "Clang not found" interruptions.
*   **Host Linker Fix:** Enforces system-level GNU linkers on dynamic hosts to avoid relocation blocks (`.relr.dyn`) on modern Glibc runtimes.

---

## 📊 Pipeline Status

| Automated Pipeline | Compilation Status |
|:-------------------|:------------------:|
| **🎛️ GKI Control Center** | [![GKI Control Center](https://github.com/naidrahiqa/epitaph_kernel/actions/workflows/build_manager_gki.yml/badge.svg)](https://github.com/naidrahiqa/epitaph_kernel/actions/workflows/build_manager_gki.yml) |
| **⚙️ Core Build Engine** | [![Core Build](https://github.com/naidrahiqa/epitaph_kernel/actions/workflows/_build_kernel_core.yml/badge.svg)](https://github.com/naidrahiqa/epitaph_kernel/actions/workflows/_build_kernel_core.yml) |

---

## 💖 Acknowledgements

Epitaph Kernel is built on top of the incredible open-source work by:
*   **[KernelSU-Next Team](https://github.com/KernelSU-Next/KernelSU-Next):** Next-gen kernel root.
*   **[simonpunk](https://gitlab.com/simonpunk/susfs4ksu):** SUSFS security and anti-detection.
*   **[osm0sis](https://github.com/osm0sis/AnyKernel3):** Premium Android ramdisk installer.
*   **[Google: Android Common Kernels](https://android.googlesource.com/kernel/manifest):** Base GKI platform code.

---

<div align="center">

### 🎮 Engineered for Performance. Tailored for Gamers.
**If you enjoy this kernel, show some love by leaving a ⭐ on this repository!**  
Developed with ❤️ by **Naidrahiqa** for the Redmi 12 (fire) Community.

</div>
