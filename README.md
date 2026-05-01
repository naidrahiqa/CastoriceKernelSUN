# ⚡ Castorice Kernel — Redmi 12 (fire)

Custom kernel for Xiaomi Redmi 12 (codename: **fire**) with **KernelSU-Next** + **SUSFS** support.

## 🔥 Two Kernel Variants

| Variant | Kernel | ROM | Build System |
|---------|--------|-----|-------------|
| **GKI 6.6** | 6.6.x | HyperOS 2.x (Android 15) | Bazel/Kleaf (ACK) |
| **Legacy 4.19** | 4.19.x | MIUI 14 / HyperOS 1.x | make + ZyClang |

> ⚠️ **Flash the correct variant for your ROM!** GKI on HyperOS 1 = bootloop. Legacy on HyperOS 2 = bootloop.

## 📋 Features

### Root & Security
- **KernelSU-Next** — Kernel-based root solution
- **SUSFS** — SUS filesystem for advanced root hiding (SUS_PATH, SUS_MOUNT, SUS_MAP, SUS_KSTAT, SPOOF_UNAME, OPEN_REDIRECT)

### Performance
- **Memory**: ZRAM (writeback), KSM, Transparent Hugepage, compaction
- **I/O**: BFQ scheduler (GKI), optimized readahead
- **Network**: TCP BBR, FQ scheduler, IPSet, TTL target
- **LCD 0c/0d**: Touchscreen fix (Legacy only)

## 🔧 How to Build

### Prerequisites
1. Fork this repo
2. Extract your **stock boot.img** from your current ROM:
   ```bash
   # On rooted device / recovery
   adb shell su -c "dd if=/dev/block/by-name/boot_a of=/sdcard/stock_boot.img"
   adb pull /sdcard/stock_boot.img
   ```
3. Upload `stock_boot.img` somewhere accessible (GitHub release, cloud storage, etc.)

### Run the Build
1. Go to **Actions** tab → Select workflow
2. Fill in **stock_boot_url** with the direct download link to your stock boot.img
3. Enable/disable KSU and SUSFS as needed
4. Click **Run workflow**

### Output Files
| File | Description |
|------|-------------|
| `*-Enforcing.img` | Flashable boot.img (SELinux Enforcing) |
| `*-Permissive.img` | Flashable boot.img (SELinux Permissive) |
| `*-AnyKernel3.zip` | Flashable ZIP via custom recovery |
| `Image*` | Raw kernel image |

## 📱 Flash Guide

### Method 1: Fastboot (Recommended)
```bash
# ALWAYS test first with temporary boot!
fastboot boot Castorice-*-Enforcing.img

# If it boots successfully, flash permanently:
fastboot flash boot Castorice-*-Enforcing.img
fastboot reboot
```

### Method 2: AnyKernel3 ZIP
Flash via TWRP / custom recovery.

### ⚠️ Recovery from Bootloop
```bash
# Flash your stock boot.img back
fastboot flash boot stock_boot.img
fastboot reboot
```

## 🔑 Technical Details

### GKI 6.6 (HyperOS 2)
- **KMI**: `6.6-android15-8` (must match device!)
- **Source**: Android Common Kernel (`common-android15-6.6`)
- **KernelSU**: Latest stable release (kprobes hook)
- **Boot image**: Repacked from stock boot.img via magiskboot
- **Module compat**: `CONFIG_MODVERSIONS=n` (allows vendor module loading)

### Legacy 4.19 (MIUI/HyperOS 1)
- **Source**: `MiCode/Xiaomi_Kernel_OpenSource` branch `fire-t-oss`
- **KernelSU**: `legacy` branch (manual VFS hook)
- **Toolchain**: ZyCromerZ Clang (latest)
- **Boot image**: Repacked from stock boot.img via magiskboot

### Device Info
| Property | Value |
|----------|-------|
| SoC | MediaTek Helio G88 (MT6768) |
| Partition | A/B dual slot |
| Boot size | 128 MB |
| vendor_boot | 64 MB |
| init_boot | ❌ Not present |
| Bootloader | LK (Little Kernel) |

## 📚 References

- [ravindu644/Android-Kernel-Tutorials](https://github.com/ravindu644/Android-Kernel-Tutorials) — Kernel building guide
- [Alexjr2/KernelSU_Next_SUSFS_fire](https://github.com/Alexjr2/KernelSU_Next_SUSFS_fire) — Reference build for fire
- [KernelSU-Next](https://github.com/KernelSU-Next/KernelSU-Next) — Root solution
- [SUSFS4KSU](https://gitlab.com/simonpunk/susfs4ksu) — Root hiding

## ⚖️ License

This project follows the GPL-2.0 license as required by the Linux kernel.
