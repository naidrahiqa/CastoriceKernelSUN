# ⚡ Castorice Kernel — Redmi 12 (fire)

GKI **6.6.58** kernel dengan **KernelSU-Next** + **SUSFS** untuk Redmi 12 (fire) HyperOS 2.0.206+

## Device Info

```
Device:      Redmi 12 (fire)
Kernel:      6.6.58-android15-8 → 6.6.58-Castorice
KMI:         android15-6.6
Boot Header: v3 (GKI)
ROM:         HyperOS 2.0.206+
```

## LCD 0c/0d — AMAN ✅

Di GKI, display driver (termasuk panel 0c/0d) ada di **vendor partition** sebagai module `.ko`.
Yang diganti hanya kernel core → LCD **tetap nyala normal**.

## Build

1. Go to **Actions** → **Build Castorice Kernel**
2. Click **Run workflow**
3. Pilih sublevel (`58`) dan SUSFS (on/off)
4. Tunggu ~60-90 menit
5. Download dari **Artifacts** atau **Releases**

## Flash

```bash
# Backup dulu!
fastboot flash boot stock_boot.img.bak

# Flash Castorice
fastboot flash boot boot.img
fastboot reboot
```

## Recovery

```bash
fastboot flash boot stock_boot.img.bak
fastboot reboot
```

## Credits

- [KernelSU-Next](https://github.com/rifsxd/KernelSU-Next)
- [SUSFS](https://gitlab.com/simonpunk/susfs4ksu)
- [Alexjr2](https://github.com/Alexjr2/KernelSU_Next_SUSFS_fire) — Inspirasi
- [WildKernels](https://github.com/WildKernels/GKI_KernelSU_SUSFS) — Reference
