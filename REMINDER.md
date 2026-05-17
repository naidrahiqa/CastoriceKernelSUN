# Pengingat Penyederhanaan & Perbaikan Alur Kerja (Workflow Fixes)

> [!NOTE]
> Dokumen ini mencatat ringkasan simplifikasi antarmuka input alur kerja, perbaikan krusial pada integrasi patch SUSFS, serta optimalisasi mesin kompilasi Bazel guna menciptakan siklus integrasi berkelanjutan (CI/CD) yang andal dan cepat.

---

### 🗑️ Komponen Input yang Dihapus/Dikunci dari Workflow
Untuk mencegah kebingungan pengembang, menjaga keaslian identitas kernel, serta menjaga kerapian konfigurasi build, beberapa opsi masukan (inputs) yang bersifat dinamis atau tidak stabil telah dihapus/dikunci dari sistem dispatcher CI/CD:

| Nama Input | Status Akhir | Alasan Penguncian / Penghapusan |
| :--- | :--- | :--- |
| `custom_name` | **Dikunci Terhardcode** (`"Epitaph"`) | Dihapus dari UI input dan dikunci secara mutlak untuk menghindari pemalsuan atau pengubahan nama identitas kernel. |
| `author_name` | **Dikunci Terhardcode** (`"Naidrahiqa"`) | Dihapus dari UI input dan dikunci secara mutlak guna menjamin hak kekayaan intelektual (copyright) pengembang. |
| `tuning_profile` | Dihapus sepenuhnya | Profil performa kustom tidak diperlukan; manajemen penjadwalan CPU bawaan GKI (Schedutil) sudah sangat memadai. |
| `safety_profile` | Dihapus sepenuhnya | Pembatasan profil keamanan tidak relevan; konfigurasi bawaan kernel sudah dirancang aman secara default. |
| `root_kernelsu_next` | Dihapus sepenuhnya | Dihapus karena repositori ini kini secara penuh didedikasikan untuk menggunakan metode root **KernelSU-Next** demi stabilitas optimal. |
| `tc_azure_latest` | Dihapus sepenuhnya | Toolchain Azure Clang telah dihapus karena ketidakcocokan arsitektur pada Android 15. |

---

## ✅ Komponen Input yang Dipertahankan
Beberapa parameter konfigurasi penting tetap dipertahankan guna memberikan fleksibilitas saat memicu jalannya proses kompilasi manual:

| Nama Parameter | Nilai Default | Deskripsi Fungsional |
| :--- | :--- | :--- |
| `release_tag` | `v1.0` | Penanda versi rilis unik untuk arsip GitHub Release. |
| `build_no_susfs` | `true` (Aktif) | Kompilasi kernel murni tanpa modul pelindung SUSFS. |
| `build_susfs` | `false` (Nonaktif) | Kompilasi kernel lengkap dengan integrasi patch SUSFS. |
| `cpu_governors` | `schedutil` | Governor manajemen frekuensi prosesor (sangat disarankan tetap menggunakan Schedutil). |
| *Toolchain Checkboxes* | *Bazel (Kleaf)* | Pilihan compiler kernel utama (sangat disarankan menggunakan Bazel bawaan). |

---

## 🔧 Penyempurnaan Prosedur Pemasangan Patch SUSFS
Integrasi modul SUSFS sebelumnya sering kali mengalami kegagalan kompilasi akibat penanganan kesalahan yang tidak ketat (`|| true` masking) dan ketidakcocokan berkas patch dengan kode dasar kernel.

### Perbaikan yang Diterapkan:
1. **Pemeriksaan Wajib (Mandatory Application)**: Penerapan patch kini memprioritaskan validasi uji coba (`git apply --check`). Jika uji coba gagal, proses build akan **dihentikan secara instan** alih-alih melanjutkan build yang rusak.
2. **Koreksi Urutan Eksekusi**: Proses perbaikan kode dasar kernel (patching) wajib diselesaikan **terlebih dahulu** sebelum berkas driver SUSFS disalin ke direktori fs.
3. **Penyajian Pesan Error yang Informatif**: Jika terjadi kegagalan patch, konsol log akan menampilkan detail versi kernel riil, nama cabang, dan daftar patch yang tersedia sebagai panduan diagnosis.
4. **Pembersihan Masking Error**: Menghapus seluruh klausa pengabaian `|| true` dari operasi-operasi yang bersifat krusial untuk kestabilan kode.

