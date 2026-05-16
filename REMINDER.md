# ⏰ Reminder — Workflow Simplified (16 Mei 2026)

---

## 🗑️ Yang Dihapus

| Item | Alasan |
|------|--------|
| `tuning_profile` input | Gak perlu, HZ default GKI udah cukup |
| `safety_profile` input | Gak perlu, default safety udah OK |
| Checkbox `root_kernelsu_next` | Cuma 1 root method, gak perlu pilihan |
| Checkbox `tc_azure_latest` | Udah dihapus sebelumnya |

## ✅ Yang Tetap Ada

| Input | Default | Keterangan |
|-------|---------|------------|
| `release_tag` | v1.0 | Tag release GitHub |
| `custom_name` | Starter | Nama kernel |
| `author_name` | Castorice | Nama developer |
| `build_no_susfs` | true (checked) | Build tanpa SUSFS |
| `build_susfs` | false (unchecked) | Build dengan SUSFS |
| `cpu_governors` | schedutil | Governor CPU |
| Toolchain checkboxes | Bazel default | Pilihan toolchain |

## 🔧 SUSFS Fix

SUSFS sering error compile karena:
- Patch gagal apply tapi build lanjut (`|| true` masking failures)
- Kernel code gak ke-patch → fs/susfs.c reference symbols yang gak ada

**Fix yang diterapkan:**
1. Patch application sekarang **MANDATORY** — `git apply --check` dulu, kalau gagal → exit langsung
2. Urutan diperbaiki: patch kernel DULU, baru copy SUSFS files
3. Error message lebih jelas: kasih tau kernel version + branch + available patches
4. Hapus `|| true` dari critical operations
5. `--dry-run` sebelum `patch` buat cek apakah patch bisa apply

**Catatan:** Kalau SUSFS patch gak compatible sama kernel version yang lagi di-tip of branch, build akan FAIL dengan error jelas. Ini lebih baik daripada fail di tengah compile dengan error yang gak jelas.

## 📋 Release Tag Format

`{tag}-{toolchain}-{governor}-{susfs}`

Contoh: `v1.0-bazel-default-schedutil-false`

## 📋 Workflow Files

- `build_manager_gki.yml` — Dispatcher (171 lines, simplified)
- `_build_kernel_core.yml` — Core build (1240 lines)
