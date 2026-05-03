<div align="center">

# ⚡ Castorice KernelSUN ⚡
**High-Performance Custom Kernel for Redmi 12 (fire)**

![Android](https://img.shields.io/badge/Android-13%20%7C%2014%20%7C%2015-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![Xiaomi](https://img.shields.io/badge/Xiaomi-HyperOS%20%7C%20MIUI-FF6900?style=for-the-badge&logo=xiaomi&logoColor=white)
![KernelSU-Next](https://img.shields.io/badge/KernelSU--Next-Integrated-12B9A1?style=for-the-badge)
![SUSFS](https://img.shields.io/badge/SUSFS-Supported-blueviolet?style=for-the-badge)

*Built with ❤️ by Castorice*

</div>

---

## 📌 Overview

**Castorice Kernel** is a highly optimized custom kernel tailored specifically for the **Xiaomi Redmi 12 (fire)**. Built to deliver maximum performance, battery efficiency, and stealthy root capabilities out-of-the-box.

We maintain **two dedicated branches/variants** to ensure maximum compatibility across all MIUI and HyperOS versions.

---

## 🚀 Kernel Variants

| Variant | Kernel Version | Supported OS | Best For | CI/CD Status |
| :---: | :---: | :--- | :--- | :---: |
| **🟢 GKI** | `Linux 6.6` | HyperOS 2.x (Android 15) | Daily Driver on Modern HyperOS | [![Build GKI](https://img.shields.io/github/actions/workflow/status/naidrahiqa/CastoriceKernelSUN/build_gki.yml?branch=main&label=Build%20GKI&style=flat-square)](https://github.com/naidrahiqa/CastoriceKernelSUN/actions) |
| **🟠 Legacy** | `Linux 4.19` | MIUI 14 (A13) & HyperOS 1 (A14) | Legacy Firmware Compatibility | [![Build Legacy](https://img.shields.io/github/actions/workflow/status/naidrahiqa/CastoriceKernelSUN/build_legacy.yml?branch=main&label=Build%20Legacy&style=flat-square)](https://github.com/naidrahiqa/CastoriceKernelSUN/actions) |

---

## ✨ Features

### 🛡️ Root & Security
*   **KernelSU-Next Built-in:** Next-generation kernel-level root solution.
*   **SUSFS Integration:** Advanced mount namespace and path hiding to bypass root detections (banking apps, games, etc).
*   **Module Spoofing:** Bypass module signature enforcement on GKI builds.

### 🧠 Memory & CPU
*   **Optimized ZRAM:** Better RAM management with LZ4 writeback.
*   **MGLRU Enabled:** Advanced Multi-Gen LRU for smoother multitasking (GKI).
*   **KSM & Compaction:** Reduces memory fragmentation on heavy workloads.

### 🌐 I/O & Networking
*   **TCP BBR Congestion Control:** Faster network throughput and lower latency.
*   **IPSet Enabled:** Support for advanced firewall and network routing modules.
*   **BFQ Scheduler:** Snappier app launches and background I/O operations.

### 📱 Device Specific Fixes
*   **LCD Touchscreen Patch:** Fixed touch registration for `0c/0d` panels (Legacy).
*   **Primary Display Fix:** Smoother UI rendering on 90Hz panels.

---

## 📥 Installation Guide

> [!WARNING]
> Ensure you are flashing the correct variant for your Android/HyperOS version. Flashing the wrong variant will result in a bootloop!

1. Download the latest `AnyKernel3.zip` from the [Releases Tab](../../releases).
2. Reboot your device into a Custom Recovery (TWRP / OrangeFox) or use a Kernel Flasher app (if already rooted).
3. Flash the `Castorice-XXX-AnyKernel3.zip`.
4. (Optional) Wipe Dalvik / Cache.
5. Reboot to System.
6. Install the [KernelSU-Next Manager App](https://github.com/KernelSU-Next/KernelSU-Next/releases) to manage root permissions.

---

## 🛠️ Automated CI/CD Builds

This repository is powered by **GitHub Actions**. You can automatically build the kernel yourself!
1. Fork this repository.
2. Go to the **Actions** tab.
3. Select either `Build Castorice GKI (6.6)` or `Build Castorice Legacy (4.19)`.
4. Click **Run workflow**. 
5. Grab your compiled flashable zip from the artifacts!

---

## 💖 Credits & Acknowledgements

*   [KernelSU-Next](https://github.com/KernelSU-Next/KernelSU-Next) for the incredible root solution.
*   [simonpunk](https://gitlab.com/simonpunk/susfs4ksu) for the SUSFS magic.
*   [osm0sis](https://github.com/osm0sis/AnyKernel3) for AnyKernel3.
*   [ZyCromerZ](https://github.com/ZyCromerZ/Clang) for the ZyClang Toolchain.
*   [MiCode](https://github.com/MiCode/Xiaomi_Kernel_OpenSource) for the open-source kernel trees.

<div align="center">
  <p><i>Enjoying the kernel? Don't forget to star ⭐ the repository!</i></p>
</div>