---

## 🔧 Optimalisasi Mesin Kompilasi Bazel/Kleaf
Berikut adalah ringkasan perbaikan teknis yang diterapkan pada subsistem kompilasi Bazel demi mengatasi batasan runner GitHub Actions:

| Jenis Perbaikan | Detail Teknis & Alasan Implementasi |
| :--- | :--- |
| **Kembalikan Opsi `--local_resources`** | Bendera pembatas memori dikembalikan ke `--local_resources=memory=6144`. Penggunaan `--local_ram_resources` terbukti tidak kompatibel dan dianggap usang (deprecated) oleh versi Bazel yang digunakan Kleaf GKI 6.6. |
| **Pengurangan Loop Percobaan Build** | Batas percobaan kompilasi Bazel diturunkan menjadi **3 kali** dengan pengulangan dinamis. Kegagalan akibat jaringan saat mengunduh remote dependencies kini diatasi tanpa membuang waktu eksekusi runner secara berlebihan. |
| **Transisi ke Skrip Python Inline** | Menghapus dependensi eksternal `buildozer` yang rawan gagal saat pemasangan. Pendaftaran modul WiFi kustom ke berkas `BUILD.bazel` kini diproses secara tangguh menggunakan skrip **Python 3 inline** bawaan runner. |
| **Integrasi WiFi Bazel Absolut** | Menggunakan skrip Python 3 inline terintegrasi yang membedah berkas `modules.bzl` (mendukung tanda kutip tunggal/ganda) serta mengisolasi blok target `kernel_build` (`kernel_aarch64`) di dalam `BUILD.bazel` secara presisi. Skrip ini menjamin penyuntikan/penggabungan modul `cfg80211.ko` dan `mac80211.ko` ke dalam `module_outs` baik berupa list literal, ekspresi, atau belum ada sama sekali, sepenuhnya menuntaskan bug kompilasi nirkabel. |
| **Perbaikan Kbuild KernelSU-Next** | Menerapkan parser Python 3 inline untuk menulis ulang variabel `KSU_GIT_VERSION`, `KSU_VERSION`, dan `KSU_VERSION_TAG`/`KSU_GIT_TAG` di dalam berkas `Kbuild` secara langsung. Skrip ini kini dibungkus dengan `textwrap.dedent` untuk mencegah `IndentationError` akibat lekukan spasi pada YAML, menghindarkan versi KernelSU-Next turun ke nilai fallback `1` di lingkungan sandbox Bazel yang terisolasi. |
| **Pencatatan Riwayat Commit Kernel** | Hash identitas commit terakhir (`KERNEL_COMMIT`) kini secara otomatis direkam ke dalam `$GITHUB_ENV` tepat setelah proses sinkronisasi repositori selesai dilakukan. |

> [!WARNING]
> Kunci cache GitHub Actions (`Cache Key`) saat ini tidak menyertakan hash commit kernel secara dinamis karena keterbatasan pengenalan waktu saat inisialisasi workflow. Apabila Anda mencurigai adanya berkas cache yang usang (stale), lakukan pembersihan cache secara manual melalui panel antarmuka GitHub Actions UI.

---

## 📋 Berkas Alur Kerja Aktif
*   [build_manager_gki.yml](file:///d:/Project%20Coding/2026/4%20April/kernel%20redmi%2012/.github/workflows/build_manager_gki.yml): Berkas utama dispatcher matriks build.
*   [_build_kernel_core.yml](file:///d:/Project%20Coding/2026/4%20April/kernel%20redmi%2012/.github/workflows/_build_kernel_core.yml): Berkas resep inti dari seluruh proses penyiapan, modifikasi, kompilasi, pengemasan, hingga publikasi kernel.
