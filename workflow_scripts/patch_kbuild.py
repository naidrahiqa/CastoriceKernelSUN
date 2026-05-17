import sys
import os
import re

def main():
    if len(sys.argv) < 5:
        print("❌ Error: Missing arguments. Usage: python3 patch_kbuild.py <KBUILD_FILE> <GIT_COUNT> <KSU_VERSION> <KSU_TAG>")
        sys.exit(1)
        
    kbuild = sys.argv[1]
    git_count = sys.argv[2]
    ksu_version = sys.argv[3]
    ksu_tag = sys.argv[4]

    if not os.path.exists(kbuild):
        print(f"❌ Error: Kbuild file not found at '{kbuild}'")
        sys.exit(1)

    with open(kbuild, "r") as f:
        content = f.read()

    # Ganti pemanggilan shell git untuk git rev-list dengan nilai numerik statis hasil hitungan CI
    content = re.sub(r"KSU_GIT_VERSION\s*[:?]?=\s*\$\(shell[^\n]+\)", f"KSU_GIT_VERSION := {git_count}", content)
    content = re.sub(r"KSU_VERSION\s*[:?]?=\s*\$\(shell[^\n]+\)", f"KSU_VERSION := {ksu_version}", content)
    
    # Ganti pula pemanggilan shell git untuk pembacaan tag ksu
    content = re.sub(r"KSU_(VERSION_|GIT_)?TAG\s*[:?]?=\s*\$\(shell[^\n]+\)", f"KSU_VERSION_TAG := \"{ksu_tag}\"", content)
    content = re.sub(r"KSU_GIT_TAG\s*[:?]?=\s*\$\(shell[^\n]+\)", f"KSU_GIT_TAG := \"{ksu_tag}\"", content)

    # Hapus pesan peringatan (warnings) tentang repositori git non-standar agar log bersih
    content = re.sub(r"\$\(warning\s+KSU_GIT_VERSION\s+not\s+defined[^\n]+\)", "", content)
    content = re.sub(r"\$\(warning\s+KSU_VERSION_TAG\s+not\s+defined[^\n]+\)", "", content)

    with open(kbuild, "w") as f:
        f.write(content)
        
    print("✅ Berhasil memodifikasi versi dan tag di dalam berkas Kbuild secara absolut!")

if __name__ == "__main__":
    main()
