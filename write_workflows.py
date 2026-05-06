import textwrap

def w(path, content):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"Written: {path} ({len(content)} chars)")

# Shared steps as Python strings (no shell escaping issues)
SHARED_HEADER_GKI = """\
permissions:
  contents: write

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: "true"
  ANDROID_VERSION: android15
  KERNEL_VERSION: "6.6"
  KMI_GENERATION: "8"
  KERNEL_NAME: Castorice
  DEVICE_CODE: fire
  KSU_VERSION: ""
  ZIP_NAME: ""
"""

print("Script loaded OK")
