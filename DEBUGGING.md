# 🛠️ Redmi 12 (fire) Kernel Debugging Guide

Dokumen ini berisi panduan praktis untuk mendiagnosis masalah kernel (bootloop, crash, atau fitur tidak jalan) pada Redmi 12, terutama bagi kamu yang tidak memiliki Custom Recovery (TWRP/OrangeFox).

---

## 🚀 1. Mengambil Log Setelah Bootloop (PStore/Ramoops)

GKI (Generic Kernel Image) memiliki fitur bernama `pstore` yang menyimpan log kernel terakhir ke dalam RAM yang tidak terhapus saat reboot (selama hardware tidak kehilangan daya total).

### Langkah-langkah:
1. **Trigger Bootloop**: Flash kernel custom kamu. Biarkan HP mencoba booting sampai terjadi "Panic" (biasanya restart sendiri atau masuk ke Fastboot).
2. **Masuk ke Fastboot**: Tekan dan tahan `Volume Down + Power`.
3. **Flash Kernel Stock**: Kembalikan HP ke kondisi bisa booting dengan mem-flash kernel ori/stock.
   ```bash
   fastboot flash boot boot_stock.img
   fastboot reboot
   ```
4. **Tarik Log PStore**: Begitu HP masuk ke sistem Android, buka terminal di PC dan jalankan:
   ```bash
   # Masuk ke shell root
   adb shell
   su
   
   # Cek apakah ada file di pstore
   ls /sys/fs/pstore/
   
   # Salin log dmesg terakhir (pilih salah satu yang ada)
   cat /sys/fs/pstore/console-ramoops-0 > /sdcard/last_kmsg.log
   cat /sys/fs/pstore/dmesg-ramoops-0 > /sdcard/panic_log.txt
   ```
5. **Analisis**: File `last_kmsg.log` tersebut berisi rekaman detik-detik sebelum kernel custom kamu mati.

---

## 📡 2. Mengambil Log Live (ADB Dmesg)

Gunakan ini jika HP **berhasil masuk ke Android** tapi ada fitur yang tidak jalan (misal: KernelSU tidak terbaca, WiFi mati, dsb).

```bash
# Simpan dmesg ke file secara real-time
adb shell "su -c dmesg" > dmesg_live.log
```

---

## 🔍 3. Apa yang Harus Dicari di Log?

Buka file log menggunakan Text Editor (VS Code/Notepad++) dan cari kata kunci berikut:

| Kata Kunci | Arti | Solusi Umum |
| :--- | :--- | :--- |
| `Kernel panic` | Kernel menyerah karena error fatal. | Cek baris di atasnya untuk melihat driver yang crash. |
| `Call Trace` | Jejak eksekusi fungsi sebelum crash. | Lihat fungsi terakhir yang dipanggil (biasanya ada nama file `.c`). |
| `init: Service '...' killed` | Proses sistem mati karena kernel bermasalah. | Sering terjadi jika `MODVERSIONS` dimatikan. |
| `KSU: ...` | Log dari KernelSU. | Cek apakah hooks berhasil terpasang atau ditolak. |
| `uapi/... missing` | Error saat compile. | Pastikan folder `uapi` sudah ikut disalin di workflow. |

---

## 💡 4. Tips Khusus Redmi 12 (fire)

### format Image
Redmi 12 menggunakan MediaTek Helio G88. Bootloader-nya seringkali **menolak** file `Image` mentah (uncompressed).
- **Selalu gunakan `Image.gz`** untuk di-pack ke AnyKernel3.
- Jika menggunakan `Image` raw, HP biasanya akan langsung masuk ke Fastboot (Bad Image).

### VBMeta Flags
Jika kamu mem-flash kernel custom, pastikan kamu sudah mematikan verifikasi Android (AVB):
```bash
fastboot --disable-verity --disable-verification flash vbmeta vbmeta.img
```
*Gunakan `vbmeta.img` dari ROM yang sedang kamu pakai.*

### KMI Version
Pastikan base kernel kamu cocok dengan versi firmware. 
- Stock HyperOS 2 biasanya menggunakan KMI versi `8`. 
- Cek `scripts/setlocalversion` jika ada masalah symbol mismatch.

---
> **Note**: Log adalah teman terbaikmu. Jangan menebak-nebak kenapa bootloop, biarkan `dmesg` yang memberitahu alasannya.
