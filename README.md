# ⚡ Castorice Kernel — Redmi 12 (fire)

Custom kernel dengan **KernelSU-Next** + **SUSFS** untuk Redmi 12 (fire).  
Tersedia dalam **2 versi** — pilih sesuai ROM kamu.

## 📦 Versi

| Versi | Kernel | Target ROM | LCD 0c/0d | Build |
|-------|--------|------------|-----------|-------|
| **Castorice Legacy** | 4.19.x | MIUI 14 / HyperOS 1.x (A13-14) | ✅ Patched | `make` + ZyClang |
| **Castorice GKI** | 6.6.135 | HyperOS 2.x (A15) | ✅ Safe (vendor module) | Bazel/Kleaf |

## 🖥️ Device Info

```
Device:      Redmi 12 (fire)
SoC:         MediaTek Helio G88 (MT6768)
```

### Legacy (4.19)
```
Kernel:      4.19.x-Castorice
KMI:         Non-GKI (Xiaomi source)
KernelSU:    KernelSU-Next Legacy (manual hook)
ROM:         MIUI 14.x / HyperOS 1.x
```

### GKI (6.6)
```
Kernel:      6.6.135-Castorice
KMI:         android15-6.6
KernelSU:    KernelSU-Next (latest)
ROM:         HyperOS 2.0.206+
```

## 📱 LCD 0c/0d — AMAN ✅

### GKI 6.6
Display driver ada di **vendor partition** sebagai `.ko` module.  
Kernel core diganti → LCD + touchscreen **tetap normal**.

### Legacy 4.19
Display driver **terintegrasi di kernel**, tapi sudah di-patch dengan:
- `fix_lcm.patch` — Fix LCM driver untuk panel 0c/0d
- `primary_display_fix.patch` — Fix pointer bug di display command

Touchscreen **aman** di kedua versi.

## 🚀 Fitur Performa Stabil

- ⚡ **CPU**: schedutil governor + Energy Aware Scheduling
- 🌐 **Network**: TCP BBR + IPSet support + TTL mangling
- 💾 **Memory**: ZRAM + LZ4 compression
- 🔧 **I/O**: CFQ (4.19) / mq-deadline (6.6)
- 🛡️ **Root**: KernelSU-Next + SUSFS (hide root)
- 🔒 **Security**: SUSFS spoof uname, cmdline, symbol hiding

## 🔨 Build

1. Go to **Actions**
2. Pilih workflow:
   - **Build Castorice Legacy (4.19)** — untuk MIUI 14 / HyperOS 1
   - **Build Castorice GKI (6.6)** — untuk HyperOS 2
3. Click **Run workflow**
4. Pilih opsi (SUSFS on/off, sublevel)
5. Tunggu selesai
6. Download dari **Artifacts** atau **Releases**

## 📲 Flash

```bash
# Backup dulu!
fastboot flash boot stock_boot.img.bak

# Flash Castorice
fastboot flash boot boot.img  # atau flash AnyKernel3 zip via recovery
fastboot reboot
```

## 🔄 Recovery

```bash
fastboot flash boot stock_boot.img.bak
fastboot reboot
```

## 📋 Credits

- [KernelSU-Next](https://github.com/rifsxd/KernelSU-Next) — Root solution
- [SUSFS](https://gitlab.com/simonpunk/susfs4ksu) — Root hiding
- [Alexjr2](https://github.com/Alexjr2/KernelSU_Next_SUSFS_fire) — Reference 4.19 build + LCD patches
- [WildKernels](https://github.com/WildKernels/GKI_KernelSU_SUSFS) — GKI reference
- [ZyCromerZ](https://github.com/ZyCromerZ/Clang) — Clang toolchain
- [sidex15](https://github.com/sidex15/KernelSU-Next) — KernelSU-Next legacy branch
