<div align="center">

# Epitaph Kernel

Epitaph Kernel adalah proyek pengembangan kernel kustom berbasis Generic Kernel Image (GKI 6.6) yang dirancang khusus untuk perangkat **Redmi 12 (fire)** yang menjalankan **HyperOS 2.0 (Android 15)**.

[![GitHub Stars](https://img.shields.io/github/stars/naidrahiqa/epitaph_kernel?style=for-the-badge&logo=github&color=yellow)](https://github.com/naidrahiqa/epitaph_kernel/stargazers)

![Android](https://img.shields.io/badge/Android-15-3DDC84?style=flat-square&logo=android)
![Xiaomi](https://img.shields.io/badge/Device-Redmi%2012%20(fire)-FF6900?style=flat-square&logo=xiaomi)
![Chipset](https://img.shields.io/badge/Chipset-MT6768-orange?style=flat-square)

Proyek ini bertujuan untuk menyediakan build kernel yang stabil dengan integrasi solusi root modern dan fitur keamanan tingkat kernel, dengan tetap mempertahankan kompatibilitas penuh terhadap modul vendor bawaan.

</div>

---

## 📌 Status Proyek & Catatan Rilis (Aktif - v72)

Kami menyajikan status pengembangan kernel ini apa adanya, sesuai dengan hasil pengujian terbaru di lapangan:

*   **v70 (Bazel Build)**: **Berhasil Booting (Booting ✅)**. Namun, masih terdapat beberapa isu operasional yang sedang diselesaikan, antara lain fungsi WiFi dan Hotspot yang tidak aktif, lag pada performa GPU (limiter error), serta penggunaan memori RAM yang cukup tinggi (~3.9 GB).
*   **v71 (ZyClang Build)**: **Bootloop (Gagal ❌)**. Kegagalan sistem ini diidentifikasi berasal dari ketidakcocokan pada toolchain ZyClang atau akibat pengaktifan konfigurasi `DEBUG_INFO_NONE` yang mengganggu kebutuhan subsystem BPF pada Android 15.
*   **v72 (Fokus Pengembangan Saat Ini)**: Difokuskan pada perbaikan fungsionalitas Hotspot (NAT/Netfilter) dan branding kernel. Proses kompilasi diwajibkan menggunakan **Bazel (Kleaf)** sebagai standar baseline demi stabilitas sistem yang optimal.

---

## ⚙️ Aturan Dasar & Spesifikasi Teknis

Untuk memastikan kernel dapat berjalan tanpa memicu kegagalan sistem (bootloop), proyek ini mengikuti arsitektur dan parameter wajib berikut:

1.  **Ukuran Halaman Memori (Page Size)**: Ditetapkan secara ketat pada **4K (CONFIG_ARM64_4K_PAGES=y)**. Penggunaan ukuran halaman 16K atau 64K akan menyebabkan bootloop instan karena modul vendor bawaan stock ROM dikompilasi menggunakan standar 4K.
2.  **Identitas Kernel (Branding)**: Dikonfigurasi dengan nama `-Epitaph` (`CONFIG_LOCALVERSION="-Epitaph"`) untuk memudahkan verifikasi versi kernel langsung dari menu Pengaturan sistem ("Tentang Ponsel").
3.  **Simbol Debugging**: Konfigurasi `CONFIG_DEBUG_INFO_NONE=y` dinonaktifkan pada tahap ini. Android 15 memerlukan informasi BTF (BPF Type Format) agar subsystem jaringan (WiFi/Data) dapat berfungsi dengan benar.
4.  **Standar Toolchain**: Baseline utama dan paling stabil adalah **Bazel / Kleaf** (compiler resmi Google GKI). Toolchain alternatif lain (seperti ZyClang, WeebX, Neutron, atau AOSP Clang) disediakan sebagai opsi eksperimental namun belum direkomendasikan untuk penggunaan harian karena risiko ketidakstabilan.

---

## 🛡️ Solusi Root & Fitur Tambahan yang Terintegrasi

*   **KernelSU-Next**: Metode root terintegrasi langsung di tingkat kernel untuk kontrol akses sistem yang lebih aman dan efisien.
*   **SUSFS (Opsional)**: Patch keamanan tingkat kernel untuk menyembunyikan status modifikasi sistem, mount point kustom, serta keberadaan root dari aplikasi yang sensitif (seperti aplikasi perbankan atau deteksi Play Integrity).
*   **Netfilter NAT**: Dukungan modul penunjang hotspot (`CONFIG_NF_NAT`, `CONFIG_IP_NF_NAT`, dan `CONFIG_NETFILTER_XT_TARGET_MASQUERADE`) yang sedang dikembangkan untuk memulihkan fungsi berbagi koneksi internet.
*   **Optimasi Jaringan**: Menggunakan TCP BBR Congestion Control dan FQ (Fair Queueing) Packet Scheduler untuk transmisi data yang lebih teratur dan efisien.

---

## 📥 Panduan Instalasi Bersih (Clean Installation)

### 1. Menonaktifkan Verifikasi Partisi (Fastboot Mode)
Sebelum memasang kernel kustom untuk pertama kalinya, Anda wajib menonaktifkan pemeriksaan veritas (AVB) pada partisi perangkat Anda.
Jalankan perangkat ke dalam **Fastboot Mode** lalu eksekusi perintah berikut melalui PC:
```bash
fastboot --disable-verity --disable-verification flash vbmeta vbmeta.img
fastboot --disable-verity --disable-verification flash vbmeta_system vbmeta_system.img
fastboot --disable-verity --disable-verification flash vbmeta_vendor vbmeta_vendor.img
```
*Catatan: Ekstrak file `.img` di atas dari Fastboot ROM stock HyperOS 2.0 resmi yang sesuai dengan versi firmware perangkat Anda.*

### 2. Pemasangan Kernel
Karena keterbatasan kompatibilitas rendering grafis pada Custom Recovery (TWRP/OrangeFox) di Android 15 untuk Redmi 12, pemasangan sangat direkomendasikan menggunakan aplikasi **Kernel Flasher**.

1.  Unduh arsip instalasi AnyKernel3 yang sesuai dari halaman rilis (misalnya: `Epitaph-v72-bazel-schedutil-false.zip`).
2.  Pasang aplikasi [Kernel Flasher Manager](https://github.com/capntrips/KernelFlasher/releases) pada perangkat Anda.
3.  Buka aplikasi, pilih arsip AnyKernel3 yang telah diunduh, lalu tekan opsi **Flash**.
4.  Setelah proses selesai dengan sukses, lakukan reboot sistem.
5.  Gunakan aplikasi manager pendukung seperti KernelSU-Next Manager untuk mengelola hak akses root.

---

## 🛠️ Panduan Debugging & Pengambilan Log

Jika Anda mengalami kendala seperti bootloop atau tidak berfungsinya suatu fitur, Anda dapat memanfaatkan fitur debugging bawaan kernel ini:

### 1. Mendiagnosis Bootloop (PStore / RAMoops)
Kernel ini mengaktifkan konfigurasi `pstore` yang menyimpan log kernel terakhir ke area RAM yang tidak terhapus selama perangkat tidak kehilangan daya total.

1.  Biarkan perangkat melakukan bootloop hingga mengarah ke Fastboot atau restart berulang.
2.  Masuk ke mode Fastboot (`Volume Down + Power`), lalu flash kembali kernel bawaan (stock):
    ```bash
    fastboot flash boot boot_stock.img
    fastboot reboot
    ```
3.  Setelah perangkat masuk ke sistem Android secara normal, ambil log kegagalan melalui ADB Shell:
    ```bash
    adb shell
    su
    # Salin log dmesg terakhir ke penyimpanan internal
    cat /sys/fs/pstore/console-ramoops-0 > /sdcard/last_kmsg.log
    cat /sys/fs/pstore/dmesg-ramoops-0 > /sdcard/panic_log.txt
    ```
4.  Periksa file `last_kmsg.log` untuk melihat baris instruksi atau driver yang memicu crash (Kernel Panic).

### 2. Menganalisis Kendala Fungsional (Live Log)
Jika perangkat berhasil masuk ke menu utama namun fungsi tertentu (seperti WiFi atau modul root) tidak aktif:
```bash
adb shell "su -c dmesg" > dmesg_live.log
```
Gunakan teks editor untuk mencari kata kunci seperti `Kernel panic`, `Call Trace`, atau pesan kesalahan driver untuk mengidentifikasi letak kendala.

---

## 🤖 Pemicu Build Otomatis (GKI Control Center)

Alur kerja (workflow) GitHub Actions di repositori ini dilengkapi dengan **GKI Control Center** untuk mempermudah build otomatis langsung di server GitHub:

1.  Lakukan **Fork** pada repositori ini.
2.  Buka menu **Actions** lalu pilih **GKI Control Center**.
3.  Tekan tombol **Run workflow** dan tentukan parameter build yang diinginkan:
    *   **Custom Name & Author**: Penamaan branding kernel kustom Anda.
    *   **SUSFS Variant**: Memilih untuk menyertakan patch SUSFS atau membuat build vanilla GKI.
    *   **Toolchain Compilation**: Memilih compiler utama (Bazel direkomendasikan untuk build stabil).

---

## 💎 Apresiasi & Sumber Terkait

Pengembangan kernel kustom ini didukung oleh kontribusi dari berbagai proyek open-source luar biasa:
*   [KernelSU-Next Team](https://github.com/KernelSU-Next/KernelSU-Next) - Solusi root modern berbasis kernel.
*   [Simonpunk (SUSFS)](https://gitlab.com/simonpunk/susfs4ksu) - Patch anti-deteksi root tingkat lanjut.
*   [Osm0sis (AnyKernel3)](https://github.com/osm0sis/AnyKernel3) - Tool installer ramdisk Android.
*   [Google AOSP Android Common Kernels](https://android.googlesource.com/kernel/manifest) - Kode dasar platform GKI.
