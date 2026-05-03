2026-05-03T01:16:23.7350641Z Current runner version: '2.334.0'
2026-05-03T01:16:23.7376787Z ##[group]Runner Image Provisioner
2026-05-03T01:16:23.7378150Z Hosted Compute Agent
2026-05-03T01:16:23.7378846Z Version: 20260213.493
2026-05-03T01:16:23.7379731Z Commit: 5c115507f6dd24b8de37d8bbe0bb4509d0cc0fa3
2026-05-03T01:16:23.7380471Z Build Date: 2026-02-13T00:28:41Z
2026-05-03T01:16:23.7381071Z Worker ID: {8954cc97-8798-4c99-909a-3dd7f6f7424e}
2026-05-03T01:16:23.7381875Z Azure Region: eastus
2026-05-03T01:16:23.7382401Z ##[endgroup]
2026-05-03T01:16:23.7384370Z ##[group]Operating System
2026-05-03T01:16:23.7385138Z Ubuntu
2026-05-03T01:16:23.7385628Z 24.04.4
2026-05-03T01:16:23.7386094Z LTS
2026-05-03T01:16:23.7386625Z ##[endgroup]
2026-05-03T01:16:23.7387144Z ##[group]Runner Image
2026-05-03T01:16:23.7387630Z Image: ubuntu-24.04
2026-05-03T01:16:23.7388757Z Version: 20260413.86.1
2026-05-03T01:16:23.7390171Z Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20260413.86/images/ubuntu/Ubuntu2404-Readme.md
2026-05-03T01:16:23.7391778Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20260413.86
2026-05-03T01:16:23.7392666Z ##[endgroup]
2026-05-03T01:16:23.7393729Z ##[group]GITHUB_TOKEN Permissions
2026-05-03T01:16:23.7395969Z Contents: write
2026-05-03T01:16:23.7396530Z Metadata: read
2026-05-03T01:16:23.7397097Z ##[endgroup]
2026-05-03T01:16:23.7399237Z Secret source: Actions
2026-05-03T01:16:23.7400521Z Prepare workflow directory
2026-05-03T01:16:23.7787933Z Prepare all required actions
2026-05-03T01:16:23.7824855Z Getting action download info
2026-05-03T01:16:24.1358174Z Download action repository 'actions/checkout@v4' (SHA:34e114876b0b11c390a56381ad16ebd13914f8d5)
2026-05-03T01:16:24.2573648Z Download action repository 'actions/upload-artifact@v4' (SHA:ea165f8d65b6e75b540449e92b4886f43607fa02)
2026-05-03T01:16:24.3705402Z Download action repository 'softprops/action-gh-release@v2' (SHA:3bb12739c298aeb8a4eeaf626c5b8d85266b0e65)
2026-05-03T01:16:24.6548499Z Complete job name: Castorice Legacy 4.19
2026-05-03T01:16:24.7361784Z ##[group]Run actions/checkout@v4
2026-05-03T01:16:24.7362646Z with:
2026-05-03T01:16:24.7363098Z   repository: naidrahiqa/CastoriceKernelSUN
2026-05-03T01:16:24.7363901Z   token: ***
2026-05-03T01:16:24.7364298Z   ssh-strict: true
2026-05-03T01:16:24.7364712Z   ssh-user: git
2026-05-03T01:16:24.7365119Z   persist-credentials: true
2026-05-03T01:16:24.7365602Z   clean: true
2026-05-03T01:16:24.7366027Z   sparse-checkout-cone-mode: true
2026-05-03T01:16:24.7366518Z   fetch-depth: 1
2026-05-03T01:16:24.7366960Z   fetch-tags: false
2026-05-03T01:16:24.7367383Z   show-progress: true
2026-05-03T01:16:24.7367796Z   lfs: false
2026-05-03T01:16:24.7368165Z   submodules: false
2026-05-03T01:16:24.7368581Z   set-safe-directory: true
2026-05-03T01:16:24.7369269Z env:
2026-05-03T01:16:24.7370007Z   KERNEL_NAME: Castorice
2026-05-03T01:16:24.7370478Z   DEVICE_CODE: fire
2026-05-03T01:16:24.7370927Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:16:24.7371466Z   CLANG_VERSION: 
2026-05-03T01:16:24.7371942Z   LLD_VERSION: 
2026-05-03T01:16:24.7372330Z   KERNEL_HEAD_HASH: 
2026-05-03T01:16:24.7372739Z   KSU_DIR: 
2026-05-03T01:16:24.7373099Z   KSU_VERSION: 
2026-05-03T01:16:24.7373482Z   KERNEL_VERSION: 
2026-05-03T01:16:24.7373881Z   ZIP_NAME: 
2026-05-03T01:16:24.7374299Z ##[endgroup]
2026-05-03T01:16:24.8499798Z Syncing repository: naidrahiqa/CastoriceKernelSUN
2026-05-03T01:16:24.8502111Z ##[group]Getting Git version info
2026-05-03T01:16:24.8502931Z Working directory is '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN'
2026-05-03T01:16:24.8504147Z [command]/usr/bin/git version
2026-05-03T01:16:24.8512551Z git version 2.53.0
2026-05-03T01:16:24.8532420Z ##[endgroup]
2026-05-03T01:16:24.8548287Z Temporarily overriding HOME='/home/runner/work/_temp/17e7fd99-b307-41cd-a033-0d2cff83e67a' before making global git config changes
2026-05-03T01:16:24.8551037Z Adding repository directory to the temporary git global config as a safe directory
2026-05-03T01:16:24.8555176Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN
2026-05-03T01:16:24.8592523Z Deleting the contents of '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN'
2026-05-03T01:16:24.8596637Z ##[group]Initializing the repository
2026-05-03T01:16:24.8601812Z [command]/usr/bin/git init /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN
2026-05-03T01:16:24.8661290Z hint: Using 'master' as the name for the initial branch. This default branch name
2026-05-03T01:16:24.8663097Z hint: will change to "main" in Git 3.0. To configure the initial branch name
2026-05-03T01:16:24.8664743Z hint: to use in all of your new repositories, which will suppress this warning,
2026-05-03T01:16:24.8666111Z hint: call:
2026-05-03T01:16:24.8666771Z hint:
2026-05-03T01:16:24.8667621Z hint: 	git config --global init.defaultBranch <name>
2026-05-03T01:16:24.8668676Z hint:
2026-05-03T01:16:24.8670087Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2026-05-03T01:16:24.8671742Z hint: 'development'. The just-created branch can be renamed via this command:
2026-05-03T01:16:24.8673045Z hint:
2026-05-03T01:16:24.8673753Z hint: 	git branch -m <name>
2026-05-03T01:16:24.8674548Z hint:
2026-05-03T01:16:24.8675588Z hint: Disable this message with "git config set advice.defaultBranchName false"
2026-05-03T01:16:24.8677527Z Initialized empty Git repository in /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/.git/
2026-05-03T01:16:24.8680925Z [command]/usr/bin/git remote add origin https://github.com/naidrahiqa/CastoriceKernelSUN
2026-05-03T01:16:24.8707897Z ##[endgroup]
2026-05-03T01:16:24.8709160Z ##[group]Disabling automatic garbage collection
2026-05-03T01:16:24.8712728Z [command]/usr/bin/git config --local gc.auto 0
2026-05-03T01:16:24.8743502Z ##[endgroup]
2026-05-03T01:16:24.8744641Z ##[group]Setting up auth
2026-05-03T01:16:24.8751315Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-05-03T01:16:24.8783209Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-05-03T01:16:24.9076103Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-05-03T01:16:24.9108748Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-05-03T01:16:24.9347945Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-05-03T01:16:24.9381175Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-05-03T01:16:24.9616723Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2026-05-03T01:16:24.9657690Z ##[endgroup]
2026-05-03T01:16:24.9659127Z ##[group]Fetching the repository
2026-05-03T01:16:24.9668972Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +f913d3f085437306c9a1e2ef5d906a94cccb0a7f:refs/remotes/origin/main
2026-05-03T01:16:25.1201320Z From https://github.com/naidrahiqa/CastoriceKernelSUN
2026-05-03T01:16:25.1203116Z  * [new ref]         f913d3f085437306c9a1e2ef5d906a94cccb0a7f -> origin/main
2026-05-03T01:16:25.1265463Z ##[endgroup]
2026-05-03T01:16:25.1266810Z ##[group]Determining the checkout info
2026-05-03T01:16:25.1268395Z ##[endgroup]
2026-05-03T01:16:25.1269603Z [command]/usr/bin/git sparse-checkout disable
2026-05-03T01:16:25.1284383Z [command]/usr/bin/git config --local --unset-all extensions.worktreeConfig
2026-05-03T01:16:25.1315887Z ##[group]Checking out the ref
2026-05-03T01:16:25.1319887Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
2026-05-03T01:16:25.1388509Z Switched to a new branch 'main'
2026-05-03T01:16:25.1390579Z branch 'main' set up to track 'origin/main'.
2026-05-03T01:16:25.1397221Z ##[endgroup]
2026-05-03T01:16:25.1445655Z [command]/usr/bin/git log -1 --format=%H
2026-05-03T01:16:25.1471402Z f913d3f085437306c9a1e2ef5d906a94cccb0a7f
2026-05-03T01:16:25.1687976Z ##[group]Run rm -f .gitmodules
2026-05-03T01:16:25.1688830Z [36;1mrm -f .gitmodules[0m
2026-05-03T01:16:25.1715100Z shell: /usr/bin/bash -e {0}
2026-05-03T01:16:25.1715794Z env:
2026-05-03T01:16:25.1716276Z   KERNEL_NAME: Castorice
2026-05-03T01:16:25.1716902Z   DEVICE_CODE: fire
2026-05-03T01:16:25.1717539Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:16:25.1718390Z   CLANG_VERSION: 
2026-05-03T01:16:25.1718908Z   LLD_VERSION: 
2026-05-03T01:16:25.1719586Z   KERNEL_HEAD_HASH: 
2026-05-03T01:16:25.1720125Z   KSU_DIR: 
2026-05-03T01:16:25.1720580Z   KSU_VERSION: 
2026-05-03T01:16:25.1721072Z   KERNEL_VERSION: 
2026-05-03T01:16:25.1721572Z   ZIP_NAME: 
2026-05-03T01:16:25.1722031Z ##[endgroup]
2026-05-03T01:16:25.1933716Z ##[group]Run echo "=== Before cleanup ==="
2026-05-03T01:16:25.1935080Z [36;1mecho "=== Before cleanup ==="[0m
2026-05-03T01:16:25.1936125Z [36;1mdf -h /[0m
2026-05-03T01:16:25.1937350Z [36;1msudo rm -rf /usr/share/dotnet /usr/local/lib/android /opt/ghc[0m
2026-05-03T01:16:25.1939890Z [36;1msudo rm -rf /usr/share/swift /usr/share/miniconda /opt/hostedtoolcache[0m
2026-05-03T01:16:25.1942279Z [36;1msudo rm -rf /usr/local/share/chromium /usr/local/share/powershell[0m
2026-05-03T01:16:25.1945925Z [36;1msudo apt-get remove -y '^dotnet-.*' '^llvm-.*' 'php.*' azure-cli google-cloud-cli google-chrome-stable firefox powershell mono-devel || true[0m
2026-05-03T01:16:25.1948148Z [36;1msudo apt-get autoremove -y[0m
2026-05-03T01:16:25.1948888Z [36;1msudo apt-get clean[0m
2026-05-03T01:16:25.1949791Z [36;1mecho "=== After cleanup ==="[0m
2026-05-03T01:16:25.1950507Z [36;1mdf -h /[0m
2026-05-03T01:16:25.1973167Z shell: /usr/bin/bash -e {0}
2026-05-03T01:16:25.1973792Z env:
2026-05-03T01:16:25.1974292Z   KERNEL_NAME: Castorice
2026-05-03T01:16:25.1974880Z   DEVICE_CODE: fire
2026-05-03T01:16:25.1975464Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:16:25.1976236Z   CLANG_VERSION: 
2026-05-03T01:16:25.1976715Z   LLD_VERSION: 
2026-05-03T01:16:25.1977186Z   KERNEL_HEAD_HASH: 
2026-05-03T01:16:25.1977690Z   KSU_DIR: 
2026-05-03T01:16:25.1978109Z   KSU_VERSION: 
2026-05-03T01:16:25.1978577Z   KERNEL_VERSION: 
2026-05-03T01:16:25.1979048Z   ZIP_NAME: 
2026-05-03T01:16:25.1979671Z ##[endgroup]
2026-05-03T01:16:25.2029977Z === Before cleanup ===
2026-05-03T01:16:25.2045259Z Filesystem      Size  Used Avail Use% Mounted on
2026-05-03T01:16:25.2046336Z /dev/root       145G   56G   90G  39% /
2026-05-03T01:17:48.3226635Z Reading package lists...
2026-05-03T01:17:48.5529328Z Building dependency tree...
2026-05-03T01:17:48.5580019Z Reading state information...
2026-05-03T01:17:48.9063883Z Package 'dotnet-hostfxr-6.0' is not installed, so not removed
2026-05-03T01:17:48.9064636Z Package 'dotnet-runtime-6.0' is not installed, so not removed
2026-05-03T01:17:48.9065253Z Package 'dotnet-sdk-6.0' is not installed, so not removed
2026-05-03T01:17:48.9066038Z Package 'dotnet-targeting-pack-6.0' is not installed, so not removed
2026-05-03T01:17:48.9066674Z Package 'dotnet-templates-6.0' is not installed, so not removed
2026-05-03T01:17:48.9067229Z Package 'llvm-21' is not installed, so not removed
2026-05-03T01:17:48.9067756Z Package 'php-lua' is not installed, so not removed
2026-05-03T01:17:48.9068295Z Package 'php-mysqlnd-ms' is not installed, so not removed
2026-05-03T01:17:48.9068846Z Package 'php-radius' is not installed, so not removed
2026-05-03T01:17:48.9069632Z Package 'php5.6-common' is not installed, so not removed
2026-05-03T01:17:48.9070207Z Package 'php5.6-json' is not installed, so not removed
2026-05-03T01:17:48.9070871Z Package 'php7.0-common' is not installed, so not removed
2026-05-03T01:17:48.9071464Z Package 'php7.1-common' is not installed, so not removed
2026-05-03T01:17:48.9072019Z Package 'php7.2-common' is not installed, so not removed
2026-05-03T01:17:48.9073096Z Package 'php7.3-common' is not installed, so not removed
2026-05-03T01:17:48.9073645Z Package 'php7.4-common' is not installed, so not removed
2026-05-03T01:17:48.9074203Z Package 'php8.0-common' is not installed, so not removed
2026-05-03T01:17:48.9074787Z Package 'php8.1-common' is not installed, so not removed
2026-05-03T01:17:48.9075337Z Package 'php8.2-common' is not installed, so not removed
2026-05-03T01:17:48.9075927Z Package 'php-pear-frontend-gtk' is not installed, so not removed
2026-05-03T01:17:48.9076579Z Package 'php-pear-frontend-web' is not installed, so not removed
2026-05-03T01:17:48.9077176Z Package 'php7.0-curl' is not installed, so not removed
2026-05-03T01:17:48.9077748Z Package 'php7.2-sodium' is not installed, so not removed
2026-05-03T01:17:48.9078282Z Package 'php5' is not installed, so not removed
2026-05-03T01:17:48.9078791Z Package 'php5-cli' is not installed, so not removed
2026-05-03T01:17:48.9079864Z Package 'php5-pgsql' is not installed, so not removed
2026-05-03T01:17:48.9080512Z Package 'php5-curl' is not installed, so not removed
2026-05-03T01:17:48.9081151Z Package 'php5-ldap' is not installed, so not removed
2026-05-03T01:17:48.9081729Z Package 'gosa-plugin-phpgw' is not installed, so not removed
2026-05-03T01:17:48.9082408Z Package 'gosa-plugin-phpgw-schema' is not installed, so not removed
2026-05-03T01:17:48.9083055Z Package 'gosa-plugin-phpscheduleit' is not installed, so not removed
2026-05-03T01:17:48.9083725Z Package 'gosa-plugin-phpscheduleit-schema' is not installed, so not removed
2026-05-03T01:17:48.9084312Z Package 'php-apc' is not installed, so not removed
2026-05-03T01:17:48.9084784Z Package 'php-suhosin' is not installed, so not removed
2026-05-03T01:17:48.9085269Z Package 'php5-mysql' is not installed, so not removed
2026-05-03T01:17:48.9085783Z Package 'libsparkline-php' is not installed, so not removed
2026-05-03T01:17:48.9086383Z Package 'libapache2-mod-php5' is not installed, so not removed
2026-05-03T01:17:48.9086931Z Package 'php5-fpm' is not installed, so not removed
2026-05-03T01:17:48.9087441Z Package 'libgv-php5' is not installed, so not removed
2026-05-03T01:17:48.9088174Z Package 'php-greew-oauth2-azure-provider' is not installed, so not removed
2026-05-03T01:17:48.9088921Z Package 'php-hayageek-oauth2-yahoo' is not installed, so not removed
2026-05-03T01:17:48.9089793Z Package 'php-league-oauth2-google' is not installed, so not removed
2026-05-03T01:17:48.9090457Z Package 'php-thenetworg-oauth2-azure' is not installed, so not removed
2026-05-03T01:17:48.9091014Z Package 'phpphylotree' is not installed, so not removed
2026-05-03T01:17:48.9091503Z Package 'php-http-request2' is not installed, so not removed
2026-05-03T01:17:48.9092022Z Package 'php-xcache' is not installed, so not removed
2026-05-03T01:17:48.9092510Z Package 'php-async-aws-s3' is not installed, so not removed
2026-05-03T01:17:48.9093081Z Package 'php-paragonie-random-compat' is not installed, so not removed
2026-05-03T01:17:48.9093665Z Package 'php-console-color2' is not installed, so not removed
2026-05-03T01:17:48.9094222Z Package 'php-doctrine-phpcr-odm' is not installed, so not removed
2026-05-03T01:17:48.9094839Z Package 'php-alcaeus-mongo-php-adapter' is not installed, so not removed
2026-05-03T01:17:48.9095455Z Package 'php-doctrine-mongodb-odm' is not installed, so not removed
2026-05-03T01:17:48.9096079Z Package 'php-mtdowling-cron-expression' is not installed, so not removed
2026-05-03T01:17:48.9096654Z Package 'php-semsol-arc2' is not installed, so not removed
2026-05-03T01:17:48.9097174Z Package 'php-fzaninotto-faker' is not installed, so not removed
2026-05-03T01:17:48.9097669Z Package 'php7.4' is not installed, so not removed
2026-05-03T01:17:48.9098103Z Package 'php7.4-cli' is not installed, so not removed
2026-05-03T01:17:48.9098581Z Package 'php-com-dotnet' is not installed, so not removed
2026-05-03T01:17:48.9099040Z Package 'php-rar' is not installed, so not removed
2026-05-03T01:17:48.9099793Z Package 'php-laminas-httphandlerrunner' is not installed, so not removed
2026-05-03T01:17:48.9100617Z Package 'php-cordoval-hamcrest-php' is not installed, so not removed
2026-05-03T01:17:48.9101265Z Package 'php-davedevelopment-hamcrest-php' is not installed, so not removed
2026-05-03T01:17:48.9101906Z Package 'php-kodova-hamcrest-php' is not installed, so not removed
2026-05-03T01:17:48.9102494Z Package 'php-league-flysystem-sftp' is not installed, so not removed
2026-05-03T01:17:48.9103186Z Package 'php-league-flysystem-eventable-filesystem' is not installed, so not removed
2026-05-03T01:17:48.9104002Z Package 'php-league-flysystem-rackspace' is not installed, so not removed
2026-05-03T01:17:48.9104671Z Package 'php-league-flysystem-azure' is not installed, so not removed
2026-05-03T01:17:48.9105299Z Package 'php-league-flysystem-webdav' is not installed, so not removed
2026-05-03T01:17:48.9105953Z Package 'php-league-flysystem-aws-s3-v2' is not installed, so not removed
2026-05-03T01:17:48.9106819Z Package 'php-league-flysystem-aws-s3-v3' is not installed, so not removed
2026-05-03T01:17:48.9107509Z Package 'php-spatie-flysystem-dropbox' is not installed, so not removed
2026-05-03T01:17:48.9108201Z Package 'php-srmklive-flysystem-dropbox-v2' is not installed, so not removed
2026-05-03T01:17:48.9108938Z Package 'php-league-flysystem-cached-adapter' is not installed, so not removed
2026-05-03T01:17:48.9109827Z Package 'php-league-flysystem-ziparchive' is not installed, so not removed
2026-05-03T01:17:48.9110486Z Package 'php-league-uri-schemes' is not installed, so not removed
2026-05-03T01:17:48.9111168Z Package 'php-jeremykendall-php-domain-parser' is not installed, so not removed
2026-05-03T01:17:48.9111808Z Package 'php-php-64bit' is not installed, so not removed
2026-05-03T01:17:48.9112327Z Package 'php-sqlite' is not installed, so not removed
2026-05-03T01:17:48.9112797Z Package 'php-lzf' is not installed, so not removed
2026-05-03T01:17:48.9113281Z Package 'php-pnctl' is not installed, so not removed
2026-05-03T01:17:48.9113839Z Package 'php-mdb2-driver-fbsql' is not installed, so not removed
2026-05-03T01:17:48.9114425Z Package 'php-mdb2-driver-ibase' is not installed, so not removed
2026-05-03T01:17:48.9114989Z Package 'php-mdb2-driver-mssql' is not installed, so not removed
2026-05-03T01:17:48.9115576Z Package 'php-mdb2-driver-mysqli' is not installed, so not removed
2026-05-03T01:17:48.9116159Z Package 'php-mdb2-driver-oci8' is not installed, so not removed
2026-05-03T01:17:48.9116725Z Package 'php-mdb2-driver-odbc' is not installed, so not removed
2026-05-03T01:17:48.9117321Z Package 'php-mdb2-driver-querysim' is not installed, so not removed
2026-05-03T01:17:48.9117923Z Package 'php-mdb2-driver-sqlite' is not installed, so not removed
2026-05-03T01:17:48.9118510Z Package 'php-mdb2-driver-sqlsrv' is not installed, so not removed
2026-05-03T01:17:48.9119149Z Package 'php-barnabywalters-mf-cleaner' is not installed, so not removed
2026-05-03T01:17:48.9119954Z Package 'php-graylog2-gelf-php' is not installed, so not removed
2026-05-03T01:17:48.9120538Z Package 'php-doctrine-couchdb' is not installed, so not removed
2026-05-03T01:17:48.9121106Z Package 'php-ruflin-elastica' is not installed, so not removed
2026-05-03T01:17:48.9121675Z Package 'php-elasticsearch' is not installed, so not removed
2026-05-03T01:17:48.9122218Z Package 'php-aws-sdk-php' is not installed, so not removed
2026-05-03T01:17:48.9122729Z Package 'php-rollbar' is not installed, so not removed
2026-05-03T01:17:48.9123246Z Package 'php-nette-finder' is not installed, so not removed
2026-05-03T01:17:48.9123755Z Package 'php-dbase' is not installed, so not removed
2026-05-03T01:17:48.9124246Z Package 'php-libsodium' is not installed, so not removed
2026-05-03T01:17:48.9124735Z Package 'php-relay' is not installed, so not removed
2026-05-03T01:17:48.9125306Z Package 'php-ocramius-proxy-manager' is not installed, so not removed
2026-05-03T01:17:48.9126018Z Package 'php-zendframework-zend-stdlib' is not installed, so not removed
2026-05-03T01:17:48.9126652Z Package 'php-rhumsaa-uuid' is not installed, so not removed
2026-05-03T01:17:48.9127430Z Package 'php-paragonie-random-lib' is not installed, so not removed
2026-05-03T01:17:48.9128064Z Package 'php-ramsey-uuid-doctrine' is not installed, so not removed
2026-05-03T01:17:48.9128653Z Package 'php-crypt-blowfish' is not installed, so not removed
2026-05-03T01:17:48.9129183Z Package 'php-compat' is not installed, so not removed
2026-05-03T01:17:48.9129818Z Package 'libssh2-php' is not installed, so not removed
2026-05-03T01:17:48.9130382Z Package 'php-php-http-discovery' is not installed, so not removed
2026-05-03T01:17:48.9131026Z Package 'php-symfony-security-guard' is not installed, so not removed
2026-05-03T01:17:48.9131631Z Package 'php-numbers-words' is not installed, so not removed
2026-05-03T01:17:48.9132182Z Package 'php7.0-thrift' is not installed, so not removed
2026-05-03T01:17:48.9132686Z Package 'php7.2-thrift' is not installed, so not removed
2026-05-03T01:17:48.9133360Z Package 'php-net-idna' is not installed, so not removed
2026-05-03T01:17:48.9133882Z Package 'php-phpstan' is not installed, so not removed
2026-05-03T01:17:48.9134421Z Package 'php-vimeo-psalm' is not installed, so not removed
2026-05-03T01:17:48.9134996Z Package 'php-container-interop' is not installed, so not removed
2026-05-03T01:17:48.9135671Z Package 'php-zendframework-zend-eventmanager' is not installed, so not removed
2026-05-03T01:17:48.9136315Z Package 'php-recode' is not installed, so not removed
2026-05-03T01:17:48.9136789Z Package 'php-gd2' is not installed, so not removed
2026-05-03T01:17:48.9137390Z Package 'php-pragmarx-google2fa-qrcode' is not installed, so not removed
2026-05-03T01:17:48.9138051Z Package 'php-bjeavons-zxcvbn-php' is not installed, so not removed
2026-05-03T01:17:48.9138663Z Package 'php-pimlie-php-dkim' is not installed, so not removed
2026-05-03T01:17:48.9139257Z Package 'libapache2-mod-php7.4' is not installed, so not removed
2026-05-03T01:17:48.9140043Z Package 'php7.4-fpm' is not installed, so not removed
2026-05-03T01:17:48.9140633Z Package 'dotnet-apphost-pack-6.0' is not installed, so not removed
2026-05-03T01:17:48.9141239Z Package 'dotnet-runtime-8.0' is not installed, so not removed
2026-05-03T01:17:48.9141839Z Package 'dotnet-apphost-pack-8.0' is not installed, so not removed
2026-05-03T01:17:48.9142422Z Package 'dotnet-host-8.0' is not installed, so not removed
2026-05-03T01:17:48.9142983Z Package 'dotnet-hostfxr-8.0' is not installed, so not removed
2026-05-03T01:17:48.9143542Z Package 'dotnet-sdk-8.0' is not installed, so not removed
2026-05-03T01:17:48.9144436Z Package 'dotnet-targeting-pack-8.0' is not installed, so not removed
2026-05-03T01:17:48.9145125Z Package 'dotnet-templates-8.0' is not installed, so not removed
2026-05-03T01:17:48.9145735Z Package 'dotnet-runtime-dbg-8.0' is not installed, so not removed
2026-05-03T01:17:48.9146438Z Package 'dotnet-sdk-8.0-source-built-artifacts' is not installed, so not removed
2026-05-03T01:17:48.9147119Z Package 'dotnet-sdk-dbg-8.0' is not installed, so not removed
2026-05-03T01:17:48.9147704Z Package 'dotnet-runtime-10.0' is not installed, so not removed
2026-05-03T01:17:48.9148311Z Package 'dotnet-apphost-pack-10.0' is not installed, so not removed
2026-05-03T01:17:48.9148896Z Package 'dotnet-host-10.0' is not installed, so not removed
2026-05-03T01:17:48.9149667Z Package 'dotnet-hostfxr-10.0' is not installed, so not removed
2026-05-03T01:17:48.9150269Z Package 'dotnet-runtime-dbg-10.0' is not installed, so not removed
2026-05-03T01:17:48.9150843Z Package 'dotnet-sdk-10.0' is not installed, so not removed
2026-05-03T01:17:48.9151441Z Package 'dotnet-targeting-pack-10.0' is not installed, so not removed
2026-05-03T01:17:48.9152077Z Package 'dotnet-templates-10.0' is not installed, so not removed
2026-05-03T01:17:48.9152663Z Package 'dotnet-sdk-aot-10.0' is not installed, so not removed
2026-05-03T01:17:48.9153231Z Package 'dotnet-sdk-dbg-10.0' is not installed, so not removed
2026-05-03T01:17:48.9153931Z Package 'dotnet-sdk-10.0-source-built-artifacts' is not installed, so not removed
2026-05-03T01:17:48.9154810Z Package 'llvm-14-linker-tools' is not installed, so not removed
2026-05-03T01:17:48.9155366Z Package 'llvm-14-dev' is not installed, so not removed
2026-05-03T01:17:48.9155907Z Package 'llvm-15-linker-tools' is not installed, so not removed
2026-05-03T01:17:48.9156454Z Package 'llvm-15-dev' is not installed, so not removed
2026-05-03T01:17:48.9156948Z Package 'llvm-15' is not installed, so not removed
2026-05-03T01:17:48.9157421Z Package 'llvm-dev' is not installed, so not removed
2026-05-03T01:17:48.9157909Z Package 'llvm-14-doc' is not installed, so not removed
2026-05-03T01:17:48.9158400Z Package 'llvm-15-doc' is not installed, so not removed
2026-05-03T01:17:48.9158893Z Package 'llvm-16-doc' is not installed, so not removed
2026-05-03T01:17:48.9159532Z Package 'llvm-17-doc' is not installed, so not removed
2026-05-03T01:17:48.9160033Z Package 'llvm-18-doc' is not installed, so not removed
2026-05-03T01:17:48.9160696Z Package 'llvm-runtime' is not installed, so not removed
2026-05-03T01:17:48.9161210Z Package 'llvm-14' is not installed, so not removed
2026-05-03T01:17:48.9161722Z Package 'llvm-14-runtime' is not installed, so not removed
2026-05-03T01:17:48.9162263Z Package 'llvm-14-tools' is not installed, so not removed
2026-05-03T01:17:48.9162811Z Package 'llvm-14-examples' is not installed, so not removed
2026-05-03T01:17:48.9163369Z Package 'llvm-15-runtime' is not installed, so not removed
2026-05-03T01:17:48.9163909Z Package 'llvm-15-tools' is not installed, so not removed
2026-05-03T01:17:48.9164451Z Package 'llvm-15-examples' is not installed, so not removed
2026-05-03T01:17:48.9165010Z Package 'llvm-16-examples' is not installed, so not removed
2026-05-03T01:17:48.9165565Z Package 'llvm-17-examples' is not installed, so not removed
2026-05-03T01:17:48.9166101Z Package 'llvm-18-examples' is not installed, so not removed
2026-05-03T01:17:48.9166635Z Package 'llvm-bolt' is not installed, so not removed
2026-05-03T01:17:48.9167149Z Package 'llvm-spirv-14' is not installed, so not removed
2026-05-03T01:17:48.9167686Z Package 'llvm-spirv-15' is not installed, so not removed
2026-05-03T01:17:48.9168205Z Package 'llvm-spirv-16' is not installed, so not removed
2026-05-03T01:17:48.9168724Z Package 'llvm-spirv-17' is not installed, so not removed
2026-05-03T01:17:48.9169241Z Package 'llvm-spirv-18' is not installed, so not removed
2026-05-03T01:17:48.9169949Z Package 'llvm-19-dev' is not installed, so not removed
2026-05-03T01:17:48.9170459Z Package 'llvm-20-dev' is not installed, so not removed
2026-05-03T01:17:48.9171031Z Package 'llvm-19-linker-tools' is not installed, so not removed
2026-05-03T01:17:48.9171644Z Package 'llvm-20-linker-tools' is not installed, so not removed
2026-05-03T01:17:48.9172169Z Package 'llvm-19-doc' is not installed, so not removed
2026-05-03T01:17:48.9172636Z Package 'llvm-20-doc' is not installed, so not removed
2026-05-03T01:17:48.9173089Z Package 'llvm-19' is not installed, so not removed
2026-05-03T01:17:48.9173569Z Package 'llvm-19-runtime' is not installed, so not removed
2026-05-03T01:17:48.9174072Z Package 'llvm-19-tools' is not installed, so not removed
2026-05-03T01:17:48.9174560Z Package 'llvm-19-examples' is not installed, so not removed
2026-05-03T01:17:48.9175031Z Package 'llvm-20' is not installed, so not removed
2026-05-03T01:17:48.9175495Z Package 'llvm-20-runtime' is not installed, so not removed
2026-05-03T01:17:48.9175988Z Package 'llvm-20-tools' is not installed, so not removed
2026-05-03T01:17:48.9176478Z Package 'llvm-20-examples' is not installed, so not removed
2026-05-03T01:17:48.9176973Z Package 'llvm-spirv-19' is not installed, so not removed
2026-05-03T01:17:48.9177453Z Package 'llvm-spirv-20' is not installed, so not removed
2026-05-03T01:17:48.9177935Z Package 'php-crypt-gpg' is not installed, so not removed
2026-05-03T01:17:48.9178455Z Package 'libapache2-mod-php' is not installed, so not removed
2026-05-03T01:17:48.9179049Z Package 'libapache2-mod-php8.3' is not installed, so not removed
2026-05-03T01:17:48.9179961Z Package 'php-json' is not installed, so not removed
2026-05-03T01:17:48.9180405Z Package 'php' is not installed, so not removed
2026-05-03T01:17:48.9180854Z Package 'php-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9181323Z Package 'php-cgi' is not installed, so not removed
2026-05-03T01:17:48.9181763Z Package 'php-cli' is not installed, so not removed
2026-05-03T01:17:48.9182199Z Package 'php-amqp' is not installed, so not removed
2026-05-03T01:17:48.9182645Z Package 'php-apcu' is not installed, so not removed
2026-05-03T01:17:48.9183083Z Package 'php-ast' is not installed, so not removed
2026-05-03T01:17:48.9183529Z Package 'php-ds' is not installed, so not removed
2026-05-03T01:17:48.9184011Z Package 'php-facedetect' is not installed, so not removed
2026-05-03T01:17:48.9184517Z Package 'php-gearman' is not installed, so not removed
2026-05-03T01:17:48.9184991Z Package 'php-gmagick' is not installed, so not removed
2026-05-03T01:17:48.9185666Z Package 'php-gnupg' is not installed, so not removed
2026-05-03T01:17:48.9186157Z Package 'php-igbinary' is not installed, so not removed
2026-05-03T01:17:48.9186632Z Package 'php-imagick' is not installed, so not removed
2026-05-03T01:17:48.9187138Z Package 'php-libvirt-php' is not installed, so not removed
2026-05-03T01:17:48.9187643Z Package 'php-mailparse' is not installed, so not removed
2026-05-03T01:17:48.9188136Z Package 'php-memcache' is not installed, so not removed
2026-05-03T01:17:48.9188616Z Package 'php-memcached' is not installed, so not removed
2026-05-03T01:17:48.9189101Z Package 'php-mongodb' is not installed, so not removed
2026-05-03T01:17:48.9189750Z Package 'php-msgpack' is not installed, so not removed
2026-05-03T01:17:48.9190205Z Package 'php-oauth' is not installed, so not removed
2026-05-03T01:17:48.9190669Z Package 'php-pcov' is not installed, so not removed
2026-05-03T01:17:48.9191124Z Package 'php-ps' is not installed, so not removed
2026-05-03T01:17:48.9191595Z Package 'php-psr' is not installed, so not removed
2026-05-03T01:17:48.9192051Z Package 'php-raphf' is not installed, so not removed
2026-05-03T01:17:48.9192513Z Package 'php-redis' is not installed, so not removed
2026-05-03T01:17:48.9192951Z Package 'php-rrd' is not installed, so not removed
2026-05-03T01:17:48.9193428Z Package 'php-smbclient' is not installed, so not removed
2026-05-03T01:17:48.9193901Z Package 'php-ssh2' is not installed, so not removed
2026-05-03T01:17:48.9194346Z Package 'php-stomp' is not installed, so not removed
2026-05-03T01:17:48.9194823Z Package 'php-tideways' is not installed, so not removed
2026-05-03T01:17:48.9195280Z Package 'php-uopz' is not installed, so not removed
2026-05-03T01:17:48.9195790Z Package 'php-uploadprogress' is not installed, so not removed
2026-05-03T01:17:48.9196283Z Package 'php-uuid' is not installed, so not removed
2026-05-03T01:17:48.9196742Z Package 'php-xdebug' is not installed, so not removed
2026-05-03T01:17:48.9197217Z Package 'php-xmlrpc' is not installed, so not removed
2026-05-03T01:17:48.9197669Z Package 'php-yac' is not installed, so not removed
2026-05-03T01:17:48.9198128Z Package 'php-yaml' is not installed, so not removed
2026-05-03T01:17:48.9198570Z Package 'php-zmq' is not installed, so not removed
2026-05-03T01:17:48.9199012Z Package 'php-curl' is not installed, so not removed
2026-05-03T01:17:48.9199586Z Package 'php-dev' is not installed, so not removed
2026-05-03T01:17:48.9200037Z Package 'php-gd' is not installed, so not removed
2026-05-03T01:17:48.9200469Z Package 'php-gmp' is not installed, so not removed
2026-05-03T01:17:48.9200911Z Package 'php-ldap' is not installed, so not removed
2026-05-03T01:17:48.9201364Z Package 'php-mysql' is not installed, so not removed
2026-05-03T01:17:48.9201808Z Package 'php-odbc' is not installed, so not removed
2026-05-03T01:17:48.9202246Z Package 'php-xml' is not installed, so not removed
2026-05-03T01:17:48.9202698Z Package 'php-pgsql' is not installed, so not removed
2026-05-03T01:17:48.9203180Z Package 'php-pspell' is not installed, so not removed
2026-05-03T01:17:48.9203819Z Package 'php-snmp' is not installed, so not removed
2026-05-03T01:17:48.9204286Z Package 'php-sqlite3' is not installed, so not removed
2026-05-03T01:17:48.9204740Z Package 'php-tidy' is not installed, so not removed
2026-05-03T01:17:48.9205215Z Package 'php-tokenizer' is not installed, so not removed
2026-05-03T01:17:48.9205738Z Package 'pkg-php-tools' is not installed, so not removed
2026-05-03T01:17:48.9206216Z Package 'dh-php' is not installed, so not removed
2026-05-03T01:17:48.9206691Z Package 'php-mbstring' is not installed, so not removed
2026-05-03T01:17:48.9207170Z Package 'php-readline' is not installed, so not removed
2026-05-03T01:17:48.9207634Z Package 'php-fpm' is not installed, so not removed
2026-05-03T01:17:48.9208123Z Package 'php-codesniffer' is not installed, so not removed
2026-05-03T01:17:48.9208673Z Package 'libphp-phpmailer' is not installed, so not removed
2026-05-03T01:17:48.9209617Z Package 'php-phpmyadmin-motranslator' is not installed, so not removed
2026-05-03T01:17:48.9210232Z Package 'php-phpseclib' is not installed, so not removed
2026-05-03T01:17:48.9210714Z Package 'php-twig' is not installed, so not removed
2026-05-03T01:17:48.9211208Z Package 'php-mapscript-ng' is not installed, so not removed
2026-05-03T01:17:48.9211777Z Package 'php-composer-ca-bundle' is not installed, so not removed
2026-05-03T01:17:48.9212434Z Package 'php-composer-class-map-generator' is not installed, so not removed
2026-05-03T01:17:48.9213143Z Package 'php-composer-metadata-minifier' is not installed, so not removed
2026-05-03T01:17:48.9213780Z Package 'php-composer-semver' is not installed, so not removed
2026-05-03T01:17:48.9214392Z Package 'php-composer-spdx-licenses' is not installed, so not removed
2026-05-03T01:17:48.9215044Z Package 'php-composer-xdebug-handler' is not installed, so not removed
2026-05-03T01:17:48.9215620Z Package 'php-json-schema' is not installed, so not removed
2026-05-03T01:17:48.9216136Z Package 'php-psr-log' is not installed, so not removed
2026-05-03T01:17:48.9216667Z Package 'php-symfony-console' is not installed, so not removed
2026-05-03T01:17:48.9217252Z Package 'php-symfony-filesystem' is not installed, so not removed
2026-05-03T01:17:48.9217828Z Package 'php-symfony-finder' is not installed, so not removed
2026-05-03T01:17:48.9218376Z Package 'php-symfony-process' is not installed, so not removed
2026-05-03T01:17:48.9218930Z Package 'php-react-promise' is not installed, so not removed
2026-05-03T01:17:48.9219623Z Package 'php-composer-pcre' is not installed, so not removed
2026-05-03T01:17:48.9220213Z Package 'php-seld-signal-handler' is not installed, so not removed
2026-05-03T01:17:48.9220747Z Package 'php-intl' is not installed, so not removed
2026-05-03T01:17:48.9221226Z Package 'php-zip' is not installed, so not removed
2026-05-03T01:17:48.9221697Z Package 'libawl-php' is not installed, so not removed
2026-05-03T01:17:48.9222220Z Package 'libphp-simplepie' is not installed, so not removed
2026-05-03T01:17:48.9222727Z Package 'php-geshi' is not installed, so not removed
2026-05-03T01:17:48.9223248Z Package 'php-random-compat' is not installed, so not removed
2026-05-03T01:17:48.9223780Z Package 'elpa-php-mode' is not installed, so not removed
2026-05-03T01:17:48.9224261Z Package 'phpunit' is not installed, so not removed
2026-05-03T01:17:48.9224721Z Package 'php-geos' is not installed, so not removed
2026-05-03T01:17:48.9225314Z Package 'golang-github-phpdave11-gofpdi-dev' is not installed, so not removed
2026-05-03T01:17:48.9225918Z Package 'php-imap' is not installed, so not removed
2026-05-03T01:17:48.9226369Z Package 'php-fpdf' is not installed, so not removed
2026-05-03T01:17:48.9226863Z Package 'icinga-php-library' is not installed, so not removed
2026-05-03T01:17:48.9227438Z Package 'icinga-php-thirdparty' is not installed, so not removed
2026-05-03T01:17:48.9227952Z Package 'php-soap' is not installed, so not removed
2026-05-03T01:17:48.9228428Z Package 'php-icinga' is not installed, so not removed
2026-05-03T01:17:48.9228896Z Package 'php-tcpdf' is not installed, so not removed
2026-05-03T01:17:48.9229696Z Package 'kdevelop-php' is not installed, so not removed
2026-05-03T01:17:48.9230216Z Package 'kdevelop-php-l10n' is not installed, so not removed
2026-05-03T01:17:48.9230725Z Package 'php-mcrypt' is not installed, so not removed
2026-05-03T01:17:48.9231186Z Package 'less.php' is not installed, so not removed
2026-05-03T01:17:48.9231729Z Package 'libphp-serialization-perl' is not installed, so not removed
2026-05-03T01:17:48.9232424Z Package 'libhtml-wikiconverter-phpwiki-perl' is not installed, so not removed
2026-05-03T01:17:48.9233109Z Package 'libjs-php-date-formatter' is not installed, so not removed
2026-05-03T01:17:48.9233693Z Package 'libmarkdown-php' is not installed, so not removed
2026-05-03T01:17:48.9234210Z Package 'libnusoap-php' is not installed, so not removed
2026-05-03T01:17:48.9234753Z Package 'php-econea-nusoap' is not installed, so not removed
2026-05-03T01:17:48.9235552Z Package 'libow-php7t64' is not installed, so not removed
2026-05-03T01:17:48.9236063Z Package 'libownet-php' is not installed, so not removed
2026-05-03T01:17:48.9236556Z Package 'libphp-adodb' is not installed, so not removed
2026-05-03T01:17:48.9237031Z Package 'php-sybase' is not installed, so not removed
2026-05-03T01:17:48.9237511Z Package 'libphp-embed' is not installed, so not removed
2026-05-03T01:17:48.9238009Z Package 'libphp8.3-embed' is not installed, so not removed
2026-05-03T01:17:48.9238527Z Package 'libphp-jabber' is not installed, so not removed
2026-05-03T01:17:48.9239032Z Package 'libphp-snoopy' is not installed, so not removed
2026-05-03T01:17:48.9239657Z Package 'libphpy-dev' is not installed, so not removed
2026-05-03T01:17:48.9240137Z Package 'libphpy1' is not installed, so not removed
2026-05-03T01:17:48.9240628Z Package 'libxrdcephposix0' is not installed, so not removed
2026-05-03T01:17:48.9241119Z Package 'php-spyc' is not installed, so not removed
2026-05-03T01:17:48.9241640Z Package 'matomo-php-tracker' is not installed, so not removed
2026-05-03T01:17:48.9242188Z Package 'php-wikidiff2' is not installed, so not removed
2026-05-03T01:17:48.9242700Z Package 'php-luasandbox' is not installed, so not removed
2026-05-03T01:17:48.9243215Z Package 'mlmmj-php-web' is not installed, so not removed
2026-05-03T01:17:48.9243747Z Package 'mlmmj-php-web-admin' is not installed, so not removed
2026-05-03T01:17:48.9244290Z Package 'php-net-socket' is not installed, so not removed
2026-05-03T01:17:48.9244867Z Package 'node-codemirror-lang-php' is not installed, so not removed
2026-05-03T01:17:48.9245501Z Package 'node-lezer-php' is not installed, so not removed
2026-05-03T01:17:48.9246002Z Package 'phpmyadmin' is not installed, so not removed
2026-05-03T01:17:48.9246471Z Package 'php-cas' is not installed, so not removed
2026-05-03T01:17:48.9246950Z Package 'php-pclzip' is not installed, so not removed
2026-05-03T01:17:48.9247431Z Package 'phpqrcode' is not installed, so not removed
2026-05-03T01:17:48.9247949Z Package 'php-symfony-config' is not installed, so not removed
2026-05-03T01:17:48.9248600Z Package 'php-symfony-dependency-injection' is not installed, so not removed
2026-05-03T01:17:48.9249189Z Package 'phpmd' is not installed, so not removed
2026-05-03T01:17:48.9249897Z Package 'php-algo26-idna-convert' is not installed, so not removed
2026-05-03T01:17:48.9250545Z Package 'php-jakeasmith-http-build-url' is not installed, so not removed
2026-05-03T01:17:48.9251157Z Package 'php-amphp-amp' is not installed, so not removed
2026-05-03T01:17:48.9251691Z Package 'php-amqp-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9252206Z Package 'php-amqplib' is not installed, so not removed
2026-05-03T01:17:48.9252719Z Package 'php-apcu-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9253340Z Package 'php-arthurhoaro-web-thumbnailer' is not installed, so not removed
2026-05-03T01:17:48.9253982Z Package 'php-text-template' is not installed, so not removed
2026-05-03T01:17:48.9254494Z Package 'php8.3-ast' is not installed, so not removed
2026-05-03T01:17:48.9255178Z Package 'php-ast-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9255730Z Package 'php-async-aws-core' is not installed, so not removed
2026-05-03T01:17:48.9256273Z Package 'php-psr-cache' is not installed, so not removed
2026-05-03T01:17:48.9256902Z Package 'php-symfony-deprecation-contracts' is not installed, so not removed
2026-05-03T01:17:48.9257583Z Package 'php-symfony-http-client' is not installed, so not removed
2026-05-03T01:17:48.9258261Z Package 'php-symfony-http-client-contracts' is not installed, so not removed
2026-05-03T01:17:48.9258959Z Package 'php-symfony-service-contracts' is not installed, so not removed
2026-05-03T01:17:48.9259759Z Package 'php-async-aws-ses' is not installed, so not removed
2026-05-03T01:17:48.9260311Z Package 'php-async-aws-sns' is not installed, so not removed
2026-05-03T01:17:48.9260841Z Package 'php-async-aws-sqs' is not installed, so not removed
2026-05-03T01:17:48.9261533Z Package 'php-auth-sasl' is not installed, so not removed
2026-05-03T01:17:48.9262073Z Package 'php-bacon-qr-code' is not installed, so not removed
2026-05-03T01:17:48.9262619Z Package 'php-dasprid-enum' is not installed, so not removed
2026-05-03T01:17:48.9263134Z Package 'php-bcmath' is not installed, so not removed
2026-05-03T01:17:48.9263647Z Package 'php-brick-math' is not installed, so not removed
2026-05-03T01:17:48.9264203Z Package 'php-brick-varexporter' is not installed, so not removed
2026-05-03T01:17:48.9264751Z Package 'php-parser' is not installed, so not removed
2026-05-03T01:17:48.9265220Z Package 'php-bz2' is not installed, so not removed
2026-05-03T01:17:48.9265783Z Package 'php-cache-integration-tests' is not installed, so not removed
2026-05-03T01:17:48.9266413Z Package 'php-cache-tag-interop' is not installed, so not removed
2026-05-03T01:17:48.9267058Z Package 'php-christianriesen-base32' is not installed, so not removed
2026-05-03T01:17:48.9267726Z Package 'php-christianriesen-otp' is not installed, so not removed
2026-05-03T01:17:48.9268374Z Package 'php-code-lts-u2f-php-server' is not installed, so not removed
2026-05-03T01:17:48.9268979Z Package 'php-codecoverage' is not installed, so not removed
2026-05-03T01:17:48.9269710Z Package 'php-file-iterator' is not installed, so not removed
2026-05-03T01:17:48.9270356Z Package 'phpunit-code-unit-reverse-lookup' is not installed, so not removed
2026-05-03T01:17:48.9271014Z Package 'phpunit-complexity' is not installed, so not removed
2026-05-03T01:17:48.9271570Z Package 'phpunit-environment' is not installed, so not removed
2026-05-03T01:17:48.9272167Z Package 'phpunit-lines-of-code' is not installed, so not removed
2026-05-03T01:17:48.9272763Z Package 'phpunit-version' is not installed, so not removed
2026-05-03T01:17:48.9273427Z Package 'php-codeigniter-framework' is not installed, so not removed
2026-05-03T01:17:48.9274192Z Package 'php-codeigniter-framework-doc' is not installed, so not removed
2026-05-03T01:17:48.9274976Z Package 'php-console-commandline' is not installed, so not removed
2026-05-03T01:17:48.9275668Z Package 'php-console-table' is not installed, so not removed
2026-05-03T01:17:48.9276298Z Package 'php-constant-time' is not installed, so not removed
2026-05-03T01:17:48.9276940Z Package 'php-dapphp-radius' is not installed, so not removed
2026-05-03T01:17:48.9277528Z Package 'php-date' is not installed, so not removed
2026-05-03T01:17:48.9278143Z Package 'php-datto-json-rpc' is not installed, so not removed
2026-05-03T01:17:48.9278854Z Package 'php-datto-json-rpc-http' is not installed, so not removed
2026-05-03T01:17:48.9279620Z Package 'php-db' is not installed, so not removed
2026-05-03T01:17:48.9280181Z Package 'php-deepcopy' is not installed, so not removed
2026-05-03T01:17:48.9280862Z Package 'php-dflydev-dot-access-data' is not installed, so not removed
2026-05-03T01:17:48.9281508Z Package 'php-di' is not installed, so not removed
2026-05-03T01:17:48.9282100Z Package 'php-psr-container' is not installed, so not removed
2026-05-03T01:17:48.9282723Z Package 'php-di-invoker' is not installed, so not removed
2026-05-03T01:17:48.9283660Z Package 'php-laravel-serializable-closure' is not installed, so not removed
2026-05-03T01:17:48.9284427Z Package 'php-directory-scanner' is not installed, so not removed
2026-05-03T01:17:48.9285045Z Package 'php-doc' is not installed, so not removed
2026-05-03T01:17:48.9285694Z Package 'php-doctrine-annotations' is not installed, so not removed
2026-05-03T01:17:48.9286396Z Package 'php-doctrine-lexer' is not installed, so not removed
2026-05-03T01:17:48.9287053Z Package 'php-doctrine-cache' is not installed, so not removed
2026-05-03T01:17:48.9287744Z Package 'php-doctrine-collections' is not installed, so not removed
2026-05-03T01:17:48.9288480Z Package 'php-doctrine-deprecations' is not installed, so not removed
2026-05-03T01:17:48.9289205Z Package 'php-doctrine-common' is not installed, so not removed
2026-05-03T01:17:48.9290230Z Package 'php-doctrine-persistence' is not installed, so not removed
2026-05-03T01:17:48.9290696Z Package 'php-doctrine-data-fixtures' is not installed, so not removed
2026-05-03T01:17:48.9291127Z Package 'php-doctrine-dbal' is not installed, so not removed
2026-05-03T01:17:48.9291506Z Package 'php-doctrine-orm' is not installed, so not removed
2026-05-03T01:17:48.9291918Z Package 'php-doctrine-event-manager' is not installed, so not removed
2026-05-03T01:17:48.9292347Z Package 'php-doctrine-inflector' is not installed, so not removed
2026-05-03T01:17:48.9292780Z Package 'php-doctrine-instantiator' is not installed, so not removed
2026-05-03T01:17:48.9293186Z Package 'php-symfony-cache' is not installed, so not removed
2026-05-03T01:17:48.9293550Z Package 'php-symfony-yaml' is not installed, so not removed
2026-05-03T01:17:48.9293995Z Package 'php-dragonmantank-cron-expression' is not installed, so not removed
2026-05-03T01:17:48.9294451Z Package 'php-webmozart-assert' is not installed, so not removed
2026-05-03T01:17:48.9294829Z Package 'php8.3-ds' is not installed, so not removed
2026-05-03T01:17:48.9295179Z Package 'php-ds-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9295544Z Package 'php-easyrdf' is not installed, so not removed
2026-05-03T01:17:48.9295894Z Package 'php-ml-json-ld' is not installed, so not removed
2026-05-03T01:17:48.9296250Z Package 'php-eluceo-ical' is not installed, so not removed
2026-05-03T01:17:48.9296637Z Package 'php-email-validator' is not installed, so not removed
2026-05-03T01:17:48.9296999Z Package 'php-embed' is not installed, so not removed
2026-05-03T01:17:48.9297393Z Package 'php-oscarotero-html-parser' is not installed, so not removed
2026-05-03T01:17:48.9297813Z Package 'php-psr-http-message' is not installed, so not removed
2026-05-03T01:17:48.9298206Z Package 'php-psr-http-client' is not installed, so not removed
2026-05-03T01:17:48.9298599Z Package 'php-psr-http-factory' is not installed, so not removed
2026-05-03T01:17:48.9299004Z Package 'php-symfony-css-selector' is not installed, so not removed
2026-05-03T01:17:48.9299549Z Package 'php-enchant' is not installed, so not removed
2026-05-03T01:17:48.9299897Z Package 'php-excimer' is not installed, so not removed
2026-05-03T01:17:48.9300258Z Package 'php8.3-facedetect' is not installed, so not removed
2026-05-03T01:17:48.9300655Z Package 'php-facedetect-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9301028Z Package 'php-faker' is not installed, so not removed
2026-05-03T01:17:48.9301380Z Package 'php-fdomdocument' is not installed, so not removed
2026-05-03T01:17:48.9301781Z Package 'php-fig-http-message-util' is not installed, so not removed
2026-05-03T01:17:48.9302185Z Package 'php-fig-link-util' is not installed, so not removed
2026-05-03T01:17:48.9302571Z Package 'php-psr-link' is not installed, so not removed
2026-05-03T01:17:48.9302924Z Package 'php-font-lib' is not installed, so not removed
2026-05-03T01:17:48.9303296Z Package 'php-fruitcake-php-cors' is not installed, so not removed
2026-05-03T01:17:48.9303740Z Package 'php-symfony-http-foundation' is not installed, so not removed
2026-05-03T01:17:48.9304263Z Package 'php-fxsl' is not installed, so not removed
2026-05-03T01:17:48.9304608Z Package 'php8.3-gearman' is not installed, so not removed
2026-05-03T01:17:48.9304988Z Package 'php-gearman-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9305369Z Package 'php-getallheaders' is not installed, so not removed
2026-05-03T01:17:48.9305731Z Package 'php-getid3' is not installed, so not removed
2026-05-03T01:17:48.9306102Z Package 'php-gettext-languages' is not installed, so not removed
2026-05-03T01:17:48.9306513Z Package 'php-oscarotero-gettext' is not installed, so not removed
2026-05-03T01:17:48.9306943Z Package 'php-giggsey-libphonenumber' is not installed, so not removed
2026-05-03T01:17:48.9307365Z Package 'php-giggsey-locale' is not installed, so not removed
2026-05-03T01:17:48.9307733Z Package 'php8.3-gmagick' is not installed, so not removed
2026-05-03T01:17:48.9308215Z Package 'php-gmagick-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9308601Z Package 'php8.3-gnupg' is not installed, so not removed
2026-05-03T01:17:48.9308976Z Package 'php-gnupg-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9309489Z Package 'php-google-protobuf' is not installed, so not removed
2026-05-03T01:17:48.9309899Z Package 'php-google-recaptcha' is not installed, so not removed
2026-05-03T01:17:48.9310350Z Package 'php-graham-campbell-result-type' is not installed, so not removed
2026-05-03T01:17:48.9310783Z Package 'php-phpoption' is not installed, so not removed
2026-05-03T01:17:48.9311156Z Package 'php-gregwar-captcha' is not installed, so not removed
2026-05-03T01:17:48.9311538Z Package 'php-guestfs' is not installed, so not removed
2026-05-03T01:17:48.9311913Z Package 'php-guzzlehttp-guzzle' is not installed, so not removed
2026-05-03T01:17:48.9312335Z Package 'php-guzzlehttp-promises' is not installed, so not removed
2026-05-03T01:17:48.9312740Z Package 'php-guzzlehttp-psr7' is not installed, so not removed
2026-05-03T01:17:48.9313115Z Package 'php-hamcrest' is not installed, so not removed
2026-05-03T01:17:48.9313497Z Package 'php-htmlawed' is not installed, so not removed
2026-05-03T01:17:48.9313852Z Package 'php-htmlpurifier' is not installed, so not removed
2026-05-03T01:17:48.9314207Z Package 'php-http' is not installed, so not removed
2026-05-03T01:17:48.9314541Z Package 'php8.3-http' is not installed, so not removed
2026-05-03T01:17:48.9314899Z Package 'php-http-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9315262Z Package 'php-http-httplug' is not installed, so not removed
2026-05-03T01:17:48.9315625Z Package 'php-http-promise' is not installed, so not removed
2026-05-03T01:17:48.9316069Z Package 'php-http-interop-http-factory-tests' is not installed, so not removed
2026-05-03T01:17:48.9316544Z Package 'php-http-message-factory' is not installed, so not removed
2026-05-03T01:17:48.9317006Z Package 'php-http-psr7-integration-tests' is not installed, so not removed
2026-05-03T01:17:48.9317456Z Package 'php-http-webdav-server' is not installed, so not removed
2026-05-03T01:17:48.9317840Z Package 'php-httpful' is not installed, so not removed
2026-05-03T01:17:48.9318208Z Package 'php-igbinary-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9318596Z Package 'php-image-text' is not installed, so not removed
2026-05-03T01:17:48.9318972Z Package 'php-imagick-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9319341Z Package 'php-interbase' is not installed, so not removed
2026-05-03T01:17:48.9319788Z Package 'php-invoker' is not installed, so not removed
2026-05-03T01:17:48.9320116Z Package 'php-jshrink' is not installed, so not removed
2026-05-03T01:17:48.9320483Z Package 'php-kissifrot-php-ixr' is not installed, so not removed
2026-05-03T01:17:48.9320851Z Package 'php-klogger' is not installed, so not removed
2026-05-03T01:17:48.9321210Z Package 'php-lcobucci-clock' is not installed, so not removed
2026-05-03T01:17:48.9321579Z Package 'php-psr-clock' is not installed, so not removed
2026-05-03T01:17:48.9321938Z Package 'php-lcobucci-jwt' is not installed, so not removed
2026-05-03T01:17:48.9322467Z Package 'php-league-commonmark' is not installed, so not removed
2026-05-03T01:17:48.9322865Z Package 'php-league-config' is not installed, so not removed
2026-05-03T01:17:48.9323269Z Package 'php-psr-event-dispatcher' is not installed, so not removed
2026-05-03T01:17:48.9323659Z Package 'php-nette-schema' is not installed, so not removed
2026-05-03T01:17:48.9324084Z Package 'php-league-csv' is not installed, so not removed
2026-05-03T01:17:48.9324455Z Package 'php-league-flysystem' is not installed, so not removed
2026-05-03T01:17:48.9324892Z Package 'php-league-mime-type-detection' is not installed, so not removed
2026-05-03T01:17:48.9325357Z Package 'php-league-html-to-markdown' is not installed, so not removed
2026-05-03T01:17:48.9325756Z Package 'php-league-uri' is not installed, so not removed
2026-05-03T01:17:48.9326267Z Package 'php-league-uri-interfaces' is not installed, so not removed
2026-05-03T01:17:48.9326702Z Package 'php-league-uri-components' is not installed, so not removed
2026-05-03T01:17:48.9327110Z Package 'php-letodms-core' is not installed, so not removed
2026-05-03T01:17:48.9327503Z Package 'php-libvirt-php-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9327878Z Package 'php-log' is not installed, so not removed
2026-05-03T01:17:48.9328207Z Package 'php-mdb2' is not installed, so not removed
2026-05-03T01:17:48.9328523Z Package 'php-mail' is not installed, so not removed
2026-05-03T01:17:48.9328868Z Package 'php-lorenzo-pinky' is not installed, so not removed
2026-05-03T01:17:48.9329229Z Package 'php-net-smtp' is not installed, so not removed
2026-05-03T01:17:48.9329686Z Package 'php-mail-mime' is not installed, so not removed
2026-05-03T01:17:48.9330039Z Package 'php8.3-mailparse' is not installed, so not removed
2026-05-03T01:17:48.9330423Z Package 'php-mailparse-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9330817Z Package 'php-malkusch-lock' is not installed, so not removed
2026-05-03T01:17:48.9331173Z Package 'php-predis' is not installed, so not removed
2026-05-03T01:17:48.9331538Z Package 'php-mariadb-mysql-kbs' is not installed, so not removed
2026-05-03T01:17:48.9331933Z Package 'php-masterminds-html5' is not installed, so not removed
2026-05-03T01:17:48.9332346Z Package 'php-matthiasmullie-minify' is not installed, so not removed
2026-05-03T01:17:48.9332811Z Package 'php-matthiasmullie-path-converter' is not installed, so not removed
2026-05-03T01:17:48.9333302Z Package 'php-maxmind-web-service-common' is not installed, so not removed
2026-05-03T01:17:48.9333713Z Package 'php-maxminddb' is not installed, so not removed
2026-05-03T01:17:48.9334061Z Package 'php8.3-maxminddb' is not installed, so not removed
2026-05-03T01:17:48.9334436Z Package 'php-maxminddb-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9334800Z Package 'php8.3-mcrypt' is not installed, so not removed
2026-05-03T01:17:48.9335172Z Package 'php-mcrypt-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9335556Z Package 'php-mdb2-driver-mysql' is not installed, so not removed
2026-05-03T01:17:48.9335945Z Package 'php-mdb2-driver-pgsql' is not installed, so not removed
2026-05-03T01:17:48.9336331Z Package 'php-memcache-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9336723Z Package 'php-memcached-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9337116Z Package 'php-msgpack-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9337461Z Package 'php-mf2' is not installed, so not removed
2026-05-03T01:17:48.9337825Z Package 'php-mikey179-vfsstream' is not installed, so not removed
2026-05-03T01:17:48.9338189Z Package 'php-ml-iri' is not installed, so not removed
2026-05-03T01:17:48.9338513Z Package 'php-mock' is not installed, so not removed
2026-05-03T01:17:48.9338867Z Package 'php-mock-phpunit' is not installed, so not removed
2026-05-03T01:17:48.9339267Z Package 'php-mock-integration' is not installed, so not removed
2026-05-03T01:17:48.9340005Z Package 'php-mockery' is not installed, so not removed
2026-05-03T01:17:48.9340523Z Package 'php-mockery-doc' is not installed, so not removed
2026-05-03T01:17:48.9340910Z Package 'php-mongodb-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9341272Z Package 'php-monolog' is not installed, so not removed
2026-05-03T01:17:48.9341619Z Package 'php-net-dime' is not installed, so not removed
2026-05-03T01:17:48.9341957Z Package 'php-net-dns2' is not installed, so not removed
2026-05-03T01:17:48.9342292Z Package 'php-net-ftp' is not installed, so not removed
2026-05-03T01:17:48.9342630Z Package 'php-net-imap' is not installed, so not removed
2026-05-03T01:17:48.9342959Z Package 'php-net-ipv6' is not installed, so not removed
2026-05-03T01:17:48.9343307Z Package 'php-net-ldap2' is not installed, so not removed
2026-05-03T01:17:48.9343655Z Package 'php-net-ldap3' is not installed, so not removed
2026-05-03T01:17:48.9344119Z Package 'php-net-nntp' is not installed, so not removed
2026-05-03T01:17:48.9344497Z Package 'php-net-publicsuffix' is not installed, so not removed
2026-05-03T01:17:48.9344890Z Package 'php-net-sieve' is not installed, so not removed
2026-05-03T01:17:48.9345271Z Package 'php-net-url' is not installed, so not removed
2026-05-03T01:17:48.9345620Z Package 'php-net-url2' is not installed, so not removed
2026-05-03T01:17:48.9345966Z Package 'php-net-whois' is not installed, so not removed
2026-05-03T01:17:48.9346374Z Package 'php-netscape-bookmark-parser' is not installed, so not removed
2026-05-03T01:17:48.9346802Z Package 'php-nette-utils' is not installed, so not removed
2026-05-03T01:17:48.9347185Z Package 'php-nikic-fast-route' is not installed, so not removed
2026-05-03T01:17:48.9347565Z Package 'php-nyholm-psr7' is not installed, so not removed
2026-05-03T01:17:48.9347911Z Package 'php8.3-oauth' is not installed, so not removed
2026-05-03T01:17:48.9348273Z Package 'php-oauth-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9348663Z Package 'php-opis-closure' is not installed, so not removed
2026-05-03T01:17:48.9349040Z Package 'php-parsedown' is not installed, so not removed
2026-05-03T01:17:48.9349549Z Package 'php-parsedown-extra' is not installed, so not removed
2026-05-03T01:17:48.9349943Z Package 'php-pcov-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9350346Z Package 'php-pda-pheanstalk' is not installed, so not removed
2026-05-03T01:17:48.9350997Z Package 'php-phar-io-manifest' is not installed, so not removed
2026-05-03T01:17:48.9351423Z Package 'php-phar-io-version' is not installed, so not removed
2026-05-03T01:17:48.9351811Z Package 'php-php-gettext' is not installed, so not removed
2026-05-03T01:17:48.9352172Z Package 'php-phpdbg' is not installed, so not removed
2026-05-03T01:17:48.9352617Z Package 'php-phpdocumentor-reflection-common' is not installed, so not removed
2026-05-03T01:17:48.9353151Z Package 'php-phpdocumentor-reflection-docblock' is not installed, so not removed
2026-05-03T01:17:48.9353678Z Package 'php-phpdocumentor-type-resolver' is not installed, so not removed
2026-05-03T01:17:48.9354160Z Package 'php-phpstan-phpdoc-parser' is not installed, so not removed
2026-05-03T01:17:48.9354625Z Package 'php-symfony-expression-language' is not installed, so not removed
2026-05-03T01:17:48.9355084Z Package 'php-phpmyadmin-shapefile' is not installed, so not removed
2026-05-03T01:17:48.9355525Z Package 'php-phpmyadmin-sql-parser' is not installed, so not removed
2026-05-03T01:17:48.9355976Z Package 'php-symfony-polyfill-php80' is not installed, so not removed
2026-05-03T01:17:48.9356369Z Package 'php-seclib' is not installed, so not removed
2026-05-03T01:17:48.9356727Z Package 'php-phpseclib3' is not installed, so not removed
2026-05-03T01:17:48.9357111Z Package 'php-phpspec-prophecy' is not installed, so not removed
2026-05-03T01:17:48.9357525Z Package 'phpunit-comparator' is not installed, so not removed
2026-05-03T01:17:48.9357940Z Package 'phpunit-recursion-context' is not installed, so not removed
2026-05-03T01:17:48.9358399Z Package 'php-phpspec-prophecy-phpunit' is not installed, so not removed
2026-05-03T01:17:48.9358994Z Package 'php-pinba' is not installed, so not removed
2026-05-03T01:17:48.9359340Z Package 'php8.3-pinba' is not installed, so not removed
2026-05-03T01:17:48.9359843Z Package 'php-pinba-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9360219Z Package 'php-proxy-manager' is not installed, so not removed
2026-05-03T01:17:48.9360571Z Package 'php8.3-ps' is not installed, so not removed
2026-05-03T01:17:48.9360915Z Package 'php-ps-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9361267Z Package 'php8.3-psr' is not installed, so not removed
2026-05-03T01:17:48.9361621Z Package 'php-psr-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9362009Z Package 'php-psr-simple-cache' is not installed, so not removed
2026-05-03T01:17:48.9362440Z Package 'php-pubsubhubbub-publisher' is not installed, so not removed
2026-05-03T01:17:48.9363003Z Package 'php-ramsey-collection' is not installed, so not removed
2026-05-03T01:17:48.9363400Z Package 'php-ramsey-uuid' is not installed, so not removed
2026-05-03T01:17:48.9363750Z Package 'php8.3-raphf' is not installed, so not removed
2026-05-03T01:17:48.9364106Z Package 'php-raphf-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9364477Z Package 'php-redis-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9364822Z Package 'php-remctl' is not installed, so not removed
2026-05-03T01:17:48.9365212Z Package 'php-roundcube-rtf-html-php' is not installed, so not removed
2026-05-03T01:17:48.9365600Z Package 'php8.3-rrd' is not installed, so not removed
2026-05-03T01:17:48.9365942Z Package 'php-rrd-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9366296Z Package 'php-sabre-dav' is not installed, so not removed
2026-05-03T01:17:48.9366657Z Package 'php-sabre-vobject' is not installed, so not removed
2026-05-03T01:17:48.9367006Z Package 'php-sass' is not installed, so not removed
2026-05-03T01:17:48.9367343Z Package 'php8.3-sass' is not installed, so not removed
2026-05-03T01:17:48.9367701Z Package 'php-sass-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9368068Z Package 'php-shellcommand' is not installed, so not removed
2026-05-03T01:17:48.9368423Z Package 'php-slim-psr7' is not installed, so not removed
2026-05-03T01:17:48.9368773Z Package 'php8.3-smbclient' is not installed, so not removed
2026-05-03T01:17:48.9369161Z Package 'php-smbclient-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9369644Z Package 'php-solr' is not installed, so not removed
2026-05-03T01:17:48.9369982Z Package 'php8.3-solr' is not installed, so not removed
2026-05-03T01:17:48.9370344Z Package 'php-solr-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9370715Z Package 'php-sparkline' is not installed, so not removed
2026-05-03T01:17:48.9371085Z Package 'php-sql-formatter' is not installed, so not removed
2026-05-03T01:17:48.9371443Z Package 'php8.3-ssh2' is not installed, so not removed
2026-05-03T01:17:48.9371794Z Package 'php-ssh2-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9372155Z Package 'php8.3-stomp' is not installed, so not removed
2026-05-03T01:17:48.9372515Z Package 'php-stomp-all-dev' is not installed, so not removed
2026-05-03T01:17:48.9372889Z Package 'php-swiftmailer' is not installed, so not removed
2026-05-03T01:17:48.9373235Z Package 'php-symfony' is not installed, so not removed
2026-05-03T01:17:48.9373586Z Package 'php-symfony-asset' is not installed, so not removed
2026-05-03T01:17:48.9373982Z Package 'php-symfony-asset-mapper' is not installed, so not removed
2026-05-03T01:17:48.9374412Z Package 'php-symfony-browser-kit' is not installed, so not removed
2026-05-03T01:17:48.9374806Z Package 'php-symfony-clock' is not installed, so not removed
2026-05-03T01:17:48.9375198Z Package 'php-symfony-debug-bundle' is not installed, so not removed
2026-05-03T01:17:48.9375636Z Package 'php-symfony-doctrine-bridge' is not installed, so not removed
2026-05-03T01:17:48.9376069Z Package 'php-symfony-dom-crawler' is not installed, so not removed
2026-05-03T01:17:48.9376606Z Package 'php-symfony-dotenv' is not installed, so not removed
2026-05-03T01:17:48.9377015Z Package 'php-symfony-error-handler' is not installed, so not removed
2026-05-03T01:17:48.9377463Z Package 'php-symfony-event-dispatcher' is not installed, so not removed
2026-05-03T01:17:48.9377879Z Package 'php-symfony-form' is not installed, so not removed
2026-05-03T01:17:48.9378291Z Package 'php-symfony-framework-bundle' is not installed, so not removed
2026-05-03T01:17:48.9378724Z Package 'php-symfony-http-kernel' is not installed, so not removed
2026-05-03T01:17:48.9379111Z Package 'php-symfony-intl' is not installed, so not removed
2026-05-03T01:17:48.9379613Z Package 'php-symfony-ldap' is not installed, so not removed
2026-05-03T01:17:48.9379972Z Package 'php-symfony-lock' is not installed, so not removed
2026-05-03T01:17:48.9380344Z Package 'php-symfony-mailer' is not installed, so not removed
2026-05-03T01:17:48.9380864Z Package 'php-symfony-messenger' is not installed, so not removed
2026-05-03T01:17:48.9381255Z Package 'php-symfony-mime' is not installed, so not removed
2026-05-03T01:17:48.9381659Z Package 'php-symfony-monolog-bridge' is not installed, so not removed
2026-05-03T01:17:48.9382076Z Package 'php-symfony-notifier' is not installed, so not removed
2026-05-03T01:17:48.9382506Z Package 'php-symfony-options-resolver' is not installed, so not removed
2026-05-03T01:17:48.9382964Z Package 'php-symfony-password-hasher' is not installed, so not removed
2026-05-03T01:17:48.9383413Z Package 'php-symfony-property-access' is not installed, so not removed
2026-05-03T01:17:48.9383849Z Package 'php-symfony-property-info' is not installed, so not removed
2026-05-03T01:17:48.9384317Z Package 'php-symfony-proxy-manager-bridge' is not installed, so not removed
2026-05-03T01:17:48.9384777Z Package 'php-symfony-rate-limiter' is not installed, so not removed
2026-05-03T01:17:48.9385197Z Package 'php-symfony-remote-event' is not installed, so not removed
2026-05-03T01:17:48.9385607Z Package 'php-symfony-routing' is not installed, so not removed
2026-05-03T01:17:48.9385998Z Package 'php-symfony-scheduler' is not installed, so not removed
2026-05-03T01:17:48.9386419Z Package 'php-symfony-security-bundle' is not installed, so not removed
2026-05-03T01:17:48.9386843Z Package 'php-symfony-security-core' is not installed, so not removed
2026-05-03T01:17:48.9387264Z Package 'php-symfony-security-csrf' is not installed, so not removed
2026-05-03T01:17:48.9387687Z Package 'php-symfony-security-http' is not installed, so not removed
2026-05-03T01:17:48.9388087Z Package 'php-symfony-semaphore' is not installed, so not removed
2026-05-03T01:17:48.9388490Z Package 'php-symfony-serializer' is not installed, so not removed
2026-05-03T01:17:48.9388884Z Package 'php-symfony-stopwatch' is not installed, so not removed
2026-05-03T01:17:48.9389271Z Package 'php-symfony-string' is not installed, so not removed
2026-05-03T01:17:48.9389816Z Package 'php-symfony-templating' is not installed, so not removed
2026-05-03T01:17:48.9390233Z Package 'php-symfony-translation' is not installed, so not removed
2026-05-03T01:17:48.9390644Z Package 'php-symfony-twig-bridge' is not installed, so not removed
2026-05-03T01:17:48.9391047Z Package 'php-symfony-twig-bundle' is not installed, so not removed
2026-05-03T01:17:48.9391446Z Package 'php-symfony-uid' is not installed, so not removed
2026-05-03T01:17:48.9391828Z Package 'php-symfony-validator' is not installed, so not removed
2026-05-03T01:17:48.9392226Z Package 'php-symfony-var-dumper' is not installed, so not removed
2026-05-03T01:17:48.9392633Z Package 'php-symfony-var-exporter' is not installed, so not removed
2026-05-03T01:17:48.9393042Z Package 'php-symfony-web-link' is not installed, so not removed
2026-05-03T01:17:48.9393488Z Package 'php-symfony-web-profiler-bundle' is not installed, so not removed
2026-05-03T01:17:48.9393925Z Package 'php-symfony-webhook' is not installed, so not removed
2026-05-03T01:17:48.9394317Z Package 'php-symfony-workflow' is not installed, so not removed
2026-05-03T01:17:48.9394908Z Package 'php-symfony-contracts' is not installed, so not removed
2026-05-03T01:17:48.9395331Z Package 'php-symfony-polyfill-php83' is not installed, so not removed
2026-05-03T01:17:48.9395784Z Package 'php-symfony-all-my-sms-notifier' is not installed, so not removed
2026-05-03T01:17:48.9396235Z Package 'php-symfony-amazon-mailer' is not installed, so not removed
2026-05-03T01:17:48.9396684Z Package 'php-symfony-amazon-sns-notifier' is not installed, so not removed
2026-05-03T01:17:48.9397154Z Package 'php-symfony-amazon-sqs-messenger' is not installed, so not removed
2026-05-03T01:17:48.9397613Z Package 'php-symfony-amqp-messenger' is not installed, so not removed
2026-05-03T01:17:48.9398066Z Package 'php-symfony-bandwidth-notifier' is not installed, so not removed
2026-05-03T01:17:48.9398547Z Package 'php-symfony-beanstalkd-messenger' is not installed, so not removed
2026-05-03T01:17:48.9399147Z Package 'php-symfony-brevo-mailer' is not installed, so not removed
2026-05-03T01:17:48.9399712Z Package 'php-symfony-brevo-notifier' is not installed, so not removed
2026-05-03T01:17:48.9400149Z Package 'php-symfony-cache-contracts' is not installed, so not removed
2026-05-03T01:17:48.9400598Z Package 'php-symfony-chatwork-notifier' is not installed, so not removed
2026-05-03T01:17:48.9401065Z Package 'php-symfony-click-send-notifier' is not installed, so not removed
2026-05-03T01:17:48.9401531Z Package 'php-symfony-clickatell-notifier' is not installed, so not removed
2026-05-03T01:17:48.9402031Z Package 'php-symfony-contact-everyone-notifier' is not installed, so not removed
2026-05-03T01:17:48.9402568Z Package 'php-symfony-event-dispatcher-contracts' is not installed, so not removed
2026-05-03T01:17:48.9403086Z Package 'php-symfony-translation-contracts' is not installed, so not removed
2026-05-03T01:17:48.9403619Z Package 'php-symfony-crowdin-translation-provider' is not installed, so not removed
2026-05-03T01:17:48.9404133Z Package 'php-symfony-discord-notifier' is not installed, so not removed
2026-05-03T01:17:48.9425224Z Package 'php-symfony-doctrine-messenger' is not installed, so not removed
2026-05-03T01:17:48.9425958Z Package 'php-symfony-engagespot-notifier' is not installed, so not removed
2026-05-03T01:17:48.9426479Z Package 'php-symfony-esendex-notifier' is not installed, so not removed
2026-05-03T01:17:48.9426932Z Package 'php-symfony-expo-notifier' is not installed, so not removed
2026-05-03T01:17:48.9427393Z Package 'php-symfony-fake-chat-notifier' is not installed, so not removed
2026-05-03T01:17:48.9427859Z Package 'php-symfony-fake-sms-notifier' is not installed, so not removed
2026-05-03T01:17:48.9428310Z Package 'php-symfony-firebase-notifier' is not installed, so not removed
2026-05-03T01:17:48.9428800Z Package 'php-symfony-forty-six-elks-notifier' is not installed, so not removed
2026-05-03T01:17:48.9429295Z Package 'php-symfony-free-mobile-notifier' is not installed, so not removed
2026-05-03T01:17:48.9429925Z Package 'php-symfony-gateway-api-notifier' is not installed, so not removed
2026-05-03T01:17:48.9430393Z Package 'php-symfony-gitter-notifier' is not installed, so not removed
2026-05-03T01:17:48.9430841Z Package 'php-symfony-go-ip-notifier' is not installed, so not removed
2026-05-03T01:17:48.9431298Z Package 'php-symfony-google-chat-notifier' is not installed, so not removed
2026-05-03T01:17:48.9431761Z Package 'php-symfony-google-mailer' is not installed, so not removed
2026-05-03T01:17:48.9432193Z Package 'php-symfony-html-sanitizer' is not installed, so not removed
2026-05-03T01:17:48.9432619Z Package 'php-symfony-infobip-mailer' is not installed, so not removed
2026-05-03T01:17:48.9433061Z Package 'php-symfony-infobip-notifier' is not installed, so not removed
2026-05-03T01:17:48.9433494Z Package 'php-symfony-iqsms-notifier' is not installed, so not removed
2026-05-03T01:17:48.9433930Z Package 'php-symfony-isendpro-notifier' is not installed, so not removed
2026-05-03T01:17:48.9434408Z Package 'php-symfony-kaz-info-teh-notifier' is not installed, so not removed
2026-05-03T01:17:48.9435168Z Package 'php-symfony-light-sms-notifier' is not installed, so not removed
2026-05-03T01:17:48.9435642Z Package 'php-symfony-line-notify-notifier' is not installed, so not removed
2026-05-03T01:17:48.9436107Z Package 'php-symfony-linked-in-notifier' is not installed, so not removed
2026-05-03T01:17:48.9436614Z Package 'php-symfony-loco-translation-provider' is not installed, so not removed
2026-05-03T01:17:48.9437171Z Package 'php-symfony-lokalise-translation-provider' is not installed, so not removed
2026-05-03T01:17:48.9437689Z Package 'php-symfony-mail-pace-mailer' is not installed, so not removed
2026-05-03T01:17:48.9438148Z Package 'php-symfony-mailchimp-mailer' is not installed, so not removed
2026-05-03T01:17:48.9438596Z Package 'php-symfony-mailer-send-mailer' is not installed, so not removed
2026-05-03T01:17:48.9439050Z Package 'php-symfony-mailgun-mailer' is not installed, so not removed
2026-05-03T01:17:48.9439713Z Package 'php-symfony-mailjet-mailer' is not installed, so not removed
2026-05-03T01:17:48.9440162Z Package 'php-symfony-mailjet-notifier' is not installed, so not removed
2026-05-03T01:17:48.9440614Z Package 'php-symfony-mastodon-notifier' is not installed, so not removed
2026-05-03T01:17:48.9441087Z Package 'php-symfony-mattermost-notifier' is not installed, so not removed
2026-05-03T01:17:48.9441531Z Package 'php-symfony-mercure' is not installed, so not removed
2026-05-03T01:17:48.9441959Z Package 'php-symfony-mercure-bundle' is not installed, so not removed
2026-05-03T01:17:48.9442406Z Package 'php-symfony-mercure-notifier' is not installed, so not removed
2026-05-03T01:17:48.9442885Z Package 'php-symfony-message-bird-notifier' is not installed, so not removed
2026-05-03T01:17:48.9443386Z Package 'php-symfony-message-media-notifier' is not installed, so not removed
2026-05-03T01:17:48.9443899Z Package 'php-symfony-microsoft-teams-notifier' is not installed, so not removed
2026-05-03T01:17:48.9444382Z Package 'php-symfony-mobyt-notifier' is not installed, so not removed
2026-05-03T01:17:48.9444812Z Package 'php-symfony-novu-notifier' is not installed, so not removed
2026-05-03T01:17:48.9445277Z Package 'php-symfony-ntfy-notifier' is not installed, so not removed
2026-05-03T01:17:48.9445715Z Package 'php-symfony-octopush-notifier' is not installed, so not removed
2026-05-03T01:17:48.9446172Z Package 'php-symfony-oh-my-smtp-mailer' is not installed, so not removed
2026-05-03T01:17:48.9446627Z Package 'php-symfony-one-signal-notifier' is not installed, so not removed
2026-05-03T01:17:48.9447099Z Package 'php-symfony-orange-sms-notifier' is not installed, so not removed
2026-05-03T01:17:48.9447560Z Package 'php-symfony-ovh-cloud-notifier' is not installed, so not removed
2026-05-03T01:17:48.9448026Z Package 'php-symfony-pager-duty-notifier' is not installed, so not removed
2026-05-03T01:17:48.9448484Z Package 'php-symfony-phpunit-bridge' is not installed, so not removed
2026-05-03T01:17:48.9448982Z Package 'php-symfony-phrase-translation-provider' is not installed, so not removed
2026-05-03T01:17:48.9449700Z Package 'php-symfony-plivo-notifier' is not installed, so not removed
2026-05-03T01:17:48.9450138Z Package 'php-symfony-polyfill' is not installed, so not removed
2026-05-03T01:17:48.9450552Z Package 'php-symfony-polyfill-apcu' is not installed, so not removed
2026-05-03T01:17:48.9450986Z Package 'php-symfony-polyfill-ctype' is not installed, so not removed
2026-05-03T01:17:48.9451413Z Package 'php-symfony-polyfill-php72' is not installed, so not removed
2026-05-03T01:17:48.9451849Z Package 'php-symfony-polyfill-php73' is not installed, so not removed
2026-05-03T01:17:48.9452273Z Package 'php-symfony-polyfill-php74' is not installed, so not removed
2026-05-03T01:17:48.9452698Z Package 'php-symfony-polyfill-php81' is not installed, so not removed
2026-05-03T01:17:48.9453124Z Package 'php-symfony-polyfill-php82' is not installed, so not removed
2026-05-03T01:17:48.9453548Z Package 'php-symfony-polyfill-iconv' is not installed, so not removed
2026-05-03T01:17:48.9454181Z Package 'php-symfony-polyfill-intl-grapheme' is not installed, so not removed
2026-05-03T01:17:48.9454676Z Package 'php-symfony-polyfill-intl-icu' is not installed, so not removed
2026-05-03T01:17:48.9455202Z Package 'php-symfony-polyfill-intl-messageformatter' is not installed, so not removed
2026-05-03T01:17:48.9455717Z Package 'php-symfony-polyfill-intl-idn' is not installed, so not removed
2026-05-03T01:17:48.9456209Z Package 'php-symfony-polyfill-intl-normalizer' is not installed, so not removed
2026-05-03T01:17:48.9456701Z Package 'php-symfony-polyfill-mbstring' is not installed, so not removed
2026-05-03T01:17:48.9457142Z Package 'php-symfony-polyfill-util' is not installed, so not removed
2026-05-03T01:17:48.9457578Z Package 'php-symfony-polyfill-xml' is not installed, so not removed
2026-05-03T01:17:48.9458001Z Package 'php-symfony-polyfill-uuid' is not installed, so not removed
2026-05-03T01:17:48.9458553Z Package 'php-symfony-postmark-mailer' is not installed, so not removed
2026-05-03T01:17:48.9459037Z Package 'php-symfony-psr-http-message-bridge' is not installed, so not removed
2026-05-03T01:17:48.9459649Z Package 'php-symfony-pushover-notifier' is not installed, so not removed
2026-05-03T01:17:48.9460139Z Package 'php-symfony-redis-messenger' is not installed, so not removed
2026-05-03T01:17:48.9460599Z Package 'php-symfony-redlink-notifier' is not installed, so not removed
2026-05-03T01:17:48.9461090Z Package 'php-symfony-ring-central-notifier' is not installed, so not removed
2026-05-03T01:17:48.9461583Z Package 'php-symfony-rocket-chat-notifier' is not installed, so not removed
2026-05-03T01:17:48.9462031Z Package 'php-symfony-runtime' is not installed, so not removed
2026-05-03T01:17:48.9462451Z Package 'php-symfony-scaleway-mailer' is not installed, so not removed
2026-05-03T01:17:48.9462890Z Package 'php-symfony-security-acl' is not installed, so not removed
2026-05-03T01:17:48.9463345Z Package 'php-symfony-sendberry-notifier' is not installed, so not removed
2026-05-03T01:17:48.9463812Z Package 'php-symfony-sendgrid-mailer' is not installed, so not removed
2026-05-03T01:17:48.9464265Z Package 'php-symfony-sendinblue-mailer' is not installed, so not removed
2026-05-03T01:17:48.9464732Z Package 'php-symfony-sendinblue-notifier' is not installed, so not removed
2026-05-03T01:17:48.9465221Z Package 'php-symfony-simple-textin-notifier' is not installed, so not removed
2026-05-03T01:17:48.9465690Z Package 'php-symfony-sinch-notifier' is not installed, so not removed
2026-05-03T01:17:48.9466121Z Package 'php-symfony-slack-notifier' is not installed, so not removed
2026-05-03T01:17:48.9466565Z Package 'php-symfony-sms-biuras-notifier' is not installed, so not removed
2026-05-03T01:17:48.9467022Z Package 'php-symfony-sms-factor-notifier' is not installed, so not removed
2026-05-03T01:17:48.9467461Z Package 'php-symfony-sms77-notifier' is not installed, so not removed
2026-05-03T01:17:48.9467901Z Package 'php-symfony-smsapi-notifier' is not installed, so not removed
2026-05-03T01:17:48.9468339Z Package 'php-symfony-smsc-notifier' is not installed, so not removed
2026-05-03T01:17:48.9468781Z Package 'php-symfony-smsmode-notifier' is not installed, so not removed
2026-05-03T01:17:48.9469229Z Package 'php-symfony-spot-hit-notifier' is not installed, so not removed
2026-05-03T01:17:48.9469795Z Package 'php-symfony-telegram-notifier' is not installed, so not removed
2026-05-03T01:17:48.9470241Z Package 'php-symfony-telnyx-notifier' is not installed, so not removed
2026-05-03T01:17:48.9470679Z Package 'php-symfony-termii-notifier' is not installed, so not removed
2026-05-03T01:17:48.9471119Z Package 'php-symfony-turbo-sms-notifier' is not installed, so not removed
2026-05-03T01:17:48.9471560Z Package 'php-symfony-twilio-notifier' is not installed, so not removed
2026-05-03T01:17:48.9472022Z Package 'php-symfony-twitter-notifier' is not installed, so not removed
2026-05-03T01:17:48.9472483Z Package 'php-symfony-vonage-notifier' is not installed, so not removed
2026-05-03T01:17:48.9472934Z Package 'php-symfony-yunpian-notifier' is not installed, so not removed
2026-05-03T01:17:48.9473521Z Package 'php-symfony-zendesk-notifier' is not installed, so not removed
2026-05-03T01:17:48.9473969Z Package 'php-symfony-zulip-notifier' is not installed, so not removed
2026-05-03T01:17:48.9474376Z Package 'php-text-captcha' is not installed, so not removed
2026-05-03T01:17:48.9474768Z Package 'php-text-password' is not installed, so not removed
2026-05-03T01:17:48.9475148Z Package 'php-text-figlet' is not installed, so not removed
2026-05-03T01:17:48.9475541Z Package 'php-text-languagedetect' is not installed, so not removed
2026-05-03T01:17:48.9475931Z Package 'php-text-wiki' is not installed, so not removed
2026-05-03T01:17:48.9476271Z Package 'php-thrift' is not installed, so not removed
2026-05-03T01:17:48.9476625Z Package 'php8.3-tideways' is not installed, so not removed
2026-05-03T01:17:48.9477122Z Package 'php-tideways-all-dev' is not installed, so not removed
2026-05-03T01:17:49.1175302Z Package 'php-tijsverkoyen-css-to-inline-styles' is not installed, so not removed
2026-05-03T01:17:49.1176197Z Package 'php-timer' is not installed, so not removed
2026-05-03T01:17:49.1176793Z Package 'php-twig-doc' is not installed, so not removed
2026-05-03T01:17:49.1177425Z Package 'php-twig-cache-extra' is not installed, so not removed
2026-05-03T01:17:49.1178159Z Package 'php-twig-cssinliner-extra' is not installed, so not removed
2026-05-03T01:17:49.1178888Z Package 'php-twig-extra-bundle' is not installed, so not removed
2026-05-03T01:17:49.1179797Z Package 'php-twig-html-extra' is not installed, so not removed
2026-05-03T01:17:49.1180495Z Package 'php-twig-i18n-extension' is not installed, so not removed
2026-05-03T01:17:49.1181178Z Package 'php-twig-inky-extra' is not installed, so not removed
2026-05-03T01:17:49.1181844Z Package 'php-twig-intl-extra' is not installed, so not removed
2026-05-03T01:17:49.1182524Z Package 'php-twig-markdown-extra' is not installed, so not removed
2026-05-03T01:17:49.1183198Z Package 'php-twig-string-extra' is not installed, so not removed
2026-05-03T01:17:49.1183824Z Package 'php8.3-uopz' is not installed, so not removed
2026-05-03T01:17:49.1184400Z Package 'php-uopz-all-dev' is not installed, so not removed
2026-05-03T01:17:49.1185046Z Package 'php8.3-uploadprogress' is not installed, so not removed
2026-05-03T01:17:49.1185757Z Package 'php-uploadprogress-all-dev' is not installed, so not removed
2026-05-03T01:17:49.1186408Z Package 'php8.3-uuid' is not installed, so not removed
2026-05-03T01:17:49.1186999Z Package 'php-uuid-all-dev' is not installed, so not removed
2026-05-03T01:17:49.1187579Z Package 'php-validate' is not installed, so not removed
2026-05-03T01:17:49.1188176Z Package 'php-vlucas-phpdotenv' is not installed, so not removed
2026-05-03T01:17:49.1188876Z Package 'php-voku-portable-ascii' is not installed, so not removed
2026-05-03T01:17:49.1189750Z Package 'php-wmerrors' is not installed, so not removed
2026-05-03T01:17:49.1190377Z Package 'php-xdebug-all-dev' is not installed, so not removed
2026-05-03T01:17:49.1190981Z Package 'php-xml-svg' is not installed, so not removed
2026-05-03T01:17:49.1191560Z Package 'php8.3-xmlrpc' is not installed, so not removed
2026-05-03T01:17:49.1192168Z Package 'php-xmlrpc-all-dev' is not installed, so not removed
2026-05-03T01:17:49.1192772Z Package 'php8.3-yac' is not installed, so not removed
2026-05-03T01:17:49.1193342Z Package 'php-yac-all-dev' is not installed, so not removed
2026-05-03T01:17:49.1193955Z Package 'php-yaml-all-dev' is not installed, so not removed
2026-05-03T01:17:49.1194554Z Package 'php-zend-code' is not installed, so not removed
2026-05-03T01:17:49.1195162Z Package 'php-zend-eventmanager' is not installed, so not removed
2026-05-03T01:17:49.1195798Z Package 'php-zend-stdlib' is not installed, so not removed
2026-05-03T01:17:49.1196388Z Package 'php-zeroc-ice' is not installed, so not removed
2026-05-03T01:17:49.1196987Z Package 'php-zeta-base' is not installed, so not removed
2026-05-03T01:17:49.1197628Z Package 'php-zeta-console-tools' is not installed, so not removed
2026-05-03T01:17:49.1198770Z Package 'php-zeta-unit-test' is not installed, so not removed
2026-05-03T01:17:49.1199639Z Package 'php-zmq-all-dev' is not installed, so not removed
2026-05-03T01:17:49.1200342Z Package 'php-zumba-json-serializer' is not installed, so not removed
2026-05-03T01:17:49.1201052Z Package 'php8.3-libvirt-php' is not installed, so not removed
2026-05-03T01:17:49.1201625Z Package 'phpab' is not installed, so not removed
2026-05-03T01:17:49.1202147Z Package 'phpcpd' is not installed, so not removed
2026-05-03T01:17:49.1202730Z Package 'phpunit-cli-parser' is not installed, so not removed
2026-05-03T01:17:49.1203352Z Package 'phpldapadmin' is not installed, so not removed
2026-05-03T01:17:49.1203914Z Package 'phpliteadmin' is not installed, so not removed
2026-05-03T01:17:49.1204526Z Package 'phpliteadmin-themes' is not installed, so not removed
2026-05-03T01:17:49.1205387Z Package 'phploc' is not installed, so not removed
2026-05-03T01:17:49.1205940Z Package 'phppgadmin' is not installed, so not removed
2026-05-03T01:17:49.1206474Z Package 'phpsysinfo' is not installed, so not removed
2026-05-03T01:17:49.1207045Z Package 'phpunit-code-unit' is not installed, so not removed
2026-05-03T01:17:49.1207649Z Package 'phpunit-diff' is not installed, so not removed
2026-05-03T01:17:49.1208247Z Package 'phpunit-exporter' is not installed, so not removed
2026-05-03T01:17:49.1208899Z Package 'phpunit-global-state' is not installed, so not removed
2026-05-03T01:17:49.1209860Z Package 'phpunit-object-enumerator' is not installed, so not removed
2026-05-03T01:17:49.1210627Z Package 'phpunit-resource-operations' is not installed, so not removed
2026-05-03T01:17:49.1211311Z Package 'phpunit-type' is not installed, so not removed
2026-05-03T01:17:49.1211964Z Package 'phpunit-object-reflector' is not installed, so not removed
2026-05-03T01:17:49.1212644Z Package 'phpwebcounter' is not installed, so not removed
2026-05-03T01:17:49.1213270Z Package 'phpwebcounter-extra' is not installed, so not removed
2026-05-03T01:17:49.1213918Z Package 'python3-phply' is not installed, so not removed
2026-05-03T01:17:49.1214553Z Package 'python3-phpserialize' is not installed, so not removed
2026-05-03T01:17:49.1215294Z Package 'python3-sphinxcontrib.phpdomain' is not installed, so not removed
2026-05-03T01:17:49.1215993Z Package 'simplesamlphp' is not installed, so not removed
2026-05-03T01:17:49.1216589Z Package 'slbackup-php' is not installed, so not removed
2026-05-03T01:17:49.1217170Z Package 'uwsgi-plugin-php' is not installed, so not removed
2026-05-03T01:17:49.1217732Z Package 'weechat-php' is not installed, so not removed
2026-05-03T01:17:49.1218256Z Package 'php-mythtv' is not installed, so not removed
2026-05-03T01:17:49.1218757Z Package 'mono-devel' is not installed, so not removed
2026-05-03T01:17:49.1219229Z The following packages will be REMOVED:
2026-05-03T01:17:49.1220107Z   azure-cli clang-16 clang-17 clang-18 clang-tidy-16 clang-tidy-17
2026-05-03T01:17:49.1220793Z   clang-tidy-18 clang-tools-16 clang-tools-17 clang-tools-18 firefox
2026-05-03T01:17:49.1221536Z   google-chrome-stable google-cloud-cli google-cloud-cli-anthoscli llvm-16
2026-05-03T01:17:49.1222288Z   llvm-16-dev llvm-16-linker-tools llvm-16-runtime llvm-16-tools llvm-17
2026-05-03T01:17:49.1223025Z   llvm-17-dev llvm-17-linker-tools llvm-17-runtime llvm-17-tools llvm-18
2026-05-03T01:17:49.1223755Z   llvm-18-dev llvm-18-linker-tools llvm-18-runtime llvm-18-tools php-common
2026-05-03T01:17:49.1224533Z   php-pear php8.3 php8.3-amqp php8.3-apcu php8.3-bcmath php8.3-bz2 php8.3-cgi
2026-05-03T01:17:49.1225313Z   php8.3-cli php8.3-common php8.3-curl php8.3-dba php8.3-dev php8.3-enchant
2026-05-03T01:17:49.1226063Z   php8.3-fpm php8.3-gd php8.3-gmp php8.3-igbinary php8.3-imagick php8.3-imap
2026-05-03T01:17:49.1226821Z   php8.3-interbase php8.3-intl php8.3-ldap php8.3-mbstring php8.3-memcache
2026-05-03T01:17:49.1227567Z   php8.3-memcached php8.3-mongodb php8.3-msgpack php8.3-mysql php8.3-odbc
2026-05-03T01:17:49.1228646Z   php8.3-opcache php8.3-pcov php8.3-pgsql php8.3-phpdbg php8.3-pspell
2026-05-03T01:17:49.1229333Z   php8.3-readline php8.3-redis php8.3-snmp php8.3-soap php8.3-sqlite3
2026-05-03T01:17:49.1230249Z   php8.3-sybase php8.3-tidy php8.3-xdebug php8.3-xml php8.3-xsl php8.3-yaml
2026-05-03T01:17:49.1230825Z   php8.3-zip php8.3-zmq powershell
2026-05-03T01:17:49.6276018Z 0 upgraded, 0 newly installed, 78 to remove and 5 not upgraded.
2026-05-03T01:17:49.7392598Z After this operation, 3857 MB disk space will be freed.
2026-05-03T01:17:49.7393056Z (Reading database ... 
2026-05-03T01:17:49.7393350Z (Reading database ... 5%
2026-05-03T01:17:49.7393676Z (Reading database ... 10%
2026-05-03T01:17:49.7393987Z (Reading database ... 15%
2026-05-03T01:17:49.7394857Z (Reading database ... 20%
2026-05-03T01:17:49.7395190Z (Reading database ... 25%
2026-05-03T01:17:49.7395499Z (Reading database ... 30%
2026-05-03T01:17:49.7396177Z (Reading database ... 35%
2026-05-03T01:17:49.7396504Z (Reading database ... 40%
2026-05-03T01:17:49.7396836Z (Reading database ... 45%
2026-05-03T01:17:49.7397155Z (Reading database ... 50%
2026-05-03T01:17:49.7790089Z (Reading database ... 55%
2026-05-03T01:17:50.0772914Z (Reading database ... 60%
2026-05-03T01:17:50.3175863Z (Reading database ... 65%
2026-05-03T01:17:50.5684643Z (Reading database ... 70%
2026-05-03T01:17:50.8324900Z (Reading database ... 75%
2026-05-03T01:17:51.2651469Z (Reading database ... 80%
2026-05-03T01:17:51.7740780Z (Reading database ... 85%
2026-05-03T01:17:52.5038835Z (Reading database ... 90%
2026-05-03T01:17:52.9713844Z (Reading database ... 95%
2026-05-03T01:17:52.9714285Z (Reading database ... 100%
2026-05-03T01:17:52.9714809Z (Reading database ... 220762 files and directories currently installed.)
2026-05-03T01:17:52.9762749Z Removing azure-cli (2.85.0-1~noble) ...
2026-05-03T01:17:57.0690121Z Removing clang-tidy-16 (1:16.0.6-23ubuntu4) ...
2026-05-03T01:17:57.1156720Z Removing clang-tools-16 (1:16.0.6-23ubuntu4) ...
2026-05-03T01:17:57.1735451Z Removing clang-16 (1:16.0.6-23ubuntu4) ...
2026-05-03T01:17:57.1888760Z Removing clang-tidy-17 (1:17.0.6-9ubuntu1) ...
2026-05-03T01:17:57.2040751Z Removing clang-tools-17 (1:17.0.6-9ubuntu1) ...
2026-05-03T01:17:57.2448161Z Removing clang-17 (1:17.0.6-9ubuntu1) ...
2026-05-03T01:17:57.2636955Z Removing clang-tidy-18 (1:18.1.3-1ubuntu1) ...
2026-05-03T01:17:57.2874125Z Removing clang-tools-18 (1:18.1.3-1ubuntu1) ...
2026-05-03T01:17:57.3238267Z Removing clang-18 (1:18.1.3-1ubuntu1) ...
2026-05-03T01:17:57.3429163Z Removing firefox (149.0.2+build1-0ubuntu0.24.04.1~mt1) ...
2026-05-03T01:17:57.4386764Z Removing google-chrome-stable (147.0.7727.55-1) ...
2026-05-03T01:17:57.6293316Z Removing google-cloud-cli-anthoscli (564.0.0-0) ...
2026-05-03T01:18:06.2722222Z Removing google-cloud-cli (564.0.0-0) ...
2026-05-03T01:19:16.2663606Z Removing llvm-16-dev (1:16.0.6-23ubuntu4) ...
2026-05-03T01:19:16.4836621Z Removing llvm-16 (1:16.0.6-23ubuntu4) ...
2026-05-03T01:19:16.5095444Z Removing llvm-16-linker-tools (1:16.0.6-23ubuntu4) ...
2026-05-03T01:19:16.5240312Z Removing llvm-16-runtime (1:16.0.6-23ubuntu4) ...
2026-05-03T01:19:16.5509680Z Removing llvm-16-tools (1:16.0.6-23ubuntu4) ...
2026-05-03T01:19:16.6552351Z Removing llvm-17-dev (1:17.0.6-9ubuntu1) ...
2026-05-03T01:19:16.8440007Z Removing llvm-17 (1:17.0.6-9ubuntu1) ...
2026-05-03T01:19:16.8707397Z Removing llvm-17-linker-tools (1:17.0.6-9ubuntu1) ...
2026-05-03T01:19:16.8846034Z Removing llvm-17-runtime (1:17.0.6-9ubuntu1) ...
2026-05-03T01:19:16.9149988Z Removing llvm-17-tools (1:17.0.6-9ubuntu1) ...
2026-05-03T01:19:17.0102458Z Removing llvm-18-dev (1:18.1.3-1ubuntu1) ...
2026-05-03T01:19:17.2222758Z Removing llvm-18 (1:18.1.3-1ubuntu1) ...
2026-05-03T01:19:17.2448801Z Removing llvm-18-linker-tools (1:18.1.3-1ubuntu1) ...
2026-05-03T01:19:17.2628666Z Removing llvm-18-runtime (1:18.1.3-1ubuntu1) ...
2026-05-03T01:19:17.2926509Z Removing llvm-18-tools (1:18.1.3-1ubuntu1) ...
2026-05-03T01:19:17.4020433Z Removing php8.3-zip (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:17.5880151Z Removing php8.3-sybase (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:17.7318933Z Removing php-pear (1:1.10.13+submodules+notgz+2022032202-2build1) ...
2026-05-03T01:19:17.8343114Z Removing php8.3 (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:17.8520298Z Removing php8.3-amqp (1.11.0-5ubuntu1) ...
2026-05-03T01:19:17.9897732Z Removing php8.3-apcu (5.1.22+4.0.11-2ubuntu1) ...
2026-05-03T01:19:18.1211652Z Removing php8.3-bcmath (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:18.2596514Z Removing php8.3-bz2 (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:18.3910626Z Removing php8.3-zmq (1.1.3-24ubuntu1) ...
2026-05-03T01:19:18.5297195Z Removing php8.3-yaml (2.2.2+2.1.0+2.0.4+1.3.2-6ubuntu1) ...
2026-05-03T01:19:18.6585269Z Removing php8.3-cgi (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:20.7989330Z apache2_invoke php8.3-cgi prerm: No action required
2026-05-03T01:19:20.8260074Z Removing php8.3-dev (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:20.9098623Z Removing php8.3-xdebug (3.2.0+3.1.6+2.9.8+2.8.1+2.5.5-3ubuntu1) ...
2026-05-03T01:19:21.0216793Z Removing php8.3-phpdbg (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:22.5956186Z Removing php8.3-redis (5.3.7+4.3.0-3ubuntu1) ...
2026-05-03T01:19:22.6800089Z Removing php8.3-xsl (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:22.6934219Z Removing php8.3-soap (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:22.7922596Z Removing php8.3-curl (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:22.8821074Z Removing php8.3-dba (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:22.9674067Z Removing php8.3-enchant (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:23.0526858Z Removing php8.3-pcov (1.0.11-5ubuntu1) ...
2026-05-03T01:19:23.1238148Z Removing php8.3-fpm (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:24.6133826Z apache2_invoke php8.3-fpm prerm: No action required
2026-05-03T01:19:24.6547100Z Removing php8.3-gd (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:24.7226591Z Removing php8.3-gmp (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:24.8106887Z Removing php8.3-memcached (3.2.0+2.2.0-4ubuntu3) ...
2026-05-03T01:19:24.8738474Z Removing php8.3-igbinary (3.2.13-1ubuntu3) ...
2026-05-03T01:19:24.9418850Z Removing php8.3-imagick (3.7.0-4ubuntu3) ...
2026-05-03T01:19:25.0059155Z Removing php8.3-imap (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:25.0701001Z Removing php8.3-interbase (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:25.1440476Z Removing php8.3-intl (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:25.2116786Z Removing php8.3-ldap (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:25.2795293Z Removing php8.3-mbstring (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:25.3517499Z Removing php8.3-memcache (8.0+4.0.5.2+3.0.9~20170802.e702b5f9+-8ubuntu1) ...
2026-05-03T01:19:25.4142183Z Removing php8.3-mongodb (1.15.0+1.11.1+1.9.2+1.7.5-1ubuntu3) ...
2026-05-03T01:19:25.4770861Z Removing php8.3-msgpack (1:2.2.0~rc2-3ubuntu1) ...
2026-05-03T01:19:25.5409585Z Removing php8.3-mysql (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:25.6791727Z Removing php8.3-odbc (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:25.7783545Z Removing php8.3-pgsql (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:25.8813089Z Removing php8.3-pspell (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:25.9510654Z Removing php8.3-snmp (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:26.0191320Z Removing php8.3-sqlite3 (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:26.1187198Z Removing php8.3-tidy (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:26.1821079Z Removing php8.3-xml (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:26.4647530Z Removing powershell (7.4.14-1.deb) ...
2026-05-03T01:19:26.5823507Z Removing php8.3-cli (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:27.1538171Z Removing php8.3-opcache (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:27.1948342Z Removing php8.3-readline (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:27.2450729Z Removing php8.3-common (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:27.4271249Z Removing php-common (2:93ubuntu2) ...
2026-05-03T01:19:27.4574660Z Stopping 'phpsessionclean.service', but its triggering units are still active:
2026-05-03T01:19:27.4575684Z 
2026-05-03T01:19:27.4575811Z phpsessionclean.timer
2026-05-03T01:19:27.4576011Z 
2026-05-03T01:19:28.0570056Z Processing triggers for libc-bin (2.39-0ubuntu8.7) ...
2026-05-03T01:19:28.1096123Z Processing triggers for systemd (255.4-1ubuntu8.15) ...
2026-05-03T01:19:28.1451787Z Processing triggers for man-db (2.12.0-4build2) ...
2026-05-03T01:19:28.1471410Z Not building database; man-db/auto-update is not 'true'.
2026-05-03T01:19:28.1483657Z Processing triggers for hicolor-icon-theme (0.17-2) ...
2026-05-03T01:19:29.6812663Z Reading package lists...
2026-05-03T01:19:29.9119111Z Building dependency tree...
2026-05-03T01:19:29.9126572Z Reading state information...
2026-05-03T01:19:30.1365532Z The following packages will be REMOVED:
2026-05-03T01:19:30.1366159Z   dictionaries-common emacsen-common firebird3.0-common firebird3.0-common-doc
2026-05-03T01:19:30.1368526Z   freetds-common hunspell-en-us icu-devtools imagemagick-6-common lib32gcc-s1
2026-05-03T01:19:30.1369866Z   lib32stdc++6 libaom3 libaspell15 libc-client2007e libc6-i386 libcanberra0t64
2026-05-03T01:19:30.1370812Z   libclang-common-16-dev libclang-common-17-dev libclang-common-18-dev
2026-05-03T01:19:30.1371649Z   libclang-rt-16-dev libclang-rt-17-dev libclang-rt-18-dev libclang1-16t64
2026-05-03T01:19:30.1372493Z   libclang1-17t64 libdbusmenu-glib4 libdbusmenu-gtk3-4 libde265-0
2026-05-03T01:19:30.1373324Z   libenchant-2-2 libfbclient2 libffi-dev libfftw3-double3 libgc1 libgd3
2026-05-03T01:19:30.1374184Z   libhashkit2t64 libheif-plugin-aomdec libheif-plugin-libde265 libheif1
2026-05-03T01:19:30.1375023Z   libhunspell-1.7-0 libicu-dev liblldb-16t64 liblldb-17t64 liblqr-1-0
2026-05-03T01:19:30.1375973Z   libmagickcore-6.q16-7t64 libmagickwand-6.q16-7t64 libmemcached11t64
2026-05-03T01:19:30.1376802Z   libncurses-dev libnorm1t64 libobjc-13-dev libobjc4 libogg0 libopenjp2-7
2026-05-03T01:19:30.1377614Z   libpcre2-16-0 libpcre2-32-0 libpcre2-dev libpcre2-posix3 libpfm4
2026-05-03T01:19:30.1378417Z   libpgm-5.3-0t64 libqdbm14t64 librabbitmq4 libraw23t64 libsnappy1v5 libsybdb5
2026-05-03T01:19:30.1379349Z   libtdb1 libtidy5deb1 libtommath1 libvorbis0a libvorbisfile3 libwebpdemux2
2026-05-03T01:19:30.1380392Z   libwebpmux3 libxml2-dev libz3-4 libz3-dev libzip4t64 libzmq5 mlock shtool
2026-05-03T01:19:30.1381094Z   sound-theme-freedesktop xul-ext-ubufox
2026-05-03T01:19:30.3901392Z 0 upgraded, 0 newly installed, 77 to remove and 5 not upgraded.
2026-05-03T01:19:30.3901846Z After this operation, 389 MB disk space will be freed.
2026-05-03T01:19:30.4077211Z (Reading database ... 
2026-05-03T01:19:30.4078978Z (Reading database ... 5%
2026-05-03T01:19:30.4079538Z (Reading database ... 10%
2026-05-03T01:19:30.4079882Z (Reading database ... 15%
2026-05-03T01:19:30.4080182Z (Reading database ... 20%
2026-05-03T01:19:30.4080489Z (Reading database ... 25%
2026-05-03T01:19:30.4080782Z (Reading database ... 30%
2026-05-03T01:19:30.4081081Z (Reading database ... 35%
2026-05-03T01:19:30.4081416Z (Reading database ... 40%
2026-05-03T01:19:30.4081732Z (Reading database ... 45%
2026-05-03T01:19:30.4082032Z (Reading database ... 50%
2026-05-03T01:19:30.4082326Z (Reading database ... 55%
2026-05-03T01:19:30.4117876Z (Reading database ... 60%
2026-05-03T01:19:30.4219971Z (Reading database ... 65%
2026-05-03T01:19:30.4246931Z (Reading database ... 70%
2026-05-03T01:19:30.4300355Z (Reading database ... 75%
2026-05-03T01:19:30.4324976Z (Reading database ... 80%
2026-05-03T01:19:30.4355173Z (Reading database ... 85%
2026-05-03T01:19:30.4385437Z (Reading database ... 90%
2026-05-03T01:19:30.4511846Z (Reading database ... 95%
2026-05-03T01:19:30.4512239Z (Reading database ... 100%
2026-05-03T01:19:30.4512746Z (Reading database ... 122759 files and directories currently installed.)
2026-05-03T01:19:30.4539595Z Removing libenchant-2-2:amd64 (2.3.3-2build2) ...
2026-05-03T01:19:30.4673056Z Removing hunspell-en-us (1:2020.12.07-2) ...
2026-05-03T01:19:30.5199890Z Removing dictionaries-common (1.29.7) ...
2026-05-03T01:19:30.5806471Z Removing 'diversion of /usr/share/dict/words to /usr/share/dict/words.pre-dictionaries-common by dictionaries-common'
2026-05-03T01:19:30.5973103Z Removing emacsen-common (3.0.5) ...
2026-05-03T01:19:30.6412086Z Removing libfbclient2:amd64 (3.0.11.33703.ds4-2ubuntu2) ...
2026-05-03T01:19:30.6544506Z Removing firebird3.0-common (3.0.11.33703.ds4-2ubuntu2) ...
2026-05-03T01:19:30.6786266Z Removing firebird3.0-common-doc (3.0.11.33703.ds4-2ubuntu2) ...
2026-05-03T01:19:30.6900057Z Removing libsybdb5:amd64 (1.3.17+ds-2build3) ...
2026-05-03T01:19:30.7068096Z Removing freetds-common (1.3.17+ds-2build3) ...
2026-05-03T01:19:30.7289049Z Removing libxml2-dev:amd64 (2.9.14+dfsg-1.3ubuntu3.7) ...
2026-05-03T01:19:30.7558552Z Removing libicu-dev:amd64 (74.2-1ubuntu3.1) ...
2026-05-03T01:19:30.7894859Z Removing icu-devtools (74.2-1ubuntu3.1) ...
2026-05-03T01:19:30.8022977Z Removing libmagickwand-6.q16-7t64:amd64 (8:6.9.12.98+dfsg1-5.2build2) ...
2026-05-03T01:19:30.8253256Z Removing libmagickcore-6.q16-7t64:amd64 (8:6.9.12.98+dfsg1-5.2build2) ...
2026-05-03T01:19:30.8579797Z Removing imagemagick-6-common (8:6.9.12.98+dfsg1-5.2build2) ...
2026-05-03T01:19:30.8684922Z Removing libclang-rt-18-dev:amd64 (1:18.1.3-1ubuntu1) ...
2026-05-03T01:19:30.8912627Z Removing libclang-rt-16-dev:amd64 (1:16.0.6-23ubuntu4) ...
2026-05-03T01:19:30.9145129Z Removing lib32stdc++6 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:30.9307604Z Removing lib32gcc-s1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:30.9450158Z Removing libaspell15:amd64 (0.60.8.1-1build1) ...
2026-05-03T01:19:30.9700190Z Removing libc-client2007e (8:2007f~dfsg-7build3) ...
2026-05-03T01:19:30.9829243Z Removing libc6-i386 (2.39-0ubuntu8.7) ...
2026-05-03T01:19:31.0195510Z Removing libcanberra0t64:amd64 (0.30-10ubuntu10) ...
2026-05-03T01:19:31.0320771Z Removing libclang-common-16-dev (1:16.0.6-23ubuntu4) ...
2026-05-03T01:19:31.0548994Z Removing libclang-common-17-dev:amd64 (1:17.0.6-9ubuntu1) ...
2026-05-03T01:19:31.0801146Z Removing libclang-common-18-dev:amd64 (1:18.1.3-1ubuntu1) ...
2026-05-03T01:19:31.1044580Z Removing libclang-rt-17-dev:amd64 (1:17.0.6-9ubuntu1) ...
2026-05-03T01:19:31.1259998Z Removing libclang1-16t64 (1:16.0.6-23ubuntu4) ...
2026-05-03T01:19:31.1383933Z Removing libclang1-17t64 (1:17.0.6-9ubuntu1) ...
2026-05-03T01:19:31.1505437Z Removing libdbusmenu-gtk3-4:amd64 (18.10.20180917~bzr492+repack1-3.1ubuntu5) ...
2026-05-03T01:19:31.1671453Z Removing libdbusmenu-glib4:amd64 (18.10.20180917~bzr492+repack1-3.1ubuntu5) ...
2026-05-03T01:19:31.1839853Z Removing libffi-dev:amd64 (3.4.6-1build1) ...
2026-05-03T01:19:31.2149248Z Removing libfftw3-double3:amd64 (3.3.10-1ubuntu3) ...
2026-05-03T01:19:31.2321230Z Removing libobjc-13-dev:amd64 (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T01:19:31.2452890Z Removing libobjc4:amd64 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:31.2572020Z Removing libgc1:amd64 (1:8.2.6-1build1) ...
2026-05-03T01:19:31.2697704Z Removing libgd3:amd64 (2.3.3-9ubuntu5) ...
2026-05-03T01:19:31.2917253Z Removing libmemcached11t64:amd64 (1.1.4-1.1build3) ...
2026-05-03T01:19:31.3035465Z Removing libhashkit2t64:amd64 (1.1.4-1.1build3) ...
2026-05-03T01:19:31.3146708Z Removing libhunspell-1.7-0:amd64 (1.7.2+really1.7.2-10build3) ...
2026-05-03T01:19:31.3259120Z Removing liblldb-16t64 (1:16.0.6-23ubuntu4) ...
2026-05-03T01:19:31.3414657Z Removing liblldb-17t64 (1:17.0.6-9ubuntu1) ...
2026-05-03T01:19:31.3532083Z Removing liblqr-1-0:amd64 (0.4.2-2.1build2) ...
2026-05-03T01:19:31.3655296Z Removing libncurses-dev:amd64 (6.4+20240113-1ubuntu2) ...
2026-05-03T01:19:31.3804209Z Removing libzmq5:amd64 (4.3.5-1build2) ...
2026-05-03T01:19:31.3920713Z Removing libnorm1t64:amd64 (1.5.9+dfsg-3.1build1) ...
2026-05-03T01:19:31.4040950Z Removing libvorbisfile3:amd64 (1.3.7-1build3) ...
2026-05-03T01:19:31.4158886Z Removing libvorbis0a:amd64 (1.3.7-1build3) ...
2026-05-03T01:19:31.4274659Z Removing libogg0:amd64 (1.3.5-3build1) ...
2026-05-03T01:19:31.4437174Z Removing libopenjp2-7:amd64 (2.5.0-2ubuntu0.4) ...
2026-05-03T01:19:31.4557342Z Removing libpcre2-dev:amd64 (10.42-4ubuntu2.1) ...
2026-05-03T01:19:31.4772922Z Removing libpcre2-16-0:amd64 (10.42-4ubuntu2.1) ...
2026-05-03T01:19:31.4891485Z Removing libpcre2-32-0:amd64 (10.42-4ubuntu2.1) ...
2026-05-03T01:19:31.5007989Z Removing libpcre2-posix3:amd64 (10.42-4ubuntu2.1) ...
2026-05-03T01:19:31.5165572Z Removing libpfm4:amd64 (4.13.0+git32-g0d4ed0e-1) ...
2026-05-03T01:19:31.5281664Z Removing libpgm-5.3-0t64:amd64 (5.3.128~dfsg-2.1build1) ...
2026-05-03T01:19:31.5400345Z Removing libqdbm14t64 (1.8.78-12.1build2) ...
2026-05-03T01:19:31.5568446Z Removing librabbitmq4:amd64 (0.11.0-1build2) ...
2026-05-03T01:19:31.5690681Z Removing libraw23t64:amd64 (0.21.2-2.1ubuntu0.24.04.1) ...
2026-05-03T01:19:31.5814146Z Removing libsnappy1v5:amd64 (1.1.10-1build1) ...
2026-05-03T01:19:31.5934310Z Removing libtdb1:amd64 (1.4.10-1build1) ...
2026-05-03T01:19:31.6058866Z Removing libtidy5deb1:amd64 (2:5.6.0-11ubuntu2) ...
2026-05-03T01:19:31.6175954Z Removing libtommath1:amd64 (1.2.1-2build1) ...
2026-05-03T01:19:31.6290915Z Removing libwebpdemux2:amd64 (1.3.2-0.4build3) ...
2026-05-03T01:19:31.6411256Z Removing libwebpmux3:amd64 (1.3.2-0.4build3) ...
2026-05-03T01:19:31.6527444Z Removing libz3-dev:amd64 (4.8.12-3.1build1) ...
2026-05-03T01:19:31.6650505Z Removing libz3-4:amd64 (4.8.12-3.1build1) ...
2026-05-03T01:19:31.6798215Z Removing libzip4t64:amd64 (1.7.3-1.1ubuntu2) ...
2026-05-03T01:19:31.6913984Z Removing mlock (8:2007f~dfsg-7build3) ...
2026-05-03T01:19:31.7026012Z Removing shtool (2.0.8-10) ...
2026-05-03T01:19:31.7161800Z Removing sound-theme-freedesktop (0.8-2ubuntu1) ...
2026-05-03T01:19:31.7290584Z Removing xul-ext-ubufox (3.4-0ubuntu1.17.10.4) ...
2026-05-03T01:19:31.7887491Z Removing libheif1:amd64 (1.17.6-1ubuntu4.2) ...
2026-05-03T01:19:31.8013765Z Removing libheif-plugin-libde265:amd64 (1.17.6-1ubuntu4.2) ...
2026-05-03T01:19:31.8139708Z Removing libde265-0:amd64 (1.0.15-1build3) ...
2026-05-03T01:19:31.8300750Z Removing libheif-plugin-aomdec:amd64 (1.17.6-1ubuntu4.2) ...
2026-05-03T01:19:31.8414175Z Removing libaom3:amd64 (3.8.2-2ubuntu0.1) ...
2026-05-03T01:19:31.8707961Z Processing triggers for man-db (2.12.0-4build2) ...
2026-05-03T01:19:31.8724873Z Not building database; man-db/auto-update is not 'true'.
2026-05-03T01:19:31.8740277Z Processing triggers for postgresql-common (290.pgdg24.04+1) ...
2026-05-03T01:19:31.9838024Z Building PostgreSQL dictionaries from installed myspell/hunspell packages...
2026-05-03T01:19:31.9838635Z Removing obsolete dictionary files:
2026-05-03T01:19:31.9839851Z   /var/cache/postgresql/dicts/en_us.affix
2026-05-03T01:19:31.9840490Z   /var/cache/postgresql/dicts/en_us.dict
2026-05-03T01:19:31.9884102Z   /usr/share/postgresql/16/tsearch_data/en_us.affix
2026-05-03T01:19:31.9884639Z   /usr/share/postgresql/16/tsearch_data/en_us.dict
2026-05-03T01:19:32.0092597Z Processing triggers for install-info (7.1-3build2) ...
2026-05-03T01:19:32.2910831Z Processing triggers for libc-bin (2.39-0ubuntu8.7) ...
2026-05-03T01:19:33.4515424Z === After cleanup ===
2026-05-03T01:19:33.4527229Z Filesystem      Size  Used Avail Use% Mounted on
2026-05-03T01:19:33.4527676Z /dev/root       145G   25G  120G  17% /
2026-05-03T01:19:33.4564335Z ##[group]Run sudo swapoff /mnt/swapfile 2>/dev/null || true
2026-05-03T01:19:33.4564769Z [36;1msudo swapoff /mnt/swapfile 2>/dev/null || true[0m
2026-05-03T01:19:33.4565085Z [36;1msudo rm -f /mnt/swapfile[0m
2026-05-03T01:19:33.4565528Z [36;1msudo fallocate -l 16G /mnt/swapfile || sudo dd if=/dev/zero of=/mnt/swapfile bs=1M count=16384[0m
2026-05-03T01:19:33.4565981Z [36;1msudo chmod 600 /mnt/swapfile[0m
2026-05-03T01:19:33.4566232Z [36;1msudo mkswap /mnt/swapfile[0m
2026-05-03T01:19:33.4566476Z [36;1msudo swapon /mnt/swapfile[0m
2026-05-03T01:19:33.4566696Z [36;1mfree -h[0m
2026-05-03T01:19:33.4589950Z shell: /usr/bin/bash -e {0}
2026-05-03T01:19:33.4590190Z env:
2026-05-03T01:19:33.4590370Z   KERNEL_NAME: Castorice
2026-05-03T01:19:33.4590587Z   DEVICE_CODE: fire
2026-05-03T01:19:33.4590798Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:19:33.4591055Z   CLANG_VERSION: 
2026-05-03T01:19:33.4591428Z   LLD_VERSION: 
2026-05-03T01:19:33.4591645Z   KERNEL_HEAD_HASH: 
2026-05-03T01:19:33.4591856Z   KSU_DIR: 
2026-05-03T01:19:33.4592017Z   KSU_VERSION: 
2026-05-03T01:19:33.4592192Z   KERNEL_VERSION: 
2026-05-03T01:19:33.4592375Z   ZIP_NAME: 
2026-05-03T01:19:33.4592567Z ##[endgroup]
2026-05-03T01:19:33.5173599Z Setting up swapspace version 1, size = 16 GiB (17179865088 bytes)
2026-05-03T01:19:33.5174153Z no label, UUID=f3c1ac3f-936f-408c-8726-9d8144be1069
2026-05-03T01:19:33.5297895Z                total        used        free      shared  buff/cache   available
2026-05-03T01:19:33.5298353Z Mem:            15Gi       994Mi        11Gi        43Mi       3.3Gi        14Gi
2026-05-03T01:19:33.5298699Z Swap:           18Gi          0B        18Gi
2026-05-03T01:19:33.5330623Z ##[group]Run sudo apt-get update
2026-05-03T01:19:33.5330944Z [36;1msudo apt-get update[0m
2026-05-03T01:19:33.5331327Z [36;1msudo apt-get install -y aria2 git ccache automake flex lzop bison gperf \[0m
2026-05-03T01:19:33.5331878Z [36;1m  build-essential zip curl zlib1g-dev g++-multilib libxml2-utils bzip2 \[0m
2026-05-03T01:19:33.5332399Z [36;1m  libbz2-dev squashfs-tools pngcrush schedtool dpkg-dev liblz4-tool make \[0m
2026-05-03T01:19:33.5332935Z [36;1m  optipng maven libssl-dev pwgen libxml-sax-base-perl libxml-simple-perl \[0m
2026-05-03T01:19:33.5333424Z [36;1m  libc6-dev-i386 lib32ncurses-dev libncurses-dev libx11-dev lib32z-dev \[0m
2026-05-03T01:19:33.5333879Z [36;1m  libstdc++6 lib32stdc++6 libgl1-mesa-dev xsltproc unzip gzip \[0m
2026-05-03T01:19:33.5334336Z [36;1m  device-tree-compiler cpio findutils python3 bc p7zip-full libelf-dev \[0m
2026-05-03T01:19:33.5334702Z [36;1m  jq libyaml-dev -y[0m
2026-05-03T01:19:33.5357942Z shell: /usr/bin/bash -e {0}
2026-05-03T01:19:33.5358179Z env:
2026-05-03T01:19:33.5358361Z   KERNEL_NAME: Castorice
2026-05-03T01:19:33.5358576Z   DEVICE_CODE: fire
2026-05-03T01:19:33.5358798Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:19:33.5359056Z   CLANG_VERSION: 
2026-05-03T01:19:33.5359249Z   LLD_VERSION: 
2026-05-03T01:19:33.5359713Z   KERNEL_HEAD_HASH: 
2026-05-03T01:19:33.5359902Z   KSU_DIR: 
2026-05-03T01:19:33.5360071Z   KSU_VERSION: 
2026-05-03T01:19:33.5360241Z   KERNEL_VERSION: 
2026-05-03T01:19:33.5360428Z   ZIP_NAME: 
2026-05-03T01:19:33.5360603Z ##[endgroup]
2026-05-03T01:19:33.6163762Z Get:1 file:/etc/apt/apt-mirrors.txt Mirrorlist [144 B]
2026-05-03T01:19:33.6704222Z Hit:2 http://azure.archive.ubuntu.com/ubuntu noble InRelease
2026-05-03T01:19:33.6711810Z Hit:6 https://packages.microsoft.com/repos/azure-cli noble InRelease
2026-05-03T01:19:33.6712846Z Get:7 https://packages.microsoft.com/ubuntu/24.04/prod noble InRelease [3600 B]
2026-05-03T01:19:33.6713986Z Get:3 http://azure.archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]
2026-05-03T01:19:33.6714989Z Get:8 https://dl.google.com/linux/chrome-stable/deb stable InRelease [1825 B]
2026-05-03T01:19:33.6764690Z Get:4 http://azure.archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]
2026-05-03T01:19:33.6804040Z Get:5 http://azure.archive.ubuntu.com/ubuntu noble-security InRelease [126 kB]
2026-05-03T01:19:33.8667795Z Get:9 https://packages.microsoft.com/ubuntu/24.04/prod noble/main armhf Packages [11.6 kB]
2026-05-03T01:19:33.8774328Z Get:10 https://packages.microsoft.com/ubuntu/24.04/prod noble/main amd64 Packages [132 kB]
2026-05-03T01:19:33.8840635Z Get:11 https://packages.microsoft.com/ubuntu/24.04/prod noble/main arm64 Packages [107 kB]
2026-05-03T01:19:33.9390939Z Get:12 https://dl.google.com/linux/chrome-stable/deb stable/main amd64 Packages [1216 B]
2026-05-03T01:19:33.9711236Z Get:13 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 Packages [1946 kB]
2026-05-03T01:19:33.9822053Z Get:14 http://azure.archive.ubuntu.com/ubuntu noble-updates/main Translation-en [348 kB]
2026-05-03T01:19:33.9845971Z Get:15 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 Components [177 kB]
2026-05-03T01:19:33.9869229Z Get:16 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 c-n-f Metadata [17.1 kB]
2026-05-03T01:19:33.9921440Z Get:17 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Packages [1685 kB]
2026-05-03T01:19:34.0007659Z Get:18 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe Translation-en [324 kB]
2026-05-03T01:19:34.0037978Z Get:19 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Components [386 kB]
2026-05-03T01:19:34.0065443Z Get:20 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 c-n-f Metadata [34.5 kB]
2026-05-03T01:19:34.0081811Z Get:21 http://azure.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Packages [3095 kB]
2026-05-03T01:19:34.0246760Z Get:22 http://azure.archive.ubuntu.com/ubuntu noble-updates/restricted Translation-en [715 kB]
2026-05-03T01:19:34.0738054Z Get:23 http://azure.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Components [212 B]
2026-05-03T01:19:34.0750386Z Get:24 http://azure.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 c-n-f Metadata [480 B]
2026-05-03T01:19:34.0761690Z Get:25 http://azure.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Packages [44.4 kB]
2026-05-03T01:19:34.0781498Z Get:26 http://azure.archive.ubuntu.com/ubuntu noble-updates/multiverse Translation-en [10.2 kB]
2026-05-03T01:19:34.0801865Z Get:27 http://azure.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Components [940 B]
2026-05-03T01:19:34.0822774Z Get:28 http://azure.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 c-n-f Metadata [656 B]
2026-05-03T01:19:34.0830445Z Get:29 http://azure.archive.ubuntu.com/ubuntu noble-backports/main amd64 Packages [64.5 kB]
2026-05-03T01:19:34.0860879Z Get:30 http://azure.archive.ubuntu.com/ubuntu noble-backports/main Translation-en [9172 B]
2026-05-03T01:19:34.0866675Z Get:31 http://azure.archive.ubuntu.com/ubuntu noble-backports/main amd64 Components [7368 B]
2026-05-03T01:19:34.0881635Z Get:32 http://azure.archive.ubuntu.com/ubuntu noble-backports/main amd64 c-n-f Metadata [368 B]
2026-05-03T01:19:34.0905270Z Get:33 http://azure.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Packages [34.1 kB]
2026-05-03T01:19:34.0924990Z Get:34 http://azure.archive.ubuntu.com/ubuntu noble-backports/universe Translation-en [18.2 kB]
2026-05-03T01:19:34.0947490Z Get:35 http://azure.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Components [10.5 kB]
2026-05-03T01:19:34.0966376Z Get:36 http://azure.archive.ubuntu.com/ubuntu noble-backports/universe amd64 c-n-f Metadata [1484 B]
2026-05-03T01:19:34.1433528Z Get:37 http://azure.archive.ubuntu.com/ubuntu noble-backports/restricted amd64 Components [212 B]
2026-05-03T01:19:34.1444468Z Get:38 http://azure.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Packages [748 B]
2026-05-03T01:19:34.1452316Z Get:39 http://azure.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Components [212 B]
2026-05-03T01:19:34.1465136Z Get:40 http://azure.archive.ubuntu.com/ubuntu noble-security/main amd64 Packages [1625 kB]
2026-05-03T01:19:34.1574258Z Get:41 http://azure.archive.ubuntu.com/ubuntu noble-security/main Translation-en [259 kB]
2026-05-03T01:19:34.1601778Z Get:42 http://azure.archive.ubuntu.com/ubuntu noble-security/main amd64 Components [21.9 kB]
2026-05-03T01:19:34.1624344Z Get:43 http://azure.archive.ubuntu.com/ubuntu noble-security/main amd64 c-n-f Metadata [11.0 kB]
2026-05-03T01:19:34.1651531Z Get:44 http://azure.archive.ubuntu.com/ubuntu noble-security/universe amd64 Packages [1182 kB]
2026-05-03T01:19:34.1715032Z Get:45 http://azure.archive.ubuntu.com/ubuntu noble-security/universe Translation-en [227 kB]
2026-05-03T01:19:34.1737502Z Get:46 http://azure.archive.ubuntu.com/ubuntu noble-security/universe amd64 Components [74.2 kB]
2026-05-03T01:19:34.1753012Z Get:47 http://azure.archive.ubuntu.com/ubuntu noble-security/universe amd64 c-n-f Metadata [23.1 kB]
2026-05-03T01:19:34.1770148Z Get:48 http://azure.archive.ubuntu.com/ubuntu noble-security/restricted amd64 Packages [2844 kB]
2026-05-03T01:19:34.1917581Z Get:49 http://azure.archive.ubuntu.com/ubuntu noble-security/restricted Translation-en [666 kB]
2026-05-03T01:19:34.1961812Z Get:50 http://azure.archive.ubuntu.com/ubuntu noble-security/restricted amd64 Components [212 B]
2026-05-03T01:19:34.1973050Z Get:51 http://azure.archive.ubuntu.com/ubuntu noble-security/multiverse amd64 Packages [28.8 kB]
2026-05-03T01:19:34.2448640Z Get:52 http://azure.archive.ubuntu.com/ubuntu noble-security/multiverse Translation-en [7172 B]
2026-05-03T01:19:34.2458093Z Get:53 http://azure.archive.ubuntu.com/ubuntu noble-security/multiverse amd64 Components [208 B]
2026-05-03T01:19:41.4509805Z Fetched 16.5 MB in 2s (7908 kB/s)
2026-05-03T01:19:42.2996037Z Reading package lists...
2026-05-03T01:19:42.3376642Z Reading package lists...
2026-05-03T01:19:42.5631297Z Building dependency tree...
2026-05-03T01:19:42.5637443Z Reading state information...
2026-05-03T01:19:42.7617886Z aria2 is already the newest version (1.37.0+debian-1build3).
2026-05-03T01:19:42.7618586Z git is already the newest version (1:2.53.0-0ppa1~ubuntu24.04.1).
2026-05-03T01:19:42.7619136Z git set to manually installed.
2026-05-03T01:19:42.7622624Z automake is already the newest version (1:1.16.5-1.3ubuntu1).
2026-05-03T01:19:42.7623213Z flex is already the newest version (2.6.4-8.2build1).
2026-05-03T01:19:42.7623840Z bison is already the newest version (2:3.8.2+dfsg-1build2).
2026-05-03T01:19:42.7624373Z zip is already the newest version (3.0-13ubuntu0.2).
2026-05-03T01:19:42.7624876Z curl is already the newest version (8.5.0-2ubuntu10.8).
2026-05-03T01:19:42.7625442Z zlib1g-dev is already the newest version (1:1.3.dfsg-3.1ubuntu2.1).
2026-05-03T01:19:42.7626021Z bzip2 is already the newest version (1.0.8-5.1build0.1).
2026-05-03T01:19:42.7626601Z squashfs-tools is already the newest version (1:4.6.1-1build1).
2026-05-03T01:19:42.7627122Z squashfs-tools set to manually installed.
2026-05-03T01:19:42.7627627Z dpkg-dev is already the newest version (1.22.6ubuntu6.5).
2026-05-03T01:19:42.7628183Z make is already the newest version (4.3-4.1build2).
2026-05-03T01:19:42.7628723Z libssl-dev is already the newest version (3.0.13-0ubuntu3.9).
2026-05-03T01:19:42.7629345Z libxml-sax-base-perl is already the newest version (1.09-3).
2026-05-03T01:19:42.7630052Z libxml-sax-base-perl set to manually installed.
2026-05-03T01:19:42.7630688Z libstdc++6 is already the newest version (14.2.0-4ubuntu2~24.04.1).
2026-05-03T01:19:42.7631348Z unzip is already the newest version (6.0-28ubuntu4.1).
2026-05-03T01:19:42.7631892Z gzip is already the newest version (1.12-1ubuntu3.1).
2026-05-03T01:19:42.7632474Z cpio is already the newest version (2.15+dfsg-1ubuntu2).
2026-05-03T01:19:42.7633028Z cpio set to manually installed.
2026-05-03T01:19:42.7633504Z findutils is already the newest version (4.9.0-5build1).
2026-05-03T01:19:42.7634059Z python3 is already the newest version (3.12.3-0ubuntu2.1).
2026-05-03T01:19:42.7634575Z bc is already the newest version (1.07.1-3ubuntu4).
2026-05-03T01:19:42.7634991Z bc set to manually installed.
2026-05-03T01:19:42.7635423Z p7zip-full is already the newest version (16.02+transitional.1).
2026-05-03T01:19:42.7635945Z libyaml-dev is already the newest version (0.2.5-1build1).
2026-05-03T01:19:42.7636431Z The following additional packages will be installed:
2026-05-03T01:19:42.7636982Z   bzip2-doc g++-13-multilib gcc-13-multilib gcc-multilib lib32asan8
2026-05-03T01:19:42.7637658Z   lib32atomic1 lib32gcc-13-dev lib32gcc-s1 lib32gomp1 lib32itm1 lib32ncurses6
2026-05-03T01:19:42.7638334Z   lib32ncursesw6 lib32quadmath0 lib32stdc++-13-dev lib32tinfo6 lib32ubsan1
2026-05-03T01:19:42.7639067Z   lib32z1 libaopalliance-java libapache-pom-java libatinject-jsr330-api-java
2026-05-03T01:19:42.7639996Z   libc6-dev-x32 libc6-i386 libc6-x32 libcdi-api-java libcommons-cli-java
2026-05-03T01:19:42.7640686Z   libcommons-io-java libcommons-lang3-java libcommons-parent-java libegl-dev
2026-05-03T01:19:42.7641336Z   libegl-mesa0 libegl1 liberror-prone-java libfdt1
2026-05-03T01:19:42.7642028Z   libgeronimo-annotation-1.3-spec-java libgeronimo-interceptor-3.0-spec-java
2026-05-03T01:19:42.7643204Z   libgl-dev libgles-dev libgles1 libgles2 libglvnd-core-dev libglvnd-dev
2026-05-03T01:19:42.7643948Z   libglx-dev libguava-java libguice-java libhiredis1.1.0 libjansi-java libjq1
2026-05-03T01:19:42.7646546Z   libjsr305-java libmaven-parent-java libmaven-resolver-java
2026-05-03T01:19:42.7647328Z   libmaven-shared-utils-java libmaven3-core-java libopengl-dev libopengl0
2026-05-03T01:19:42.7648005Z   libplexus-cipher-java libplexus-classworlds-java
2026-05-03T01:19:42.7648675Z   libplexus-component-annotations-java libplexus-interpolation-java
2026-05-03T01:19:42.7649710Z   libplexus-sec-dispatcher-java libplexus-utils2-java libpthread-stubs0-dev
2026-05-03T01:19:42.7650849Z   libsisu-inject-java libsisu-plexus-java libslf4j-java libwagon-file-java
2026-05-03T01:19:42.7651620Z   libwagon-http-shaded-java libwagon-provider-api-java libx32asan8
2026-05-03T01:19:42.7652323Z   libx32atomic1 libx32gcc-13-dev libx32gcc-s1 libx32gomp1 libx32itm1
2026-05-03T01:19:42.7653080Z   libx32quadmath0 libx32stdc++-13-dev libx32stdc++6 libx32ubsan1 libxau-dev
2026-05-03T01:19:42.7653824Z   libxcb1-dev libxdmcp-dev x11proto-dev xorg-sgml-doctools xtrans-dev
2026-05-03T01:19:42.7654382Z Suggested packages:
2026-05-03T01:19:42.7654836Z   distcc | icecc lib32stdc++6-13-dbg libx32stdc++6-13-dbg ncurses-doc
2026-05-03T01:19:42.7655529Z   libatinject-jsr330-api-java-doc libel-api-java libcommons-io-java-doc
2026-05-03T01:19:42.7656305Z   libasm-java libcglib-java libjsr305-java-doc libmaven-shared-utils-java-doc
2026-05-03T01:19:42.7656943Z   liblogback-java libplexus-utils2-java-doc junit4 testng
2026-05-03T01:19:42.7657340Z   libcommons-logging-java liblog4j1.2-java libx11-doc libxcb-doc
2026-05-03T01:19:42.8326064Z The following NEW packages will be installed:
2026-05-03T01:19:42.8326723Z   build-essential bzip2-doc ccache device-tree-compiler g++-13-multilib
2026-05-03T01:19:42.8327486Z   g++-multilib gcc-13-multilib gcc-multilib gperf lib32asan8 lib32atomic1
2026-05-03T01:19:42.8328182Z   lib32gcc-13-dev lib32gcc-s1 lib32gomp1 lib32itm1 lib32ncurses-dev
2026-05-03T01:19:42.8328919Z   lib32ncurses6 lib32ncursesw6 lib32quadmath0 lib32stdc++-13-dev lib32stdc++6
2026-05-03T01:19:42.8329743Z   lib32tinfo6 lib32ubsan1 lib32z1 lib32z1-dev libaopalliance-java
2026-05-03T01:19:42.8330592Z   libapache-pom-java libatinject-jsr330-api-java libbz2-dev libc6-dev-i386
2026-05-03T01:19:42.8331326Z   libc6-dev-x32 libc6-i386 libc6-x32 libcdi-api-java libcommons-cli-java
2026-05-03T01:19:42.8332079Z   libcommons-io-java libcommons-lang3-java libcommons-parent-java libegl-dev
2026-05-03T01:19:42.8332783Z   libegl-mesa0 libegl1 libelf-dev liberror-prone-java libfdt1
2026-05-03T01:19:42.8333491Z   libgeronimo-annotation-1.3-spec-java libgeronimo-interceptor-3.0-spec-java
2026-05-03T01:19:42.8334557Z   libgl-dev libgl1-mesa-dev libgles-dev libgles1 libgles2 libglvnd-core-dev
2026-05-03T01:19:42.8335276Z   libglvnd-dev libglx-dev libguava-java libguice-java libhiredis1.1.0
2026-05-03T01:19:42.8335935Z   libjansi-java libjsr305-java liblz4-tool libmaven-parent-java
2026-05-03T01:19:42.8336636Z   libmaven-resolver-java libmaven-shared-utils-java libmaven3-core-java
2026-05-03T01:19:42.8337315Z   libncurses-dev libopengl-dev libopengl0 libplexus-cipher-java
2026-05-03T01:19:42.8337985Z   libplexus-classworlds-java libplexus-component-annotations-java
2026-05-03T01:19:42.8338654Z   libplexus-interpolation-java libplexus-sec-dispatcher-java
2026-05-03T01:19:42.8339308Z   libplexus-utils2-java libpthread-stubs0-dev libsisu-inject-java
2026-05-03T01:19:42.8340062Z   libsisu-plexus-java libslf4j-java libwagon-file-java
2026-05-03T01:19:42.8340726Z   libwagon-http-shaded-java libwagon-provider-api-java libx11-dev libx32asan8
2026-05-03T01:19:42.8341483Z   libx32atomic1 libx32gcc-13-dev libx32gcc-s1 libx32gomp1 libx32itm1
2026-05-03T01:19:42.8342182Z   libx32quadmath0 libx32stdc++-13-dev libx32stdc++6 libx32ubsan1 libxau-dev
2026-05-03T01:19:42.8342947Z   libxcb1-dev libxdmcp-dev libxml-simple-perl libxml2-utils lzop maven optipng
2026-05-03T01:19:42.8344009Z   pngcrush pwgen schedtool x11proto-dev xorg-sgml-doctools xsltproc xtrans-dev
2026-05-03T01:19:42.8344621Z The following packages will be upgraded:
2026-05-03T01:19:42.8350229Z   jq libjq1
2026-05-03T01:19:42.8562258Z 2 upgraded, 106 newly installed, 0 to remove and 48 not upgraded.
2026-05-03T01:19:42.8562760Z Need to get 41.7 MB of archives.
2026-05-03T01:19:42.8563211Z After this operation, 138 MB of additional disk space will be used.
2026-05-03T01:19:42.8563792Z Get:1 file:/etc/apt/apt-mirrors.txt Mirrorlist [144 B]
2026-05-03T01:19:42.8831837Z Get:2 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 build-essential amd64 12.10ubuntu1 [4928 B]
2026-05-03T01:19:42.8904615Z Get:3 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 bzip2-doc all 1.0.8-5.1build0.1 [499 kB]
2026-05-03T01:19:42.9093245Z Get:4 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libhiredis1.1.0 amd64 1.2.0-6ubuntu3 [41.4 kB]
2026-05-03T01:19:42.9173296Z Get:5 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 ccache amd64 4.9.1-1 [592 kB]
2026-05-03T01:19:42.9365047Z Get:6 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libc6-i386 amd64 2.39-0ubuntu8.7 [2788 kB]
2026-05-03T01:19:43.0121094Z Get:7 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libc6-dev-i386 amd64 2.39-0ubuntu8.7 [1447 kB]
2026-05-03T01:19:43.0542748Z Get:8 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libc6-x32 amd64 2.39-0ubuntu8.7 [2914 kB]
2026-05-03T01:19:43.1371353Z Get:9 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libc6-dev-x32 amd64 2.39-0ubuntu8.7 [1637 kB]
2026-05-03T01:19:43.1835496Z Get:10 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32gcc-s1 amd64 14.2.0-4ubuntu2~24.04.1 [92.3 kB]
2026-05-03T01:19:43.1924114Z Get:11 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32gcc-s1 amd64 14.2.0-4ubuntu2~24.04.1 [78.5 kB]
2026-05-03T01:19:43.2017179Z Get:12 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32gomp1 amd64 14.2.0-4ubuntu2~24.04.1 [141 kB]
2026-05-03T01:19:43.2116884Z Get:13 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32gomp1 amd64 14.2.0-4ubuntu2~24.04.1 [144 kB]
2026-05-03T01:19:43.2239933Z Get:14 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32itm1 amd64 14.2.0-4ubuntu2~24.04.1 [29.5 kB]
2026-05-03T01:19:43.2325401Z Get:15 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32itm1 amd64 14.2.0-4ubuntu2~24.04.1 [29.8 kB]
2026-05-03T01:19:43.2402388Z Get:16 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32atomic1 amd64 14.2.0-4ubuntu2~24.04.1 [8594 B]
2026-05-03T01:19:43.2491362Z Get:17 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32atomic1 amd64 14.2.0-4ubuntu2~24.04.1 [10.3 kB]
2026-05-03T01:19:43.2567562Z Get:18 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32asan8 amd64 14.2.0-4ubuntu2~24.04.1 [2880 kB]
2026-05-03T01:19:43.3351715Z Get:19 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32asan8 amd64 14.2.0-4ubuntu2~24.04.1 [2893 kB]
2026-05-03T01:19:43.4601851Z Get:20 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32stdc++6 amd64 14.2.0-4ubuntu2~24.04.1 [814 kB]
2026-05-03T01:19:43.4867248Z Get:21 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32ubsan1 amd64 14.2.0-4ubuntu2~24.04.1 [1150 kB]
2026-05-03T01:19:43.5210437Z Get:22 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32stdc++6 amd64 14.2.0-4ubuntu2~24.04.1 [778 kB]
2026-05-03T01:19:43.5497445Z Get:23 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32ubsan1 amd64 14.2.0-4ubuntu2~24.04.1 [1169 kB]
2026-05-03T01:19:43.5898503Z Get:24 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32quadmath0 amd64 14.2.0-4ubuntu2~24.04.1 [227 kB]
2026-05-03T01:19:43.6025817Z Get:25 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32quadmath0 amd64 14.2.0-4ubuntu2~24.04.1 [157 kB]
2026-05-03T01:19:43.6132830Z Get:26 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32gcc-13-dev amd64 13.3.0-6ubuntu2~24.04.1 [2380 kB]
2026-05-03T01:19:43.6855514Z Get:27 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32gcc-13-dev amd64 13.3.0-6ubuntu2~24.04.1 [2190 kB]
2026-05-03T01:19:43.7535990Z Get:28 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 gcc-13-multilib amd64 13.3.0-6ubuntu2~24.04.1 [880 B]
2026-05-03T01:19:43.7614174Z Get:29 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32stdc++-13-dev amd64 13.3.0-6ubuntu2~24.04.1 [1150 kB]
2026-05-03T01:19:43.8033838Z Get:30 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32stdc++-13-dev amd64 13.3.0-6ubuntu2~24.04.1 [1086 kB]
2026-05-03T01:19:43.8553773Z Get:31 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 g++-13-multilib amd64 13.3.0-6ubuntu2~24.04.1 [892 B]
2026-05-03T01:19:43.8622104Z Get:32 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 gcc-multilib amd64 4:13.2.0-7ubuntu1 [1474 B]
2026-05-03T01:19:43.8708249Z Get:33 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 g++-multilib amd64 4:13.2.0-7ubuntu1 [884 B]
2026-05-03T01:19:43.8779047Z Get:34 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 gperf amd64 3.1-1build1 [103 kB]
2026-05-03T01:19:43.8891247Z Get:35 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 jq amd64 1.7.1-3ubuntu0.24.04.2 [65.7 kB]
2026-05-03T01:19:43.8993159Z Get:36 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libjq1 amd64 1.7.1-3ubuntu0.24.04.2 [142 kB]
2026-05-03T01:19:43.9105735Z Get:37 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 lib32tinfo6 amd64 6.4+20240113-1ubuntu2 [105 kB]
2026-05-03T01:19:43.9211389Z Get:38 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 lib32ncurses6 amd64 6.4+20240113-1ubuntu2 [113 kB]
2026-05-03T01:19:43.9797304Z Get:39 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 lib32ncursesw6 amd64 6.4+20240113-1ubuntu2 [153 kB]
2026-05-03T01:19:43.9921599Z Get:40 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libncurses-dev amd64 6.4+20240113-1ubuntu2 [384 kB]
2026-05-03T01:19:44.0164371Z Get:41 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 lib32ncurses-dev amd64 6.4+20240113-1ubuntu2 [344 kB]
2026-05-03T01:19:44.0373395Z Get:42 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32z1 amd64 1:1.3.dfsg-3.1ubuntu2.1 [57.4 kB]
2026-05-03T01:19:44.0476554Z Get:43 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32z1-dev amd64 1:1.3.dfsg-3.1ubuntu2.1 [56.4 kB]
2026-05-03T01:19:44.0577643Z Get:44 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libapache-pom-java all 29-2 [5284 B]
2026-05-03T01:19:44.0653873Z Get:45 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libatinject-jsr330-api-java all 1.0+ds1-5 [5348 B]
2026-05-03T01:19:44.0736098Z Get:46 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libbz2-dev amd64 1.0.8-5.1build0.1 [33.6 kB]
2026-05-03T01:19:44.0848359Z Get:47 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libgeronimo-interceptor-3.0-spec-java all 1.0.1-4fakesync [8616 B]
2026-05-03T01:19:44.0928419Z Get:48 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libcdi-api-java all 1.2-3 [54.3 kB]
2026-05-03T01:19:44.1029941Z Get:49 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libcommons-cli-java all 1.6.0-1 [59.9 kB]
2026-05-03T01:19:44.1137879Z Get:50 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libcommons-parent-java all 56-1 [10.7 kB]
2026-05-03T01:19:44.1224456Z Get:51 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libcommons-io-java all 2.11.0-2 [297 kB]
2026-05-03T01:19:44.1467216Z Get:52 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libcommons-lang3-java all 3.14.0-1 [586 kB]
2026-05-03T01:19:44.1865606Z Get:53 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libegl-mesa0 amd64 25.2.8-0ubuntu0.24.04.1 [117 kB]
2026-05-03T01:19:44.1999066Z Get:54 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libegl1 amd64 1.7.0-1build1 [28.7 kB]
2026-05-03T01:19:44.2079700Z Get:55 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 xorg-sgml-doctools all 1:1.11-1.1 [10.9 kB]
2026-05-03T01:19:44.2176068Z Get:56 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 x11proto-dev all 2023.2-1 [602 kB]
2026-05-03T01:19:44.2923822Z Get:57 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libxau-dev amd64 1:1.0.9-1build6 [9570 B]
2026-05-03T01:19:44.3032636Z Get:58 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libxdmcp-dev amd64 1:1.1.3-0ubuntu6 [26.5 kB]
2026-05-03T01:19:44.3125942Z Get:59 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 xtrans-dev all 1.4.0-1 [68.9 kB]
2026-05-03T01:19:44.3262089Z Get:60 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libpthread-stubs0-dev amd64 0.4-1build3 [4746 B]
2026-05-03T01:19:44.3345717Z Get:61 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libxcb1-dev amd64 1.15-1ubuntu2 [85.8 kB]
2026-05-03T01:19:44.3465963Z Get:62 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libx11-dev amd64 2:1.8.7-1build1 [732 kB]
2026-05-03T01:19:44.3950037Z Get:63 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libglx-dev amd64 1.7.0-1build1 [14.2 kB]
2026-05-03T01:19:44.4036275Z Get:64 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libgl-dev amd64 1.7.0-1build1 [102 kB]
2026-05-03T01:19:44.4169169Z Get:65 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libegl-dev amd64 1.7.0-1build1 [18.2 kB]
2026-05-03T01:19:44.4265465Z Get:66 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libelf-dev amd64 0.190-1.1ubuntu0.1 [68.5 kB]
2026-05-03T01:19:44.4361791Z Get:67 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libjsr305-java all 0.1~+svn49-11 [27.0 kB]
2026-05-03T01:19:44.4488396Z Get:68 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libguava-java all 32.0.1-1 [2692 kB]
2026-05-03T01:19:44.5570381Z Get:69 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 liberror-prone-java all 2.18.0-1 [22.5 kB]
2026-05-03T01:19:44.5651536Z Get:70 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libgeronimo-annotation-1.3-spec-java all 1.3-1 [11.2 kB]
2026-05-03T01:19:44.5726435Z Get:71 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libgles1 amd64 1.7.0-1build1 [11.6 kB]
2026-05-03T01:19:44.5802266Z Get:72 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libgles2 amd64 1.7.0-1build1 [17.1 kB]
2026-05-03T01:19:44.5882513Z Get:73 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libgles-dev amd64 1.7.0-1build1 [50.5 kB]
2026-05-03T01:19:44.5978314Z Get:74 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libaopalliance-java all 20070526-7 [8166 B]
2026-05-03T01:19:44.6053969Z Get:75 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libguice-java all 4.2.3-2 [1434 kB]
2026-05-03T01:19:44.6958730Z Get:76 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libjansi-java all 2.4.1-2 [83.0 kB]
2026-05-03T01:19:44.7051818Z Get:77 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libmaven-parent-java all 35-1 [5810 B]
2026-05-03T01:19:44.7143436Z Get:78 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libplexus-utils2-java all 3.4.2-1 [256 kB]
2026-05-03T01:19:44.7282246Z Get:79 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libwagon-provider-api-java all 3.5.3-1 [47.9 kB]
2026-05-03T01:19:44.7368195Z Get:80 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libmaven-resolver-java all 1.6.3-1 [544 kB]
2026-05-03T01:19:44.7576729Z Get:81 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libmaven-shared-utils-java all 3.3.4-1 [137 kB]
2026-05-03T01:19:44.7685795Z Get:82 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libplexus-cipher-java all 2.0-1 [14.7 kB]
2026-05-03T01:19:44.7763806Z Get:83 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libplexus-classworlds-java all 2.7.0-1 [50.0 kB]
2026-05-03T01:19:44.7852408Z Get:84 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libplexus-component-annotations-java all 2.1.1-1 [6550 B]
2026-05-03T01:19:44.7925806Z Get:85 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libplexus-interpolation-java all 1.26-1 [76.8 kB]
2026-05-03T01:19:44.8018872Z Get:86 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libplexus-sec-dispatcher-java all 2.0-3 [28.1 kB]
2026-05-03T01:19:44.8096441Z Get:87 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libslf4j-java all 1.7.32-1 [141 kB]
2026-05-03T01:19:44.8216782Z Get:88 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libsisu-inject-java all 0.3.4-2 [347 kB]
2026-05-03T01:19:44.8371674Z Get:89 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libsisu-plexus-java all 0.3.4-3 [181 kB]
2026-05-03T01:19:44.8487611Z Get:90 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libmaven3-core-java all 3.8.7-2 [1565 kB]
2026-05-03T01:19:44.8949266Z Get:91 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libopengl0 amd64 1.7.0-1build1 [32.8 kB]
2026-05-03T01:19:44.9032025Z Get:92 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libopengl-dev amd64 1.7.0-1build1 [3454 B]
2026-05-03T01:19:44.9109088Z Get:93 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libwagon-file-java all 3.5.3-1 [7918 B]
2026-05-03T01:19:44.9601739Z Get:94 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libwagon-http-shaded-java all 3.5.3-1 [1332 kB]
2026-05-03T01:19:45.0073146Z Get:95 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libxml-simple-perl all 2.25-2 [64.1 kB]
2026-05-03T01:19:45.0163118Z Get:96 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libxml2-utils amd64 2.9.14+dfsg-1.3ubuntu3.7 [39.4 kB]
2026-05-03T01:19:45.0247772Z Get:97 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 lzop amd64 1.04-2build3 [82.2 kB]
2026-05-03T01:19:45.0339080Z Get:98 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 maven all 3.8.7-2 [18.3 kB]
2026-05-03T01:19:45.0447590Z Get:99 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 optipng amd64 0.7.8+ds-1build2 [110 kB]
2026-05-03T01:19:45.0554734Z Get:100 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 pngcrush amd64 1.8.13-1build2 [49.5 kB]
2026-05-03T01:19:45.0662679Z Get:101 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 pwgen amd64 2.08-2build2 [17.2 kB]
2026-05-03T01:19:45.0742577Z Get:102 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 xsltproc amd64 1.1.39-0exp1ubuntu0.24.04.3 [15.0 kB]
2026-05-03T01:19:45.0845177Z Get:103 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libfdt1 amd64 1.7.0-2build1 [20.1 kB]
2026-05-03T01:19:45.0960495Z Get:104 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 device-tree-compiler amd64 1.7.0-2build1 [228 kB]
2026-05-03T01:19:45.1064402Z Get:105 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libglvnd-core-dev amd64 1.7.0-1build1 [13.6 kB]
2026-05-03T01:19:45.1155430Z Get:106 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libglvnd-dev amd64 1.7.0-1build1 [3198 B]
2026-05-03T01:19:45.1236941Z Get:107 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libgl1-mesa-dev amd64 25.2.8-0ubuntu0.24.04.1 [22.5 kB]
2026-05-03T01:19:45.1321739Z Get:108 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 liblz4-tool all 1.9.4-1build1.1 [2484 B]
2026-05-03T01:19:45.1392282Z Get:109 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 schedtool amd64 1.3.0-4 [22.0 kB]
2026-05-03T01:19:45.4844583Z Fetched 41.7 MB in 2s (18.1 MB/s)
2026-05-03T01:19:45.5046968Z Selecting previously unselected package build-essential.
2026-05-03T01:19:45.5101037Z (Reading database ... 
2026-05-03T01:19:45.5101892Z (Reading database ... 5%
2026-05-03T01:19:45.5102306Z (Reading database ... 10%
2026-05-03T01:19:45.5102676Z (Reading database ... 15%
2026-05-03T01:19:45.5103002Z (Reading database ... 20%
2026-05-03T01:19:45.5103392Z (Reading database ... 25%
2026-05-03T01:19:45.5104021Z (Reading database ... 30%
2026-05-03T01:19:45.5104248Z (Reading database ... 35%
2026-05-03T01:19:45.5104456Z (Reading database ... 40%
2026-05-03T01:19:45.5104666Z (Reading database ... 45%
2026-05-03T01:19:45.5104876Z (Reading database ... 50%
2026-05-03T01:19:45.5105079Z (Reading database ... 55%
2026-05-03T01:19:45.5133440Z (Reading database ... 60%
2026-05-03T01:19:45.5225352Z (Reading database ... 65%
2026-05-03T01:19:45.5254240Z (Reading database ... 70%
2026-05-03T01:19:45.5273402Z (Reading database ... 75%
2026-05-03T01:19:45.5322774Z (Reading database ... 80%
2026-05-03T01:19:45.5351951Z (Reading database ... 85%
2026-05-03T01:19:45.5379011Z (Reading database ... 90%
2026-05-03T01:19:45.5489662Z (Reading database ... 95%
2026-05-03T01:19:45.5490254Z (Reading database ... 100%
2026-05-03T01:19:45.5490589Z (Reading database ... 119905 files and directories currently installed.)
2026-05-03T01:19:45.5516214Z Preparing to unpack .../000-build-essential_12.10ubuntu1_amd64.deb ...
2026-05-03T01:19:45.5525594Z Unpacking build-essential (12.10ubuntu1) ...
2026-05-03T01:19:45.5703585Z Selecting previously unselected package bzip2-doc.
2026-05-03T01:19:45.5781865Z Preparing to unpack .../001-bzip2-doc_1.0.8-5.1build0.1_all.deb ...
2026-05-03T01:19:45.5788709Z Unpacking bzip2-doc (1.0.8-5.1build0.1) ...
2026-05-03T01:19:45.6002410Z Selecting previously unselected package libhiredis1.1.0:amd64.
2026-05-03T01:19:45.6081661Z Preparing to unpack .../002-libhiredis1.1.0_1.2.0-6ubuntu3_amd64.deb ...
2026-05-03T01:19:45.6093985Z Unpacking libhiredis1.1.0:amd64 (1.2.0-6ubuntu3) ...
2026-05-03T01:19:45.6280862Z Selecting previously unselected package ccache.
2026-05-03T01:19:45.6358624Z Preparing to unpack .../003-ccache_4.9.1-1_amd64.deb ...
2026-05-03T01:19:45.6366577Z Unpacking ccache (4.9.1-1) ...
2026-05-03T01:19:45.6645646Z Selecting previously unselected package libc6-i386.
2026-05-03T01:19:45.6725300Z Preparing to unpack .../004-libc6-i386_2.39-0ubuntu8.7_amd64.deb ...
2026-05-03T01:19:45.6750741Z Unpacking libc6-i386 (2.39-0ubuntu8.7) ...
2026-05-03T01:19:45.7690276Z Selecting previously unselected package libc6-dev-i386.
2026-05-03T01:19:45.7771990Z Preparing to unpack .../005-libc6-dev-i386_2.39-0ubuntu8.7_amd64.deb ...
2026-05-03T01:19:45.7778460Z Unpacking libc6-dev-i386 (2.39-0ubuntu8.7) ...
2026-05-03T01:19:45.8406944Z Selecting previously unselected package libc6-x32.
2026-05-03T01:19:45.8488923Z Preparing to unpack .../006-libc6-x32_2.39-0ubuntu8.7_amd64.deb ...
2026-05-03T01:19:45.8522569Z Unpacking libc6-x32 (2.39-0ubuntu8.7) ...
2026-05-03T01:19:45.9470386Z Selecting previously unselected package libc6-dev-x32.
2026-05-03T01:19:45.9552739Z Preparing to unpack .../007-libc6-dev-x32_2.39-0ubuntu8.7_amd64.deb ...
2026-05-03T01:19:45.9559008Z Unpacking libc6-dev-x32 (2.39-0ubuntu8.7) ...
2026-05-03T01:19:46.0024158Z Selecting previously unselected package lib32gcc-s1.
2026-05-03T01:19:46.0105858Z Preparing to unpack .../008-lib32gcc-s1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.0113247Z Unpacking lib32gcc-s1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:46.0294273Z Selecting previously unselected package libx32gcc-s1.
2026-05-03T01:19:46.0371719Z Preparing to unpack .../009-libx32gcc-s1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.0378741Z Unpacking libx32gcc-s1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:46.0559864Z Selecting previously unselected package lib32gomp1.
2026-05-03T01:19:46.0636969Z Preparing to unpack .../010-lib32gomp1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.0645163Z Unpacking lib32gomp1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:46.0830549Z Selecting previously unselected package libx32gomp1.
2026-05-03T01:19:46.0908235Z Preparing to unpack .../011-libx32gomp1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.0915609Z Unpacking libx32gomp1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:46.1107370Z Selecting previously unselected package lib32itm1.
2026-05-03T01:19:46.1185465Z Preparing to unpack .../012-lib32itm1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.1193093Z Unpacking lib32itm1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:46.1368001Z Selecting previously unselected package libx32itm1.
2026-05-03T01:19:46.1443648Z Preparing to unpack .../013-libx32itm1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.1451345Z Unpacking libx32itm1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:46.1624830Z Selecting previously unselected package lib32atomic1.
2026-05-03T01:19:46.1700135Z Preparing to unpack .../014-lib32atomic1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.1707539Z Unpacking lib32atomic1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:46.1878949Z Selecting previously unselected package libx32atomic1.
2026-05-03T01:19:46.1954862Z Preparing to unpack .../015-libx32atomic1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.1961930Z Unpacking libx32atomic1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:46.2135590Z Selecting previously unselected package lib32asan8.
2026-05-03T01:19:46.2212269Z Preparing to unpack .../016-lib32asan8_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.2221388Z Unpacking lib32asan8 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:46.2779120Z Selecting previously unselected package libx32asan8.
2026-05-03T01:19:46.2861056Z Preparing to unpack .../017-libx32asan8_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.2869998Z Unpacking libx32asan8 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:46.3446194Z Selecting previously unselected package lib32stdc++6.
2026-05-03T01:19:46.3528951Z Preparing to unpack .../018-lib32stdc++6_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.3535869Z Unpacking lib32stdc++6 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:46.3811346Z Selecting previously unselected package lib32ubsan1.
2026-05-03T01:19:46.3894584Z Preparing to unpack .../019-lib32ubsan1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.3903309Z Unpacking lib32ubsan1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:46.4247407Z Selecting previously unselected package libx32stdc++6.
2026-05-03T01:19:46.4329847Z Preparing to unpack .../020-libx32stdc++6_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.4336379Z Unpacking libx32stdc++6 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:46.4600542Z Selecting previously unselected package libx32ubsan1.
2026-05-03T01:19:46.4682032Z Preparing to unpack .../021-libx32ubsan1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.4689893Z Unpacking libx32ubsan1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:46.5002985Z Selecting previously unselected package lib32quadmath0.
2026-05-03T01:19:46.5085917Z Preparing to unpack .../022-lib32quadmath0_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.5093824Z Unpacking lib32quadmath0 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:46.5297286Z Selecting previously unselected package libx32quadmath0.
2026-05-03T01:19:46.5379079Z Preparing to unpack .../023-libx32quadmath0_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.5385808Z Unpacking libx32quadmath0 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:46.5566500Z Selecting previously unselected package lib32gcc-13-dev.
2026-05-03T01:19:46.5647223Z Preparing to unpack .../024-lib32gcc-13-dev_13.3.0-6ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.5653765Z Unpacking lib32gcc-13-dev (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T01:19:46.6118942Z Selecting previously unselected package libx32gcc-13-dev.
2026-05-03T01:19:46.6200573Z Preparing to unpack .../025-libx32gcc-13-dev_13.3.0-6ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.6206562Z Unpacking libx32gcc-13-dev (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T01:19:46.6632284Z Selecting previously unselected package gcc-13-multilib.
2026-05-03T01:19:46.6714251Z Preparing to unpack .../026-gcc-13-multilib_13.3.0-6ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.6721212Z Unpacking gcc-13-multilib (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T01:19:46.6884489Z Selecting previously unselected package lib32stdc++-13-dev.
2026-05-03T01:19:46.6966773Z Preparing to unpack .../027-lib32stdc++-13-dev_13.3.0-6ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.6973643Z Unpacking lib32stdc++-13-dev (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T01:19:46.7543520Z Selecting previously unselected package libx32stdc++-13-dev.
2026-05-03T01:19:46.7626257Z Preparing to unpack .../028-libx32stdc++-13-dev_13.3.0-6ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.7633884Z Unpacking libx32stdc++-13-dev (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T01:19:46.8053909Z Selecting previously unselected package g++-13-multilib.
2026-05-03T01:19:46.8136146Z Preparing to unpack .../029-g++-13-multilib_13.3.0-6ubuntu2~24.04.1_amd64.deb ...
2026-05-03T01:19:46.8143099Z Unpacking g++-13-multilib (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T01:19:46.8307096Z Selecting previously unselected package gcc-multilib.
2026-05-03T01:19:46.8390059Z Preparing to unpack .../030-gcc-multilib_4%3a13.2.0-7ubuntu1_amd64.deb ...
2026-05-03T01:19:46.8397143Z Unpacking gcc-multilib (4:13.2.0-7ubuntu1) ...
2026-05-03T01:19:46.8560552Z Selecting previously unselected package g++-multilib.
2026-05-03T01:19:46.8640751Z Preparing to unpack .../031-g++-multilib_4%3a13.2.0-7ubuntu1_amd64.deb ...
2026-05-03T01:19:46.8648296Z Unpacking g++-multilib (4:13.2.0-7ubuntu1) ...
2026-05-03T01:19:46.8811989Z Selecting previously unselected package gperf.
2026-05-03T01:19:46.8893671Z Preparing to unpack .../032-gperf_3.1-1build1_amd64.deb ...
2026-05-03T01:19:46.8902129Z Unpacking gperf (3.1-1build1) ...
2026-05-03T01:19:46.9222898Z Preparing to unpack .../033-jq_1.7.1-3ubuntu0.24.04.2_amd64.deb ...
2026-05-03T01:19:46.9240009Z Unpacking jq (1.7.1-3ubuntu0.24.04.2) over (1.7.1-3ubuntu0.24.04.1) ...
2026-05-03T01:19:46.9627126Z Preparing to unpack .../034-libjq1_1.7.1-3ubuntu0.24.04.2_amd64.deb ...
2026-05-03T01:19:46.9647158Z Unpacking libjq1:amd64 (1.7.1-3ubuntu0.24.04.2) over (1.7.1-3ubuntu0.24.04.1) ...
2026-05-03T01:19:46.9860701Z Selecting previously unselected package lib32tinfo6.
2026-05-03T01:19:46.9944822Z Preparing to unpack .../035-lib32tinfo6_6.4+20240113-1ubuntu2_amd64.deb ...
2026-05-03T01:19:46.9952598Z Unpacking lib32tinfo6 (6.4+20240113-1ubuntu2) ...
2026-05-03T01:19:47.0152582Z Selecting previously unselected package lib32ncurses6.
2026-05-03T01:19:47.0234718Z Preparing to unpack .../036-lib32ncurses6_6.4+20240113-1ubuntu2_amd64.deb ...
2026-05-03T01:19:47.0241967Z Unpacking lib32ncurses6 (6.4+20240113-1ubuntu2) ...
2026-05-03T01:19:47.0442340Z Selecting previously unselected package lib32ncursesw6.
2026-05-03T01:19:47.0525845Z Preparing to unpack .../037-lib32ncursesw6_6.4+20240113-1ubuntu2_amd64.deb ...
2026-05-03T01:19:47.0535118Z Unpacking lib32ncursesw6 (6.4+20240113-1ubuntu2) ...
2026-05-03T01:19:47.0730354Z Selecting previously unselected package libncurses-dev:amd64.
2026-05-03T01:19:47.0812639Z Preparing to unpack .../038-libncurses-dev_6.4+20240113-1ubuntu2_amd64.deb ...
2026-05-03T01:19:47.0819710Z Unpacking libncurses-dev:amd64 (6.4+20240113-1ubuntu2) ...
2026-05-03T01:19:47.1156222Z Selecting previously unselected package lib32ncurses-dev.
2026-05-03T01:19:47.1239197Z Preparing to unpack .../039-lib32ncurses-dev_6.4+20240113-1ubuntu2_amd64.deb ...
2026-05-03T01:19:47.1247828Z Unpacking lib32ncurses-dev (6.4+20240113-1ubuntu2) ...
2026-05-03T01:19:47.1517204Z Selecting previously unselected package lib32z1.
2026-05-03T01:19:47.1600738Z Preparing to unpack .../040-lib32z1_1%3a1.3.dfsg-3.1ubuntu2.1_amd64.deb ...
2026-05-03T01:19:47.1608045Z Unpacking lib32z1 (1:1.3.dfsg-3.1ubuntu2.1) ...
2026-05-03T01:19:47.1784279Z Selecting previously unselected package lib32z1-dev.
2026-05-03T01:19:47.1866098Z Preparing to unpack .../041-lib32z1-dev_1%3a1.3.dfsg-3.1ubuntu2.1_amd64.deb ...
2026-05-03T01:19:47.1873507Z Unpacking lib32z1-dev (1:1.3.dfsg-3.1ubuntu2.1) ...
2026-05-03T01:19:47.2054683Z Selecting previously unselected package libapache-pom-java.
2026-05-03T01:19:47.2136855Z Preparing to unpack .../042-libapache-pom-java_29-2_all.deb ...
2026-05-03T01:19:47.2143452Z Unpacking libapache-pom-java (29-2) ...
2026-05-03T01:19:47.2420310Z Selecting previously unselected package libatinject-jsr330-api-java.
2026-05-03T01:19:47.2503367Z Preparing to unpack .../043-libatinject-jsr330-api-java_1.0+ds1-5_all.deb ...
2026-05-03T01:19:47.2510209Z Unpacking libatinject-jsr330-api-java (1.0+ds1-5) ...
2026-05-03T01:19:47.2744703Z Selecting previously unselected package libbz2-dev:amd64.
2026-05-03T01:19:47.2826655Z Preparing to unpack .../044-libbz2-dev_1.0.8-5.1build0.1_amd64.deb ...
2026-05-03T01:19:47.2833154Z Unpacking libbz2-dev:amd64 (1.0.8-5.1build0.1) ...
2026-05-03T01:19:47.3008014Z Selecting previously unselected package libgeronimo-interceptor-3.0-spec-java.
2026-05-03T01:19:47.3090441Z Preparing to unpack .../045-libgeronimo-interceptor-3.0-spec-java_1.0.1-4fakesync_all.deb ...
2026-05-03T01:19:47.3097460Z Unpacking libgeronimo-interceptor-3.0-spec-java (1.0.1-4fakesync) ...
2026-05-03T01:19:47.3295584Z Selecting previously unselected package libcdi-api-java.
2026-05-03T01:19:47.3378783Z Preparing to unpack .../046-libcdi-api-java_1.2-3_all.deb ...
2026-05-03T01:19:47.3386820Z Unpacking libcdi-api-java (1.2-3) ...
2026-05-03T01:19:47.3608581Z Selecting previously unselected package libcommons-cli-java.
2026-05-03T01:19:47.3691665Z Preparing to unpack .../047-libcommons-cli-java_1.6.0-1_all.deb ...
2026-05-03T01:19:47.3699626Z Unpacking libcommons-cli-java (1.6.0-1) ...
2026-05-03T01:19:47.3885054Z Selecting previously unselected package libcommons-parent-java.
2026-05-03T01:19:47.3967070Z Preparing to unpack .../048-libcommons-parent-java_56-1_all.deb ...
2026-05-03T01:19:47.3974105Z Unpacking libcommons-parent-java (56-1) ...
2026-05-03T01:19:47.4162782Z Selecting previously unselected package libcommons-io-java.
2026-05-03T01:19:47.4244732Z Preparing to unpack .../049-libcommons-io-java_2.11.0-2_all.deb ...
2026-05-03T01:19:47.4251590Z Unpacking libcommons-io-java (2.11.0-2) ...
2026-05-03T01:19:47.4443723Z Selecting previously unselected package libcommons-lang3-java.
2026-05-03T01:19:47.4524310Z Preparing to unpack .../050-libcommons-lang3-java_3.14.0-1_all.deb ...
2026-05-03T01:19:47.4532307Z Unpacking libcommons-lang3-java (3.14.0-1) ...
2026-05-03T01:19:47.4743525Z Selecting previously unselected package libegl-mesa0:amd64.
2026-05-03T01:19:47.4824763Z Preparing to unpack .../051-libegl-mesa0_25.2.8-0ubuntu0.24.04.1_amd64.deb ...
2026-05-03T01:19:47.4832468Z Unpacking libegl-mesa0:amd64 (25.2.8-0ubuntu0.24.04.1) ...
2026-05-03T01:19:47.5034281Z Selecting previously unselected package libegl1:amd64.
2026-05-03T01:19:47.5115174Z Preparing to unpack .../052-libegl1_1.7.0-1build1_amd64.deb ...
2026-05-03T01:19:47.5122195Z Unpacking libegl1:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:47.5302610Z Selecting previously unselected package xorg-sgml-doctools.
2026-05-03T01:19:47.5384033Z Preparing to unpack .../053-xorg-sgml-doctools_1%3a1.11-1.1_all.deb ...
2026-05-03T01:19:47.5391364Z Unpacking xorg-sgml-doctools (1:1.11-1.1) ...
2026-05-03T01:19:47.5642336Z Selecting previously unselected package x11proto-dev.
2026-05-03T01:19:47.5725595Z Preparing to unpack .../054-x11proto-dev_2023.2-1_all.deb ...
2026-05-03T01:19:47.5732599Z Unpacking x11proto-dev (2023.2-1) ...
2026-05-03T01:19:47.6227652Z Selecting previously unselected package libxau-dev:amd64.
2026-05-03T01:19:47.6311519Z Preparing to unpack .../055-libxau-dev_1%3a1.0.9-1build6_amd64.deb ...
2026-05-03T01:19:47.6318948Z Unpacking libxau-dev:amd64 (1:1.0.9-1build6) ...
2026-05-03T01:19:47.6504721Z Selecting previously unselected package libxdmcp-dev:amd64.
2026-05-03T01:19:47.6586229Z Preparing to unpack .../056-libxdmcp-dev_1%3a1.1.3-0ubuntu6_amd64.deb ...
2026-05-03T01:19:47.6593227Z Unpacking libxdmcp-dev:amd64 (1:1.1.3-0ubuntu6) ...
2026-05-03T01:19:47.6771505Z Selecting previously unselected package xtrans-dev.
2026-05-03T01:19:47.6852622Z Preparing to unpack .../057-xtrans-dev_1.4.0-1_all.deb ...
2026-05-03T01:19:47.6859224Z Unpacking xtrans-dev (1.4.0-1) ...
2026-05-03T01:19:47.7080733Z Selecting previously unselected package libpthread-stubs0-dev:amd64.
2026-05-03T01:19:47.7163246Z Preparing to unpack .../058-libpthread-stubs0-dev_0.4-1build3_amd64.deb ...
2026-05-03T01:19:47.7170996Z Unpacking libpthread-stubs0-dev:amd64 (0.4-1build3) ...
2026-05-03T01:19:47.7345755Z Selecting previously unselected package libxcb1-dev:amd64.
2026-05-03T01:19:47.7428149Z Preparing to unpack .../059-libxcb1-dev_1.15-1ubuntu2_amd64.deb ...
2026-05-03T01:19:47.7434691Z Unpacking libxcb1-dev:amd64 (1.15-1ubuntu2) ...
2026-05-03T01:19:47.7639000Z Selecting previously unselected package libx11-dev:amd64.
2026-05-03T01:19:47.7721882Z Preparing to unpack .../060-libx11-dev_2%3a1.8.7-1build1_amd64.deb ...
2026-05-03T01:19:47.7728716Z Unpacking libx11-dev:amd64 (2:1.8.7-1build1) ...
2026-05-03T01:19:47.8010259Z Selecting previously unselected package libglx-dev:amd64.
2026-05-03T01:19:47.8093784Z Preparing to unpack .../061-libglx-dev_1.7.0-1build1_amd64.deb ...
2026-05-03T01:19:47.8100179Z Unpacking libglx-dev:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:47.8281019Z Selecting previously unselected package libgl-dev:amd64.
2026-05-03T01:19:47.8363198Z Preparing to unpack .../062-libgl-dev_1.7.0-1build1_amd64.deb ...
2026-05-03T01:19:47.8369943Z Unpacking libgl-dev:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:47.8586958Z Selecting previously unselected package libegl-dev:amd64.
2026-05-03T01:19:47.8668509Z Preparing to unpack .../063-libegl-dev_1.7.0-1build1_amd64.deb ...
2026-05-03T01:19:47.8675373Z Unpacking libegl-dev:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:47.8856400Z Selecting previously unselected package libelf-dev:amd64.
2026-05-03T01:19:47.8938238Z Preparing to unpack .../064-libelf-dev_0.190-1.1ubuntu0.1_amd64.deb ...
2026-05-03T01:19:47.8945032Z Unpacking libelf-dev:amd64 (0.190-1.1ubuntu0.1) ...
2026-05-03T01:19:47.9148012Z Selecting previously unselected package libjsr305-java.
2026-05-03T01:19:47.9230313Z Preparing to unpack .../065-libjsr305-java_0.1~+svn49-11_all.deb ...
2026-05-03T01:19:47.9237096Z Unpacking libjsr305-java (0.1~+svn49-11) ...
2026-05-03T01:19:47.9453643Z Selecting previously unselected package libguava-java.
2026-05-03T01:19:47.9535505Z Preparing to unpack .../066-libguava-java_32.0.1-1_all.deb ...
2026-05-03T01:19:47.9542020Z Unpacking libguava-java (32.0.1-1) ...
2026-05-03T01:19:47.9811763Z Selecting previously unselected package liberror-prone-java.
2026-05-03T01:19:47.9894192Z Preparing to unpack .../067-liberror-prone-java_2.18.0-1_all.deb ...
2026-05-03T01:19:47.9901459Z Unpacking liberror-prone-java (2.18.0-1) ...
2026-05-03T01:19:48.0122501Z Selecting previously unselected package libgeronimo-annotation-1.3-spec-java.
2026-05-03T01:19:48.0205108Z Preparing to unpack .../068-libgeronimo-annotation-1.3-spec-java_1.3-1_all.deb ...
2026-05-03T01:19:48.0212491Z Unpacking libgeronimo-annotation-1.3-spec-java (1.3-1) ...
2026-05-03T01:19:48.0418362Z Selecting previously unselected package libgles1:amd64.
2026-05-03T01:19:48.0500479Z Preparing to unpack .../069-libgles1_1.7.0-1build1_amd64.deb ...
2026-05-03T01:19:48.0508062Z Unpacking libgles1:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:48.0697603Z Selecting previously unselected package libgles2:amd64.
2026-05-03T01:19:48.0780312Z Preparing to unpack .../070-libgles2_1.7.0-1build1_amd64.deb ...
2026-05-03T01:19:48.0788001Z Unpacking libgles2:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:48.0969636Z Selecting previously unselected package libgles-dev:amd64.
2026-05-03T01:19:48.1052093Z Preparing to unpack .../071-libgles-dev_1.7.0-1build1_amd64.deb ...
2026-05-03T01:19:48.1060364Z Unpacking libgles-dev:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:48.1276893Z Selecting previously unselected package libaopalliance-java.
2026-05-03T01:19:48.1359034Z Preparing to unpack .../072-libaopalliance-java_20070526-7_all.deb ...
2026-05-03T01:19:48.1366690Z Unpacking libaopalliance-java (20070526-7) ...
2026-05-03T01:19:48.1545555Z Selecting previously unselected package libguice-java.
2026-05-03T01:19:48.1626787Z Preparing to unpack .../073-libguice-java_4.2.3-2_all.deb ...
2026-05-03T01:19:48.1633658Z Unpacking libguice-java (4.2.3-2) ...
2026-05-03T01:19:48.2844632Z Selecting previously unselected package libjansi-java.
2026-05-03T01:19:48.2928044Z Preparing to unpack .../074-libjansi-java_2.4.1-2_all.deb ...
2026-05-03T01:19:48.2935851Z Unpacking libjansi-java (2.4.1-2) ...
2026-05-03T01:19:48.3123424Z Selecting previously unselected package libmaven-parent-java.
2026-05-03T01:19:48.3206440Z Preparing to unpack .../075-libmaven-parent-java_35-1_all.deb ...
2026-05-03T01:19:48.3213548Z Unpacking libmaven-parent-java (35-1) ...
2026-05-03T01:19:48.3427342Z Selecting previously unselected package libplexus-utils2-java.
2026-05-03T01:19:48.3511227Z Preparing to unpack .../076-libplexus-utils2-java_3.4.2-1_all.deb ...
2026-05-03T01:19:48.3517065Z Unpacking libplexus-utils2-java (3.4.2-1) ...
2026-05-03T01:19:48.3717198Z Selecting previously unselected package libwagon-provider-api-java.
2026-05-03T01:19:48.3800109Z Preparing to unpack .../077-libwagon-provider-api-java_3.5.3-1_all.deb ...
2026-05-03T01:19:48.3807847Z Unpacking libwagon-provider-api-java (3.5.3-1) ...
2026-05-03T01:19:48.4005489Z Selecting previously unselected package libmaven-resolver-java.
2026-05-03T01:19:48.4088707Z Preparing to unpack .../078-libmaven-resolver-java_1.6.3-1_all.deb ...
2026-05-03T01:19:48.4095887Z Unpacking libmaven-resolver-java (1.6.3-1) ...
2026-05-03T01:19:48.4389666Z Selecting previously unselected package libmaven-shared-utils-java.
2026-05-03T01:19:48.4474702Z Preparing to unpack .../079-libmaven-shared-utils-java_3.3.4-1_all.deb ...
2026-05-03T01:19:48.4481966Z Unpacking libmaven-shared-utils-java (3.3.4-1) ...
2026-05-03T01:19:48.4822483Z Selecting previously unselected package libplexus-cipher-java.
2026-05-03T01:19:48.4906231Z Preparing to unpack .../080-libplexus-cipher-java_2.0-1_all.deb ...
2026-05-03T01:19:48.4913433Z Unpacking libplexus-cipher-java (2.0-1) ...
2026-05-03T01:19:48.5117130Z Selecting previously unselected package libplexus-classworlds-java.
2026-05-03T01:19:48.5201642Z Preparing to unpack .../081-libplexus-classworlds-java_2.7.0-1_all.deb ...
2026-05-03T01:19:48.5207982Z Unpacking libplexus-classworlds-java (2.7.0-1) ...
2026-05-03T01:19:48.5398515Z Selecting previously unselected package libplexus-component-annotations-java.
2026-05-03T01:19:48.5482730Z Preparing to unpack .../082-libplexus-component-annotations-java_2.1.1-1_all.deb ...
2026-05-03T01:19:48.5489110Z Unpacking libplexus-component-annotations-java (2.1.1-1) ...
2026-05-03T01:19:48.5685978Z Selecting previously unselected package libplexus-interpolation-java.
2026-05-03T01:19:48.5771444Z Preparing to unpack .../083-libplexus-interpolation-java_1.26-1_all.deb ...
2026-05-03T01:19:48.5778214Z Unpacking libplexus-interpolation-java (1.26-1) ...
2026-05-03T01:19:48.6008919Z Selecting previously unselected package libplexus-sec-dispatcher-java.
2026-05-03T01:19:48.6092115Z Preparing to unpack .../084-libplexus-sec-dispatcher-java_2.0-3_all.deb ...
2026-05-03T01:19:48.6098776Z Unpacking libplexus-sec-dispatcher-java (2.0-3) ...
2026-05-03T01:19:48.6285730Z Selecting previously unselected package libslf4j-java.
2026-05-03T01:19:48.6367990Z Preparing to unpack .../085-libslf4j-java_1.7.32-1_all.deb ...
2026-05-03T01:19:48.6374495Z Unpacking libslf4j-java (1.7.32-1) ...
2026-05-03T01:19:48.6659894Z Selecting previously unselected package libsisu-inject-java.
2026-05-03T01:19:48.6742495Z Preparing to unpack .../086-libsisu-inject-java_0.3.4-2_all.deb ...
2026-05-03T01:19:48.6749170Z Unpacking libsisu-inject-java (0.3.4-2) ...
2026-05-03T01:19:48.7165242Z Selecting previously unselected package libsisu-plexus-java.
2026-05-03T01:19:48.7248536Z Preparing to unpack .../087-libsisu-plexus-java_0.3.4-3_all.deb ...
2026-05-03T01:19:48.7254903Z Unpacking libsisu-plexus-java (0.3.4-3) ...
2026-05-03T01:19:48.7559112Z Selecting previously unselected package libmaven3-core-java.
2026-05-03T01:19:48.7642071Z Preparing to unpack .../088-libmaven3-core-java_3.8.7-2_all.deb ...
2026-05-03T01:19:48.7648969Z Unpacking libmaven3-core-java (3.8.7-2) ...
2026-05-03T01:19:48.8037110Z Selecting previously unselected package libopengl0:amd64.
2026-05-03T01:19:48.8120390Z Preparing to unpack .../089-libopengl0_1.7.0-1build1_amd64.deb ...
2026-05-03T01:19:48.8127169Z Unpacking libopengl0:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:48.8308084Z Selecting previously unselected package libopengl-dev:amd64.
2026-05-03T01:19:48.8388165Z Preparing to unpack .../090-libopengl-dev_1.7.0-1build1_amd64.deb ...
2026-05-03T01:19:48.8395646Z Unpacking libopengl-dev:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:48.8571149Z Selecting previously unselected package libwagon-file-java.
2026-05-03T01:19:48.8672450Z Preparing to unpack .../091-libwagon-file-java_3.5.3-1_all.deb ...
2026-05-03T01:19:48.8679915Z Unpacking libwagon-file-java (3.5.3-1) ...
2026-05-03T01:19:48.8868394Z Selecting previously unselected package libwagon-http-shaded-java.
2026-05-03T01:19:48.8951372Z Preparing to unpack .../092-libwagon-http-shaded-java_3.5.3-1_all.deb ...
2026-05-03T01:19:48.8957857Z Unpacking libwagon-http-shaded-java (3.5.3-1) ...
2026-05-03T01:19:48.9181426Z Selecting previously unselected package libxml-simple-perl.
2026-05-03T01:19:48.9262758Z Preparing to unpack .../093-libxml-simple-perl_2.25-2_all.deb ...
2026-05-03T01:19:48.9269550Z Unpacking libxml-simple-perl (2.25-2) ...
2026-05-03T01:19:48.9500858Z Selecting previously unselected package libxml2-utils.
2026-05-03T01:19:48.9593239Z Preparing to unpack .../094-libxml2-utils_2.9.14+dfsg-1.3ubuntu3.7_amd64.deb ...
2026-05-03T01:19:48.9601211Z Unpacking libxml2-utils (2.9.14+dfsg-1.3ubuntu3.7) ...
2026-05-03T01:19:48.9809223Z Selecting previously unselected package lzop.
2026-05-03T01:19:48.9899552Z Preparing to unpack .../095-lzop_1.04-2build3_amd64.deb ...
2026-05-03T01:19:48.9907783Z Unpacking lzop (1.04-2build3) ...
2026-05-03T01:19:49.0122343Z Selecting previously unselected package maven.
2026-05-03T01:19:49.0204680Z Preparing to unpack .../096-maven_3.8.7-2_all.deb ...
2026-05-03T01:19:49.0211857Z Unpacking maven (3.8.7-2) ...
2026-05-03T01:19:49.0437781Z Selecting previously unselected package optipng.
2026-05-03T01:19:49.0518255Z Preparing to unpack .../097-optipng_0.7.8+ds-1build2_amd64.deb ...
2026-05-03T01:19:49.0525211Z Unpacking optipng (0.7.8+ds-1build2) ...
2026-05-03T01:19:49.0730020Z Selecting previously unselected package pngcrush.
2026-05-03T01:19:49.0810082Z Preparing to unpack .../098-pngcrush_1.8.13-1build2_amd64.deb ...
2026-05-03T01:19:49.0816595Z Unpacking pngcrush (1.8.13-1build2) ...
2026-05-03T01:19:49.0995423Z Selecting previously unselected package pwgen.
2026-05-03T01:19:49.1074696Z Preparing to unpack .../099-pwgen_2.08-2build2_amd64.deb ...
2026-05-03T01:19:49.1081362Z Unpacking pwgen (2.08-2build2) ...
2026-05-03T01:19:49.1250549Z Selecting previously unselected package xsltproc.
2026-05-03T01:19:49.1327737Z Preparing to unpack .../100-xsltproc_1.1.39-0exp1ubuntu0.24.04.3_amd64.deb ...
2026-05-03T01:19:49.1333740Z Unpacking xsltproc (1.1.39-0exp1ubuntu0.24.04.3) ...
2026-05-03T01:19:49.1511442Z Selecting previously unselected package libfdt1:amd64.
2026-05-03T01:19:49.1588883Z Preparing to unpack .../101-libfdt1_1.7.0-2build1_amd64.deb ...
2026-05-03T01:19:49.1595839Z Unpacking libfdt1:amd64 (1.7.0-2build1) ...
2026-05-03T01:19:49.1767463Z Selecting previously unselected package device-tree-compiler.
2026-05-03T01:19:49.1846083Z Preparing to unpack .../102-device-tree-compiler_1.7.0-2build1_amd64.deb ...
2026-05-03T01:19:49.1853657Z Unpacking device-tree-compiler (1.7.0-2build1) ...
2026-05-03T01:19:49.2075907Z Selecting previously unselected package libglvnd-core-dev:amd64.
2026-05-03T01:19:49.2157265Z Preparing to unpack .../103-libglvnd-core-dev_1.7.0-1build1_amd64.deb ...
2026-05-03T01:19:49.2163506Z Unpacking libglvnd-core-dev:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:49.2340870Z Selecting previously unselected package libglvnd-dev:amd64.
2026-05-03T01:19:49.2423146Z Preparing to unpack .../104-libglvnd-dev_1.7.0-1build1_amd64.deb ...
2026-05-03T01:19:49.2430585Z Unpacking libglvnd-dev:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:49.2605197Z Selecting previously unselected package libgl1-mesa-dev:amd64.
2026-05-03T01:19:49.2690031Z Preparing to unpack .../105-libgl1-mesa-dev_25.2.8-0ubuntu0.24.04.1_amd64.deb ...
2026-05-03T01:19:49.2696594Z Unpacking libgl1-mesa-dev:amd64 (25.2.8-0ubuntu0.24.04.1) ...
2026-05-03T01:19:49.2876472Z Selecting previously unselected package liblz4-tool.
2026-05-03T01:19:49.2958596Z Preparing to unpack .../106-liblz4-tool_1.9.4-1build1.1_all.deb ...
2026-05-03T01:19:49.2965180Z Unpacking liblz4-tool (1.9.4-1build1.1) ...
2026-05-03T01:19:49.3132274Z Selecting previously unselected package schedtool.
2026-05-03T01:19:49.3214800Z Preparing to unpack .../107-schedtool_1.3.0-4_amd64.deb ...
2026-05-03T01:19:49.3221103Z Unpacking schedtool (1.3.0-4) ...
2026-05-03T01:19:49.3629273Z Setting up bzip2-doc (1.0.8-5.1build0.1) ...
2026-05-03T01:19:49.3650717Z Setting up libslf4j-java (1.7.32-1) ...
2026-05-03T01:19:49.3668443Z Setting up libplexus-utils2-java (3.4.2-1) ...
2026-05-03T01:19:49.3687984Z Setting up libncurses-dev:amd64 (6.4+20240113-1ubuntu2) ...
2026-05-03T01:19:49.3705270Z Setting up libplexus-classworlds-java (2.7.0-1) ...
2026-05-03T01:19:49.3727647Z Setting up libjsr305-java (0.1~+svn49-11) ...
2026-05-03T01:19:49.3745739Z Setting up libglvnd-core-dev:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:49.3762413Z Setting up libaopalliance-java (20070526-7) ...
2026-05-03T01:19:49.3780248Z Setting up libcommons-cli-java (1.6.0-1) ...
2026-05-03T01:19:49.3797490Z Setting up libjq1:amd64 (1.7.1-3ubuntu0.24.04.2) ...
2026-05-03T01:19:49.3814813Z Setting up pngcrush (1.8.13-1build2) ...
2026-05-03T01:19:49.3831388Z Setting up xsltproc (1.1.39-0exp1ubuntu0.24.04.3) ...
2026-05-03T01:19:49.3848002Z Setting up libplexus-component-annotations-java (2.1.1-1) ...
2026-05-03T01:19:49.3868901Z Setting up libfdt1:amd64 (1.7.0-2build1) ...
2026-05-03T01:19:49.3890984Z Setting up gperf (3.1-1build1) ...
2026-05-03T01:19:49.3907847Z Setting up libpthread-stubs0-dev:amd64 (0.4-1build3) ...
2026-05-03T01:19:49.3924482Z Setting up libopengl0:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:49.3942936Z Setting up libc6-x32 (2.39-0ubuntu8.7) ...
2026-05-03T01:19:49.3979896Z Setting up libgeronimo-annotation-1.3-spec-java (1.3-1) ...
2026-05-03T01:19:49.3996049Z Setting up libgeronimo-interceptor-3.0-spec-java (1.0.1-4fakesync) ...
2026-05-03T01:19:49.4012011Z Setting up xtrans-dev (1.4.0-1) ...
2026-05-03T01:19:49.4027850Z Setting up libegl-mesa0:amd64 (25.2.8-0ubuntu0.24.04.1) ...
2026-05-03T01:19:49.4048309Z Setting up libgles2:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:49.4065557Z Setting up optipng (0.7.8+ds-1build2) ...
2026-05-03T01:19:49.4081906Z Setting up libjansi-java (2.4.1-2) ...
2026-05-03T01:19:49.4099821Z Setting up libapache-pom-java (29-2) ...
2026-05-03T01:19:49.4116663Z Setting up libatinject-jsr330-api-java (1.0+ds1-5) ...
2026-05-03T01:19:49.4134607Z Setting up libgles1:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:49.4152791Z Setting up libplexus-interpolation-java (1.26-1) ...
2026-05-03T01:19:49.4168784Z Setting up libelf-dev:amd64 (0.190-1.1ubuntu0.1) ...
2026-05-03T01:19:49.4187325Z Setting up device-tree-compiler (1.7.0-2build1) ...
2026-05-03T01:19:49.4204858Z Setting up libxml-simple-perl (2.25-2) ...
2026-05-03T01:19:49.4221974Z Setting up libx32gomp1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.4242278Z Setting up liblz4-tool (1.9.4-1build1.1) ...
2026-05-03T01:19:49.4258977Z Setting up jq (1.7.1-3ubuntu0.24.04.2) ...
2026-05-03T01:19:49.4278777Z Setting up lzop (1.04-2build3) ...
2026-05-03T01:19:49.4295605Z Setting up libegl1:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:49.4313656Z Setting up libc6-i386 (2.39-0ubuntu8.7) ...
2026-05-03T01:19:49.4360302Z Setting up build-essential (12.10ubuntu1) ...
2026-05-03T01:19:49.4381979Z Setting up libx32quadmath0 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.4399131Z Setting up xorg-sgml-doctools (1:1.11-1.1) ...
2026-05-03T01:19:49.4418514Z Setting up libwagon-http-shaded-java (3.5.3-1) ...
2026-05-03T01:19:49.4436375Z Setting up libopengl-dev:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:49.4455620Z Setting up libxml2-utils (2.9.14+dfsg-1.3ubuntu3.7) ...
2026-05-03T01:19:49.4474393Z Setting up libcdi-api-java (1.2-3) ...
2026-05-03T01:19:49.4491166Z Setting up libhiredis1.1.0:amd64 (1.2.0-6ubuntu3) ...
2026-05-03T01:19:49.4511933Z Setting up pwgen (2.08-2build2) ...
2026-05-03T01:19:49.4529532Z Setting up lib32atomic1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.4548719Z Setting up schedtool (1.3.0-4) ...
2026-05-03T01:19:49.4568100Z Setting up libbz2-dev:amd64 (1.0.8-5.1build0.1) ...
2026-05-03T01:19:49.4585290Z Setting up libx32atomic1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.4606409Z Setting up libwagon-provider-api-java (3.5.3-1) ...
2026-05-03T01:19:49.4624483Z Setting up lib32z1 (1:1.3.dfsg-3.1ubuntu2.1) ...
2026-05-03T01:19:49.4643516Z Setting up libc6-dev-i386 (2.39-0ubuntu8.7) ...
2026-05-03T01:19:49.4664275Z Setting up lib32itm1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.4684669Z Setting up libx32gcc-s1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.4706474Z Setting up libmaven-parent-java (35-1) ...
2026-05-03T01:19:49.4727972Z Setting up ccache (4.9.1-1) ...
2026-05-03T01:19:49.4752472Z Updating symlinks in /usr/lib/ccache ...
2026-05-03T01:19:49.4872508Z Setting up libcommons-parent-java (56-1) ...
2026-05-03T01:19:49.4892819Z Setting up libsisu-inject-java (0.3.4-2) ...
2026-05-03T01:19:49.4911692Z Setting up libx32itm1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.4934303Z Setting up libplexus-cipher-java (2.0-1) ...
2026-05-03T01:19:49.4951435Z Setting up libx32asan8 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.4980689Z Setting up libc6-dev-x32 (2.39-0ubuntu8.7) ...
2026-05-03T01:19:49.5002011Z Setting up libsisu-plexus-java (0.3.4-3) ...
2026-05-03T01:19:49.5020072Z Setting up lib32gomp1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.5043642Z Setting up lib32gcc-s1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.5064298Z Setting up lib32stdc++6 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.5095988Z Setting up lib32asan8 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.5113303Z Setting up lib32z1-dev (1:1.3.dfsg-3.1ubuntu2.1) ...
2026-05-03T01:19:49.5137587Z Setting up libcommons-lang3-java (3.14.0-1) ...
2026-05-03T01:19:49.5154675Z Setting up lib32tinfo6 (6.4+20240113-1ubuntu2) ...
2026-05-03T01:19:49.5171798Z Setting up lib32quadmath0 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.5192051Z Setting up libplexus-sec-dispatcher-java (2.0-3) ...
2026-05-03T01:19:49.5208357Z Setting up libwagon-file-java (3.5.3-1) ...
2026-05-03T01:19:49.5227502Z Setting up libx32stdc++6 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.5245216Z Setting up libx32ubsan1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.5266986Z Setting up libcommons-io-java (2.11.0-2) ...
2026-05-03T01:19:49.5289270Z Setting up lib32ncurses6 (6.4+20240113-1ubuntu2) ...
2026-05-03T01:19:49.5311659Z Setting up lib32ncursesw6 (6.4+20240113-1ubuntu2) ...
2026-05-03T01:19:49.5334877Z Setting up lib32ubsan1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.5360280Z Setting up lib32gcc-13-dev (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T01:19:49.5381995Z Setting up libmaven-resolver-java (1.6.3-1) ...
2026-05-03T01:19:49.5517103Z Setting up libx32gcc-13-dev (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T01:19:49.5541433Z Setting up libmaven-shared-utils-java (3.3.4-1) ...
2026-05-03T01:19:49.5560577Z Setting up gcc-13-multilib (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T01:19:49.5580195Z Setting up lib32stdc++-13-dev (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T01:19:49.5609780Z Setting up gcc-multilib (4:13.2.0-7ubuntu1) ...
2026-05-03T01:19:49.5632631Z Setting up lib32ncurses-dev (6.4+20240113-1ubuntu2) ...
2026-05-03T01:19:49.5653783Z Setting up libx32stdc++-13-dev (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T01:19:49.5672974Z Setting up g++-13-multilib (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T01:19:49.5693767Z Setting up g++-multilib (4:13.2.0-7ubuntu1) ...
2026-05-03T01:19:49.5750079Z Setting up liberror-prone-java (2.18.0-1) ...
2026-05-03T01:19:49.5787293Z Setting up libguava-java (32.0.1-1) ...
2026-05-03T01:19:49.5838249Z Setting up libguice-java (4.2.3-2) ...
2026-05-03T01:19:49.5887724Z Setting up libmaven3-core-java (3.8.7-2) ...
2026-05-03T01:19:49.5916001Z Setting up maven (3.8.7-2) ...
2026-05-03T01:19:49.6009971Z update-alternatives: using /usr/share/maven/bin/mvn to provide /usr/bin/mvn (mvn) in auto mode
2026-05-03T01:19:49.6090072Z Processing triggers for man-db (2.12.0-4build2) ...
2026-05-03T01:19:49.6108888Z Not building database; man-db/auto-update is not 'true'.
2026-05-03T01:19:49.6131127Z Processing triggers for sgml-base (1.31) ...
2026-05-03T01:19:49.6238321Z Processing triggers for install-info (7.1-3build2) ...
2026-05-03T01:19:49.7155079Z Setting up x11proto-dev (2023.2-1) ...
2026-05-03T01:19:49.7177516Z Setting up libxau-dev:amd64 (1:1.0.9-1build6) ...
2026-05-03T01:19:49.7202941Z Processing triggers for libc-bin (2.39-0ubuntu8.7) ...
2026-05-03T01:19:49.7369565Z Setting up libxdmcp-dev:amd64 (1:1.1.3-0ubuntu6) ...
2026-05-03T01:19:49.7409843Z Setting up libxcb1-dev:amd64 (1.15-1ubuntu2) ...
2026-05-03T01:19:49.7437360Z Setting up libx11-dev:amd64 (2:1.8.7-1build1) ...
2026-05-03T01:19:49.7471817Z Setting up libglx-dev:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:49.7502524Z Setting up libgl-dev:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:49.7526679Z Setting up libegl-dev:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:49.7558523Z Setting up libgles-dev:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:49.7579698Z Setting up libglvnd-dev:amd64 (1.7.0-1build1) ...
2026-05-03T01:19:49.7606050Z Setting up libgl1-mesa-dev:amd64 (25.2.8-0ubuntu0.24.04.1) ...
2026-05-03T01:19:50.7717127Z 
2026-05-03T01:19:50.7717835Z Running kernel seems to be up-to-date.
2026-05-03T01:19:50.7718202Z 
2026-05-03T01:19:50.7718339Z No services need to be restarted.
2026-05-03T01:19:50.7718592Z 
2026-05-03T01:19:50.7718726Z No containers need to be restarted.
2026-05-03T01:19:50.7718897Z 
2026-05-03T01:19:50.7719018Z No user sessions are running outdated binaries.
2026-05-03T01:19:50.7719230Z 
2026-05-03T01:19:50.7719634Z No VM guests are running outdated hypervisor (qemu) binaries on this host.
2026-05-03T01:19:51.8489976Z ##[group]Run ZYCLANG=$(curl -sI https://github.com/ZyCromerZ/Clang/releases/latest | awk -F/ '/location:/ {print $NF}' | tr -d '\r')
2026-05-03T01:19:51.8490924Z [36;1mZYCLANG=$(curl -sI https://github.com/ZyCromerZ/Clang/releases/latest | awk -F/ '/location:/ {print $NF}' | tr -d '\r')[0m
2026-05-03T01:19:51.8491744Z [36;1mZYASSET=$(curl -sL https://github.com/ZyCromerZ/Clang/releases/expanded_assets/$ZYCLANG | grep -oP '[^/"]+\.tar.gz' | head -n1)[0m
2026-05-03T01:19:51.8492447Z [36;1mZYCLANG_DLINK="https://github.com/ZyCromerZ/Clang/releases/latest/download/$ZYASSET"[0m
2026-05-03T01:19:51.8492858Z [36;1m[0m
2026-05-03T01:19:51.8493065Z [36;1mecho "Downloading: $ZYCLANG_DLINK"[0m
2026-05-03T01:19:51.8493350Z [36;1mmkdir -p $GITHUB_WORKSPACE/ZyClang[0m
2026-05-03T01:19:51.8493687Z [36;1maria2c -s16 -x16 -k1M "$ZYCLANG_DLINK" -o ZyClang.tar.gz[0m
2026-05-03T01:19:51.8494077Z [36;1mtar -C $GITHUB_WORKSPACE/ZyClang/ -zxf ZyClang.tar.gz[0m
2026-05-03T01:19:51.8494445Z [36;1mrm -f ZyClang.tar.gz[0m
2026-05-03T01:19:51.8494663Z [36;1m[0m
2026-05-03T01:19:51.8494976Z [36;1mCLANG_VERSION=$($GITHUB_WORKSPACE/ZyClang/bin/clang --version | head -n 1)[0m
2026-05-03T01:19:51.8495486Z [36;1mLLD_VERSION=$($GITHUB_WORKSPACE/ZyClang/bin/ld.lld --version | head -n 1)[0m
2026-05-03T01:19:51.8495915Z [36;1mecho "CLANG_VERSION=$CLANG_VERSION" >> $GITHUB_ENV[0m
2026-05-03T01:19:51.8496287Z [36;1mecho "LLD_VERSION=$LLD_VERSION" >> $GITHUB_ENV[0m
2026-05-03T01:19:51.8496587Z [36;1mecho "Clang: $CLANG_VERSION"[0m
2026-05-03T01:19:51.8496843Z [36;1mecho "LLD: $LLD_VERSION"[0m
2026-05-03T01:19:51.8519678Z shell: /usr/bin/bash -e {0}
2026-05-03T01:19:51.8519934Z env:
2026-05-03T01:19:51.8520115Z   KERNEL_NAME: Castorice
2026-05-03T01:19:51.8520331Z   DEVICE_CODE: fire
2026-05-03T01:19:51.8520556Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:19:51.8520818Z   CLANG_VERSION: 
2026-05-03T01:19:51.8521019Z   LLD_VERSION: 
2026-05-03T01:19:51.8521391Z   KERNEL_HEAD_HASH: 
2026-05-03T01:19:51.8521586Z   KSU_DIR: 
2026-05-03T01:19:51.8521751Z   KSU_VERSION: 
2026-05-03T01:19:51.8521926Z   KERNEL_VERSION: 
2026-05-03T01:19:51.8522104Z   ZIP_NAME: 
2026-05-03T01:19:51.8522283Z ##[endgroup]
2026-05-03T01:19:52.0569948Z Downloading: https://github.com/ZyCromerZ/Clang/releases/latest/download/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.3837823Z 
2026-05-03T01:19:52.3838737Z 05/03 01:19:52 [[1;32mNOTICE[0m] Downloading 1 item(s)
2026-05-03T01:19:52.4459780Z 
2026-05-03T01:19:52.4461181Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#7 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.5625188Z 
2026-05-03T01:19:52.5632740Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#7 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A04%3A43Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A04%3A05Z&ske=2026-05-03T02%3A04%3A43Z&sks=b&skv=2018-11-09&sig=L6oFv9Ty3ZQwxeIPPV%2B4UbQDS0YZtQJAe6HNZUjAynU%3D&jwt=***
2026-05-03T01:19:52.6149993Z 
2026-05-03T01:19:52.6151489Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#9 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6153402Z 
2026-05-03T01:19:52.6154365Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#10 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6155714Z 
2026-05-03T01:19:52.6156627Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#11 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6157474Z 
2026-05-03T01:19:52.6158769Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#12 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6159790Z 
2026-05-03T01:19:52.6160522Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#13 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6161050Z 
2026-05-03T01:19:52.6161588Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#14 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6162096Z 
2026-05-03T01:19:52.6162620Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#15 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6163313Z 
2026-05-03T01:19:52.6164157Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#16 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6164659Z 
2026-05-03T01:19:52.6165176Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#17 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6165665Z 
2026-05-03T01:19:52.6166179Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#20 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6166671Z 
2026-05-03T01:19:52.6167179Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#23 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6167670Z 
2026-05-03T01:19:52.6168186Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#18 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6168669Z 
2026-05-03T01:19:52.6169182Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#19 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6170051Z 
2026-05-03T01:19:52.6170588Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#21 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6188688Z 
2026-05-03T01:19:52.6189807Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#17 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6190687Z 
2026-05-03T01:19:52.6191594Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#22 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6192441Z 
2026-05-03T01:19:52.6193085Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#12 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6194470Z 
2026-05-03T01:19:52.6195318Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#19 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6197341Z 
2026-05-03T01:19:52.6198250Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#16 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6198989Z 
2026-05-03T01:19:52.6200305Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#14 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6200851Z 
2026-05-03T01:19:52.6201385Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#15 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6201877Z 
2026-05-03T01:19:52.6202673Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#23 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6203515Z 
2026-05-03T01:19:52.6204070Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#13 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6204561Z 
2026-05-03T01:19:52.6205068Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#18 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6227289Z 
2026-05-03T01:19:52.6228274Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#14 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6231081Z 
2026-05-03T01:19:52.6232024Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#15 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6232843Z 
2026-05-03T01:19:52.6233700Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#13 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6717258Z 
2026-05-03T01:19:52.6723988Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#10 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6726547Z 
2026-05-03T01:19:52.6733010Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#17 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6735214Z 
2026-05-03T01:19:52.6740370Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#12 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6742605Z 
2026-05-03T01:19:52.6748591Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#9 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6750536Z 
2026-05-03T01:19:52.6755156Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#11 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6756985Z 
2026-05-03T01:19:52.6762537Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#14 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6764279Z 
2026-05-03T01:19:52.6771195Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#15 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6772968Z 
2026-05-03T01:19:52.6778896Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#16 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6781160Z 
2026-05-03T01:19:52.6786373Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#19 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6788470Z 
2026-05-03T01:19:52.6793258Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#20 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6794979Z 
2026-05-03T01:19:52.6800080Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#21 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6802784Z 
2026-05-03T01:19:52.6807544Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#13 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6809297Z 
2026-05-03T01:19:52.6814096Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#22 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6815841Z 
2026-05-03T01:19:52.6820504Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#18 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6822216Z 
2026-05-03T01:19:52.6826678Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#23 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6828565Z 
2026-05-03T01:19:52.6829118Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#12 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6829726Z 
2026-05-03T01:19:52.6830247Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#15 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6830742Z 
2026-05-03T01:19:52.6831261Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#11 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6902341Z 
2026-05-03T01:19:52.6903488Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#16 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6904378Z 
2026-05-03T01:19:52.6905267Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#21 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6906101Z 
2026-05-03T01:19:52.6911315Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#11 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6913351Z 
2026-05-03T01:19:52.6917862Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#12 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6919878Z 
2026-05-03T01:19:52.6924659Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#15 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6926356Z 
2026-05-03T01:19:52.6926937Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#18 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6927465Z 
2026-05-03T01:19:52.6928090Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#19 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6928597Z 
2026-05-03T01:19:52.6929222Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#20 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6949080Z 
2026-05-03T01:19:52.6950331Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#15 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6951542Z 
2026-05-03T01:19:52.6957450Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#16 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6959287Z 
2026-05-03T01:19:52.6960182Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#18 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6960710Z 
2026-05-03T01:19:52.6961256Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#19 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6961760Z 
2026-05-03T01:19:52.6966281Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#21 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.6968001Z 
2026-05-03T01:19:52.6968531Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#20 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6969062Z 
2026-05-03T01:19:52.6969981Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#11 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6970486Z 
2026-05-03T01:19:52.6971034Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#12 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6992122Z 
2026-05-03T01:19:52.6993078Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#12 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.6993960Z 
2026-05-03T01:19:52.6999775Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#15 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.7001650Z 
2026-05-03T01:19:52.7002239Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#16 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.7002751Z 
2026-05-03T01:19:52.7007259Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#21 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.7009186Z 
2026-05-03T01:19:52.7009950Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#18 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.7010459Z 
2026-05-03T01:19:52.7010984Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#19 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.7011474Z 
2026-05-03T01:19:52.7011987Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#11 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.7020016Z 
2026-05-03T01:19:52.7026227Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#20 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.7036439Z 
2026-05-03T01:19:52.7037583Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#16 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.7039110Z 
2026-05-03T01:19:52.7049120Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#12 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.7052660Z 
2026-05-03T01:19:52.7053981Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#15 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.7054896Z 
2026-05-03T01:19:52.7063475Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#11 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.7066792Z 
2026-05-03T01:19:52.7076154Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#21 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.7079797Z 
2026-05-03T01:19:52.7080981Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#19 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.7081912Z 
2026-05-03T01:19:52.7083244Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#18 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.7084458Z 
2026-05-03T01:19:52.7093041Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#16 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.7096602Z 
2026-05-03T01:19:52.7098096Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#15 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.7143870Z 
2026-05-03T01:19:52.7152125Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#18 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.7155291Z 
2026-05-03T01:19:52.7156319Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#19 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T01:19:52.7157235Z 
2026-05-03T01:19:52.7166336Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#21 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.7170408Z 
2026-05-03T01:19:52.7178465Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#15 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:52.7207865Z 
2026-05-03T01:19:52.7216723Z 05/03 01:19:52 [[1;32mNOTICE[0m] CUID#19 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T02%3A02%3A58Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T01%3A02%3A06Z&ske=2026-05-03T02%3A02%3A58Z&sks=b&skv=2018-11-09&sig=eN1J6B6rSiTkks9gsDjTR0WgXi8ysnGtHFWx27w0r0c%3D&jwt=***
2026-05-03T01:19:55.1569571Z [#80f467 320MiB/580MiB(55%) CN:16 DL:400MiB]
2026-05-03T01:19:55.1569893Z 
2026-05-03T01:19:55.1570615Z 05/03 01:19:55 [[1;32mNOTICE[0m] Download complete: /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/ZyClang.tar.gz
2026-05-03T01:19:55.1571468Z 
2026-05-03T01:19:55.1571590Z Download Results:
2026-05-03T01:19:55.1571860Z gid   |stat|avg speed  |path/URI
2026-05-03T01:19:55.1572141Z ======+====+===========+=======================================================
2026-05-03T01:19:55.1572937Z 80f467|OK  |   419MiB/s|/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/ZyClang.tar.gz
2026-05-03T01:19:55.1573294Z 
2026-05-03T01:19:55.1573372Z Status Legend:
2026-05-03T01:19:55.1573566Z (OK):download completed.
2026-05-03T01:20:08.3172188Z Clang: ZyC clang version 15.0.7 (https://github.com/llvm/llvm-project 8dfdcc7b7bf66834a761bd8de445840ef68e4d1a)
2026-05-03T01:20:08.3172994Z LLD: LLD 15.0.7 (compatible with GNU linkers)
2026-05-03T01:20:08.4122122Z ##[group]Run git clone --depth=1 https://github.com/MiCode/Xiaomi_Kernel_OpenSource.git \
2026-05-03T01:20:08.4123087Z [36;1mgit clone --depth=1 https://github.com/MiCode/Xiaomi_Kernel_OpenSource.git \[0m
2026-05-03T01:20:08.4123768Z [36;1m  -b fire-t-oss $GITHUB_WORKSPACE/kernel[0m
2026-05-03T01:20:08.4124212Z [36;1mcd $GITHUB_WORKSPACE/kernel[0m
2026-05-03T01:20:08.4124706Z [36;1mKERNEL_HEAD_HASH=$(git log --pretty=format:'%H' -1)[0m
2026-05-03T01:20:08.4125314Z [36;1mecho "KERNEL_HEAD_HASH=$KERNEL_HEAD_HASH" >> $GITHUB_ENV[0m
2026-05-03T01:20:08.4125883Z [36;1mecho "Kernel HEAD: $KERNEL_HEAD_HASH"[0m
2026-05-03T01:20:08.4154413Z shell: /usr/bin/bash -e {0}
2026-05-03T01:20:08.4154752Z env:
2026-05-03T01:20:08.4154990Z   KERNEL_NAME: Castorice
2026-05-03T01:20:08.4155275Z   DEVICE_CODE: fire
2026-05-03T01:20:08.4155563Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:20:08.4156368Z   CLANG_VERSION: ZyC clang version 15.0.7 (https://github.com/llvm/llvm-project 8dfdcc7b7bf66834a761bd8de445840ef68e4d1a)
2026-05-03T01:20:08.4157159Z   LLD_VERSION: LLD 15.0.7 (compatible with GNU linkers)
2026-05-03T01:20:08.4157559Z   KERNEL_HEAD_HASH: 
2026-05-03T01:20:08.4157832Z   KSU_DIR: 
2026-05-03T01:20:08.4158088Z   KSU_VERSION: 
2026-05-03T01:20:08.4158358Z   KERNEL_VERSION: 
2026-05-03T01:20:08.4158626Z   ZIP_NAME: 
2026-05-03T01:20:08.4158887Z ##[endgroup]
2026-05-03T01:20:08.4233035Z Cloning into '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel'...
2026-05-03T01:20:28.0787952Z Updating files:  21% (16752/76589)
2026-05-03T01:20:28.1323513Z Updating files:  22% (16850/76589)
2026-05-03T01:20:28.1789184Z Updating files:  23% (17616/76589)
2026-05-03T01:20:28.2189979Z Updating files:  24% (18382/76589)
2026-05-03T01:20:28.2620908Z Updating files:  25% (19148/76589)
2026-05-03T01:20:28.3064988Z Updating files:  26% (19914/76589)
2026-05-03T01:20:28.3621014Z Updating files:  27% (20680/76589)
2026-05-03T01:20:28.4154696Z Updating files:  28% (21445/76589)
2026-05-03T01:20:28.4926478Z Updating files:  29% (22211/76589)
2026-05-03T01:20:28.5478086Z Updating files:  30% (22977/76589)
2026-05-03T01:20:28.6057143Z Updating files:  31% (23743/76589)
2026-05-03T01:20:28.6688349Z Updating files:  32% (24509/76589)
2026-05-03T01:20:28.8166548Z Updating files:  33% (25275/76589)
2026-05-03T01:20:28.9681494Z Updating files:  34% (26041/76589)
2026-05-03T01:20:29.0364827Z Updating files:  35% (26807/76589)
2026-05-03T01:20:29.0728362Z Updating files:  36% (27573/76589)
2026-05-03T01:20:29.0773727Z Updating files:  36% (28238/76589)
2026-05-03T01:20:29.1431980Z Updating files:  37% (28338/76589)
2026-05-03T01:20:29.1997328Z Updating files:  38% (29104/76589)
2026-05-03T01:20:29.2604438Z Updating files:  39% (29870/76589)
2026-05-03T01:20:29.3309056Z Updating files:  40% (30636/76589)
2026-05-03T01:20:29.3842153Z Updating files:  41% (31402/76589)
2026-05-03T01:20:29.4352905Z Updating files:  42% (32168/76589)
2026-05-03T01:20:29.4880468Z Updating files:  43% (32934/76589)
2026-05-03T01:20:29.5364066Z Updating files:  44% (33700/76589)
2026-05-03T01:20:29.5848642Z Updating files:  45% (34466/76589)
2026-05-03T01:20:29.6495702Z Updating files:  46% (35231/76589)
2026-05-03T01:20:29.7146475Z Updating files:  47% (35997/76589)
2026-05-03T01:20:29.7921129Z Updating files:  48% (36763/76589)
2026-05-03T01:20:29.8651918Z Updating files:  49% (37529/76589)
2026-05-03T01:20:29.9319599Z Updating files:  50% (38295/76589)
2026-05-03T01:20:30.0113555Z Updating files:  51% (39061/76589)
2026-05-03T01:20:30.0727785Z Updating files:  52% (39827/76589)
2026-05-03T01:20:30.0736146Z Updating files:  52% (40583/76589)
2026-05-03T01:20:30.1307093Z Updating files:  53% (40593/76589)
2026-05-03T01:20:30.1980310Z Updating files:  54% (41359/76589)
2026-05-03T01:20:30.2442475Z Updating files:  55% (42124/76589)
2026-05-03T01:20:30.3041414Z Updating files:  56% (42890/76589)
2026-05-03T01:20:30.3614583Z Updating files:  57% (43656/76589)
2026-05-03T01:20:30.4206927Z Updating files:  58% (44422/76589)
2026-05-03T01:20:30.4711214Z Updating files:  59% (45188/76589)
2026-05-03T01:20:30.5285507Z Updating files:  60% (45954/76589)
2026-05-03T01:20:30.5886989Z Updating files:  61% (46720/76589)
2026-05-03T01:20:30.6700083Z Updating files:  62% (47486/76589)
2026-05-03T01:20:30.7447687Z Updating files:  63% (48252/76589)
2026-05-03T01:20:30.8474771Z Updating files:  64% (49017/76589)
2026-05-03T01:20:30.9425082Z Updating files:  65% (49783/76589)
2026-05-03T01:20:31.0260423Z Updating files:  66% (50549/76589)
2026-05-03T01:20:31.0727972Z Updating files:  67% (51315/76589)
2026-05-03T01:20:31.1150677Z Updating files:  67% (51700/76589)
2026-05-03T01:20:31.1812220Z Updating files:  68% (52081/76589)
2026-05-03T01:20:31.2460579Z Updating files:  69% (52847/76589)
2026-05-03T01:20:31.3367467Z Updating files:  70% (53613/76589)
2026-05-03T01:20:31.4102155Z Updating files:  71% (54379/76589)
2026-05-03T01:20:31.5162607Z Updating files:  72% (55145/76589)
2026-05-03T01:20:31.5763214Z Updating files:  73% (55910/76589)
2026-05-03T01:20:31.6381358Z Updating files:  74% (56676/76589)
2026-05-03T01:20:31.6998748Z Updating files:  75% (57442/76589)
2026-05-03T01:20:31.7664716Z Updating files:  76% (58208/76589)
2026-05-03T01:20:31.8390643Z Updating files:  77% (58974/76589)
2026-05-03T01:20:31.9075581Z Updating files:  78% (59740/76589)
2026-05-03T01:20:31.9869027Z Updating files:  79% (60506/76589)
2026-05-03T01:20:32.0694788Z Updating files:  80% (61272/76589)
2026-05-03T01:20:32.0728500Z Updating files:  81% (62038/76589)
2026-05-03T01:20:32.1321139Z Updating files:  81% (62075/76589)
2026-05-03T01:20:32.1722369Z Updating files:  82% (62803/76589)
2026-05-03T01:20:32.2236388Z Updating files:  83% (63569/76589)
2026-05-03T01:20:32.2827737Z Updating files:  84% (64335/76589)
2026-05-03T01:20:32.3305662Z Updating files:  85% (65101/76589)
2026-05-03T01:20:32.3805013Z Updating files:  86% (65867/76589)
2026-05-03T01:20:32.4393660Z Updating files:  87% (66633/76589)
2026-05-03T01:20:32.5149055Z Updating files:  88% (67399/76589)
2026-05-03T01:20:32.5840077Z Updating files:  89% (68165/76589)
2026-05-03T01:20:32.6576578Z Updating files:  90% (68931/76589)
2026-05-03T01:20:32.7239298Z Updating files:  91% (69696/76589)
2026-05-03T01:20:32.8143288Z Updating files:  92% (70462/76589)
2026-05-03T01:20:32.8798508Z Updating files:  93% (71228/76589)
2026-05-03T01:20:32.9672883Z Updating files:  94% (71994/76589)
2026-05-03T01:20:33.0233003Z Updating files:  95% (72760/76589)
2026-05-03T01:20:33.0672590Z Updating files:  96% (73526/76589)
2026-05-03T01:20:33.0728468Z Updating files:  97% (74292/76589)
2026-05-03T01:20:33.1163118Z Updating files:  97% (74375/76589)
2026-05-03T01:20:33.1623986Z Updating files:  98% (75058/76589)
2026-05-03T01:20:33.2005162Z Updating files:  99% (75824/76589)
2026-05-03T01:20:33.2005583Z Updating files: 100% (76589/76589)
2026-05-03T01:20:33.2005956Z Updating files: 100% (76589/76589), done.
2026-05-03T01:20:33.2842980Z Kernel HEAD: 1d1aedfe40b2f5fd06c783b752af0197f38966eb
2026-05-03T01:20:33.2892295Z ##[group]Run cd $GITHUB_WORKSPACE/kernel
2026-05-03T01:20:33.2892632Z [36;1mcd $GITHUB_WORKSPACE/kernel[0m
2026-05-03T01:20:33.2893166Z [36;1mcurl -LSs "https://raw.githubusercontent.com/sidex15/KernelSU-Next/legacy/kernel/setup.sh" | bash -s legacy[0m
2026-05-03T01:20:33.2893662Z [36;1m[0m
2026-05-03T01:20:33.2893840Z [36;1mKSU_DIR=""[0m
2026-05-03T01:20:33.2894065Z [36;1mif [ -d "KernelSU-Next" ]; then[0m
2026-05-03T01:20:33.2894329Z [36;1m  KSU_DIR="KernelSU-Next"[0m
2026-05-03T01:20:33.2894573Z [36;1melif [ -d "KernelSU" ]; then[0m
2026-05-03T01:20:33.2894986Z [36;1m  KSU_DIR="KernelSU"[0m
2026-05-03T01:20:33.2895196Z [36;1melse[0m
2026-05-03T01:20:33.2895423Z [36;1m  echo "ERROR: KernelSU directory not found!"[0m
2026-05-03T01:20:33.2895695Z [36;1m  exit 1[0m
2026-05-03T01:20:33.2895873Z [36;1mfi[0m
2026-05-03T01:20:33.2896037Z [36;1m[0m
2026-05-03T01:20:33.2896296Z [36;1mKSU_GIT_VERSION=$(cd $KSU_DIR && git rev-list --count legacy)[0m
2026-05-03T01:20:33.2896723Z [36;1mKERNELSU_VERSION=$(($KSU_GIT_VERSION + 30000 + 60))[0m
2026-05-03T01:20:33.2897055Z [36;1mecho "KSU_DIR=$KSU_DIR" >> $GITHUB_ENV[0m
2026-05-03T01:20:33.2897381Z [36;1mecho "KSU_VERSION=$KERNELSU_VERSION" >> $GITHUB_ENV[0m
2026-05-03T01:20:33.2897779Z [36;1mecho "KernelSU-Next Legacy installed - version $KERNELSU_VERSION"[0m
2026-05-03T01:20:33.2919589Z shell: /usr/bin/bash -e {0}
2026-05-03T01:20:33.2919829Z env:
2026-05-03T01:20:33.2920014Z   KERNEL_NAME: Castorice
2026-05-03T01:20:33.2920225Z   DEVICE_CODE: fire
2026-05-03T01:20:33.2920437Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:20:33.2920982Z   CLANG_VERSION: ZyC clang version 15.0.7 (https://github.com/llvm/llvm-project 8dfdcc7b7bf66834a761bd8de445840ef68e4d1a)
2026-05-03T01:20:33.2921518Z   LLD_VERSION: LLD 15.0.7 (compatible with GNU linkers)
2026-05-03T01:20:33.2921866Z   KERNEL_HEAD_HASH: 1d1aedfe40b2f5fd06c783b752af0197f38966eb
2026-05-03T01:20:33.2922155Z   KSU_DIR: 
2026-05-03T01:20:33.2922331Z   KSU_VERSION: 
2026-05-03T01:20:33.2922513Z   KERNEL_VERSION: 
2026-05-03T01:20:33.2922692Z   ZIP_NAME: 
2026-05-03T01:20:33.2922867Z ##[endgroup]
2026-05-03T01:20:33.3928101Z [+] Setting up KernelSU-Next...
2026-05-03T01:20:33.3942705Z Cloning into 'KernelSU-Next'...
2026-05-03T01:20:34.5818076Z [+] Repository cloned.
2026-05-03T01:20:34.6117261Z No local changes to save
2026-05-03T01:20:34.6120179Z [-] Stashed current changes.
2026-05-03T01:20:34.7332454Z Already up to date.
2026-05-03T01:20:34.7337138Z [+] Repository updated.
2026-05-03T01:20:34.7786768Z Switched to a new branch 'legacy'
2026-05-03T01:20:34.7789673Z branch 'legacy' set up to track 'origin/legacy'.
2026-05-03T01:20:34.7794190Z [-] Checked out legacy.
2026-05-03T01:20:34.7824770Z [+] Symlink created.
2026-05-03T01:20:34.7839605Z [+] Modified Makefile.
2026-05-03T01:20:34.7869755Z [+] Modified Kconfig.
2026-05-03T01:20:34.7870088Z [+] Done.
2026-05-03T01:20:34.8105077Z KernelSU-Next Legacy installed - version 33042
2026-05-03T01:20:34.8135799Z ##[group]Run cd $GITHUB_WORKSPACE
2026-05-03T01:20:34.8136090Z [36;1mcd $GITHUB_WORKSPACE[0m
2026-05-03T01:20:34.8136498Z [36;1mgit clone --depth=1 https://gitlab.com/simonpunk/susfs4ksu.git -b kernel-4.19[0m
2026-05-03T01:20:34.8136901Z [36;1m[0m
2026-05-03T01:20:34.8137094Z [36;1mcd $GITHUB_WORKSPACE/kernel[0m
2026-05-03T01:20:34.8137344Z [36;1m# Copy SUSFS source files[0m
2026-05-03T01:20:34.8137599Z [36;1mecho "Copying SUSFS files..."[0m
2026-05-03T01:20:34.8137887Z [36;1mcp -rv ../susfs4ksu/kernel_patches/fs/* fs/[0m
2026-05-03T01:20:34.8138268Z [36;1mcp -rv ../susfs4ksu/kernel_patches/include/linux/* include/linux/[0m
2026-05-03T01:20:34.8138619Z [36;1m[0m
2026-05-03T01:20:34.8138811Z [36;1mecho "Verifying copied files:"[0m
2026-05-03T01:20:34.8139074Z [36;1mls -la include/linux/susfs*[0m
2026-05-03T01:20:34.8139314Z [36;1mls -la fs/susfs*[0m
2026-05-03T01:20:34.8139769Z [36;1mecho "SUSFS source files copied"[0m
2026-05-03T01:20:34.8161612Z shell: /usr/bin/bash -e {0}
2026-05-03T01:20:34.8161845Z env:
2026-05-03T01:20:34.8162028Z   KERNEL_NAME: Castorice
2026-05-03T01:20:34.8162240Z   DEVICE_CODE: fire
2026-05-03T01:20:34.8162460Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:20:34.8162990Z   CLANG_VERSION: ZyC clang version 15.0.7 (https://github.com/llvm/llvm-project 8dfdcc7b7bf66834a761bd8de445840ef68e4d1a)
2026-05-03T01:20:34.8163521Z   LLD_VERSION: LLD 15.0.7 (compatible with GNU linkers)
2026-05-03T01:20:34.8163872Z   KERNEL_HEAD_HASH: 1d1aedfe40b2f5fd06c783b752af0197f38966eb
2026-05-03T01:20:34.8164172Z   KSU_DIR: KernelSU-Next
2026-05-03T01:20:34.8164385Z   KSU_VERSION: 33042
2026-05-03T01:20:34.8164769Z   KERNEL_VERSION: 
2026-05-03T01:20:34.8164957Z   ZIP_NAME: 
2026-05-03T01:20:34.8165132Z ##[endgroup]
2026-05-03T01:20:34.8219643Z Cloning into 'susfs4ksu'...
2026-05-03T01:20:35.3463225Z Copying SUSFS files...
2026-05-03T01:20:35.3478018Z '../susfs4ksu/kernel_patches/fs/sus_su.c' -> 'fs/sus_su.c'
2026-05-03T01:20:35.3478665Z '../susfs4ksu/kernel_patches/fs/susfs.c' -> 'fs/susfs.c'
2026-05-03T01:20:35.3494976Z '../susfs4ksu/kernel_patches/include/linux/sus_su.h' -> 'include/linux/sus_su.h'
2026-05-03T01:20:35.3495795Z '../susfs4ksu/kernel_patches/include/linux/susfs.h' -> 'include/linux/susfs.h'
2026-05-03T01:20:35.3496479Z '../susfs4ksu/kernel_patches/include/linux/susfs_def.h' -> 'include/linux/susfs_def.h'
2026-05-03T01:20:35.3497021Z Verifying copied files:
2026-05-03T01:20:35.3517326Z -rw-r--r-- 1 runner runner 5921 May  3 01:20 include/linux/susfs.h
2026-05-03T01:20:35.3518034Z -rw-r--r-- 1 runner runner 2565 May  3 01:20 include/linux/susfs_def.h
2026-05-03T01:20:35.3532574Z -rw-r--r-- 1 runner runner 32318 May  3 01:20 fs/susfs.c
2026-05-03T01:20:35.3534489Z SUSFS source files copied
2026-05-03T01:20:35.3562420Z ##[group]Run cd $GITHUB_WORKSPACE
2026-05-03T01:20:35.3562724Z [36;1mcd $GITHUB_WORKSPACE[0m
2026-05-03T01:20:35.3563164Z [36;1mgit clone --depth=1 https://github.com/Alexjr2/KernelSU_Next_SUSFS_fire.git ref_patches[0m
2026-05-03T01:20:35.3563619Z [36;1mecho "=== Available patches ==="[0m
2026-05-03T01:20:35.3563914Z [36;1mls -la ref_patches/patchs/ || true[0m
2026-05-03T01:20:35.3585640Z shell: /usr/bin/bash -e {0}
2026-05-03T01:20:35.3585876Z env:
2026-05-03T01:20:35.3586062Z   KERNEL_NAME: Castorice
2026-05-03T01:20:35.3586281Z   DEVICE_CODE: fire
2026-05-03T01:20:35.3586498Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:20:35.3587047Z   CLANG_VERSION: ZyC clang version 15.0.7 (https://github.com/llvm/llvm-project 8dfdcc7b7bf66834a761bd8de445840ef68e4d1a)
2026-05-03T01:20:35.3587582Z   LLD_VERSION: LLD 15.0.7 (compatible with GNU linkers)
2026-05-03T01:20:35.3587949Z   KERNEL_HEAD_HASH: 1d1aedfe40b2f5fd06c783b752af0197f38966eb
2026-05-03T01:20:35.3588305Z   KSU_DIR: KernelSU-Next
2026-05-03T01:20:35.3588511Z   KSU_VERSION: 33042
2026-05-03T01:20:35.3588715Z   KERNEL_VERSION: 
2026-05-03T01:20:35.3588897Z   ZIP_NAME: 
2026-05-03T01:20:35.3589081Z ##[endgroup]
2026-05-03T01:20:35.3643351Z Cloning into 'ref_patches'...
2026-05-03T01:20:35.5092650Z === Available patches ===
2026-05-03T01:20:35.5106907Z total 148
2026-05-03T01:20:35.5107196Z drwxr-xr-x 2 runner runner  4096 May  3 01:20 .
2026-05-03T01:20:35.5107532Z drwxr-xr-x 5 runner runner  4096 May  3 01:20 ..
2026-05-03T01:20:35.5107938Z -rw-r--r-- 1 runner runner 43209 May  3 01:20 50_add_susfs_in_kernel-4.19.patch
2026-05-03T01:20:35.5108390Z -rw-r--r-- 1 runner runner  2588 May  3 01:20 69_hide_ksu.patch
2026-05-03T01:20:35.5108770Z -rw-r--r-- 1 runner runner  2801 May  3 01:20 69_hide_stuff.patch
2026-05-03T01:20:35.5109146Z -rw-r--r-- 1 runner runner  6296 May  3 01:20 ath9k_htc.patch
2026-05-03T01:20:35.5109791Z -rw-r--r-- 1 runner runner  3442 May  3 01:20 backslashxxksu.patch
2026-05-03T01:20:35.5110391Z -rw-r--r-- 1 runner runner   654 May  3 01:20 fix_kernel_genheaders.patch
2026-05-03T01:20:35.5110845Z -rw-r--r-- 1 runner runner 57742 May  3 01:20 fix_lcm.patch
2026-05-03T01:20:35.5111400Z -rw-r--r-- 1 runner runner  4772 May  3 01:20 ksu_hooks_4.19.patch
2026-05-03T01:20:35.5112022Z -rw-r--r-- 1 runner runner  4036 May  3 01:20 ksu_hooks_sukisu_4.19.patch
2026-05-03T01:20:35.5160905Z ##[group]Run cd $GITHUB_WORKSPACE/kernel
2026-05-03T01:20:35.5161257Z [36;1mcd $GITHUB_WORKSPACE/kernel[0m
2026-05-03T01:20:35.5161494Z [36;1m[0m
2026-05-03T01:20:35.5161742Z [36;1m# Apply KSU hooks for 4.19 (manual hook, NO kprobes)[0m
2026-05-03T01:20:35.5162057Z [36;1mif [ "true" = "true" ]; then[0m
2026-05-03T01:20:35.5162321Z [36;1m  echo "Applying KSU hooks patch..."[0m
2026-05-03T01:20:35.5162833Z [36;1m  patch -p1 --forward < ../ref_patches/patchs/ksu_hooks_4.19.patch || echo "WARN: ksu_hooks patch had issues"[0m
2026-05-03T01:20:35.5163496Z [36;1m[0m
2026-05-03T01:20:35.5163701Z [36;1m  echo "Applying hide KSU patch..."[0m
2026-05-03T01:20:35.5164168Z [36;1m  patch -p1 --forward < ../ref_patches/patchs/69_hide_ksu.patch || echo "WARN: hide_ksu patch had issues"[0m
2026-05-03T01:20:35.5164601Z [36;1mfi[0m
2026-05-03T01:20:35.5164769Z [36;1m[0m
2026-05-03T01:20:35.5164957Z [36;1m# Fix kernel genheaders (build fix)[0m
2026-05-03T01:20:35.5165258Z [36;1mecho "Applying genheaders fix..."[0m
2026-05-03T01:20:35.5165770Z [36;1mpatch -p1 --forward < ../ref_patches/patchs/fix_kernel_genheaders.patch || echo "WARN: genheaders patch had issues"[0m
2026-05-03T01:20:35.5166252Z [36;1m[0m
2026-05-03T01:20:35.5166433Z [36;1m# SUSFS kernel integration patch[0m
2026-05-03T01:20:35.5166714Z [36;1mif [ "true" = "true" ]; then[0m
2026-05-03T01:20:35.5167003Z [36;1m  echo "Applying SUSFS kernel patch..."[0m
2026-05-03T01:20:35.5167557Z [36;1m  patch -p1 --forward < ../ref_patches/patchs/50_add_susfs_in_kernel-4.19.patch || echo "WARN: susfs patch had issues"[0m
2026-05-03T01:20:35.5168051Z [36;1m[0m
2026-05-03T01:20:35.5168243Z [36;1m  # Fix SUSFS format strings for 4.19[0m
2026-05-03T01:20:35.5168665Z [36;1m  sed -i "s/poofed_size: '%u'/poofed_size: '%llu'/g" ./fs/susfs.c 2>/dev/null || true[0m
2026-05-03T01:20:35.5169186Z [36;1m  sed -i "s/length of string: %u/length of string: %lu/g" ./fs/susfs.c 2>/dev/null || true[0m
2026-05-03T01:20:35.5169775Z [36;1m[0m
2026-05-03T01:20:35.5169981Z [36;1m  # Fix task_work_add compatibility[0m
2026-05-03T01:20:35.5170269Z [36;1m  if [ -d "KernelSU-Next" ]; then[0m
2026-05-03T01:20:35.5170589Z [36;1m    sed -i "/task_work_add(tsk, cb, TWA_RESUME);/c\\[0m
2026-05-03T01:20:35.5170932Z [36;1m#if LINUX_VERSION_CODE >= KERNEL_VERSION(5, 10, 0)\\[0m
2026-05-03T01:20:35.5171266Z [36;1m\\ttask_work_add(tsk, cb, TWA_RESUME);\\[0m
2026-05-03T01:20:35.5171526Z [36;1m#else\\[0m
2026-05-03T01:20:35.5171737Z [36;1m\\ttask_work_add(tsk, cb, true);\\[0m
2026-05-03T01:20:35.5172087Z [36;1m#endif" ./KernelSU-Next/kernel/allowlist.c 2>/dev/null || true[0m
2026-05-03T01:20:35.5172413Z [36;1m  fi[0m
2026-05-03T01:20:35.5172586Z [36;1mfi[0m
2026-05-03T01:20:35.5172748Z [36;1m[0m
2026-05-03T01:20:35.5172977Z [36;1m# ===== LCD 0c/0d FIX (CRITICAL FOR TOUCHSCREEN) =====[0m
2026-05-03T01:20:35.5173337Z [36;1mecho "Applying LCM fix (LCD 0c/0d touchscreen fix)..."[0m
2026-05-03T01:20:35.5173849Z [36;1mpatch -p1 --forward < ../ref_patches/patchs/fix_lcm.patch || echo "WARN: fix_lcm patch had issues"[0m
2026-05-03T01:20:35.5174275Z [36;1m[0m
2026-05-03T01:20:35.5174508Z [36;1mecho "Applying primary display fix..."[0m
2026-05-03T01:20:35.5175029Z [36;1mpatch -p1 --forward < ../ref_patches/primary_display_fix.patch || echo "WARN: primary_display_fix patch had issues"[0m
2026-05-03T01:20:35.5175500Z [36;1m[0m
2026-05-03T01:20:35.5175684Z [36;1mecho "All patches applied"[0m
2026-05-03T01:20:35.5197319Z shell: /usr/bin/bash -e {0}
2026-05-03T01:20:35.5197571Z env:
2026-05-03T01:20:35.5207289Z   KERNEL_NAME: Castorice
2026-05-03T01:20:35.5207572Z   DEVICE_CODE: fire
2026-05-03T01:20:35.5207809Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:20:35.5208353Z   CLANG_VERSION: ZyC clang version 15.0.7 (https://github.com/llvm/llvm-project 8dfdcc7b7bf66834a761bd8de445840ef68e4d1a)
2026-05-03T01:20:35.5208892Z   LLD_VERSION: LLD 15.0.7 (compatible with GNU linkers)
2026-05-03T01:20:35.5209650Z   KERNEL_HEAD_HASH: 1d1aedfe40b2f5fd06c783b752af0197f38966eb
2026-05-03T01:20:35.5209960Z   KSU_DIR: KernelSU-Next
2026-05-03T01:20:35.5210169Z   KSU_VERSION: 33042
2026-05-03T01:20:35.5210360Z   KERNEL_VERSION: 
2026-05-03T01:20:35.5210547Z   ZIP_NAME: 
2026-05-03T01:20:35.5210729Z ##[endgroup]
2026-05-03T01:20:35.5252539Z Applying KSU hooks patch...
2026-05-03T01:20:35.5558832Z patching file fs/exec.c
2026-05-03T01:20:35.5559775Z Hunk #1 succeeded at 1888 (offset -24 lines).
2026-05-03T01:20:35.5562603Z patching file fs/open.c
2026-05-03T01:20:35.5565969Z patching file fs/read_write.c
2026-05-03T01:20:35.5569052Z patching file fs/stat.c
2026-05-03T01:20:35.5569548Z Hunk #1 succeeded at 354 (offset 1 line).
2026-05-03T01:20:35.5569950Z Hunk #2 succeeded at 367 (offset 1 line).
2026-05-03T01:20:35.5572760Z patching file drivers/input/input.c
2026-05-03T01:20:35.5573170Z Hunk #1 succeeded at 433 (offset -11 lines).
2026-05-03T01:20:35.5575667Z patching file kernel/reboot.c
2026-05-03T01:20:35.5578025Z patching file security/selinux/avc.c
2026-05-03T01:20:35.5578433Z Hunk #1 succeeded at 776 (offset -1 lines).
2026-05-03T01:20:35.5578852Z Hunk #2 succeeded at 788 (offset -1 lines).
2026-05-03T01:20:35.5581878Z Applying hide KSU patch...
2026-05-03T01:20:35.5592539Z patching file fs/proc/task_mmu.c
2026-05-03T01:20:35.5596819Z patching file fs/proc/base.c
2026-05-03T01:20:35.5601944Z Applying genheaders fix...
2026-05-03T01:20:35.5610524Z patching file kernel/gen_kheaders.sh
2026-05-03T01:20:35.5613693Z Applying SUSFS kernel patch...
2026-05-03T01:20:35.5622269Z patching file fs/Makefile
2026-05-03T01:20:35.5624449Z patching file fs/dcache.c
2026-05-03T01:20:35.5625637Z Hunk #2 succeeded at 2192 (offset -1 lines).
2026-05-03T01:20:35.5626061Z Hunk #3 succeeded at 2280 (offset -1 lines).
2026-05-03T01:20:35.5628631Z patching file fs/namei.c
2026-05-03T01:20:35.5630919Z Hunk #9 succeeded at 2957 (offset -20 lines).
2026-05-03T01:20:35.5631344Z Hunk #10 succeeded at 2991 (offset -20 lines).
2026-05-03T01:20:35.5631777Z Hunk #11 succeeded at 3134 (offset -20 lines).
2026-05-03T01:20:35.5632181Z Hunk #12 succeeded at 3211 (offset -20 lines).
2026-05-03T01:20:35.5632600Z Hunk #13 succeeded at 3363 (offset -20 lines).
2026-05-03T01:20:35.5633019Z Hunk #14 succeeded at 3412 (offset -20 lines).
2026-05-03T01:20:35.5633302Z Hunk #15 succeeded at 3437 (offset -20 lines).
2026-05-03T01:20:35.5633568Z Hunk #16 succeeded at 3780 (offset -22 lines).
2026-05-03T01:20:35.5633830Z Hunk #17 succeeded at 3800 (offset -22 lines).
2026-05-03T01:20:35.5634493Z patching file fs/namespace.c
2026-05-03T01:20:35.5636646Z Hunk #11 succeeded at 2397 (offset -23 lines).
2026-05-03T01:20:35.5637063Z Hunk #12 succeeded at 3014 (offset -26 lines).
2026-05-03T01:20:35.5637477Z Hunk #13 succeeded at 3100 (offset -26 lines).
2026-05-03T01:20:35.5637876Z Hunk #14 succeeded at 3123 (offset -26 lines).
2026-05-03T01:20:35.5638282Z Hunk #15 succeeded at 3168 (offset -26 lines).
2026-05-03T01:20:35.5638684Z Hunk #16 succeeded at 3737 (offset -26 lines).
2026-05-03T01:20:35.5639096Z patching file fs/notify/fdinfo.c
2026-05-03T01:20:35.5639662Z Hunk #4 succeeded at 135 (offset 7 lines).
2026-05-03T01:20:35.5640400Z patching file fs/overlayfs/inode.c
2026-05-03T01:20:35.5641985Z patching file fs/overlayfs/readdir.c
2026-05-03T01:20:35.5643648Z patching file fs/overlayfs/super.c
2026-05-03T01:20:35.5645121Z patching file fs/proc/cmdline.c
2026-05-03T01:20:35.5645747Z patching file fs/proc/fd.c
2026-05-03T01:20:35.5647329Z patching file fs/proc/task_mmu.c
2026-05-03T01:20:35.5647791Z Hunk #2 succeeded at 367 with fuzz 1 (offset 17 lines).
2026-05-03T01:20:35.5648301Z Hunk #3 succeeded at 386 with fuzz 2 (offset 18 lines).
2026-05-03T01:20:35.5650431Z patching file fs/proc_namespace.c
2026-05-03T01:20:35.5651528Z patching file fs/readdir.c
2026-05-03T01:20:35.5652983Z patching file fs/stat.c
2026-05-03T01:20:35.5654281Z patching file fs/statfs.c
2026-05-03T01:20:35.5655637Z patching file include/linux/mount.h
2026-05-03T01:20:35.5656854Z patching file include/linux/sched.h
2026-05-03T01:20:35.5657886Z Hunk #1 succeeded at 1319 (offset -6 lines).
2026-05-03T01:20:35.5658311Z Hunk #2 succeeded at 1349 (offset -6 lines).
2026-05-03T01:20:35.5659119Z patching file kernel/kallsyms.c
2026-05-03T01:20:35.5661386Z patching file kernel/sys.c
2026-05-03T01:20:35.5736050Z Applying LCM fix (LCD 0c/0d touchscreen fix)...
2026-05-03T01:20:35.5746266Z patching file drivers/input/touchscreen/mediatek/focaltech_FT8720/focaltech_core.c
2026-05-03T01:20:35.5747449Z Hunk #1 succeeded at 2716 (offset 320 lines).
2026-05-03T01:20:35.5749016Z patching file drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0c_dsc_vdo/Makefile
2026-05-03T01:20:35.5750243Z patching file drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0c_dsc_vdo/data_hw_roundedpattern.h
2026-05-03T01:20:35.5751720Z patching file drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0c_dsc_vdo/dsi_panel_m19a_42_03_0c_dsc_vdo.c
2026-05-03T01:20:35.5754480Z patching file drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0d_dsc_vdo/Makefile
2026-05-03T01:20:35.5755460Z patching file drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0d_dsc_vdo/data_hw_roundedpattern.h
2026-05-03T01:20:35.5756754Z patching file drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0d_dsc_vdo/dsi_panel_m19a_42_03_0d_dsc_vdo.c
2026-05-03T01:20:35.5759482Z patching file drivers/misc/mediatek/lcm/mt65xx_lcm_list.c
2026-05-03T01:20:35.5761089Z patching file drivers/misc/mediatek/lcm/mt65xx_lcm_list.h
2026-05-03T01:20:35.5770320Z patching file drivers/misc/mediatek/leds/mt6768/ktd3136_bl.c
2026-05-03T01:20:35.5770988Z patching file drivers/misc/mediatek/leds/mt6768/ti-lmu-backlight-core.c
2026-05-03T01:20:35.5771566Z Applying primary display fix...
2026-05-03T01:20:35.5784926Z patching file drivers/misc/mediatek/video/mt6768/videox/primary_display.c
2026-05-03T01:20:35.5794500Z All patches applied
2026-05-03T01:20:35.5823289Z ##[group]Run cd $GITHUB_WORKSPACE/kernel
2026-05-03T01:20:35.5823677Z [36;1mcd $GITHUB_WORKSPACE/kernel[0m
2026-05-03T01:20:35.5823979Z [36;1mDEFCONFIG="arch/arm64/configs/fire_defconfig"[0m
2026-05-03T01:20:35.5824268Z [36;1m[0m
2026-05-03T01:20:35.5824519Z [36;1m# Use reference fire_defconfig as base (stock Xiaomi)[0m
2026-05-03T01:20:35.5824887Z [36;1mif [ -f "../ref_patches/fire_defconfig" ]; then[0m
2026-05-03T01:20:35.5825226Z [36;1m  echo "Using reference fire_defconfig..."[0m
2026-05-03T01:20:35.5825557Z [36;1m  cp ../ref_patches/fire_defconfig $DEFCONFIG[0m
2026-05-03T01:20:35.5825824Z [36;1mfi[0m
2026-05-03T01:20:35.5825998Z [36;1m[0m
2026-05-03T01:20:35.5826174Z [36;1m# KernelSU configs[0m
2026-05-03T01:20:35.5826415Z [36;1mif [ "true" = "true" ]; then[0m
2026-05-03T01:20:35.5826659Z [36;1m  echo "" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5826964Z [36;1m  echo "# KernelSU-Next (Legacy Manual Hook)" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5827344Z [36;1m  echo "CONFIG_KSU=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5827649Z [36;1m  echo "CONFIG_KSU_KPROBES_HOOK=n" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5827975Z [36;1m  echo "CONFIG_KSU_MANUAL_HOOK=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5828243Z [36;1mfi[0m
2026-05-03T01:20:35.5828407Z [36;1m[0m
2026-05-03T01:20:35.5828582Z [36;1m# SUSFS configs[0m
2026-05-03T01:20:35.5828832Z [36;1mif [ "true" = "true" ] && [ "true" = "true" ]; then[0m
2026-05-03T01:20:35.5829119Z [36;1m  echo "" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5829351Z [36;1m  echo "# SUSFS" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5829833Z [36;1m  echo "CONFIG_KSU_SUSFS=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5830153Z [36;1m  echo "CONFIG_KSU_SUSFS_SUS_PATH=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5830491Z [36;1m  echo "CONFIG_KSU_SUSFS_SUS_MOUNT=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5830821Z [36;1m  echo "CONFIG_KSU_SUSFS_SUS_MAP=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5831206Z [36;1m  echo "CONFIG_KSU_SUSFS_AUTO_ADD_SUS_KSU_DEFAULT_MOUNT=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5831651Z [36;1m  echo "CONFIG_KSU_SUSFS_AUTO_ADD_SUS_BIND_MOUNT=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5832026Z [36;1m  echo "CONFIG_KSU_SUSFS_SUS_KSTAT=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5832362Z [36;1m  echo "CONFIG_KSU_SUSFS_TRY_UMOUNT=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5832767Z [36;1m  echo "CONFIG_KSU_SUSFS_AUTO_ADD_TRY_UMOUNT_FOR_BIND_MOUNT=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5833182Z [36;1m  echo "CONFIG_KSU_SUSFS_SPOOF_UNAME=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5833521Z [36;1m  echo "CONFIG_KSU_SUSFS_ENABLE_LOG=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5833884Z [36;1m  echo "CONFIG_KSU_SUSFS_HIDE_KSU_SUSFS_SYMBOLS=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5834497Z [36;1m  echo "CONFIG_KSU_SUSFS_SPOOF_CMDLINE_OR_BOOTCONFIG=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5834904Z [36;1m  echo "CONFIG_KSU_SUSFS_OPEN_REDIRECT=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5835246Z [36;1m  echo "CONFIG_KSU_SUSFS_SUS_SU=n" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5835521Z [36;1mfi[0m
2026-05-03T01:20:35.5835687Z [36;1m[0m
2026-05-03T01:20:35.5835870Z [36;1m# Memory & CPU Optimization[0m
2026-05-03T01:20:35.5836114Z [36;1mecho "" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5836395Z [36;1mecho "# Memory Optimization" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5836683Z [36;1mecho "CONFIG_ZRAM=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5836966Z [36;1mecho "CONFIG_ZSMALLOC=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5837263Z [36;1mecho "CONFIG_COMPACTION=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5837543Z [36;1mecho "CONFIG_KSM=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5837811Z [36;1mecho "CONFIG_HZ_1000=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5838056Z [36;1m[0m
2026-05-03T01:20:35.5838252Z [36;1m# Networking (stable performance)[0m
2026-05-03T01:20:35.5838500Z [36;1mecho "" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5838766Z [36;1mecho "# Networking Performance" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5839242Z [36;1mecho "CONFIG_TCP_CONG_ADVANCED=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5840100Z [36;1mecho "CONFIG_TCP_CONG_BBR=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5840430Z [36;1mecho "CONFIG_IP_NF_TARGET_TTL=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5840746Z [36;1mecho "CONFIG_IP6_NF_TARGET_HL=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5841018Z [36;1m[0m
2026-05-03T01:20:35.5841199Z [36;1m# IPSet Support[0m
2026-05-03T01:20:35.5841421Z [36;1mecho "" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5841652Z [36;1mecho "# IPSet" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5841953Z [36;1mecho "CONFIG_IP_SET=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5842255Z [36;1mecho "CONFIG_IP_SET_MAX=65534" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5842563Z [36;1mecho "CONFIG_IP_SET_BITMAP_IP=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5842904Z [36;1mecho "CONFIG_IP_SET_BITMAP_IPMAC=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5843240Z [36;1mecho "CONFIG_IP_SET_BITMAP_PORT=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5843564Z [36;1mecho "CONFIG_IP_SET_HASH_IP=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5843878Z [36;1mecho "CONFIG_IP_SET_HASH_IPMARK=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5844201Z [36;1mecho "CONFIG_IP_SET_HASH_IPPORT=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5844545Z [36;1mecho "CONFIG_IP_SET_HASH_IPPORTIP=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5844898Z [36;1mecho "CONFIG_IP_SET_HASH_IPPORTNET=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5845239Z [36;1mecho "CONFIG_IP_SET_HASH_IPMAC=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5845554Z [36;1mecho "CONFIG_IP_SET_HASH_MAC=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5845888Z [36;1mecho "CONFIG_IP_SET_HASH_NETPORTNET=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5846218Z [36;1mecho "CONFIG_IP_SET_HASH_NET=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5846534Z [36;1mecho "CONFIG_IP_SET_HASH_NETNET=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5846866Z [36;1mecho "CONFIG_IP_SET_HASH_NETPORT=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5847196Z [36;1mecho "CONFIG_IP_SET_HASH_NETIFACE=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5847520Z [36;1mecho "CONFIG_IP_SET_LIST_SET=y" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5847778Z [36;1m[0m
2026-05-03T01:20:35.5848030Z [36;1m# Branding / Vermagic (MUST MATCH STOCK OR WIFI BREAKS)[0m
2026-05-03T01:20:35.5848341Z [36;1mecho "" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5848582Z [36;1mecho "# Branding" >> $DEFCONFIG[0m
2026-05-03T01:20:35.5849053Z [36;1msed -i 's/CONFIG_LOCALVERSION=".*"/CONFIG_LOCALVERSION="-Castorice-perf-g2da4f2613486"/' $DEFCONFIG[0m
2026-05-03T01:20:35.5849669Z [36;1m[0m
2026-05-03T01:20:35.5849856Z [36;1mecho "=== Defconfig tail ==="[0m
2026-05-03T01:20:35.5850107Z [36;1mtail -40 $DEFCONFIG[0m
2026-05-03T01:20:35.5871596Z shell: /usr/bin/bash -e {0}
2026-05-03T01:20:35.5871830Z env:
2026-05-03T01:20:35.5872011Z   KERNEL_NAME: Castorice
2026-05-03T01:20:35.5872369Z   DEVICE_CODE: fire
2026-05-03T01:20:35.5872582Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:20:35.5873123Z   CLANG_VERSION: ZyC clang version 15.0.7 (https://github.com/llvm/llvm-project 8dfdcc7b7bf66834a761bd8de445840ef68e4d1a)
2026-05-03T01:20:35.5873650Z   LLD_VERSION: LLD 15.0.7 (compatible with GNU linkers)
2026-05-03T01:20:35.5873999Z   KERNEL_HEAD_HASH: 1d1aedfe40b2f5fd06c783b752af0197f38966eb
2026-05-03T01:20:35.5874301Z   KSU_DIR: KernelSU-Next
2026-05-03T01:20:35.5874501Z   KSU_VERSION: 33042
2026-05-03T01:20:35.5874694Z   KERNEL_VERSION: 
2026-05-03T01:20:35.5874874Z   ZIP_NAME: 
2026-05-03T01:20:35.5875053Z ##[endgroup]
2026-05-03T01:20:35.5915395Z Using reference fire_defconfig...
2026-05-03T01:20:35.5966988Z === Defconfig tail ===
2026-05-03T01:20:35.5976516Z CONFIG_KSU_SUSFS_ENABLE_LOG=y
2026-05-03T01:20:35.5976902Z CONFIG_KSU_SUSFS_HIDE_KSU_SUSFS_SYMBOLS=y
2026-05-03T01:20:35.5977247Z CONFIG_KSU_SUSFS_SPOOF_CMDLINE_OR_BOOTCONFIG=y
2026-05-03T01:20:35.5977618Z CONFIG_KSU_SUSFS_OPEN_REDIRECT=y
2026-05-03T01:20:35.5977970Z CONFIG_KSU_SUSFS_SUS_SU=n
2026-05-03T01:20:35.5978179Z 
2026-05-03T01:20:35.5978301Z # Memory Optimization
2026-05-03T01:20:35.5978598Z CONFIG_ZRAM=y
2026-05-03T01:20:35.5979115Z CONFIG_ZSMALLOC=y
2026-05-03T01:20:35.5979560Z CONFIG_COMPACTION=y
2026-05-03T01:20:35.5979848Z CONFIG_KSM=y
2026-05-03T01:20:35.5980106Z CONFIG_HZ_1000=y
2026-05-03T01:20:35.5980277Z 
2026-05-03T01:20:35.5980411Z # Networking Performance
2026-05-03T01:20:35.5980908Z CONFIG_TCP_CONG_ADVANCED=y
2026-05-03T01:20:35.5981222Z CONFIG_TCP_CONG_BBR=y
2026-05-03T01:20:35.5981511Z CONFIG_IP_NF_TARGET_TTL=y
2026-05-03T01:20:35.5981770Z CONFIG_IP6_NF_TARGET_HL=y
2026-05-03T01:20:35.5981895Z 
2026-05-03T01:20:35.5981967Z # IPSet
2026-05-03T01:20:35.5982135Z CONFIG_IP_SET=y
2026-05-03T01:20:35.5982313Z CONFIG_IP_SET_MAX=65534
2026-05-03T01:20:35.5982515Z CONFIG_IP_SET_BITMAP_IP=y
2026-05-03T01:20:35.5982736Z CONFIG_IP_SET_BITMAP_IPMAC=y
2026-05-03T01:20:35.5982972Z CONFIG_IP_SET_BITMAP_PORT=y
2026-05-03T01:20:35.5983186Z CONFIG_IP_SET_HASH_IP=y
2026-05-03T01:20:35.5983388Z CONFIG_IP_SET_HASH_IPMARK=y
2026-05-03T01:20:35.5983603Z CONFIG_IP_SET_HASH_IPPORT=y
2026-05-03T01:20:35.5983814Z CONFIG_IP_SET_HASH_IPPORTIP=y
2026-05-03T01:20:35.5984051Z CONFIG_IP_SET_HASH_IPPORTNET=y
2026-05-03T01:20:35.5984267Z CONFIG_IP_SET_HASH_IPMAC=y
2026-05-03T01:20:35.5984477Z CONFIG_IP_SET_HASH_MAC=y
2026-05-03T01:20:35.5984686Z CONFIG_IP_SET_HASH_NETPORTNET=y
2026-05-03T01:20:35.5984920Z CONFIG_IP_SET_HASH_NET=y
2026-05-03T01:20:35.5985135Z CONFIG_IP_SET_HASH_NETNET=y
2026-05-03T01:20:35.5985353Z CONFIG_IP_SET_HASH_NETPORT=y
2026-05-03T01:20:35.5985570Z CONFIG_IP_SET_HASH_NETIFACE=y
2026-05-03T01:20:35.5985776Z CONFIG_IP_SET_LIST_SET=y
2026-05-03T01:20:35.5985897Z 
2026-05-03T01:20:35.5985975Z # Branding
2026-05-03T01:20:35.6007527Z ##[group]Run cd $GITHUB_WORKSPACE/kernel
2026-05-03T01:20:35.6007872Z [36;1mcd $GITHUB_WORKSPACE/kernel[0m
2026-05-03T01:20:35.6008110Z [36;1m[0m
2026-05-03T01:20:35.6008380Z [36;1mecho "=== Fixing modern Clang vs 4.19 incompatibilities ==="[0m
2026-05-03T01:20:35.6008714Z [36;1m[0m
2026-05-03T01:20:35.6009009Z [36;1m# Step 1: Remove ENTIRE compound -Werror=xxx flags from all Makefiles[0m
2026-05-03T01:20:35.6009791Z [36;1m# Must come BEFORE removing standalone -Werror to avoid leaving orphan '=xxx'[0m
2026-05-03T01:20:35.6010225Z [36;1mecho "Removing compound -Werror=xxx flags..."[0m
2026-05-03T01:20:35.6010587Z [36;1mfind . -type f \( -name "Makefile" -o -name "Kbuild" \) \[0m
2026-05-03T01:20:35.6010948Z [36;1m  -exec sed -i 's/-Werror=[a-zA-Z_-]*//g' {} +[0m
2026-05-03T01:20:35.6011211Z [36;1m[0m
2026-05-03T01:20:35.6011496Z [36;1m# Step 2: Remove standalone -Werror (safe now since compounds are gone)[0m
2026-05-03T01:20:35.6011915Z [36;1mecho "Removing standalone -Werror..."[0m
2026-05-03T01:20:35.6012242Z [36;1mfind . -type f \( -name "Makefile" -o -name "Kbuild" \) \[0m
2026-05-03T01:20:35.6012630Z [36;1m  -exec sed -i 's/ -Werror / /g; s/ -Werror$//g; s/^-Werror //g' {} +[0m
2026-05-03T01:20:35.6013111Z [36;1m[0m
2026-05-03T01:20:35.6013406Z [36;1m# Step 3: Remove GCC-specific warning flags that clang doesn't understand[0m
2026-05-03T01:20:35.6013839Z [36;1mecho "Removing clang-incompatible warning flags..."[0m
2026-05-03T01:20:35.6014199Z [36;1mfind . -type f \( -name "Makefile" -o -name "Kbuild" \) \[0m
2026-05-03T01:20:35.6014565Z [36;1m  -exec sed -i 's/-Wno-unused-but-set-variable//g' {} + \[0m
2026-05-03T01:20:35.6014938Z [36;1m  -exec sed -i 's/-Wno-unused-but-set-parameter//g' {} + \[0m
2026-05-03T01:20:35.6015306Z [36;1m  -exec sed -i 's/-Wunused-but-set-variable//g' {} + \[0m
2026-05-03T01:20:35.6015670Z [36;1m  -exec sed -i 's/-Wunused-but-set-parameter//g' {} +[0m
2026-05-03T01:20:35.6015961Z [36;1m[0m
2026-05-03T01:20:35.6016241Z [36;1m# Step 4: Fix strict-prototypes (clang 15+ enforces C2x no-K&R rule)[0m
2026-05-03T01:20:35.6016637Z [36;1mecho "Fixing strict-prototypes issues..."[0m
2026-05-03T01:20:35.6017051Z [36;1m# zram_debugfs_init / destroy sed removed because they corrupt function calls.[0m
2026-05-03T01:20:35.6017528Z [36;1m# -Wno-strict-prototypes is already added below to handle this.[0m
2026-05-03T01:20:35.6017852Z [36;1m[0m
2026-05-03T01:20:35.6018055Z [36;1m# Step 5: Add clang compatibility CFLAGS[0m
2026-05-03T01:20:35.6018444Z [36;1m# CRITICAL: Append at END of Makefile, NOT inside the KBUILD_CFLAGS := block![0m
2026-05-03T01:20:35.6018897Z [36;1m# The old sed '/^KBUILD_CFLAGS.*:=/a ...' was inserting lines in the[0m
2026-05-03T01:20:35.6019544Z [36;1m# middle of a multi-line backslash-continuation block, breaking Makefile syntax.[0m
2026-05-03T01:20:35.6020204Z [36;1m# Error was: "Makefile:447: *** recipe commences before first target. Stop."[0m
2026-05-03T01:20:35.6020581Z [36;1mif [ -f "Makefile" ]; then[0m
2026-05-03T01:20:35.6020938Z [36;1m  echo "Adding clang compatibility CFLAGS (appending to end of Makefile)..."[0m
2026-05-03T01:20:35.6021335Z [36;1m  cat >> Makefile << 'CLANG_COMPAT_EOF'[0m
2026-05-03T01:20:35.6021591Z [36;1m[0m
2026-05-03T01:20:35.6021807Z [36;1m# Clang compatibility flags (appended by CI)[0m
2026-05-03T01:20:35.6022087Z [36;1mKBUILD_CFLAGS += -Wno-error[0m
2026-05-03T01:20:35.6022438Z [36;1mKBUILD_CFLAGS += -Wno-implicit-function-declaration[0m
2026-05-03T01:20:35.6022781Z [36;1mKBUILD_CFLAGS += -Wno-strict-prototypes[0m
2026-05-03T01:20:35.6023067Z [36;1mKBUILD_CFLAGS += -Wno-return-type[0m
2026-05-03T01:20:35.6023368Z [36;1mKBUILD_CFLAGS += -Wno-unknown-warning-option[0m
2026-05-03T01:20:35.6023668Z [36;1mKBUILD_CFLAGS += -Wno-int-conversion[0m
2026-05-03T01:20:35.6023953Z [36;1mKBUILD_CFLAGS += -Wno-unused-function[0m
2026-05-03T01:20:35.6024262Z [36;1mKBUILD_CFLAGS += -Wno-misleading-indentation[0m
2026-05-03T01:20:35.6024736Z [36;1mKBUILD_CFLAGS += -Wno-bool-operation[0m
2026-05-03T01:20:35.6025024Z [36;1mKBUILD_CFLAGS += -Wno-uninitialized[0m
2026-05-03T01:20:35.6025285Z [36;1mCLANG_COMPAT_EOF[0m
2026-05-03T01:20:35.6025542Z [36;1m  echo "Clang CFLAGS appended successfully"[0m
2026-05-03T01:20:35.6025813Z [36;1mfi[0m
2026-05-03T01:20:35.6025980Z [36;1m[0m
2026-05-03T01:20:35.6026176Z [36;1mecho "=== Compiler fixes applied ==="[0m
2026-05-03T01:20:35.6046517Z shell: /usr/bin/bash -e {0}
2026-05-03T01:20:35.6046750Z env:
2026-05-03T01:20:35.6046937Z   KERNEL_NAME: Castorice
2026-05-03T01:20:35.6047155Z   DEVICE_CODE: fire
2026-05-03T01:20:35.6047374Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:20:35.6047896Z   CLANG_VERSION: ZyC clang version 15.0.7 (https://github.com/llvm/llvm-project 8dfdcc7b7bf66834a761bd8de445840ef68e4d1a)
2026-05-03T01:20:35.6048429Z   LLD_VERSION: LLD 15.0.7 (compatible with GNU linkers)
2026-05-03T01:20:35.6048778Z   KERNEL_HEAD_HASH: 1d1aedfe40b2f5fd06c783b752af0197f38966eb
2026-05-03T01:20:35.6049087Z   KSU_DIR: KernelSU-Next
2026-05-03T01:20:35.6049305Z   KSU_VERSION: 33042
2026-05-03T01:20:35.6049692Z   KERNEL_VERSION: 
2026-05-03T01:20:35.6049883Z   ZIP_NAME: 
2026-05-03T01:20:35.6050204Z ##[endgroup]
2026-05-03T01:20:35.6088999Z === Fixing modern Clang vs 4.19 incompatibilities ===
2026-05-03T01:20:35.6089628Z Removing compound -Werror=xxx flags...
2026-05-03T01:20:36.2367436Z Removing standalone -Werror...
2026-05-03T01:20:36.8966425Z Removing clang-incompatible warning flags...
2026-05-03T01:20:39.7662294Z Fixing strict-prototypes issues...
2026-05-03T01:20:39.7662935Z Adding clang compatibility CFLAGS (appending to end of Makefile)...
2026-05-03T01:20:39.7677977Z Clang CFLAGS appended successfully
2026-05-03T01:20:39.7678504Z === Compiler fixes applied ===
2026-05-03T01:20:39.7714919Z ##[group]Run cd $GITHUB_WORKSPACE/kernel
2026-05-03T01:20:39.7715414Z [36;1mcd $GITHUB_WORKSPACE/kernel[0m
2026-05-03T01:20:39.7715773Z [36;1m[0m
2026-05-03T01:20:39.7716068Z [36;1mexport KBUILD_BUILD_USER=Castorice[0m
2026-05-03T01:20:39.7716507Z [36;1mexport KBUILD_BUILD_HOST=naidrahiqa[0m
2026-05-03T01:20:39.7716925Z [36;1mexport KBUILD_BUILD_VERSION=1[0m
2026-05-03T01:20:39.7717287Z [36;1m[0m
2026-05-03T01:20:39.7717637Z [36;1mARGS="PATH=$GITHUB_WORKSPACE/ZyClang/bin:$PATH \[0m
2026-05-03T01:20:39.7718100Z [36;1m  ARCH=arm64 \[0m
2026-05-03T01:20:39.7718417Z [36;1m  SUBARCH=arm64 \[0m
2026-05-03T01:20:39.7718780Z [36;1m  CROSS_COMPILE=aarch64-linux-gnu- \[0m
2026-05-03T01:20:39.7719246Z [36;1m  CROSS_COMPILE_ARM32=arm-linux-gnueabi- \[0m
2026-05-03T01:20:39.7719840Z [36;1m  CC=clang \[0m
2026-05-03T01:20:39.7720131Z [36;1m  NM=llvm-nm \[0m
2026-05-03T01:20:39.7720434Z [36;1m  CXX=clang++ \[0m
2026-05-03T01:20:39.7720734Z [36;1m  AR=llvm-ar \[0m
2026-05-03T01:20:39.7721073Z [36;1m  LD=ld.lld \[0m
2026-05-03T01:20:39.7721388Z [36;1m  STRIP=llvm-strip \[0m
2026-05-03T01:20:39.7721737Z [36;1m  OBJCOPY=llvm-objcopy \[0m
2026-05-03T01:20:39.7722093Z [36;1m  OBJDUMP=llvm-objdump \[0m
2026-05-03T01:20:39.7722447Z [36;1m  OBJSIZE=llvm-size \[0m
2026-05-03T01:20:39.7722786Z [36;1m  READELF=llvm-readelf \[0m
2026-05-03T01:20:39.7723132Z [36;1m  HOSTAR=llvm-ar \[0m
2026-05-03T01:20:39.7723471Z [36;1m  HOSTLD=ld.lld \[0m
2026-05-03T01:20:39.7723793Z [36;1m  HOSTCC=clang \[0m
2026-05-03T01:20:39.7724103Z [36;1m  HOSTCXX=clang++ \[0m
2026-05-03T01:20:39.7724428Z [36;1m  LLVM=1"[0m
2026-05-03T01:20:39.7724701Z [36;1m[0m
2026-05-03T01:20:39.7724950Z [36;1m# Generate .config[0m
2026-05-03T01:20:39.7725274Z [36;1mrm -rf out[0m
2026-05-03T01:20:39.7725583Z [36;1mmake O=out $ARGS fire_defconfig[0m
2026-05-03T01:20:39.7725951Z [36;1m[0m
2026-05-03T01:20:39.7726401Z [36;1mKERNEL_VERSION=$(make O=out $ARGS kernelversion 2>/dev/null | grep "4.19")[0m
2026-05-03T01:20:39.7727058Z [36;1mecho "KERNEL_VERSION=$KERNEL_VERSION" >> $GITHUB_ENV[0m
2026-05-03T01:20:39.7727577Z [36;1mecho "=== Building Linux $KERNEL_VERSION ==="[0m
2026-05-03T01:20:39.7727985Z [36;1m[0m
2026-05-03T01:20:39.7728231Z [36;1m# Build[0m
2026-05-03T01:20:39.7728607Z [36;1mmake O=out $ARGS -j"$(nproc --all)" 2>&1 | tee build.log[0m
2026-05-03T01:20:39.7729068Z [36;1m[0m
2026-05-03T01:20:39.7729311Z [36;1m# Verify[0m
2026-05-03T01:20:39.7729787Z [36;1mIMAGE="out/arch/arm64/boot/Image.gz-dtb"[0m
2026-05-03T01:20:39.7730200Z [36;1mif [ ! -f "$IMAGE" ]; then[0m
2026-05-03T01:20:39.7730621Z [36;1m  echo "BUILD FAILED! Image.gz-dtb not found"[0m
2026-05-03T01:20:39.7731042Z [36;1m  tail -100 build.log[0m
2026-05-03T01:20:39.7731371Z [36;1m  exit 1[0m
2026-05-03T01:20:39.7731634Z [36;1mfi[0m
2026-05-03T01:20:39.7731905Z [36;1mecho "BUILD SUCCESS: $IMAGE"[0m
2026-05-03T01:20:39.7732273Z [36;1mls -lah $IMAGE[0m
2026-05-03T01:20:39.7760297Z shell: /usr/bin/bash -e {0}
2026-05-03T01:20:39.7760638Z env:
2026-05-03T01:20:39.7760889Z   KERNEL_NAME: Castorice
2026-05-03T01:20:39.7761233Z   DEVICE_CODE: fire
2026-05-03T01:20:39.7761550Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:20:39.7762352Z   CLANG_VERSION: ZyC clang version 15.0.7 (https://github.com/llvm/llvm-project 8dfdcc7b7bf66834a761bd8de445840ef68e4d1a)
2026-05-03T01:20:39.7763180Z   LLD_VERSION: LLD 15.0.7 (compatible with GNU linkers)
2026-05-03T01:20:39.7763915Z   KERNEL_HEAD_HASH: 1d1aedfe40b2f5fd06c783b752af0197f38966eb
2026-05-03T01:20:39.7764380Z   KSU_DIR: KernelSU-Next
2026-05-03T01:20:39.7764685Z   KSU_VERSION: 33042
2026-05-03T01:20:39.7764962Z   KERNEL_VERSION: 
2026-05-03T01:20:39.7765234Z   ZIP_NAME: 
2026-05-03T01:20:39.7765480Z ##[endgroup]
2026-05-03T01:20:39.8222054Z make[1]: Entering directory '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/out'
2026-05-03T01:20:40.1574039Z   HOSTCC  scripts/basic/fixdep
2026-05-03T01:20:40.4937644Z   GEN     ./Makefile
2026-05-03T01:20:40.5119745Z   HOSTCC  scripts/kconfig/conf.o
2026-05-03T01:20:40.6719328Z   YACC    scripts/kconfig/zconf.tab.c
2026-05-03T01:20:40.8596234Z   LEX     scripts/kconfig/zconf.lex.c
2026-05-03T01:20:40.9975994Z   HOSTCC  scripts/kconfig/zconf.tab.o
2026-05-03T01:20:42.1946051Z   HOSTLD  scripts/kconfig/conf
2026-05-03T01:20:42.5987749Z drivers/misc/mediatek/base/power/Kconfig:90:warning: ignoring type redefinition of 'MTK_QOS_FRAMEWORK' from 'tristate' to 'bool'
2026-05-03T01:20:42.6148103Z drivers/input/touchscreen/mediatek/goodix_berlin_driver/Kconfig:4:warning: ignoring type redefinition of 'TOUCHSCREEN_GOODIX_BRL' from 'bool' to 'tristate'
2026-05-03T01:20:42.6217009Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T01:20:42.6218302Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T01:20:42.6219887Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T01:20:42.6221126Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T01:20:42.6222469Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T01:20:42.6223776Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T01:20:42.6225182Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T01:20:42.6226513Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T01:20:42.6227908Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T01:20:42.6229217Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T01:20:42.6230713Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T01:20:42.6544952Z drivers/soc/mediatek/Kconfig:7:warning: ignoring type redefinition of 'MTK_CMDQ' from 'bool' to 'tristate'
2026-05-03T01:20:42.7623889Z drivers/input/touchscreen/mediatek/hxchipset_hx83102p/Kconfig:19:warning: choice value used outside its choice group
2026-05-03T01:20:42.7625211Z drivers/input/touchscreen/mediatek/hxchipset_hx83102p/Kconfig:28:warning: choice value used outside its choice group
2026-05-03T01:20:42.7626679Z drivers/input/touchscreen/mediatek/hxchipset_hx83102p/Kconfig:16:warning: choice default symbol 'TOUCHSCREEN_HIMAX_INCELL' is not contained in the choice
2026-05-03T01:20:42.7922547Z arch/arm64/configs/fire_defconfig:447:warning: override: reassigning to symbol CMDLINE_FORCE
2026-05-03T01:20:42.7923514Z arch/arm64/configs/fire_defconfig:448:warning: override: reassigning to symbol EFI
2026-05-03T01:20:42.7959069Z arch/arm64/configs/fire_defconfig:5548:warning: override: reassigning to symbol CRYPTO_GHASH_ARM64_CE
2026-05-03T01:20:42.7960201Z arch/arm64/configs/fire_defconfig:5573:warning: override: reassigning to symbol ZRAM
2026-05-03T01:20:42.7961628Z arch/arm64/configs/fire_defconfig:5574:warning: override: reassigning to symbol ZSMALLOC
2026-05-03T01:20:42.7962572Z arch/arm64/configs/fire_defconfig:5575:warning: override: reassigning to symbol COMPACTION
2026-05-03T01:20:42.7963477Z arch/arm64/configs/fire_defconfig:5576:warning: override: reassigning to symbol KSM
2026-05-03T01:20:42.7964359Z arch/arm64/configs/fire_defconfig:5577:warning: override: reassigning to symbol HZ_1000
2026-05-03T01:20:42.7965485Z arch/arm64/configs/fire_defconfig:5577:warning: override: HZ_1000 changes choice state
2026-05-03T01:20:42.7966470Z arch/arm64/configs/fire_defconfig:5580:warning: override: reassigning to symbol TCP_CONG_ADVANCED
2026-05-03T01:20:42.7967445Z arch/arm64/configs/fire_defconfig:5581:warning: override: reassigning to symbol TCP_CONG_BBR
2026-05-03T01:20:42.7968419Z arch/arm64/configs/fire_defconfig:5582:warning: override: reassigning to symbol IP_NF_TARGET_TTL
2026-05-03T01:20:42.7969619Z arch/arm64/configs/fire_defconfig:5583:warning: override: reassigning to symbol IP6_NF_TARGET_HL
2026-05-03T01:20:42.7970536Z arch/arm64/configs/fire_defconfig:5586:warning: override: reassigning to symbol IP_SET
2026-05-03T01:20:42.7976140Z 
2026-05-03T01:20:42.7976596Z WARNING: unmet direct dependencies detected for BACKLIGHT_CLASS_DEVICE
2026-05-03T01:20:42.7977083Z   Depends on [n]: HAS_IOMEM [=y] && BACKLIGHT_LCD_SUPPORT [=n]
2026-05-03T01:20:42.7977400Z   Selected by [y]:
2026-05-03T01:20:42.7977607Z   - LM3697_SUPPORT [=y]
2026-05-03T01:20:42.8014671Z 
2026-05-03T01:20:42.8015052Z WARNING: unmet direct dependencies detected for MTK_PID_MAP
2026-05-03T01:20:42.8015836Z   Depends on [n]: (MTK_GMO_RAM_OPTIMIZE [=n] && MTK_ENG_BUILD [=n] || !MTK_GMO_RAM_OPTIMIZE [=n]) && DEBUG_FS [=n]
2026-05-03T01:20:42.8016483Z   Selected by [y]:
2026-05-03T01:20:42.8016754Z   - MACH_MT6768 [=y]
2026-05-03T01:20:42.8024172Z 
2026-05-03T01:20:42.8024600Z WARNING: unmet direct dependencies detected for MTK_CACHE_PARITY_CHECK
2026-05-03T01:20:42.8025119Z   Depends on [n]: MTK_SDA [=n]
2026-05-03T01:20:42.8025439Z   Selected by [y]:
2026-05-03T01:20:42.8025708Z   - MACH_MT6768 [=y]
2026-05-03T01:20:42.8062611Z 
2026-05-03T01:20:42.8063049Z WARNING: unmet direct dependencies detected for BACKLIGHT_CLASS_DEVICE
2026-05-03T01:20:42.8063711Z   Depends on [n]: HAS_IOMEM [=y] && BACKLIGHT_LCD_SUPPORT [=n]
2026-05-03T01:20:42.8064167Z   Selected by [y]:
2026-05-03T01:20:42.8064445Z   - LM3697_SUPPORT [=y]
2026-05-03T01:20:42.8087543Z 
2026-05-03T01:20:42.8087914Z WARNING: unmet direct dependencies detected for MTK_PID_MAP
2026-05-03T01:20:42.8088758Z   Depends on [n]: (MTK_GMO_RAM_OPTIMIZE [=n] && MTK_ENG_BUILD [=n] || !MTK_GMO_RAM_OPTIMIZE [=n]) && DEBUG_FS [=n]
2026-05-03T01:20:42.8089636Z   Selected by [y]:
2026-05-03T01:20:42.8089934Z   - MACH_MT6768 [=y]
2026-05-03T01:20:42.8091401Z 
2026-05-03T01:20:42.8091718Z WARNING: unmet direct dependencies detected for MTK_CACHE_PARITY_CHECK
2026-05-03T01:20:42.8092249Z   Depends on [n]: MTK_SDA [=n]
2026-05-03T01:20:42.8092591Z   Selected by [y]:
2026-05-03T01:20:42.8092867Z   - MACH_MT6768 [=y]
2026-05-03T01:20:42.8836164Z #
2026-05-03T01:20:42.8836500Z # configuration written to .config
2026-05-03T01:20:42.8836891Z #
2026-05-03T01:20:42.8860035Z make[1]: Leaving directory '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/out'
2026-05-03T01:20:44.3010146Z === Building Linux 4.19.191 ===
2026-05-03T01:20:44.3074991Z make[1]: Entering directory '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/out'
2026-05-03T01:20:45.5843232Z   UPD     include/config/kernel.release
2026-05-03T01:20:45.5958160Z   GEN     ./Makefile
2026-05-03T01:20:45.6021478Z   WRAP    arch/arm64/include/generated/uapi/asm/errno.h
2026-05-03T01:20:45.6024406Z   WRAP    arch/arm64/include/generated/uapi/asm/ioctl.h
2026-05-03T01:20:45.6027982Z   WRAP    arch/arm64/include/generated/uapi/asm/ioctls.h
2026-05-03T01:20:45.6040607Z   WRAP    arch/arm64/include/generated/uapi/asm/ipcbuf.h
2026-05-03T01:20:45.6041810Z   WRAP    arch/arm64/include/generated/uapi/asm/kvm_para.h
2026-05-03T01:20:45.6051770Z   WRAP    arch/arm64/include/generated/uapi/asm/mman.h
2026-05-03T01:20:45.6055076Z   WRAP    arch/arm64/include/generated/uapi/asm/msgbuf.h
2026-05-03T01:20:45.6055591Z   WRAP    arch/arm64/include/generated/uapi/asm/poll.h
2026-05-03T01:20:45.6062749Z   WRAP    arch/arm64/include/generated/uapi/asm/sembuf.h
2026-05-03T01:20:45.6070382Z   WRAP    arch/arm64/include/generated/uapi/asm/resource.h
2026-05-03T01:20:45.6072829Z   WRAP    arch/arm64/include/generated/uapi/asm/shmbuf.h
2026-05-03T01:20:45.6073739Z   WRAP    arch/arm64/include/generated/uapi/asm/socket.h
2026-05-03T01:20:45.6084778Z   WRAP    arch/arm64/include/generated/uapi/asm/sockios.h
2026-05-03T01:20:45.6085579Z   WRAP    arch/arm64/include/generated/uapi/asm/swab.h
2026-05-03T01:20:45.6086357Z   WRAP    arch/arm64/include/generated/uapi/asm/termbits.h
2026-05-03T01:20:45.6092216Z   WRAP    arch/arm64/include/generated/uapi/asm/termios.h
2026-05-03T01:20:45.6101455Z   WRAP    arch/arm64/include/generated/uapi/asm/types.h
2026-05-03T01:20:45.6173351Z   UPD     include/generated/uapi/linux/version.h
2026-05-03T01:20:45.6475158Z   UPD     include/generated/utsrelease.h
2026-05-03T01:20:46.3218710Z $GED: CONFIG_MTK_PLATFORM is ["mt6768"]
2026-05-03T01:20:46.3310261Z *MTK_GPU_VERSION 2 = valhall
2026-05-03T01:20:46.3390358Z *MTK_GPU_VERSION 3 = r32p1
2026-05-03T01:20:46.3442231Z mali MTK evironment, building r32p1 DDK
2026-05-03T01:20:46.3443435Z mtk-Kbuild CONFIG_MALI_PLATFORM_THIRDPARTY := y
2026-05-03T01:20:46.3444237Z mtk-Kbuild CONFIG_MALI_PLATFORM_THIRDPARTY_NAME := "mt6768"
2026-05-03T01:20:46.3444953Z mali MTK evironment, building r32p1 DDK
2026-05-03T01:20:46.3445551Z mtk-Kbuild CONFIG_MALI_PLATFORM_THIRDPARTY := y
2026-05-03T01:20:46.3446350Z mtk-Kbuild CONFIG_MALI_PLATFORM_THIRDPARTY_NAME := "mt6768"
2026-05-03T01:20:46.3447121Z mali MTK evironment, building r32p1 DDK
2026-05-03T01:20:46.3447728Z mtk-Kbuild CONFIG_MALI_PLATFORM_THIRDPARTY := y
2026-05-03T01:20:46.3448438Z mtk-Kbuild CONFIG_MALI_PLATFORM_THIRDPARTY_NAME := "mt6768"
2026-05-03T01:20:46.3550634Z   Using .. as source for kernel
2026-05-03T01:20:46.3952277Z   WRAP    arch/arm64/include/generated/asm/bugs.h
2026-05-03T01:20:46.3963479Z   WRAP    arch/arm64/include/generated/asm/delay.h
2026-05-03T01:20:46.3980022Z   WRAP    arch/arm64/include/generated/asm/div64.h
2026-05-03T01:20:46.3989954Z   WRAP    arch/arm64/include/generated/asm/dma.h
2026-05-03T01:20:46.4001984Z   WRAP    arch/arm64/include/generated/asm/dma-contiguous.h
2026-05-03T01:20:46.4002904Z   WRAP    arch/arm64/include/generated/asm/early_ioremap.h
2026-05-03T01:20:46.4028356Z   WRAP    arch/arm64/include/generated/asm/emergency-restart.h
2026-05-03T01:20:46.4054163Z   WRAP    arch/arm64/include/generated/asm/hw_irq.h
2026-05-03T01:20:46.4056759Z   WRAP    arch/arm64/include/generated/asm/irq_regs.h
2026-05-03T01:20:46.4057676Z   WRAP    arch/arm64/include/generated/asm/kdebug.h
2026-05-03T01:20:46.4062921Z   WRAP    arch/arm64/include/generated/asm/kmap_types.h
2026-05-03T01:20:46.4083992Z   WRAP    arch/arm64/include/generated/asm/local.h
2026-05-03T01:20:46.4088771Z   WRAP    arch/arm64/include/generated/asm/local64.h
2026-05-03T01:20:46.4107420Z   WRAP    arch/arm64/include/generated/asm/mcs_spinlock.h
2026-05-03T01:20:46.4120180Z   WRAP    arch/arm64/include/generated/asm/mm-arch-hooks.h
2026-05-03T01:20:46.4150049Z   WRAP    arch/arm64/include/generated/asm/msi.h
2026-05-03T01:20:46.4176784Z   WRAP    arch/arm64/include/generated/asm/preempt.h
2026-05-03T01:20:46.4181763Z   WRAP    arch/arm64/include/generated/asm/qrwlock.h
2026-05-03T01:20:46.4182543Z   WRAP    arch/arm64/include/generated/asm/qspinlock.h
2026-05-03T01:20:46.4183094Z   WRAP    arch/arm64/include/generated/asm/rwsem.h
2026-05-03T01:20:46.4183585Z   WRAP    arch/arm64/include/generated/asm/segment.h
2026-05-03T01:20:46.4184864Z   WRAP    arch/arm64/include/generated/asm/serial.h
2026-05-03T01:20:46.4200131Z   WRAP    arch/arm64/include/generated/asm/set_memory.h
2026-05-03T01:20:46.4228800Z   WRAP    arch/arm64/include/generated/asm/sizes.h
2026-05-03T01:20:46.4229708Z   WRAP    arch/arm64/include/generated/asm/switch_to.h
2026-05-03T01:20:46.4230379Z   WRAP    arch/arm64/include/generated/asm/trace_clock.h
2026-05-03T01:20:46.4240846Z   WRAP    arch/arm64/include/generated/asm/unaligned.h
2026-05-03T01:20:46.4259549Z   WRAP    arch/arm64/include/generated/asm/user.h
2026-05-03T01:20:46.4266419Z   WRAP    arch/arm64/include/generated/asm/vga.h
2026-05-03T01:20:46.4275130Z   WRAP    arch/arm64/include/generated/asm/xor.h
2026-05-03T01:20:46.5650731Z   HOSTCC  scripts/dtc/dtc.o
2026-05-03T01:20:46.5800507Z   HOSTCC  scripts/dtc/flattree.o
2026-05-03T01:20:46.7220953Z   HOSTCC  scripts/genksyms/genksyms.o
2026-05-03T01:20:46.7350963Z -- KernelSU-Next Git repo detected at: /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/KernelSU-Next
2026-05-03T01:20:46.7380522Z -- KernelSU-Next version: 33132
2026-05-03T01:20:46.7409972Z -- KernelSU-Next tag: v3.2.0-legacy
2026-05-03T01:20:46.7451627Z -- KernelSU-Next Manager signature size: 0x3e6
2026-05-03T01:20:46.7479206Z -- KernelSU-Next Manager signature hash: 79e590113c4c4c0c222978e413a5faa801666957b1212a328e46c00c69821bf7
2026-05-03T01:20:46.7490870Z -- KernelSU-Next: Hook mode: Manual
2026-05-03T01:20:46.7491770Z -- KSU_NEXT: adding function 'static int can_umount(const struct path *path, int flags);' to ../fs/namespace.c
2026-05-03T01:20:46.7493069Z -- KSU_NEXT: adding function 'int path_umount(struct path *path, int flags);' to ../fs/namespace.c
2026-05-03T01:20:46.7600426Z -- KSU_NEXT: adding 'int path_umount(struct path *path, int flags);' to ../fs/internal.h
2026-05-03T01:20:46.7630006Z -- KSU_NEXT: patching struct seccomp for filter_count
2026-05-03T01:20:46.7660001Z -- KSU_NEXT: patching selinux/hooks.c for selinux_inode
2026-05-03T01:20:46.7870431Z -- KSU_NEXT: patching selinux/selinuxfs.c for selinux_inode
2026-05-03T01:20:46.7920166Z -- KSU_NEXT: patching selinux/xfrm.c for selinux_cred
2026-05-03T01:20:46.7960185Z -- KSU_NEXT: patching selinux/include/objsec.h for selinux_inode
2026-05-03T01:20:46.8020289Z -- KSU_NEXT: patching selinux/include/objsec.h for selinux_cred
2026-05-03T01:20:46.8220728Z   HOSTCC  scripts/dtc/fstree.o
2026-05-03T01:20:46.8898916Z   HOSTCC  scripts/dtc/data.o
2026-05-03T01:20:46.9060536Z   HOSTCC  scripts/dtc/livetree.o
2026-05-03T01:20:46.9420369Z   YACC    scripts/genksyms/parse.tab.c
2026-05-03T01:20:47.0605290Z   CC      scripts/mod/empty.o
2026-05-03T01:20:47.0754347Z   LEX     scripts/genksyms/lex.lex.c
2026-05-03T01:20:47.0845733Z   YACC    scripts/genksyms/parse.tab.h
2026-05-03T01:20:47.1180533Z   HOSTCC  scripts/mod/mk_elfconfig
2026-05-03T01:20:47.2040506Z   CC      scripts/mod/devicetable-offsets.s
2026-05-03T01:20:47.2161100Z   HOSTCC  scripts/genksyms/parse.tab.o
2026-05-03T01:20:47.2379769Z   HOSTCC  scripts/dtc/treesource.o
2026-05-03T01:20:47.2460902Z   MKELF   scripts/mod/elfconfig.h
2026-05-03T01:20:47.2490110Z   HOSTCC  scripts/mod/modpost.o
2026-05-03T01:20:47.3760510Z   HOSTCC  scripts/dtc/srcpos.o
2026-05-03T01:20:47.3790255Z   HOSTCC  scripts/genksyms/lex.lex.o
2026-05-03T01:20:47.5120759Z   HOSTCC  scripts/dtc/checks.o
2026-05-03T01:20:47.5820794Z ../drivers/misc/mediatek/base/power/cpufreq_v1/src/Makefile:89: "use CONFIG_MTK_TINYSYS_SSPM_V1"
2026-05-03T01:20:47.7740587Z ../drivers/misc/mediatek/base/power/ppm_v3/src/Makefile:110: USE_PPM_CPI
2026-05-03T01:20:47.7860421Z   HOSTLD  scripts/genksyms/genksyms
2026-05-03T01:20:47.8430574Z   UPD     scripts/mod/devicetable-offsets.h
2026-05-03T01:20:47.8448714Z   HOSTCC  scripts/dtc/util.o
2026-05-03T01:20:47.9200593Z   HOSTCC  scripts/mod/sumversion.o
2026-05-03T01:20:47.9436084Z   CC      kernel/bounds.s
2026-05-03T01:20:47.9610494Z ..
2026-05-03T01:20:47.9700098Z FDVT: Drv use 4.0 folder
2026-05-03T01:20:47.9759919Z ..
2026-05-03T01:20:47.9840117Z   LEX     scripts/dtc/dtc-lexer.lex.c
2026-05-03T01:20:47.9895263Z ..
2026-05-03T01:20:47.9960213Z   YACC    scripts/dtc/dtc-parser.tab.h
2026-05-03T01:20:48.0460740Z   UPD     include/generated/timeconst.h
2026-05-03T01:20:48.0487803Z ../drivers/misc/mediatek/ccu/src/Makefile:33: CCU_MAKE_FILE_CALLED
2026-05-03T01:20:48.0537064Z   UPD     include/generated/bounds.h
2026-05-03T01:20:48.0556521Z ../drivers/misc/mediatek/ccu/src/1.2/Makefile:28: CCU_INC=../drivers/misc/mediatek/ccu/src/mt6768/ccu_ext_interface
2026-05-03T01:20:48.0570512Z   CC      arch/arm64/kernel/asm-offsets.s
2026-05-03T01:20:48.1290397Z   YACC    scripts/dtc/dtc-parser.tab.c
2026-05-03T01:20:48.1350129Z   HOSTCC  scripts/mod/file2alias.o
2026-05-03T01:20:48.2610624Z CONFIG_MTK_PLATFORM_CCCI := mt6768
2026-05-03T01:20:48.2650432Z CONFIG_MTK_PLATFORM_CCCI := "mt6768"
2026-05-03T01:20:48.2680218Z MTK_PLATFORM_CCCI := mt6768
2026-05-03T01:20:48.2709997Z   HOSTCC  scripts/dtc/yamltree.o
2026-05-03T01:20:48.3866660Z   HOSTCC  scripts/dtc/dtc-lexer.lex.o
2026-05-03T01:20:48.3880555Z ************  drivers/trusty/mtee-kree mk ************
2026-05-03T01:20:48.4371974Z imgsensor drv by common ../common/v1/s5kjns_sunny_mipi_raw/ ../common/v1/ov50d40_truly_mipi_raw/ ../common/v1/ov8856_sunny_mipi_raw/ ../common/v1/ov8856_ofilm_mipi_raw/ ../common/v1/imx355_sunny_mipi_raw/ ../common/v1/sc820cs_truly_mipi_raw/ ../common/v1/sc202cs_sunny_mipi_raw/ ../common/v1/ov02b10_truly_mipi_raw/
2026-05-03T01:20:48.5590672Z   HOSTLD  scripts/mod/modpost
2026-05-03T01:20:48.5970646Z   UPD     include/generated/asm-offsets.h
2026-05-03T01:20:48.5997390Z   CALL    ../scripts/checksyscalls.sh
2026-05-03T01:20:48.6664461Z   LDS     scripts/module-lto.lds
2026-05-03T01:20:48.6778661Z   HOSTCC  scripts/selinux/genheaders/genheaders
2026-05-03T01:20:48.6997215Z   HOSTCC  scripts/dtc/dtc-parser.tab.o
2026-05-03T01:20:48.7230335Z M4U platform folder:"mt6768"
2026-05-03T01:20:48.7251300Z M4U version:2.0
2026-05-03T01:20:48.8196732Z   HOSTCC  scripts/selinux/mdp/mdp
2026-05-03T01:20:48.9170636Z   HOSTLD  scripts/dtc/dtc
2026-05-03T01:20:48.9578259Z   HOSTCC  scripts/bin2c
2026-05-03T01:20:48.9609026Z   LDS     arch/arm64/kernel/vdso/vdso.lds
2026-05-03T01:20:48.9796502Z   CC      arch/arm64/kernel/vdso/vgettimeofday.o
2026-05-03T01:20:48.9840376Z   AS      arch/arm64/kernel/vdso/note.o
2026-05-03T01:20:49.0231365Z   HOSTCC  scripts/kallsyms
2026-05-03T01:20:49.0481100Z   AS      arch/arm64/kernel/vdso/sigreturn.o
2026-05-03T01:20:49.0880511Z   HOSTCC  scripts/pnmtologo
2026-05-03T01:20:49.1128713Z   LD      arch/arm64/kernel/vdso/vdso.so.dbg
2026-05-03T01:20:49.1410633Z   VDSOSYM include/generated/vdso-offsets.h
2026-05-03T01:20:49.1681428Z   HOSTCC  scripts/sortextable
2026-05-03T01:20:49.3368144Z TCORE_UT_TESTS_SUPPORT = n
2026-05-03T01:20:49.3396208Z TCORE_PROFILING_SUPPORT = n
2026-05-03T01:20:49.3401248Z TCORE_PROFILING_AUTO_DUMP = n
2026-05-03T01:20:49.3401870Z TCORE_MEMORY_LEAK_DETECTION_SUPPORT = n
2026-05-03T01:20:49.3511924Z   HOSTCC  scripts/asn1_compiler
2026-05-03T01:20:49.3915974Z   HOSTCC  scripts/extract-cert
2026-05-03T01:20:49.6778355Z ION:enable mtk ion
2026-05-03T01:20:49.6858925Z "CONFIG_MICROTRUST_TEE_VERSION="400""
2026-05-03T01:20:49.6933732Z "CONFIG_MICROTRUST_TEE_SUPPORT=y"
2026-05-03T01:20:49.6934545Z "CONFIG_MICROTRUST_TZ_DRIVER=Y"
2026-05-03T01:20:49.6935146Z "CONFIG_MICROTRUST_VFS_DRIVER=Y"
2026-05-03T01:20:49.6935785Z "CONFIG_MICROTRUST_FP_DRIVER=Y"
2026-05-03T01:20:49.6936200Z "CONFIG_MICROTRUST_DEBUG="
2026-05-03T01:20:49.6936565Z "CONFIG_MICROTRUST_TEST_DRIVERS="
2026-05-03T01:20:49.7385666Z ../scripts/extract-cert.c:46:14: warning: 'ERR_get_error_line' is deprecated [-Wdeprecated-declarations]
2026-05-03T01:20:49.7410109Z         while ((e = ERR_get_error_line(&file, &line))) {
2026-05-03T01:20:49.7430341Z                     ^
2026-05-03T01:20:49.7440626Z /usr/include/openssl/err.h:422:1: note: 'ERR_get_error_line' has been explicitly marked deprecated here
2026-05-03T01:20:49.7470147Z OSSL_DEPRECATEDIN_3_0
2026-05-03T01:20:49.7499981Z ^
2026-05-03T01:20:49.7511335Z /usr/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
2026-05-03T01:20:49.7525346Z #   define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
2026-05-03T01:20:49.7526472Z                                                 ^
2026-05-03T01:20:49.7527375Z /usr/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
2026-05-03T01:20:49.7528422Z #     define OSSL_DEPRECATED(since) __attribute__((deprecated))
2026-05-03T01:20:49.7529146Z                                                    ^
2026-05-03T01:20:49.7530513Z ../scripts/extract-cert.c:59:9: warning: 'ERR_get_error_line' is deprecated [-Wdeprecated-declarations]
2026-05-03T01:20:49.7531590Z         while (ERR_get_error_line(&file, &line)) {}
2026-05-03T01:20:49.7532008Z                ^
2026-05-03T01:20:49.7532591Z /usr/include/openssl/err.h:422:1: note: 'ERR_get_error_line' has been explicitly marked deprecated here
2026-05-03T01:20:49.7533277Z OSSL_DEPRECATEDIN_3_0
2026-05-03T01:20:49.7533574Z ^
2026-05-03T01:20:49.7534047Z /usr/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
2026-05-03T01:20:49.7534799Z #   define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
2026-05-03T01:20:49.7535319Z                                                 ^
2026-05-03T01:20:49.7535892Z /usr/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
2026-05-03T01:20:49.7536576Z #     define OSSL_DEPRECATED(since) __attribute__((deprecated))
2026-05-03T01:20:49.7537080Z                                                    ^
2026-05-03T01:20:49.7537813Z ../scripts/extract-cert.c:124:3: warning: 'ENGINE_load_builtin_engines' is deprecated [-Wdeprecated-declarations]
2026-05-03T01:20:49.7538582Z                 ENGINE_load_builtin_engines();
2026-05-03T01:20:49.7539008Z                 ^
2026-05-03T01:20:49.7539918Z /usr/include/openssl/engine.h:358:1: note: 'ENGINE_load_builtin_engines' has been explicitly marked deprecated here
2026-05-03T01:20:49.7540774Z OSSL_DEPRECATEDIN_3_0 void ENGINE_load_builtin_engines(void);
2026-05-03T01:20:49.7541241Z ^
2026-05-03T01:20:49.7541701Z /usr/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
2026-05-03T01:20:49.7542428Z #   define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
2026-05-03T01:20:49.7542944Z                                                 ^
2026-05-03T01:20:49.7543511Z /usr/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
2026-05-03T01:20:49.7544172Z #     define OSSL_DEPRECATED(since) __attribute__((deprecated))
2026-05-03T01:20:49.7544710Z                                                    ^
2026-05-03T01:20:49.7545376Z ../scripts/extract-cert.c:126:7: warning: 'ENGINE_by_id' is deprecated [-Wdeprecated-declarations]
2026-05-03T01:20:49.7546047Z                 e = ENGINE_by_id("pkcs11");
2026-05-03T01:20:49.7546416Z                     ^
2026-05-03T01:20:49.7547052Z /usr/include/openssl/engine.h:336:1: note: 'ENGINE_by_id' has been explicitly marked deprecated here
2026-05-03T01:20:49.7547909Z OSSL_DEPRECATEDIN_3_0 ENGINE *ENGINE_by_id(const char *id);
2026-05-03T01:20:49.7548359Z ^
2026-05-03T01:20:49.7548816Z /usr/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
2026-05-03T01:20:49.7549812Z #   define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
2026-05-03T01:20:49.7550355Z                                                 ^
2026-05-03T01:20:49.7550968Z /usr/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
2026-05-03T01:20:49.7551653Z #     define OSSL_DEPRECATED(since) __attribute__((deprecated))
2026-05-03T01:20:49.7552148Z                                                    ^
2026-05-03T01:20:49.7552829Z ../scripts/extract-cert.c:128:7: warning: 'ENGINE_init' is deprecated [-Wdeprecated-declarations]
2026-05-03T01:20:49.7553498Z                 if (ENGINE_init(e))
2026-05-03T01:20:49.7553834Z                     ^
2026-05-03T01:20:49.7554405Z /usr/include/openssl/engine.h:620:1: note: 'ENGINE_init' has been explicitly marked deprecated here
2026-05-03T01:20:49.7555111Z OSSL_DEPRECATEDIN_3_0 int ENGINE_init(ENGINE *e);
2026-05-03T01:20:49.7555755Z ^
2026-05-03T01:20:49.7556234Z /usr/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
2026-05-03T01:20:49.7556953Z #   define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
2026-05-03T01:20:49.7557473Z                                                 ^
2026-05-03T01:20:49.7558041Z /usr/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
2026-05-03T01:20:49.7558723Z #     define OSSL_DEPRECATED(since) __attribute__((deprecated))
2026-05-03T01:20:49.7587392Z                                                    ^
2026-05-03T01:20:49.7588291Z ../scripts/extract-cert.c:133:9: warning: 'ENGINE_ctrl_cmd_string' is deprecated [-Wdeprecated-declarations]
2026-05-03T01:20:49.7589201Z                         ERR(!ENGINE_ctrl_cmd_string(e, "PIN", key_pass, 0), "Set PKCS#11 PIN");
2026-05-03T01:20:49.7589983Z                              ^
2026-05-03T01:20:49.7590676Z /usr/include/openssl/engine.h:478:1: note: 'ENGINE_ctrl_cmd_string' has been explicitly marked deprecated here
2026-05-03T01:20:49.7591428Z OSSL_DEPRECATEDIN_3_0
2026-05-03T01:20:49.7591723Z ^
2026-05-03T01:20:49.7592185Z /usr/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
2026-05-03T01:20:49.7592960Z #   define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
2026-05-03T01:20:49.7593473Z                                                 ^
2026-05-03T01:20:49.7594063Z /usr/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
2026-05-03T01:20:49.7594886Z #     define OSSL_DEPRECATED(since) __attribute__((deprecated))
2026-05-03T01:20:49.7595369Z                                                    ^
2026-05-03T01:20:49.7596068Z ../scripts/extract-cert.c:134:3: warning: 'ENGINE_ctrl_cmd' is deprecated [-Wdeprecated-declarations]
2026-05-03T01:20:49.7596841Z                 ENGINE_ctrl_cmd(e, "LOAD_CERT_CTRL", 0, &parms, NULL, 1);
2026-05-03T01:20:49.7597305Z                 ^
2026-05-03T01:20:49.7597892Z /usr/include/openssl/engine.h:450:1: note: 'ENGINE_ctrl_cmd' has been explicitly marked deprecated here
2026-05-03T01:20:49.7598732Z OSSL_DEPRECATEDIN_3_0 int ENGINE_ctrl_cmd(ENGINE *e, const char *cmd_name,
2026-05-03T01:20:49.7599249Z ^
2026-05-03T01:20:49.7599990Z /usr/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
2026-05-03T01:20:49.7600720Z #   define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
2026-05-03T01:20:49.7601226Z                                                 ^
2026-05-03T01:20:49.7601778Z /usr/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
2026-05-03T01:20:49.7602218Z #     define OSSL_DEPRECATED(since) __attribute__((deprecated))
2026-05-03T01:20:49.7602532Z                                                    ^
2026-05-03T01:20:49.7690086Z 7 warnings generated.
2026-05-03T01:20:49.8720484Z   CHK     include/generated/compile.h
2026-05-03T01:20:49.8780247Z   CC      init/main.o
2026-05-03T01:20:49.8940803Z   HOSTCC  usr/gen_init_cpio
2026-05-03T01:20:49.9131373Z   UPD     include/generated/compile.h
2026-05-03T01:20:49.9182693Z   CC      init/do_mounts.o
2026-05-03T01:20:49.9380371Z   CC      arch/arm64/kernel/probes/kprobes.o
2026-05-03T01:20:50.0790416Z   GEN     usr/initramfs_data.cpio
2026-05-03T01:20:50.1150382Z   AS      usr/initramfs_data.o
2026-05-03T01:20:50.1570436Z   AR      usr/built-in.a
2026-05-03T01:20:50.1780405Z   OBJCOPY arch/arm64/kernel/vdso/vdso.so
2026-05-03T01:20:50.1809986Z   AS      arch/arm64/kernel/vdso/vdso.o
2026-05-03T01:20:50.2230496Z   AR      arch/arm64/kernel/vdso/built-in.a
2026-05-03T01:20:50.2320179Z   CC      init/do_mounts_rd.o
2026-05-03T01:20:50.4700860Z   CC      arch/arm64/kernel/probes/decode-insn.o
2026-05-03T01:20:50.9260633Z   CC      arch/arm64/mm/dma-mapping.o
2026-05-03T01:20:50.9410614Z   AS      arch/arm64/kernel/probes/kprobes_trampoline.o
2026-05-03T01:20:50.9864035Z   CC      arch/arm64/kernel/probes/simulate-insn.o
2026-05-03T01:20:51.1580614Z   CC      init/do_mounts_initrd.o
2026-05-03T01:20:51.4479112Z   CC      arch/arm64/mm/extable.o
2026-05-03T01:20:51.4591974Z   CC      arch/arm64/kernel/probes/uprobes.o
2026-05-03T01:20:51.7382036Z   CC      init/initramfs.o
2026-05-03T01:20:51.7530326Z   CC      arch/arm64/net/bpf_jit_comp.o
2026-05-03T01:20:51.8614693Z   CC      arch/arm64/mm/fault.o
2026-05-03T01:20:51.8800274Z   AR      arch/arm64/kernel/probes/built-in.a
2026-05-03T01:20:51.8863389Z   CC      arch/arm64/kernel/debug-monitors.o
2026-05-03T01:20:52.4040415Z   CC      init/calibrate.o
2026-05-03T01:20:52.4951007Z   AS      arch/arm64/kernel/entry.o
2026-05-03T01:20:52.5690566Z   CC      arch/arm64/kernel/irq.o
2026-05-03T01:20:52.6030451Z   CC      init/init_task.o
2026-05-03T01:20:52.6830611Z   AR      arch/arm64/net/built-in.a
2026-05-03T01:20:52.7205529Z   CC      arch/arm64/crypto/sha2-ce-glue.o
2026-05-03T01:20:52.8420536Z   CC      arch/arm64/mm/init.o
2026-05-03T01:20:53.2231298Z   CC      arch/arm64/kernel/fpsimd.o
2026-05-03T01:20:53.3280450Z   AS      arch/arm64/crypto/sha2-ce-core.o
2026-05-03T01:20:53.3830497Z   CC      arch/arm64/crypto/ghash-ce-glue.o
2026-05-03T01:20:53.4619337Z   CC      init/version.o
2026-05-03T01:20:53.7291246Z   AS      arch/arm64/mm/cache.o
2026-05-03T01:20:53.7800737Z   CC      arch/arm64/mm/copypage.o
2026-05-03T01:20:53.8489219Z   AR      init/built-in.a
2026-05-03T01:20:54.0010594Z   AS      arch/arm64/crypto/ghash-ce-core.o
2026-05-03T01:20:54.0520428Z   CC      kernel/bpf/core.o
2026-05-03T01:20:54.0610703Z   AS      arch/arm64/kernel/entry-fpsimd.o
2026-05-03T01:20:54.0670363Z   AS      arch/arm64/crypto/aes-ce-core.o
2026-05-03T01:20:54.1110479Z   CC      arch/arm64/crypto/aes-ce-glue.o
2026-05-03T01:20:54.1200382Z   CC      arch/arm64/kernel/process.o
2026-05-03T01:20:54.4010437Z   CC      arch/arm64/mm/flush.o
2026-05-03T01:20:54.6620736Z   CC      arch/arm64/crypto/aes-glue-ce.o
2026-05-03T01:20:55.1160500Z   CC      arch/arm64/mm/ioremap.o
2026-05-03T01:20:55.2300075Z   CC      arch/arm64/kernel/ptrace.o
2026-05-03T01:20:55.2344977Z   AS      arch/arm64/crypto/aes-ce.o
2026-05-03T01:20:55.2870384Z   CC      arch/arm64/crypto/sha256-glue.o
2026-05-03T01:20:55.5294826Z   CC      kernel/bpf/syscall.o
2026-05-03T01:20:55.6966337Z   CC      arch/arm64/mm/mmap.o
2026-05-03T01:20:56.1700903Z   CC      arch/arm64/mm/pgd.o
2026-05-03T01:20:56.1910662Z   SHIPPED arch/arm64/crypto/sha256-core.S
2026-05-03T01:20:56.1960178Z   AS      arch/arm64/crypto/aes-cipher-core.o
2026-05-03T01:20:56.2440635Z   CC      arch/arm64/crypto/aes-cipher-glue.o
2026-05-03T01:20:56.2777407Z   CC      arch/arm64/kernel/setup.o
2026-05-03T01:20:56.6270382Z   CC      arch/arm64/mm/mmu.o
2026-05-03T01:20:56.7460687Z   AS      arch/arm64/crypto/sha256-core.o
2026-05-03T01:20:56.7920628Z   AR      arch/arm64/crypto/built-in.a
2026-05-03T01:20:56.8120605Z   CC      kernel/cgroup/cgroup.o
2026-05-03T01:20:57.1735570Z   CC      arch/arm64/kernel/signal.o
2026-05-03T01:20:57.2210561Z   CC      kernel/bpf/verifier.o
2026-05-03T01:20:57.6530695Z   CC      arch/arm64/mm/context.o
2026-05-03T01:20:58.2107845Z   AS      arch/arm64/mm/proc.o
2026-05-03T01:20:58.2606656Z   CC      arch/arm64/mm/pageattr.o
2026-05-03T01:20:58.4720592Z   CC      arch/arm64/kernel/sys.o
2026-05-03T01:20:58.9020418Z   AR      arch/arm64/mm/built-in.a
2026-05-03T01:20:58.9230425Z   CC      arch/arm64/kernel/stacktrace.o
2026-05-03T01:20:59.0500497Z   CC      kernel/dma/mapping.o
2026-05-03T01:20:59.1960386Z   CC      kernel/cgroup/rstat.o
2026-05-03T01:20:59.3486285Z   CC      kernel/bpf/inode.o
2026-05-03T01:20:59.5802753Z   CC      arch/arm64/kernel/time.o
2026-05-03T01:20:59.8270379Z   CC      kernel/dma/contiguous.o
2026-05-03T01:20:59.8890065Z   CC      kernel/cgroup/namespace.o
2026-05-03T01:21:00.1390472Z   CC      arch/arm64/kernel/traps.o
2026-05-03T01:21:00.4601702Z   CC      kernel/bpf/helpers.o
2026-05-03T01:21:00.4885825Z   CC      kernel/dma/coherent.o
2026-05-03T01:21:00.5620394Z   CC      kernel/cgroup/cgroup-v1.o
2026-05-03T01:21:00.8130381Z   CC      arch/arm64/kernel/io.o
2026-05-03T01:21:01.0531239Z ../kernel/cgroup/cgroup-v1.c:908:6: warning: variable 'nr_opts' set but not used [-Wunused-but-set-variable]
2026-05-03T01:21:01.0532087Z         int nr_opts = 0;
2026-05-03T01:21:01.0532407Z             ^
2026-05-03T01:21:01.2236494Z   CC      kernel/bpf/tnum.o
2026-05-03T01:21:01.2620625Z   CC      arch/arm64/kernel/vdso.o
2026-05-03T01:21:01.2680583Z 1 warning generated.
2026-05-03T01:21:01.2960341Z   CC      kernel/dma/removed.o
2026-05-03T01:21:01.4145905Z   CC      kernel/bpf/hashtab.o
2026-05-03T01:21:01.5310419Z   CC      kernel/cgroup/freezer.o
2026-05-03T01:21:01.8151138Z   AS      arch/arm64/kernel/hyp-stub.o
2026-05-03T01:21:01.8660491Z   CC      arch/arm64/kernel/psci.o
2026-05-03T01:21:01.9722453Z   CC      kernel/cgroup/legacy_freezer.o
2026-05-03T01:21:02.1612172Z   CC      kernel/dma/direct.o
2026-05-03T01:21:02.2940606Z   CC      arch/arm64/kernel/cpu_ops.o
2026-05-03T01:21:02.3900377Z   CC      kernel/bpf/arraymap.o
2026-05-03T01:21:02.4840378Z   CC      kernel/cgroup/cpuset.o
2026-05-03T01:21:02.8257886Z   CC      arch/arm64/kernel/insn.o
2026-05-03T01:21:02.8990164Z   CC      kernel/dma/swiotlb.o
2026-05-03T01:21:02.9981186Z ../kernel/cgroup/cpuset.c:1529:17: warning: variable 'cs' set but not used [-Wunused-but-set-variable]
2026-05-03T01:21:03.0009908Z         struct cpuset *cs;
2026-05-03T01:21:03.0039883Z                        ^
2026-05-03T01:21:03.2850691Z   CC      kernel/bpf/percpu_freelist.o
2026-05-03T01:21:03.4040332Z 1 warning generated.
2026-05-03T01:21:03.4700619Z   CC      arch/arm64/kernel/return_address.o
2026-05-03T01:21:03.4820600Z   CC      kernel/bpf/bpf_lru_list.o
2026-05-03T01:21:03.7142828Z   AR      kernel/cgroup/built-in.a
2026-05-03T01:21:03.7400430Z   CC      kernel/events/core.o
2026-05-03T01:21:03.8120484Z   CC      kernel/bpf/lpm_trie.o
2026-05-03T01:21:03.9740553Z   AR      kernel/dma/built-in.a
2026-05-03T01:21:04.0195977Z   CC      certs/system_keyring.o
2026-05-03T01:21:04.1768740Z   CC      arch/arm64/kernel/cpuinfo.o
2026-05-03T01:21:04.4730408Z   EXTRACT_CERTS   
2026-05-03T01:21:04.4760156Z   AS      certs/system_certificates.o
2026-05-03T01:21:04.5160452Z   AR      certs/built-in.a
2026-05-03T01:21:04.5271719Z   CC      kernel/events/ring_buffer.o
2026-05-03T01:21:04.7400610Z   CC      kernel/bpf/map_in_map.o
2026-05-03T01:21:04.8180609Z   CC      arch/arm64/kernel/cpu_errata.o
2026-05-03T01:21:04.9880372Z   CC      kernel/bpf/local_storage.o
2026-05-03T01:21:05.4067382Z   CC      arch/arm64/kernel/cpufeature.o
2026-05-03T01:21:05.5865983Z   CC      kernel/irq/irqdesc.o
2026-05-03T01:21:05.7860435Z   CC      kernel/bpf/disasm.o
2026-05-03T01:21:06.0240646Z   CC      kernel/bpf/btf.o
2026-05-03T01:21:06.2600613Z   CC      kernel/irq/handle.o
2026-05-03T01:21:06.3630618Z   CC      arch/arm64/kernel/alternative.o
2026-05-03T01:21:06.6762691Z   CC      kernel/events/callchain.o
2026-05-03T01:21:06.9515743Z   CC      kernel/irq/manage.o
2026-05-03T01:21:07.0160641Z   CC      arch/arm64/kernel/cacheinfo.o
2026-05-03T01:21:07.2700513Z   CC      kernel/bpf/devmap.o
2026-05-03T01:21:07.3690522Z   CC      arch/arm64/kernel/smp.o
2026-05-03T01:21:07.4030542Z   CC      kernel/events/hw_breakpoint.o
2026-05-03T01:21:07.7880401Z   CC      kernel/irq/spurious.o
2026-05-03T01:21:08.1608943Z   CC      kernel/bpf/cpumap.o
2026-05-03T01:21:08.1790510Z   CC      kernel/irq/resend.o
2026-05-03T01:21:08.2930784Z   CC      kernel/events/uprobes.o
2026-05-03T01:21:08.5000743Z   CC      arch/arm64/kernel/smp_spin_table.o
2026-05-03T01:21:08.5233074Z   CC      kernel/irq/chip.o
2026-05-03T01:21:08.9650447Z   CC      arch/arm64/kernel/topology.o
2026-05-03T01:21:09.0320604Z   CC      kernel/bpf/offload.o
2026-05-03T01:21:09.3493254Z   CC      kernel/irq/dummychip.o
2026-05-03T01:21:09.5112467Z   AS      arch/arm64/kernel/smccc-call.o
2026-05-03T01:21:09.5570378Z   CC      arch/arm64/kernel/syscall.o
2026-05-03T01:21:09.5750359Z   AR      kernel/events/built-in.a
2026-05-03T01:21:09.6230389Z   CC      mm/filemap.o
2026-05-03T01:21:09.8830419Z   CC      kernel/irq/devres.o
2026-05-03T01:21:10.1300663Z   CC      arch/arm64/kernel/sys32.o
2026-05-03T01:21:10.4570733Z   CC      kernel/bpf/stackmap.o
2026-05-03T01:21:10.4750362Z   CC      kernel/irq/autoprobe.o
2026-05-03T01:21:10.6790679Z   CC      arch/arm64/kernel/signal32.o
2026-05-03T01:21:11.1063692Z   CC      kernel/irq/irqdomain.o
2026-05-03T01:21:11.2491289Z   CC      mm/mempool.o
2026-05-03T01:21:11.3741581Z   CC      kernel/bpf/cgroup.o
2026-05-03T01:21:11.4900646Z   CC      arch/arm64/kernel/sys_compat.o
2026-05-03T01:21:12.0220624Z   CC      kernel/irq/proc.o
2026-05-03T01:21:12.0851004Z   AS      arch/arm64/kernel/sigreturn32.o
2026-05-03T01:21:12.1270631Z   AS      arch/arm64/kernel/kuser32.o
2026-05-03T01:21:12.1700575Z   CC      arch/arm64/kernel/arm64ksyms.o
2026-05-03T01:21:12.2784827Z   CC      mm/oom_kill.o
2026-05-03T01:21:12.4890404Z   CC      kernel/irq/cpuhotplug.o
2026-05-03T01:21:12.7170610Z   CC      kernel/bpf/reuseport_array.o
2026-05-03T01:21:12.9050511Z   CC      kernel/irq/pm.o
2026-05-03T01:21:12.9780700Z   CC      arch/arm64/kernel/module.o
2026-05-03T01:21:13.4920551Z   CC      arch/arm64/kernel/module-plts.o
2026-05-03T01:21:13.5306868Z   AR      kernel/bpf/built-in.a
2026-05-03T01:21:13.5751065Z   CC      mm/fadvise.o
2026-05-03T01:21:13.5860327Z   CC      fs/configfs/inode.o
2026-05-03T01:21:13.7374382Z   CC      kernel/irq/msi.o
2026-05-03T01:21:13.8230827Z   CC      arch/arm64/kernel/perf_regs.o
2026-05-03T01:21:14.1770611Z   CC      fs/configfs/file.o
2026-05-03T01:21:14.3898962Z   CC      arch/arm64/kernel/perf_callchain.o
2026-05-03T01:21:14.3920132Z   CC      kernel/irq/affinity.o
2026-05-03T01:21:14.5860604Z   CC      fs/configfs/dir.o
2026-05-03T01:21:14.5912257Z   CC      mm/maccess.o
2026-05-03T01:21:14.8370626Z   AR      kernel/irq/built-in.a
2026-05-03T01:21:14.8710818Z   AR      kernel/livepatch/built-in.a
2026-05-03T01:21:14.8890752Z   CC      kernel/locking/mutex.o
2026-05-03T01:21:14.9730644Z   CC      arch/arm64/kernel/perf_event.o
2026-05-03T01:21:15.2644494Z   CC      mm/page_alloc.o
2026-05-03T01:21:15.3987683Z   CC      fs/configfs/symlink.o
2026-05-03T01:21:15.5083350Z   CC      kernel/locking/semaphore.o
2026-05-03T01:21:15.6381482Z   CC      arch/arm64/kernel/hw_breakpoint.o
2026-05-03T01:21:15.8540662Z   CC      fs/configfs/mount.o
2026-05-03T01:21:16.2390418Z   CC      kernel/locking/rwsem.o
2026-05-03T01:21:16.3050420Z   AS      arch/arm64/kernel/sleep.o
2026-05-03T01:21:16.3538771Z   CC      fs/configfs/item.o
2026-05-03T01:21:16.3581193Z   CC      arch/arm64/kernel/suspend.o
2026-05-03T01:21:16.6540559Z   CC      kernel/locking/percpu-rwsem.o
2026-05-03T01:21:16.8280388Z   AR      fs/configfs/built-in.a
2026-05-03T01:21:16.8499606Z   CC      fs/crypto/crypto.o
2026-05-03T01:21:16.8804211Z   CC      arch/arm64/kernel/cpuidle.o
2026-05-03T01:21:17.0870385Z   CC      kernel/locking/spinlock.o
2026-05-03T01:21:17.3860636Z   CC      arch/arm64/kernel/armv8_deprecated.o
2026-05-03T01:21:17.4560358Z   CC      mm/page-writeback.o
2026-05-03T01:21:17.5652620Z   CC      kernel/locking/osq_lock.o
2026-05-03T01:21:17.6540430Z   CC      fs/crypto/fname.o
2026-05-03T01:21:17.8581009Z   CC      kernel/locking/qspinlock.o
2026-05-03T01:21:18.1039598Z   CC      arch/arm64/kernel/kaslr.o
2026-05-03T01:21:18.1430426Z   CC      kernel/locking/rtmutex.o
2026-05-03T01:21:18.4700632Z   CC      fs/crypto/hkdf.o
2026-05-03T01:21:18.5740376Z   CC      arch/arm64/kernel/ssbd.o
2026-05-03T01:21:18.7183832Z   CC      kernel/locking/rwsem-xadd.o
2026-05-03T01:21:18.9110475Z   CC      fs/crypto/hooks.o
2026-05-03T01:21:18.9390057Z   AS      arch/arm64/kernel/head.o
2026-05-03T01:21:18.9896418Z   CC      mm/readahead.o
2026-05-03T01:21:18.9907485Z   LDS     arch/arm64/kernel/vmlinux.lds
2026-05-03T01:21:19.0266106Z   AR      arch/arm64/kernel/built-in.a
2026-05-03T01:21:19.0630366Z   CC      fs/devpts/inode.o
2026-05-03T01:21:19.2420399Z   CC      kernel/locking/qrwlock.o
2026-05-03T01:21:19.5340427Z   AR      kernel/locking/built-in.a
2026-05-03T01:21:19.5630430Z   CC      kernel/power/qos.o
2026-05-03T01:21:19.5831049Z   AR      fs/devpts/built-in.a
2026-05-03T01:21:19.5950927Z   CC      fs/crypto/keyring.o
2026-05-03T01:21:19.6390602Z   CC      kernel/power/main.o
2026-05-03T01:21:20.0830675Z   CC      mm/swap.o
2026-05-03T01:21:20.4135240Z   AR      ipc/built-in.a
2026-05-03T01:21:20.4190149Z   CC      fs/crypto/keysetup.o
2026-05-03T01:21:20.4310239Z   CC      kernel/printk/printk.o
2026-05-03T01:21:20.6580476Z   CC      kernel/power/process.o
2026-05-03T01:21:21.1830518Z   CC      fs/crypto/keysetup_v1.o
2026-05-03T01:21:21.2650428Z   CC      mm/truncate.o
2026-05-03T01:21:21.3662349Z   CC      kernel/power/suspend.o
2026-05-03T01:21:21.8233282Z   CC      kernel/printk/printk_safe.o
2026-05-03T01:21:21.8700373Z   CC      fs/crypto/policy.o
2026-05-03T01:21:22.0770772Z   AR      kernel/printk/built-in.a
2026-05-03T01:21:22.0950484Z   CC      fs/exfat/exfat_core.o
2026-05-03T01:21:22.3180388Z   CC      mm/vmscan.o
2026-05-03T01:21:22.4381319Z   CC      kernel/power/wakelock.o
2026-05-03T01:21:22.5970533Z   CC      fs/crypto/bio.o
2026-05-03T01:21:22.9830659Z   CC      kernel/power/poweroff.o
2026-05-03T01:21:23.1251017Z ../mm/vmscan.c:2855:17: warning: variable 'node_lru_pages' set but not used [-Wunused-but-set-variable]
2026-05-03T01:21:23.1270032Z                 unsigned long node_lru_pages = 0;
2026-05-03T01:21:23.1280291Z                               ^
2026-05-03T01:21:23.1330221Z ../mm/vmscan.c:3464:6: warning: variable 'nid' set but not used [-Wunused-but-set-variable]
2026-05-03T01:21:23.1331367Z         int nid;
2026-05-03T01:21:23.1349672Z             ^
2026-05-03T01:21:23.1914025Z   CC      kernel/power/energy_model.o
2026-05-03T01:21:23.3034458Z   CC      fs/exfat/exfat_super.o
2026-05-03T01:21:23.3920662Z   CC      fs/crypto/inline_crypt.o
2026-05-03T01:21:23.8500451Z   CC      kernel/power/wakeup_reason.o
2026-05-03T01:21:23.9240305Z 2 warnings generated.
2026-05-03T01:21:24.2520411Z   CC      fs/exfat/exfat_api.o
2026-05-03T01:21:24.3166886Z   AR      fs/crypto/built-in.a
2026-05-03T01:21:24.3515774Z   CC      mm/shmem.o
2026-05-03T01:21:24.3809047Z   CC      security/integrity/iint.o
2026-05-03T01:21:24.6920579Z   AR      kernel/power/built-in.a
2026-05-03T01:21:24.7197646Z   CC      kernel/rcu/update.o
2026-05-03T01:21:24.8430978Z   CC      security/integrity/integrity_audit.o
2026-05-03T01:21:25.1150416Z   CC      fs/exfat/exfat_blkdev.o
2026-05-03T01:21:25.3160359Z   AR      security/integrity/built-in.a
2026-05-03T01:21:25.3377534Z   CC      security/keys/gc.o
2026-05-03T01:21:25.6472792Z   CC      kernel/rcu/sync.o
2026-05-03T01:21:25.7000613Z   CC      fs/exfat/exfat_cache.o
2026-05-03T01:21:25.8220734Z   CC      security/keys/key.o
2026-05-03T01:21:25.8903012Z   CC      mm/util.o
2026-05-03T01:21:25.9060540Z   CC      kernel/rcu/srcutree.o
2026-05-03T01:21:26.3073576Z   CC      fs/exfat/exfat_data.o
2026-05-03T01:21:26.6254667Z   CC      kernel/rcu/tree.o
2026-05-03T01:21:26.6390574Z   CC      security/keys/keyring.o
2026-05-03T01:21:26.7856580Z   CC      mm/mmzone.o
2026-05-03T01:21:26.8140430Z   CC      fs/exfat/exfat_bitmap.o
2026-05-03T01:21:26.8590416Z   CC      fs/exfat/exfat_nls.o
2026-05-03T01:21:27.3180742Z In file included from ../kernel/rcu/tree.c:4188:
2026-05-03T01:21:27.3210458Z ../kernel/rcu/tree_exp.h:653:19: warning: variable 'rdp' set but not used [-Wunused-but-set-variable]
2026-05-03T01:21:27.3239990Z         struct rcu_data *rdp;
2026-05-03T01:21:27.3253006Z                          ^
2026-05-03T01:21:27.3594269Z In file included from ../kernel/rcu/tree.c:4189:
2026-05-03T01:21:27.3600338Z ../kernel/rcu/tree_plugin.h:712:22: warning: variable 't' set but not used [-Wunused-but-set-variable]
2026-05-03T01:21:27.3720221Z         struct task_struct *t;
2026-05-03T01:21:27.3750591Z                             ^
2026-05-03T01:21:27.4035034Z   CC      mm/vmstat.o
2026-05-03T01:21:27.4790648Z   CC      security/keys/keyctl.o
2026-05-03T01:21:27.4854189Z   CC      fs/exfat/exfat_oal.o
2026-05-03T01:21:27.8591934Z   CC      fs/exfat/exfat_upcase.o
2026-05-03T01:21:28.1010356Z 2 warnings generated.
2026-05-03T01:21:28.2040334Z   AR      fs/exfat/built-in.a
2026-05-03T01:21:28.2115745Z   CC      security/keys/permission.o
2026-05-03T01:21:28.2190189Z   AR      fs/exofs/built-in.a
2026-05-03T01:21:28.2352738Z   CC      fs/exportfs/expfs.o
2026-05-03T01:21:28.5089922Z   CC      kernel/rcu/rcu_segcblist.o
2026-05-03T01:21:28.5369578Z   CC      mm/backing-dev.o
2026-05-03T01:21:28.7765949Z   AR      fs/exportfs/built-in.a
2026-05-03T01:21:28.8050768Z   CC      fs/ext4/balloc.o
2026-05-03T01:21:28.8170489Z   AR      kernel/rcu/built-in.a
2026-05-03T01:21:28.8320863Z   CC      security/keys/process_keys.o
2026-05-03T01:21:28.8490438Z   CC      kernel/sched/extension/eas_plus.o
2026-05-03T01:21:29.6094888Z   CC      security/keys/request_key.o
2026-05-03T01:21:29.6102344Z   CC      mm/mm_init.o
2026-05-03T01:21:29.7441020Z ../kernel/sched/extension/eas_plus.c:364:6: warning: variable 'task_prefer' set but not used [-Wunused-but-set-variable]
2026-05-03T01:21:29.7470025Z         int task_prefer;
2026-05-03T01:21:29.7470608Z             ^
2026-05-03T01:21:29.8880739Z   CC      fs/ext4/bitmap.o
2026-05-03T01:21:29.9560013Z 1 warning generated.
2026-05-03T01:21:30.2777371Z   CC      mm/mmu_context.o
2026-05-03T01:21:30.3901289Z   CC      security/keys/request_key_auth.o
2026-05-03T01:21:30.4630688Z   CC      kernel/sched/extension/debug.o
2026-05-03T01:21:30.4740363Z   CC      fs/ext4/block_validity.o
2026-05-03T01:21:30.8770586Z   CC      security/keys/user_defined.o
2026-05-03T01:21:30.9290417Z   CC      mm/percpu.o
2026-05-03T01:21:31.1910576Z   CC      fs/ext4/dir.o
2026-05-03T01:21:31.3210786Z   CC      kernel/sched/extension/tuning.o
2026-05-03T01:21:31.6002915Z   CC      security/keys/compat.o
2026-05-03T01:21:32.0020569Z   CC      fs/ext4/ext4_jbd2.o
2026-05-03T01:21:32.1300672Z   CC      security/keys/proc.o
2026-05-03T01:21:32.3600375Z   CC      mm/slab_common.o
2026-05-03T01:21:32.5957622Z   CC      security/keys/sysctl.o
2026-05-03T01:21:32.8090365Z   CC      kernel/sched/extension/debug_aee.o
2026-05-03T01:21:32.9230618Z   CC      fs/ext4/extents.o
2026-05-03T01:21:33.0240554Z   AR      security/keys/built-in.a
2026-05-03T01:21:33.0520537Z   GEN     security/selinux/flask.h security/selinux/av_permissions.h
2026-05-03T01:21:33.0580070Z   CC      security/selinux/avc.o
2026-05-03T01:21:33.6250423Z   CC      mm/compaction.o
2026-05-03T01:21:33.7285186Z   AR      kernel/sched/extension/built-in.a
2026-05-03T01:21:33.7415367Z   CC      kernel/sched/core.o
2026-05-03T01:21:34.0970543Z   CC      security/selinux/hooks.o
2026-05-03T01:21:34.8960600Z   CC      fs/ext4/extents_status.o
2026-05-03T01:21:35.1690375Z   CC      mm/vmacache.o
2026-05-03T01:21:35.6131238Z   CC      mm/interval_tree.o
2026-05-03T01:21:36.0135154Z   CC      fs/ext4/file.o
2026-05-03T01:21:36.0270401Z   CC      security/selinux/selinuxfs.o
2026-05-03T01:21:36.2400627Z   CC      mm/list_lru.o
2026-05-03T01:21:36.7230750Z   CC      fs/ext4/fsmap.o
2026-05-03T01:21:37.0090416Z   CC      mm/workingset.o
2026-05-03T01:21:37.0480504Z   CC      kernel/sched/loadavg.o
2026-05-03T01:21:37.2780657Z   CC      security/selinux/netlink.o
2026-05-03T01:21:37.5201276Z ../mm/workingset.c:200:15: warning: variable 'nid' set but not used [-Wunused-but-set-variable]
2026-05-03T01:21:37.5219942Z         int memcgid, nid;
2026-05-03T01:21:37.5249984Z                      ^
2026-05-03T01:21:37.6120421Z 1 warning generated.
2026-05-03T01:21:37.6430340Z   CC      mm/debug.o
2026-05-03T01:21:37.8248030Z   CC      fs/ext4/fsync.o
2026-05-03T01:21:37.8620632Z   CC      security/selinux/nlmsgtab.o
2026-05-03T01:21:38.3525625Z   CC      kernel/sched/clock.o
2026-05-03T01:21:38.5540553Z   CC      mm/gup.o
2026-05-03T01:21:38.5591267Z   CC      security/selinux/netif.o
2026-05-03T01:21:38.7480464Z   CC      fs/ext4/hash.o
2026-05-03T01:21:39.4366373Z   CC      fs/ext4/ialloc.o
2026-05-03T01:21:39.4926255Z   CC      security/selinux/netnode.o
2026-05-03T01:21:39.5902620Z   CC      kernel/sched/cputime.o
2026-05-03T01:21:39.7460665Z   CC      mm/highmem.o
2026-05-03T01:21:40.3297359Z mm/.tmp_highmem.o: no symbols
2026-05-03T01:21:40.3371007Z   CC      mm/memory.o
2026-05-03T01:21:40.3940355Z   CC      security/selinux/netport.o
2026-05-03T01:21:40.5564785Z   CC      fs/ext4/indirect.o
2026-05-03T01:21:40.9160512Z   CC      kernel/sched/idle.o
2026-05-03T01:21:41.0190706Z ../mm/memory.c:4535:8: warning: variable 'p4dval' set but not used [-Wunused-but-set-variable]
2026-05-03T01:21:41.0220065Z         p4d_t p4dval;
2026-05-03T01:21:41.0239917Z               ^
2026-05-03T01:21:41.2005573Z   CC      security/selinux/ibpkey.o
2026-05-03T01:21:41.6810949Z   CC      fs/ext4/inline.o
2026-05-03T01:21:41.8930459Z 1 warning generated.
2026-05-03T01:21:42.0960688Z   CC      security/selinux/exports.o
2026-05-03T01:21:42.2770639Z   CC      mm/mincore.o
2026-05-03T01:21:42.3412475Z   CC      kernel/sched/fair.o
2026-05-03T01:21:42.5000309Z   CC      security/selinux/ss/ebitmap.o
2026-05-03T01:21:42.5930710Z   CC      fs/ext4/inode.o
2026-05-03T01:21:42.9705584Z   CC      mm/mlock.o
2026-05-03T01:21:43.3572108Z ../kernel/sched/fair.c:6932:16: warning: variable 'target_util' set but not used [-Wunused-but-set-variable]
2026-05-03T01:21:43.3600051Z         unsigned long target_util = ULONG_MAX;
2026-05-03T01:21:43.3620227Z                       ^
2026-05-03T01:21:43.3658762Z   CC      security/selinux/ss/hashtab.o
2026-05-03T01:21:43.3690866Z ../kernel/sched/fair.c:7666:37: warning: comparison of distinct pointer types ('typeof (1) *' (aka 'int *') and 'typeof ((best_energy >> 4)) *' (aka 'unsigned long *')) [-Wcompare-distinct-pointer-types]
2026-05-03T01:21:43.3720131Z                                 if((best_energy - cur_energy) > max(1, (best_energy >> 4))) {
2026-05-03T01:21:43.3749978Z                                                                 ^~~~~~~~~~~~~~~~~~~~~~~~~~
2026-05-03T01:21:43.3770151Z ../include/linux/kernel.h:859:19: note: expanded from macro 'max'
2026-05-03T01:21:43.3800115Z #define max(x, y)       __careful_cmp(x, y, >)
2026-05-03T01:21:43.3839917Z                         ^~~~~~~~~~~~~~~~~~~~~~
2026-05-03T01:21:43.3870088Z ../include/linux/kernel.h:843:24: note: expanded from macro '__careful_cmp'
2026-05-03T01:21:43.3899962Z         __builtin_choose_expr(__safe_cmp(x, y), \
2026-05-03T01:21:43.3929891Z                               ^~~~~~~~~~~~~~~~
2026-05-03T01:21:43.3950197Z ../include/linux/kernel.h:833:4: note: expanded from macro '__safe_cmp'
2026-05-03T01:21:43.3980167Z                 (__typecheck(x, y) && __no_side_effects(x, y))
2026-05-03T01:21:43.4019937Z                  ^~~~~~~~~~~~~~~~~
2026-05-03T01:21:43.4050638Z ../include/linux/kernel.h:819:29: note: expanded from macro '__typecheck'
2026-05-03T01:21:43.4079970Z                 (!!(sizeof((typeof(x) *)1 == (typeof(y) *)1)))
2026-05-03T01:21:43.4109924Z                            ~~~~~~~~~~~~~~ ^  ~~~~~~~~~~~~~~
2026-05-03T01:21:43.6930437Z   CC      security/selinux/ss/symtab.o
2026-05-03T01:21:43.8240553Z   CC      security/selinux/ss/sidtab.o
2026-05-03T01:21:44.0650443Z   CC      mm/mmap.o
2026-05-03T01:21:44.7020340Z   CC      fs/ext4/ioctl.o
2026-05-03T01:21:44.7490973Z ../mm/mmap.c:2370:16: warning: variable 'new_start' set but not used [-Wunused-but-set-variable]
2026-05-03T01:21:44.7520573Z         unsigned long new_start;
2026-05-03T01:21:44.7549896Z                       ^
2026-05-03T01:21:44.8630454Z   CC      security/selinux/ss/avtab.o
2026-05-03T01:21:45.0580414Z 2 warnings generated.
2026-05-03T01:21:45.0970413Z   CC      kernel/sched/rt.o
2026-05-03T01:21:45.2130379Z 1 warning generated.
2026-05-03T01:21:45.6019074Z   CC      mm/mprotect.o
2026-05-03T01:21:45.7320615Z   CC      security/selinux/ss/policydb.o
2026-05-03T01:21:45.8312606Z   CC      fs/ext4/mballoc.o
2026-05-03T01:21:45.9290757Z ../kernel/sched/rt.c:1445:22: warning: variable 'curr' set but not used [-Wunused-but-set-variable]
2026-05-03T01:21:45.9350031Z         struct task_struct *curr;
2026-05-03T01:21:45.9379934Z                             ^
2026-05-03T01:21:46.2570376Z 1 warning generated.
2026-05-03T01:21:46.2930519Z   CC      kernel/sched/deadline.o
2026-05-03T01:21:46.3910515Z   CC      mm/mremap.o
2026-05-03T01:21:47.0436770Z   CC      security/selinux/ss/services.o
2026-05-03T01:21:47.1430358Z   CC      mm/msync.o
2026-05-03T01:21:47.5080449Z   CC      kernel/sched/wait.o
2026-05-03T01:21:47.7110450Z   CC      mm/page_vma_mapped.o
2026-05-03T01:21:47.8500806Z   CC      fs/ext4/migrate.o
2026-05-03T01:21:47.9500820Z ../security/selinux/ss/services.c:2314:17: warning: variable 'sidtab' set but not used [-Wunused-but-set-variable]
2026-05-03T01:21:47.9502155Z         struct sidtab *sidtab;
2026-05-03T01:21:47.9530310Z                        ^
2026-05-03T01:21:47.9559938Z ../security/selinux/ss/services.c:2403:17: warning: variable 'sidtab' set but not used [-Wunused-but-set-variable]
2026-05-03T01:21:47.9569925Z         struct sidtab *sidtab;
2026-05-03T01:21:47.9590198Z                        ^
2026-05-03T01:21:47.9620573Z ../security/selinux/ss/services.c:2448:17: warning: variable 'sidtab' set but not used [-Wunused-but-set-variable]
2026-05-03T01:21:47.9650030Z         struct sidtab *sidtab;
2026-05-03T01:21:47.9660058Z                        ^
2026-05-03T01:21:47.9680464Z ../security/selinux/ss/services.c:2799:17: warning: variable 'sidtab' set but not used [-Wunused-but-set-variable]
2026-05-03T01:21:47.9710003Z         struct sidtab *sidtab;
2026-05-03T01:21:47.9740025Z                        ^
2026-05-03T01:21:48.3120700Z   CC      mm/pagewalk.o
2026-05-03T01:21:48.3560393Z 4 warnings generated.
2026-05-03T01:21:48.3954264Z   CC      security/selinux/ss/conditional.o
2026-05-03T01:21:48.5420353Z   CC      fs/ext4/mmp.o
2026-05-03T01:21:48.7884933Z   CC      mm/pgtable-generic.o
2026-05-03T01:21:48.7910203Z   CC      kernel/sched/wait_bit.o
2026-05-03T01:21:49.2423681Z   CC      fs/ext4/move_extent.o
2026-05-03T01:21:49.3140387Z   CC      security/selinux/ss/mls.o
2026-05-03T01:21:49.3760396Z   CC      mm/rmap.o
2026-05-03T01:21:49.9210666Z ../mm/rmap.c:960:17: warning: variable 'cstart' set but not used [-Wunused-but-set-variable]
2026-05-03T01:21:49.9230450Z                 unsigned long cstart;
2026-05-03T01:21:49.9259906Z                               ^
2026-05-03T01:21:49.9904822Z   CC      fs/ext4/namei.o
2026-05-03T01:21:50.0880411Z   CC      kernel/sched/swait.o
2026-05-03T01:21:50.1120424Z 1 warning generated.
2026-05-03T01:21:50.1802356Z   CC      security/selinux/ss/status.o
2026-05-03T01:21:50.4532823Z   CC      mm/vmalloc.o
2026-05-03T01:21:51.0580489Z   AR      security/selinux/built-in.a
2026-05-03T01:21:51.0683448Z   CC      security/commoncap.o
2026-05-03T01:21:51.3806458Z   CC      kernel/sched/completion.o
2026-05-03T01:21:51.4910588Z   CC      fs/ext4/page-io.o
2026-05-03T01:21:51.8310430Z   CC      security/min_addr.o
2026-05-03T01:21:51.8900434Z   CC      mm/process_vm_access.o
2026-05-03T01:21:52.2890597Z   CC      fs/ext4/readpage.o
2026-05-03T01:21:52.4405330Z   CC      security/security.o
2026-05-03T01:21:52.5196043Z   CC      mm/init-mm.o
2026-05-03T01:21:52.6107668Z   CC      kernel/sched/stubs.o
2026-05-03T01:21:52.8150566Z   CC      mm/nobootmem.o
2026-05-03T01:21:53.0430419Z   CC      fs/ext4/resize.o
2026-05-03T01:21:53.5958742Z   CC      mm/madvise.o
2026-05-03T01:21:53.8294082Z   CC      kernel/sched/cpupri.o
2026-05-03T01:21:53.9750936Z   CC      security/lsm_audit.o
2026-05-03T01:21:54.0350435Z   CC      fs/ext4/super.o
2026-05-03T01:21:54.4346254Z   CC      mm/memblock.o
2026-05-03T01:21:54.7500686Z   CC      kernel/sched/cpudeadline.o
2026-05-03T01:21:54.9590618Z   AR      security/built-in.a
2026-05-03T01:21:54.9860598Z   CC      fs/f2fs/dir.o
2026-05-03T01:21:55.3870695Z   CC      mm/page_io.o
2026-05-03T01:21:55.6620437Z   CC      kernel/sched/topology.o
2026-05-03T01:21:56.0498259Z   CC      mm/swap_state.o
2026-05-03T01:21:56.0740439Z   CC      fs/f2fs/file.o
2026-05-03T01:21:56.8310559Z   CC      mm/swapfile.o
2026-05-03T01:21:56.8940579Z   CC      kernel/sched/stop_task.o
2026-05-03T01:21:56.9990533Z   CC      fs/ext4/symlink.o
2026-05-03T01:21:57.6401314Z   CC      fs/ext4/sysfs.o
2026-05-03T01:21:57.7837265Z   CC      kernel/sched/pelt.o
2026-05-03T01:21:58.0060657Z   CC      fs/f2fs/inode.o
2026-05-03T01:21:58.2960343Z   CC      fs/ext4/xattr.o
2026-05-03T01:21:58.4760664Z   CC      mm/swap_slots.o
2026-05-03T01:21:58.7560358Z   CC      kernel/sched/stats.o
2026-05-03T01:21:59.0260377Z   CC      mm/dmapool.o
2026-05-03T01:21:59.1460624Z   CC      fs/f2fs/namei.o
2026-05-03T01:21:59.5370530Z   CC      fs/ext4/xattr_trusted.o
2026-05-03T01:21:59.6050604Z   CC      kernel/sched/debug.o
2026-05-03T01:21:59.8240333Z   CC      mm/sparse.o
2026-05-03T01:22:00.2040760Z   CC      fs/ext4/xattr_user.o
2026-05-03T01:22:00.2930718Z   CC      fs/f2fs/hash.o
2026-05-03T01:22:00.5970632Z   CC      mm/sparse-vmemmap.o
2026-05-03T01:22:00.6780398Z   CC      kernel/sched/tune.o
2026-05-03T01:22:00.8290395Z   CC      fs/ext4/acl.o
2026-05-03T01:22:00.9360734Z   CC      fs/f2fs/super.o
2026-05-03T01:22:01.1171335Z   CC      mm/ksm.o
2026-05-03T01:22:01.5208485Z   CC      fs/ext4/xattr_security.o
2026-05-03T01:22:02.1700283Z   CC      fs/ext4/verity.o
2026-05-03T01:22:02.1910570Z   CC      mm/slub.o
2026-05-03T01:22:02.2540422Z   CC      kernel/sched/cpuacct.o
2026-05-03T01:22:02.8540420Z   AR      fs/ext4/built-in.a
2026-05-03T01:22:02.8736773Z   CC      kernel/time/time.o
2026-05-03T01:22:03.0760418Z   CC      fs/f2fs/inline.o
2026-05-03T01:22:03.1460641Z   CC      kernel/sched/cpufreq.o
2026-05-03T01:22:03.8810695Z   CC      mm/migrate.o
2026-05-03T01:22:03.8890310Z   CC      kernel/time/timer.o
2026-05-03T01:22:04.0030498Z   CC      fs/f2fs/checkpoint.o
2026-05-03T01:22:04.3580617Z   CC      kernel/sched/cpufreq_schedutil.o
2026-05-03T01:22:05.1529074Z   CC      mm/page_counter.o
2026-05-03T01:22:05.2590440Z   CC      kernel/time/hrtimer.o
2026-05-03T01:22:05.3370406Z   CC      fs/f2fs/gc.o
2026-05-03T01:22:05.4357956Z   CC      mm/memcontrol.o
2026-05-03T01:22:05.9750387Z   CC      kernel/sched/membarrier.o
2026-05-03T01:22:06.3446281Z   CC      kernel/time/timekeeping.o
2026-05-03T01:22:06.7940455Z   CC      kernel/sched/isolation.o
2026-05-03T01:22:06.8460420Z   CC      fs/f2fs/data.o
2026-05-03T01:22:07.3826385Z   CC      kernel/time/ntp.o
2026-05-03T01:22:07.8630379Z   CC      mm/vmpressure.o
2026-05-03T01:22:07.9324678Z   CC      kernel/time/clocksource.o
2026-05-03T01:22:07.9795343Z   CC      kernel/sched/psi.o
2026-05-03T01:22:08.4270718Z   CC      mm/swap_cgroup.o
2026-05-03T01:22:08.5570422Z   CC      kernel/time/jiffies.o
2026-05-03T01:22:08.8200522Z   CC      fs/f2fs/node.o
2026-05-03T01:22:08.9428441Z   CC      mm/page_isolation.o
2026-05-03T01:22:08.9860378Z   AR      kernel/sched/built-in.a
2026-05-03T01:22:09.0738849Z   CC      kernel/time/timer_list.o
2026-05-03T01:22:09.1190728Z   CC      crypto/asymmetric_keys/asymmetric_type.o
2026-05-03T01:22:09.5786486Z   CC      mm/zsmalloc.o
2026-05-03T01:22:09.5946593Z   CC      kernel/time/timeconv.o
2026-05-03T01:22:09.7852688Z   CC      crypto/asymmetric_keys/restrict.o
2026-05-03T01:22:10.0600315Z   CC      kernel/time/timecounter.o
2026-05-03T01:22:10.0742377Z   CC      crypto/asymmetric_keys/signature.o
2026-05-03T01:22:10.1340462Z   CC      kernel/time/alarmtimer.o
2026-05-03T01:22:10.4519938Z   CC      fs/f2fs/segment.o
2026-05-03T01:22:10.6080789Z   CC      crypto/asymmetric_keys/public_key.o
2026-05-03T01:22:10.7280326Z   CC      mm/early_ioremap.o
2026-05-03T01:22:11.0854260Z   CC      kernel/time/posix-timers.o
2026-05-03T01:22:11.2207205Z   CC      mm/cma.o
2026-05-03T01:22:11.3117341Z   ASN.1   crypto/asymmetric_keys/x509.asn1.c
2026-05-03T01:22:11.3151877Z   ASN.1   crypto/asymmetric_keys/x509_akid.asn1.c
2026-05-03T01:22:11.3180787Z   CC      crypto/asymmetric_keys/x509_public_key.o
2026-05-03T01:22:11.7750453Z   ASN.1   crypto/asymmetric_keys/pkcs7.asn1.c
2026-05-03T01:22:11.7810218Z   CC      crypto/asymmetric_keys/pkcs7_trust.o
2026-05-03T01:22:11.8570485Z   CC      kernel/time/posix-cpu-timers.o
2026-05-03T01:22:12.1580553Z   CC      crypto/asymmetric_keys/pkcs7_verify.o
2026-05-03T01:22:12.2380327Z   CC      mm/frame_vector.o
2026-05-03T01:22:12.4331616Z   CC      fs/f2fs/recovery.o
2026-05-03T01:22:12.4680624Z   CC      kernel/time/posix-clock.o
2026-05-03T01:22:12.7130691Z   CC      crypto/asymmetric_keys/x509.asn1.o
2026-05-03T01:22:12.7500518Z   CC      crypto/asymmetric_keys/x509_akid.asn1.o
2026-05-03T01:22:12.7900488Z   CC      crypto/asymmetric_keys/x509_cert_parser.o
2026-05-03T01:22:12.9540888Z   CC      mm/usercopy.o
2026-05-03T01:22:13.1884082Z   CC      crypto/asymmetric_keys/pkcs7.asn1.o
2026-05-03T01:22:13.2331171Z   CC      crypto/asymmetric_keys/pkcs7_parser.o
2026-05-03T01:22:13.3370842Z   CC      kernel/time/itimer.o
2026-05-03T01:22:13.4060504Z   CC      fs/f2fs/shrinker.o
2026-05-03T01:22:13.6220543Z   CC      mm/memfd.o
2026-05-03T01:22:13.7488600Z   AR      crypto/asymmetric_keys/built-in.a
2026-05-03T01:22:13.7690688Z   CC      crypto/api.o
2026-05-03T01:22:13.9660516Z   CC      kernel/time/clockevents.o
2026-05-03T01:22:14.0089111Z   CC      fs/f2fs/extent_cache.o
2026-05-03T01:22:14.3244849Z   AR      mm/built-in.a
2026-05-03T01:22:14.4000354Z   CC      kernel/trace/trace_clock.o
2026-05-03T01:22:14.5981068Z   CC      kernel/time/tick-common.o
2026-05-03T01:22:14.7315026Z   CC      crypto/cipher.o
2026-05-03T01:22:14.8770574Z   CC      kernel/trace/ring_buffer.o
2026-05-03T01:22:14.9590671Z   CC      fs/f2fs/sysfs.o
2026-05-03T01:22:15.3670613Z   CC      crypto/compress.o
2026-05-03T01:22:15.6400436Z   CC      kernel/time/tick-broadcast.o
2026-05-03T01:22:15.9020407Z   CC      crypto/memneq.o
2026-05-03T01:22:15.9400356Z   CC      fs/f2fs/debug.o
2026-05-03T01:22:16.2593025Z   CC      kernel/trace/trace.o
2026-05-03T01:22:16.3244060Z   CC      kernel/time/tick-broadcast-hrtimer.o
2026-05-03T01:22:16.6316951Z   CC      crypto/crypto_wq.o
2026-05-03T01:22:16.6510483Z   CC      kernel/time/sched_clock.o
2026-05-03T01:22:16.6950355Z   CC      fs/f2fs/xattr.o
2026-05-03T01:22:17.0090669Z   CC      kernel/time/tick-oneshot.o
2026-05-03T01:22:17.3686100Z   CC      kernel/time/tick-sched.o
2026-05-03T01:22:17.3800474Z   CC      crypto/algapi.o
2026-05-03T01:22:17.5890421Z   CC      fs/f2fs/acl.o
2026-05-03T01:22:18.1950331Z   CC      kernel/trace/trace_output.o
2026-05-03T01:22:18.2197321Z   CC      fs/f2fs/verity.o
2026-05-03T01:22:18.3670263Z   CC      kernel/time/vsyscall.o
2026-05-03T01:22:18.6250473Z   CC      crypto/scatterwalk.o
2026-05-03T01:22:18.6550584Z   CC      kernel/time/timer_list_aee.o
2026-05-03T01:22:18.8761284Z   AR      fs/f2fs/built-in.a
2026-05-03T01:22:18.8990446Z   CC      fs/fat/cache.o
2026-05-03T01:22:19.2066273Z   AR      kernel/time/built-in.a
2026-05-03T01:22:19.2400797Z   CC      kernel/trace/trace_seq.o
2026-05-03T01:22:19.2580449Z   CC      fs/fat/dir.o
2026-05-03T01:22:19.4090787Z   CC      crypto/proc.o
2026-05-03T01:22:19.4565458Z   CC      block/partitions/check.o
2026-05-03T01:22:19.7800445Z   CC      kernel/trace/trace_stat.o
2026-05-03T01:22:19.9720566Z   CC      crypto/aead.o
2026-05-03T01:22:20.0468411Z   CC      block/partitions/msdos.o
2026-05-03T01:22:20.3654225Z   CC      fs/fat/fatent.o
2026-05-03T01:22:20.4250654Z   CC      kernel/trace/trace_printk.o
2026-05-03T01:22:20.6220627Z   CC      block/partitions/efi.o
2026-05-03T01:22:21.0950580Z   CC      crypto/ablkcipher.o
2026-05-03T01:22:21.2950551Z   AR      block/partitions/built-in.a
2026-05-03T01:22:21.3040532Z   CC      block/bio.o
2026-05-03T01:22:21.3280783Z   CC      kernel/trace/trace_sched_switch.o
2026-05-03T01:22:21.3510616Z   CC      fs/fat/file.o
2026-05-03T01:22:22.0460558Z   CC      crypto/blkcipher.o
2026-05-03T01:22:22.0776353Z   CC      kernel/trace/trace_nop.o
2026-05-03T01:22:22.3460602Z   CC      fs/fat/inode.o
2026-05-03T01:22:22.6180567Z   CC      kernel/trace/blktrace.o
2026-05-03T01:22:22.6935179Z   CC      block/elevator.o
2026-05-03T01:22:23.0460409Z   CC      crypto/skcipher.o
2026-05-03T01:22:23.4744290Z   CC      fs/fat/misc.o
2026-05-03T01:22:23.6760513Z   CC      kernel/trace/trace_events.o
2026-05-03T01:22:23.8700370Z   CC      block/blk-core.o
2026-05-03T01:22:24.1320354Z   CC      fs/fat/nfs.o
2026-05-03T01:22:24.3623120Z   CC      crypto/seqiv.o
2026-05-03T01:22:24.6470579Z   CC      fs/fat/namei_vfat.o
2026-05-03T01:22:24.9610585Z   CC      crypto/echainiv.o
2026-05-03T01:22:25.0700489Z   CC      kernel/trace/trace_export.o
2026-05-03T01:22:25.3670527Z   CC      fs/fat/namei_msdos.o
2026-05-03T01:22:25.5650674Z   CC      crypto/ahash.o
2026-05-03T01:22:25.6932177Z   CC      kernel/trace/trace_event_perf.o
2026-05-03T01:22:25.8540508Z   AR      fs/fat/built-in.a
2026-05-03T01:22:25.8730572Z   CC      block/blk-tag.o
2026-05-03T01:22:25.8790378Z   CC      fs/fuse/dev.o
2026-05-03T01:22:26.5961202Z   CC      kernel/trace/trace_events_filter.o
2026-05-03T01:22:26.6131049Z   CC      crypto/shash.o
2026-05-03T01:22:26.8490746Z   CC      block/blk-sysfs.o
2026-05-03T01:22:27.2630427Z   CC      fs/fuse/dir.o
2026-05-03T01:22:27.6040480Z   CC      crypto/akcipher.o
2026-05-03T01:22:27.7115100Z   CC      kernel/trace/trace_events_trigger.o
2026-05-03T01:22:27.8626180Z   CC      block/blk-flush.o
2026-05-03T01:22:28.0540357Z   CC      fs/fuse/file.o
2026-05-03T01:22:28.4914812Z   CC      crypto/kpp.o
2026-05-03T01:22:28.7180558Z   CC      kernel/trace/bpf_trace.o
2026-05-03T01:22:28.7560553Z   CC      block/blk-settings.o
2026-05-03T01:22:29.3719783Z   ASN.1   crypto/rsapubkey.asn1.c
2026-05-03T01:22:29.3740153Z   ASN.1   crypto/rsaprivkey.asn1.c
2026-05-03T01:22:29.3794417Z   CC      crypto/rsa.o
2026-05-03T01:22:29.4725921Z   CC      fs/fuse/inode.o
2026-05-03T01:22:29.6522229Z   CC      block/blk-ioc.o
2026-05-03T01:22:29.9216454Z   CC      crypto/rsa_helper.o
2026-05-03T01:22:30.1070448Z   CC      kernel/trace/trace_kprobe.o
2026-05-03T01:22:30.1190336Z   CC      crypto/rsa-pkcs1pad.o
2026-05-03T01:22:30.4524720Z   CC      fs/fuse/control.o
2026-05-03T01:22:30.5290375Z   CC      block/blk-map.o
2026-05-03T01:22:30.7310597Z   CC      crypto/acompress.o
2026-05-03T01:22:30.9280456Z   CC      kernel/trace/power-traces.o
2026-05-03T01:22:31.0690710Z   CC      fs/fuse/xattr.o
2026-05-03T01:22:31.3712032Z   CC      block/blk-exec.o
2026-05-03T01:22:31.6460413Z   CC      crypto/scompress.o
2026-05-03T01:22:31.6942774Z   CC      fs/fuse/acl.o
2026-05-03T01:22:32.1230369Z   CC      kernel/trace/rpm-traces.o
2026-05-03T01:22:32.1530469Z   CC      block/blk-merge.o
2026-05-03T01:22:32.2316822Z   CC      fs/fuse/passthrough.o
2026-05-03T01:22:32.5105802Z   CC      crypto/algboss.o
2026-05-03T01:22:32.8838413Z   AR      fs/fuse/built-in.a
2026-05-03T01:22:32.9068658Z   CC      fs/incfs/data_mgmt.o
2026-05-03T01:22:32.9681391Z   CC      kernel/trace/trace_probe.o
2026-05-03T01:22:33.1840544Z   CC      crypto/testmgr.o
2026-05-03T01:22:33.3181005Z ../fs/incfs/data_mgmt.c:1065:21: warning: variable 'mi' set but not used [-Wunused-but-set-variable]
2026-05-03T01:22:33.3209982Z         struct mount_info *mi = NULL;
2026-05-03T01:22:33.3239874Z                            ^
2026-05-03T01:22:33.3570354Z   CC      block/blk-softirq.o
2026-05-03T01:22:33.5386637Z 1 warning generated.
2026-05-03T01:22:33.5730603Z   CC      fs/incfs/format.o
2026-05-03T01:22:33.7080658Z   CC      kernel/trace/trace_uprobe.o
2026-05-03T01:22:34.0820565Z   CC      crypto/crypto_user.o
2026-05-03T01:22:34.0940173Z   CC      fs/incfs/integrity.o
2026-05-03T01:22:34.2260465Z   CC      block/blk-timeout.o
2026-05-03T01:22:34.4182543Z   CC      fs/incfs/main.o
2026-05-03T01:22:34.5158901Z   CC      kernel/trace/mtk_trace.o
2026-05-03T01:22:34.7844968Z   CC      crypto/cmac.o
2026-05-03T01:22:34.8020605Z   CC      fs/incfs/vfs.o
2026-05-03T01:22:35.0827527Z   CC [M]  kernel/trace/trace_mmstat.o
2026-05-03T01:22:35.0869029Z   CC      block/blk-lib.o
2026-05-03T01:22:35.4110497Z   CC      crypto/hmac.o
2026-05-03T01:22:35.7630395Z   AR      fs/incfs/built-in.a
2026-05-03T01:22:35.7810446Z   CC      fs/isofs/namei.o
2026-05-03T01:22:35.8425304Z   AR      kernel/trace/built-in.a
2026-05-03T01:22:35.8690720Z   CHK     kernel/kheaders_data.tar.xz
2026-05-03T01:22:35.9807084Z   CC      block/blk-mq.o
2026-05-03T01:22:36.0180570Z   CC      crypto/xcbc.o
2026-05-03T01:22:36.0220310Z   GEN     kernel/kheaders_data.tar.xz
2026-05-03T01:22:36.2280643Z   CC      fs/isofs/inode.o
2026-05-03T01:22:36.6580682Z   CC      crypto/crypto_null.o
2026-05-03T01:22:37.0070414Z   CC      fs/isofs/dir.o
2026-05-03T01:22:37.7531289Z   CC      crypto/md5.o
2026-05-03T01:22:37.7605530Z   CC      fs/isofs/util.o
2026-05-03T01:22:37.7628431Z   CC      block/blk-mq-tag.o
2026-05-03T01:22:38.4140516Z   CC      fs/isofs/rock.o
2026-05-03T01:22:38.8383615Z   CC      crypto/sha1_generic.o
2026-05-03T01:22:38.9840802Z   CC      block/blk-stat.o
2026-05-03T01:22:39.1963952Z   CC      fs/isofs/export.o
2026-05-03T01:22:39.8880519Z   CC      crypto/sha256_generic.o
2026-05-03T01:22:39.8990618Z   CC      fs/isofs/joliet.o
2026-05-03T01:22:40.2810414Z   CC      block/blk-mq-sysfs.o
2026-05-03T01:22:40.7231245Z   CC      fs/isofs/compress.o
2026-05-03T01:22:40.9850526Z   CC      crypto/sha512_generic.o
2026-05-03T01:22:41.4732330Z   CC      block/blk-mq-cpumap.o
2026-05-03T01:22:41.6460294Z   AR      fs/isofs/built-in.a
2026-05-03T01:22:41.6820404Z   CC      fs/jbd2/transaction.o
2026-05-03T01:22:42.0190666Z   CC      crypto/gf128mul.o
2026-05-03T01:22:42.4765250Z   CC      block/blk-mq-sched.o
2026-05-03T01:22:42.9180853Z   CC      crypto/ecb.o
2026-05-03T01:22:43.3515858Z   CC      fs/jbd2/commit.o
2026-05-03T01:22:43.7250460Z   CC      crypto/cbc.o
2026-05-03T01:22:43.8450387Z   CC      block/ioctl.o
2026-05-03T01:22:44.2378800Z   CC      fs/jbd2/recovery.o
2026-05-03T01:22:44.5800716Z   CC      crypto/cts.o
2026-05-03T01:22:45.0676919Z   CC      fs/jbd2/checkpoint.o
2026-05-03T01:22:45.3516151Z   CC      block/genhd.o
2026-05-03T01:22:45.4581674Z   CC      crypto/xts.o
2026-05-03T01:22:45.8423981Z   CC      fs/jbd2/revoke.o
2026-05-03T01:22:46.3030279Z   CC      crypto/ctr.o
2026-05-03T01:22:46.5169015Z ../fs/jbd2/revoke.c:532:17: warning: variable 'count' set but not used [-Wunused-but-set-variable]
2026-05-03T01:22:46.5221854Z         int i, offset, count;
2026-05-03T01:22:46.5267267Z                        ^
2026-05-03T01:22:46.6941763Z 1 warning generated.
2026-05-03T01:22:46.7617623Z   CC      fs/jbd2/journal.o
2026-05-03T01:22:46.9682615Z   CC      block/partition-generic.o
2026-05-03T01:22:47.1184328Z   CC      crypto/gcm.o
2026-05-03T01:22:48.1580380Z   CC      crypto/ccm.o
2026-05-03T01:22:48.3740390Z   CC      block/ioprio.o
2026-05-03T01:22:48.7783528Z   AR      fs/jbd2/built-in.a
2026-05-03T01:22:48.8270539Z   CC      fs/kernfs/mount.o
2026-05-03T01:22:49.1870625Z   CC      crypto/chacha20poly1305.o
2026-05-03T01:22:49.4630487Z   CC      fs/kernfs/inode.o
2026-05-03T01:22:49.6260422Z   CC      block/badblocks.o
2026-05-03T01:22:49.9464320Z   CC      crypto/cryptd.o
2026-05-03T01:22:50.0736278Z   CC      block/blk-rq-qos.o
2026-05-03T01:22:50.0900341Z   CC      fs/kernfs/dir.o
2026-05-03T01:22:50.5170313Z   CC      block/scsi_ioctl.o
2026-05-03T01:22:50.9220470Z   CC      fs/kernfs/file.o
2026-05-03T01:22:50.9440645Z   CC      crypto/des_generic.o
2026-05-03T01:22:51.3980399Z   CC      block/noop-iosched.o
2026-05-03T01:22:51.6530571Z   CC      crypto/blowfish_generic.o
2026-05-03T01:22:51.7760374Z   CC      fs/kernfs/symlink.o
2026-05-03T01:22:51.8430368Z   CC      block/deadline-iosched.o
2026-05-03T01:22:52.1341145Z   CC      crypto/blowfish_common.o
2026-05-03T01:22:52.3290539Z   CC      block/cfq-iosched.o
2026-05-03T01:22:52.3316795Z   AR      fs/kernfs/built-in.a
2026-05-03T01:22:52.3579161Z   CC      fs/nls/nls_base.o
2026-05-03T01:22:52.7840813Z   CC      crypto/twofish_generic.o
2026-05-03T01:22:52.8440399Z   CC      fs/nls/nls_cp437.o
2026-05-03T01:22:53.1490424Z   CC      fs/nls/nls_cp950.o
2026-05-03T01:22:53.1910775Z   CC      crypto/twofish_common.o
2026-05-03T01:22:53.2350531Z   CC      block/mq-deadline.o
2026-05-03T01:22:53.6050743Z   CC      fs/nls/nls_ascii.o
2026-05-03T01:22:53.7400420Z   CC      block/kyber-iosched.o
2026-05-03T01:22:53.7597240Z   CC      crypto/aes_generic.o
2026-05-03T01:22:53.8920460Z   CC      fs/nls/nls_iso8859-1.o
2026-05-03T01:22:54.1320609Z   CC      fs/nls/nls_utf8.o
2026-05-03T01:22:54.3700514Z   AR      fs/nls/built-in.a
2026-05-03T01:22:54.3930414Z   CC      fs/notify/dnotify/dnotify.o
2026-05-03T01:22:54.4062665Z   CC      crypto/arc4.o
2026-05-03T01:22:54.4190433Z   CC      block/bfq-iosched.o
2026-05-03T01:22:54.7370307Z   AR      fs/notify/dnotify/built-in.a
2026-05-03T01:22:54.7540485Z   AR      fs/notify/fanotify/built-in.a
2026-05-03T01:22:54.7720376Z   CC      fs/notify/inotify/inotify_fsnotify.o
2026-05-03T01:22:54.9860442Z   CC      crypto/chacha_generic.o
2026-05-03T01:22:55.1240985Z   CC      fs/notify/inotify/inotify_user.o
2026-05-03T01:22:55.5326366Z   CC      crypto/poly1305_generic.o
2026-05-03T01:22:55.5580922Z   CC      block/bfq-wf2q.o
2026-05-03T01:22:55.8610604Z   AR      fs/notify/inotify/built-in.a
2026-05-03T01:22:55.8682891Z   CC      fs/notify/fsnotify.o
2026-05-03T01:22:56.1030416Z   CC      crypto/deflate.o
2026-05-03T01:22:56.1130273Z   CC      block/bfq-cgroup.o
2026-05-03T01:22:56.5884631Z   CC      block/compat_ioctl.o
2026-05-03T01:22:56.5950387Z   CC      crypto/crc32c_generic.o
2026-05-03T01:22:56.6640359Z   CC      fs/notify/notification.o
2026-05-03T01:22:57.1600419Z   CC      crypto/crc32_generic.o
2026-05-03T01:22:57.2320571Z   CC      block/blk-mq-virtio.o
2026-05-03T01:22:57.4307888Z   CC      fs/notify/group.o
2026-05-03T01:22:57.6820501Z   CC      crypto/authenc.o
2026-05-03T01:22:57.9030335Z   CC      block/keyslot-manager.o
2026-05-03T01:22:58.0150336Z   CC      fs/notify/mark.o
2026-05-03T01:22:58.6110265Z   CC      fs/notify/fdinfo.o
2026-05-03T01:22:58.7240403Z   CC      block/bio-crypt-ctx.o
2026-05-03T01:22:58.8176883Z   CC      crypto/authencesn.o
2026-05-03T01:22:59.0736316Z   AR      fs/notify/built-in.a
2026-05-03T01:22:59.0980803Z   CC      fs/ntfs/aops.o
2026-05-03T01:22:59.4988060Z   CC      crypto/lzo.o
2026-05-03T01:22:59.5240483Z   CC      block/blk-crypto.o
2026-05-03T01:22:59.7630370Z   CC      fs/ntfs/attrib.o
2026-05-03T01:23:00.0165464Z   CC      crypto/lz4.o
2026-05-03T01:23:00.3337162Z   CC      crypto/rng.o
2026-05-03T01:23:00.3643442Z   CC      block/blk-crypto-fallback.o
2026-05-03T01:23:00.4440507Z   CC      fs/ntfs/collate.o
2026-05-03T01:23:00.9490374Z   CC      fs/ntfs/compress.o
2026-05-03T01:23:01.1040649Z   CC      crypto/drbg.o
2026-05-03T01:23:01.1750374Z   AR      block/built-in.a
2026-05-03T01:23:01.2330462Z   CC      fs/overlayfs/super.o
2026-05-03T01:23:01.6980981Z   CC      crypto/jitterentropy.o
2026-05-03T01:23:01.7026557Z   CC      fs/ntfs/debug.o
2026-05-03T01:23:01.7250773Z ../crypto/jitterentropy.c:668:6: warning: variable 'count_var' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:01.7279974Z         int count_var = 0;
2026-05-03T01:23:01.7309874Z             ^
2026-05-03T01:23:01.7340043Z 1 warning generated.
2026-05-03T01:23:01.7490269Z   CC      crypto/jitterentropy-kcapi.o
2026-05-03T01:23:01.9130403Z   CC      fs/overlayfs/namei.o
2026-05-03T01:23:01.9890640Z   CC      fs/ntfs/dir.o
2026-05-03T01:23:02.3320379Z   CC      crypto/ghash-generic.o
2026-05-03T01:23:02.4611046Z   CC      fs/overlayfs/util.o
2026-05-03T01:23:02.5140588Z   CC      fs/ntfs/file.o
2026-05-03T01:23:02.7601315Z   CC      kernel/fork.o
2026-05-03T01:23:02.9060412Z   CC      crypto/hash_info.o
2026-05-03T01:23:02.9700542Z   CC      crypto/simd.o
2026-05-03T01:23:02.9880908Z   CC      fs/overlayfs/inode.o
2026-05-03T01:23:03.0550719Z ../fs/ntfs/file.c:340:14: warning: variable 'base_ni' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:03.0579978Z         ntfs_inode *base_ni, *ni = NTFS_I(vi);
2026-05-03T01:23:03.0599912Z                     ^
2026-05-03T01:23:03.4541380Z   CC      fs/overlayfs/file.o
2026-05-03T01:23:03.4780408Z 1 warning generated.
2026-05-03T01:23:03.5110395Z   CC      fs/ntfs/index.o
2026-05-03T01:23:03.8610621Z   CC      crypto/rsapubkey.asn1.o
2026-05-03T01:23:03.9030452Z   CC      crypto/rsaprivkey.asn1.o
2026-05-03T01:23:03.9393703Z   CC      fs/overlayfs/dir.o
2026-05-03T01:23:03.9450699Z   AR      crypto/built-in.a
2026-05-03T01:23:03.9930513Z   CC      fs/ntfs/inode.o
2026-05-03T01:23:04.1120447Z   CC      fs/proc/task_mmu.o
2026-05-03T01:23:04.4869044Z ../fs/ntfs/inode.c:2378:6: warning: variable 'attr_len' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:04.4899922Z         u32 attr_len;
2026-05-03T01:23:04.4929906Z             ^
2026-05-03T01:23:04.5670797Z   CC      kernel/exec_domain.o
2026-05-03T01:23:04.5810752Z   CC      fs/overlayfs/readdir.o
2026-05-03T01:23:04.7560375Z 1 warning generated.
2026-05-03T01:23:04.7901804Z   CC      fs/ntfs/mft.o
2026-05-03T01:23:04.9780564Z   CC      fs/proc/inode.o
2026-05-03T01:23:05.1400942Z   CC      kernel/panic.o
2026-05-03T01:23:05.2402475Z   CC      fs/overlayfs/copy_up.o
2026-05-03T01:23:05.5080402Z   CC      fs/proc/root.o
2026-05-03T01:23:05.7774314Z   CC      fs/ntfs/mst.o
2026-05-03T01:23:05.8933061Z   CC      fs/overlayfs/export.o
2026-05-03T01:23:05.9745214Z   CC      fs/proc/base.o
2026-05-03T01:23:05.9880339Z   CC      kernel/cpu.o
2026-05-03T01:23:06.2188852Z   CC      fs/ntfs/namei.o
2026-05-03T01:23:06.3517980Z   AR      fs/overlayfs/built-in.a
2026-05-03T01:23:06.3620354Z   CC      kernel/exit.o
2026-05-03T01:23:06.7480469Z   CC      fs/ntfs/runlist.o
2026-05-03T01:23:07.0510580Z   CC      fs/proc/generic.o
2026-05-03T01:23:07.4170727Z   CC      wt_sys/trigger_panic.o
2026-05-03T01:23:07.4840563Z   CC      fs/ntfs/super.o
2026-05-03T01:23:07.7916891Z   CC      fs/proc/array.o
2026-05-03T01:23:07.7945480Z   AR      wt_sys/built-in.a
2026-05-03T01:23:07.8119226Z   CC      fs/pstore/inode.o
2026-05-03T01:23:08.1687567Z   CC      kernel/softirq.o
2026-05-03T01:23:08.3070641Z   CC      fs/ntfs/sysctl.o
2026-05-03T01:23:08.3910660Z   CC      fs/pstore/platform.o
2026-05-03T01:23:08.5503641Z   CC      fs/proc/fd.o
2026-05-03T01:23:08.6748931Z   CC      fs/ntfs/unistr.o
2026-05-03T01:23:08.9920617Z   CC      fs/pstore/pmsg.o
2026-05-03T01:23:09.0390530Z   CC      fs/proc/proc_tty.o
2026-05-03T01:23:09.1980472Z   CC      fs/ntfs/upcase.o
2026-05-03T01:23:09.2330426Z   CC      kernel/resource.o
2026-05-03T01:23:09.3820401Z   CC      fs/pstore/ram.o
2026-05-03T01:23:09.4866353Z   CC      fs/proc/cmdline.o
2026-05-03T01:23:09.6860373Z   CC      fs/ntfs/bitmap.o
2026-05-03T01:23:09.8381024Z   CC      fs/proc/consoles.o
2026-05-03T01:23:09.9512284Z   CC      fs/pstore/ram_core.o
2026-05-03T01:23:10.1040403Z   CC      kernel/sysctl.o
2026-05-03T01:23:10.2091389Z   CC      fs/ntfs/lcnalloc.o
2026-05-03T01:23:10.2540442Z   CC      fs/proc/cpuinfo.o
2026-05-03T01:23:10.5648763Z   AR      fs/pstore/built-in.a
2026-05-03T01:23:10.5880158Z   CC      fs/quota/dquot.o
2026-05-03T01:23:10.6330624Z   CC      fs/proc/devices.o
2026-05-03T01:23:10.7990690Z   CC      fs/ntfs/logfile.o
2026-05-03T01:23:10.9720422Z   CC      fs/proc/interrupts.o
2026-05-03T01:23:11.0770960Z ../fs/quota/dquot.c:1054:6: warning: variable 'reserved' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:11.0810031Z         int reserved = 0;
2026-05-03T01:23:11.0830115Z             ^
2026-05-03T01:23:11.2880781Z ../fs/ntfs/logfile.c:495:21: warning: variable 'log_page_mask' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:11.2910069Z         int log_page_size, log_page_mask, err;
2026-05-03T01:23:11.2939929Z                            ^
2026-05-03T01:23:11.3740557Z   CC      fs/proc/loadavg.o
2026-05-03T01:23:11.4260631Z 1 warning generated.
2026-05-03T01:23:11.4530827Z 1 warning generated.
2026-05-03T01:23:11.4559952Z   CC      fs/ntfs/quota.o
2026-05-03T01:23:11.7340439Z   CC      fs/quota/quota_v2.o
2026-05-03T01:23:11.8090323Z   CC      fs/proc/meminfo.o
2026-05-03T01:23:11.8300505Z   CC      kernel/sysctl_binary.o
2026-05-03T01:23:11.9710558Z   CC      fs/ntfs/usnjrnl.o
2026-05-03T01:23:12.1360542Z   CC      fs/quota/quota_tree.o
2026-05-03T01:23:12.3420631Z   CC      fs/proc/stat.o
2026-05-03T01:23:12.4794783Z   AR      fs/ntfs/built-in.a
2026-05-03T01:23:12.5000586Z   CC      fs/ramfs/inode.o
2026-05-03T01:23:12.7374854Z   CC      kernel/capability.o
2026-05-03T01:23:12.7930568Z   CC      fs/proc/uptime.o
2026-05-03T01:23:12.8880400Z   CC      fs/quota/quota.o
2026-05-03T01:23:13.0900658Z   CC      fs/ramfs/file-mmu.o
2026-05-03T01:23:13.1620368Z   CC      fs/proc/util.o
2026-05-03T01:23:13.3700582Z   CC      fs/proc/version.o
2026-05-03T01:23:13.4890650Z   AR      fs/ramfs/built-in.a
2026-05-03T01:23:13.5422911Z   CC      drivers/amba/bus.o
2026-05-03T01:23:13.5980123Z   CC      fs/quota/kqid.o
2026-05-03T01:23:13.6570434Z   CC      kernel/ptrace.o
2026-05-03T01:23:13.7208401Z   CC      fs/proc/softirqs.o
2026-05-03T01:23:14.1005832Z   CC      fs/quota/netlink.o
2026-05-03T01:23:14.1030740Z   CC      fs/proc/namespaces.o
2026-05-03T01:23:14.1783366Z   AR      drivers/amba/built-in.a
2026-05-03T01:23:14.1960353Z   CC      drivers/android/binderfs.o
2026-05-03T01:23:14.6930422Z   CC      kernel/user.o
2026-05-03T01:23:14.7120713Z   CC      fs/proc/self.o
2026-05-03T01:23:14.7500572Z   CC      drivers/android/binder.o
2026-05-03T01:23:14.9950566Z   AR      fs/quota/built-in.a
2026-05-03T01:23:15.0394285Z   AR      sound/arm/built-in.a
2026-05-03T01:23:15.0566050Z   AR      sound/atmel/built-in.a
2026-05-03T01:23:15.0858721Z   CC      sound/core/seq/seq.o
2026-05-03T01:23:15.1527160Z   CC      fs/proc/thread_self.o
2026-05-03T01:23:15.2420496Z   CC      kernel/signal.o
2026-05-03T01:23:15.5160601Z   CC      sound/core/seq/seq_lock.o
2026-05-03T01:23:15.6043544Z   CC      fs/proc/secboot_fuse.o
2026-05-03T01:23:15.9490905Z   CC      fs/proc/serial_num.o
2026-05-03T01:23:15.9518319Z   CC      sound/core/seq/seq_clientmgr.o
2026-05-03T01:23:16.3097855Z   CC      fs/proc/proc_sysctl.o
2026-05-03T01:23:16.6920253Z   CC      drivers/android/binder_alloc.o
2026-05-03T01:23:16.8661004Z   CC      sound/core/seq/seq_memory.o
2026-05-03T01:23:17.2310313Z   CC      kernel/sys.o
2026-05-03T01:23:17.2940416Z   CC      fs/proc/proc_net.o
2026-05-03T01:23:17.4850542Z   AR      drivers/android/built-in.a
2026-05-03T01:23:17.5020295Z   AR      drivers/auxdisplay/built-in.a
2026-05-03T01:23:17.5280980Z   CC      drivers/base/firmware_loader/fallback_table.o
2026-05-03T01:23:17.5580561Z   CC      sound/core/seq/seq_queue.o
2026-05-03T01:23:18.0900484Z   CC      sound/core/seq/seq_fifo.o
2026-05-03T01:23:18.1140387Z   CC      fs/proc/kmsg.o
2026-05-03T01:23:18.2160427Z   CC      drivers/base/firmware_loader/main.o
2026-05-03T01:23:18.5090524Z   CC      fs/proc/page.o
2026-05-03T01:23:18.5630529Z   CC      sound/core/seq/seq_prioq.o
2026-05-03T01:23:18.8102818Z   CC      kernel/umh.o
2026-05-03T01:23:19.0280540Z   CC      sound/core/seq/seq_timer.o
2026-05-03T01:23:19.0950574Z   CC      drivers/base/firmware_loader/fallback.o
2026-05-03T01:23:19.1130766Z   AR      fs/proc/built-in.a
2026-05-03T01:23:19.1370359Z   CC      fs/sdcardfs/dentry.o
2026-05-03T01:23:19.5080599Z   CC      sound/core/seq/seq_system.o
2026-05-03T01:23:19.6200847Z   CC      fs/sdcardfs/file.o
2026-05-03T01:23:19.6470595Z   AR      drivers/base/firmware_loader/built-in.a
2026-05-03T01:23:19.6710613Z   CC      drivers/base/power/sysfs.o
2026-05-03T01:23:19.7580538Z   CC      kernel/workqueue.o
2026-05-03T01:23:19.9245503Z   CC      sound/core/seq/seq_ports.o
2026-05-03T01:23:20.0861619Z   CC      fs/sdcardfs/inode.o
2026-05-03T01:23:20.2330379Z   CC      drivers/base/power/generic_ops.o
2026-05-03T01:23:20.6116693Z   CC      sound/core/seq/seq_info.o
2026-05-03T01:23:20.6160148Z   CC      fs/sdcardfs/main.o
2026-05-03T01:23:20.7140414Z   CC      drivers/base/power/common.o
2026-05-03T01:23:21.0389039Z   CC      sound/core/seq/seq_dummy.o
2026-05-03T01:23:21.2920338Z   CC      drivers/base/power/qos.o
2026-05-03T01:23:21.3711805Z   CC      fs/sdcardfs/super.o
2026-05-03T01:23:21.4427270Z   CC      sound/core/seq/seq_midi.o
2026-05-03T01:23:21.5000868Z   CC      kernel/pid.o
2026-05-03T01:23:21.8530637Z   CC      fs/sdcardfs/lookup.o
2026-05-03T01:23:21.8970437Z   CC      sound/core/seq/seq_midi_event.o
2026-05-03T01:23:22.2729882Z ../fs/sdcardfs/lookup.c:89:30: warning: variable 'info' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:22.2740020Z         struct sdcardfs_inode_info *info;
2026-05-03T01:23:22.2798040Z                                     ^
2026-05-03T01:23:22.2800487Z ../fs/sdcardfs/lookup.c:261:27: warning: variable 'sbi' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:22.2830001Z         struct sdcardfs_sb_info *sbi;
2026-05-03T01:23:22.2859875Z                                  ^
2026-05-03T01:23:22.3172248Z   CC      drivers/base/power/runtime.o
2026-05-03T01:23:22.3190105Z 2 warnings generated.
2026-05-03T01:23:22.3714302Z   CC      fs/sdcardfs/mmap.o
2026-05-03T01:23:22.3866037Z   AR      sound/core/seq/built-in.a
2026-05-03T01:23:22.4025394Z   CC      sound/core/sound.o
2026-05-03T01:23:22.5598875Z   CC      kernel/task_work.o
2026-05-03T01:23:22.8374551Z   CC      fs/sdcardfs/packagelist.o
2026-05-03T01:23:23.0490669Z   CC      drivers/base/power/wakeirq.o
2026-05-03T01:23:23.0680598Z   CC      sound/core/init.o
2026-05-03T01:23:23.1360596Z   CC      kernel/extable.o
2026-05-03T01:23:23.6270539Z   CC      drivers/base/power/main.o
2026-05-03T01:23:23.8220491Z   CC      kernel/params.o
2026-05-03T01:23:23.8480454Z   CC      sound/core/memory.o
2026-05-03T01:23:24.3530403Z   CC      sound/core/control.o
2026-05-03T01:23:24.4550603Z   CC      fs/sdcardfs/derived_perm.o
2026-05-03T01:23:24.4720547Z   CC      kernel/kthread.o
2026-05-03T01:23:24.9280677Z   CC      drivers/base/power/wakeup.o
2026-05-03T01:23:24.9640594Z   AR      fs/sdcardfs/built-in.a
2026-05-03T01:23:24.9850207Z   CC      fs/sysfs/file.o
2026-05-03T01:23:25.4880480Z   CC      kernel/sys_ni.o
2026-05-03T01:23:25.5760600Z   CC      sound/core/misc.o
2026-05-03T01:23:25.6726422Z   CC      fs/sysfs/dir.o
2026-05-03T01:23:25.6950630Z   CC      kernel/nsproxy.o
2026-05-03T01:23:26.0430443Z   CC      sound/core/device.o
2026-05-03T01:23:26.0640581Z   CC      drivers/base/power/wakeup_stats.o
2026-05-03T01:23:26.2000438Z   CC      fs/sysfs/symlink.o
2026-05-03T01:23:26.3146728Z   CC      kernel/notifier.o
2026-05-03T01:23:26.4170729Z   CC      drivers/base/power/domain.o
2026-05-03T01:23:26.5384715Z   CC      sound/core/info.o
2026-05-03T01:23:26.8630419Z   CC      fs/sysfs/mount.o
2026-05-03T01:23:27.0480630Z   CC      kernel/ksysfs.o
2026-05-03T01:23:27.2285319Z   CC      fs/sysfs/group.o
2026-05-03T01:23:27.3160813Z   CC      sound/core/ctljack.o
2026-05-03T01:23:27.5416272Z   CC      drivers/base/power/domain_governor.o
2026-05-03T01:23:27.6132561Z   CC      sound/core/jack.o
2026-05-03T01:23:27.6780975Z   AR      fs/sysfs/built-in.a
2026-05-03T01:23:27.6826058Z   CC      kernel/cred.o
2026-05-03T01:23:27.7022418Z   CC      fs/tracefs/inode.o
2026-05-03T01:23:27.8890525Z   CC      drivers/base/power/clock_ops.o
2026-05-03T01:23:28.2430960Z   CC      sound/core/hwdep.o
2026-05-03T01:23:28.2560262Z   AR      fs/tracefs/built-in.a
2026-05-03T01:23:28.2732574Z   SHIPPED fs/unicode/utf8data.h
2026-05-03T01:23:28.2766864Z   CC      fs/unicode/utf8-core.o
2026-05-03T01:23:28.5272153Z   AR      drivers/base/power/built-in.a
2026-05-03T01:23:28.5585656Z   CC      drivers/base/regmap/regmap.o
2026-05-03T01:23:28.5940506Z   CC      kernel/reboot.o
2026-05-03T01:23:28.7300422Z   CC      fs/unicode/utf8-norm.o
2026-05-03T01:23:29.0030304Z   CC      sound/core/timer.o
2026-05-03T01:23:29.3570699Z   AR      fs/unicode/built-in.a
2026-05-03T01:23:29.3810334Z   CC      fs/verity/enable.o
2026-05-03T01:23:29.5409687Z   CC      kernel/async.o
2026-05-03T01:23:29.9748398Z   CC      kernel/range.o
2026-05-03T01:23:30.0470456Z   CC      sound/core/hrtimer.o
2026-05-03T01:23:30.0690549Z   CC      drivers/base/regmap/regcache.o
2026-05-03T01:23:30.1040537Z   CC      kernel/smpboot.o
2026-05-03T01:23:30.3440565Z   CC      fs/verity/hash_algs.o
2026-05-03T01:23:30.3700533Z   CC      sound/core/pcm.o
2026-05-03T01:23:30.6470374Z   CC      kernel/ucount.o
2026-05-03T01:23:30.8330433Z   CC      drivers/base/regmap/regcache-rbtree.o
2026-05-03T01:23:30.8807719Z   CC      fs/verity/init.o
2026-05-03T01:23:30.9450583Z   CC      kernel/kmod.o
2026-05-03T01:23:31.2276007Z   CC      fs/verity/measure.o
2026-05-03T01:23:31.2800664Z   CC      sound/core/pcm_native.o
2026-05-03T01:23:31.3440590Z   CC      drivers/base/regmap/regcache-flat.o
2026-05-03T01:23:31.7730557Z   CC      fs/verity/open.o
2026-05-03T01:23:31.7940733Z   CC      drivers/base/regmap/regmap-i2c.o
2026-05-03T01:23:31.8390676Z   CC      kernel/groups.o
2026-05-03T01:23:32.3370398Z   CC      fs/verity/verify.o
2026-05-03T01:23:32.3930652Z   CC      drivers/base/regmap/regmap-spi.o
2026-05-03T01:23:32.7817119Z   CC      kernel/freezer.o
2026-05-03T01:23:33.0530380Z   CC      fs/verity/signature.o
2026-05-03T01:23:33.0730773Z   CC      drivers/base/regmap/regmap-mmio.o
2026-05-03T01:23:33.0941473Z   CC      sound/core/pcm_lib.o
2026-05-03T01:23:33.6029102Z   AR      fs/verity/built-in.a
2026-05-03T01:23:33.6038168Z   CC      kernel/profile.o
2026-05-03T01:23:33.6177755Z   CC      fs/open.o
2026-05-03T01:23:33.7060517Z   AR      drivers/base/regmap/built-in.a
2026-05-03T01:23:33.7310342Z   AR      drivers/base/test/built-in.a
2026-05-03T01:23:33.7400143Z   CC      drivers/base/component.o
2026-05-03T01:23:34.4347536Z   CC      kernel/stacktrace.o
2026-05-03T01:23:34.4460563Z   CC      drivers/base/core.o
2026-05-03T01:23:34.4730625Z   CC      sound/core/pcm_misc.o
2026-05-03T01:23:34.7910382Z   CC      fs/read_write.o
2026-05-03T01:23:35.0982404Z   CC      kernel/futex.o
2026-05-03T01:23:35.1372226Z   CC      sound/core/pcm_memory.o
2026-05-03T01:23:35.8952015Z   CC      sound/core/memalloc.o
2026-05-03T01:23:35.9320483Z   CC      drivers/base/bus.o
2026-05-03T01:23:36.1320614Z   CC      fs/file_table.o
2026-05-03T01:23:36.2350179Z   CC      kernel/smp.o
2026-05-03T01:23:36.6081793Z   CC      drivers/base/dd.o
2026-05-03T01:23:36.6680714Z   CC      sound/core/pcm_timer.o
2026-05-03T01:23:36.8120399Z   CC      kernel/uid16.o
2026-05-03T01:23:37.0310546Z   CC      fs/super.o
2026-05-03T01:23:37.1630584Z   CC      sound/core/seq_device.o
2026-05-03T01:23:37.4439991Z   CC      drivers/base/syscore.o
2026-05-03T01:23:37.4710574Z   CC      kernel/module.o
2026-05-03T01:23:37.7961166Z   CC      sound/core/rawmidi.o
2026-05-03T01:23:38.1300648Z   CC      fs/char_dev.o
2026-05-03T01:23:38.4110515Z   CC      drivers/base/driver.o
2026-05-03T01:23:38.8842032Z   CC      drivers/base/class.o
2026-05-03T01:23:38.9072407Z   AR      sound/core/built-in.a
2026-05-03T01:23:38.9580693Z   AR      sound/drivers/mpu401/built-in.a
2026-05-03T01:23:38.9821047Z   AR      sound/drivers/opl3/built-in.a
2026-05-03T01:23:39.0060578Z   AR      sound/drivers/opl4/built-in.a
2026-05-03T01:23:39.0120007Z   CC      fs/stat.o
2026-05-03T01:23:39.0210121Z   AR      sound/drivers/pcsp/built-in.a
2026-05-03T01:23:39.0340243Z   AR      sound/drivers/vx/built-in.a
2026-05-03T01:23:39.0510114Z   AR      sound/drivers/built-in.a
2026-05-03T01:23:39.0690186Z   AR      sound/firewire/built-in.a
2026-05-03T01:23:39.0840117Z   AR      sound/hda/built-in.a
2026-05-03T01:23:39.1070361Z   AR      sound/i2c/other/built-in.a
2026-05-03T01:23:39.1260299Z   AR      sound/i2c/built-in.a
2026-05-03T01:23:39.1633294Z   AR      sound/isa/ad1816a/built-in.a
2026-05-03T01:23:39.1687074Z   CC      kernel/kallsyms.o
2026-05-03T01:23:39.1806918Z   AR      sound/isa/ad1848/built-in.a
2026-05-03T01:23:39.1980250Z   AR      sound/isa/cs423x/built-in.a
2026-05-03T01:23:39.2151191Z   AR      sound/isa/es1688/built-in.a
2026-05-03T01:23:39.2328891Z   AR      sound/isa/galaxy/built-in.a
2026-05-03T01:23:39.2491517Z   AR      sound/isa/gus/built-in.a
2026-05-03T01:23:39.2690303Z   AR      sound/isa/msnd/built-in.a
2026-05-03T01:23:39.2840326Z   AR      sound/isa/opti9xx/built-in.a
2026-05-03T01:23:39.3010309Z   AR      sound/isa/sb/built-in.a
2026-05-03T01:23:39.3190851Z   AR      sound/isa/wavefront/built-in.a
2026-05-03T01:23:39.3349038Z   AR      sound/isa/wss/built-in.a
2026-05-03T01:23:39.3636080Z   AR      sound/isa/built-in.a
2026-05-03T01:23:39.3774188Z   AR      sound/mips/built-in.a
2026-05-03T01:23:39.3950355Z   AR      sound/parisc/built-in.a
2026-05-03T01:23:39.4180392Z   AR      sound/pci/ac97/built-in.a
2026-05-03T01:23:39.4360349Z   AR      sound/pci/ali5451/built-in.a
2026-05-03T01:23:39.4540325Z   AR      sound/pci/asihpi/built-in.a
2026-05-03T01:23:39.4720323Z   AR      sound/pci/au88x0/built-in.a
2026-05-03T01:23:39.4880423Z   AR      sound/pci/aw2/built-in.a
2026-05-03T01:23:39.5033216Z   CC      drivers/base/platform.o
2026-05-03T01:23:39.5058453Z   AR      sound/pci/ca0106/built-in.a
2026-05-03T01:23:39.5257094Z   AR      sound/pci/cs46xx/built-in.a
2026-05-03T01:23:39.5470332Z   AR      sound/pci/cs5535audio/built-in.a
2026-05-03T01:23:39.5618665Z   AR      sound/pci/ctxfi/built-in.a
2026-05-03T01:23:39.5796922Z   AR      sound/pci/echoaudio/built-in.a
2026-05-03T01:23:39.5970329Z   AR      sound/pci/emu10k1/built-in.a
2026-05-03T01:23:39.6129315Z   AR      sound/pci/hda/built-in.a
2026-05-03T01:23:39.6310270Z   AR      sound/pci/ice1712/built-in.a
2026-05-03T01:23:39.6480505Z   AR      sound/pci/korg1212/built-in.a
2026-05-03T01:23:39.6643348Z   AR      sound/pci/lola/built-in.a
2026-05-03T01:23:39.6827925Z   AR      sound/pci/lx6464es/built-in.a
2026-05-03T01:23:39.6993050Z   AR      sound/pci/mixart/built-in.a
2026-05-03T01:23:39.7170180Z   AR      sound/pci/nm256/built-in.a
2026-05-03T01:23:39.7358307Z   AR      sound/pci/oxygen/built-in.a
2026-05-03T01:23:39.7533004Z   AR      sound/pci/pcxhr/built-in.a
2026-05-03T01:23:39.7670051Z   AR      sound/pci/riptide/built-in.a
2026-05-03T01:23:39.7843588Z   AR      sound/pci/rme9652/built-in.a
2026-05-03T01:23:39.8000139Z   AR      sound/pci/trident/built-in.a
2026-05-03T01:23:39.8150127Z   AR      sound/pci/vx222/built-in.a
2026-05-03T01:23:39.8330148Z   AR      sound/pci/ymfpci/built-in.a
2026-05-03T01:23:39.8720410Z   AR      sound/pci/built-in.a
2026-05-03T01:23:39.8930330Z   AR      sound/pcmcia/pdaudiocf/built-in.a
2026-05-03T01:23:39.9080384Z   AR      sound/pcmcia/vx/built-in.a
2026-05-03T01:23:39.9200209Z   AR      sound/pcmcia/built-in.a
2026-05-03T01:23:39.9350107Z   AR      sound/ppc/built-in.a
2026-05-03T01:23:39.9519876Z   AR      sound/sh/built-in.a
2026-05-03T01:23:39.9569126Z   CC      fs/exec.o
2026-05-03T01:23:39.9739865Z   AR      sound/soc/adi/built-in.a
2026-05-03T01:23:39.9897160Z   AR      sound/soc/amd/built-in.a
2026-05-03T01:23:40.0070255Z   AR      sound/soc/atmel/built-in.a
2026-05-03T01:23:40.0260094Z   AR      sound/soc/au1x/built-in.a
2026-05-03T01:23:40.0410075Z   AR      sound/soc/bcm/built-in.a
2026-05-03T01:23:40.0590159Z   AR      sound/soc/cirrus/built-in.a
2026-05-03T01:23:40.0830191Z   CC      sound/soc/codecs/aw87xxx/aw87xxx.o
2026-05-03T01:23:40.2511982Z   CC      kernel/compat.o
2026-05-03T01:23:40.4490443Z   CC      drivers/base/cpu.o
2026-05-03T01:23:40.6120838Z ../sound/soc/codecs/aw87xxx/aw87xxx.c:513:8: warning: variable 'profile' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:40.6159948Z         char *profile;
2026-05-03T01:23:40.6190004Z               ^
2026-05-03T01:23:40.7940378Z 1 warning generated.
2026-05-03T01:23:41.0917529Z   CC      drivers/base/firmware.o
2026-05-03T01:23:41.1060290Z   CC      sound/soc/codecs/aw87xxx/aw87xxx_device.o
2026-05-03T01:23:41.2740466Z   CC      kernel/utsname.o
2026-05-03T01:23:41.4470576Z   CC      fs/pipe.o
2026-05-03T01:23:41.5210664Z   CC      drivers/base/init.o
2026-05-03T01:23:41.5890412Z   CC      kernel/pid_namespace.o
2026-05-03T01:23:41.7650549Z   CC      sound/soc/codecs/aw87xxx/aw87xxx_monitor.o
2026-05-03T01:23:41.8150355Z   CC      drivers/base/map.o
2026-05-03T01:23:42.1730382Z   CC      drivers/base/devres.o
2026-05-03T01:23:42.4650591Z   GZIP    kernel/config_data.gz
2026-05-03T01:23:42.4804227Z   CC      kernel/stop_machine.o
2026-05-03T01:23:42.5060560Z   CC      fs/namei.o
2026-05-03T01:23:42.5140383Z   CC      sound/soc/codecs/aw87xxx/aw87xxx_bin_parse.o
2026-05-03T01:23:42.7299518Z   CC      drivers/base/attribute_container.o
2026-05-03T01:23:43.0280629Z   CC      sound/soc/codecs/aw87xxx/aw87xxx_dsp.o
2026-05-03T01:23:43.2242869Z   CC      kernel/audit.o
2026-05-03T01:23:43.2410166Z   CC      drivers/base/transport_class.o
2026-05-03T01:23:43.7086364Z   CC      drivers/base/topology.o
2026-05-03T01:23:43.8130525Z   CC      sound/soc/codecs/aw87xxx/aw87xxx_acf_bin.o
2026-05-03T01:23:44.1730840Z   CC      drivers/base/container.o
2026-05-03T01:23:44.2240919Z ../sound/soc/codecs/aw87xxx/aw87xxx_acf_bin.c:152:21: warning: variable 'acf_dde' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:44.2241864Z         struct aw_acf_dde *acf_dde = NULL;
2026-05-03T01:23:44.2242255Z                            ^
2026-05-03T01:23:44.2243493Z ../sound/soc/codecs/aw87xxx/aw87xxx_acf_bin.c:284:31: warning: variable 'acf_dde' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:44.2244358Z         struct aw_acf_dde_v_1_0_0_0 *acf_dde = NULL;
2026-05-03T01:23:44.2244788Z                                      ^
2026-05-03T01:23:44.3632837Z   CC      fs/fcntl.o
2026-05-03T01:23:44.4590401Z   CC      drivers/base/property.o
2026-05-03T01:23:44.5770458Z 2 warnings generated.
2026-05-03T01:23:44.6130539Z   AR      sound/soc/codecs/aw87xxx/built-in.a
2026-05-03T01:23:44.6580416Z   CC      sound/soc/codecs/sipa/sipa.o
2026-05-03T01:23:44.7180389Z   CC      kernel/auditfilter.o
2026-05-03T01:23:45.3480542Z   CC      fs/ioctl.o
2026-05-03T01:23:45.7990616Z   CC      kernel/auditsc.o
2026-05-03T01:23:45.8255295Z   CC      drivers/base/cacheinfo.o
2026-05-03T01:23:45.8330873Z   CC      sound/soc/codecs/sipa/sipa_regmap.o
2026-05-03T01:23:46.3430337Z   CC      drivers/base/devcon.o
2026-05-03T01:23:46.3640364Z   CC      fs/readdir.o
2026-05-03T01:23:46.4840585Z   CC      sound/soc/codecs/sipa/sipa_aux_dev_if.o
2026-05-03T01:23:46.7950368Z   CC      drivers/base/module.o
2026-05-03T01:23:47.0531249Z   CC      kernel/audit_watch.o
2026-05-03T01:23:47.0750779Z ../drivers/base/module.c:36:6: warning: variable 'no_warn' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:47.0810043Z         int no_warn;
2026-05-03T01:23:47.0839957Z             ^
2026-05-03T01:23:47.0929901Z 1 warning generated.
2026-05-03T01:23:47.1199093Z   CC      drivers/base/soc.o
2026-05-03T01:23:47.3150283Z   CC      fs/select.o
2026-05-03T01:23:47.3470415Z   CC      sound/soc/codecs/sipa/sipa_91xx.o
2026-05-03T01:23:47.6210521Z   CC      drivers/base/pinctrl.o
2026-05-03T01:23:47.7332372Z   CC      kernel/audit_fsnotify.o
2026-05-03T01:23:47.8731082Z ../sound/soc/codecs/sipa/sipa_91xx.c:82:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:47.8750278Z         int ret;
2026-05-03T01:23:47.8759872Z             ^
2026-05-03T01:23:47.9500349Z 1 warning generated.
2026-05-03T01:23:47.9793940Z   CC      sound/soc/codecs/sipa/sipa_parameter.o
2026-05-03T01:23:48.0240635Z   CC      drivers/base/platform-msi.o
2026-05-03T01:23:48.3660660Z   CC      kernel/audit_tree.o
2026-05-03T01:23:48.5910858Z   CC      sound/soc/codecs/sipa/sipa_tuning_misc.o
2026-05-03T01:23:48.6060432Z   CC      drivers/base/arch_topology.o
2026-05-03T01:23:48.9560598Z   CC      fs/dcache.o
2026-05-03T01:23:49.0077929Z   CC      sound/soc/codecs/sipa/sipa_tuning_if.o
2026-05-03T01:23:49.1240597Z   AR      drivers/base/built-in.a
2026-05-03T01:23:49.1561168Z   CC      kernel/kprobes.o
2026-05-03T01:23:49.1760797Z   CC      drivers/block/zram/zcomp.o
2026-05-03T01:23:49.4450425Z   AR      sound/soc/codecs/sipa/built-in.a
2026-05-03T01:23:49.4590321Z   CC      sound/soc/codecs/mt6358.o
2026-05-03T01:23:49.5570713Z   CC      drivers/block/zram/zram_drv.o
2026-05-03T01:23:50.1300314Z   CC      fs/inode.o
2026-05-03T01:23:50.2020352Z   CC      kernel/seccomp.o
2026-05-03T01:23:50.5260596Z   CC [M]  sound/soc/codecs/mt6357-accdet.o
2026-05-03T01:23:50.5340254Z   AR      drivers/block/zram/built-in.a
2026-05-03T01:23:50.5433128Z   CC      drivers/block/brd.o
2026-05-03T01:23:51.0830889Z ../sound/soc/codecs/mt6357-accdet.c:619:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:51.0869954Z         int ret = 0;
2026-05-03T01:23:51.0889886Z             ^
2026-05-03T01:23:51.0890625Z ../sound/soc/codecs/mt6357-accdet.c:702:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:51.0891743Z         int ret = 0;
2026-05-03T01:23:51.0892036Z             ^
2026-05-03T01:23:51.0930355Z ../sound/soc/codecs/mt6357-accdet.c:1496:22: warning: variable 'acc_sts' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:51.0949935Z         u32 irq_status = 0, acc_sts = 0, eint_sts = 0;
2026-05-03T01:23:51.0950394Z                             ^
2026-05-03T01:23:51.0951120Z ../sound/soc/codecs/mt6357-accdet.c:1496:35: warning: variable 'eint_sts' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:51.0952169Z         u32 irq_status = 0, acc_sts = 0, eint_sts = 0;
2026-05-03T01:23:51.0952599Z                                          ^
2026-05-03T01:23:51.0953356Z ../sound/soc/codecs/mt6357-accdet.c:1566:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:51.0954148Z         int ret = 0;
2026-05-03T01:23:51.0954429Z             ^
2026-05-03T01:23:51.1070345Z ../sound/soc/codecs/mt6357-accdet.c:1975:19: warning: variable 'res' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:51.1098155Z         struct resource *res;
2026-05-03T01:23:51.1098908Z                          ^
2026-05-03T01:23:51.2130541Z   CC      kernel/utsname_sysctl.o
2026-05-03T01:23:51.2220498Z   CC      drivers/block/loop.o
2026-05-03T01:23:51.3120616Z 6 warnings generated.
2026-05-03T01:23:51.4580536Z   CC      kernel/taskstats.o
2026-05-03T01:23:51.5268570Z   CC      fs/attr.o
2026-05-03T01:23:51.6510383Z   CC [M]  sound/soc/codecs/mt6359-accdet.o
2026-05-03T01:23:52.1590509Z   CC      kernel/tsacct.o
2026-05-03T01:23:52.2071340Z ../sound/soc/codecs/mt6359-accdet.c:742:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:52.2079985Z         int ret = 0;
2026-05-03T01:23:52.2099969Z             ^
2026-05-03T01:23:52.2100678Z ../sound/soc/codecs/mt6359-accdet.c:825:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:52.2101465Z         int ret = 0;
2026-05-03T01:23:52.2101799Z             ^
2026-05-03T01:23:52.2190695Z ../sound/soc/codecs/mt6359-accdet.c:2091:33: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:52.2219901Z         u32 efuseval = 0, eintvth = 0, ret = 0;
2026-05-03T01:23:52.2220345Z                                        ^
2026-05-03T01:23:52.2250363Z ../sound/soc/codecs/mt6359-accdet.c:2142:22: warning: variable 'acc_sts' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:52.2251256Z         u32 irq_status = 0, acc_sts = 0, eint_sts = 0;
2026-05-03T01:23:52.2251691Z                             ^
2026-05-03T01:23:52.2252447Z ../sound/soc/codecs/mt6359-accdet.c:2142:35: warning: variable 'eint_sts' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:52.2253309Z         u32 irq_status = 0, acc_sts = 0, eint_sts = 0;
2026-05-03T01:23:52.2253722Z                                          ^
2026-05-03T01:23:52.2254444Z ../sound/soc/codecs/mt6359-accdet.c:2185:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:52.2255195Z         int ret = 0;
2026-05-03T01:23:52.2255482Z             ^
2026-05-03T01:23:52.2310850Z ../sound/soc/codecs/mt6359-accdet.c:2981:19: warning: variable 'res' set but not used [-Wunused-but-set-variable]
2026-05-03T01:23:52.2339816Z         struct resource *res;
2026-05-03T01:23:52.2340420Z                          ^
2026-05-03T01:23:52.2700104Z   CC      fs/bad_inode.o
2026-05-03T01:23:52.4910348Z   AR      drivers/block/built-in.a
2026-05-03T01:23:52.5053784Z 7 warnings generated.
2026-05-03T01:23:52.5090146Z   AR      drivers/bus/built-in.a
2026-05-03T01:23:52.5240312Z   AR      drivers/cdrom/built-in.a
2026-05-03T01:23:52.5420400Z   AR      drivers/char/agp/built-in.a
2026-05-03T01:23:52.5597954Z   CC      drivers/char/hw_random/core.o
2026-05-03T01:23:52.6342217Z   CC      kernel/tracepoint.o
2026-05-03T01:23:52.8330413Z   CC      fs/file.o
2026-05-03T01:23:52.8429683Z   AR      sound/soc/codecs/built-in.a
2026-05-03T01:23:52.8640295Z   AR      sound/soc/davinci/built-in.a
2026-05-03T01:23:52.8790084Z   AR      sound/soc/dwc/built-in.a
2026-05-03T01:23:52.8970070Z   AR      sound/soc/fsl/built-in.a
2026-05-03T01:23:52.9120180Z   AR      sound/soc/generic/built-in.a
2026-05-03T01:23:52.9290116Z   AR      sound/soc/hisilicon/built-in.a
2026-05-03T01:23:52.9470079Z   AR      sound/soc/img/built-in.a
2026-05-03T01:23:52.9680108Z   AR      sound/soc/intel/boards/built-in.a
2026-05-03T01:23:52.9860102Z   AR      sound/soc/intel/common/built-in.a
2026-05-03T01:23:52.9980856Z   AR      sound/soc/intel/built-in.a
2026-05-03T01:23:53.0171439Z   AR      sound/soc/jz4740/built-in.a
2026-05-03T01:23:53.0364630Z   AR      sound/soc/kirkwood/built-in.a
2026-05-03T01:23:53.0900843Z   CC      sound/soc/mediatek/common/mtk-mmap-ion.o
2026-05-03T01:23:53.2020699Z   CC      drivers/char/hw_random/mtk-rng.o
2026-05-03T01:23:53.2340345Z   CC      kernel/irq_work.o
2026-05-03T01:23:53.5252599Z   CC      sound/soc/mediatek/common/mtk-afe-platform-driver.o
2026-05-03T01:23:53.5850429Z   CC      drivers/char/hw_random/mt67xx-rng.o
2026-05-03T01:23:53.8010368Z   CC      kernel/cpu_pm.o
2026-05-03T01:23:53.8184774Z   CC      fs/filesystems.o
2026-05-03T01:23:53.8870618Z   AR      drivers/char/hw_random/built-in.a
2026-05-03T01:23:53.9063258Z   CC      drivers/char/rpmb/rpmb-mtk.o
2026-05-03T01:23:54.2450969Z   CC      kernel/iomem.o
2026-05-03T01:23:54.3185673Z   CC      sound/soc/mediatek/common/mtk-afe-fe-dai.o
2026-05-03T01:23:54.6610612Z   CC      fs/namespace.o
2026-05-03T01:23:54.9170335Z   CC      kernel/rseq.o
2026-05-03T01:23:54.9376668Z   CC      drivers/char/rpmb/core.o
2026-05-03T01:23:55.2030814Z   CC      sound/soc/mediatek/common/mtk-sram-manager.o
2026-05-03T01:23:55.4780423Z   AR      drivers/char/rpmb/built-in.a
2026-05-03T01:23:55.4900151Z   CC      drivers/char/mem.o
2026-05-03T01:23:55.5730703Z   CC [M]  kernel/kheaders.o
2026-05-03T01:23:55.8380381Z   UPD     kernel/config_data.h
2026-05-03T01:23:55.8437426Z   CC      kernel/configs.o
2026-05-03T01:23:55.9840597Z   CC      fs/seq_file.o
2026-05-03T01:23:56.0240465Z   CC      sound/soc/mediatek/common/mtk-sp-pcm-ops.o
2026-05-03T01:23:56.0860528Z   CC      drivers/char/random.o
2026-05-03T01:23:56.2030623Z   AR      kernel/built-in.a
2026-05-03T01:23:56.2920257Z   AR      sound/sparc/built-in.a
2026-05-03T01:23:56.3130232Z   CC      sound/soc/mediatek/mt6768/mt6768-afe-pcm.o
2026-05-03T01:23:56.7810602Z   CC      fs/xattr.o
2026-05-03T01:23:56.8310625Z   CC      sound/soc/mediatek/common/mtk-afe-debug.o
2026-05-03T01:23:56.9470441Z   CC      sound/soc/mediatek/mt6768/mt6768-afe-clk.o
2026-05-03T01:23:57.4460471Z   CC      drivers/char/misc.o
2026-05-03T01:23:57.5350722Z   CC      sound/soc/mediatek/mt6768/mt6768-afe-gpio.o
2026-05-03T01:23:57.5820768Z   CC      sound/soc/mediatek/common/mtk-sp-spk-amp.o
2026-05-03T01:23:57.8430443Z   CC      fs/libfs.o
2026-05-03T01:23:58.1015676Z   CC      sound/soc/mediatek/mt6768/mt6768-dai-adda.o
2026-05-03T01:23:58.1070313Z   AR      drivers/char/built-in.a
2026-05-03T01:23:58.1260307Z   AR      drivers/char/ipmi/built-in.a
2026-05-03T01:23:58.1510460Z   AR      drivers/clk/actions/built-in.a
2026-05-03T01:23:58.1676166Z   AR      drivers/clk/bcm/built-in.a
2026-05-03T01:23:58.1854061Z   AR      drivers/clk/imgtec/built-in.a
2026-05-03T01:23:58.2061794Z   CC      drivers/clk/mediatek/clk-fixup-div.o
2026-05-03T01:23:58.3690431Z   CC      sound/soc/mediatek/common/mtk-usip.o
2026-05-03T01:23:58.5840394Z   CC      drivers/clk/mediatek/clk-mtk.o
2026-05-03T01:23:58.6152667Z   CC      sound/soc/mediatek/mt6768/mt6768-afe-control.o
2026-05-03T01:23:58.8370570Z   CC      fs/fs-writeback.o
2026-05-03T01:23:58.9370602Z   CC      sound/soc/mediatek/common/mtk-btcvsd.o
2026-05-03T01:23:59.1740743Z   CC      drivers/clk/mediatek/clk-pll.o
2026-05-03T01:23:59.3950500Z   CC      sound/soc/mediatek/mt6768/mt6768-dai-i2s.o
2026-05-03T01:23:59.6086267Z   AR      sound/soc/mediatek/common/built-in.a
2026-05-03T01:23:59.6560545Z   AR      firmware/built-in.a
2026-05-03T01:23:59.6730172Z   AR      sound/soc/meson/built-in.a
2026-05-03T01:23:59.6910149Z   AR      sound/spi/built-in.a
2026-05-03T01:23:59.7060073Z   AR      drivers/clk/mvebu/built-in.a
2026-05-03T01:23:59.7268674Z   CC      drivers/clocksource/timer-of.o
2026-05-03T01:23:59.7991525Z   CC      drivers/clk/mediatek/clk-gate.o
2026-05-03T01:23:59.9820493Z   CC      sound/soc/mediatek/mt6768/mt6768-dai-hw-gain.o
2026-05-03T01:24:00.1124579Z   CC      drivers/clocksource/timer-probe.o
2026-05-03T01:24:00.3890431Z   CC      drivers/clk/mediatek/clk-apmixed.o
2026-05-03T01:24:00.4390435Z   CC      drivers/clocksource/mmio.o
2026-05-03T01:24:00.4483411Z   CC      fs/pnode.o
2026-05-03T01:24:00.4720537Z   CC      sound/soc/mediatek/mt6768/mt6768-dai-pcm.o
2026-05-03T01:24:00.7500528Z   CC      drivers/clk/mediatek/clk-cpumux.o
2026-05-03T01:24:00.7780924Z   CC      drivers/clocksource/timer-mediatek.o
2026-05-03T01:24:00.9280339Z   CC      fs/splice.o
2026-05-03T01:24:01.0150651Z   CC      sound/soc/mediatek/mt6768/mt6768-dai-hostless.o
2026-05-03T01:24:01.1130591Z   CC      drivers/clk/mediatek/reset.o
2026-05-03T01:24:01.1530596Z   CC      drivers/clocksource/arm_arch_timer.o
2026-05-03T01:24:01.4960537Z   CC      drivers/clk/mediatek/clk-mux.o
2026-05-03T01:24:01.5488681Z   CC      sound/soc/mediatek/mt6768/mt6768-misc-control.o
2026-05-03T01:24:01.9600364Z   CC      drivers/clocksource/dummy_timer.o
2026-05-03T01:24:02.0680533Z   CC      drivers/clk/mediatek/clkchk.o
2026-05-03T01:24:02.1840671Z   CC      sound/soc/mediatek/mt6768/mt6768-mt6358.o
2026-05-03T01:24:02.1944332Z   CC      fs/sync.o
2026-05-03T01:24:02.2730470Z   AR      drivers/clocksource/built-in.a
2026-05-03T01:24:02.3210491Z   CC      net/802/p8022.o
2026-05-03T01:24:02.4510582Z   CC      drivers/clk/mediatek/clk-mt6768.o
2026-05-03T01:24:02.7820520Z   AR      sound/soc/mediatek/mt6768/built-in.a
2026-05-03T01:24:02.8000201Z   AR      sound/soc/mediatek/built-in.a
2026-05-03T01:24:02.8110965Z ../drivers/clk/mediatek/clk-mt6768.c:3054:31: warning: variable 'clk26cali_1' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:02.8130076Z         unsigned int clk_misc_cfg_0, clk26cali_1;
2026-05-03T01:24:02.8165922Z                                      ^
2026-05-03T01:24:02.8198107Z ../drivers/clk/mediatek/clk-mt6768.c:3053:21: warning: variable 'clk26cali_0' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:02.8239990Z         unsigned int temp, clk26cali_0, clk_dbg_cfg;
2026-05-03T01:24:02.8250350Z                            ^
2026-05-03T01:24:02.8290411Z ../drivers/clk/mediatek/clk-mt6768.c:3097:21: warning: variable 'clk26cali_0' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:02.8327284Z         unsigned int temp, clk26cali_0, clk_dbg_cfg;
2026-05-03T01:24:02.8358904Z                            ^
2026-05-03T01:24:02.8390377Z ../drivers/clk/mediatek/clk-mt6768.c:3098:31: warning: variable 'clk26cali_1' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:02.8399944Z         unsigned int clk_misc_cfg_0, clk26cali_1;
2026-05-03T01:24:02.8429879Z                                      ^
2026-05-03T01:24:02.8430353Z   AR      sound/soc/mxs/built-in.a
2026-05-03T01:24:02.8470674Z   AR      sound/soc/nuc900/built-in.a
2026-05-03T01:24:02.8547568Z   AR      sound/soc/omap/built-in.a
2026-05-03T01:24:02.8730421Z   AR      sound/soc/pxa/built-in.a
2026-05-03T01:24:02.8900441Z   AR      sound/soc/qcom/built-in.a
2026-05-03T01:24:02.8930257Z 4 warnings generated.
2026-05-03T01:24:02.9040531Z   AR      sound/soc/rockchip/built-in.a
2026-05-03T01:24:02.9208424Z   AR      sound/soc/samsung/built-in.a
2026-05-03T01:24:02.9250420Z   CC      drivers/clk/mediatek/clk-mtk-v1.o
2026-05-03T01:24:02.9450347Z   AR      sound/soc/sh/built-in.a
2026-05-03T01:24:02.9623636Z   AR      sound/soc/sirf/built-in.a
2026-05-03T01:24:02.9745264Z   AR      sound/soc/spear/built-in.a
2026-05-03T01:24:02.9889119Z   AR      sound/soc/sti/built-in.a
2026-05-03T01:24:03.0060191Z   AR      sound/soc/stm/built-in.a
2026-05-03T01:24:03.0210101Z   AR      sound/soc/sunxi/built-in.a
2026-05-03T01:24:03.0354527Z   AR      sound/soc/tegra/built-in.a
2026-05-03T01:24:03.0520095Z   AR      sound/soc/txx9/built-in.a
2026-05-03T01:24:03.0665781Z   AR      sound/soc/uniphier/built-in.a
2026-05-03T01:24:03.0819953Z   AR      sound/soc/ux500/built-in.a
2026-05-03T01:24:03.0980205Z   AR      sound/soc/xtensa/built-in.a
2026-05-03T01:24:03.1120135Z   AR      sound/soc/zte/built-in.a
2026-05-03T01:24:03.1209993Z   CC      sound/soc/soc-core.o
2026-05-03T01:24:03.1733310Z   CC      fs/utimes.o
2026-05-03T01:24:03.2201357Z   CC      drivers/clk/mediatek/clk-mt6768-pg.o
2026-05-03T01:24:03.2551192Z   CC      net/802/psnap.o
2026-05-03T01:24:03.6141072Z ../drivers/clk/mediatek/clk-mt6768-pg.c:3670:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:03.6159940Z         int ret = 0;
2026-05-03T01:24:03.6160266Z             ^
2026-05-03T01:24:03.8270533Z 1 warning generated.
2026-05-03T01:24:03.8338309Z   CC      fs/d_path.o
2026-05-03T01:24:03.8590509Z   CC      drivers/clk/mediatek/clkdbg.o
2026-05-03T01:24:04.2071005Z ../drivers/clk/mediatek/clkdbg.c:698:8: warning: variable 'ign' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:04.2089887Z         char *ign;
2026-05-03T01:24:04.2129898Z               ^
2026-05-03T01:24:04.2140448Z ../drivers/clk/mediatek/clkdbg.c:754:8: warning: variable 'ign' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:04.2169922Z         char *ign;
2026-05-03T01:24:04.2189975Z               ^
2026-05-03T01:24:04.2200377Z ../drivers/clk/mediatek/clkdbg.c:856:8: warning: variable 'ign' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:04.2201199Z         char *ign;
2026-05-03T01:24:04.2201496Z               ^
2026-05-03T01:24:04.2202145Z ../drivers/clk/mediatek/clkdbg.c:888:8: warning: variable 'ign' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:04.2202886Z         char *ign;
2026-05-03T01:24:04.2203159Z               ^
2026-05-03T01:24:04.2203795Z ../drivers/clk/mediatek/clkdbg.c:937:8: warning: variable 'ign' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:04.2204555Z         char *ign;
2026-05-03T01:24:04.2204831Z               ^
2026-05-03T01:24:04.2205458Z ../drivers/clk/mediatek/clkdbg.c:1126:8: warning: variable 'ign' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:04.2206165Z         char *ign;
2026-05-03T01:24:04.2206436Z               ^
2026-05-03T01:24:04.2770323Z   CC      net/802/stp.o
2026-05-03T01:24:04.4850552Z 6 warnings generated.
2026-05-03T01:24:04.7245573Z   CC      fs/stack.o
2026-05-03T01:24:04.7787949Z   AR      drivers/clk/mediatek/built-in.a
2026-05-03T01:24:04.8030096Z   AR      drivers/clk/renesas/built-in.a
2026-05-03T01:24:04.8200200Z   AR      drivers/clk/ti/built-in.a
2026-05-03T01:24:04.8300134Z   CC      drivers/clk/clk-devres.o
2026-05-03T01:24:04.8710492Z   CC      sound/soc/soc-dapm.o
2026-05-03T01:24:05.1866309Z   CC      fs/fs_struct.o
2026-05-03T01:24:05.1997752Z   AR      net/802/built-in.a
2026-05-03T01:24:05.2210326Z   CC      net/8021q/vlan_core.o
2026-05-03T01:24:05.3050109Z   CC      drivers/clk/clk-bulk.o
2026-05-03T01:24:05.7560365Z   CC      fs/statfs.o
2026-05-03T01:24:05.7620219Z   CC      drivers/clk/clkdev.o
2026-05-03T01:24:06.2860965Z   CC      net/8021q/vlan.o
2026-05-03T01:24:06.3240213Z   CC      drivers/clk/clk.o
2026-05-03T01:24:06.3670666Z   CC      sound/soc/soc-jack.o
2026-05-03T01:24:06.6493864Z   CC      fs/fs_pin.o
2026-05-03T01:24:06.9720879Z ../drivers/clk/clk.c:641:24: warning: variable 'ignore' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:06.9769953Z         int level, rc = 0, i, ignore;
2026-05-03T01:24:06.9779992Z                               ^
2026-05-03T01:24:07.0410424Z   CC      net/8021q/vlan_dev.o
2026-05-03T01:24:07.0467840Z   CC      fs/nsfs.o
2026-05-03T01:24:07.3890912Z   CC      sound/soc/soc-utils.o
2026-05-03T01:24:07.6550986Z   CC      fs/buffer.o
2026-05-03T01:24:07.7420771Z 1 warning generated.
2026-05-03T01:24:07.9760527Z   CC      net/8021q/vlan_netlink.o
2026-05-03T01:24:08.1280528Z   CC      drivers/clk/clk-divider.o
2026-05-03T01:24:08.1550268Z   CC      sound/soc/soc-pcm.o
2026-05-03T01:24:08.7212912Z   CC      net/8021q/vlanproc.o
2026-05-03T01:24:08.7618801Z   CC      drivers/clk/clk-fixed-factor.o
2026-05-03T01:24:09.3560490Z   CC      drivers/clk/clk-fixed-rate.o
2026-05-03T01:24:09.3697332Z   CC      fs/block_dev.o
2026-05-03T01:24:09.3973458Z   AR      net/8021q/built-in.a
2026-05-03T01:24:09.4170410Z   CC      net/bpf/test_run.o
2026-05-03T01:24:09.4620414Z   CC      sound/soc/soc-io.o
2026-05-03T01:24:09.9350529Z   CC      drivers/clk/clk-gate.o
2026-05-03T01:24:10.1820714Z   AR      net/bpf/built-in.a
2026-05-03T01:24:10.2080496Z   AR      net/bridge/netfilter/built-in.a
2026-05-03T01:24:10.2200217Z   CC      net/bridge/br.o
2026-05-03T01:24:10.2840465Z   CC      sound/soc/soc-devres.o
2026-05-03T01:24:10.4460387Z   CC      drivers/clk/clk-multiplier.o
2026-05-03T01:24:10.5540402Z   CC      fs/direct-io.o
2026-05-03T01:24:10.9344471Z   CC      drivers/clk/clk-mux.o
2026-05-03T01:24:11.1050241Z   CC      net/bridge/br_device.o
2026-05-03T01:24:11.1083930Z   CC      sound/soc/soc-ops.o
2026-05-03T01:24:11.4750399Z   CC      drivers/clk/clk-composite.o
2026-05-03T01:24:11.7910050Z   CC      drivers/clk/clk-fractional-divider.o
2026-05-03T01:24:11.8610602Z   CC      fs/mpage.o
2026-05-03T01:24:12.0520594Z   AR      sound/soc/built-in.a
2026-05-03T01:24:12.0910614Z   AR      sound/synth/emux/built-in.a
2026-05-03T01:24:12.1025617Z   AR      sound/synth/built-in.a
2026-05-03T01:24:12.1248876Z   AR      sound/usb/6fire/built-in.a
2026-05-03T01:24:12.1411115Z   AR      sound/usb/bcd2000/built-in.a
2026-05-03T01:24:12.1579827Z   AR      sound/usb/caiaq/built-in.a
2026-05-03T01:24:12.1740335Z   AR      sound/usb/hiface/built-in.a
2026-05-03T01:24:12.1940062Z   AR      sound/usb/misc/built-in.a
2026-05-03T01:24:12.2218159Z   AR      sound/usb/usx2y/built-in.a
2026-05-03T01:24:12.2303107Z   CC      sound/usb/card.o
2026-05-03T01:24:12.3270673Z   CC      drivers/clk/clk-gpio.o
2026-05-03T01:24:12.4144481Z   CC      net/bridge/br_fdb.o
2026-05-03T01:24:12.8470574Z   CC      drivers/clk/clk-conf.o
2026-05-03T01:24:13.0680457Z   CC      fs/proc_namespace.o
2026-05-03T01:24:13.2020481Z   CC      sound/usb/clock.o
2026-05-03T01:24:13.3204574Z   CC      drivers/clk/clk-xgene.o
2026-05-03T01:24:13.5150438Z   CC      fs/eventpoll.o
2026-05-03T01:24:13.7466742Z   AR      drivers/clk/built-in.a
2026-05-03T01:24:13.7580040Z   CC      sound/usb/endpoint.o
2026-05-03T01:24:13.7850293Z   CC      drivers/cpufreq/cpufreq.o
2026-05-03T01:24:14.1670801Z   CC      net/bridge/br_forward.o
2026-05-03T01:24:14.3830602Z   CC      sound/usb/format.o
2026-05-03T01:24:14.7082527Z   CC      fs/anon_inodes.o
2026-05-03T01:24:14.9980510Z   CC      sound/usb/helper.o
2026-05-03T01:24:15.1780400Z   CC      drivers/cpufreq/freq_table.o
2026-05-03T01:24:15.2260659Z   CC      fs/signalfd.o
2026-05-03T01:24:15.5407706Z   CC      net/bridge/br_if.o
2026-05-03T01:24:15.6059654Z   CC      sound/usb/mixer.o
2026-05-03T01:24:15.6290515Z   CC      drivers/cpufreq/cpufreq_stats.o
2026-05-03T01:24:15.8290332Z   CC      fs/timerfd.o
2026-05-03T01:24:16.0340457Z   CC      drivers/cpufreq/cpufreq_times.o
2026-05-03T01:24:16.0375091Z ../sound/usb/mixer.c:1902:28: warning: variable 'first_ch_bits' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:16.0420127Z         unsigned int master_bits, first_ch_bits;
2026-05-03T01:24:16.0449956Z                                   ^
2026-05-03T01:24:16.4950532Z   CC      fs/eventfd.o
2026-05-03T01:24:16.5250307Z 1 warning generated.
2026-05-03T01:24:16.5590572Z   CC      sound/usb/mixer_quirks.o
2026-05-03T01:24:16.5770618Z   CC      net/bridge/br_input.o
2026-05-03T01:24:16.7030666Z   CC      drivers/cpufreq/cpufreq_performance.o
2026-05-03T01:24:17.0230564Z   CC      drivers/cpufreq/cpufreq_powersave.o
2026-05-03T01:24:17.2190514Z   CC      sound/usb/mixer_scarlett.o
2026-05-03T01:24:17.3440557Z   CC      drivers/cpufreq/cpufreq_userspace.o
2026-05-03T01:24:17.4120570Z   CC      fs/aio.o
2026-05-03T01:24:17.6480651Z   CC      drivers/cpufreq/cpufreq_ondemand.o
2026-05-03T01:24:17.6990677Z   CC      sound/usb/mixer_us16x08.o
2026-05-03T01:24:17.9410645Z   CC      net/bridge/br_ioctl.o
2026-05-03T01:24:18.2440502Z   CC      sound/usb/pcm.o
2026-05-03T01:24:18.2630562Z   CC      drivers/cpufreq/cpufreq_governor.o
2026-05-03T01:24:18.8790603Z   CC      drivers/cpufreq/cpufreq_governor_attr_set.o
2026-05-03T01:24:18.8850328Z   CC      net/bridge/br_stp.o
2026-05-03T01:24:19.0140560Z   CC      fs/locks.o
2026-05-03T01:24:19.2731072Z   CC      sound/usb/power.o
2026-05-03T01:24:19.4320935Z   AR      drivers/cpufreq/built-in.a
2026-05-03T01:24:19.4690536Z   CC      drivers/cpuidle/governors/menu.o
2026-05-03T01:24:19.7178193Z   CC      sound/usb/proc.o
2026-05-03T01:24:19.8179984Z   CC      net/bridge/br_stp_bpdu.o
2026-05-03T01:24:19.8431412Z   CC      drivers/cpuidle/governors/mtk_menu.o
2026-05-03T01:24:20.2140604Z   CC      sound/usb/quirks.o
2026-05-03T01:24:20.4430594Z   AR      drivers/cpuidle/governors/built-in.a
2026-05-03T01:24:20.4530113Z   CC      drivers/cpuidle/cpuidle.o
2026-05-03T01:24:20.4590087Z   CC      fs/compat.o
2026-05-03T01:24:20.7608007Z   CC      net/bridge/br_stp_if.o
2026-05-03T01:24:20.8050624Z   CC      sound/usb/stream.o
2026-05-03T01:24:21.0180413Z   CC      fs/compat_ioctl.o
2026-05-03T01:24:21.5139292Z   CC      sound/usb/validate.o
2026-05-03T01:24:21.5560556Z   CC      drivers/cpuidle/driver.o
2026-05-03T01:24:21.6870528Z   CC      net/bridge/br_stp_timer.o
2026-05-03T01:24:21.9280538Z   CC      sound/usb/midi.o
2026-05-03T01:24:22.1250360Z   CC      drivers/cpuidle/governor.o
2026-05-03T01:24:22.5151294Z   CC      fs/binfmt_script.o
2026-05-03T01:24:22.6040868Z   CC      drivers/cpuidle/sysfs.o
2026-05-03T01:24:22.6090216Z   CC      net/bridge/br_netlink.o
2026-05-03T01:24:22.8840535Z   CC      fs/binfmt_elf.o
2026-05-03T01:24:22.9310374Z   AR      sound/usb/built-in.a
2026-05-03T01:24:22.9535451Z   AR      sound/x86/built-in.a
2026-05-03T01:24:22.9750374Z   AR      sound/xen/built-in.a
2026-05-03T01:24:22.9763141Z   CC      drivers/cpuidle/dt_idle_states.o
2026-05-03T01:24:22.9836947Z   CC      sound/sound_core.o
2026-05-03T01:24:23.4620591Z   CC      sound/last.o
2026-05-03T01:24:23.4950577Z   CC      drivers/cpuidle/cpuidle-mtk_acao.o
2026-05-03T01:24:23.5600596Z   CC      net/bridge/br_netlink_tunnel.o
2026-05-03T01:24:23.7389085Z   CC      fs/compat_binfmt_elf.o
2026-05-03T01:24:23.7770432Z   AR      sound/built-in.a
2026-05-03T01:24:23.8040418Z   AR      drivers/cpuidle/built-in.a
2026-05-03T01:24:23.8070097Z   AR      drivers/crypto/hisilicon/built-in.a
2026-05-03T01:24:23.8160086Z   CC      fs/mbcache.o
2026-05-03T01:24:23.8199850Z   AR      drivers/crypto/built-in.a
2026-05-03T01:24:23.8346586Z   CC      drivers/devfreq/devfreq.o
2026-05-03T01:24:24.4790546Z   CC      net/bridge/br_arp_nd_proxy.o
2026-05-03T01:24:24.4850287Z   CC      drivers/devfreq/helio-dvfsrc-ipi.o
2026-05-03T01:24:24.5610563Z   CC      arch/arm64/lib/atomic_ll_sc.o
2026-05-03T01:24:24.6380360Z   CC      fs/posix_acl.o
2026-05-03T01:24:24.7480655Z ../drivers/devfreq/helio-dvfsrc-ipi.c:42:22: warning: variable 'qos_task' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:24.7505365Z         struct task_struct *qos_task;
2026-05-03T01:24:24.7505965Z                             ^
2026-05-03T01:24:24.7530211Z   AS      arch/arm64/lib/clear_page.o
2026-05-03T01:24:24.7581202Z 1 warning generated.
2026-05-03T01:24:24.7847929Z   CC      drivers/devfreq/helio-dvfsrc-v2/helio-dvfsrc.o
2026-05-03T01:24:24.8050487Z   AS      arch/arm64/lib/clear_user.o
2026-05-03T01:24:24.8560435Z   AS      arch/arm64/lib/copy_from_user.o
2026-05-03T01:24:24.9070418Z   AS      arch/arm64/lib/copy_in_user.o
2026-05-03T01:24:24.9600444Z   AS      arch/arm64/lib/copy_page.o
2026-05-03T01:24:25.0090437Z   AS      arch/arm64/lib/copy_to_user.o
2026-05-03T01:24:25.0630385Z   CC      arch/arm64/lib/delay.o
2026-05-03T01:24:25.2861233Z   CC      drivers/devfreq/helio-dvfsrc-v2/helio-dvfsrc-mt6768.o
2026-05-03T01:24:25.2980376Z   CC      fs/coredump.o
2026-05-03T01:24:25.3475064Z   CC      net/bridge/br_sysfs_if.o
2026-05-03T01:24:25.5000375Z   AS      arch/arm64/lib/memchr.o
2026-05-03T01:24:25.5484565Z   AS      arch/arm64/lib/memcmp.o
2026-05-03T01:24:25.5970752Z   AS      arch/arm64/lib/memcpy.o
2026-05-03T01:24:25.6470413Z   AS      arch/arm64/lib/memmove.o
2026-05-03T01:24:25.6920390Z   AS      arch/arm64/lib/memset.o
2026-05-03T01:24:25.7400425Z   AS      arch/arm64/lib/strchr.o
2026-05-03T01:24:25.7880378Z   AS      arch/arm64/lib/strcmp.o
2026-05-03T01:24:25.8360243Z   AS      arch/arm64/lib/strlen.o
2026-05-03T01:24:25.8860948Z   AS      arch/arm64/lib/strncmp.o
2026-05-03T01:24:25.9350410Z   AS      arch/arm64/lib/strnlen.o
2026-05-03T01:24:25.9850366Z   AS      arch/arm64/lib/strrchr.o
2026-05-03T01:24:26.0300346Z   AS      arch/arm64/lib/tishift.o
2026-05-03T01:24:26.0720373Z   AR      arch/arm64/lib/lib.a
2026-05-03T01:24:26.0930388Z   EXPORTS arch/arm64/lib/lib-ksyms.o
2026-05-03T01:24:26.1698053Z   CC      drivers/devfreq/helio-dvfsrc-v2/helio-dvfsrc-opp-mt6768.o
2026-05-03T01:24:26.1714677Z   CC      net/bridge/br_sysfs_br.o
2026-05-03T01:24:26.3100692Z   AR      arch/arm64/lib/built-in.a
2026-05-03T01:24:26.3320060Z   CC      net/core/sock.o
2026-05-03T01:24:26.5914649Z   CC      fs/drop_caches.o
2026-05-03T01:24:26.6720766Z   CC      drivers/devfreq/helio-dvfsrc-v2/helio-dvfsrc-opp.o
2026-05-03T01:24:27.0440736Z   CC      drivers/devfreq/helio-dvfsrc-v2/helio-dvfsrc-sysfs.o
2026-05-03T01:24:27.0460095Z   CC      fs/iomap.o
2026-05-03T01:24:27.1750562Z   CC      net/bridge/br_nf_core.o
2026-05-03T01:24:27.4470582Z   AR      drivers/devfreq/built-in.a
2026-05-03T01:24:27.4750307Z   CC      drivers/dma/mediatek/mtk-uart-apdma.o
2026-05-03T01:24:28.0550672Z   CC      net/bridge/br_multicast.o
2026-05-03T01:24:28.1200336Z   AR      drivers/dma/mediatek/built-in.a
2026-05-03T01:24:28.1350197Z   AR      drivers/dma/qcom/built-in.a
2026-05-03T01:24:28.1500195Z   AR      drivers/dma/ti/built-in.a
2026-05-03T01:24:28.1680220Z   AR      drivers/dma/xilinx/built-in.a
2026-05-03T01:24:28.1770126Z   CC      drivers/dma/dmaengine.o
2026-05-03T01:24:28.3393868Z   CC      net/core/request_sock.o
2026-05-03T01:24:28.3590338Z   CC      fs/dcookies.o
2026-05-03T01:24:29.1430372Z   CC      drivers/dma/virt-dma.o
2026-05-03T01:24:29.1860530Z   CC      net/core/skbuff.o
2026-05-03T01:24:29.2470351Z   AR      fs/built-in.a
2026-05-03T01:24:29.3520219Z   CC      net/ethernet/eth.o
2026-05-03T01:24:29.8750448Z   CC      drivers/dma/of-dma.o
2026-05-03T01:24:29.8980363Z   CC      net/bridge/br_mdb.o
2026-05-03T01:24:30.6413291Z   AR      drivers/dma/built-in.a
2026-05-03T01:24:30.6650623Z   CC      drivers/dma-buf/dma-buf.o
2026-05-03T01:24:30.7090558Z   AR      net/ethernet/built-in.a
2026-05-03T01:24:30.7420461Z   CC      net/ipv4/netfilter/nf_nat_l3proto_ipv4.o
2026-05-03T01:24:30.8540580Z   CC      net/bridge/br_netfilter_hooks.o
2026-05-03T01:24:31.5040566Z   CC      net/core/datagram.o
2026-05-03T01:24:31.5320390Z   CC      drivers/dma-buf/dma-fence.o
2026-05-03T01:24:31.8570500Z   CC      net/bridge/br_netfilter_ipv6.o
2026-05-03T01:24:32.1230561Z   CC      net/ipv4/netfilter/nf_nat_proto_icmp.o
2026-05-03T01:24:32.4850321Z   CC      drivers/dma-buf/dma-fence-array.o
2026-05-03T01:24:32.8500294Z   AR      net/bridge/built-in.a
2026-05-03T01:24:32.8740289Z   AR      drivers/energy_model/built-in.a
2026-05-03T01:24:32.8790458Z   CC      drivers/dma-buf/reservation.o
2026-05-03T01:24:32.9269151Z   CC      net/core/stream.o
2026-05-03T01:24:32.9748459Z   CC      lib/crypto/chacha.o
2026-05-03T01:24:33.0300716Z   CC      net/ipv4/netfilter/nf_nat_masquerade_ipv4.o
2026-05-03T01:24:33.1700405Z   CC      lib/crypto/libchacha.o
2026-05-03T01:24:33.4180446Z   CC      drivers/dma-buf/seqno-fence.o
2026-05-03T01:24:33.9302318Z   CC      lib/crypto/poly1305-donna64.o
2026-05-03T01:24:34.0850285Z   CC      drivers/dma-buf/sync_file.o
2026-05-03T01:24:34.1890429Z   CC      net/core/scm.o
2026-05-03T01:24:34.3300494Z   CC      net/ipv4/netfilter/nf_defrag_ipv4.o
2026-05-03T01:24:34.3900413Z   CC      lib/crypto/poly1305.o
2026-05-03T01:24:34.7770679Z   AR      drivers/dma-buf/built-in.a
2026-05-03T01:24:34.8040450Z   CC      drivers/extcon/extcon.o
2026-05-03T01:24:34.8570427Z   AR      lib/crypto/built-in.a
2026-05-03T01:24:34.8830213Z   CC      lib/fonts/fonts.o
2026-05-03T01:24:35.3322562Z   CC      lib/fonts/font_8x16.o
2026-05-03T01:24:35.5090452Z   CC      net/core/gen_stats.o
2026-05-03T01:24:35.6088768Z   CC      drivers/extcon/devres.o
2026-05-03T01:24:35.6270753Z   CC      net/ipv4/netfilter/nf_socket_ipv4.o
2026-05-03T01:24:35.7640850Z   AR      lib/fonts/built-in.a
2026-05-03T01:24:35.7860190Z   CC      lib/lz4/lz4_compress.o
2026-05-03T01:24:36.0370401Z   AR      drivers/extcon/built-in.a
2026-05-03T01:24:36.0550224Z   AR      drivers/firewire/built-in.a
2026-05-03T01:24:36.0970456Z   AR      drivers/firmware/broadcom/built-in.a
2026-05-03T01:24:36.1136044Z   AR      drivers/firmware/meson/built-in.a
2026-05-03T01:24:36.1330225Z   AR      drivers/firmware/tegra/built-in.a
2026-05-03T01:24:36.1420155Z   CC      drivers/firmware/psci.o
2026-05-03T01:24:36.4190507Z   CC      lib/lz4/lz4_decompress.o
2026-05-03T01:24:36.5369656Z   CC      net/core/gen_estimator.o
2026-05-03T01:24:36.7880560Z   AR      drivers/firmware/built-in.a
2026-05-03T01:24:36.8059809Z   CC      drivers/gpio/devres.o
2026-05-03T01:24:37.0120268Z   AR      lib/lz4/built-in.a
2026-05-03T01:24:37.0331165Z   CC      lib/lzo/lzo1x_compress.o
2026-05-03T01:24:37.0620536Z   CC      net/ipv4/netfilter/nf_tproxy_ipv4.o
2026-05-03T01:24:37.4610677Z   CC      drivers/gpio/gpiolib.o
2026-05-03T01:24:37.5120385Z   CC      lib/lzo/lzo1x_decompress_safe.o
2026-05-03T01:24:37.7200546Z   CC      net/core/net_namespace.o
2026-05-03T01:24:37.9470534Z   AR      lib/lzo/built-in.a
2026-05-03T01:24:37.9720673Z   CC      lib/mpi/generic_mpih-lshift.o
2026-05-03T01:24:38.4081228Z   CC      net/ipv4/netfilter/nf_reject_ipv4.o
2026-05-03T01:24:38.4350607Z   CC      lib/mpi/generic_mpih-mul1.o
2026-05-03T01:24:38.8274570Z   CC      lib/mpi/generic_mpih-mul2.o
2026-05-03T01:24:38.9680396Z   CC      drivers/gpio/gpiolib-legacy.o
2026-05-03T01:24:39.1190714Z   CC      net/core/secure_seq.o
2026-05-03T01:24:39.2342771Z   CC      lib/mpi/generic_mpih-mul3.o
2026-05-03T01:24:39.6170432Z   CC      drivers/gpio/gpiolib-devprop.o
2026-05-03T01:24:39.6586919Z   CC      lib/mpi/generic_mpih-rshift.o
2026-05-03T01:24:39.6840872Z   CC      net/ipv4/netfilter/nf_nat_h323.o
2026-05-03T01:24:40.0844927Z   CC      lib/mpi/generic_mpih-sub1.o
2026-05-03T01:24:40.1016413Z   CC      drivers/gpio/gpiolib-of.o
2026-05-03T01:24:40.4180278Z   CC      net/core/flow_dissector.o
2026-05-03T01:24:40.5040671Z   CC      lib/mpi/generic_mpih-add1.o
2026-05-03T01:24:40.7470571Z   CC      net/ipv4/netfilter/nf_nat_pptp.o
2026-05-03T01:24:40.8060451Z   AR      drivers/gpio/built-in.a
2026-05-03T01:24:40.8414818Z   AR      drivers/gpu/drm/amd/lib/built-in.a
2026-05-03T01:24:40.8642301Z   AR      drivers/gpu/drm/bridge/synopsys/built-in.a
2026-05-03T01:24:40.8790098Z   AR      drivers/gpu/drm/bridge/built-in.a
2026-05-03T01:24:40.8963385Z   AR      drivers/gpu/drm/hisilicon/built-in.a
2026-05-03T01:24:40.9140385Z   AR      drivers/gpu/drm/i2c/built-in.a
2026-05-03T01:24:40.9361120Z   AR      drivers/gpu/drm/omapdrm/displays/built-in.a
2026-05-03T01:24:40.9410364Z   CC      lib/mpi/mpicoder.o
2026-05-03T01:24:40.9533999Z   AR      drivers/gpu/drm/omapdrm/dss/built-in.a
2026-05-03T01:24:40.9680231Z   AR      drivers/gpu/drm/omapdrm/built-in.a
2026-05-03T01:24:40.9845302Z   AR      drivers/gpu/drm/panel/built-in.a
2026-05-03T01:24:41.0017795Z   AR      drivers/gpu/drm/tilcdc/built-in.a
2026-05-03T01:24:41.0250173Z   AR      drivers/gpu/drm/built-in.a
2026-05-03T01:24:41.0377952Z $GED: CONFIG_MTK_PLATFORM is ["mt6768"]
2026-05-03T01:24:41.0520112Z   CC      drivers/gpu/mediatek/ged/src/ged.o
2026-05-03T01:24:41.5100578Z   CC      drivers/gpu/mediatek/ged/src/ged_base.o
2026-05-03T01:24:41.6800518Z   CC      net/ipv4/netfilter/nf_nat_proto_gre.o
2026-05-03T01:24:41.6870124Z   CC      lib/mpi/mpi-bit.o
2026-05-03T01:24:41.8248158Z   CC      drivers/gpu/mediatek/ged/src/ged_main.o
2026-05-03T01:24:41.8441261Z   CC      net/core/sysctl_net_core.o
2026-05-03T01:24:42.3146402Z   CC      lib/mpi/mpi-cmp.o
2026-05-03T01:24:42.4120753Z   CC      drivers/gpu/mediatek/ged/src/ged_sysfs.o
2026-05-03T01:24:42.6831639Z   CC      drivers/gpu/mediatek/ged/src/ged_hal.o
2026-05-03T01:24:42.9651930Z   CC      lib/mpi/mpih-cmp.o
2026-05-03T01:24:43.0167132Z   CC      net/ipv4/netfilter/ip_tables.o
2026-05-03T01:24:43.1431197Z ../drivers/gpu/mediatek/ged/src/ged_hal.c:212:9: warning: unused variable 'j' [-Wunused-variable]
2026-05-03T01:24:43.1459930Z         int i, j;
2026-05-03T01:24:43.1489873Z                ^
2026-05-03T01:24:43.1997281Z   CC      net/core/dev.o
2026-05-03T01:24:43.2190265Z 1 warning generated.
2026-05-03T01:24:43.2520559Z   CC      drivers/gpu/mediatek/ged/src/ged_log.o
2026-05-03T01:24:43.3590204Z   CC      lib/mpi/mpih-div.o
2026-05-03T01:24:43.8241045Z ../drivers/gpu/mediatek/ged/src/ged_log.c:845:12: warning: variable 'err' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:43.8269949Z         GED_ERROR err;
2026-05-03T01:24:43.8272154Z                   ^
2026-05-03T01:24:43.8273317Z ../drivers/gpu/mediatek/ged/src/ged_log.c:863:12: warning: variable 'err' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:43.8274319Z         GED_ERROR err;
2026-05-03T01:24:43.8274758Z                   ^
2026-05-03T01:24:43.8460546Z   CC      lib/mpi/mpih-mul.o
2026-05-03T01:24:43.9130356Z 2 warnings generated.
2026-05-03T01:24:44.2310538Z   CC      drivers/gpu/mediatek/ged/src/ged_bridge.o
2026-05-03T01:24:44.3530586Z   CC      lib/mpi/mpi-pow.o
2026-05-03T01:24:44.6160689Z   CC      drivers/gpu/mediatek/ged/src/ged_monitor_3D_fence.o
2026-05-03T01:24:44.7103667Z   CC      net/ipv4/netfilter/iptable_filter.o
2026-05-03T01:24:44.9170793Z   CC      drivers/gpu/mediatek/ged/src/ged_notify_sw_vsync.o
2026-05-03T01:24:45.0040336Z   CC      lib/mpi/mpiutil.o
2026-05-03T01:24:45.2290739Z   CC      drivers/gpu/mediatek/ged/src/ged_hashtable.o
2026-05-03T01:24:45.4480629Z   CC      drivers/gpu/mediatek/ged/src/ged_thread.o
2026-05-03T01:24:45.6070549Z   CC      net/ipv4/netfilter/iptable_mangle.o
2026-05-03T01:24:45.6810663Z   CC      drivers/gpu/mediatek/ged/src/ged_ge.o
2026-05-03T01:24:45.6874387Z   AR      lib/mpi/built-in.a
2026-05-03T01:24:45.7130741Z   CC      lib/reed_solomon/reed_solomon.o
2026-05-03T01:24:46.1110728Z   CC      drivers/gpu/mediatek/ged/src/ged_dvfs.o
2026-05-03T01:24:46.3150690Z   AR      lib/reed_solomon/built-in.a
2026-05-03T01:24:46.3350274Z   CC      lib/zlib_deflate/deflate.o
2026-05-03T01:24:46.3731054Z ../drivers/gpu/mediatek/ged/src/ged_dvfs.c:410:22: warning: variable 'ui32LastPredictMaxBW' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:46.3760133Z         static unsigned int ui32LastPredictMaxBW;
2026-05-03T01:24:46.3789871Z                             ^
2026-05-03T01:24:46.3790746Z ../drivers/gpu/mediatek/ged/src/ged_dvfs.c:417:11: warning: variable 'ui64AvgBW' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:46.3850112Z         uint64_t ui64AvgBW = 0;
2026-05-03T01:24:46.3876155Z                  ^
2026-05-03T01:24:46.3900655Z ../drivers/gpu/mediatek/ged/src/ged_dvfs.c:412:22: warning: variable 'ui32LastActivePredictAvgBW' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:46.3930158Z         static unsigned int ui32LastActivePredictAvgBW;
2026-05-03T01:24:46.3959801Z                             ^
2026-05-03T01:24:46.3990441Z ../drivers/gpu/mediatek/ged/src/ged_dvfs.c:411:22: warning: variable 'ui32LastPredictAvgBW' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:46.4018242Z         static unsigned int ui32LastPredictAvgBW;
2026-05-03T01:24:46.4049793Z                             ^
2026-05-03T01:24:46.4078955Z ../drivers/gpu/mediatek/ged/src/ged_dvfs.c:806:15: warning: variable 'ui32CurFreqID' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:46.4109948Z         unsigned int ui32CurFreqID;
2026-05-03T01:24:46.4139905Z                      ^
2026-05-03T01:24:46.4170485Z ../drivers/gpu/mediatek/ged/src/ged_dvfs.c:1011:8: warning: mixing declarations and code is a C99 extension [-Wdeclaration-after-statement]
2026-05-03T01:24:46.4200018Z                         int i32NewFreqID =
2026-05-03T01:24:46.4223418Z                             ^
2026-05-03T01:24:46.4260423Z ../drivers/gpu/mediatek/ged/src/ged_dvfs.c:987:13: warning: variable 'pre_frame_idx' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:46.4289959Z         static int pre_frame_idx;
2026-05-03T01:24:46.4320433Z                    ^
2026-05-03T01:24:46.4350396Z ../drivers/gpu/mediatek/ged/src/ged_dvfs.c:1920:15: warning: variable 'gpu_freq_pre' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:46.4379934Z         unsigned int gpu_freq_pre;
2026-05-03T01:24:46.4409885Z                      ^
2026-05-03T01:24:46.4439936Z   CC      net/ipv4/netfilter/iptable_nat.o
2026-05-03T01:24:46.5150467Z 8 warnings generated.
2026-05-03T01:24:46.7098783Z   CC      drivers/gpu/mediatek/ged/src/ged_gpu_tuner.o
2026-05-03T01:24:46.7240418Z   CC      lib/zlib_deflate/deftree.o
2026-05-03T01:24:46.8540428Z   CC      net/core/ethtool.o
2026-05-03T01:24:47.0493462Z   CC      lib/zlib_deflate/deflate_syms.o
2026-05-03T01:24:47.0674438Z   CC      drivers/gpu/mediatek/ged/src/ged_kpi.o
2026-05-03T01:24:47.2350599Z   CC      net/ipv4/netfilter/iptable_raw.o
2026-05-03T01:24:47.3562733Z ../drivers/gpu/mediatek/ged/src/ged_kpi.c:52:9: warning: 'GED_TAG' macro redefined [-Wmacro-redefined]
2026-05-03T01:24:47.3573583Z #define GED_TAG "[GED_KPI]"
2026-05-03T01:24:47.3599899Z         ^
2026-05-03T01:24:47.3630189Z ../drivers/gpu/mediatek/ged/include/ged_base.h:12:9: note: previous definition is here
2026-05-03T01:24:47.3659898Z #define GED_TAG "[GPU/GED]"
2026-05-03T01:24:47.3689873Z         ^
2026-05-03T01:24:47.4800393Z   AR      lib/zlib_deflate/built-in.a
2026-05-03T01:24:47.5010379Z   CC      lib/zlib_inflate/inffast.o
2026-05-03T01:24:47.5720666Z 1 warning generated.
2026-05-03T01:24:47.6590561Z   CC      lib/zlib_inflate/inflate.o
2026-05-03T01:24:47.7590742Z ../drivers/gpu/mediatek/ged/src/ged_kpi.c:52:9: warning: 'GED_TAG' macro redefined [-Wmacro-redefined]
2026-05-03T01:24:47.7619939Z #define GED_TAG "[GED_KPI]"
2026-05-03T01:24:47.7649863Z         ^
2026-05-03T01:24:47.7680194Z ../drivers/gpu/mediatek/ged/include/ged_base.h:12:9: note: previous definition is here
2026-05-03T01:24:47.7680916Z #define GED_TAG "[GPU/GED]"
2026-05-03T01:24:47.7681252Z         ^
2026-05-03T01:24:47.7681558Z 1 warning generated.
2026-05-03T01:24:47.7770057Z   AR      drivers/gpu/mediatek/ged/built-in.a
2026-05-03T01:24:47.7950158Z *MTK_GPU_VERSION 2 = valhall
2026-05-03T01:24:47.8009990Z *MTK_GPU_VERSION 3 = r32p1
2026-05-03T01:24:47.8069931Z mali MTK evironment, building r32p1 DDK
2026-05-03T01:24:47.8070492Z mtk-Kbuild CONFIG_MALI_PLATFORM_THIRDPARTY := y
2026-05-03T01:24:47.8100028Z mtk-Kbuild CONFIG_MALI_PLATFORM_THIRDPARTY_NAME := "mt6768"
2026-05-03T01:24:47.8129920Z mali MTK evironment, building r32p1 DDK
2026-05-03T01:24:47.8130458Z mtk-Kbuild CONFIG_MALI_PLATFORM_THIRDPARTY := y
2026-05-03T01:24:47.8160035Z mtk-Kbuild CONFIG_MALI_PLATFORM_THIRDPARTY_NAME := "mt6768"
2026-05-03T01:24:47.8160645Z mali MTK evironment, building r32p1 DDK
2026-05-03T01:24:47.8201032Z mtk-Kbuild CONFIG_MALI_PLATFORM_THIRDPARTY := y
2026-05-03T01:24:47.8220175Z mtk-Kbuild CONFIG_MALI_PLATFORM_THIRDPARTY_NAME := "mt6768"
2026-05-03T01:24:47.8250502Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/platform/mtk_platform_common/mtk_platform_common.o
2026-05-03T01:24:47.9600567Z   CC      lib/zlib_inflate/infutil.o
2026-05-03T01:24:48.0341687Z   CC      net/ipv4/netfilter/iptable_security.o
2026-05-03T01:24:48.2020675Z   CC      lib/zlib_inflate/inftrees.o
2026-05-03T01:24:48.3477729Z   CC      net/core/dev_addr_lists.o
2026-05-03T01:24:48.3640294Z   CC      lib/zlib_inflate/inflate_syms.o
2026-05-03T01:24:48.4521062Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/platform/mtk_platform_common/mtk_gpu_dvfs.o
2026-05-03T01:24:48.7915487Z   AR      lib/zlib_inflate/built-in.a
2026-05-03T01:24:48.8030128Z   HOSTCC  lib/gen_crc32table
2026-05-03T01:24:48.9120611Z   CC      net/ipv4/netfilter/ipt_ah.o
2026-05-03T01:24:48.9500625Z   GEN     lib/oid_registry_data.c
2026-05-03T01:24:48.9680107Z   CC      lib/lockref.o
2026-05-03T01:24:49.0381078Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/platform/mtk_platform_common/mtk_mfg_counter.o
2026-05-03T01:24:49.2350736Z   CC      lib/bcd.o
2026-05-03T01:24:49.2980401Z   CC      lib/div64.o
2026-05-03T01:24:49.3671393Z ../drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/platform/mtk_platform_common/mtk_mfg_counter.c:543:7: warning: variable 'shader_block' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:49.3698598Z                 int shader_block, block_type, i, j, name_offset, data_offset, cnt, nr_hwc_blocks;
2026-05-03T01:24:49.3730098Z                     ^
2026-05-03T01:24:49.3760749Z ../drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/platform/mtk_platform_common/mtk_mfg_counter.c:629:35: warning: variable 'data_offset' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:49.3790021Z                 int nr_hwc_blocks, name_offset, data_offset;
2026-05-03T01:24:49.3819925Z                                                 ^
2026-05-03T01:24:49.3850768Z ../drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/platform/mtk_platform_common/mtk_mfg_counter.c:776:6: warning: variable 'nr_hwc_blocks' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:49.3877074Z         int nr_hwc_blocks, name_offset, data_offset;
2026-05-03T01:24:49.3909856Z             ^
2026-05-03T01:24:49.4420385Z   CC      net/core/dst.o
2026-05-03T01:24:49.4540299Z   CC      lib/sort.o
2026-05-03T01:24:49.5278099Z   CC      lib/parser.o
2026-05-03T01:24:49.5680577Z 3 warnings generated.
2026-05-03T01:24:49.5920804Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/platform/mtk_platform_common/mtk_gpu_power_sspm_ipi.o
2026-05-03T01:24:49.6091703Z   CC      net/ipv4/netfilter/ipt_MASQUERADE.o
2026-05-03T01:24:49.9680316Z   CC      lib/debug_locks.o
2026-05-03T01:24:50.1231533Z ../drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/platform/mtk_platform_common/mtk_gpu_power_sspm_ipi.c:70:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:50.1250350Z         int ret;
2026-05-03T01:24:50.1280049Z             ^
2026-05-03T01:24:50.1580602Z 1 warning generated.
2026-05-03T01:24:50.2120524Z   CC      lib/random32.o
2026-05-03T01:24:50.4810943Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_cache_policy.o
2026-05-03T01:24:50.5360887Z   CC      net/ipv4/netfilter/ipt_REJECT.o
2026-05-03T01:24:50.6239777Z   CC      lib/bust_spinlocks.o
2026-05-03T01:24:50.8409952Z   CC      net/core/netevent.o
2026-05-03T01:24:51.0420584Z   CC      lib/kasprintf.o
2026-05-03T01:24:51.4000315Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_ccswe.o
2026-05-03T01:24:51.4120705Z   CC      lib/bitmap.o
2026-05-03T01:24:51.4210523Z   CC      net/ipv4/netfilter/arp_tables.o
2026-05-03T01:24:51.7320745Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_mem.o
2026-05-03T01:24:51.7374362Z   CC      net/core/neighbour.o
2026-05-03T01:24:52.2899866Z   CC      lib/scatterlist.o
2026-05-03T01:24:52.9910582Z   CC      net/ipv4/netfilter/arpt_mangle.o
2026-05-03T01:24:53.1410460Z   CC      lib/gcd.o
2026-05-03T01:24:53.1901068Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_mem_pool_group.o
2026-05-03T01:24:53.3303942Z   CC      lib/lcm.o
2026-05-03T01:24:53.3980421Z   CC      lib/list_sort.o
2026-05-03T01:24:53.6117752Z   CC      lib/uuid.o
2026-05-03T01:24:53.6664714Z   CC      net/core/rtnetlink.o
2026-05-03T01:24:53.7210469Z   CC      net/ipv4/netfilter/arptable_filter.o
2026-05-03T01:24:53.7640846Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_native_mgm.o
2026-05-03T01:24:53.8520442Z   CC      lib/flex_array.o
2026-05-03T01:24:54.2480402Z   CC      lib/iov_iter.o
2026-05-03T01:24:54.3391173Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_ctx_sched.o
2026-05-03T01:24:54.4280887Z   AR      net/ipv4/netfilter/built-in.a
2026-05-03T01:24:54.4510358Z   CC      net/ipv4/route.o
2026-05-03T01:24:54.9361162Z ../drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_ctx_sched.c:327:6: warning: variable 'as_nr' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:54.9370083Z         int as_nr;
2026-05-03T01:24:54.9389885Z             ^
2026-05-03T01:24:54.9750175Z 1 warning generated.
2026-05-03T01:24:55.0081448Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_gpuprops.o
2026-05-03T01:24:55.4024028Z ../net/ipv4/route.c:870:6: warning: variable 'log_martians' set but not used [-Wunused-but-set-variable]
2026-05-03T01:24:55.4065142Z         int log_martians;
2026-05-03T01:24:55.4109780Z             ^
2026-05-03T01:24:55.4710496Z   CC      lib/clz_ctz.o
2026-05-03T01:24:55.6610505Z   CC      lib/bsearch.o
2026-05-03T01:24:55.6820657Z   CC      net/core/utils.o
2026-05-03T01:24:55.8440984Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_pm.o
2026-05-03T01:24:55.9290329Z 1 warning generated.
2026-05-03T01:24:56.3540366Z   CC      lib/find_bit.o
2026-05-03T01:24:56.4618546Z   CC      net/ipv4/inetpeer.o
2026-05-03T01:24:56.5380456Z   CC      lib/llist.o
2026-05-03T01:24:56.7020542Z   CC      lib/memweight.o
2026-05-03T01:24:56.7251007Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_config.o
2026-05-03T01:24:56.8776283Z   CC      net/core/link_watch.o
2026-05-03T01:24:56.9133157Z   CC      lib/kfifo.o
2026-05-03T01:24:57.3369293Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_vinstr.o
2026-05-03T01:24:57.6370362Z   CC      net/ipv4/protocol.o
2026-05-03T01:24:57.6888659Z   CC      lib/percpu-refcount.o
2026-05-03T01:24:57.9460930Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_hwcnt.o
2026-05-03T01:24:58.0910445Z   CC      net/core/filter.o
2026-05-03T01:24:58.1030255Z   CC      lib/rhashtable.o
2026-05-03T01:24:58.2791437Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_hwcnt_gpu.o
2026-05-03T01:24:58.5205438Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_hwcnt_legacy.o
2026-05-03T01:24:58.8000527Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_hwcnt_types.o
2026-05-03T01:24:58.8390618Z   CC      net/ipv4/ip_input.o
2026-05-03T01:24:59.2020874Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_hwcnt_virtualizer.o
2026-05-03T01:24:59.2640460Z   CC      lib/reciprocal_div.o
2026-05-03T01:24:59.4590369Z   CC      lib/once.o
2026-05-03T01:24:59.5130827Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_softjobs.o
2026-05-03T01:24:59.8174041Z   CC      lib/refcount.o
2026-05-03T01:24:59.9602866Z   CC      net/ipv4/ip_fragment.o
2026-05-03T01:25:00.1070400Z   CC      lib/usercopy.o
2026-05-03T01:25:00.3858609Z lib/.tmp_usercopy.o: no symbols
2026-05-03T01:25:00.3917976Z   CC      lib/errseq.o
2026-05-03T01:25:00.5011154Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_hw.o
2026-05-03T01:25:00.5990439Z   CC      lib/bucket_locks.o
2026-05-03T01:25:00.8496648Z   CC      net/core/sock_diag.o
2026-05-03T01:25:01.0768230Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_debug.o
2026-05-03T01:25:01.1930473Z   CC      lib/string_helpers.o
2026-05-03T01:25:01.3090450Z   CC      net/ipv4/ip_forward.o
2026-05-03T01:25:01.9200626Z   CC      lib/hexdump.o
2026-05-03T01:25:01.9981735Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_gpu_memory_debugfs.o
2026-05-03T01:25:02.0819982Z   CC      net/core/dev_ioctl.o
2026-05-03T01:25:02.1161164Z   CC      lib/kstrtox.o
2026-05-03T01:25:02.2530649Z   CC      net/ipv4/ip_options.o
2026-05-03T01:25:02.6180932Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_mem_linux.o
2026-05-03T01:25:02.6278245Z   CC      lib/pci_iomap.o
2026-05-03T01:25:03.0460350Z lib/.tmp_pci_iomap.o: no symbols
2026-05-03T01:25:03.0509939Z   CC      lib/iomap_copy.o
2026-05-03T01:25:03.0760310Z   CC      net/core/tso.o
2026-05-03T01:25:03.2441177Z ../drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_mem_linux.c:1044:18: warning: variable 'dma_buf' set but not used [-Wunused-but-set-variable]
2026-05-03T01:25:03.2469952Z         struct dma_buf *dma_buf;
2026-05-03T01:25:03.2480055Z                         ^
2026-05-03T01:25:03.4800354Z   CC      lib/devres.o
2026-05-03T01:25:03.6180504Z 1 warning generated.
2026-05-03T01:25:03.6834486Z   CC      net/ipv4/ip_output.o
2026-05-03T01:25:03.9731089Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_core_linux.o
2026-05-03T01:25:04.2430587Z   CC      lib/logic_pio.o
2026-05-03T01:25:04.3000382Z   CC      net/core/sock_reuseport.o
2026-05-03T01:25:04.7030563Z   CC      lib/hweight.o
2026-05-03T01:25:04.8690401Z   CC      lib/assoc_array.o
2026-05-03T01:25:05.3641271Z   CC      lib/list_debug.o
2026-05-03T01:25:05.4616515Z   CC      net/ipv4/ip_sockglue.o
2026-05-03T01:25:05.5610316Z   CC      net/core/fib_notifier.o
2026-05-03T01:25:05.6015008Z   CC      lib/bitrev.o
2026-05-03T01:25:05.6390499Z lib/.tmp_bitrev.o: no symbols
2026-05-03T01:25:05.6419961Z   CC      lib/rational.o
2026-05-03T01:25:05.6671202Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_mem_profile_debugfs.o
2026-05-03T01:25:05.7095041Z   CC      lib/crc-ccitt.o
2026-05-03T01:25:06.1700481Z   CC      lib/crc16.o
2026-05-03T01:25:06.3111458Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_disjoint_events.o
2026-05-03T01:25:06.5550485Z   CC      net/core/xdp.o
2026-05-03T01:25:06.5700323Z   CC      lib/libcrc32c.o
2026-05-03T01:25:07.0290343Z   CC      lib/genalloc.o
2026-05-03T01:25:07.0400320Z   CC      net/ipv4/inet_hashtables.o
2026-05-03T01:25:07.2190852Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_gator_api.o
2026-05-03T01:25:07.6920548Z   CC      lib/textsearch.o
2026-05-03T01:25:07.8754088Z   CC      net/core/net-sysfs.o
2026-05-03T01:25:08.1526685Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_debug_mem_view.o
2026-05-03T01:25:08.1773533Z   CC      lib/ts_kmp.o
2026-05-03T01:25:08.4840743Z   CC      lib/ts_bm.o
2026-05-03T01:25:08.5500540Z   CC      net/ipv4/inet_timewait_sock.o
2026-05-03T01:25:08.7394661Z drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/.tmp_mali_kbase_debug_mem_view.o: no symbols
2026-05-03T01:25:08.7480535Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_smc.o
2026-05-03T01:25:08.8480415Z   CC      lib/ts_fsm.o
2026-05-03T01:25:09.2207342Z   CC      lib/percpu_counter.o
2026-05-03T01:25:09.3361004Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_mem_pool.o
2026-05-03T01:25:09.4050632Z   CC      net/core/net-procfs.o
2026-05-03T01:25:09.7374175Z   CC      lib/audit.o
2026-05-03T01:25:09.8240585Z   CC      net/ipv4/inet_connection_sock.o
2026-05-03T01:25:10.0280803Z   CC      net/core/fib_rules.o
2026-05-03T01:25:10.1810376Z   CC      lib/compat_audit.o
2026-05-03T01:25:10.2220558Z   CC      lib/fault-inject.o
2026-05-03T01:25:10.3960850Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_mem_pool_debugfs.o
2026-05-03T01:25:10.7753370Z   CC      lib/syscall.o
2026-05-03T01:25:10.9839836Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_debugfs_helper.o
2026-05-03T01:25:11.2530601Z   CC      lib/dynamic_debug.o
2026-05-03T01:25:11.3291175Z ../drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_debugfs_helper.c:93:9: warning: variable 'index' set but not used [-Wunused-but-set-variable]
2026-05-03T01:25:11.3319784Z         size_t index;
2026-05-03T01:25:11.3359882Z                ^
2026-05-03T01:25:11.3830457Z 1 warning generated.
2026-05-03T01:25:11.4170368Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_strings.o
2026-05-03T01:25:11.4605004Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_as_fault_debugfs.o
2026-05-03T01:25:11.4633245Z   CC      net/ipv4/tcp.o
2026-05-03T01:25:11.5590343Z   CC      net/core/net-traces.o
2026-05-03T01:25:12.0768728Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_regs_history_debugfs.o
2026-05-03T01:25:12.4360359Z   CC      lib/nlattr.o
2026-05-03T01:25:12.7012077Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_dvfs_debugfs.o
2026-05-03T01:25:13.2800943Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_power_gpu_frequency_trace.o
2026-05-03T01:25:13.3488916Z   CC      lib/checksum.o
2026-05-03T01:25:13.6020529Z   CC      net/ipv4/tcp_input.o
2026-05-03T01:25:13.6210661Z   CC      net/core/dst_cache.o
2026-05-03T01:25:13.8055261Z   CC      lib/cpu_rmap.o
2026-05-03T01:25:13.8250857Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_trace_gpu_mem.o
2026-05-03T01:25:14.3350791Z   CC      lib/dynamic_queue_limits.o
2026-05-03T01:25:14.4843521Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_fence_ops.o
2026-05-03T01:25:14.6020382Z   CC      lib/glob.o
2026-05-03T01:25:14.8410658Z   CC      net/core/gro_cells.o
2026-05-03T01:25:14.9960402Z   CC      lib/strncpy_from_user.o
2026-05-03T01:25:15.0940772Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_sync_file.o
2026-05-03T01:25:15.6610738Z   CC      lib/strnlen_user.o
2026-05-03T01:25:15.8020526Z   AR      net/core/built-in.a
2026-05-03T01:25:15.8090858Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_sync_common.o
2026-05-03T01:25:15.8790526Z   AR      virt/lib/built-in.a
2026-05-03T01:25:15.8900117Z   AR      virt/built-in.a
2026-05-03T01:25:15.9010411Z   CC      net/ipv4/tcp_output.o
2026-05-03T01:25:16.2940408Z   CC      lib/net_utils.o
2026-05-03T01:25:16.4500815Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_jm.o
2026-05-03T01:25:16.4875325Z   CC      drivers/hid/usbhid/hid-core.o
2026-05-03T01:25:17.0510587Z   CC      lib/sg_pool.o
2026-05-03T01:25:17.0530916Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_hwcnt_backend_jm.o
2026-05-03T01:25:17.4350470Z   AR      drivers/hid/usbhid/built-in.a
2026-05-03T01:25:17.4460165Z   CC      drivers/hid/hid-core.o
2026-05-03T01:25:17.6690281Z   CC      lib/asn1_decoder.o
2026-05-03T01:25:17.7471082Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_dummy_job_wa.o
2026-05-03T01:25:17.9095885Z   CC      net/ipv4/tcp_timer.o
2026-05-03T01:25:18.1120522Z   CC      lib/oid_registry.o
2026-05-03T01:25:18.4030980Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_debug_job_fault.o
2026-05-03T01:25:18.5687519Z   CC      drivers/hid/hid-input.o
2026-05-03T01:25:18.5850462Z   CC      lib/sbitmap.o
2026-05-03T01:25:18.9920950Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_event.o
2026-05-03T01:25:19.2590368Z   CC      lib/argv_split.o
2026-05-03T01:25:19.3201147Z   CC      net/ipv4/tcp_ipv4.o
2026-05-03T01:25:19.5538284Z   CC      drivers/hid/hid-quirks.o
2026-05-03T01:25:19.6328104Z   CC      lib/bug.o
2026-05-03T01:25:19.9160792Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_jd.o
2026-05-03T01:25:19.9291344Z   CC      lib/clz_tab.o
2026-05-03T01:25:19.9680978Z   CC      lib/cmdline.o
2026-05-03T01:25:20.1740332Z   CC      lib/cpumask.o
2026-05-03T01:25:20.2130376Z   CC      drivers/hid/hidraw.o
2026-05-03T01:25:20.4921618Z ../drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_jd.c:1584:7: warning: variable 'need_to_try_schedule_context' set but not used [-Wunused-but-set-variable]
2026-05-03T01:25:20.4949950Z         bool need_to_try_schedule_context;
2026-05-03T01:25:20.4970065Z              ^
2026-05-03T01:25:20.5520236Z   CC      lib/ctype.o
2026-05-03T01:25:20.6210414Z   CC      lib/dec_and_lock.o
2026-05-03T01:25:20.7340421Z 1 warning generated.
2026-05-03T01:25:20.8605428Z   CC      lib/decompress.o
2026-05-03T01:25:20.9470219Z   CC      drivers/hid/uhid.o
2026-05-03T01:25:20.9625413Z   CC      lib/decompress_inflate.o
2026-05-03T01:25:21.0740807Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_jd_debugfs.o
2026-05-03T01:25:21.1134935Z   CC      net/ipv4/tcp_minisocks.o
2026-05-03T01:25:21.1151121Z drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/.tmp_mali_kbase_jd_debugfs.o: no symbols
2026-05-03T01:25:21.1221025Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_js.o
2026-05-03T01:25:21.3554255Z   CC      lib/decompress_unlz4.o
2026-05-03T01:25:21.6811350Z ../drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_js.c:559:32: warning: variable 'js_devdata' set but not used [-Wunused-but-set-variable]
2026-05-03T01:25:21.6840091Z         struct kbasep_js_device_data *js_devdata;
2026-05-03T01:25:21.6859923Z                                       ^
2026-05-03T01:25:21.6890833Z ../drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_js.c:578:23: warning: variable 'kbdev' set but not used [-Wunused-but-set-variable]
2026-05-03T01:25:21.6919922Z         struct kbase_device *kbdev;
2026-05-03T01:25:21.6939961Z                              ^
2026-05-03T01:25:21.6941163Z ../drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_js.c:626:30: warning: variable 'js_kctx_info' set but not used [-Wunused-but-set-variable]
2026-05-03T01:25:21.6979958Z         struct kbasep_js_kctx_info *js_kctx_info;
2026-05-03T01:25:21.7006873Z                                     ^
2026-05-03T01:25:21.7030867Z ../drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_js.c:1598:6: warning: variable 'kctx_as_nr' set but not used [-Wunused-but-set-variable]
2026-05-03T01:25:21.7032125Z         int kctx_as_nr;
2026-05-03T01:25:21.7071324Z             ^
2026-05-03T01:25:21.7075015Z ../drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_js.c:1982:8: warning: variable 'retained' set but not used [-Wunused-but-set-variable]
2026-05-03T01:25:21.7080966Z                 bool retained;
2026-05-03T01:25:21.7081759Z                      ^
2026-05-03T01:25:21.7164954Z   CC      lib/dump_stack.o
2026-05-03T01:25:21.7165657Z   CC      drivers/hid/hid-generic.o
2026-05-03T01:25:21.7558191Z ../drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_js.c:3710:8: warning: variable 'was_retained' set but not used [-Wunused-but-set-variable]
2026-05-03T01:25:21.7590456Z                 bool was_retained;
2026-05-03T01:25:21.7591151Z                      ^
2026-05-03T01:25:22.1240546Z   CC      drivers/hid/hid-a4tech.o
2026-05-03T01:25:22.1500334Z 6 warnings generated.
2026-05-03T01:25:22.3887130Z   CC      lib/earlycpio.o
2026-05-03T01:25:22.4897313Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_js_ctx_attr.o
2026-05-03T01:25:22.4930182Z   CC      drivers/hid/hid-apple.o
2026-05-03T01:25:22.5200399Z   CC      lib/extable.o
2026-05-03T01:25:22.5700563Z   CC      net/ipv4/tcp_cong.o
2026-05-03T01:25:22.8766551Z   CC      lib/fdt.o
2026-05-03T01:25:22.9490108Z   CC      drivers/hid/hid-belkin.o
2026-05-03T01:25:23.0400564Z   CC      lib/fdt_empty_tree.o
2026-05-03T01:25:23.1560968Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_kinstr_jm.o
2026-05-03T01:25:23.1790275Z   CC      lib/fdt_ro.o
2026-05-03T01:25:23.3562293Z   CC      drivers/hid/hid-cherry.o
2026-05-03T01:25:23.4409995Z   CC      lib/fdt_rw.o
2026-05-03T01:25:23.6733143Z   CC      lib/fdt_strerror.o
2026-05-03T01:25:23.7287813Z   CC      drivers/hid/hid-chicony.o
2026-05-03T01:25:23.7975929Z   CC      lib/fdt_sw.o
2026-05-03T01:25:23.9790400Z   CC      lib/fdt_wip.o
2026-05-03T01:25:24.0894510Z   CC      net/ipv4/tcp_metrics.o
2026-05-03T01:25:24.1030540Z   CC      lib/flex_proportions.o
2026-05-03T01:25:24.1260406Z   CC      drivers/hid/hid-cypress.o
2026-05-03T01:25:24.1941055Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mali_kbase_fence.o
2026-05-03T01:25:24.3890355Z   CC      lib/idr.o
2026-05-03T01:25:24.5390555Z   CC      drivers/hid/hid-dr.o
2026-05-03T01:25:24.8240344Z   CC      lib/int_sqrt.o
2026-05-03T01:25:24.8571034Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/context/mali_kbase_context.o
2026-05-03T01:25:24.9210569Z   CC      drivers/hid/hid-ezkey.o
2026-05-03T01:25:24.9960419Z   CC      lib/ioremap.o
2026-05-03T01:25:25.1910822Z   CC      net/ipv4/tcp_fastopen.o
2026-05-03T01:25:25.3110459Z   CC      drivers/hid/hid-gyration.o
2026-05-03T01:25:25.5161165Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/context/backend/mali_kbase_context_jm.o
2026-05-03T01:25:25.7042095Z   CC      lib/irq_regs.o
2026-05-03T01:25:25.7077064Z   CC      drivers/hid/hid-kensington.o
2026-05-03T01:25:25.9380581Z   CC      lib/is_single_threaded.o
2026-05-03T01:25:26.1164489Z   CC      drivers/hid/hid-kye.o
2026-05-03T01:25:26.2470436Z   CC      lib/klist.o
2026-05-03T01:25:26.4350985Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/debug/mali_kbase_debug_ktrace.o
2026-05-03T01:25:26.5282721Z   CC      drivers/hid/hid-lg.o
2026-05-03T01:25:26.5786439Z   CC      net/ipv4/tcp_rate.o
2026-05-03T01:25:26.6900428Z   CC      lib/kobject.o
2026-05-03T01:25:27.0091800Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/debug/backend/mali_kbase_debug_ktrace_jm.o
2026-05-03T01:25:27.0637795Z   CC      drivers/hid/hid-magicmouse.o
2026-05-03T01:25:27.2860404Z   CC      lib/kobject_uevent.o
2026-05-03T01:25:27.5200603Z   CC      drivers/hid/hid-microsoft.o
2026-05-03T01:25:27.5571145Z drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/debug/backend/.tmp_mali_kbase_debug_ktrace_jm.o: no symbols
2026-05-03T01:25:27.5630373Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/device/mali_kbase_device.o
2026-05-03T01:25:27.9297776Z   CC      net/ipv4/tcp_recovery.o
2026-05-03T01:25:27.9670455Z   CC      drivers/hid/hid-monterey.o
2026-05-03T01:25:28.3380550Z   CC      drivers/hid/hid-nintendo.o
2026-05-03T01:25:28.4804444Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/device/mali_kbase_device_hw.o
2026-05-03T01:25:28.5535502Z   CC      lib/nmi_backtrace.o
2026-05-03T01:25:28.7880602Z   CC      drivers/hid/hid-pl.o
2026-05-03T01:25:28.8100327Z   CC      net/ipv4/tcp_ulp.o
2026-05-03T01:25:29.0370412Z lib/.tmp_nmi_backtrace.o: no symbols
2026-05-03T01:25:29.0398173Z   CC      lib/nodemask.o
2026-05-03T01:25:29.1990601Z   CC      drivers/hid/hid-petalynx.o
2026-05-03T01:25:29.3703595Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/device/backend/mali_kbase_device_jm.o
2026-05-03T01:25:29.4480660Z   CC      lib/plist.o
2026-05-03T01:25:29.6260581Z   CC      drivers/hid/hid-samsung.o
2026-05-03T01:25:29.6650483Z   CC      lib/radix-tree.o
2026-05-03T01:25:29.9900952Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/device/backend/mali_kbase_device_hw_jm.o
2026-05-03T01:25:30.0855707Z   CC      drivers/hid/hid-sjoy.o
2026-05-03T01:25:30.1728654Z   CC      net/ipv4/tcp_offload.o
2026-05-03T01:25:30.3298418Z   CC      lib/ratelimit.o
2026-05-03T01:25:30.4980657Z   CC      drivers/hid/hid-sony.o
2026-05-03T01:25:30.5632046Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_cache_policy_backend.o
2026-05-03T01:25:30.7080397Z   CC      lib/rbtree.o
2026-05-03T01:25:31.0640368Z   CC      lib/seq_buf.o
2026-05-03T01:25:31.1250789Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_gpuprops_backend.o
2026-05-03T01:25:31.1623626Z   CC      drivers/hid/hid-sunplus.o
2026-05-03T01:25:31.4670124Z   CC      lib/sha1.o
2026-05-03T01:25:31.5250505Z   CC      drivers/hid/hid-gaff.o
2026-05-03T01:25:31.5420499Z   CC      net/ipv4/datagram.o
2026-05-03T01:25:31.7410626Z   CC      lib/show_mem.o
2026-05-03T01:25:31.7740821Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_irq_linux.o
2026-05-03T01:25:31.9142547Z   CC      drivers/hid/hid-tmff.o
2026-05-03T01:25:32.1740406Z   CC      lib/siphash.o
2026-05-03T01:25:32.3240573Z   CC      drivers/hid/hid-topseed.o
2026-05-03T01:25:32.6800963Z   CC      drivers/hid/hid-twinhan.o
2026-05-03T01:25:32.7000932Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_js_backend.o
2026-05-03T01:25:32.7070712Z   CC      lib/string.o
2026-05-03T01:25:32.8190581Z   CC      net/ipv4/raw.o
2026-05-03T01:25:33.1010374Z   CC      drivers/hid/hid-zpff.o
2026-05-03T01:25:33.1910439Z   CC      lib/timerqueue.o
2026-05-03T01:25:33.3160875Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_pm_backend.o
2026-05-03T01:25:33.4780282Z   CC      lib/vsprintf.o
2026-05-03T01:25:33.5200569Z   AR      drivers/hid/built-in.a
2026-05-03T01:25:33.5500201Z   AR      drivers/gpu/vga/built-in.a
2026-05-03T01:25:33.5770312Z   CC      drivers/gpu/mediatek/gpufreq/mt6768/mtk_picachu.o
2026-05-03T01:25:34.1129869Z   CC      drivers/gpu/mediatek/gpufreq/mt6768/mtk_gpufreq_core.o
2026-05-03T01:25:34.2371088Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_pm_driver.o
2026-05-03T01:25:34.4100649Z   CC      net/ipv4/udp.o
2026-05-03T01:25:35.1630357Z   CC      lib/win_minmax.o
2026-05-03T01:25:35.2606330Z   CC      drivers/gpu/mediatek/gpufreq/mt6768/mtk_gpu_log.o
2026-05-03T01:25:35.3321094Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_pm_metrics.o
2026-05-03T01:25:35.5160467Z   CC      drivers/gpu/mediatek/gpufreq/mt6768/mtk_gpu_bw.o
2026-05-03T01:25:35.5780446Z   GEN     lib/crc32table.h
2026-05-03T01:25:35.5815543Z   AR      lib/lib.a
2026-05-03T01:25:35.6730509Z   CC      lib/crc32.o
2026-05-03T01:25:36.0560415Z   AR      drivers/gpu/mediatek/gpufreq/mt6768/built-in.a
2026-05-03T01:25:36.0740204Z   AR      drivers/gpu/mediatek/gpufreq/built-in.a
2026-05-03T01:25:36.1151073Z   CC      net/ipv6/netfilter/ip6_tables.o
2026-05-03T01:25:36.1971086Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_pm_ca.o
2026-05-03T01:25:36.5270372Z   EXPORTS lib/lib-ksyms.o
2026-05-03T01:25:36.6938612Z   CC      net/ipv4/udplite.o
2026-05-03T01:25:36.8421497Z lib/nmi_backtrace.o: no symbols
2026-05-03T01:25:36.9990363Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_pm_always_on.o
2026-05-03T01:25:37.0076964Z   AR      lib/built-in.a
2026-05-03T01:25:37.1030903Z   CC      net/ipv6/netfilter/ip6table_filter.o
2026-05-03T01:25:37.6350514Z   CC      net/key/af_key.o
2026-05-03T01:25:37.9130793Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_pm_coarse_demand.o
2026-05-03T01:25:37.9260309Z   CC      net/ipv6/netfilter/ip6table_mangle.o
2026-05-03T01:25:37.9670025Z   CC      net/ipv4/udp_offload.o
2026-05-03T01:25:38.7750489Z   CC      net/ipv6/netfilter/ip6table_raw.o
2026-05-03T01:25:38.8120993Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_pm_policy.o
2026-05-03T01:25:38.9280571Z   AR      net/key/built-in.a
2026-05-03T01:25:38.9408071Z   AR      drivers/hwtracing/intel_th/built-in.a
2026-05-03T01:25:38.9580470Z   CC      drivers/gpu/mediatek/hal/mtk_gpu_utility.o
2026-05-03T01:25:39.3765660Z   CC      net/ipv4/arp.o
2026-05-03T01:25:39.4324453Z   AR      drivers/gpu/mediatek/hal/built-in.a
2026-05-03T01:25:39.4450481Z   CC      net/ipv6/af_inet6.o
2026-05-03T01:25:39.6121047Z   CC      net/ipv6/netfilter/nf_nat_l3proto_ipv6.o
2026-05-03T01:25:39.7460785Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_time.o
2026-05-03T01:25:40.3830978Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_l2_mmu_config.o
2026-05-03T01:25:40.8820553Z   CC      net/ipv4/icmp.o
2026-05-03T01:25:40.9192022Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_clk_rate_trace_mgr.o
2026-05-03T01:25:40.9980621Z   CC      net/ipv6/netfilter/nf_nat_proto_icmpv6.o
2026-05-03T01:25:41.1620691Z   DTC     arch/arm64/boot/dts/mediatek/auto2712p1v1-ivi-boot.dtb
2026-05-03T01:25:41.2031399Z ../arch/arm64/boot/dts/mediatek/auto2712p1v1-common.dtsi:535.20-550.4: Warning (i2c_bus_reg): /soc/i2c@11007000/rtq2134-regulator: I2C bus unit address format error, expected "18"
2026-05-03T01:25:41.2060996Z ../arch/arm64/boot/dts/mediatek/auto2712p1v1-common.dtsi:552.29-568.4: Warning (i2c_bus_reg): /soc/i2c@11007000/rtq5115-regulator: I2C bus unit address format error, expected "3f"
2026-05-03T01:25:41.2090632Z ../arch/arm64/boot/dts/mediatek/auto2712p1v1-common.dtsi:577.20-600.4: Warning (i2c_bus_reg): /soc/i2c@11008000/rtq2134-regulator: I2C bus unit address format error, expected "18"
2026-05-03T01:25:41.2092601Z ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:335.23-344.5: Warning (spi_bus_bridge): /soc/spi@10013000: incorrect #address-cells for SPI bus
2026-05-03T01:25:41.2120264Z   also defined at ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:335.23-344.5
2026-05-03T01:25:41.2150245Z   also defined at ../arch/arm64/boot/dts/mediatek/auto2712p1v1-common.dtsi:1937.8-1945.3
2026-05-03T01:25:41.2180439Z ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:335.23-344.5: Warning (spi_bus_bridge): /soc/spi@10013000: incorrect #size-cells for SPI bus
2026-05-03T01:25:41.2181762Z   also defined at ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:335.23-344.5
2026-05-03T01:25:41.2210307Z   also defined at ../arch/arm64/boot/dts/mediatek/auto2712p1v1-common.dtsi:1937.8-1945.3
2026-05-03T01:25:41.2240428Z arch/arm64/boot/dts/mediatek/auto2712p1v1-ivi-boot.dtb: Warning (spi_bus_reg): Failed prerequisite 'spi_bus_bridge'
2026-05-03T01:25:41.2270587Z ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:1364.4-42: Warning (mboxes_property): /soc/dispsys@14000000:mboxes: cell 4 is not a phandle reference
2026-05-03T01:25:41.2272781Z ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:1359.40-1365.5: Warning (mboxes_property): /soc/dispsys@14000000: Missing property '#mbox-cells' in node /soc/intpol-controller@10220a80 or bad phandle (referred from mboxes[4])
2026-05-03T01:25:41.2274289Z   also defined at ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:1359.40-1365.5
2026-05-03T01:25:41.2275382Z ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:1385.4-24: Warning (mboxes_property): /soc/rdma@14001000:mboxes: property size (12) too small for cell size 3
2026-05-03T01:25:41.2277095Z ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:1400.4-24: Warning (mboxes_property): /soc/rdma@14002000:mboxes: property size (12) too small for cell size 3
2026-05-03T01:25:41.2278652Z ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:1734.4-24: Warning (mboxes_property): /soc/rdma@14028000:mboxes: property size (12) too small for cell size 3
2026-05-03T01:25:41.2280407Z ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:1886.4-24: Warning (mboxes_property): /soc/rdma@14033000:mboxes: property size (12) too small for cell size 3
2026-05-03T01:25:41.2282308Z ../arch/arm64/boot/dts/mediatek/auto2712p1v1-common.dtsi:1918.19-1920.5: Warning (graph_endpoint): /soc/rdma@1400f000/port/endpoint: graph connection to node '/soc/dsi@14035000/ports/port/endpoint' is not bidirectional
2026-05-03T01:25:41.2450384Z   DTC     arch/arm64/boot/dts/mediatek/auto2712p1v1-ivi-nand-boot.dtb
2026-05-03T01:25:41.2851423Z ../arch/arm64/boot/dts/mediatek/auto2712p1v1-common.dtsi:535.20-550.4: Warning (i2c_bus_reg): /soc/i2c@11007000/rtq2134-regulator: I2C bus unit address format error, expected "18"
2026-05-03T01:25:41.2870745Z ../arch/arm64/boot/dts/mediatek/auto2712p1v1-common.dtsi:552.29-568.4: Warning (i2c_bus_reg): /soc/i2c@11007000/rtq5115-regulator: I2C bus unit address format error, expected "3f"
2026-05-03T01:25:41.2890686Z ../arch/arm64/boot/dts/mediatek/auto2712p1v1-common.dtsi:577.20-600.4: Warning (i2c_bus_reg): /soc/i2c@11008000/rtq2134-regulator: I2C bus unit address format error, expected "18"
2026-05-03T01:25:41.2892424Z ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:335.23-344.5: Warning (spi_bus_bridge): /soc/spi@10013000: incorrect #address-cells for SPI bus
2026-05-03T01:25:41.2893500Z   also defined at ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:335.23-344.5
2026-05-03T01:25:41.2894288Z   also defined at ../arch/arm64/boot/dts/mediatek/auto2712p1v1-common.dtsi:1937.8-1945.3
2026-05-03T01:25:41.2895401Z ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:335.23-344.5: Warning (spi_bus_bridge): /soc/spi@10013000: incorrect #size-cells for SPI bus
2026-05-03T01:25:41.2896446Z   also defined at ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:335.23-344.5
2026-05-03T01:25:41.2897216Z   also defined at ../arch/arm64/boot/dts/mediatek/auto2712p1v1-common.dtsi:1937.8-1945.3
2026-05-03T01:25:41.2898299Z arch/arm64/boot/dts/mediatek/auto2712p1v1-ivi-nand-boot.dtb: Warning (spi_bus_reg): Failed prerequisite 'spi_bus_bridge'
2026-05-03T01:25:41.2899900Z ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:1364.4-42: Warning (mboxes_property): /soc/dispsys@14000000:mboxes: cell 4 is not a phandle reference
2026-05-03T01:25:41.2901824Z ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:1359.40-1365.5: Warning (mboxes_property): /soc/dispsys@14000000: Missing property '#mbox-cells' in node /soc/intpol-controller@10220a80 or bad phandle (referred from mboxes[4])
2026-05-03T01:25:41.2903348Z   also defined at ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:1359.40-1365.5
2026-05-03T01:25:41.2904516Z ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:1385.4-24: Warning (mboxes_property): /soc/rdma@14001000:mboxes: property size (12) too small for cell size 3
2026-05-03T01:25:41.2906056Z ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:1400.4-24: Warning (mboxes_property): /soc/rdma@14002000:mboxes: property size (12) too small for cell size 3
2026-05-03T01:25:41.2907588Z ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:1734.4-24: Warning (mboxes_property): /soc/rdma@14028000:mboxes: property size (12) too small for cell size 3
2026-05-03T01:25:41.2909640Z ../arch/arm64/boot/dts/mediatek/mt2712.dtsi:1886.4-24: Warning (mboxes_property): /soc/rdma@14033000:mboxes: property size (12) too small for cell size 3
2026-05-03T01:25:41.2940856Z ../arch/arm64/boot/dts/mediatek/auto2712p1v1-common.dtsi:1918.19-1920.5: Warning (graph_endpoint): /soc/rdma@1400f000/port/endpoint: graph connection to node '/soc/dsi@14035000/ports/port/endpoint' is not bidirectional
2026-05-03T01:25:41.4330556Z   CC      net/l2tp/l2tp_core.o
2026-05-03T01:25:41.8482332Z   CC      net/ipv6/netfilter/nf_defrag_ipv6_hooks.o
2026-05-03T01:25:41.8961247Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_instr_backend.o
2026-05-03T01:25:42.4780827Z   CC      net/ipv4/devinet.o
2026-05-03T01:25:42.7911058Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_jm_as.o
2026-05-03T01:25:43.1150606Z   CC      net/l2tp/l2tp_ppp.o
2026-05-03T01:25:43.2142805Z   CC      net/ipv6/netfilter/nf_conntrack_reasm.o
2026-05-03T01:25:43.3521606Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_debug_job_fault_backend.o
2026-05-03T01:25:43.9661234Z drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/.tmp_mali_kbase_debug_job_fault_backend.o: no symbols
2026-05-03T01:25:43.9700647Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_jm_hw.o
2026-05-03T01:25:44.0680374Z   CC      net/ipv4/af_inet.o
2026-05-03T01:25:44.2300534Z   AR      net/l2tp/built-in.a
2026-05-03T01:25:44.2546157Z   AR      drivers/i2c/algos/built-in.a
2026-05-03T01:25:44.2775202Z   CC      drivers/i2c/busses/i2c-mtk.o
2026-05-03T01:25:44.5656935Z ../drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_jm_hw.c:1006:7: warning: variable 'stopped' set but not used [-Wunused-but-set-variable]
2026-05-03T01:25:44.5706107Z         bool stopped;
2026-05-03T01:25:44.5749905Z              ^
2026-05-03T01:25:44.6517305Z   CC      net/ipv6/netfilter/nf_socket_ipv6.o
2026-05-03T01:25:44.7090392Z 1 warning generated.
2026-05-03T01:25:45.0561140Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/backend/gpu/mali_kbase_jm_rb.o
2026-05-03T01:25:45.5000290Z   CC      drivers/i2c/busses/i2c-mtk_debug.o
2026-05-03T01:25:45.7230682Z   CC      net/ipv4/igmp.o
2026-05-03T01:25:45.7750847Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mmu/mali_kbase_mmu.o
2026-05-03T01:25:45.9793402Z ../drivers/i2c/busses/i2c-mtk_debug.c:378:8: warning: variable 'buf_test' set but not used [-Wunused-but-set-variable]
2026-05-03T01:25:45.9829903Z         char *buf_test;
2026-05-03T01:25:45.9840012Z               ^
2026-05-03T01:25:46.0343836Z   CC      net/ipv6/netfilter/nf_tproxy_ipv6.o
2026-05-03T01:25:46.0790760Z 1 warning generated.
2026-05-03T01:25:46.3631593Z   AR      drivers/i2c/busses/built-in.a
2026-05-03T01:25:46.3853781Z   AR      drivers/i2c/muxes/built-in.a
2026-05-03T01:25:46.3960817Z   CC      drivers/i2c/i2c-boardinfo.o
2026-05-03T01:25:46.8944798Z   CC      drivers/i2c/i2c-core-base.o
2026-05-03T01:25:46.9030854Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mmu/mali_kbase_mmu_hw_direct.o
2026-05-03T01:25:47.3630708Z   CC      net/ipv6/netfilter/nf_reject_ipv6.o
2026-05-03T01:25:47.4741231Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mmu/mali_kbase_mmu_mode_aarch64.o
2026-05-03T01:25:47.4874034Z   CC      net/ipv4/fib_frontend.o
2026-05-03T01:25:48.1360985Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/mmu/backend/mali_kbase_mmu_jm.o
2026-05-03T01:25:48.1710376Z   CC      drivers/i2c/i2c-core-smbus.o
2026-05-03T01:25:48.7304545Z   CC      net/ipv6/netfilter/ip6t_frag.o
2026-05-03T01:25:48.7681138Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/tl/mali_kbase_timeline.o
2026-05-03T01:25:48.9745349Z   CC      net/ipv4/fib_semantics.o
2026-05-03T01:25:49.1700421Z   CC      drivers/i2c/i2c-core-of.o
2026-05-03T01:25:49.4301007Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/tl/mali_kbase_timeline_io.o
2026-05-03T01:25:49.6080292Z   CC      net/ipv6/netfilter/ip6t_ipv6header.o
2026-05-03T01:25:49.7110956Z   CC      drivers/i2c/i2c-mux.o
2026-05-03T01:25:50.0901156Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/tl/mali_kbase_tlstream.o
2026-05-03T01:25:50.3007803Z   AR      drivers/i2c/built-in.a
2026-05-03T01:25:50.3175649Z   CC      net/ipv6/anycast.o
2026-05-03T01:25:50.4300658Z   CC      net/ipv6/netfilter/ip6t_rpfilter.o
2026-05-03T01:25:50.5840594Z   CC      net/ipv4/fib_trie.o
2026-05-03T01:25:50.6588617Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/tl/mali_kbase_tracepoints.o
2026-05-03T01:25:51.2660727Z   AR      drivers/i3c/built-in.a
2026-05-03T01:25:51.2824785Z   CC      net/llc/llc_core.o
2026-05-03T01:25:51.3200486Z   CC      net/ipv6/netfilter/ip6t_REJECT.o
2026-05-03T01:25:51.4240577Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/tl/backend/mali_kbase_timeline_jm.o
2026-05-03T01:25:52.0551079Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/gpu/mali_kbase_gpu.o
2026-05-03T01:25:52.1760552Z   AR      net/ipv6/netfilter/built-in.a
2026-05-03T01:25:52.1940198Z   CC      net/ipv6/ip6_output.o
2026-05-03T01:25:52.3200388Z   CC      net/llc/llc_input.o
2026-05-03T01:25:52.4590641Z   CC      net/ipv4/fib_notifier.o
2026-05-03T01:25:52.5961069Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/gpu/backend/mali_kbase_gpu_fault_jm.o
2026-05-03T01:25:53.1761365Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/thirdparty/mali_kbase_mmap.o
2026-05-03T01:25:53.3249171Z   CC      net/ipv4/inet_fragment.o
2026-05-03T01:25:53.3273937Z   CC      net/llc/llc_output.o
2026-05-03T01:25:53.8012061Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/platform/mt6768/mali_kbase_config_mt6768.o
2026-05-03T01:25:54.1410371Z   CC      net/ipv6/ip6_input.o
2026-05-03T01:25:54.2306619Z   AR      net/llc/built-in.a
2026-05-03T01:25:54.2519091Z   AR      drivers/idle/built-in.a
2026-05-03T01:25:54.2614955Z   CC      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/platform/mt6768/mali_kbase_cpu_mt6768.o
2026-05-03T01:25:54.4590570Z   CC      net/ipv6/addrconf.o
2026-05-03T01:25:54.8410938Z   AR      drivers/gpu/mediatek/gpu_mali/mali_valhall/mali-r32p1/drivers/gpu/arm/midgard/built-in.a
2026-05-03T01:25:54.9100718Z   AR      drivers/gpu/mediatek/gpu_mali/mali_valhall/built-in.a
2026-05-03T01:25:54.9280133Z   AR      drivers/gpu/mediatek/gpu_mali/built-in.a
2026-05-03T01:25:54.9480031Z   AR      drivers/gpu/mediatek/built-in.a
2026-05-03T01:25:54.9730399Z   AR      drivers/gpu/built-in.a
2026-05-03T01:25:55.0026395Z   AR      drivers/iio/accel/built-in.a
2026-05-03T01:25:55.0073136Z   CC      net/ipv4/ping.o
2026-05-03T01:25:55.0201075Z   CC      drivers/iio/adc/mt635x-auxadc_v1.o
2026-05-03T01:25:55.4075658Z   CC      drivers/iio/adc/mt6577_auxadc.o
2026-05-03T01:25:55.6970393Z   CC      net/mac80211/main.o
2026-05-03T01:25:55.8410356Z   AR      drivers/iio/adc/built-in.a
2026-05-03T01:25:55.8590269Z   AR      drivers/iio/afe/built-in.a
2026-05-03T01:25:55.8750246Z   AR      drivers/iio/amplifiers/built-in.a
2026-05-03T01:25:55.8920115Z   AR      drivers/iio/buffer/built-in.a
2026-05-03T01:25:55.9080176Z   AR      drivers/iio/chemical/built-in.a
2026-05-03T01:25:55.9310319Z   AR      drivers/iio/common/cros_ec_sensors/built-in.a
2026-05-03T01:25:55.9490472Z   AR      drivers/iio/common/hid-sensors/built-in.a
2026-05-03T01:25:55.9670539Z   AR      drivers/iio/common/ms_sensors/built-in.a
2026-05-03T01:25:55.9825585Z   AR      drivers/iio/common/ssp_sensors/built-in.a
2026-05-03T01:25:55.9980987Z   AR      drivers/iio/common/st_sensors/built-in.a
2026-05-03T01:25:56.0175394Z   AR      drivers/iio/common/built-in.a
2026-05-03T01:25:56.0348146Z   AR      drivers/iio/counter/built-in.a
2026-05-03T01:25:56.0526524Z   AR      drivers/iio/dac/built-in.a
2026-05-03T01:25:56.0713779Z   AR      drivers/iio/dummy/built-in.a
2026-05-03T01:25:56.0882397Z   AR      drivers/iio/frequency/built-in.a
2026-05-03T01:25:56.1052958Z   AR      drivers/iio/gyro/built-in.a
2026-05-03T01:25:56.1222750Z   AR      drivers/iio/health/built-in.a
2026-05-03T01:25:56.1436737Z   AR      drivers/iio/humidity/built-in.a
2026-05-03T01:25:56.1656107Z   AR      drivers/iio/imu/bmi160/built-in.a
2026-05-03T01:25:56.1893965Z   AR      drivers/iio/imu/inv_mpu6050/built-in.a
2026-05-03T01:25:56.2040214Z   AR      drivers/iio/imu/st_lsm6dsx/built-in.a
2026-05-03T01:25:56.2190166Z   AR      drivers/iio/imu/built-in.a
2026-05-03T01:25:56.2364273Z   AR      drivers/iio/light/built-in.a
2026-05-03T01:25:56.2532897Z   AR      drivers/iio/magnetometer/built-in.a
2026-05-03T01:25:56.2698922Z   AR      drivers/iio/multiplexer/built-in.a
2026-05-03T01:25:56.2880290Z   AR      drivers/iio/orientation/built-in.a
2026-05-03T01:25:56.3090438Z   AR      drivers/iio/potentiometer/built-in.a
2026-05-03T01:25:56.3352743Z   AR      drivers/iio/potentiostat/built-in.a
2026-05-03T01:25:56.3626869Z   AR      drivers/iio/pressure/built-in.a
2026-05-03T01:25:56.3861334Z   AR      drivers/iio/proximity/built-in.a
2026-05-03T01:25:56.4020414Z   AR      drivers/iio/resolver/built-in.a
2026-05-03T01:25:56.4223797Z   AR      drivers/iio/temperature/built-in.a
2026-05-03T01:25:56.4396315Z   AR      drivers/iio/trigger/built-in.a
2026-05-03T01:25:56.4493461Z   CC      drivers/iio/industrialio-core.o
2026-05-03T01:25:56.4750345Z   CC      net/ipv4/ip_tunnel_core.o
2026-05-03T01:25:56.8587985Z   CC      net/ipv6/addrlabel.o
2026-05-03T01:25:57.3540570Z   CC      drivers/iio/industrialio-event.o
2026-05-03T01:25:57.7670518Z   CC      net/ipv6/route.o
2026-05-03T01:25:57.8460656Z   CC      net/ipv4/gre_offload.o
2026-05-03T01:25:57.8810378Z   CC      net/mac80211/status.o
2026-05-03T01:25:58.0910000Z   CC      drivers/iio/inkern.o
2026-05-03T01:25:58.7790399Z   CC      net/ipv4/metrics.o
2026-05-03T01:25:58.7940265Z   AR      drivers/iio/built-in.a
2026-05-03T01:25:58.8270376Z   CC      drivers/input/fingerprint/fpc/mtk_spi.o
2026-05-03T01:25:59.3291220Z ../drivers/input/fingerprint/fpc/mtk_spi.c:309:19: warning: mixing declarations and code is a C99 extension [-Wdeclaration-after-statement]
2026-05-03T01:25:59.3292621Z         struct fpc_data *fpc = dev_get_drvdata(device);
2026-05-03T01:25:59.3319916Z                          ^
2026-05-03T01:25:59.3970839Z 1 warning generated.
2026-05-03T01:25:59.4280524Z   AR      drivers/input/fingerprint/fpc/built-in.a
2026-05-03T01:25:59.4510436Z   CC      drivers/input/fingerprint/goodix/gf_spi_tee.o
2026-05-03T01:26:00.0652439Z   CC      net/ipv4/netlink.o
2026-05-03T01:26:00.0740666Z   CC      net/mac80211/driver-ops.o
2026-05-03T01:26:00.2090368Z   CC      net/ipv6/ip6_fib.o
2026-05-03T01:26:00.2281277Z ../drivers/input/fingerprint/goodix/gf_spi_tee.c:1175:19: warning: variable 'ms' set but not used [-Wunused-but-set-variable]
2026-05-03T01:26:00.2300014Z         struct mt_spi_t *ms = NULL;
2026-05-03T01:26:00.2329910Z                          ^
2026-05-03T01:26:00.2360525Z ../drivers/input/fingerprint/goodix/gf_spi_tee.c:1913:6: warning: mixing declarations and code is a C99 extension [-Wdeclaration-after-statement]
2026-05-03T01:26:00.2380600Z         int status = -EINVAL;
2026-05-03T01:26:00.2419887Z             ^
2026-05-03T01:26:00.2450221Z ../drivers/input/fingerprint/goodix/gf_spi_tee.c:2207:1: warning: unused label 'err' [-Wunused-label]
2026-05-03T01:26:00.2479842Z err:
2026-05-03T01:26:00.2509859Z ^~~~
2026-05-03T01:26:00.2540511Z ../drivers/input/fingerprint/goodix/gf_spi_tee.c:2281:6: warning: mixing declarations and code is a C99 extension [-Wdeclaration-after-statement]
2026-05-03T01:26:00.2569925Z         int status = -EINVAL;
2026-05-03T01:26:00.2599847Z             ^
2026-05-03T01:26:00.4132251Z 4 warnings generated.
2026-05-03T01:26:00.4520595Z   CC      drivers/input/fingerprint/goodix/gf_spi_factory.o
2026-05-03T01:26:01.0690913Z ../net/ipv6/ip6_fib.c:1632:6: warning: variable 'iter' set but not used [-Wunused-but-set-variable]
2026-05-03T01:26:01.0719941Z         int iter = 0;
2026-05-03T01:26:01.0720268Z             ^
2026-05-03T01:26:01.2751237Z   CC      net/ipv4/ip_tunnel.o
2026-05-03T01:26:01.2995743Z drivers/input/fingerprint/goodix/.tmp_gf_spi_factory.o: no symbols
2026-05-03T01:26:01.3050377Z   AR      drivers/input/fingerprint/goodix/built-in.a
2026-05-03T01:26:01.3172166Z   AR      drivers/input/fingerprint/built-in.a
2026-05-03T01:26:01.3361538Z   CC      drivers/input/joystick/xpad.o
2026-05-03T01:26:01.3740496Z 1 warning generated.
2026-05-03T01:26:01.5710603Z   CC      net/mac80211/sta_info.o
2026-05-03T01:26:01.8551509Z   CC      net/ipv6/ipv6_sockglue.o
2026-05-03T01:26:01.9032595Z   AR      drivers/input/joystick/built-in.a
2026-05-03T01:26:01.9380585Z   CC      drivers/input/keyboard/mediatek/mt6768/hal_kpd.o
2026-05-03T01:26:02.5660503Z   AR      drivers/input/keyboard/mediatek/mt6768/built-in.a
2026-05-03T01:26:02.5770315Z   CC      drivers/input/keyboard/mediatek/kpd.o
2026-05-03T01:26:02.8985604Z   CC      net/ipv4/sysctl_net_ipv4.o
2026-05-03T01:26:03.1764079Z   AR      drivers/input/keyboard/mediatek/built-in.a
2026-05-03T01:26:03.1867505Z   CC      drivers/input/keyboard/gpio_keys.o
2026-05-03T01:26:03.4156995Z   CC      net/ipv6/ndisc.o
2026-05-03T01:26:03.7793427Z   AR      drivers/input/keyboard/built-in.a
2026-05-03T01:26:03.7990264Z   CC      drivers/input/misc/uinput.o
2026-05-03T01:26:03.8632938Z   CC      net/ipv4/proc.o
2026-05-03T01:26:04.3610500Z   AR      drivers/input/misc/built-in.a
2026-05-03T01:26:04.3945796Z   CC      drivers/input/touchscreen/mediatek/NT36672C_SPI/nt36xxx.o
2026-05-03T01:26:04.4207864Z   CC      net/mac80211/wep.o
2026-05-03T01:26:04.8790520Z   CC      net/ipv6/udp.o
2026-05-03T01:26:04.8940385Z   CC      net/ipv4/fib_rules.o
2026-05-03T01:26:04.9150877Z ../drivers/input/touchscreen/mediatek/NT36672C_SPI/nt36xxx.c:229:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:26:04.9160097Z         int ret = 0;
2026-05-03T01:26:04.9209996Z             ^
2026-05-03T01:26:04.9491009Z ../drivers/input/touchscreen/mediatek/NT36672C_SPI/nt36xxx.c:1690:11: warning: variable 'pen_battery' set but not used [-Wunused-but-set-variable]
2026-05-03T01:26:04.9510142Z         uint32_t pen_battery = 0;
2026-05-03T01:26:04.9539975Z                  ^
2026-05-03T01:26:04.9550436Z ../drivers/input/touchscreen/mediatek/NT36672C_SPI/nt36xxx.c:2183:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:26:04.9570086Z         int ret;
2026-05-03T01:26:04.9600009Z             ^
2026-05-03T01:26:05.2160483Z 3 warnings generated.
2026-05-03T01:26:05.2510562Z   CC      drivers/input/touchscreen/mediatek/NT36672C_SPI/nt36xxx_fw_update.o
2026-05-03T01:26:05.3500387Z   CC      net/mac80211/aead_api.o
2026-05-03T01:26:05.7461172Z ../drivers/input/touchscreen/mediatek/NT36672C_SPI/nt36xxx_fw_update.c:589:8: warning: variable 'name' set but not used [-Wunused-but-set-variable]
2026-05-03T01:26:05.7520120Z         char *name;
2026-05-03T01:26:05.7549994Z               ^
2026-05-03T01:26:05.8650565Z   CC      net/mac80211/wpa.o
2026-05-03T01:26:05.8920268Z 1 warning generated.
2026-05-03T01:26:05.9220788Z   CC      drivers/input/touchscreen/mediatek/NT36672C_SPI/nt36xxx_ext_proc.o
2026-05-03T01:26:06.2773142Z   CC      net/ipv4/ipmr.o
2026-05-03T01:26:06.4645573Z   CC      drivers/input/touchscreen/mediatek/NT36672C_SPI/nt36xxx_mp_ctrlram.o
2026-05-03T01:26:06.8222522Z   CC      net/ipv6/udplite.o
2026-05-03T01:26:06.9050405Z   CC      net/mac80211/scan.o
2026-05-03T01:26:07.3530807Z   AR      drivers/input/touchscreen/mediatek/NT36672C_SPI/built-in.a
2026-05-03T01:26:07.3880889Z   CC      drivers/input/touchscreen/mediatek/focaltech_FT8720/focaltech_test/supported_ic/focaltech_test_ft8720.o
2026-05-03T01:26:07.7181546Z   CC      net/ipv6/raw.o
2026-05-03T01:26:08.0300440Z   AR      drivers/input/touchscreen/mediatek/focaltech_FT8720/focaltech_test/supported_ic/built-in.a
2026-05-03T01:26:08.0360414Z   CC      drivers/input/touchscreen/mediatek/focaltech_FT8720/focaltech_test/focaltech_test.o
2026-05-03T01:26:08.3890390Z   CC      net/ipv4/ipmr_base.o
2026-05-03T01:26:09.1490852Z   CC      net/mac80211/offchannel.o
2026-05-03T01:26:09.3530920Z   CC      net/ipv6/icmp.o
2026-05-03T01:26:09.4241589Z   CC      drivers/input/touchscreen/mediatek/focaltech_FT8720/focaltech_test/focaltech_test_ini.o
2026-05-03T01:26:09.8346813Z   CC      net/ipv4/ipip.o
2026-05-03T01:26:10.3571002Z   AR      drivers/input/touchscreen/mediatek/focaltech_FT8720/focaltech_test/built-in.a
2026-05-03T01:26:10.3680492Z   CC      drivers/input/touchscreen/mediatek/focaltech_FT8720/focaltech_core.o
2026-05-03T01:26:10.8151179Z ../drivers/input/touchscreen/mediatek/focaltech_FT8720/focaltech_core.c:130:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:26:10.8179934Z         int ret;
2026-05-03T01:26:10.8218992Z             ^
2026-05-03T01:26:10.8240137Z   CC      net/ipv4/gre_demux.o
2026-05-03T01:26:10.9311268Z   CC      net/ipv6/mcast.o
2026-05-03T01:26:11.0478370Z 1 warning generated.
2026-05-03T01:26:11.0880768Z   CC      drivers/input/touchscreen/mediatek/focaltech_FT8720/focaltech_ex_fun.o
2026-05-03T01:26:11.1720544Z   CC      net/mac80211/ht.o
2026-05-03T01:26:11.8349295Z   CC      drivers/input/touchscreen/mediatek/focaltech_FT8720/focaltech_ex_mode.o
2026-05-03T01:26:12.2690397Z   CC      net/ipv4/udp_tunnel.o
2026-05-03T01:26:12.4136075Z   CC      drivers/input/touchscreen/mediatek/focaltech_FT8720/focaltech_gesture.o
2026-05-03T01:26:12.7760488Z   CC      net/ipv6/reassembly.o
2026-05-03T01:26:12.9370796Z   CC      drivers/input/touchscreen/mediatek/focaltech_FT8720/focaltech_esdcheck.o
2026-05-03T01:26:13.1040598Z   CC      net/mac80211/agg-tx.o
2026-05-03T01:26:13.5353062Z   CC      net/ipv4/ip_vti.o
2026-05-03T01:26:13.5584729Z   CC      drivers/input/touchscreen/mediatek/focaltech_FT8720/focaltech_point_report_check.o
2026-05-03T01:26:13.9151323Z   CC      net/ipv6/tcp_ipv6.o
2026-05-03T01:26:14.0900843Z   CC      drivers/input/touchscreen/mediatek/focaltech_FT8720/focaltech_proximity.o
2026-05-03T01:26:14.5980379Z   CC      net/ipv4/syncookies.o
2026-05-03T01:26:14.7060803Z   CC      drivers/input/touchscreen/mediatek/focaltech_FT8720/focaltech_flash.o
2026-05-03T01:26:15.1220533Z   CC      net/mac80211/agg-rx.o
2026-05-03T01:26:15.1461970Z   CC      net/ipv6/ping.o
2026-05-03T01:26:15.4690760Z   CC      drivers/input/touchscreen/mediatek/focaltech_FT8720/focaltech_spi.o
2026-05-03T01:26:16.0238897Z   CC      net/ipv4/ah4.o
2026-05-03T01:26:16.0500309Z   AR      drivers/input/touchscreen/mediatek/focaltech_FT8720/built-in.a
2026-05-03T01:26:16.0697484Z   CC      drivers/input/touchscreen/mediatek/xiaomi/xiaomi_touch.o
2026-05-03T01:26:16.4851981Z ../drivers/input/touchscreen/mediatek/xiaomi/xiaomi_touch.c:183:23: warning: variable 'dev' set but not used [-Wunused-but-set-variable]
2026-05-03T01:26:16.4880152Z         struct xiaomi_touch *dev = NULL;
2026-05-03T01:26:16.4910022Z                              ^
2026-05-03T01:26:16.5200238Z   CC      net/ipv6/exthdrs.o
2026-05-03T01:26:16.5340229Z 1 warning generated.
2026-05-03T01:26:16.5633840Z   AR      drivers/input/touchscreen/mediatek/xiaomi/built-in.a
2026-05-03T01:26:16.5730252Z   CC      drivers/input/touchscreen/mediatek/mtk_tpd.o
2026-05-03T01:26:17.0641206Z   CC      net/ipv4/esp4.o
2026-05-03T01:26:17.0670088Z   CC      net/mac80211/vht.o
2026-05-03T01:26:17.1960430Z   CC      drivers/input/touchscreen/mediatek/tpd_button.o
2026-05-03T01:26:17.6840862Z   CC      drivers/input/touchscreen/mediatek/tpd_calibrate.o
2026-05-03T01:26:18.0960535Z   CC      net/ipv6/datagram.o
2026-05-03T01:26:18.1291230Z   CC      drivers/input/touchscreen/mediatek/tpd_debug.o
2026-05-03T01:26:18.6230623Z   CC      net/ipv4/ipcomp.o
2026-05-03T01:26:18.9845048Z   CC      net/mac80211/he.o
2026-05-03T01:26:19.0301133Z   CC      drivers/input/touchscreen/mediatek/tpd_default.o
2026-05-03T01:26:19.4270668Z   CC      net/ipv6/ip6_flowlabel.o
2026-05-03T01:26:19.4680798Z   CC      drivers/input/touchscreen/mediatek/tpd_misc.o
2026-05-03T01:26:19.4750290Z   CC      net/ipv4/xfrm4_tunnel.o
2026-05-03T01:26:19.8730547Z   CC      net/mac80211/ibss.o
2026-05-03T01:26:20.1650960Z   CC      drivers/input/touchscreen/mediatek/tpd_setting.o
2026-05-03T01:26:20.3260551Z   CC      net/ipv4/xfrm4_mode_beet.o
2026-05-03T01:26:20.6150656Z   CC      drivers/input/touchscreen/mediatek/tpd_notify.o
2026-05-03T01:26:20.8578881Z   CC      net/ipv6/inet6_connection_sock.o
2026-05-03T01:26:21.2490874Z   CC      net/ipv4/tunnel4.o
2026-05-03T01:26:21.3710147Z   AR      drivers/input/touchscreen/mediatek/built-in.a
2026-05-03T01:26:21.3856973Z   CC      drivers/input/touchscreen/of_touchscreen.o
2026-05-03T01:26:21.4010864Z   CC      net/mac80211/iface.o
2026-05-03T01:26:21.9801339Z   AR      drivers/input/touchscreen/built-in.a
2026-05-03T01:26:21.9980515Z   CC      drivers/input/input.o
2026-05-03T01:26:22.1320755Z   CC      net/ipv6/udp_offload.o
2026-05-03T01:26:22.6056458Z   CC      net/ipv4/xfrm4_mode_transport.o
2026-05-03T01:26:22.9430424Z   CC      drivers/input/input-compat.o
2026-05-03T01:26:23.0670492Z   CC      net/ipv6/seg6.o
2026-05-03T01:26:23.0690547Z   CC      net/mac80211/rate.o
2026-05-03T01:26:23.4600524Z   CC      net/ipv4/xfrm4_mode_tunnel.o
2026-05-03T01:26:23.5620218Z   CC      drivers/input/input-mt.o
2026-05-03T01:26:24.0010668Z   CC      net/ipv6/fib6_notifier.o
2026-05-03T01:26:24.3340486Z   CC      drivers/input/ff-core.o
2026-05-03T01:26:24.3610665Z   CC      net/ipv4/ipconfig.o
2026-05-03T01:26:24.8366457Z   CC      net/ipv6/sysctl_net_ipv6.o
2026-05-03T01:26:24.9820389Z   CC      drivers/input/input-leds.o
2026-05-03T01:26:25.2732656Z   CC      net/mac80211/michael.o
2026-05-03T01:26:25.3570576Z   CC      drivers/input/evdev.o
2026-05-03T01:26:25.5130561Z   CC      net/ipv4/netfilter.o
2026-05-03T01:26:25.7120443Z   CC      net/ipv6/ip6mr.o
2026-05-03T01:26:25.9485552Z   CC      net/mac80211/tkip.o
2026-05-03T01:26:26.1751810Z   AR      drivers/input/built-in.a
2026-05-03T01:26:26.2100493Z   CC      drivers/iommu/iommu.o
2026-05-03T01:26:26.8830510Z   CC      net/ipv4/inet_diag.o
2026-05-03T01:26:27.3170569Z   CC      drivers/iommu/iommu-traces.o
2026-05-03T01:26:27.6960559Z   CC      net/ipv6/xfrm6_policy.o
2026-05-03T01:26:27.9667475Z   CC      net/mac80211/aes_cmac.o
2026-05-03T01:26:28.2509791Z   CC      drivers/iommu/iommu-sysfs.o
2026-05-03T01:26:28.3280390Z   CC      net/ipv4/tcp_diag.o
2026-05-03T01:26:28.5622443Z   CC      net/ipv6/xfrm6_state.o
2026-05-03T01:26:28.8232672Z   CC      net/mac80211/aes_gmac.o
2026-05-03T01:26:28.9841252Z   CC      drivers/iommu/dma-iommu.o
2026-05-03T01:26:29.2576063Z   CC      net/ipv4/udp_diag.o
2026-05-03T01:26:29.5210842Z   CC      net/ipv6/xfrm6_input.o
2026-05-03T01:26:29.5251027Z ../drivers/iommu/dma-iommu.c:1130:9: warning: variable 'map_len' set but not used [-Wunused-but-set-variable]
2026-05-03T01:26:29.5271342Z         size_t map_len = 0;
2026-05-03T01:26:29.5310024Z                ^
2026-05-03T01:26:29.5340401Z ../drivers/iommu/dma-iommu.c:1128:26: warning: variable 'prev' set but not used [-Wunused-but-set-variable]
2026-05-03T01:26:29.5360039Z         struct scatterlist *s, *prev = NULL;
2026-05-03T01:26:29.5369892Z                                 ^
2026-05-03T01:26:29.5400329Z ../drivers/iommu/dma-iommu.c:1129:9: warning: variable 'iova_len' set but not used [-Wunused-but-set-variable]
2026-05-03T01:26:29.5420040Z         size_t iova_len = 0;
2026-05-03T01:26:29.5429911Z                ^
2026-05-03T01:26:29.6790704Z 3 warnings generated.
2026-05-03T01:26:29.7420632Z   CC      net/mac80211/fils_aead.o
2026-05-03T01:26:29.9808513Z   CC      drivers/iommu/iova.o
2026-05-03T01:26:30.1400572Z   CC      net/ipv4/tcp_bbr.o
2026-05-03T01:26:30.8201066Z   CC      net/mac80211/cfg.o
2026-05-03T01:26:30.8700579Z   CC      drivers/iommu/of_iommu.o
2026-05-03T01:26:30.8910656Z   CC      net/ipv6/xfrm6_output.o
2026-05-03T01:26:31.2410585Z   CC      net/ipv4/tcp_bic.o
2026-05-03T01:26:31.6750575Z   AR      drivers/iommu/built-in.a
2026-05-03T01:26:31.7040343Z   CC      drivers/irqchip/irqchip.o
2026-05-03T01:26:32.0603994Z   CC      drivers/irqchip/irq-gic.o
2026-05-03T01:26:32.1244803Z   CC      net/ipv4/tcp_cubic.o
2026-05-03T01:26:32.2980801Z   CC      net/ipv6/xfrm6_protocol.o
2026-05-03T01:26:32.5970396Z   CC      drivers/irqchip/irq-gic-common.o
2026-05-03T01:26:32.9823227Z   CC      drivers/irqchip/irq-gic-v3.o
2026-05-03T01:26:33.0510588Z   CC      net/ipv4/xfrm4_policy.o
2026-05-03T01:26:33.4308984Z   CC      net/mac80211/ethtool.o
2026-05-03T01:26:33.6760370Z   CC      net/ipv6/netfilter.o
2026-05-03T01:26:33.7080366Z   CC      drivers/irqchip/irq-gic-v3-mbi.o
2026-05-03T01:26:33.8748914Z   CC      net/ipv4/xfrm4_state.o
2026-05-03T01:26:34.3611492Z   CC      drivers/irqchip/irq-gic-v3-its.o
2026-05-03T01:26:34.7950825Z   CC      net/ipv4/xfrm4_input.o
2026-05-03T01:26:34.8410671Z   CC      net/mac80211/rx.o
2026-05-03T01:26:35.0628522Z   CC      net/ipv6/fib6_rules.o
2026-05-03T01:26:35.7390635Z   CC      drivers/irqchip/irq-gic-v3-its-platform-msi.o
2026-05-03T01:26:36.1160409Z   CC      net/ipv4/xfrm4_output.o
2026-05-03T01:26:36.1670538Z   CC      drivers/irqchip/irq-gic-v4.o
2026-05-03T01:26:36.3790452Z   CC      net/ipv6/proc.o
2026-05-03T01:26:36.5030561Z   CC      drivers/irqchip/irq-partition-percpu.o
2026-05-03T01:26:37.0756249Z   CC      drivers/irqchip/irq-mtk-sysirq.o
2026-05-03T01:26:37.3040635Z   CC      net/ipv6/syncookies.o
2026-05-03T01:26:37.4816649Z   CC      net/ipv4/xfrm4_protocol.o
2026-05-03T01:26:37.5050512Z   CC      drivers/irqchip/irq-mtk-cirq.o
2026-05-03T01:26:37.5590588Z   CC      net/mac80211/spectmgmt.o
2026-05-03T01:26:37.9553756Z   AR      drivers/irqchip/built-in.a
2026-05-03T01:26:38.0258370Z -- KernelSU-Next Git repo detected at: /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/KernelSU-Next
2026-05-03T01:26:38.0301996Z -- KernelSU-Next version: 33132
2026-05-03T01:26:38.0357737Z -- KernelSU-Next tag: v3.2.0-legacy
2026-05-03T01:26:38.0380715Z -- KernelSU-Next Manager signature size: 0x3e6
2026-05-03T01:26:38.0387565Z -- KernelSU-Next Manager signature hash: 79e590113c4c4c0c222978e413a5faa801666957b1212a328e46c00c69821bf7
2026-05-03T01:26:38.0398680Z -- KernelSU-Next: Hook mode: Manual
2026-05-03T01:26:38.1050499Z   CC      drivers/kernelsu/core/init.o
2026-05-03T01:26:38.5471720Z   CC      net/mac80211/tx.o
2026-05-03T01:26:38.6540373Z   CC      net/ipv6/ah6.o
2026-05-03T01:26:38.8889250Z   AR      net/ipv4/built-in.a
2026-05-03T01:26:38.9290531Z   CC      drivers/kernelsu/compat/kernel_compat.o
2026-05-03T01:26:38.9910636Z   CC      net/netfilter/ipset/ip_set_core.o
2026-05-03T01:26:39.7203843Z   CC      net/ipv6/esp6.o
2026-05-03T01:26:39.7846696Z   CC      drivers/kernelsu/feature/kernel_umount.o
2026-05-03T01:26:40.6480799Z   CC      drivers/kernelsu/feature/sucompat.o
2026-05-03T01:26:40.6510306Z   CC      net/netfilter/ipset/ip_set_getport.o
2026-05-03T01:26:41.3030703Z   CC      net/ipv6/ipcomp6.o
2026-05-03T01:26:41.3570400Z   CC      net/mac80211/key.o
2026-05-03T01:26:41.6250641Z   CC      drivers/kernelsu/hook/hook_manager.o
2026-05-03T01:26:41.8470670Z   CC      drivers/kernelsu/hook/lsm_hooks.o
2026-05-03T01:26:41.9653086Z   CC      net/netfilter/ipset/pfxlen.o
2026-05-03T01:26:42.2450426Z   CC      net/ipv6/xfrm6_tunnel.o
2026-05-03T01:26:42.7045826Z   CC      drivers/kernelsu/hook/setuid_hook.o
2026-05-03T01:26:43.3771933Z   CC      net/netfilter/ipset/ip_set_bitmap_ip.o
2026-05-03T01:26:43.5400636Z   CC      drivers/kernelsu/extras.o
2026-05-03T01:26:43.5915677Z   CC      net/ipv6/tunnel6.o
2026-05-03T01:26:43.6390348Z   CC      net/mac80211/util.o
2026-05-03T01:26:43.9800580Z   CC      drivers/kernelsu/tiny_sulog.o
2026-05-03T01:26:44.3240649Z   CC      drivers/kernelsu/infra/file_wrapper.o
2026-05-03T01:26:44.4260749Z   CC      net/netfilter/ipset/ip_set_bitmap_ipmac.o
2026-05-03T01:26:44.9570721Z   CC      net/ipv6/xfrm6_mode_transport.o
2026-05-03T01:26:45.3270642Z   CC      drivers/kernelsu/infra/seccomp_cache.o
2026-05-03T01:26:45.3610544Z drivers/kernelsu/infra/.tmp_seccomp_cache.o: no symbols
2026-05-03T01:26:45.3660132Z   CC      drivers/kernelsu/infra/su_mount_ns.o
2026-05-03T01:26:45.4990733Z   CC      net/netfilter/ipset/ip_set_bitmap_port.o
2026-05-03T01:26:45.8820541Z   CC      net/ipv6/xfrm6_mode_tunnel.o
2026-05-03T01:26:46.2931034Z   CC      drivers/kernelsu/manager/apk_sign.o
2026-05-03T01:26:46.2950360Z   CC      net/mac80211/wme.o
2026-05-03T01:26:46.4130622Z   CC      net/netfilter/ipset/ip_set_hash_ip.o
2026-05-03T01:26:46.7589912Z   CC      net/ipv6/xfrm6_mode_ro.o
2026-05-03T01:26:47.2505711Z   CC      drivers/kernelsu/manager/throne_tracker.o
2026-05-03T01:26:47.3380462Z   CC      net/mac80211/chan.o
2026-05-03T01:26:47.6670736Z   CC      net/ipv6/xfrm6_mode_beet.o
2026-05-03T01:26:47.9108731Z   CC      net/netfilter/ipset/ip_set_hash_ipmac.o
2026-05-03T01:26:48.1430654Z   CC      drivers/kernelsu/manager/pkg_observer.o
2026-05-03T01:26:48.4891171Z ../drivers/kernelsu/manager/pkg_observer.c:130:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:26:48.4899872Z         int ret = 0;
2026-05-03T01:26:48.4930032Z             ^
2026-05-03T01:26:48.5200199Z 1 warning generated.
2026-05-03T01:26:48.5470419Z   CC      drivers/kernelsu/policy/allowlist.o
2026-05-03T01:26:48.5950612Z   CC      net/ipv6/mip6.o
2026-05-03T01:26:49.3890653Z   CC      net/netfilter/ipset/ip_set_hash_ipmark.o
2026-05-03T01:26:49.5688217Z   CC      net/ipv6/ip6_vti.o
2026-05-03T01:26:49.5722062Z   CC      drivers/kernelsu/policy/app_profile.o
2026-05-03T01:26:49.7268467Z   CC      net/mac80211/trace.o
2026-05-03T01:26:50.5700686Z   CC      drivers/kernelsu/policy/feature.o
2026-05-03T01:26:50.7324823Z   CC      drivers/kernelsu/runtime/boot_event.o
2026-05-03T01:26:50.7390328Z   CC      net/ipv6/sit.o
2026-05-03T01:26:50.8430657Z   CC      net/netfilter/ipset/ip_set_hash_ipport.o
2026-05-03T01:26:51.0682509Z   CC      drivers/kernelsu/runtime/ksud_integration.o
2026-05-03T01:26:52.1002597Z   CC      drivers/kernelsu/selinux/selinux.o
2026-05-03T01:26:52.1910474Z   CC      net/ipv6/ip6_tunnel.o
2026-05-03T01:26:52.3865938Z   CC      net/netfilter/ipset/ip_set_hash_ipportip.o
2026-05-03T01:26:52.4270661Z   CC      net/mac80211/mlme.o
2026-05-03T01:26:53.0150692Z   CC      drivers/kernelsu/selinux/rules.o
2026-05-03T01:26:53.9115759Z   CC      net/netfilter/ipset/ip_set_hash_ipportnet.o
2026-05-03T01:26:54.0010552Z   CC      net/ipv6/addrconf_core.o
2026-05-03T01:26:54.0220633Z   CC      drivers/kernelsu/selinux/sepolicy.o
2026-05-03T01:26:54.9416332Z   CC      drivers/kernelsu/supercall/dispatch.o
2026-05-03T01:26:55.3680794Z   CC      net/ipv6/exthdrs_core.o
2026-05-03T01:26:55.4513230Z   CC      net/mac80211/tdls.o
2026-05-03T01:26:55.5320615Z   CC      net/netfilter/ipset/ip_set_hash_mac.o
2026-05-03T01:26:55.9320813Z   CC      drivers/kernelsu/supercall/perm.o
2026-05-03T01:26:56.2278993Z   CC      drivers/kernelsu/supercall/supercall.o
2026-05-03T01:26:56.6570436Z   CC      net/ipv6/ip6_checksum.o
2026-05-03T01:26:56.7104454Z   CC      net/netfilter/ipset/ip_set_hash_net.o
2026-05-03T01:26:56.7330866Z   AR      drivers/kernelsu/built-in.a
2026-05-03T01:26:56.7590366Z   CC      drivers/leds/trigger/ledtrig-timer.o
2026-05-03T01:26:57.0858750Z   AR      drivers/leds/trigger/built-in.a
2026-05-03T01:26:57.0970376Z   CC      drivers/leds/led-core.o
2026-05-03T01:26:57.6141062Z   CC      drivers/leds/led-class.o
2026-05-03T01:26:57.7820702Z   CC      net/mac80211/ocb.o
2026-05-03T01:26:57.9277354Z   CC      net/ipv6/ip6_icmp.o
2026-05-03T01:26:58.0891122Z   CC      drivers/leds/led-triggers.o
2026-05-03T01:26:58.2810632Z   CC      net/netfilter/ipset/ip_set_hash_netport.o
2026-05-03T01:26:58.6310214Z   AR      drivers/leds/built-in.a
2026-05-03T01:26:58.6508517Z   AR      drivers/macintosh/built-in.a
2026-05-03T01:26:58.6703419Z   CC      drivers/mailbox/mailbox.o
2026-05-03T01:26:59.0570241Z   CC      net/mac80211/led.o
2026-05-03T01:26:59.2730405Z   CC      net/ipv6/output_core.o
2026-05-03T01:26:59.2770157Z   CC      drivers/mailbox/mtk-cmdq-mailbox.o
2026-05-03T01:26:59.8998143Z ../drivers/mailbox/mtk-cmdq-mailbox.c:1360:20: warning: variable 'prefetch' set but not used [-Wunused-but-set-variable]
2026-05-03T01:26:59.9030613Z                 wait_token, cfg, prefetch, pri = 0;
2026-05-03T01:26:59.9059912Z                                  ^
2026-05-03T01:26:59.9089967Z   CC      net/netfilter/ipset/ip_set_hash_netiface.o
2026-05-03T01:26:59.9360761Z ../drivers/mailbox/mtk-cmdq-mailbox.c:2371:6: warning: variable 'tmp_num' set but not used [-Wunused-but-set-variable]
2026-05-03T01:26:59.9390007Z         u32 tmp_num = 0;
2026-05-03T01:26:59.9419973Z             ^
2026-05-03T01:27:00.2100404Z 2 warnings generated.
2026-05-03T01:27:00.5160407Z   CC      net/mac80211/pm.o
2026-05-03T01:27:00.5430363Z   AR      drivers/mailbox/built-in.a
2026-05-03T01:27:00.5650330Z   CC      drivers/md/dm-uevent.o
2026-05-03T01:27:00.6040354Z   CC      net/ipv6/protocol.o
2026-05-03T01:27:01.4210611Z   CC      drivers/md/dm.o
2026-05-03T01:27:01.4990539Z   CC      net/netfilter/ipset/ip_set_hash_netnet.o
2026-05-03T01:27:01.8488760Z   CC      net/ipv6/ip6_offload.o
2026-05-03T01:27:02.4610513Z   CC      net/mac80211/rc80211_minstrel.o
2026-05-03T01:27:02.6280361Z   CC      net/ipv6/tcpv6_offload.o
2026-05-03T01:27:02.7990516Z   CC      drivers/md/dm-table.o
2026-05-03T01:27:03.4335493Z   CC      net/netfilter/ipset/ip_set_hash_netportnet.o
2026-05-03T01:27:03.5980513Z   CC      net/ipv6/exthdrs_offload.o
2026-05-03T01:27:03.9170006Z   CC      net/mac80211/rc80211_minstrel_ht.o
2026-05-03T01:27:04.0440531Z   CC      drivers/md/dm-target.o
2026-05-03T01:27:04.4392647Z   CC      net/ipv6/inet6_hashtables.o
2026-05-03T01:27:05.0326237Z   CC      drivers/md/dm-linear.o
2026-05-03T01:27:05.4950524Z   AR      net/mac80211/built-in.a
2026-05-03T01:27:05.5500606Z   AR      drivers/media/common/b2c2/built-in.a
2026-05-03T01:27:05.5660340Z   AR      drivers/media/common/saa7146/built-in.a
2026-05-03T01:27:05.5885283Z   AR      drivers/media/common/siano/built-in.a
2026-05-03T01:27:05.5950815Z   CC      drivers/md/dm-stripe.o
2026-05-03T01:27:05.6050258Z   AR      drivers/media/common/v4l2-tpg/built-in.a
2026-05-03T01:27:05.6250586Z   CC      drivers/media/common/videobuf2/videobuf2-core.o
2026-05-03T01:27:05.8280539Z   CC      net/ipv6/ip6_udp_tunnel.o
2026-05-03T01:27:05.9240742Z   CC      net/netfilter/ipset/ip_set_list_set.o
2026-05-03T01:27:06.1950481Z   CC      drivers/md/dm-ioctl.o
2026-05-03T01:27:06.7750560Z   CC      drivers/media/common/videobuf2/vb2-trace.o
2026-05-03T01:27:06.9547886Z   AR      net/netfilter/ipset/built-in.a
2026-05-03T01:27:06.9717786Z   CC      net/netfilter/core.o
2026-05-03T01:27:07.1330255Z   CC      drivers/md/dm-io.o
2026-05-03T01:27:07.1930318Z   CC      net/ipv6/mcast_snoop.o
2026-05-03T01:27:07.6173960Z   CC      drivers/media/common/videobuf2/videobuf2-v4l2.o
2026-05-03T01:27:08.1860831Z   CC      drivers/md/dm-kcopyd.o
2026-05-03T01:27:08.2868739Z   CC      net/netfilter/nf_log.o
2026-05-03T01:27:08.3979801Z   AR      net/ipv6/built-in.a
2026-05-03T01:27:08.4960169Z   AR      drivers/memory/mediatek/built-in.a
2026-05-03T01:27:08.5040384Z   CC      drivers/media/common/videobuf2/videobuf2-memops.o
2026-05-03T01:27:08.5041249Z   CC      drivers/memory/mtk-smi.o
2026-05-03T01:27:09.1081047Z   AR      drivers/memory/built-in.a
2026-05-03T01:27:09.1200904Z   CC      drivers/md/dm-sysfs.o
2026-05-03T01:27:09.2520721Z   CC      drivers/media/common/videobuf2/videobuf2-dma-contig.o
2026-05-03T01:27:09.3080574Z   CC      net/netfilter/nf_queue.o
2026-05-03T01:27:09.6397684Z   AR      drivers/media/firewire/built-in.a
2026-05-03T01:27:09.6600116Z   CC      net/netlink/af_netlink.o
2026-05-03T01:27:09.7891282Z   CC      drivers/md/dm-stats.o
2026-05-03T01:27:10.1188709Z   AR      drivers/media/common/videobuf2/built-in.a
2026-05-03T01:27:10.1380223Z   AR      drivers/media/common/built-in.a
2026-05-03T01:27:10.1630900Z   AR      drivers/media/i2c/soc_camera/built-in.a
2026-05-03T01:27:10.1780299Z   AR      drivers/media/i2c/built-in.a
2026-05-03T01:27:10.2007165Z   AR      drivers/media/mmc/siano/built-in.a
2026-05-03T01:27:10.2170409Z   AR      drivers/media/mmc/built-in.a
2026-05-03T01:27:10.2397782Z   AR      drivers/media/pci/b2c2/built-in.a
2026-05-03T01:27:10.2580915Z   AR      drivers/media/pci/ddbridge/built-in.a
2026-05-03T01:27:10.2730290Z   AR      drivers/media/pci/dm1105/built-in.a
2026-05-03T01:27:10.3120541Z   AR      drivers/media/pci/intel/ipu3/built-in.a
2026-05-03T01:27:10.3390617Z   AR      drivers/media/pci/intel/built-in.a
2026-05-03T01:27:10.3580556Z   AR      drivers/media/pci/mantis/built-in.a
2026-05-03T01:27:10.3780475Z   AR      drivers/media/pci/netup_unidvb/built-in.a
2026-05-03T01:27:10.3930502Z   AR      drivers/media/pci/ngene/built-in.a
2026-05-03T01:27:10.4110341Z   AR      drivers/media/pci/pluto2/built-in.a
2026-05-03T01:27:10.4290323Z   AR      drivers/media/pci/pt1/built-in.a
2026-05-03T01:27:10.4440374Z   AR      drivers/media/pci/pt3/built-in.a
2026-05-03T01:27:10.4590289Z   AR      drivers/media/pci/saa7146/built-in.a
2026-05-03T01:27:10.4665430Z   CC      net/netfilter/nf_sockopt.o
2026-05-03T01:27:10.4767205Z   AR      drivers/media/pci/smipcie/built-in.a
2026-05-03T01:27:10.4956261Z   AR      drivers/media/pci/ttpci/built-in.a
2026-05-03T01:27:10.5270880Z   AR      drivers/media/pci/built-in.a
2026-05-03T01:27:10.5502530Z   AR      drivers/media/platform/cros-ec-cec/built-in.a
2026-05-03T01:27:10.5683484Z   AR      drivers/media/platform/davinci/built-in.a
2026-05-03T01:27:10.5840333Z   AR      drivers/media/platform/meson/built-in.a
2026-05-03T01:27:10.6060500Z   CC      drivers/media/platform/mtk-vcodec/mtk_vcodec_dec_drv.o
2026-05-03T01:27:10.7150644Z   CC      drivers/md/dm-rq.o
2026-05-03T01:27:11.2981183Z   CC      drivers/media/platform/mtk-vcodec/vdec_drv_if.o
2026-05-03T01:27:11.7070425Z   CC      net/netfilter/utils.o
2026-05-03T01:27:11.7627767Z   CC      net/netlink/genetlink.o
2026-05-03T01:27:11.7833476Z   CC      drivers/md/dm-builtin.o
2026-05-03T01:27:12.0535870Z   CC      drivers/media/platform/mtk-vcodec/mtk_vcodec_dec.o
2026-05-03T01:27:12.6119860Z ../drivers/media/platform/mtk-vcodec/mtk_vcodec_dec.c:980:27: warning: variable 'vb2_v4l2' set but not used [-Wunused-but-set-variable]
2026-05-03T01:27:12.6120904Z                 struct vb2_v4l2_buffer *vb2_v4l2 = NULL;
2026-05-03T01:27:12.6121345Z                                         ^
2026-05-03T01:27:12.7772293Z   CC      drivers/md/dm-bufio.o
2026-05-03T01:27:12.8934360Z 1 warning generated.
2026-05-03T01:27:12.9260556Z   CC      drivers/media/platform/mtk-vcodec/mt6768/mtk_vcodec_dec_pm.o
2026-05-03T01:27:12.9970448Z   CC      net/netfilter/nfnetlink.o
2026-05-03T01:27:13.1441239Z   AR      net/netlink/built-in.a
2026-05-03T01:27:13.1670250Z   CC      drivers/mfd/mfd-core.o
2026-05-03T01:27:13.4640992Z ../drivers/media/platform/mtk-vcodec/mt6768/mtk_vcodec_dec_pm.c:336:7: warning: variable 'emi_bw_output' set but not used [-Wunused-but-set-variable]
2026-05-03T01:27:13.4680092Z         long emi_bw_output = 0;
2026-05-03T01:27:13.4709858Z              ^
2026-05-03T01:27:13.4740547Z ../drivers/media/platform/mtk-vcodec/mt6768/mtk_vcodec_dec_pm.c:332:6: warning: variable 'b_freq_idx' set but not used [-Wunused-but-set-variable]
2026-05-03T01:27:13.4769946Z         int b_freq_idx = 0;
2026-05-03T01:27:13.4799864Z             ^
2026-05-03T01:27:13.4830524Z ../drivers/media/platform/mtk-vcodec/mt6768/mtk_vcodec_dec_pm.c:335:7: warning: variable 'emi_bw_input' set but not used [-Wunused-but-set-variable]
2026-05-03T01:27:13.4859892Z         long emi_bw_input = 0;
2026-05-03T01:27:13.4889839Z              ^
2026-05-03T01:27:13.5010077Z 3 warnings generated.
2026-05-03T01:27:13.5310681Z   CC      drivers/media/platform/mtk-vcodec/vdec/vdec_common_if.o
2026-05-03T01:27:13.7700685Z   CC      drivers/mfd/ti-lmu.o
2026-05-03T01:27:13.7880273Z   CC      drivers/md/dm-crypt.o
2026-05-03T01:27:14.1540472Z   CC      drivers/media/platform/mtk-vcodec/vdec/vdec_log_if.o
2026-05-03T01:27:14.2495436Z   CC      drivers/mfd/syscon.o
2026-05-03T01:27:14.3130841Z   CC      net/netfilter/nfnetlink_queue.o
2026-05-03T01:27:14.6960605Z   CC      drivers/media/platform/mtk-vcodec/vdec_vcu_if.o
2026-05-03T01:27:14.8700421Z   CC      drivers/mfd/mt6358-core.o
2026-05-03T01:27:15.1801101Z   CC      drivers/md/dm-default-key.o
2026-05-03T01:27:15.3140551Z   CC      drivers/media/platform/mtk-vcodec/mtk_vcodec_enc.o
2026-05-03T01:27:15.5060618Z   CC      net/netfilter/nfnetlink_log.o
2026-05-03T01:27:15.5870542Z   CC      drivers/mfd/mt635x-ot-debug.o
2026-05-03T01:27:15.7650693Z   CC      drivers/md/dm-snap.o
2026-05-03T01:27:15.8531290Z ../drivers/media/platform/mtk-vcodec/mtk_vcodec_enc.c:2394:14: warning: variable 'length' set but not used [-Wunused-but-set-variable]
2026-05-03T01:27:15.8560161Z         int ret, i, length;
2026-05-03T01:27:15.8589896Z                     ^
2026-05-03T01:27:15.8590801Z ../drivers/media/platform/mtk-vcodec/mtk_vcodec_enc.c:2727:20: warning: variable 'ctrl' set but not used [-Wunused-but-set-variable]
2026-05-03T01:27:15.8620070Z         struct v4l2_ctrl *ctrl;
2026-05-03T01:27:15.8650007Z                           ^
2026-05-03T01:27:16.1590351Z 2 warnings generated.
2026-05-03T01:27:16.1740330Z   CC      drivers/mfd/mt6358-misc.o
2026-05-03T01:27:16.1941142Z   CC      drivers/media/platform/mtk-vcodec/mtk_vcodec_enc_drv.o
2026-05-03T01:27:16.5710573Z   CC      net/netfilter/nf_conntrack_core.o
2026-05-03T01:27:16.8900657Z   CC      drivers/media/platform/mtk-vcodec/mt6768/mtk_vcodec_enc_pm.o
2026-05-03T01:27:16.9610455Z   CC      drivers/md/dm-exception-store.o
2026-05-03T01:27:16.9820370Z   AR      drivers/mfd/built-in.a
2026-05-03T01:27:16.9980410Z   CC      drivers/media/platform/mtk-vcodec/venc_drv_if.o
2026-05-03T01:27:17.5110657Z   CC      drivers/md/dm-snap-transient.o
2026-05-03T01:27:17.8040570Z   CC      net/netfilter/nf_conntrack_standalone.o
2026-05-03T01:27:17.8480601Z   CC      drivers/media/platform/mtk-vcodec/venc/venc_common_if.o
2026-05-03T01:27:18.0286713Z   CC      drivers/md/dm-snap-persistent.o
2026-05-03T01:27:18.4910456Z   CC      drivers/media/platform/mtk-vcodec/venc/venc_log_if.o
2026-05-03T01:27:18.5440614Z   AR      drivers/media/radio/built-in.a
2026-05-03T01:27:18.5630716Z   CC      net/nfc/core.o
2026-05-03T01:27:18.6681272Z   CC      drivers/md/dm-verity-avb.o
2026-05-03T01:27:19.0351360Z   CC      drivers/media/platform/mtk-vcodec/venc_vcu_if.o
2026-05-03T01:27:19.1480434Z   CC      net/netfilter/nf_conntrack_expect.o
2026-05-03T01:27:19.2286504Z   CC      drivers/md/dm-verity-fec.o
2026-05-03T01:27:19.6627011Z   CC      drivers/media/platform/mtk-vcodec/mt6768/mtk_vcodec_intr.o
2026-05-03T01:27:19.8330387Z   CC      net/nfc/netlink.o
2026-05-03T01:27:19.8780409Z   CC      drivers/md/dm-verity-target.o
2026-05-03T01:27:20.5380736Z   CC      drivers/media/platform/mtk-vcodec/mtk_vcodec_util.o
2026-05-03T01:27:20.5620536Z   CC      net/netfilter/nf_conntrack_helper.o
2026-05-03T01:27:20.6250992Z   CC      drivers/md/dm-bow.o
2026-05-03T01:27:21.0360624Z ../drivers/media/platform/mtk-vcodec/mtk_vcodec_util.c:143:41: warning: variable 'src_vb2_v4l2' set but not used [-Wunused-but-set-variable]
2026-05-03T01:27:21.0400073Z         struct vb2_v4l2_buffer *dst_vb2_v4l2, *src_vb2_v4l2;
2026-05-03T01:27:21.0400850Z                                                ^
2026-05-03T01:27:21.1290426Z 1 warning generated.
2026-05-03T01:27:21.1840322Z   CC      net/nfc/af_nfc.o
2026-05-03T01:27:21.4373654Z   CC      drivers/media/platform/mtk-vcodec/mt6768/vcodec_dvfs.o
2026-05-03T01:27:21.4500420Z   CC      drivers/md/dm-user.o
2026-05-03T01:27:21.6541430Z ../drivers/media/platform/mtk-vcodec/mt6768/vcodec_dvfs.c:649:6: warning: variable 'target64' set but not used [-Wunused-but-set-variable]
2026-05-03T01:27:21.6589919Z         u64 target64;
2026-05-03T01:27:21.6599877Z             ^
2026-05-03T01:27:21.6990836Z 1 warning generated.
2026-05-03T01:27:21.7213618Z   CC      drivers/media/platform/mtk-vcodec/mt6768/vcodec_bw.o
2026-05-03T01:27:21.9594269Z   AR      drivers/media/platform/mtk-vcodec/built-in.a
2026-05-03T01:27:21.9755471Z   CC      net/netfilter/nf_conntrack_proto.o
2026-05-03T01:27:21.9850337Z   CC      drivers/media/platform/mtk-vcu/mtk_vcu.o
2026-05-03T01:27:22.1080382Z   AR      drivers/md/built-in.a
2026-05-03T01:27:22.1430656Z   CC      net/packet/af_packet.o
2026-05-03T01:27:22.3310472Z   CC      net/nfc/rawsock.o
2026-05-03T01:27:23.4620521Z   CC      net/netfilter/nf_conntrack_proto_generic.o
2026-05-03T01:27:23.4660608Z   CC      drivers/media/platform/mtk-vcu/mtk_vcodec_mem.o
2026-05-03T01:27:23.5460553Z   CC      net/nfc/llcp_core.o
2026-05-03T01:27:23.9821610Z ../drivers/media/platform/mtk-vcu/mtk_vcodec_mem.c:85:6: warning: variable 'op' set but not used [-Wunused-but-set-variable]
2026-05-03T01:27:23.9840429Z         int op;
2026-05-03T01:27:23.9880135Z             ^
2026-05-03T01:27:24.0590505Z 1 warning generated.
2026-05-03T01:27:24.1020598Z   AR      drivers/media/platform/mtk-vcu/built-in.a
2026-05-03T01:27:24.1190443Z   AR      drivers/media/platform/omap/built-in.a
2026-05-03T01:27:24.1350325Z   AR      drivers/media/platform/stm32/built-in.a
2026-05-03T01:27:24.1565147Z   AR      drivers/media/platform/built-in.a
2026-05-03T01:27:24.1860314Z   AR      drivers/media/rc/keymaps/built-in.a
2026-05-03T01:27:24.1980345Z   AR      drivers/media/rc/built-in.a
2026-05-03T01:27:24.2130627Z   AR      drivers/media/spi/built-in.a
2026-05-03T01:27:24.2340407Z   AR      drivers/media/tuners/built-in.a
2026-05-03T01:27:24.2535661Z   AR      drivers/media/usb/b2c2/built-in.a
2026-05-03T01:27:24.2660835Z   AR      net/packet/built-in.a
2026-05-03T01:27:24.2740329Z   AR      drivers/media/usb/dvb-usb/built-in.a
2026-05-03T01:27:24.2883373Z   CC      drivers/media/v4l2-core/v4l2-dev.o
2026-05-03T01:27:24.2908330Z   AR      drivers/media/usb/dvb-usb-v2/built-in.a
2026-05-03T01:27:24.3085320Z   AR      drivers/media/usb/s2255/built-in.a
2026-05-03T01:27:24.3270535Z   AR      drivers/media/usb/siano/built-in.a
2026-05-03T01:27:24.3420444Z   AR      drivers/media/usb/stkwebcam/built-in.a
2026-05-03T01:27:24.3590452Z   AR      drivers/media/usb/ttusb-budget/built-in.a
2026-05-03T01:27:24.3813209Z   AR      drivers/media/usb/ttusb-dec/built-in.a
2026-05-03T01:27:24.3894366Z   CC      net/netfilter/nf_conntrack_proto_tcp.o
2026-05-03T01:27:24.3992806Z   AR      drivers/media/usb/zr364xx/built-in.a
2026-05-03T01:27:24.4210422Z   AR      drivers/media/usb/built-in.a
2026-05-03T01:27:24.4410284Z   CC      net/rfkill/core.o
2026-05-03T01:27:24.6250391Z   CC      net/nfc/llcp_commands.o
2026-05-03T01:27:25.2350389Z   CC      net/rfkill/input.o
2026-05-03T01:27:25.2640478Z   CC      drivers/media/v4l2-core/v4l2-ioctl.o
2026-05-03T01:27:25.5502886Z   CC      net/nfc/llcp_sock.o
2026-05-03T01:27:25.6371944Z   AR      net/rfkill/built-in.a
2026-05-03T01:27:25.6640569Z   AR      drivers/misc/cb710/built-in.a
2026-05-03T01:27:25.6913169Z   CC      drivers/misc/eeprom/eeprom_93cx6.o
2026-05-03T01:27:25.9092085Z   CC      net/netfilter/nf_conntrack_proto_udp.o
2026-05-03T01:27:26.1322320Z   AR      drivers/misc/eeprom/built-in.a
2026-05-03T01:27:26.1500523Z   AR      drivers/misc/lis3lv02d/built-in.a
2026-05-03T01:27:26.2110582Z   CC      drivers/misc/mediatek/accdet/mt6358/accdet.o
2026-05-03T01:27:26.4130547Z   CC      drivers/media/v4l2-core/v4l2-device.o
2026-05-03T01:27:26.5181058Z   AR      net/nfc/built-in.a
2026-05-03T01:27:26.5320323Z   CC      drivers/media/media-device.o
2026-05-03T01:27:27.2200446Z   AR      drivers/misc/mediatek/accdet/mt6358/built-in.a
2026-05-03T01:27:27.2286876Z   CC      drivers/misc/mediatek/accdet/accdet_drv.o
2026-05-03T01:27:27.2367793Z   CC      drivers/media/v4l2-core/v4l2-fh.o
2026-05-03T01:27:27.2800610Z   CC      net/netfilter/nf_conntrack_proto_icmp.o
2026-05-03T01:27:27.4746167Z   CC      drivers/misc/mediatek/aee/aed/aed-main.o
2026-05-03T01:27:27.7240611Z   AR      drivers/misc/mediatek/accdet/built-in.a
2026-05-03T01:27:27.7460463Z   CC      drivers/misc/mediatek/aee/hangdet/aee_hangdet.o
2026-05-03T01:27:27.8600476Z   CC      drivers/media/v4l2-core/v4l2-event.o
2026-05-03T01:27:28.2110302Z   CC      net/netfilter/nf_conntrack_extend.o
2026-05-03T01:27:28.5821084Z   CC      drivers/misc/mediatek/aee/aed/aee-common.o
2026-05-03T01:27:28.6130416Z   CC      drivers/media/v4l2-core/v4l2-ctrls.o
2026-05-03T01:27:29.0600985Z   AR      drivers/misc/mediatek/aee/hangdet/built-in.a
2026-05-03T01:27:29.0840385Z   CC      net/sched/sch_generic.o
2026-05-03T01:27:29.1770228Z   CC      drivers/misc/mediatek/aee/aed/reboot-reason.o
2026-05-03T01:27:29.5190433Z   CC      net/netfilter/nf_conntrack_acct.o
2026-05-03T01:27:29.8980351Z   AR      drivers/misc/mediatek/aee/aed/built-in.a
2026-05-03T01:27:29.9008934Z   CC      drivers/media/v4l2-core/v4l2-subdev.o
2026-05-03T01:27:29.9233954Z   CC      drivers/misc/mediatek/aee/mrdump/mboot_params.o
2026-05-03T01:27:30.7120443Z   CC      drivers/media/v4l2-core/v4l2-clk.o
2026-05-03T01:27:30.7690412Z   CC      net/netfilter/nf_conntrack_seqadj.o
2026-05-03T01:27:30.7923160Z   CC      net/sched/sch_mq.o
2026-05-03T01:27:31.0591356Z   CC      drivers/misc/mediatek/aee/mrdump/mrdump_control.o
2026-05-03T01:27:31.5154398Z   CC      drivers/media/v4l2-core/v4l2-async.o
2026-05-03T01:27:31.5500598Z   CC      net/sched/sch_api.o
2026-05-03T01:27:31.5560285Z   CC      drivers/misc/mediatek/aee/mrdump/mrdump_hw.o
2026-05-03T01:27:32.0211407Z   CC      drivers/misc/mediatek/aee/mrdump/mrdump_full.o
2026-05-03T01:27:32.1950471Z   CC      net/netfilter/nf_conntrack_proto_icmpv6.o
2026-05-03T01:27:32.3100550Z   CC      drivers/media/v4l2-core/v4l2-compat-ioctl32.o
2026-05-03T01:27:32.4962929Z   CC      drivers/misc/mediatek/aee/mrdump/mrdump_mini.o
2026-05-03T01:27:33.0910642Z   CC      net/netfilter/nf_conntrack_ecache.o
2026-05-03T01:27:33.4899977Z   CC      net/sched/sch_blackhole.o
2026-05-03T01:27:33.8874847Z   CC      drivers/misc/mediatek/aee/mrdump/mrdump_panic.o
2026-05-03T01:27:34.0233110Z   CC      drivers/media/v4l2-core/v4l2-trace.o
2026-05-03T01:27:34.1320370Z   CC      net/sched/cls_api.o
2026-05-03T01:27:34.4340450Z   CC      net/netfilter/nf_conntrack_proto_dccp.o
2026-05-03T01:27:34.5500510Z   CC      drivers/misc/mediatek/aee/mrdump/mrdump_helper.o
2026-05-03T01:27:35.0266729Z   CC      drivers/media/v4l2-core/v4l2-mc.o
2026-05-03T01:27:35.7035988Z   CC      net/sched/act_api.o
2026-05-03T01:27:35.7350678Z   CC      drivers/misc/mediatek/aee/mrdump/mrdump_arm64.o
2026-05-03T01:27:35.8040685Z   CC      net/netfilter/nf_conntrack_proto_sctp.o
2026-05-03T01:27:35.8580446Z   CC      drivers/media/v4l2-core/v4l2-common.o
2026-05-03T01:27:36.1636332Z   AR      drivers/misc/mediatek/aee/mrdump/built-in.a
2026-05-03T01:27:36.1843103Z   AR      drivers/misc/mediatek/aee/built-in.a
2026-05-03T01:27:36.2120533Z   CC      drivers/misc/mediatek/atf/atf_logger.o
2026-05-03T01:27:36.6970142Z   CC      drivers/media/v4l2-core/v4l2-dv-timings.o
2026-05-03T01:27:36.7000300Z   AR      drivers/misc/mediatek/atf/built-in.a
2026-05-03T01:27:36.7330609Z   CC      drivers/misc/mediatek/base/power/clkbuf_v1/mt6768/mtk_clkbuf_hw.o
2026-05-03T01:27:37.3110477Z   CC      net/netfilter/nf_conntrack_proto_gre.o
2026-05-03T01:27:37.5050584Z   CC      net/sched/act_police.o
2026-05-03T01:27:37.5510551Z   CC      drivers/media/v4l2-core/v4l2-mem2mem.o
2026-05-03T01:27:37.6400569Z   AR      drivers/misc/mediatek/base/power/clkbuf_v1/mt6768/built-in.a
2026-05-03T01:27:37.6490410Z   CC      drivers/misc/mediatek/base/power/clkbuf_v1/mtk_clkbuf_ctl.o
2026-05-03T01:27:38.2159004Z   AR      drivers/misc/mediatek/base/power/clkbuf_v1/built-in.a
2026-05-03T01:27:38.2429268Z   CC      drivers/misc/mediatek/base/power/cm_mgr_v1/mt6768/mtk_cm_mgr_platform.o
2026-05-03T01:27:38.2600479Z   CC      net/sched/act_mirred.o
2026-05-03T01:27:38.4990720Z   AR      drivers/media/v4l2-core/built-in.a
2026-05-03T01:27:38.5282464Z   CC      drivers/media/media-devnode.o
2026-05-03T01:27:38.6660612Z   CC      net/netfilter/nf_conntrack_netlink.o
2026-05-03T01:27:39.0403404Z   CC      net/sched/act_ipt.o
2026-05-03T01:27:39.0430109Z   CC      drivers/media/media-entity.o
2026-05-03T01:27:39.3830576Z   AR      drivers/misc/mediatek/base/power/cm_mgr_v1/mt6768/built-in.a
2026-05-03T01:27:39.3930233Z   CC      drivers/misc/mediatek/base/power/cm_mgr_v1/mtk_cm_mgr.o
2026-05-03T01:27:39.8287311Z   CC      net/sched/sch_fifo.o
2026-05-03T01:27:39.8650820Z   CC      drivers/media/media-request.o
2026-05-03T01:27:39.8960606Z   CC      net/netfilter/nf_conntrack_amanda.o
2026-05-03T01:27:40.2050413Z   AR      drivers/misc/mediatek/base/power/cm_mgr_v1/built-in.a
2026-05-03T01:27:40.2215363Z ../drivers/misc/mediatek/base/power/cpufreq_v1/src/Makefile:89: "use CONFIG_MTK_TINYSYS_SSPM_V1"
2026-05-03T01:27:40.2440808Z   CC      drivers/misc/mediatek/base/power/cpufreq_v1/src/mach/mt6768/mtk_cpufreq_platform.o
2026-05-03T01:27:40.5308064Z   AR      drivers/media/built-in.a
2026-05-03T01:27:40.5600484Z   CC      drivers/misc/mediatek/base/power/cpuhotplug/mtk_cpuhp_core.o
2026-05-03T01:27:40.8700707Z   AR      drivers/misc/mediatek/base/power/cpufreq_v1/src/mach/mt6768/built-in.a
2026-05-03T01:27:40.8809672Z   AR      drivers/misc/mediatek/base/power/cpufreq_v1/src/mach/built-in.a
2026-05-03T01:27:40.8960059Z   CC      drivers/misc/mediatek/base/power/cpufreq_v1/src/v2/mtk_cpufreq_main.o
2026-05-03T01:27:40.8999739Z   CC      net/sched/sch_htb.o
2026-05-03T01:27:41.0940649Z   CC      drivers/misc/mediatek/base/power/cpuhotplug/mtk_cpuhp_ppm.o
2026-05-03T01:27:41.2370969Z   CC      net/netfilter/nf_conntrack_ftp.o
2026-05-03T01:27:41.4572301Z   CC      drivers/misc/mediatek/base/power/cpuhotplug/mtk_cpuhp_platform.o
2026-05-03T01:27:41.5021142Z   AR      drivers/misc/mediatek/base/power/cpuhotplug/built-in.a
2026-05-03T01:27:41.5200507Z   CC      drivers/misc/mediatek/base/power/cpuidle_v3/mtk_cpuidle.o
2026-05-03T01:27:41.6761208Z   CC      drivers/misc/mediatek/base/power/cpufreq_v1/src/v2/mtk_cpufreq_interface.o
2026-05-03T01:27:41.8960647Z   CC      net/sched/sch_ingress.o
2026-05-03T01:27:42.0340938Z   AR      drivers/misc/mediatek/base/power/cpuidle_v3/built-in.a
2026-05-03T01:27:42.0529040Z   CC      drivers/misc/mi-memory/mi_memory.o
2026-05-03T01:27:42.3263609Z   CC      drivers/misc/mediatek/base/power/cpufreq_v1/src/v2/mtk_cpufreq_api.o
2026-05-03T01:27:42.5594509Z   CC      drivers/misc/mi-memory/mmc_hr_ops.o
2026-05-03T01:27:42.6060558Z   CC      net/sched/sch_fq_codel.o
2026-05-03T01:27:42.7420429Z   CC      net/netfilter/nf_conntrack_h323_main.o
2026-05-03T01:27:43.1023584Z   CC      drivers/misc/mi-memory/mmc_sysfs.o
2026-05-03T01:27:43.4781027Z ../drivers/misc/mi-memory/mmc_sysfs.c:49:24: warning: extra tokens at end of #undef directive [-Wextra-tokens]
2026-05-03T01:27:43.4809951Z #undef MICRON_HR_CMD56 1
2026-05-03T01:27:43.4830146Z                        ^
2026-05-03T01:27:43.4869893Z                        //
2026-05-03T01:27:43.4910368Z ../drivers/misc/mi-memory/mmc_sysfs.c:123:18: warning: unused variable 'i' [-Wunused-variable]
2026-05-03T01:27:43.4929896Z     int err = 0, i = 0;
2026-05-03T01:27:43.4960020Z                  ^
2026-05-03T01:27:43.5170036Z 2 warnings generated.
2026-05-03T01:27:43.5470398Z   CC      drivers/misc/mi-memory/mv.o
2026-05-03T01:27:43.5860600Z   CC      drivers/misc/mediatek/base/power/cpufreq_v1/src/v2/mtk_cpufreq_debug.o
2026-05-03T01:27:43.6550593Z   CC      net/sched/sch_fq.o
2026-05-03T01:27:44.0635606Z   CC      drivers/misc/mi-memory/memory_type.o
2026-05-03T01:27:44.1770611Z   CC      drivers/misc/mediatek/base/power/cpufreq_v1/src/v2/mtk_cpufreq_hybrid.o
2026-05-03T01:27:44.4550416Z   CC      net/netfilter/nf_conntrack_h323_asn1.o
2026-05-03T01:27:44.4950538Z   AR      drivers/misc/mi-memory/built-in.a
2026-05-03T01:27:44.5140180Z   CC      net/sctp/sm_statetable.o
2026-05-03T01:27:44.7058307Z   CC      net/sched/cls_u32.o
2026-05-03T01:27:44.7200343Z   CC      net/netfilter/nf_conntrack_irc.o
2026-05-03T01:27:45.0082504Z   AR      drivers/misc/mediatek/base/power/cpufreq_v1/src/built-in.a
2026-05-03T01:27:45.0230637Z   AR      drivers/misc/mediatek/base/power/cpufreq_v1/built-in.a
2026-05-03T01:27:45.0531353Z   CC      drivers/misc/mediatek/base/power/dcm_v1/mt6768/mtk_dcm_autogen.o
2026-05-03T01:27:45.4660575Z   CC      net/sctp/sm_statefuns.o
2026-05-03T01:27:45.5700989Z   CC      drivers/misc/mediatek/base/power/dcm_v1/mt6768/mtk_dcm_internal.o
2026-05-03T01:27:45.6826862Z   CC      net/sched/cls_fw.o
2026-05-03T01:27:46.0071260Z   AR      drivers/misc/mediatek/base/power/dcm_v1/mt6768/built-in.a
2026-05-03T01:27:46.0160206Z   CC      drivers/misc/mediatek/base/power/dcm_v1/mtk_dcm.o
2026-05-03T01:27:46.1030603Z   CC      net/netfilter/nf_conntrack_broadcast.o
2026-05-03T01:27:46.3381786Z   AR      drivers/misc/mediatek/base/power/dcm_v1/built-in.a
2026-05-03T01:27:46.3648914Z   CC      drivers/misc/mediatek/base/power/eem_v2/mt6768/mtk_eem.o
2026-05-03T01:27:46.5420344Z   CC      net/sched/cls_flow.o
2026-05-03T01:27:47.1475886Z   CC      net/sctp/sm_sideeffect.o
2026-05-03T01:27:47.4270566Z   CC      net/netfilter/nf_conntrack_netbios_ns.o
2026-05-03T01:27:47.6665010Z   CC      net/sched/cls_bpf.o
2026-05-03T01:27:48.0165445Z   CC      drivers/misc/mediatek/base/power/eem_v2/mt6768/mtk_eem_platform.o
2026-05-03T01:27:48.1546886Z   CC      net/sctp/protocol.o
2026-05-03T01:27:48.3380417Z   CC      net/netfilter/nf_conntrack_pptp.o
2026-05-03T01:27:48.4890784Z   CC      drivers/misc/mediatek/base/power/eem_v2/mt6768/mtk_eem_internal.o
2026-05-03T01:27:48.6513415Z   CC      net/sched/ematch.o
2026-05-03T01:27:48.9620876Z   CC      drivers/misc/mediatek/base/power/eem_v2/mt6768/mtk_eem_api.o
2026-05-03T01:27:49.3381062Z   CC      net/sctp/endpointola.o
2026-05-03T01:27:49.3770753Z drivers/misc/mediatek/base/power/eem_v2/mt6768/.tmp_mtk_eem_api.o: no symbols
2026-05-03T01:27:49.3820291Z   AR      drivers/misc/mediatek/base/power/eem_v2/mt6768/built-in.a
2026-05-03T01:27:49.3950293Z   AR      drivers/misc/mediatek/base/power/eem_v2/built-in.a
2026-05-03T01:27:49.4190540Z   CC      drivers/misc/mediatek/base/power/leakage_table_v2/mtk_static_power.o
2026-05-03T01:27:49.7540386Z   CC      net/netfilter/nf_conntrack_sane.o
2026-05-03T01:27:49.7780348Z   CC      net/sched/em_u32.o
2026-05-03T01:27:50.1180952Z   CC      drivers/misc/mediatek/base/power/leakage_table_v2/mtk_static_power_mt6768.o
2026-05-03T01:27:50.1620583Z   AR      drivers/misc/mediatek/base/power/leakage_table_v2/built-in.a
2026-05-03T01:27:50.1920574Z   CC      drivers/misc/mediatek/base/power/mcdi/mcdi_v1/mtk_mcdi_main.o
2026-05-03T01:27:50.3410733Z   CC      net/sctp/associola.o
2026-05-03T01:27:50.4520612Z   AR      net/sched/built-in.a
2026-05-03T01:27:50.4790534Z   CC      drivers/misc/mediatek/blocktag/blocktag-core.o
2026-05-03T01:27:50.6835620Z   CC      net/netfilter/nf_conntrack_tftp.o
2026-05-03T01:27:51.0800816Z   CC      drivers/misc/mediatek/base/power/mcdi/mcdi_v1/mtk_mcdi_util.o
2026-05-03T01:27:51.5010139Z   CC      net/sctp/transport.o
2026-05-03T01:27:51.5600809Z   CC      drivers/misc/mediatek/base/power/mcdi/mcdi_v1/mtk_mcdi_profile.o
2026-05-03T01:27:52.0417042Z   CC      net/netfilter/nf_nat_core.o
2026-05-03T01:27:52.0530617Z   CC      drivers/misc/mediatek/blocktag/blocktag-index.o
2026-05-03T01:27:52.0760666Z   CC      drivers/misc/mediatek/base/power/mcdi/mcdi_v1/mtk_mcdi_cpc.o
2026-05-03T01:27:52.4053278Z   CC      net/sctp/chunk.o
2026-05-03T01:27:52.6070809Z   CC      drivers/misc/mediatek/base/power/mcdi/mcdi_v1/mtk_mcdi_mcupm.o
2026-05-03T01:27:52.7850759Z   AR      drivers/misc/mediatek/blocktag/built-in.a
2026-05-03T01:27:52.8120489Z   CC      drivers/mmc/core/core.o
2026-05-03T01:27:53.0411712Z   AR      drivers/misc/mediatek/base/power/mcdi/mcdi_v1/built-in.a
2026-05-03T01:27:53.0623855Z   CC      drivers/misc/mediatek/base/power/mcdi/mt6768/mtk_mcdi_plat.o
2026-05-03T01:27:53.3770665Z   CC      net/sctp/sm_make_chunk.o
2026-05-03T01:27:53.5501763Z   CC      drivers/misc/mediatek/base/power/mcdi/mt6768/mtk_mcdi_state.o
2026-05-03T01:27:53.7740520Z   CC      net/netfilter/nf_nat_proto_unknown.o
2026-05-03T01:27:53.7830506Z   AR      drivers/misc/mediatek/base/power/mcdi/mt6768/built-in.a
2026-05-03T01:27:53.7950487Z   CC      drivers/misc/mediatek/base/power/mcdi/mtk_mcdi_governor.o
2026-05-03T01:27:54.2750640Z   CC      drivers/mmc/core/bus.o
2026-05-03T01:27:54.3324886Z   CC      drivers/misc/mediatek/base/power/mcdi/mtk_mcdi_governor_lib.o
2026-05-03T01:27:54.6860620Z   CC      net/netfilter/nf_nat_proto_common.o
2026-05-03T01:27:54.7660470Z   CC      net/sctp/ulpevent.o
2026-05-03T01:27:54.8080793Z   CC      drivers/misc/mediatek/base/power/mcdi/mtk_mcdi_governor_hint.o
2026-05-03T01:27:54.9660677Z   CC      drivers/misc/mediatek/base/power/mcdi/mtk_mcdi_api.o
2026-05-03T01:27:55.1444654Z   CC      drivers/mmc/core/host.o
2026-05-03T01:27:55.4245916Z   AR      drivers/misc/mediatek/base/power/mcdi/built-in.a
2026-05-03T01:27:55.4530466Z   CC      drivers/misc/mediatek/base/power/mdpm_v1/mt6768/mtk_mdpm_platform.o
2026-05-03T01:27:55.7680505Z   CC      net/sctp/inqueue.o
2026-05-03T01:27:55.7790453Z   AR      drivers/misc/mediatek/base/power/mdpm_v1/mt6768/built-in.a
2026-05-03T01:27:55.7880415Z   CC      drivers/misc/mediatek/base/power/mdpm_v1/mtk_mdpm_common.o
2026-05-03T01:27:55.9111041Z   CC      net/netfilter/nf_nat_proto_udp.o
2026-05-03T01:27:56.0690445Z   CC      drivers/mmc/core/mmc.o
2026-05-03T01:27:56.3670605Z   AR      drivers/misc/mediatek/base/power/mdpm_v1/built-in.a
2026-05-03T01:27:56.3840466Z   CC      drivers/misc/mediatek/base/power/pbm_v4/mtk_pbm.o
2026-05-03T01:27:56.7460270Z   CC      net/sctp/outqueue.o
2026-05-03T01:27:56.8350428Z   CC      net/netfilter/nf_nat_proto_tcp.o
2026-05-03T01:27:56.9250652Z   CC      drivers/mmc/core/mmc_ops.o
2026-05-03T01:27:57.0580657Z   AR      drivers/misc/mediatek/base/power/pbm_v4/built-in.a
2026-05-03T01:27:57.0849621Z   CC      drivers/misc/mediatek/base/power/power_gs_v1/mt6768/mtk_power_gs_6358_array.o
2026-05-03T01:27:57.3940851Z   CC      drivers/misc/mediatek/base/power/power_gs_v1/mt6768/mtk_cg_array.o
2026-05-03T01:27:57.6890649Z   CC      drivers/misc/mediatek/base/power/power_gs_v1/mt6768/mtk_dcm_array.o
2026-05-03T01:27:57.7170529Z   CC      net/netfilter/nf_nat_helper.o
2026-05-03T01:27:57.8780816Z   CC      drivers/mmc/core/sd.o
2026-05-03T01:27:57.9300649Z   CC      net/sctp/ulpqueue.o
2026-05-03T01:27:57.9750810Z   CC      drivers/misc/mediatek/base/power/power_gs_v1/mt6768/mtk_power_gs_sp.o
2026-05-03T01:27:58.3939029Z   CC      drivers/misc/mediatek/base/power/power_gs_v1/mt6768/mtk_power_gs_compare.o
2026-05-03T01:27:58.5789086Z   CC      drivers/mmc/core/sd_ops.o
2026-05-03T01:27:58.8047650Z   CC      drivers/misc/mediatek/base/power/power_gs_v1/mt6768/mtk_power_gs_dump_pmic.o
2026-05-03T01:27:59.0108160Z   CC      net/sctp/tsnmap.o
2026-05-03T01:27:59.1310856Z   CC      net/netfilter/nf_nat_proto_dccp.o
2026-05-03T01:27:59.2540701Z   AR      drivers/misc/mediatek/base/power/power_gs_v1/mt6768/built-in.a
2026-05-03T01:27:59.2650249Z   CC      drivers/misc/mediatek/base/power/power_gs_v1/mtk_power_gs.o
2026-05-03T01:27:59.4175796Z   CC      drivers/mmc/core/sdio.o
2026-05-03T01:27:59.9802623Z   CC      drivers/misc/mediatek/base/power/power_gs_v1/mtk_power_gs_api.o
2026-05-03T01:27:59.9820609Z   CC      net/sctp/bind_addr.o
2026-05-03T01:27:59.9970628Z   CC      net/netfilter/nf_nat_proto_sctp.o
2026-05-03T01:28:00.1110699Z   CC      drivers/mmc/core/sdio_ops.o
2026-05-03T01:28:00.4940680Z   AR      drivers/misc/mediatek/base/power/power_gs_v1/built-in.a
2026-05-03T01:28:00.5114279Z ../drivers/misc/mediatek/base/power/ppm_v3/src/Makefile:110: USE_PPM_CPI
2026-05-03T01:28:00.5370512Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mach/mt6768/mtk_ppm_platform.o
2026-05-03T01:28:00.7080558Z   CC      drivers/mmc/core/sdio_bus.o
2026-05-03T01:28:00.9455656Z   CC      net/netfilter/nf_nat_redirect.o
2026-05-03T01:28:00.9851278Z   CC      net/sctp/socket.o
2026-05-03T01:28:01.1070796Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mach/mt6768/mtk_ppm_power_data.o
2026-05-03T01:28:01.5149591Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mach/mt6768/mtk_ppm_cobra_algo.o
2026-05-03T01:28:01.6411142Z   CC      drivers/mmc/core/sdio_cis.o
2026-05-03T01:28:01.8930954Z ../net/sctp/socket.c:1113:6: warning: variable 'addrcnt' set but not used [-Wunused-but-set-variable]
2026-05-03T01:28:01.8959886Z         int addrcnt = 0;
2026-05-03T01:28:01.8980017Z             ^
2026-05-03T01:28:02.0630813Z   AR      drivers/misc/mediatek/base/power/ppm_v3/src/mach/mt6768/built-in.a
2026-05-03T01:28:02.0743906Z   AR      drivers/misc/mediatek/base/power/ppm_v3/src/mach/built-in.a
2026-05-03T01:28:02.0857820Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mtk_ppm_main.o
2026-05-03T01:28:02.1100545Z   CC      drivers/mmc/core/sdio_io.o
2026-05-03T01:28:02.2360561Z   CC      net/netfilter/nf_nat_amanda.o
2026-05-03T01:28:02.9927907Z   CC      drivers/mmc/core/sdio_irq.o
2026-05-03T01:28:03.0030799Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mtk_ppm_interface.o
2026-05-03T01:28:03.1773192Z   CC      net/netfilter/nf_nat_ftp.o
2026-05-03T01:28:03.2160594Z 1 warning generated.
2026-05-03T01:28:03.4814951Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mtk_ppm_api.o
2026-05-03T01:28:03.7730406Z   CC      net/sctp/primitive.o
2026-05-03T01:28:03.8422709Z   CC      drivers/mmc/core/slot-gpio.o
2026-05-03T01:28:03.8550708Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mtk_ppm_profile.o
2026-05-03T01:28:03.9890420Z   CC      net/netfilter/nf_nat_irc.o
2026-05-03T01:28:04.2760739Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mtk_ppm_ipi.o
2026-05-03T01:28:04.5685655Z   CC      drivers/mmc/core/pwrseq.o
2026-05-03T01:28:04.6020703Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mtk_ppm_cpi.o
2026-05-03T01:28:04.7330655Z   CC      net/sctp/output.o
2026-05-03T01:28:04.9080541Z   CC      net/netfilter/nf_nat_tftp.o
2026-05-03T01:28:05.1827210Z   CC      drivers/mmc/core/pwrseq_simple.o
2026-05-03T01:28:05.2410824Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mtk_ppm_policy_dlpt.o
2026-05-03T01:28:05.6720546Z   CC      drivers/mmc/core/pwrseq_emmc.o
2026-05-03T01:28:05.6780590Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mtk_ppm_policy_sys_boost.o
2026-05-03T01:28:05.7968191Z   CC      net/netfilter/nf_conncount.o
2026-05-03T01:28:05.7990006Z   CC      net/sctp/input.o
2026-05-03T01:28:06.0781263Z   CC      drivers/mmc/core/block.o
2026-05-03T01:28:06.3950708Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mtk_ppm_policy_ptpod.o
2026-05-03T01:28:06.8160080Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mtk_ppm_policy_pwr_thro.o
2026-05-03T01:28:07.1933570Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mtk_ppm_policy_thermal.o
2026-05-03T01:28:07.2630392Z   CC      net/netfilter/x_tables.o
2026-05-03T01:28:07.2765428Z   CC      net/sctp/debug.o
2026-05-03T01:28:07.3740610Z   CC      drivers/mmc/core/queue.o
2026-05-03T01:28:07.6521771Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mtk_ppm_policy_lcm_off.o
2026-05-03T01:28:08.0520617Z   CC      drivers/mmc/core/mmc_crypto.o
2026-05-03T01:28:08.1780593Z   CC      net/sctp/stream.o
2026-05-03T01:28:08.1890620Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mtk_ppm_policy_hard_user_limit.o
2026-05-03T01:28:08.6941578Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mtk_ppm_policy_user_limit.o
2026-05-03T01:28:08.7060268Z   CC      drivers/mmc/core/crypto.o
2026-05-03T01:28:08.8980364Z   CC      net/netfilter/xt_tcpudp.o
2026-05-03T01:28:09.1800532Z   CC      net/sctp/auth.o
2026-05-03T01:28:09.1940691Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mtk_ppm_policy_force_limit.o
2026-05-03T01:28:09.5256435Z   CC      drivers/mmc/core/mtk_mmc_block.o
2026-05-03T01:28:09.5990690Z   CC      drivers/misc/mediatek/base/power/ppm_v3/src/mtk_ppm_policy_ut.o
2026-05-03T01:28:09.8470536Z   CC      net/netfilter/xt_mark.o
2026-05-03T01:28:10.0650889Z ../drivers/mmc/core/mtk_mmc_block.c:299:42: warning: unused variable 'result' [-Wunused-variable]
2026-05-03T01:28:10.0670091Z         uint64_t min, period, tsk_start, usage, result;
2026-05-03T01:28:10.0690163Z                                                 ^
2026-05-03T01:28:10.0700302Z ../drivers/mmc/core/mtk_mmc_block.c:299:35: warning: unused variable 'usage' [-Wunused-variable]
2026-05-03T01:28:10.0730131Z         uint64_t min, period, tsk_start, usage, result;
2026-05-03T01:28:10.0759959Z                                          ^
2026-05-03T01:28:10.1050457Z   AR      drivers/misc/mediatek/base/power/ppm_v3/src/built-in.a
2026-05-03T01:28:10.1190701Z   AR      drivers/misc/mediatek/base/power/ppm_v3/built-in.a
2026-05-03T01:28:10.1570622Z   CC      drivers/misc/mediatek/base/power/spm/common_v1/mtk_idle_fs/mtk_lp_kernfs.o
2026-05-03T01:28:10.1920731Z 2 warnings generated.
2026-05-03T01:28:10.2875832Z   CC      net/sctp/offload.o
2026-05-03T01:28:10.4960526Z   CC      drivers/mmc/core/ffu-mi.o
2026-05-03T01:28:10.5150419Z   CC      net/netfilter/xt_connmark.o
2026-05-03T01:28:10.6902743Z   CC      drivers/misc/mediatek/base/power/spm/common_v1/mtk_idle_fs/mtk_lp_sysfs.o
2026-05-03T01:28:10.9870836Z   CC      drivers/misc/mediatek/base/power/spm/common_v1/mtk_idle_fs/mtk_idle_sysfs.o
2026-05-03T01:28:11.2160658Z   CC      net/sctp/stream_sched.o
2026-05-03T01:28:11.3700465Z   CC      drivers/misc/mediatek/base/power/spm/common_v1/mtk_idle_fs/mtk_lp_sysfs_procfs.o
2026-05-03T01:28:11.3980379Z   CC      net/netfilter/xt_nat.o
2026-05-03T01:28:11.7734445Z   AR      drivers/misc/mediatek/base/power/spm/common_v1/mtk_idle_fs/built-in.a
2026-05-03T01:28:11.7880455Z   CC      drivers/misc/mediatek/base/power/spm/common_v1/mtk_idle.o
2026-05-03T01:28:11.9680699Z   CC      net/sctp/stream_sched_prio.o
2026-05-03T01:28:12.3190489Z   CC      net/netfilter/xt_CLASSIFY.o
2026-05-03T01:28:12.5990534Z   CC      drivers/misc/mediatek/base/power/spm/common_v1/mtk_idle_select.o
2026-05-03T01:28:12.7332748Z   CC      net/sctp/stream_sched_rr.o
2026-05-03T01:28:12.9570526Z   CC      net/netfilter/xt_CONNSECMARK.o
2026-05-03T01:28:13.1481732Z   CC      drivers/misc/mediatek/base/power/spm/common_v1/mtk_idle_internal.o
2026-05-03T01:28:13.4840635Z   CC      net/sctp/stream_interleave.o
2026-05-03T01:28:13.8745653Z   CC      net/netfilter/xt_CT.o
2026-05-03T01:28:13.9150790Z   CC      drivers/misc/mediatek/base/power/spm/common_v1/mtk_idle_profile.o
2026-05-03T01:28:14.4060746Z   CC      drivers/misc/mediatek/base/power/spm/common_v1/mtk_idle_twam.o
2026-05-03T01:28:14.4730569Z   CC      net/sctp/proc.o
2026-05-03T01:28:14.6210370Z   AR      drivers/mmc/core/built-in.a
2026-05-03T01:28:14.6570484Z   CC      drivers/mmc/host/mtk-sd.o
2026-05-03T01:28:14.8041470Z   CC      drivers/misc/mediatek/base/power/spm/common_v1/mtk_spm_resource_req.o
2026-05-03T01:28:14.8262023Z   CC      net/netfilter/xt_HL.o
2026-05-03T01:28:15.1633638Z ../drivers/mmc/host/mtk-sd.c:764:6: warning: unused variable 'count' [-Wunused-variable]
2026-05-03T01:28:15.1660075Z         u32 count = 0;
2026-05-03T01:28:15.1689869Z             ^
2026-05-03T01:28:15.4060501Z   CC      net/sctp/sysctl.o
2026-05-03T01:28:15.4540464Z   CC      drivers/misc/mediatek/base/power/spm/common_v1/mtk_sleep.o
2026-05-03T01:28:15.5960547Z 1 warning generated.
2026-05-03T01:28:15.6310165Z   CC      drivers/mmc/host/cqhci.o
2026-05-03T01:28:15.6750462Z   CC      net/netfilter/xt_NETMAP.o
2026-05-03T01:28:16.3420741Z   CC      drivers/misc/mediatek/base/power/spm/common_v1/mtk_sleep_init.o
2026-05-03T01:28:16.3624240Z   CC      net/sctp/ipv6.o
2026-05-03T01:28:16.5660528Z   CC      drivers/mmc/host/cqhci-crypto.o
2026-05-03T01:28:16.5850617Z   CC      net/netfilter/xt_NFLOG.o
2026-05-03T01:28:16.6600659Z   CC      drivers/misc/mediatek/base/power/spm/common_v1/mtk_vcore_dvfs.o
2026-05-03T01:28:17.1103917Z   AR      drivers/mmc/host/built-in.a
2026-05-03T01:28:17.1251464Z   CC      drivers/misc/mediatek/base/power/spm/common_v1/mtk_idle_module.o
2026-05-03T01:28:17.1280448Z   AR      drivers/mmc/built-in.a
2026-05-03T01:28:17.1541159Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/mtk_spm.o
2026-05-03T01:28:17.2705381Z   CC      net/netfilter/xt_NFQUEUE.o
2026-05-03T01:28:17.4550677Z   CC      net/sctp/diag.o
2026-05-03T01:28:17.6940647Z   CC      drivers/misc/mediatek/base/power/spm/common_v1/mtk_idle_export_legacy.o
2026-05-03T01:28:18.0664160Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/mtk_spm_twam.o
2026-05-03T01:28:18.1193692Z   CC      net/netfilter/xt_REDIRECT.o
2026-05-03T01:28:18.1514106Z   AR      drivers/misc/mediatek/base/power/spm/common_v1/built-in.a
2026-05-03T01:28:18.1844301Z   AR      drivers/misc/mic/bus/built-in.a
2026-05-03T01:28:18.1980408Z   AR      drivers/misc/mic/built-in.a
2026-05-03T01:28:18.2070166Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/mtk_spm_irq.o
2026-05-03T01:28:18.4280437Z   AR      net/sctp/built-in.a
2026-05-03T01:28:18.4410127Z   CC      net/netfilter/xt_SECMARK.o
2026-05-03T01:28:18.7445984Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/mtk_spm_dram.o
2026-05-03T01:28:18.7560460Z   CC      drivers/misc/mediatek/btif/common/mtk_btif.o
2026-05-03T01:28:19.0473713Z   CC      drivers/misc/mediatek/base/power/udi_v2/mtk_udi.o
2026-05-03T01:28:19.1340538Z   CC      net/netfilter/xt_TPROXY.o
2026-05-03T01:28:19.4547779Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/mtk_spm_internal.o
2026-05-03T01:28:19.5852031Z   AR      drivers/misc/mediatek/base/power/udi_v2/built-in.a
2026-05-03T01:28:19.6158488Z   AR      drivers/net/dsa/b53/built-in.a
2026-05-03T01:28:19.6325047Z   AR      drivers/net/dsa/microchip/built-in.a
2026-05-03T01:28:19.6485156Z   AR      drivers/net/dsa/mv88e6xxx/built-in.a
2026-05-03T01:28:19.6653821Z   AR      drivers/net/dsa/built-in.a
2026-05-03T01:28:19.6851776Z   CC      drivers/net/phy/mdio-boardinfo.o
2026-05-03T01:28:19.9030694Z   CC      drivers/misc/mediatek/btif/common/mtk_btif_exp.o
2026-05-03T01:28:19.9150464Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/mtk_spm_suspend.o
2026-05-03T01:28:20.1090617Z   CC      net/netfilter/xt_TCPMSS.o
2026-05-03T01:28:20.5480442Z   CC      drivers/net/phy/phy.o
2026-05-03T01:28:20.5860723Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/mtk_spm_suspend_process.o
2026-05-03T01:28:20.7699757Z   CC      drivers/misc/mediatek/btif/common/btif_dma_plat.o
2026-05-03T01:28:21.0272542Z   CC      net/netfilter/xt_TRACE.o
2026-05-03T01:28:21.0730712Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/mtk_sspm.o
2026-05-03T01:28:21.4160580Z   CC      drivers/misc/mediatek/btif/common/btif_plat.o
2026-05-03T01:28:21.5981491Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/mtk_spm_power.o
2026-05-03T01:28:21.6660457Z   CC      net/netfilter/xt_IDLETIMER.o
2026-05-03T01:28:21.6960392Z   CC      drivers/net/phy/phy-c45.o
2026-05-03T01:28:22.0375956Z   AR      drivers/misc/mediatek/btif/common/built-in.a
2026-05-03T01:28:22.0523730Z   AR      drivers/misc/mediatek/btif/built-in.a
2026-05-03T01:28:22.0640995Z   CC      net/netfilter/xt_bpf.o
2026-05-03T01:28:22.1000674Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/mtk_spm_fs.o
2026-05-03T01:28:22.5444745Z   CC      drivers/net/phy/phy-core.o
2026-05-03T01:28:22.5920705Z   AR      drivers/misc/ti-st/built-in.a
2026-05-03T01:28:22.6076868Z   CC      net/unix/af_unix.o
2026-05-03T01:28:22.6940578Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/mtk_spm_utils.o
2026-05-03T01:28:22.7870179Z   CC      net/netfilter/xt_comment.o
2026-05-03T01:28:23.3970566Z   CC      drivers/net/phy/phy_device.o
2026-05-03T01:28:23.4194305Z   CC      net/netfilter/xt_connbytes.o
2026-05-03T01:28:23.4780612Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/mtk_idle_cond_check.o
2026-05-03T01:28:24.0430854Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/mtk_spm_idle.o
2026-05-03T01:28:24.1540421Z   CC      net/unix/garbage.o
2026-05-03T01:28:24.3520668Z   CC      net/netfilter/xt_connlimit.o
2026-05-03T01:28:24.6660742Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/mtk_spm_vcore_dvfs.o
2026-05-03T01:28:24.6965679Z   CC      drivers/net/phy/mdio_bus.o
2026-05-03T01:28:25.0178065Z   CC      net/unix/sysctl_net_unix.o
2026-05-03T01:28:25.1240576Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/mtk_idle_module_plat.o
2026-05-03T01:28:25.2720521Z   CC      net/netfilter/xt_conntrack.o
2026-05-03T01:28:25.5360795Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/mtk_spm_resource_req_console.o
2026-05-03T01:28:25.8282997Z   CC      net/unix/scm.o
2026-05-03T01:28:25.9390693Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/models/mtk_idle_dram.o
2026-05-03T01:28:25.9600517Z   CC      drivers/net/phy/mdio_device.o
2026-05-03T01:28:26.2312096Z   CC      net/netfilter/xt_ecn.o
2026-05-03T01:28:26.4340700Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/models/mtk_idle_syspll.o
2026-05-03T01:28:26.8603745Z   CC      drivers/net/phy/swphy.o
2026-05-03T01:28:26.9270602Z   CC      drivers/misc/mediatek/base/power/spm/mt6768/models/mtk_idle_bus26m.o
2026-05-03T01:28:27.0318196Z   AR      net/unix/built-in.a
2026-05-03T01:28:27.0650528Z   CC      drivers/nfc/pn557/nfc.o
2026-05-03T01:28:27.1490517Z   CC      net/netfilter/xt_esp.o
2026-05-03T01:28:27.4090555Z   AR      drivers/misc/mediatek/base/power/spm/mt6768/built-in.a
2026-05-03T01:28:27.4270224Z   AR      drivers/misc/mediatek/base/power/spm/built-in.a
2026-05-03T01:28:27.4420433Z ../drivers/misc/mediatek/base/power/upower_v2/Makefile:33: extraneous text after 'ifeq' directive
2026-05-03T01:28:27.4505400Z   CC      drivers/misc/mediatek/base/power/upower_v2/mtk_unified_power.o
2026-05-03T01:28:27.6049675Z   CC      drivers/net/phy/fixed_phy.o
2026-05-03T01:28:27.6160209Z   CC      drivers/nfc/pn557/sn1xx.o
2026-05-03T01:28:27.9420743Z   CC      drivers/misc/mediatek/base/power/upower_v2/mtk_unified_power_internal.o
2026-05-03T01:28:28.0081044Z   CC      net/netfilter/xt_hashlimit.o
2026-05-03T01:28:28.0930553Z   CC      drivers/nfc/pn557/pn8xt.o
2026-05-03T01:28:28.2500829Z   CC      drivers/misc/mediatek/base/power/upower_v2/mtk_unified_power_api.o
2026-05-03T01:28:28.5158218Z   AR      drivers/net/phy/built-in.a
2026-05-03T01:28:28.5470454Z   CC      drivers/net/ppp/ppp_generic.o
2026-05-03T01:28:28.5550006Z ../drivers/nfc/pn557/pn8xt.c:186:10: warning: variable 'clk_sw_ctr_ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:28:28.5550933Z     bool clk_sw_ctr_ret = 0;
2026-05-03T01:28:28.5579890Z          ^
2026-05-03T01:28:28.6675848Z   CC      drivers/misc/mediatek/base/power/upower_v2/mtk_unified_power_mt6768.o
2026-05-03T01:28:28.6678891Z 1 warning generated.
2026-05-03T01:28:28.6976618Z   AR      drivers/nfc/pn557/built-in.a
2026-05-03T01:28:28.7131291Z   AR      drivers/nfc/built-in.a
2026-05-03T01:28:28.7330323Z   AR      drivers/nvme/host/built-in.a
2026-05-03T01:28:28.7495280Z   AR      drivers/nvme/target/built-in.a
2026-05-03T01:28:28.7650022Z   AR      drivers/nvme/built-in.a
2026-05-03T01:28:28.7850194Z   CC      drivers/misc/mediatek/c2k_usb/f_rawbulk.o
2026-05-03T01:28:29.1598407Z   CC      net/netfilter/xt_helper.o
2026-05-03T01:28:29.1910678Z   AR      drivers/misc/mediatek/base/power/upower_v2/built-in.a
2026-05-03T01:28:29.2240233Z   AR      drivers/misc/mediatek/base/power/built-in.a
2026-05-03T01:28:29.2520247Z   AR      drivers/misc/mediatek/base/built-in.a
2026-05-03T01:28:29.2670086Z   CC      drivers/misc/uid_sys_stats.o
2026-05-03T01:28:29.6441646Z   CC      drivers/misc/mediatek/c2k_usb/rawbulk.o
2026-05-03T01:28:29.9179994Z   GEN     net/wireless/shipped-certs.c
2026-05-03T01:28:29.9287735Z   CC      net/wireless/core.o
2026-05-03T01:28:30.0685702Z   CC      net/netfilter/xt_hl.o
2026-05-03T01:28:30.2480468Z   CC      drivers/net/ppp/ppp_async.o
2026-05-03T01:28:30.4800820Z   CC      drivers/misc/mediatek/c2k_usb/rawbulk_transfer.o
2026-05-03T01:28:30.9223366Z   CC      net/netfilter/xt_iprange.o
2026-05-03T01:28:31.1467389Z   CC      drivers/net/ppp/bsd_comp.o
2026-05-03T01:28:31.5380398Z   CC      drivers/net/ppp/ppp_deflate.o
2026-05-03T01:28:31.5594067Z   AR      drivers/misc/mediatek/c2k_usb/built-in.a
2026-05-03T01:28:31.5870390Z   AS      drivers/misc/mediatek/cache/cache-mtk-aarch64.o
2026-05-03T01:28:31.6413345Z   AR      drivers/misc/mediatek/cache/built-in.a
2026-05-03T01:28:31.6771274Z   CC      drivers/misc/mediatek/cam_cal/src/mt6768/../common/v1/eeprom_driver.o
2026-05-03T01:28:31.7613074Z   CC      net/netfilter/xt_l2tp.o
2026-05-03T01:28:31.8420466Z   CC      drivers/net/ppp/ppp_mppe.o
2026-05-03T01:28:32.0390401Z   CC      net/wireless/sysfs.o
2026-05-03T01:28:32.3640828Z   CC      drivers/misc/mediatek/cam_cal/src/mt6768/../common/v1/eeprom_i2c_common_driver.o
2026-05-03T01:28:32.4000557Z   CC      drivers/net/ppp/ppp_synctty.o
2026-05-03T01:28:32.6845783Z   CC      net/netfilter/xt_length.o
2026-05-03T01:28:32.8950630Z   CC      drivers/misc/mediatek/cam_cal/src/mt6768/eeprom_i2c_custom_driver.o
2026-05-03T01:28:33.2231033Z   CC      drivers/net/ppp/pppox.o
2026-05-03T01:28:33.3200306Z   CC      net/wireless/radiotap.o
2026-05-03T01:28:33.4066291Z   CC      drivers/misc/mediatek/cam_cal/src/mt6768/cam_cal_list.o
2026-05-03T01:28:33.5660609Z   CC      net/netfilter/xt_limit.o
2026-05-03T01:28:33.7400526Z   CC      drivers/misc/mediatek/cam_cal/src/mt6768/eeprom_i2c_dev.o
2026-05-03T01:28:33.7830730Z   AR      drivers/misc/mediatek/cam_cal/src/mt6768/built-in.a
2026-05-03T01:28:33.7945588Z   AR      drivers/misc/mediatek/cam_cal/src/built-in.a
2026-05-03T01:28:33.8065764Z   AR      drivers/misc/mediatek/cam_cal/built-in.a
2026-05-03T01:28:33.8310418Z   CC      drivers/misc/mediatek/cameraisp/dip/cameradip_dummy.o
2026-05-03T01:28:33.8670607Z drivers/misc/mediatek/cameraisp/dip/.tmp_cameradip_dummy.o: no symbols
2026-05-03T01:28:33.8680189Z   AR      drivers/misc/mediatek/cameraisp/dip/built-in.a
2026-05-03T01:28:33.8789955Z ..
2026-05-03T01:28:33.8910222Z   CC      drivers/misc/mediatek/cameraisp/dpe/cameradpe_dummy.o
2026-05-03T01:28:33.9230596Z drivers/misc/mediatek/cameraisp/dpe/.tmp_cameradpe_dummy.o: no symbols
2026-05-03T01:28:33.9280673Z   CC      drivers/misc/mediatek/cameraisp/dpe/mt6768/camera_dpe.o
2026-05-03T01:28:34.2559982Z   CC      net/netfilter/xt_mac.o
2026-05-03T01:28:34.3240302Z   CC      net/wireless/util.o
2026-05-03T01:28:34.4408821Z   CC      drivers/net/ppp/pppoe.o
2026-05-03T01:28:34.9220386Z   CC      net/netfilter/xt_multiport.o
2026-05-03T01:28:35.2275605Z   AR      drivers/misc/mediatek/cameraisp/dpe/built-in.a
2026-05-03T01:28:35.2390064Z FDVT: Drv use 4.0 folder
2026-05-03T01:28:35.2469895Z ..
2026-05-03T01:28:35.2540056Z   CC      drivers/misc/mediatek/cameraisp/fdvt/4.0/camera_fdvt.o
2026-05-03T01:28:35.4501393Z   CC      drivers/net/ppp/pptp.o
2026-05-03T01:28:35.7828112Z   CC      net/netfilter/xt_owner.o
2026-05-03T01:28:36.0600730Z   AR      drivers/misc/mediatek/cameraisp/fdvt/4.0/built-in.a
2026-05-03T01:28:36.0690424Z   CC      drivers/misc/mediatek/cameraisp/fdvt/fdvt_dummy.o
2026-05-03T01:28:36.0990520Z drivers/misc/mediatek/cameraisp/fdvt/.tmp_fdvt_dummy.o: no symbols
2026-05-03T01:28:36.1080225Z   AR      drivers/misc/mediatek/cameraisp/fdvt/built-in.a
2026-05-03T01:28:36.1248235Z ..
2026-05-03T01:28:36.1380279Z   CC      drivers/misc/mediatek/cameraisp/rsc/engine_request.o
2026-05-03T01:28:36.4920598Z   AR      drivers/net/ppp/built-in.a
2026-05-03T01:28:36.5115107Z   CC      drivers/net/slip/slhc.o
2026-05-03T01:28:36.5893270Z   AR      drivers/misc/mediatek/cameraisp/rsc/built-in.a
2026-05-03T01:28:36.6206749Z   CC      drivers/misc/mediatek/cameraisp/src/mt6768/camera_isp.o
2026-05-03T01:28:36.6406010Z   CC      net/netfilter/xt_physdev.o
2026-05-03T01:28:36.6849854Z   CC      net/wireless/reg.o
2026-05-03T01:28:37.5820641Z   CC      net/netfilter/xt_pkttype.o
2026-05-03T01:28:37.9470570Z   AR      drivers/net/slip/built-in.a
2026-05-03T01:28:37.9674554Z   CC      drivers/net/usb/asix_devices.o
2026-05-03T01:28:38.4316463Z   CC      net/netfilter/xt_policy.o
2026-05-03T01:28:38.7650576Z   CC      drivers/net/usb/asix_common.o
2026-05-03T01:28:39.2660437Z   CC      net/netfilter/xt_quota.o
2026-05-03T01:28:39.3139613Z   CC      net/wireless/scan.o
2026-05-03T01:28:39.5192264Z   CC      drivers/net/usb/ax88172a.o
2026-05-03T01:28:39.5330580Z   AR      drivers/misc/mediatek/cameraisp/src/mt6768/built-in.a
2026-05-03T01:28:39.5420493Z   CC      drivers/misc/mediatek/cameraisp/src/cameraisp_dummy.o
2026-05-03T01:28:39.5770615Z drivers/misc/mediatek/cameraisp/src/.tmp_cameraisp_dummy.o: no symbols
2026-05-03T01:28:39.5825936Z   AR      drivers/misc/mediatek/cameraisp/src/built-in.a
2026-05-03T01:28:39.6023924Z   CC      drivers/misc/mediatek/cameraisp/wpe/camerawpe_dummy.o
2026-05-03T01:28:39.6420855Z drivers/misc/mediatek/cameraisp/wpe/.tmp_camerawpe_dummy.o: no symbols
2026-05-03T01:28:39.6430398Z   AR      drivers/misc/mediatek/cameraisp/wpe/built-in.a
2026-05-03T01:28:39.6620383Z   AR      drivers/misc/mediatek/cameraisp/built-in.a
2026-05-03T01:28:39.6862920Z   CC      drivers/misc/mediatek/ccci_util/ccci_util_lib_fo.o
2026-05-03T01:28:39.9650504Z   CC      net/netfilter/xt_quota2.o
2026-05-03T01:28:40.2664800Z   CC      drivers/net/usb/ax88179_178a.o
2026-05-03T01:28:40.7153976Z   CC      net/netfilter/xt_realm.o
2026-05-03T01:28:40.8910749Z   CC      drivers/misc/mediatek/ccci_util/ccci_util_lib_load_img.o
2026-05-03T01:28:41.1921793Z   CC      drivers/net/usb/cdc_ether.o
2026-05-03T01:28:41.5708151Z   CC      net/wireless/nl80211.o
2026-05-03T01:28:41.5898790Z   CC      net/netfilter/xt_recent.o
2026-05-03T01:28:41.8510609Z   CC      drivers/misc/mediatek/ccci_util/ccci_util_lib_sys.o
2026-05-03T01:28:42.3070364Z   CC      drivers/net/usb/net1080.o
2026-05-03T01:28:42.5220667Z   CC      net/netfilter/xt_sctp.o
2026-05-03T01:28:42.6541278Z   CC      drivers/misc/mediatek/ccci_util/ccci_private_log.o
2026-05-03T01:28:43.0520614Z   CC      drivers/net/usb/cdc_subset.o
2026-05-03T01:28:43.5030483Z   CC      net/netfilter/xt_socket.o
2026-05-03T01:28:43.6005450Z   CC      drivers/misc/mediatek/ccci_util/ccci_util_lib_time.o
2026-05-03T01:28:43.7509709Z   CC      drivers/net/usb/zaurus.o
2026-05-03T01:28:44.3840734Z   CC      drivers/misc/mediatek/ccci_util/ccci_util_lib_main.o
2026-05-03T01:28:44.4690703Z   CC      net/netfilter/xt_state.o
2026-05-03T01:28:44.4779224Z   CC      drivers/net/usb/usbnet.o
2026-05-03T01:28:45.0160518Z   CC      drivers/misc/mediatek/ccci_util/ccci_util_ld_md_errno.o
2026-05-03T01:28:45.0590744Z   CC      drivers/misc/mediatek/ccci_util/ccci_util_broadcast.o
2026-05-03T01:28:45.3890803Z   CC      net/netfilter/xt_statistic.o
2026-05-03T01:28:45.9070628Z   CC      drivers/net/usb/cdc_ncm.o
2026-05-03T01:28:45.9390660Z   CC      drivers/misc/mediatek/ccci_util/ccci_util_pin_broadcast.o
2026-05-03T01:28:45.9940559Z   CC      net/netfilter/xt_string.o
2026-05-03T01:28:46.4280553Z   CC      drivers/misc/mediatek/ccci_util/ccci_util_sib.o
2026-05-03T01:28:46.6163573Z ../drivers/net/usb/cdc_ncm.c:1612:22: warning: variable 'ctx' set but not used [-Wunused-but-set-variable]
2026-05-03T01:28:46.6189925Z         struct cdc_ncm_ctx *ctx;
2026-05-03T01:28:46.6209997Z                             ^
2026-05-03T01:28:46.6640339Z   CC      net/wireless/mlme.o
2026-05-03T01:28:46.6970395Z   CC      net/netfilter/xt_tcpmss.o
2026-05-03T01:28:46.8370225Z 1 warning generated.
2026-05-03T01:28:46.9506116Z   CC      drivers/misc/mediatek/ccci_util/ccci_util_md_rat.o
2026-05-03T01:28:47.2369770Z   AR      drivers/net/usb/built-in.a
2026-05-03T01:28:47.2671910Z   AR      drivers/net/wireless/admtek/built-in.a
2026-05-03T01:28:47.2937872Z   CC [M]  drivers/net/wireless/ath/ath9k/ar9002_hw.o
2026-05-03T01:28:47.5375728Z   CC      net/netfilter/xt_time.o
2026-05-03T01:28:47.7760661Z   CC      drivers/misc/mediatek/ccci_util/ccci_util_dummy.o
2026-05-03T01:28:48.2510351Z   CC      net/netfilter/xt_u32.o
2026-05-03T01:28:48.2820689Z   AR      drivers/misc/mediatek/ccci_util/built-in.a
2026-05-03T01:28:48.3010457Z   CC [M]  drivers/net/wireless/ath/ath9k/ar9003_hw.o
2026-05-03T01:28:48.3070249Z   CC      drivers/misc/mediatek/ccmni/ccmni.o
2026-05-03T01:28:48.7816871Z   CC      net/wireless/ibss.o
2026-05-03T01:28:48.8425341Z   AR      net/netfilter/built-in.a
2026-05-03T01:28:48.8980958Z   AR      drivers/net/wireless/ath/built-in.a
2026-05-03T01:28:48.9179085Z   CC      drivers/nvmem/core.o
2026-05-03T01:28:49.4630941Z   CC [M]  drivers/net/wireless/ath/ath9k/hw.o
2026-05-03T01:28:49.7280386Z   CC      drivers/nvmem/nvmem-sysfs.o
2026-05-03T01:28:49.8570398Z   AR      drivers/misc/mediatek/ccmni/built-in.a
2026-05-03T01:28:49.8710404Z ../drivers/misc/mediatek/ccu/src/Makefile:33: CCU_MAKE_FILE_CALLED
2026-05-03T01:28:49.8760434Z ../drivers/misc/mediatek/ccu/src/1.2/Makefile:28: CCU_INC=../drivers/misc/mediatek/ccu/src/mt6768/ccu_ext_interface
2026-05-03T01:28:49.8840356Z   CC      drivers/misc/mediatek/ccu/src/1.2/ccu_drv.o
2026-05-03T01:28:50.1153549Z   CC      drivers/nvmem/mtk-devinfo.o
2026-05-03T01:28:50.5020249Z   AR      drivers/nvmem/built-in.a
2026-05-03T01:28:50.5126783Z   CC      net/wireless/sme.o
2026-05-03T01:28:50.5730515Z   CC      drivers/misc/hardware_info.o
2026-05-03T01:28:50.5946694Z   CC      drivers/misc/mediatek/ccu/src/1.2/ccu_n3d_a.o
2026-05-03T01:28:50.9951398Z   CC      drivers/misc/mediatek/ccu/src/1.2/ccu_i2c.o
2026-05-03T01:28:51.1590945Z   CC      drivers/net/dummy.o
2026-05-03T01:28:51.2350492Z   CC [M]  drivers/net/wireless/ath/ath9k/ar9003_phy.o
2026-05-03T01:28:51.5900734Z   AR      drivers/misc/mediatek/ccu/src/1.2/built-in.a
2026-05-03T01:28:51.6080544Z   CC      drivers/misc/mediatek/ccu/src/mt6768/ccu_hw.o
2026-05-03T01:28:51.9030580Z   AR      drivers/net/wireless/atmel/built-in.a
2026-05-03T01:28:51.9219872Z   CC      net/xfrm/xfrm_policy.o
2026-05-03T01:28:52.4080476Z   CC      drivers/misc/mediatek/ccu/src/mt6768/ccu_reg.o
2026-05-03T01:28:52.5480520Z   CC      net/wireless/chan.o
2026-05-03T01:28:52.7420476Z   CC [M]  drivers/net/wireless/ath/ath9k/ar9002_phy.o
2026-05-03T01:28:52.7880794Z   CC      drivers/misc/mediatek/ccu/src/mt6768/ccu_kd_mailbox.o
2026-05-03T01:28:53.2777855Z   CC      drivers/misc/mediatek/ccu/src/mt6768/ccu_i2c_hw.o
2026-05-03T01:28:53.6541958Z   CC      drivers/misc/mediatek/ccu/src/mt6768/ccu_sw_ver.o
2026-05-03T01:28:53.6850842Z   CC [M]  drivers/net/wireless/ath/ath9k/ar5008_phy.o
2026-05-03T01:28:53.6870654Z drivers/misc/mediatek/ccu/src/mt6768/.tmp_ccu_sw_ver.o: no symbols
2026-05-03T01:28:53.6900735Z   AR      drivers/misc/mediatek/ccu/src/mt6768/built-in.a
2026-05-03T01:28:53.7030289Z   AR      drivers/misc/mediatek/ccu/src/built-in.a
2026-05-03T01:28:53.7210405Z   CC      drivers/misc/mediatek/cirq/mtk_sys_cirq.o
2026-05-03T01:28:54.2346566Z   CC      net/xfrm/xfrm_state.o
2026-05-03T01:28:54.5360496Z   CC      net/wireless/ethtool.o
2026-05-03T01:28:54.6865724Z   AR      drivers/misc/mediatek/cirq/built-in.a
2026-05-03T01:28:54.6908403Z   CC [M]  drivers/net/wireless/ath/ath9k/ar9002_calib.o
2026-05-03T01:28:54.7180686Z   CC      drivers/misc/mediatek/cmdq/bridge/cmdq-bdg-mailbox.o
2026-05-03T01:28:55.2525063Z ../drivers/misc/mediatek/cmdq/bridge/cmdq-bdg-mailbox.c:138:22: warning: cast to smaller integer type 'u32' (aka 'unsigned int') from 'void *' [-Wvoid-pointer-to-int-cast]
2026-05-03T01:28:55.2550015Z         return spi_read_reg((u32)thread->base + addr);
2026-05-03T01:28:55.2570172Z                             ^~~~~~~~~~~~~~~~~
2026-05-03T01:28:55.2600625Z ../drivers/misc/mediatek/cmdq/bridge/cmdq-bdg-mailbox.c:144:16: warning: cast to smaller integer type 'u32' (aka 'unsigned int') from 'void *' [-Wvoid-pointer-to-int-cast]
2026-05-03T01:28:55.2609980Z         spi_write_reg((u32)thread->base + addr, val);
2026-05-03T01:28:55.2610469Z                       ^~~~~~~~~~~~~~~~~
2026-05-03T01:28:55.2765789Z ../drivers/misc/mediatek/cmdq/bridge/cmdq-bdg-mailbox.c:359:3: warning: cast to smaller integer type 'u32' (aka 'unsigned int') from 'void *' [-Wvoid-pointer-to-int-cast]
2026-05-03T01:28:55.2790063Z                 (u32)thread->base + CMDQ_THR_STATUS, val, sizeof(u32) * 10);
2026-05-03T01:28:55.2809887Z                 ^~~~~~~~~~~~~~~~~
2026-05-03T01:28:55.2810978Z ../drivers/misc/mediatek/cmdq/bridge/cmdq-bdg-mailbox.c:362:15: warning: cast to smaller integer type 'u32' (aka 'unsigned int') from 'void *' [-Wvoid-pointer-to-int-cast]
2026-05-03T01:28:55.2812681Z         spi_read_mem((u32)thread->base + CMDQ_THR_SPR0, spr, sizeof(u32) * 4);
2026-05-03T01:28:55.2813229Z                      ^~~~~~~~~~~~~~~~~
2026-05-03T01:28:55.4830651Z 4 warnings generated.
2026-05-03T01:28:55.7122038Z   CC [M]  drivers/net/wireless/ath/ath9k/ar9003_calib.o
2026-05-03T01:28:55.8050522Z   CC      drivers/misc/mediatek/cmdq/bridge/cmdq-bdg-test.o
2026-05-03T01:28:56.1180385Z   CC      net/xfrm/xfrm_hash.o
2026-05-03T01:28:56.3040501Z   CC      net/wireless/mesh.o
2026-05-03T01:28:56.3117749Z   AR      drivers/misc/mediatek/cmdq/bridge/built-in.a
2026-05-03T01:28:56.3320840Z   CC      drivers/misc/mediatek/cmdq/mdp_sync/mdp_fence.o
2026-05-03T01:28:56.5610584Z   CC      net/xfrm/xfrm_input.o
2026-05-03T01:28:56.7130570Z   CC [M]  drivers/net/wireless/ath/ath9k/calib.o
2026-05-03T01:28:56.8242302Z   AR      drivers/misc/mediatek/cmdq/mdp_sync/built-in.a
2026-05-03T01:28:56.8670472Z   CC      drivers/misc/mediatek/cmdq/v3/mt6768/cmdq_mdp.o
2026-05-03T01:28:57.5705104Z   AR      drivers/misc/mediatek/cmdq/v3/mt6768/built-in.a
2026-05-03T01:28:57.5771090Z   CC      net/wireless/ap.o
2026-05-03T01:28:57.5820214Z   CC      drivers/misc/mediatek/cmdq/v3/cmdq_sec.o
2026-05-03T01:28:58.1420374Z   CC      net/xfrm/xfrm_output.o
2026-05-03T01:28:58.1640625Z   CC [M]  drivers/net/wireless/ath/ath9k/eeprom.o
2026-05-03T01:28:58.3735256Z   CC      drivers/misc/mediatek/cmdq/v3/cmdq_sec_mtee.o
2026-05-03T01:28:58.7180556Z   CC      net/wireless/trace.o
2026-05-03T01:28:59.0130458Z   CC      drivers/misc/mediatek/cmdq/v3/cmdq_sec_gp.o
2026-05-03T01:28:59.1838285Z   CC [M]  drivers/net/wireless/ath/ath9k/eeprom_def.o
2026-05-03T01:28:59.5540527Z   CC      drivers/misc/mediatek/cmdq/v3/cmdq_record.o
2026-05-03T01:28:59.5790626Z   CC      net/xfrm/xfrm_sysctl.o
2026-05-03T01:29:00.2983861Z   CC [M]  drivers/net/wireless/ath/ath9k/eeprom_4k.o
2026-05-03T01:29:00.5240555Z   CC      net/xfrm/xfrm_replay.o
2026-05-03T01:29:00.5970695Z   CC      drivers/misc/mediatek/cmdq/v3/cmdq_virtual.o
2026-05-03T01:29:01.2400657Z   CC      drivers/misc/mediatek/cmdq/v3/cmdq_device.o
2026-05-03T01:29:01.3281277Z   CC [M]  drivers/net/wireless/ath/ath9k/eeprom_9287.o
2026-05-03T01:29:01.8670387Z   CC      net/xfrm/xfrm_device.o
2026-05-03T01:29:01.9510344Z   CC      net/wireless/ocb.o
2026-05-03T01:29:01.9701541Z   CC      drivers/misc/mediatek/cmdq/v3/cmdq_driver.o
2026-05-03T01:29:02.3860390Z   CC [M]  drivers/net/wireless/ath/ath9k/ani.o
2026-05-03T01:29:02.7658630Z   CC      net/xfrm/xfrm_proc.o
2026-05-03T01:29:02.8081239Z   CC      drivers/misc/mediatek/cmdq/v3/cmdq_mdp_common.o
2026-05-03T01:29:03.2014513Z   CC      net/wireless/of.o
2026-05-03T01:29:03.6760582Z   CC      net/xfrm/xfrm_algo.o
2026-05-03T01:29:03.7620421Z   CC [M]  drivers/net/wireless/ath/ath9k/mac.o
2026-05-03T01:29:03.8633540Z   CC      drivers/misc/mediatek/cmdq/v3/cmdq_test.o
2026-05-03T01:29:04.3450427Z   CC      net/wireless/shipped-certs.o
2026-05-03T01:29:04.9380393Z   CC      net/wireless/wext-core.o
2026-05-03T01:29:05.0020450Z   CC      net/xfrm/xfrm_user.o
2026-05-03T01:29:05.2460690Z   CC [M]  drivers/net/wireless/ath/ath9k/ar9002_mac.o
2026-05-03T01:29:05.2640720Z   CC      drivers/misc/mediatek/cmdq/v3/cmdq_event_common.o
2026-05-03T01:29:05.8530435Z   CC      drivers/misc/mediatek/cmdq/v3/cmdq_subsys_common.o
2026-05-03T01:29:06.1371594Z   CC      net/wireless/wext-proc.o
2026-05-03T01:29:06.3900460Z   CC      drivers/misc/mediatek/cmdq/v3/cmdq_helper_ext.o
2026-05-03T01:29:06.6140651Z   CC [M]  drivers/net/wireless/ath/ath9k/ar9003_mac.o
2026-05-03T01:29:06.7521171Z   CC      net/wireless/wext-priv.o
2026-05-03T01:29:06.7670508Z   CC      net/xfrm/xfrm_ipcomp.o
2026-05-03T01:29:07.4890431Z   AR      net/wireless/built-in.a
2026-05-03T01:29:07.5113843Z   CC [M]  drivers/net/wireless/ath/main.o
2026-05-03T01:29:08.0255370Z   CC [M]  drivers/net/wireless/ath/ath9k/ar9003_eeprom.o
2026-05-03T01:29:08.1850118Z   CC      net/xfrm/xfrm_interface.o
2026-05-03T01:29:08.3753301Z   CC      drivers/misc/mediatek/cmdq/v3/cmdq_mmp.o
2026-05-03T01:29:08.7685043Z   CC      drivers/of/base.o
2026-05-03T01:29:08.9570640Z   AR      drivers/misc/mediatek/cmdq/v3/built-in.a
2026-05-03T01:29:08.9740452Z   AR      drivers/misc/mediatek/cmdq/built-in.a
2026-05-03T01:29:09.0010576Z   CC      drivers/misc/mediatek/conn_md/conn_md.o
2026-05-03T01:29:09.2100194Z   AR      net/xfrm/built-in.a
2026-05-03T01:29:09.2310497Z   CC      net/socket.o
2026-05-03T01:29:09.3550722Z   CC [M]  drivers/net/wireless/ath/ath9k/ar9003_paprd.o
2026-05-03T01:29:09.5790605Z   CC      drivers/misc/mediatek/conn_md/conn_md_exp.o
2026-05-03T01:29:09.6257734Z   CC      drivers/of/device.o
2026-05-03T01:29:10.3220495Z   CC      drivers/misc/mediatek/conn_md/conn_md_log.o
2026-05-03T01:29:10.4410708Z   CC      drivers/of/platform.o
2026-05-03T01:29:10.7468881Z   CC      drivers/misc/mediatek/conn_md/conn_md_dump.o
2026-05-03T01:29:10.7901700Z   CC [M]  drivers/net/wireless/ath/ath9k/btcoex.o
2026-05-03T01:29:11.2611172Z   CC      drivers/misc/mediatek/conn_md/conn_md_dbg.o
2026-05-03T01:29:11.2650302Z   CC      drivers/of/property.o
2026-05-03T01:29:11.3200335Z   CC      net/compat.o
2026-05-03T01:29:11.7708902Z   CC      drivers/misc/mediatek/conn_md/conn_md_test.o
2026-05-03T01:29:11.9210790Z   CC      drivers/of/kobj.o
2026-05-03T01:29:12.1775971Z   CC [M]  drivers/net/wireless/ath/ath9k/ar9003_mci.o
2026-05-03T01:29:12.2226459Z   AR      drivers/misc/mediatek/conn_md/built-in.a
2026-05-03T01:29:12.2450753Z   CC      drivers/of/fdt.o
2026-05-03T01:29:12.2470220Z   CC      drivers/misc/mediatek/connectivity/common/connectivity_build_in_adapter.o
2026-05-03T01:29:12.9631041Z ../drivers/net/wireless/ath/ath9k/ar9003_mci.c:588:21: warning: variable 'mismatch' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:12.9662416Z         u32 *p_gpm = NULL, mismatch = 0, more_data;
2026-05-03T01:29:12.9706929Z                            ^
2026-05-03T01:29:12.9707843Z ../drivers/net/wireless/ath/ath9k/ar9003_mci.c:1058:6: warning: variable 'new_flags' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:12.9737820Z         u32 new_flags, to_set, to_clear;
2026-05-03T01:29:12.9759897Z             ^
2026-05-03T01:29:12.9910363Z   CC      net/sysctl_net.o
2026-05-03T01:29:13.0900617Z 2 warnings generated.
2026-05-03T01:29:13.2080655Z   CC      drivers/of/fdt_address.o
2026-05-03T01:29:13.5157972Z   CC      drivers/of/address.o
2026-05-03T01:29:13.5500465Z   CC [M]  drivers/net/wireless/ath/ath9k/ar9003_aic.o
2026-05-03T01:29:13.6367238Z   CC      drivers/misc/mediatek/connectivity/common/wmt_build_in_adapter.o
2026-05-03T01:29:14.1388050Z   AR      net/built-in.a
2026-05-03T01:29:14.2032251Z   CC      drivers/misc/simtray.o
2026-05-03T01:29:14.2550648Z   CC      drivers/misc/mediatek/connectivity/power_throttling/adapter.o
2026-05-03T01:29:14.3890086Z   CC      drivers/of/irq.o
2026-05-03T01:29:14.5290435Z   CC [M]  drivers/net/wireless/ath/ath9k/common.o
2026-05-03T01:29:14.6640607Z   CC      drivers/net/ifb.o
2026-05-03T01:29:14.8983502Z   CC      drivers/misc/mediatek/connectivity/power_throttling/core.o
2026-05-03T01:29:15.1760732Z   AR      drivers/misc/mediatek/connectivity/built-in.a
2026-05-03T01:29:15.2080320Z   CC      drivers/misc/mediatek/cqdma/cqdma.o
2026-05-03T01:29:15.2730371Z   CC      drivers/of/of_net.o
2026-05-03T01:29:15.4290430Z   AR      drivers/net/wireless/broadcom/built-in.a
2026-05-03T01:29:15.4470247Z   CC      drivers/opp/core.o
2026-05-03T01:29:15.9252094Z   CC [M]  drivers/net/wireless/ath/ath9k/common-init.o
2026-05-03T01:29:16.0860513Z   AR      drivers/misc/mediatek/cqdma/built-in.a
2026-05-03T01:29:16.1040312Z   CC      drivers/misc/mediatek/dbgtop/dbgtop.o
2026-05-03T01:29:16.1903282Z   CC      drivers/opp/cpu.o
2026-05-03T01:29:16.2178814Z   CC      drivers/of/of_mdio.o
2026-05-03T01:29:16.7360765Z   CC      drivers/opp/of.o
2026-05-03T01:29:16.8620638Z   AR      drivers/misc/mediatek/dbgtop/built-in.a
2026-05-03T01:29:16.8953461Z   CC      drivers/misc/mediatek/debug_latch/lastbus/mt6768/plat_lastbus.o
2026-05-03T01:29:17.1750644Z   AR      drivers/misc/mediatek/debug_latch/lastbus/mt6768/built-in.a
2026-05-03T01:29:17.1815274Z   CC      drivers/misc/mediatek/debug_latch/lastbus/lastbus.o
2026-05-03T01:29:17.2431289Z   CC [M]  drivers/net/wireless/ath/ath9k/common-beacon.o
2026-05-03T01:29:17.3030383Z   CC      drivers/of/of_reserved_mem.o
2026-05-03T01:29:17.3180585Z   AR      drivers/opp/built-in.a
2026-05-03T01:29:17.3320131Z   CC [M]  drivers/net/wireless/ath/regd.o
2026-05-03T01:29:17.5300752Z   AR      drivers/misc/mediatek/debug_latch/lastbus/built-in.a
2026-05-03T01:29:17.5510850Z   CC      drivers/misc/mediatek/debug_latch/plat_dbg_info/plat_dbg_info.o
2026-05-03T01:29:18.0550432Z   AR      drivers/of/built-in.a
2026-05-03T01:29:18.0972073Z   AR      drivers/pci/controller/dwc/built-in.a
2026-05-03T01:29:18.1120509Z   AR      drivers/pci/controller/built-in.a
2026-05-03T01:29:18.1245794Z   AR      drivers/pci/switch/built-in.a
2026-05-03T01:29:18.1395882Z   AR      drivers/pci/built-in.a
2026-05-03T01:29:18.1505275Z   CC [M]  drivers/net/wireless/ath/ath9k/htc_hst.o
2026-05-03T01:29:18.1611114Z   CC      drivers/misc/mediatek/debug_latch/plat_dbg_info/plat_sram_flag.o
2026-05-03T01:29:18.5490826Z   CC      drivers/misc/cpumaxfreq.o
2026-05-03T01:29:18.6617993Z   AR      drivers/net/wireless/cisco/built-in.a
2026-05-03T01:29:18.6707085Z   CC      drivers/net/mii.o
2026-05-03T01:29:18.7248030Z   AR      drivers/misc/mediatek/debug_latch/plat_dbg_info/built-in.a
2026-05-03T01:29:18.7440303Z   AR      drivers/misc/mediatek/debug_latch/built-in.a
2026-05-03T01:29:18.7622819Z   CC      drivers/misc/mediatek/devinfo/devinfo.o
2026-05-03T01:29:18.9200260Z   CC      drivers/perf/arm_dsu_pmu.o
2026-05-03T01:29:19.0907388Z   CC [M]  drivers/net/wireless/ath/ath9k/hif_usb.o
2026-05-03T01:29:19.5521746Z   CC      drivers/perf/arm_pmu.o
2026-05-03T01:29:19.5550010Z   AR      drivers/misc/mediatek/devinfo/built-in.a
2026-05-03T01:29:19.5710267Z   CC      drivers/misc/mediatek/dfd/dfd.o
2026-05-03T01:29:19.7200404Z   CC [M]  drivers/net/wireless/ath/hw.o
2026-05-03T01:29:19.9470460Z   AR      drivers/misc/mediatek/dfd/built-in.a
2026-05-03T01:29:19.9710370Z   CC      drivers/misc/mediatek/dramc/mt6768/mtk_dramc.o
2026-05-03T01:29:20.1380856Z   CC [M]  drivers/net/wireless/ath/ath9k/wmi.o
2026-05-03T01:29:20.5413586Z   CC      drivers/perf/arm_pmu_platform.o
2026-05-03T01:29:20.7860640Z   AR      drivers/misc/mediatek/dramc/mt6768/built-in.a
2026-05-03T01:29:20.7950237Z   CC      drivers/misc/mediatek/dramc/dramc.o
2026-05-03T01:29:21.0407096Z   AR      drivers/phy/broadcom/built-in.a
2026-05-03T01:29:21.0561004Z   CC [M]  drivers/net/wireless/ath/ath9k/htc_drv_txrx.o
2026-05-03T01:29:21.0610338Z   AR      drivers/phy/hisilicon/built-in.a
2026-05-03T01:29:21.0756628Z   AR      drivers/phy/marvell/built-in.a
2026-05-03T01:29:21.0960478Z   CC      drivers/phy/mediatek/phy-mtk-tphy.o
2026-05-03T01:29:21.1440483Z   AR      drivers/perf/built-in.a
2026-05-03T01:29:21.1639250Z   AR      drivers/phy/motorola/built-in.a
2026-05-03T01:29:21.1799869Z   AR      drivers/net/wireless/intel/built-in.a
2026-05-03T01:29:21.1920447Z   CC      drivers/net/Space.o
2026-05-03T01:29:21.2385404Z   CC      drivers/misc/mediatek/dramc/mtk_lastdramc.o
2026-05-03T01:29:21.4761324Z ../drivers/phy/mediatek/phy-mtk-tphy.c:436:9: warning: variable 'temp' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:21.4790104Z         int i, temp;
2026-05-03T01:29:21.4790477Z                ^
2026-05-03T01:29:21.5060569Z ../drivers/phy/mediatek/phy-mtk-tphy.c:1555:17: warning: unused variable 'dev' [-Wunused-variable]
2026-05-03T01:29:21.5089948Z         struct device *dev = &instance->phy->dev;
2026-05-03T01:29:21.5119921Z                        ^
2026-05-03T01:29:21.7120585Z 2 warnings generated.
2026-05-03T01:29:21.7240528Z drivers/misc/mediatek/dramc/.tmp_mtk_lastdramc.o: no symbols
2026-05-03T01:29:21.7280299Z   CC      drivers/misc/mediatek/dramc/mtk_memtest.o
2026-05-03T01:29:21.7390615Z   AR      drivers/phy/mediatek/built-in.a
2026-05-03T01:29:21.7559671Z   AR      drivers/phy/qualcomm/built-in.a
2026-05-03T01:29:21.7726063Z   AR      drivers/phy/ralink/built-in.a
2026-05-03T01:29:21.7898005Z   AR      drivers/phy/samsung/built-in.a
2026-05-03T01:29:21.8074686Z   AR      drivers/phy/st/built-in.a
2026-05-03T01:29:21.8250307Z   AR      drivers/phy/ti/built-in.a
2026-05-03T01:29:21.8340308Z   CC      drivers/phy/phy-core.o
2026-05-03T01:29:21.8900797Z CONFIG_MTK_PLATFORM_CCCI := mt6768
2026-05-03T01:29:21.8925664Z CONFIG_MTK_PLATFORM_CCCI := "mt6768"
2026-05-03T01:29:21.8940126Z MTK_PLATFORM_CCCI := mt6768
2026-05-03T01:29:21.8970051Z CONFIG_MTK_PLATFORM := mt6768
2026-05-03T01:29:21.8982094Z CONFIG_MTK_PLATFORM := "mt6768"
2026-05-03T01:29:21.9023549Z MTK_PLATFORM := "mt6768"
2026-05-03T01:29:21.9040022Z CONFIG_MTK_PLATFORM := mt6768
2026-05-03T01:29:21.9059931Z CONFIG_MTK_PLATFORM := "mt6768"
2026-05-03T01:29:21.9089912Z MTK_PLATFORM := "mt6768"
2026-05-03T01:29:21.9120047Z   CC      drivers/misc/mediatek/eccci/mt6768/ccci_platform.o
2026-05-03T01:29:22.1560651Z   CC [M]  drivers/net/wireless/ath/ath9k/htc_drv_main.o
2026-05-03T01:29:22.2130678Z drivers/misc/mediatek/dramc/.tmp_mtk_memtest.o: no symbols
2026-05-03T01:29:22.2170026Z   CC      drivers/misc/mediatek/dramc/mtk_rshmoo.o
2026-05-03T01:29:22.4640501Z   AR      drivers/phy/built-in.a
2026-05-03T01:29:22.4790481Z   CC [M]  drivers/net/wireless/ath/key.o
2026-05-03T01:29:22.6570703Z drivers/misc/mediatek/dramc/.tmp_mtk_rshmoo.o: no symbols
2026-05-03T01:29:22.6640095Z   AR      drivers/misc/mediatek/dramc/built-in.a
2026-05-03T01:29:22.6840488Z   AR      drivers/net/wireless/intersil/built-in.a
2026-05-03T01:29:22.6930272Z   CC      drivers/net/loopback.o
2026-05-03T01:29:22.9840773Z   CC      drivers/misc/mediatek/eccci/mt6768/md_sys1_platform.o
2026-05-03T01:29:23.2229180Z   CC [M]  drivers/net/wireless/ath/ath9k/htc_drv_beacon.o
2026-05-03T01:29:23.5570576Z   CC      drivers/misc/mediatek/eccci/fsm/ccci_fsm.o
2026-05-03T01:29:23.8773561Z   AR      drivers/pinctrl/actions/built-in.a
2026-05-03T01:29:23.8940533Z   AR      drivers/pinctrl/bcm/built-in.a
2026-05-03T01:29:23.9120205Z   AR      drivers/pinctrl/cirrus/built-in.a
2026-05-03T01:29:23.9180188Z   AR      drivers/misc/mediatek/eccci/mt6768/built-in.a
2026-05-03T01:29:23.9270321Z   AR      drivers/pinctrl/freescale/built-in.a
2026-05-03T01:29:23.9422807Z   CC      drivers/misc/mediatek/emi/mt6768/bwl_platform.o
2026-05-03T01:29:23.9482234Z   CC      drivers/pinctrl/mediatek/mtk-eint.o
2026-05-03T01:29:24.2020948Z   CC [M]  drivers/net/wireless/ath/ath9k/htc_drv_init.o
2026-05-03T01:29:24.4020682Z   CC      drivers/misc/mediatek/emi/mt6768/mpu_platform.o
2026-05-03T01:29:24.6770738Z   CC      drivers/pinctrl/mediatek/pinctrl-mtk-common-v2.o
2026-05-03T01:29:24.8560631Z   CC      drivers/misc/mediatek/emi/mt6768/plat_debug_api.o
2026-05-03T01:29:25.0170507Z   CC      drivers/misc/mediatek/eccci/fsm/ccci_fsm_ioctl.o
2026-05-03T01:29:25.0990924Z ../drivers/pinctrl/mediatek/pinctrl-mtk-common-v2.c:118:39: warning: variable 'e' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:25.1000102Z         const struct mtk_pin_field_calc *c, *e;
2026-05-03T01:29:25.1020149Z                                              ^
2026-05-03T01:29:25.1980467Z 1 warning generated.
2026-05-03T01:29:25.2727223Z   CC [M]  drivers/net/wireless/ath/ath9k/htc_drv_gpio.o
2026-05-03T01:29:25.3500537Z   CC      drivers/misc/mediatek/emi/mt6768/../emi_ctrl_v1.o
2026-05-03T01:29:25.4320296Z   CC      drivers/pinctrl/mediatek/pinctrl-paris.o
2026-05-03T01:29:25.8988024Z   CC      drivers/misc/mediatek/eccci/fsm/ccci_fsm_monitor.o
2026-05-03T01:29:26.0500586Z   CC      drivers/misc/mediatek/emi/mt6768/../submodule/bwl_v1.o
2026-05-03T01:29:26.1820005Z   LD [M]  drivers/net/wireless/ath/ath9k/ath9k_hw.o
2026-05-03T01:29:26.2045619Z   CC      drivers/pinctrl/mediatek/pinctrl-mtk-common-v2_debug.o
2026-05-03T01:29:26.2430737Z   LD [M]  drivers/net/wireless/ath/ath9k/ath9k_common.o
2026-05-03T01:29:26.2720581Z   LD [M]  drivers/net/wireless/ath/ath9k/ath9k_htc.o
2026-05-03T01:29:26.3020730Z   CC [M]  drivers/net/wireless/ath/dfs_pattern_detector.o
2026-05-03T01:29:26.5620823Z   CC      drivers/misc/mediatek/emi/mt6768/../submodule/mpu_v1.o
2026-05-03T01:29:26.5621993Z   CC      drivers/misc/mediatek/eccci/fsm/ccci_fsm_poller.o
2026-05-03T01:29:26.6271227Z ../drivers/pinctrl/mediatek/pinctrl-mtk-common-v2_debug.c:252:20: warning: variable 'chip' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:26.6272322Z         struct gpio_chip *chip;
2026-05-03T01:29:26.6330082Z                           ^
2026-05-03T01:29:26.6827059Z 1 warning generated.
2026-05-03T01:29:26.9330266Z   CC      drivers/pinctrl/mediatek/pinctrl-mt6768.o
2026-05-03T01:29:27.2251032Z   CC      drivers/misc/mediatek/eccci/fsm/ccci_fsm_scp.o
2026-05-03T01:29:27.4418415Z   AR      drivers/pinctrl/mediatek/built-in.a
2026-05-03T01:29:27.4660433Z   AR      drivers/pinctrl/mvebu/built-in.a
2026-05-03T01:29:27.4918820Z   AR      drivers/pinctrl/nomadik/built-in.a
2026-05-03T01:29:27.5161156Z   CC      drivers/misc/mediatek/emi/mt6768/../submodule/elm_v2.o
2026-05-03T01:29:27.5200259Z   AR      drivers/pinctrl/sprd/built-in.a
2026-05-03T01:29:27.5372340Z   AR      drivers/pinctrl/ti/built-in.a
2026-05-03T01:29:27.5456588Z   CC      drivers/pinctrl/core.o
2026-05-03T01:29:27.5770535Z   CC [M]  drivers/net/wireless/ath/dfs_pri_detector.o
2026-05-03T01:29:28.0700230Z   CC      drivers/misc/mediatek/emi/mt6768/../submodule/pasr_api_v1.o
2026-05-03T01:29:28.2812100Z   CC      drivers/misc/mediatek/eccci/fsm/ccci_fsm_ee.o
2026-05-03T01:29:28.3462541Z   AR      drivers/misc/mediatek/emi/mt6768/built-in.a
2026-05-03T01:29:28.3650340Z   AR      drivers/misc/mediatek/emi/built-in.a
2026-05-03T01:29:28.3840278Z   AR      drivers/net/wireless/marvell/built-in.a
2026-05-03T01:29:28.3950163Z   CC      drivers/net/tun.o
2026-05-03T01:29:28.4020114Z   CC      drivers/pinctrl/pinctrl-utils.o
2026-05-03T01:29:28.4219993Z   LD [M]  drivers/net/wireless/ath/ath.o
2026-05-03T01:29:28.4600502Z   AR      drivers/net/wireless/mediatek/built-in.a
2026-05-03T01:29:28.4750101Z   AR      drivers/net/wireless/quantenna/built-in.a
2026-05-03T01:29:28.4930210Z   AR      drivers/net/wireless/ralink/built-in.a
2026-05-03T01:29:28.5080227Z   AR      drivers/net/wireless/realtek/built-in.a
2026-05-03T01:29:28.5260471Z   AR      drivers/net/wireless/rsi/built-in.a
2026-05-03T01:29:28.5440326Z   AR      drivers/net/wireless/st/built-in.a
2026-05-03T01:29:28.5580155Z   AR      drivers/net/wireless/ti/built-in.a
2026-05-03T01:29:28.5760180Z   AR      drivers/net/wireless/zydas/built-in.a
2026-05-03T01:29:28.6044005Z   AR      drivers/net/wireless/built-in.a
2026-05-03T01:29:28.6230339Z   AR      drivers/platform/built-in.a
2026-05-03T01:29:28.6456126Z   CC      drivers/misc/mediatek/eccci/hif/ccci_hif.o
2026-05-03T01:29:28.9920959Z   CC      drivers/misc/mediatek/eccci/fsm/ccci_fsm_sys.o
2026-05-03T01:29:28.9929963Z   CC      drivers/pinctrl/pinmux.o
2026-05-03T01:29:29.4360257Z   CC      drivers/pinctrl/pinconf.o
2026-05-03T01:29:29.6900619Z   CC      drivers/misc/mediatek/eccci/fsm/mdee_dumper_v1.o
2026-05-03T01:29:29.7400547Z   CC      drivers/misc/mediatek/eccci/hif/ccci_cldma_plat.o
2026-05-03T01:29:29.8550611Z   CC      drivers/pinctrl/devicetree.o
2026-05-03T01:29:30.4250465Z   CC      drivers/misc/mediatek/eccci/hif/ccci_hif_cldma.o
2026-05-03T01:29:30.4310295Z   CC      drivers/misc/mediatek/eccci/fsm/mdee_dumper_v2.o
2026-05-03T01:29:30.4831088Z   CC      drivers/net/veth.o
2026-05-03T01:29:30.4840157Z   CC      drivers/pinctrl/pinconf-generic.o
2026-05-03T01:29:31.1701314Z   AR      drivers/pinctrl/built-in.a
2026-05-03T01:29:31.1860236Z   CC      drivers/misc/mediatek/eccci/fsm/mdee_dumper_v3.o
2026-05-03T01:29:31.1990536Z   AR      drivers/misc/mediatek/ext_disp/common/built-in.a
2026-05-03T01:29:31.2300475Z   CC      drivers/misc/mediatek/ext_disp/mt6768/external_display.o
2026-05-03T01:29:31.7418051Z   AR      drivers/net/built-in.a
2026-05-03T01:29:31.7709036Z   CC      drivers/misc/mediatek/eccci/port/port_cfg.o
2026-05-03T01:29:31.8259540Z   CC      drivers/misc/mediatek/eccci/hif/ccci_hif_dpmaif.o
2026-05-03T01:29:31.9840574Z   CC      drivers/misc/mediatek/eccci/fsm/mdee_dumper_v5.o
2026-05-03T01:29:32.2181541Z   CC      drivers/misc/mediatek/ext_disp/mt6768/mtk_extd_mgr.o
2026-05-03T01:29:32.6371133Z ../drivers/misc/mediatek/eccci/hif/ccci_hif_dpmaif.c:452:4: warning: cast to smaller integer type 'u32' (aka 'unsigned int') from 'u64 *' (aka 'unsigned long long *') [-Wpointer-to-int-cast]
2026-05-03T01:29:32.6410001Z                         (u32)data_64ptr, (i * 8),
2026-05-03T01:29:32.6470259Z                         ^~~~~~~~~~~~~~~
2026-05-03T01:29:32.6501010Z ../drivers/misc/mediatek/eccci/hif/ccci_hif_dpmaif.c:119:51: note: expanded from macro 'DPMA_DRB_DATA_INFO'
2026-05-03T01:29:32.6501928Z         ccci_dump_write(0, CCCI_DUMP_DPMA_DRB, 0, fmt, ##args)
2026-05-03T01:29:32.6502454Z                                                          ^~~~
2026-05-03T01:29:32.6503558Z ../drivers/misc/mediatek/eccci/hif/ccci_hif_dpmaif.c:465:37: warning: cast to smaller integer type 'u32' (aka 'unsigned int') from 'u8 *' (aka 'unsigned char *') [-Wpointer-to-int-cast]
2026-05-03T01:29:32.6504822Z                 DPMA_DRB_DATA_INFO("%08X(%04d):", (u32)data_8ptr, count * 8);
2026-05-03T01:29:32.6505374Z                                                   ^~~~~~~~~~~~~~
2026-05-03T01:29:32.6506112Z ../drivers/misc/mediatek/eccci/hif/ccci_hif_dpmaif.c:119:51: note: expanded from macro 'DPMA_DRB_DATA_INFO'
2026-05-03T01:29:32.6506927Z         ccci_dump_write(0, CCCI_DUMP_DPMA_DRB, 0, fmt, ##args)
2026-05-03T01:29:32.6507418Z                                                          ^~~~
2026-05-03T01:29:32.7510682Z   AR      drivers/misc/mediatek/eccci/fsm/built-in.a
2026-05-03T01:29:32.7861417Z   CC      drivers/misc/mediatek/ext_gic/mt6768/plat_sw_mode.o
2026-05-03T01:29:32.7921912Z   CC      drivers/misc/mediatek/eccci/port/port_char.o
2026-05-03T01:29:32.8258337Z   AR      drivers/misc/mediatek/ext_gic/mt6768/built-in.a
2026-05-03T01:29:32.8350359Z   CC      drivers/misc/mediatek/ext_gic/mtk-gic-v3-extend.o
2026-05-03T01:29:32.9181499Z   CC      drivers/misc/mediatek/ext_disp/mt6768/extd_debug.o
2026-05-03T01:29:32.9521386Z drivers/misc/mediatek/ext_disp/mt6768/.tmp_extd_debug.o: no symbols
2026-05-03T01:29:32.9583796Z   CC      drivers/misc/mediatek/ext_disp/mt6768/extd_utils.o
2026-05-03T01:29:33.2781082Z 2 warnings generated.
2026-05-03T01:29:33.4939180Z   CC      drivers/misc/mediatek/eccci/port/port_ctlmsg.o
2026-05-03T01:29:33.5109092Z   AR      drivers/misc/mediatek/ext_gic/built-in.a
2026-05-03T01:29:33.5190227Z   CC      drivers/misc/mediatek/ext_disp/mt6768/extd_hdmi.o
2026-05-03T01:29:33.5578925Z   CC      drivers/power/reset/reboot-mode.o
2026-05-03T01:29:33.5650453Z   CC      drivers/misc/mediatek/ext_disp/mt6768/extd_epd.o
2026-05-03T01:29:33.6100461Z   CC      drivers/misc/mediatek/ext_disp/mt6768/extd_lcm.o
2026-05-03T01:29:33.6550604Z   CC      drivers/misc/mediatek/ext_disp/mt6768/extd_multi_control.o
2026-05-03T01:29:33.6924113Z   CC      drivers/misc/mediatek/eccci/hif/dpmaif_drv.o
2026-05-03T01:29:34.0340558Z   CC      drivers/power/reset/syscon-reboot-mode.o
2026-05-03T01:29:34.1310515Z   CC      drivers/misc/mediatek/eccci/port/port_udc.o
2026-05-03T01:29:34.3530554Z   AR      drivers/power/reset/built-in.a
2026-05-03T01:29:34.3575021Z   CC      drivers/misc/mediatek/ext_disp/mt6768/extd_factory.o
2026-05-03T01:29:34.3853336Z   CC      drivers/power/supply/mediatek/battery/mtk_battery.o
2026-05-03T01:29:34.4330589Z   CC      drivers/misc/mediatek/eccci/hif/ccci_debug_info.o
2026-05-03T01:29:34.9420328Z   AR      drivers/misc/mediatek/ext_disp/mt6768/built-in.a
2026-05-03T01:29:34.9549530Z   AR      drivers/misc/mediatek/ext_disp/built-in.a
2026-05-03T01:29:34.9740646Z   CC      drivers/misc/mediatek/eccci/udc/udc.o
2026-05-03T01:29:34.9910431Z   CC      drivers/misc/mediatek/eccci/port/port_misc.o
2026-05-03T01:29:35.1380627Z   CC      drivers/misc/mediatek/eccci/hif/net_speed_monitor.o
2026-05-03T01:29:35.2490516Z ../drivers/power/supply/mediatek/battery/mtk_battery.c:2005:9: warning: variable 'uid' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:35.2519980Z         kuid_t uid;
2026-05-03T01:29:35.2550062Z                ^
2026-05-03T01:29:35.2749350Z ../drivers/power/supply/mediatek/battery/mtk_battery.c:3504:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:35.2759890Z         int ret;
2026-05-03T01:29:35.2760192Z             ^
2026-05-03T01:29:35.2761254Z ../drivers/power/supply/mediatek/battery/mtk_battery.c:3546:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:35.2762139Z         int ret;
2026-05-03T01:29:35.2762825Z             ^
2026-05-03T01:29:35.2764068Z ../drivers/power/supply/mediatek/battery/mtk_battery.c:3595:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:35.2790049Z         int ret;
2026-05-03T01:29:35.2814050Z             ^
2026-05-03T01:29:35.2842899Z ../drivers/power/supply/mediatek/battery/mtk_battery.c:3651:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:35.2854477Z         int ret;
2026-05-03T01:29:35.2874003Z             ^
2026-05-03T01:29:35.2900564Z ../drivers/power/supply/mediatek/battery/mtk_battery.c:3709:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:35.2929925Z         int ret;
2026-05-03T01:29:35.2959889Z             ^
2026-05-03T01:29:35.2960724Z ../drivers/power/supply/mediatek/battery/mtk_battery.c:3763:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:35.2961621Z         int ret;
2026-05-03T01:29:35.2961894Z             ^
2026-05-03T01:29:35.2962663Z ../drivers/power/supply/mediatek/battery/mtk_battery.c:3806:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:35.2963493Z         int ret;
2026-05-03T01:29:35.2963761Z             ^
2026-05-03T01:29:35.2964522Z ../drivers/power/supply/mediatek/battery/mtk_battery.c:3852:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:35.2965380Z         int ret;
2026-05-03T01:29:35.2965644Z             ^
2026-05-03T01:29:35.2966410Z ../drivers/power/supply/mediatek/battery/mtk_battery.c:4302:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:35.2999947Z         int ret = 0;
2026-05-03T01:29:35.3026883Z             ^
2026-05-03T01:29:35.3058726Z ../drivers/power/supply/mediatek/battery/mtk_battery.c:4666:23: warning: variable 'class_dev' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:35.3080075Z         struct class_device *class_dev = NULL;
2026-05-03T01:29:35.3090010Z                              ^
2026-05-03T01:29:35.3120536Z ../drivers/power/supply/mediatek/battery/mtk_battery.c:4664:6: warning: variable 'ret_device_file' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:35.3140006Z         int ret_device_file = 0;
2026-05-03T01:29:35.3170018Z             ^
2026-05-03T01:29:35.3170902Z ../drivers/power/supply/mediatek/battery/mtk_battery.c:4971:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:35.3199977Z         int ret;
2026-05-03T01:29:35.3230001Z             ^
2026-05-03T01:29:35.3530494Z   AR      drivers/misc/mediatek/eccci/udc/built-in.a
2026-05-03T01:29:35.3710211Z   AR      drivers/ptp/built-in.a
2026-05-03T01:29:35.3920422Z   CC      drivers/power/supply/mediatek/charger/charger_class.o
2026-05-03T01:29:35.6720387Z 13 warnings generated.
2026-05-03T01:29:35.7086638Z   CC      drivers/misc/mediatek/eccci/port/port_ipc.o
2026-05-03T01:29:35.7170587Z   CC      drivers/power/supply/mediatek/battery/mtk_power_misc.o
2026-05-03T01:29:35.9620463Z   CC      drivers/misc/mediatek/eccci/hif/ccci_ringbuf.o
2026-05-03T01:29:35.9810501Z   CC      drivers/power/supply/mediatek/charger/mtk_charger.o
2026-05-03T01:29:36.4560974Z ../drivers/power/supply/mediatek/battery/mtk_power_misc.c:497:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:36.4620261Z         int ret = 0;
2026-05-03T01:29:36.4658479Z             ^
2026-05-03T01:29:36.4693021Z   CC      drivers/misc/mediatek/eccci/port/port_net.o
2026-05-03T01:29:36.5430407Z 1 warning generated.
2026-05-03T01:29:36.5830811Z   CC      drivers/power/supply/mediatek/battery/mtk_gauge_coulomb_service.o
2026-05-03T01:29:36.7120817Z   CC      drivers/misc/mediatek/eccci/hif/ccci_hif_ccif.o
2026-05-03T01:29:36.8951118Z ../drivers/power/supply/mediatek/charger/mtk_charger.c:3072:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:36.8980195Z         int ret;
2026-05-03T01:29:36.9009879Z             ^
2026-05-03T01:29:36.9011150Z ../drivers/power/supply/mediatek/charger/mtk_charger.c:3105:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:36.9012089Z         int ret;
2026-05-03T01:29:36.9039967Z             ^
2026-05-03T01:29:36.9040786Z ../drivers/power/supply/mediatek/charger/mtk_charger.c:3135:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:36.9069768Z         int ret;
2026-05-03T01:29:36.9099956Z             ^
2026-05-03T01:29:36.9100951Z ../drivers/power/supply/mediatek/charger/mtk_charger.c:3164:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:36.9128597Z         int ret;
2026-05-03T01:29:36.9160185Z             ^
2026-05-03T01:29:36.9190417Z ../drivers/power/supply/mediatek/charger/mtk_charger.c:3193:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:36.9191425Z         int ret;
2026-05-03T01:29:36.9219986Z             ^
2026-05-03T01:29:36.9250618Z ../drivers/power/supply/mediatek/charger/mtk_charger.c:3715:9: warning: variable 'uid' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:36.9279926Z         kuid_t uid;
2026-05-03T01:29:36.9280256Z                ^
2026-05-03T01:29:36.9281087Z ../drivers/power/supply/mediatek/charger/mtk_charger.c:3925:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:36.9281993Z         int ret;
2026-05-03T01:29:36.9282289Z             ^
2026-05-03T01:29:36.9283043Z ../drivers/power/supply/mediatek/charger/mtk_charger.c:3968:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:36.9283922Z         int ret;
2026-05-03T01:29:36.9284185Z             ^
2026-05-03T01:29:36.9284930Z ../drivers/power/supply/mediatek/charger/mtk_charger.c:4009:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:36.9285771Z         int ret;
2026-05-03T01:29:36.9286031Z             ^
2026-05-03T01:29:36.9286766Z ../drivers/power/supply/mediatek/charger/mtk_charger.c:4050:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:36.9287615Z         int ret;
2026-05-03T01:29:36.9287882Z             ^
2026-05-03T01:29:36.9288591Z ../drivers/power/supply/mediatek/charger/mtk_charger.c:4091:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:36.9289647Z         int ret;
2026-05-03T01:29:36.9289928Z             ^
2026-05-03T01:29:36.9290663Z ../drivers/power/supply/mediatek/charger/mtk_charger.c:4127:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:36.9291500Z         int ret;
2026-05-03T01:29:36.9291765Z             ^
2026-05-03T01:29:36.9292556Z ../drivers/power/supply/mediatek/charger/mtk_charger.c:4166:6: warning: variable 'ret_device_file' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:36.9293491Z         int ret_device_file;
2026-05-03T01:29:36.9293828Z             ^
2026-05-03T01:29:37.3630359Z 13 warnings generated.
2026-05-03T01:29:37.4066483Z   CC      drivers/misc/mediatek/eccci/port/port_poller.o
2026-05-03T01:29:37.4850821Z   CC      drivers/power/supply/mediatek/battery/mtk_gauge_class.o
2026-05-03T01:29:37.8880594Z   CC      drivers/power/supply/mediatek/charger/mtk_switch_charging.o
2026-05-03T01:29:38.0750885Z   CC      drivers/misc/mediatek/eccci/port/port_proxy.o
2026-05-03T01:29:38.3628516Z   AR      drivers/misc/mediatek/eccci/hif/built-in.a
2026-05-03T01:29:38.3750485Z   CC      drivers/misc/mediatek/eccci/ccci_core.o
2026-05-03T01:29:38.7458665Z   CC      drivers/power/supply/mediatek/charger/mtk_pdc_intf.o
2026-05-03T01:29:38.7820574Z   CC      drivers/power/supply/mediatek/battery/mtk_battery_recovery.o
2026-05-03T01:29:39.4110453Z   CC      drivers/power/supply/power_supply_core.o
2026-05-03T01:29:39.6120663Z   CC      drivers/power/supply/mediatek/charger/mtk_chg_type_det.o
2026-05-03T01:29:39.7395089Z   CC      drivers/misc/mediatek/eccci/port/port_rpc.o
2026-05-03T01:29:39.7630883Z   CC      drivers/power/supply/mediatek/battery/mtk_battery_core.o
2026-05-03T01:29:40.0550508Z   CC      drivers/misc/mediatek/extcon/extcon-mtk-usb.o
2026-05-03T01:29:40.6400720Z   CC      drivers/power/supply/mediatek/charger/mtk_pe40_intf.o
2026-05-03T01:29:40.6444288Z   CC      drivers/misc/mediatek/eccci/port/port_smem.o
2026-05-03T01:29:40.7010028Z ../drivers/power/supply/mediatek/battery/mtk_battery_core.c:2858:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:40.7032597Z         int ret = 0;
2026-05-03T01:29:40.7069122Z             ^
2026-05-03T01:29:40.7079713Z ../drivers/power/supply/mediatek/battery/mtk_battery_core.c:2938:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:40.7108703Z         int ret = 0;
2026-05-03T01:29:40.7140011Z             ^
2026-05-03T01:29:40.8190491Z   AR      drivers/misc/mediatek/extcon/built-in.a
2026-05-03T01:29:40.8400450Z   CC      drivers/power/supply/mediatek/misc/mtk_gauge_time_service.o
2026-05-03T01:29:41.1330567Z 2 warnings generated.
2026-05-03T01:29:41.1790468Z   AR      drivers/power/supply/mediatek/battery/built-in.a
2026-05-03T01:29:41.1970186Z   AR      drivers/pwm/built-in.a
2026-05-03T01:29:41.2110270Z   CC      drivers/misc/mediatek/eccci/ccci_bm.o
2026-05-03T01:29:41.4225486Z   AR      drivers/power/supply/mediatek/misc/built-in.a
2026-05-03T01:29:41.4410585Z ../drivers/power/supply/mediatek/charger/mtk_pe40_intf.c  CC      drivers/regulator/core.o
2026-05-03T01:29:41.4450337Z :524:19: warning: variable 'pe40' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:41.4462828Z         struct mtk_pe40 *pe40 = NULL;
2026-05-03T01:29:41.4499833Z                          ^
2026-05-03T01:29:41.4530409Z ../drivers/power/supply/mediatek/charger/mtk_pe40_intf.c:525:23: warning: variable 'pdata' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:41.4559925Z         struct charger_data *pdata = NULL;
2026-05-03T01:29:41.4589924Z                              ^
2026-05-03T01:29:41.4620473Z ../drivers/power/supply/mediatek/charger/mtk_pe40_intf.c:945:22: warning: variable 'cv' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:41.4649865Z         int icl, ccl, ccl2, cv, max_icl;
2026-05-03T01:29:41.4679940Z                             ^
2026-05-03T01:29:41.4688153Z ../drivers/power/supply/mediatek/charger/mtk_pe40_intf.c:950:6: warning: variable 'watt' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:41.4689116Z         int watt;
2026-05-03T01:29:41.4689616Z             ^
2026-05-03T01:29:41.4690417Z ../drivers/power/supply/mediatek/charger/mtk_pe40_intf.c:951:6: warning: variable 'max_watt' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:41.4691340Z         int max_watt;
2026-05-03T01:29:41.4691643Z             ^
2026-05-03T01:29:41.5450651Z 5 warnings generated.
2026-05-03T01:29:41.5851433Z   CC      drivers/power/supply/mediatek/charger/mtk_linear_charging.o
2026-05-03T01:29:41.8407027Z   CC      drivers/misc/mediatek/eccci/port/port_sysmsg.o
2026-05-03T01:29:42.2460748Z   CC      drivers/power/supply/power_supply_sysfs.o
2026-05-03T01:29:42.4600298Z   CC      drivers/misc/mediatek/eccci/port/ccci_swtp.o
2026-05-03T01:29:42.4810493Z   CC      drivers/power/supply/mediatek/charger/adapter_class.o
2026-05-03T01:29:42.6410737Z   CC      drivers/misc/mediatek/flashlight/flashlight-core.o
2026-05-03T01:29:42.9458947Z   CC      drivers/power/supply/mediatek/charger/mtk_pd_adapter.o
2026-05-03T01:29:43.0518608Z   CC      drivers/regulator/dummy.o
2026-05-03T01:29:43.0802308Z   AR      drivers/misc/mediatek/eccci/port/built-in.a
2026-05-03T01:29:43.0946636Z   CC      drivers/misc/mediatek/eccci/ccci_modem.o
2026-05-03T01:29:43.5620587Z   CC      drivers/misc/mediatek/flashlight/flashlight-device.o
2026-05-03T01:29:43.6090570Z   CC      drivers/regulator/fixed-helper.o
2026-05-03T01:29:43.6880653Z   CC      drivers/misc/mediatek/flashlight/flashlights-aw3641e.o
2026-05-03T01:29:43.8329834Z   CC      drivers/power/supply/mediatek/charger/mtk_switch_charging2.o
2026-05-03T01:29:44.1342734Z   CC      drivers/regulator/helpers.o
2026-05-03T01:29:44.2590618Z   AR      drivers/misc/mediatek/flashlight/built-in.a
2026-05-03T01:29:44.2898863Z   AR      drivers/reset/hisilicon/built-in.a
2026-05-03T01:29:44.3100491Z   CC      drivers/reset/core.o
2026-05-03T01:29:44.3765205Z   CC      drivers/misc/mediatek/eccci/ccci_rtc.o
2026-05-03T01:29:44.6834973Z   CC      drivers/regulator/devres.o
2026-05-03T01:29:44.7778551Z   CC      drivers/power/supply/mediatek/charger/mtk_intf.o
2026-05-03T01:29:44.9270558Z   AR      drivers/reset/built-in.a
2026-05-03T01:29:44.9400289Z   CC      drivers/power/supply/power_supply_leds.o
2026-05-03T01:29:45.2280742Z   CC      drivers/misc/mediatek/flashlight/richtek/rt-flashlight.o
2026-05-03T01:29:45.3645492Z   CC      drivers/misc/mediatek/eccci/modem_sys1.o
2026-05-03T01:29:45.5290398Z   CC      drivers/regulator/of_regulator.o
2026-05-03T01:29:45.5678972Z   CC      drivers/power/supply/mediatek/charger/mtk_pe40.o
2026-05-03T01:29:45.7250485Z   CC      drivers/misc/mediatek/flashlight/richtek/rtfled.o
2026-05-03T01:29:46.2370770Z   AR      drivers/misc/mediatek/flashlight/richtek/built-in.a
2026-05-03T01:29:46.2566299Z   CC      drivers/rtc/rtc-lib.o
2026-05-03T01:29:46.3150903Z ../drivers/power/supply/mediatek/charger/mtk_pe40.c:683:6: warning: variable 'watt' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:46.3179972Z         int watt;
2026-05-03T01:29:46.3209861Z             ^
2026-05-03T01:29:46.3240443Z ../drivers/power/supply/mediatek/charger/mtk_pe40.c:684:6: warning: variable 'max_watt' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:46.3269858Z         int max_watt;
2026-05-03T01:29:46.3284885Z             ^
2026-05-03T01:29:46.3323752Z ../drivers/power/supply/mediatek/charger/mtk_pe40.c:680:16: warning: variable 'cv' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:46.3360117Z         int icl, ccl, cv, max_icl;
2026-05-03T01:29:46.3378033Z                       ^
2026-05-03T01:29:46.3790365Z 3 warnings generated.
2026-05-03T01:29:46.4220435Z   CC      drivers/regulator/mt6358-regulator.o
2026-05-03T01:29:46.4335610Z   CC      drivers/power/supply/mediatek/charger/mtk_pdc.o
2026-05-03T01:29:46.6421516Z   CC      drivers/misc/mediatek/eccci/ccci_md_clk.o
2026-05-03T01:29:46.8530768Z   CC      drivers/rtc/hctosys.o
2026-05-03T01:29:47.0590969Z   AR      drivers/regulator/built-in.a
2026-05-03T01:29:47.0760225Z   CC      drivers/rtc/class.o
2026-05-03T01:29:47.2783874Z   CC      drivers/misc/mediatek/freqhopping/mt6768/mtk_freqhopping_sspm.o
2026-05-03T01:29:47.2880934Z   CC      drivers/power/supply/mediatek/charger/syv690.o
2026-05-03T01:29:47.3280586Z   CC      drivers/misc/mediatek/eccci/ccci_auxadc.o
2026-05-03T01:29:47.7756455Z   CC      drivers/rtc/interface.o
2026-05-03T01:29:47.8500665Z   AR      drivers/misc/mediatek/freqhopping/mt6768/built-in.a
2026-05-03T01:29:47.8590383Z   CC      drivers/misc/mediatek/freqhopping/mtk_freqhopping_drv.o
2026-05-03T01:29:48.3770647Z   AR      drivers/misc/mediatek/eccci/built-in.a
2026-05-03T01:29:48.4035030Z   GEN     drivers/scsi/scsi_devinfo_tbl.c
2026-05-03T01:29:48.4170348Z   CC      drivers/scsi/scsi.o
2026-05-03T01:29:48.6620592Z   AR      drivers/misc/mediatek/freqhopping/built-in.a
2026-05-03T01:29:48.6770509Z ************  drivers/trusty/mtee-kree mk ************
2026-05-03T01:29:48.7020584Z   CC      drivers/misc/mediatek/geniezone/gz-trusty/trusty.o
2026-05-03T01:29:48.8120628Z   AR      drivers/power/supply/mediatek/charger/built-in.a
2026-05-03T01:29:48.8317065Z   AR      drivers/power/supply/mediatek/built-in.a
2026-05-03T01:29:48.8480338Z   AR      drivers/power/supply/built-in.a
2026-05-03T01:29:48.8660315Z   AR      drivers/power/built-in.a
2026-05-03T01:29:48.8810581Z   CC      drivers/misc/mediatek/geniezone/gz-trusty/smcnr-table.o
2026-05-03T01:29:48.9120535Z   CC      drivers/rtc/nvmem.o
2026-05-03T01:29:49.4917224Z   CC      drivers/rtc/rtc-dev.o
2026-05-03T01:29:49.5590538Z   CC      drivers/scsi/hosts.o
2026-05-03T01:29:49.5792501Z   CC      drivers/misc/mediatek/geniezone/gz_main.o
2026-05-03T01:29:49.5871211Z   CC      drivers/misc/mediatek/geniezone/gz-trusty/trusty-irq.o
2026-05-03T01:29:49.9820124Z   CC      drivers/rtc/rtc-proc.o
2026-05-03T01:29:50.2127510Z   CC      drivers/misc/mediatek/geniezone/gz-trusty/trusty-virtio.o
2026-05-03T01:29:50.2755667Z   CC      drivers/misc/mediatek/hifi4dsp_spi/hifi4dsp_spi.o
2026-05-03T01:29:50.3930955Z   CC      drivers/rtc/rtc-sysfs.o
2026-05-03T01:29:50.5100356Z   CC      drivers/scsi/scsi_ioctl.o
2026-05-03T01:29:50.9660628Z   CC      drivers/misc/mediatek/geniezone/gz-trusty/trusty-mem.o
2026-05-03T01:29:51.0340549Z   CC      drivers/rtc/rtc-mt6358.o
2026-05-03T01:29:51.1150531Z   AR      drivers/misc/mediatek/hifi4dsp_spi/built-in.a
2026-05-03T01:29:51.1380818Z   AR      drivers/soc/amlogic/built-in.a
2026-05-03T01:29:51.1560571Z   AR      drivers/soc/bcm/built-in.a
2026-05-03T01:29:51.1731887Z   AR      drivers/soc/fsl/built-in.a
2026-05-03T01:29:51.1980412Z   CC      drivers/soc/mediatek/devapc/devapc-mtk-common.o
2026-05-03T01:29:51.4130773Z   CC      drivers/misc/mediatek/geniezone/gz-trusty/trusty-ipc.o
2026-05-03T01:29:51.4222471Z   CC      drivers/scsi/scsicam.o
2026-05-03T01:29:51.7010536Z   AR      drivers/rtc/built-in.a
2026-05-03T01:29:51.7200716Z   CC      drivers/soc/mediatek/devapc/devapc-mt6768.o
2026-05-03T01:29:52.0052104Z   CC      drivers/soc/mediatek/mtk-pm-qos.o
2026-05-03T01:29:52.2620453Z   CC      drivers/scsi/scsi_error.o
2026-05-03T01:29:52.2660219Z   AR      drivers/soc/mediatek/devapc/built-in.a
2026-05-03T01:29:52.2870587Z   CC      drivers/misc/mediatek/ice_debug/ice_debug.o
2026-05-03T01:29:52.5590544Z   CC      drivers/misc/mediatek/geniezone/gz-trusty/gz-log.o
2026-05-03T01:29:52.6640270Z   AR      drivers/misc/mediatek/ice_debug/built-in.a
2026-05-03T01:29:52.6840130Z imgsensor drv by common ../common/v1/s5kjns_sunny_mipi_raw/ ../common/v1/ov50d40_truly_mipi_raw/ ../common/v1/ov8856_sunny_mipi_raw/ ../common/v1/ov8856_ofilm_mipi_raw/ ../common/v1/imx355_sunny_mipi_raw/ ../common/v1/sc820cs_truly_mipi_raw/ ../common/v1/sc202cs_sunny_mipi_raw/ ../common/v1/ov02b10_truly_mipi_raw/
2026-05-03T01:29:52.6990553Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/imx355_sunny_mipi_raw/imx355_sunny_mipi_raw.o
2026-05-03T01:29:52.9254849Z   CC      drivers/soc/mediatek/mtk-cmdq-helper.o
2026-05-03T01:29:53.3090682Z   AR      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/imx355_sunny_mipi_raw/built-in.a
2026-05-03T01:29:53.3268461Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/ov02b10_truly_mipi_raw/ov02b10_truly_mipi_raw.o
2026-05-03T01:29:53.3670527Z   AR      drivers/misc/mediatek/geniezone/gz-trusty/built-in.a
2026-05-03T01:29:53.3850531Z   CC      drivers/misc/mediatek/geniezone/mtee_ut/gz_ut.o
2026-05-03T01:29:53.4591025Z ../drivers/soc/mediatek/mtk-cmdq-helper.c:1314:7: warning: unused variable 'inst' [-Wunused-variable]
2026-05-03T01:29:53.4620033Z         u64 *inst;
2026-05-03T01:29:53.4670322Z              ^
2026-05-03T01:29:53.4740018Z   CC      drivers/scsi/scsi_lib.o
2026-05-03T01:29:53.4790526Z ../drivers/soc/mediatek/mtk-cmdq-helper.c:2462:22: warning: variable 'client' set but not used [-Wunused-but-set-variable]
2026-05-03T01:29:53.4833100Z         struct cmdq_client *client;
2026-05-03T01:29:53.4859892Z                             ^
2026-05-03T01:29:53.7440508Z 2 warnings generated.
2026-05-03T01:29:53.8570806Z   CC      drivers/misc/mediatek/geniezone/mtee_ut/gz_chmem_ut.o
2026-05-03T01:29:54.0760893Z   AR      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/ov02b10_truly_mipi_raw/built-in.a
2026-05-03T01:29:54.0970793Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/ov50d40_truly_mipi_raw/ov50d40_truly_mipi_raw.o
2026-05-03T01:29:54.1130671Z   CC      drivers/soc/mediatek/mtk-infracfg.o
2026-05-03T01:29:54.3270567Z   CC      drivers/soc/mediatek/mtk-scpsys-ext.o
2026-05-03T01:29:54.3470565Z   CC      drivers/misc/mediatek/geniezone/mtee_ut/gz_shmem_ut.o
2026-05-03T01:29:54.6702128Z   CC      drivers/soc/mediatek/mtk-pmic-wrap_v1.o
2026-05-03T01:29:54.7099138Z   AR      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/ov50d40_truly_mipi_raw/built-in.a
2026-05-03T01:29:54.7301548Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/ov8856_ofilm_mipi_raw/ov8856ofilmmipiraw_Sensor.o
2026-05-03T01:29:54.7940535Z   CC      drivers/scsi/scsi_lib_dma.o
2026-05-03T01:29:54.8140511Z   CC      drivers/misc/mediatek/geniezone/mtee_ut/gz_vreg_ut.o
2026-05-03T01:29:55.1500727Z   CC      drivers/misc/mediatek/geniezone/mtee-kree/tz_mmap.o
2026-05-03T01:29:55.2510963Z   AR      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/ov8856_ofilm_mipi_raw/built-in.a
2026-05-03T01:29:55.2720754Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/ov8856_sunny_mipi_raw/ov8856sunnymipiraw_Sensor.o
2026-05-03T01:29:55.6227705Z   CC      drivers/scsi/scsi_scan.o
2026-05-03T01:29:55.6310722Z   CC      drivers/misc/mediatek/geniezone/mtee-kree/tz_system.o
2026-05-03T01:29:55.6320397Z   CC      drivers/soc/mediatek/mtk-scpsys.o
2026-05-03T01:29:55.7694153Z   AR      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/ov8856_sunny_mipi_raw/built-in.a
2026-05-03T01:29:55.7890623Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/s5kjns_sunny_mipi_raw/s5kjns_sunny_mipi_raw.o
2026-05-03T01:29:56.3340844Z   CC      drivers/soc/mediatek/mtk-socinfo.o
2026-05-03T01:29:56.3870761Z   AR      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/s5kjns_sunny_mipi_raw/built-in.a
2026-05-03T01:29:56.4050683Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/sc202cs_sunny_mipi_raw/sc202cs_sunny_mipi_raw.o
2026-05-03T01:29:56.5263621Z   CC      drivers/misc/mediatek/geniezone/mtee-kree/kree_mem.o
2026-05-03T01:29:56.6350493Z   AR      drivers/soc/mediatek/built-in.a
2026-05-03T01:29:56.6574259Z   AR      drivers/soc/qcom/built-in.a
2026-05-03T01:29:56.6750520Z   AR      drivers/soc/renesas/built-in.a
2026-05-03T01:29:56.6980297Z   AR      drivers/soc/xilinx/built-in.a
2026-05-03T01:29:56.7153227Z   AR      drivers/soc/built-in.a
2026-05-03T01:29:56.7210723Z   CC      drivers/scsi/scsi_sysfs.o
2026-05-03T01:29:56.7390386Z   CC      drivers/misc/mediatek/irtx/mtk_irtx_pwm.o
2026-05-03T01:29:56.9448383Z   AR      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/sc202cs_sunny_mipi_raw/built-in.a
2026-05-03T01:29:56.9660787Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/sc820cs_truly_mipi_raw/sc820cs_truly_mipi_raw.o
2026-05-03T01:29:57.3670433Z   AR      drivers/misc/mediatek/geniezone/built-in.a
2026-05-03T01:29:57.3790487Z   CC      drivers/scsi/scsi_devinfo.o
2026-05-03T01:29:57.3850459Z   AR      drivers/misc/mediatek/irtx/built-in.a
2026-05-03T01:29:57.4050461Z   CC      drivers/misc/mediatek/jpeg/v2/jpeg_drv_enc.o
2026-05-03T01:29:57.5551024Z   AR      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/sc820cs_truly_mipi_raw/built-in.a
2026-05-03T01:29:57.5806470Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/camera_hw/gpio/gpio.o
2026-05-03T01:29:57.8090561Z   CC      drivers/spi/spi.o
2026-05-03T01:29:57.9620768Z   CC      drivers/misc/mediatek/jpeg/v2/jpeg_drv_dec.o
2026-05-03T01:29:58.1510088Z   AR      drivers/misc/mediatek/imgsensor/src/mt6768/camera_hw/gpio/built-in.a
2026-05-03T01:29:58.1710588Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/camera_hw/mclk/mclk.o
2026-05-03T01:29:58.2490572Z   CC      drivers/scsi/scsi_sysctl.o
2026-05-03T01:29:58.4280744Z drivers/misc/mediatek/jpeg/v2/.tmp_jpeg_drv_dec.o: no symbols
2026-05-03T01:29:58.4340365Z   CC      drivers/misc/mediatek/jpeg/v2/jpeg_drv.o
2026-05-03T01:29:58.7460785Z   AR      drivers/misc/mediatek/imgsensor/src/mt6768/camera_hw/mclk/built-in.a
2026-05-03T01:29:58.7670633Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/camera_hw/regulator/regulator.o
2026-05-03T01:29:58.7782934Z   CC      drivers/scsi/scsi_proc.o
2026-05-03T01:29:59.2790630Z   CC      drivers/misc/mediatek/jpeg/v2/jpeg_ion.o
2026-05-03T01:29:59.3340792Z   CC      drivers/scsi/scsi_trace.o
2026-05-03T01:29:59.3804383Z   AR      drivers/misc/mediatek/imgsensor/src/mt6768/camera_hw/regulator/built-in.a
2026-05-03T01:29:59.3860431Z   CC      drivers/spi/spi-mt65xx.o
2026-05-03T01:29:59.3920308Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/camera_hw/imgsensor_cfg_table.o
2026-05-03T01:29:59.6847187Z   AR      drivers/misc/mediatek/jpeg/v2/built-in.a
2026-05-03T01:29:59.6990256Z   AR      drivers/misc/mediatek/jpeg/built-in.a
2026-05-03T01:29:59.7150176Z ION:enable mtk ion
2026-05-03T01:29:59.7410247Z   CC      drivers/staging/android/mtk_ion/mtk/ion_drv.o
2026-05-03T01:29:59.9521772Z   CC      drivers/scsi/scsi_logging.o
2026-05-03T01:29:59.9530701Z   AR      drivers/misc/mediatek/imgsensor/src/mt6768/camera_hw/built-in.a
2026-05-03T01:29:59.9634209Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/imgsensor.o
2026-05-03T01:30:00.0740525Z   CC      drivers/spi/spi-mt65xx-dev.o
2026-05-03T01:30:00.2461327Z ../drivers/staging/android/mtk_ion/mtk/ion_drv.c:570:24: warning: cast to smaller integer type 'unsigned int' from 'void *' [-Wvoid-pointer-to-int-cast]
2026-05-03T01:30:00.2490270Z                 m4u_mva_unmap_kernel((unsigned int)param->va,
2026-05-03T01:30:00.2519991Z                                      ^~~~~~~~~~~~~~~~~~~~~~~
2026-05-03T01:30:00.4050339Z 1 warning generated.
2026-05-03T01:30:00.5340634Z ../drivers/spi/spi-mt65xx-dev.c:76:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:00.5369812Z         int ret;
2026-05-03T01:30:00.5400320Z             ^
2026-05-03T01:30:00.6060555Z 1 warning generated.
2026-05-03T01:30:00.6790480Z   CC      drivers/staging/android/mtk_ion/mtk/ion_mm_heap.o
2026-05-03T01:30:00.8220470Z   CC      drivers/scsi/scsi_pm.o
2026-05-03T01:30:00.8607087Z   AR      drivers/spi/built-in.a
2026-05-03T01:30:00.8917502Z   CC      drivers/misc/mediatek/lcm/dsi_panel_m19a_36_02_0a_dsc_vdo/dsi_panel_m19a_36_02_0a_dsc_vdo.o
2026-05-03T01:30:01.1760945Z ../drivers/staging/android/mtk_ion/mtk/ion_mm_heap.c:1208:29: warning: variable 'bug_info' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:01.1790196Z         struct ion_mm_buffer_info *bug_info;
2026-05-03T01:30:01.1819901Z                                    ^
2026-05-03T01:30:01.1970495Z ../drivers/staging/android/mtk_ion/mtk/ion_mm_heap.c:2197:8: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:01.1999981Z                         int ret;
2026-05-03T01:30:01.2029942Z                             ^
2026-05-03T01:30:01.2060455Z ../drivers/staging/android/mtk_ion/mtk/ion_mm_heap.c:1934:15: warning: variable 'buffer_sec' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:01.2061445Z         unsigned int buffer_sec = 0;
2026-05-03T01:30:01.2089936Z                      ^
2026-05-03T01:30:01.2120432Z ../drivers/staging/android/mtk_ion/mtk/ion_mm_heap.c:2395:28: warning: variable 'end' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:01.2149908Z         unsigned long long start, end;
2026-05-03T01:30:01.2179886Z                                   ^
2026-05-03T01:30:01.3728840Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/imgsensor_hw.o
2026-05-03T01:30:01.3927884Z   AR      drivers/misc/mediatek/lcm/dsi_panel_m19a_36_02_0a_dsc_vdo/built-in.a
2026-05-03T01:30:01.4103490Z   CC      drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0b_dsc_vdo/dsi_panel_m19a_42_03_0b_dsc_vdo.o
2026-05-03T01:30:01.4570399Z 4 warnings generated.
2026-05-03T01:30:01.6390487Z   CC      drivers/scsi/scsi_common.o
2026-05-03T01:30:01.7531226Z   CC      drivers/staging/android/mtk_ion/mtk/ion_fb_heap.o
2026-05-03T01:30:01.7911096Z ../drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0b_dsc_vdo/dsi_panel_m19a_42_03_0b_dsc_vdo.c:482:8: warning: type specifier missing, defaults to 'int' [-Wimplicit-int]
2026-05-03T01:30:01.7919973Z extern fts_fwresume_work(void);
2026-05-03T01:30:01.7920375Z ~~~~~~ ^
2026-05-03T01:30:01.7920675Z int
2026-05-03T01:30:01.8280339Z 1 warning generated.
2026-05-03T01:30:01.8603614Z   AR      drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0b_dsc_vdo/built-in.a
2026-05-03T01:30:01.8630017Z   CC      drivers/scsi/sd.o
2026-05-03T01:30:01.8780653Z   CC      drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0c_dsc_vdo/dsi_panel_m19a_42_03_0c_dsc_vdo.o
2026-05-03T01:30:01.8800280Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/imgsensor_i2c.o
2026-05-03T01:30:02.2772558Z   CC      drivers/staging/android/mtk_ion/mtk/ion_sec_heap.o
2026-05-03T01:30:02.3845538Z   AR      drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0c_dsc_vdo/built-in.a
2026-05-03T01:30:02.4020729Z   CC      drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0d_dsc_vdo/dsi_panel_m19a_42_03_0d_dsc_vdo.o
2026-05-03T01:30:02.4320609Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/imgsensor_legacy.o
2026-05-03T01:30:02.8750687Z   CC      drivers/staging/android/mtk_ion/mtk/ion_profile.o
2026-05-03T01:30:02.8980794Z   AR      drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0d_dsc_vdo/built-in.a
2026-05-03T01:30:02.9177787Z   CC      drivers/misc/mediatek/lcm/virtual_dsi_vdo_default/virtual_dsi_vdo_default.o
2026-05-03T01:30:02.9203839Z   CC      drivers/staging/android/mtk_ion/mtk/ion_history.o
2026-05-03T01:30:02.9710785Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/imgsensor_proc.o
2026-05-03T01:30:03.0660612Z   AR      drivers/scsi/built-in.a
2026-05-03T01:30:03.1092655Z   CC      drivers/misc/mediatek/leds/mt6768/mtk_leds.o
2026-05-03T01:30:03.2300183Z   AR      drivers/misc/mediatek/lcm/virtual_dsi_vdo_default/built-in.a
2026-05-03T01:30:03.2413689Z   CC      drivers/misc/mediatek/lcm/mt65xx_lcm_list.o
2026-05-03T01:30:03.3901347Z ../drivers/staging/android/mtk_ion/mtk/ion_history.c:684:6: warning: variable 'heap_id' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:03.3929900Z         int heap_id = 0;
2026-05-03T01:30:03.3959922Z             ^
2026-05-03T01:30:03.5120152Z 1 warning generated.
2026-05-03T01:30:03.5401103Z   CC      drivers/staging/android/mtk_ion/mtk/ion_comm.o
2026-05-03T01:30:03.5461851Z   CC      drivers/misc/mediatek/lcm/lcm_common.o
2026-05-03T01:30:03.5660867Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/../common/v1/imgsensor_sensor_list.o
2026-05-03T01:30:03.5780596Z drivers/misc/mediatek/lcm/.tmp_lcm_common.o: no symbols
2026-05-03T01:30:03.5840436Z   CC      drivers/misc/mediatek/lcm/lcm_gpio.o
2026-05-03T01:30:03.6190381Z drivers/misc/mediatek/lcm/.tmp_lcm_gpio.o: no symbols
2026-05-03T01:30:03.6219929Z   CC      drivers/misc/mediatek/lcm/lcm_i2c.o
2026-05-03T01:30:03.6630437Z   CC      drivers/misc/mediatek/lcm/lcm_pmic.o
2026-05-03T01:30:03.8570435Z   CC      drivers/misc/mediatek/lcm/lcm_util.o
2026-05-03T01:30:03.8870483Z drivers/misc/mediatek/lcm/.tmp_lcm_util.o: no symbols
2026-05-03T01:30:03.8900169Z   CC      drivers/misc/mediatek/lcm/ocp2131_bias.o
2026-05-03T01:30:04.0420635Z   CC      drivers/misc/mediatek/leds/mt6768/ktd3136_bl.o
2026-05-03T01:30:04.0640475Z   AR      drivers/staging/android/mtk_ion/mtk/built-in.a
2026-05-03T01:30:04.0760447Z   CC      drivers/staging/android/mtk_ion/ion.o
2026-05-03T01:30:04.0860749Z   CC      drivers/misc/mediatek/imgsensor/src/mt6768/imgsensor_clk.o
2026-05-03T01:30:04.3398309Z   AR      drivers/misc/mediatek/lcm/built-in.a
2026-05-03T01:30:04.3630315Z   CC      drivers/staging/erofs/super.o
2026-05-03T01:30:04.5330322Z   AR      drivers/misc/mediatek/imgsensor/src/mt6768/built-in.a
2026-05-03T01:30:04.5480230Z   AR      drivers/misc/mediatek/imgsensor/src/built-in.a
2026-05-03T01:30:04.5590140Z   CC      drivers/misc/mediatek/leds/mtk_leds_drv.o
2026-05-03T01:30:04.7080820Z   CC      drivers/misc/mediatek/leds/mt6768/ti-lmu-backlight-core.o
2026-05-03T01:30:05.1491169Z   CC      drivers/staging/android/mtk_ion/ion-ioctl.o
2026-05-03T01:30:05.1948168Z   CC      drivers/staging/erofs/inode.o
2026-05-03T01:30:05.2914360Z   CC      drivers/misc/mediatek/leds/mt6768/ti-lmu-backlight-data.o
2026-05-03T01:30:05.3304535Z   CC      drivers/staging/android/ashmem.o
2026-05-03T01:30:05.5011430Z ../drivers/staging/android/mtk_ion/ion-ioctl.c:96:7: warning: variable 'heap_mask' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:05.5039944Z                 int heap_mask;
2026-05-03T01:30:05.5040313Z                     ^
2026-05-03T01:30:05.5490231Z 1 warning generated.
2026-05-03T01:30:05.5790422Z   CC      drivers/staging/android/mtk_ion/ion_heap.o
2026-05-03T01:30:05.8166463Z   CC      drivers/staging/erofs/data.o
2026-05-03T01:30:05.8420859Z ../drivers/staging/android/ashmem.c:407:17: warning: variable 'inode' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:05.8449913Z                 struct inode *inode;
2026-05-03T01:30:05.8520148Z                               ^
2026-05-03T01:30:05.9750549Z 1 warning generated.
2026-05-03T01:30:06.0050620Z   CC      drivers/staging/android/alarm-dev.o
2026-05-03T01:30:06.0767804Z   AR      drivers/misc/mediatek/leds/mt6768/built-in.a
2026-05-03T01:30:06.0920155Z   AR      drivers/misc/mediatek/leds/built-in.a
2026-05-03T01:30:06.1300569Z   CC      drivers/misc/mediatek/lens/mtk/main/main_lens.o
2026-05-03T01:30:06.3367578Z   CC      drivers/staging/android/mtk_ion/ion_page_pool.o
2026-05-03T01:30:06.4320537Z   CC      drivers/staging/erofs/namei.o
2026-05-03T01:30:06.4680741Z   CC      drivers/misc/mediatek/lens/mtk/main2/main2_lens.o
2026-05-03T01:30:06.8559567Z   CC      drivers/misc/mediatek/lens/mtk/main/common/fp5510e2af/FP5510E2AF.o
2026-05-03T01:30:06.9240709Z   CC      drivers/staging/android/mtk_ion/ion_system_heap.o
2026-05-03T01:30:06.9759042Z   CC      drivers/staging/erofs/dir.o
2026-05-03T01:30:07.1850552Z   CC      drivers/misc/mediatek/lens/mtk/main2/common/ak7371af/AK7371AF.o
2026-05-03T01:30:07.2900740Z   CC      drivers/misc/mediatek/lens/mtk/main/common/bu6424af/BU6424AF.o
2026-05-03T01:30:07.4640984Z   CC      drivers/staging/android/mtk_ion/ion_carveout_heap.o
2026-05-03T01:30:07.5060316Z   CC      drivers/staging/erofs/utils.o
2026-05-03T01:30:07.6236827Z   CC      drivers/misc/mediatek/lens/mtk/main2/common/ak7374af/AK7374AF.o
2026-05-03T01:30:07.7159910Z   CC      drivers/misc/mediatek/lens/mtk/main/common/bu6429af/BU6429AF.o
2026-05-03T01:30:07.9771753Z   CC      drivers/staging/android/mtk_ion/ion_chunk_heap.o
2026-05-03T01:30:08.0630672Z   CC      drivers/staging/erofs/pcpubuf.o
2026-05-03T01:30:08.0670319Z   CC      drivers/misc/mediatek/lens/mtk/main2/common/bu64748af/bu64748_function.o
2026-05-03T01:30:08.1540564Z   CC      drivers/misc/mediatek/lens/mtk/main/common/bu64748af/bu64748_function.o
2026-05-03T01:30:08.4550541Z   CC      drivers/misc/mediatek/lens/mtk/main2/common/bu64748af/bu64748af.o
2026-05-03T01:30:08.4910660Z   CC      drivers/staging/android/mtk_ion/ion_cma_heap.o
2026-05-03T01:30:08.5400416Z   CC      drivers/misc/mediatek/lens/mtk/main/common/bu64748af/bu64748af.o
2026-05-03T01:30:08.6290597Z   CC      drivers/staging/erofs/xattr.o
2026-05-03T01:30:08.8822593Z   CC      drivers/misc/mediatek/lens/mtk/main2/common/lc898212xdaf_f/LC89821x_STMV.o
2026-05-03T01:30:08.9650832Z   CC      drivers/misc/mediatek/lens/mtk/main/common/dw9714af/DW9714AF.o
2026-05-03T01:30:09.0160654Z   CC      drivers/staging/android/mtk_ion/compat_ion.o
2026-05-03T01:30:09.0181066Z   CC      drivers/misc/mediatek/lens/mtk/main2/common/lc898212xdaf_f/LC898212XDAF_F.o
2026-05-03T01:30:09.3030604Z   CC      drivers/staging/erofs/decompressor.o
2026-05-03T01:30:09.3880775Z   CC      drivers/misc/mediatek/lens/mtk/main/common/dw9800waf/DW9800WAF.o
2026-05-03T01:30:09.4750771Z   CC      drivers/misc/mediatek/lens/mtk/main2/common/lc898217af/LC898217AF.o
2026-05-03T01:30:09.8440917Z   CC      drivers/misc/mediatek/lens/mtk/main/common/dw9814af/DW9814AF.o
2026-05-03T01:30:09.8900778Z   CC      drivers/misc/mediatek/lens/mtk/main2/common/lc898217afa/LC898217AFA.o
2026-05-03T01:30:09.9066571Z   CC      drivers/staging/erofs/zmap.o
2026-05-03T01:30:10.2716384Z   CC      drivers/misc/mediatek/lens/mtk/main/common/dw9718af/DW9718AF.o
2026-05-03T01:30:10.2885412Z   CC      drivers/misc/mediatek/lens/mtk/main2/common/lc898217afb/LC898217AFB.o
2026-05-03T01:30:10.3967078Z   AR      drivers/staging/android/mtk_ion/built-in.a
2026-05-03T01:30:10.4110630Z   CC      drivers/staging/android/debug_kinfo.o
2026-05-03T01:30:10.5840571Z   CC      drivers/staging/erofs/zdata.o
2026-05-03T01:30:10.7060718Z   CC      drivers/misc/mediatek/lens/mtk/main/common/dw9718saf/DW9718SAF.o
2026-05-03T01:30:10.7140615Z   CC      drivers/misc/mediatek/lens/mtk/main2/common/lc898217afc/LC898217AFC.o
2026-05-03T01:30:10.9000621Z   AR      drivers/staging/android/built-in.a
2026-05-03T01:30:10.9192081Z "CONFIG_MICROTRUST_TEE_VERSION="400""
2026-05-03T01:30:10.9259270Z "CONFIG_MICROTRUST_TEE_SUPPORT=y"
2026-05-03T01:30:10.9260446Z "CONFIG_MICROTRUST_TZ_DRIVER=y"
2026-05-03T01:30:10.9261023Z "CONFIG_MICROTRUST_VFS_DRIVER=y"
2026-05-03T01:30:10.9261881Z "CONFIG_MICROTRUST_FP_DRIVER=y"
2026-05-03T01:30:10.9262421Z "CONFIG_MICROTRUST_DEBUG="
2026-05-03T01:30:10.9262984Z "CONFIG_MICROTRUST_TEST_DRIVERS="
2026-05-03T01:30:10.9500212Z   CC      drivers/tee/teei/400/tee/soter/core.o
2026-05-03T01:30:11.1449763Z   CC      drivers/misc/mediatek/lens/mtk/main2/common/dw9718taf/DW9718TAF.o
2026-05-03T01:30:11.1520628Z   CC      drivers/misc/mediatek/lens/mtk/main/common/dw9718taf/DW9718TAF.o
2026-05-03T01:30:11.3661009Z   CC      drivers/tee/teei/400/tee/soter/call.o
2026-05-03T01:30:11.4700564Z   AR      drivers/staging/erofs/built-in.a
2026-05-03T01:30:11.4929134Z   AR      drivers/staging/iio/accel/built-in.a
2026-05-03T01:30:11.5110447Z   AR      drivers/staging/iio/adc/built-in.a
2026-05-03T01:30:11.5290409Z   AR      drivers/staging/iio/addac/built-in.a
2026-05-03T01:30:11.5470274Z   AR      drivers/staging/iio/cdc/built-in.a
2026-05-03T01:30:11.5607238Z   AR      drivers/staging/iio/frequency/built-in.a
2026-05-03T01:30:11.5761092Z   CC      drivers/misc/mediatek/lens/mtk/main2/common/gt9772af/GT9772AF.o
2026-05-03T01:30:11.5770291Z   CC      drivers/misc/mediatek/lens/mtk/main/common/dw9719taf/DW9719TAF.o
2026-05-03T01:30:11.5790704Z   AR      drivers/staging/iio/impedance-analyzer/built-in.a
2026-05-03T01:30:11.5920376Z   AR      drivers/staging/iio/meter/built-in.a
2026-05-03T01:30:11.6089153Z   AR      drivers/staging/iio/resolver/built-in.a
2026-05-03T01:30:11.6300487Z   AR      drivers/staging/iio/built-in.a
2026-05-03T01:30:11.6480347Z   AR      drivers/staging/media/built-in.a
2026-05-03T01:30:11.6680390Z   CC      drivers/staging/rtmm/rtmm_main.o
2026-05-03T01:30:11.7180462Z   AR      drivers/tee/teei/400/tee/soter/built-in.a
2026-05-03T01:30:11.7300445Z   CC      drivers/tee/teei/400/tee/tee_core.o
2026-05-03T01:30:11.9711875Z   CC      drivers/staging/rtmm/rtmm_reclaim.o
2026-05-03T01:30:12.0117808Z   AR      drivers/misc/mediatek/lens/mtk/main2/built-in.a
2026-05-03T01:30:12.0150601Z   CC      drivers/misc/mediatek/lens/mtk/main/common/dw9763af/DW9763AF.o
2026-05-03T01:30:12.0339788Z   CC      drivers/tee/teei/400/teei_fp/fp_func.o
2026-05-03T01:30:12.4690765Z   CC      drivers/misc/mediatek/lens/mtk/main/common/dw9839af/DW9839AF.o
2026-05-03T01:30:12.6145650Z   AR      drivers/staging/rtmm/built-in.a
2026-05-03T01:30:12.6322499Z   AR      drivers/staging/built-in.a
2026-05-03T01:30:12.6555495Z   CC      drivers/misc/mediatek/log_store/log_store.o
2026-05-03T01:30:12.8030606Z   CC      drivers/tee/teei/400/tee/tee_shm.o
2026-05-03T01:30:12.8861115Z   AR      drivers/tee/teei/400/teei_fp/built-in.a
2026-05-03T01:30:12.8991046Z M4U platform folder:"mt6768"
2026-05-03T01:30:12.9029908Z M4U version:2.0
2026-05-03T01:30:12.9118694Z   CC      drivers/misc/mediatek/lens/mtk/main/common/gt9764af/GT9764AF.o
2026-05-03T01:30:12.9160065Z   CC      drivers/misc/mediatek/m4u/2.0/m4u.o
2026-05-03T01:30:13.3367066Z   CC      drivers/misc/mediatek/lens/mtk/main/common/lc898212af/LC898212AF.o
2026-05-03T01:30:13.3597290Z   AR      drivers/misc/mediatek/log_store/built-in.a
2026-05-03T01:30:13.3813478Z   CC      drivers/misc/mediatek/m4u/mt6768/m4u_hw.o
2026-05-03T01:30:13.5426159Z   CC      drivers/tee/teei/400/tee/tee_shm_pool.o
2026-05-03T01:30:13.8021226Z   CC      drivers/misc/mediatek/lens/mtk/main/common/lc898212xdaf/LC898212XDAF.o
2026-05-03T01:30:14.1895519Z   CC      drivers/misc/mediatek/m4u/2.0/m4u_mva.o
2026-05-03T01:30:14.2055192Z   CC      drivers/tee/teei/400/tee/tee_client_api.o
2026-05-03T01:30:14.2590659Z   CC      drivers/misc/mediatek/lens/mtk/main/common/lc898212xdaf/AfInter.o
2026-05-03T01:30:14.2865420Z   AR      drivers/misc/mediatek/m4u/mt6768/built-in.a
2026-05-03T01:30:14.3071213Z   CC      drivers/misc/mediatek/lens/mtk/main3/main3_lens.o
2026-05-03T01:30:14.5820792Z   CC      drivers/misc/mediatek/lens/mtk/main/common/lc898212xdaf/AfInit.o
2026-05-03T01:30:14.6340689Z   CC      drivers/misc/mediatek/lens/mtk/main/common/lc898212xdaf/AfSTMV.o
2026-05-03T01:30:14.6830982Z   CC      drivers/misc/mediatek/lens/mtk/main/common/lc898214af/LC898214AF.o
2026-05-03T01:30:14.7120395Z   CC      drivers/misc/mediatek/m4u/2.0/m4u_pgtable.o
2026-05-03T01:30:14.8270785Z   CC      drivers/misc/mediatek/lens/mtk/main3/common/bu24253af/BU24253AF.o
2026-05-03T01:30:15.0125522Z   AR      drivers/tee/teei/400/tee/built-in.a
2026-05-03T01:30:15.0410486Z   CC      drivers/tee/teei/400/tz_dcih/tz_dcih.o
2026-05-03T01:30:15.1445137Z   CC      drivers/misc/mediatek/lens/mtk/main/common/lc898217af/LC898217AF.o
2026-05-03T01:30:15.2150750Z   CC      drivers/misc/mediatek/lens/mtk/main3/common/gt9772af/GT9772AF.o
2026-05-03T01:30:15.3711585Z   CC      drivers/misc/mediatek/m4u/2.0/m4u_debug.o
2026-05-03T01:30:15.5550320Z   CC      drivers/tee/teei/400/tz_dcih/tz_dcih_test.o
2026-05-03T01:30:15.5820761Z   CC      drivers/misc/mediatek/lens/mtk/main/common/lc898217afa/LC898217AFA.o
2026-05-03T01:30:15.6410164Z   AR      drivers/misc/mediatek/lens/mtk/main3/built-in.a
2026-05-03T01:30:15.6643977Z   AR      drivers/thermal/broadcom/built-in.a
2026-05-03T01:30:15.6810608Z   AR      drivers/thermal/samsung/built-in.a
2026-05-03T01:30:15.7000232Z   AR      drivers/thermal/tegra/built-in.a
2026-05-03T01:30:15.7090213Z   CC      drivers/thermal/thermal_core.o
2026-05-03T01:30:15.9585303Z   AR      drivers/tee/teei/400/tz_dcih/built-in.a
2026-05-03T01:30:15.9599161Z   CC      drivers/misc/mediatek/m4u/2.0/m4u_sec_gp.o
2026-05-03T01:30:15.9820964Z   CC      drivers/tee/teei/400/tz_driver/teei_client_main.o
2026-05-03T01:30:16.0190567Z   CC      drivers/misc/mediatek/lens/mtk/main/common/lc898217afb/LC898217AFB.o
2026-05-03T01:30:16.4625931Z ../drivers/thermal/thermal_core.c:1246:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:16.4645707Z         int ret;
2026-05-03T01:30:16.4675756Z             ^
2026-05-03T01:30:16.4677088Z ../drivers/thermal/thermal_core.c:1247:8: warning: 'snprintf' size argument is too large; destination buffer has size 128, but size argument is 4096 [-Wfortify-source]
2026-05-03T01:30:16.4678362Z         ret = snprintf(boost_buf, PAGE_SIZE, buf);
2026-05-03T01:30:16.4678935Z               ^
2026-05-03T01:30:16.4679654Z   AR      drivers/misc/mediatek/m4u/2.0/built-in.a
2026-05-03T01:30:16.4680899Z ../drivers/thermal/thermal_core.c:1341:2: warning: 'snprintf' size argument is too large; destination buffer has size 128, but size argument is 4096 [-Wfortify-source]
2026-05-03T01:30:16.4682203Z         snprintf(board_sensor_temp, PAGE_SIZE, buf);
2026-05-03T01:30:16.4682790Z         ^
2026-05-03T01:30:16.4683379Z   CC      drivers/misc/mediatek/lens/mtk/main/common/lc898217afc/LC898217AFC.o
2026-05-03T01:30:16.4834544Z   AR      drivers/misc/mediatek/m4u/built-in.a
2026-05-03T01:30:16.5096559Z   AR      drivers/tty/ipwireless/built-in.a
2026-05-03T01:30:16.5390574Z   CC      drivers/tty/serial/8250/8250_core.o
2026-05-03T01:30:16.7270394Z 3 warnings generated.
2026-05-03T01:30:16.9071497Z   CC      drivers/misc/mediatek/lens/mtk/main/common/lc898229af/LC898229AF.o
2026-05-03T01:30:16.9561001Z   CC      drivers/tee/teei/400/tz_driver/fdrv.o
2026-05-03T01:30:17.1535180Z   CC      drivers/thermal/thermal_sysfs.o
2026-05-03T01:30:17.3229143Z   CC      drivers/misc/mediatek/lens/mtk/main/common/lc898122af/LC898122AF.o
2026-05-03T01:30:17.4370592Z   CC      drivers/tty/serial/8250/8250_port.o
2026-05-03T01:30:17.6301367Z   CC      drivers/thermal/thermal_helpers.o
2026-05-03T01:30:17.7140733Z   CC      drivers/tee/teei/400/tz_driver/backward_driver.o
2026-05-03T01:30:17.7570733Z   CC      drivers/misc/mediatek/lens/mtk/main/common/lc898122af/OisCmd.o
2026-05-03T01:30:17.8730644Z   CC      drivers/misc/mediatek/lens/mtk/main/common/lc898122af/OisIni.o
2026-05-03T01:30:17.9520650Z   CC      drivers/misc/mediatek/lens/mtk/main/common/wv511aaf/WV511AAF.o
2026-05-03T01:30:18.1511006Z   CC      drivers/thermal/of-thermal.o
2026-05-03T01:30:18.2473469Z   CC      drivers/tee/teei/400/tz_driver/irq_register.o
2026-05-03T01:30:18.3882384Z   CC      drivers/misc/mediatek/lens/mtk/main/common/ak7371af/AK7371AF.o
2026-05-03T01:30:18.5250406Z   CC      drivers/tty/serial/8250/8250_dma.o
2026-05-03T01:30:18.8384401Z   CC      drivers/tee/teei/400/tz_driver/notify_queue.o
2026-05-03T01:30:18.8462806Z   CC      drivers/misc/mediatek/lens/mtk/main/common/bu63169af/BU63169AF.o
2026-05-03T01:30:19.1610621Z   CC      drivers/thermal/backward_compatible.o
2026-05-03T01:30:19.2460825Z   CC      drivers/misc/mediatek/lens/mtk/main/common/bu63169af/OIS_func.o
2026-05-03T01:30:19.3520582Z   CC      drivers/tee/teei/400/tz_driver/teei_fp.o
2026-05-03T01:30:19.3540986Z   CC      drivers/misc/mediatek/lens/mtk/main/common/bu63169af/OIS_main.o
2026-05-03T01:30:19.3650642Z   CC      drivers/tty/serial/8250/8250_early.o
2026-05-03T01:30:19.3950508Z   CC      drivers/misc/mediatek/lens/mtk/main/common/bu63169af/OIS_user.o
2026-05-03T01:30:19.4430579Z   CC      drivers/misc/mediatek/lens/mtk/main/common/bu64253gwzaf/BU64253GWZAF.o
2026-05-03T01:30:19.4701026Z   CC      drivers/thermal/cpu_cooling.o
2026-05-03T01:30:19.5750352Z   CC      drivers/tee/teei/400/tz_driver/teei_smc_call.o
2026-05-03T01:30:19.8030894Z ../drivers/thermal/cpu_cooling.c:490:15: warning: variable 'cur_freq' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:19.8059999Z         unsigned int cur_freq, target_freq;
2026-05-03T01:30:19.8089943Z                      ^
2026-05-03T01:30:19.8240044Z   CC      drivers/tty/serial/8250/8250_fsl.o
2026-05-03T01:30:19.8800818Z   CC      drivers/misc/mediatek/lens/mtk/main/common/gt9768af/GT9768AF.o
2026-05-03T01:30:19.9390338Z 1 warning generated.
2026-05-03T01:30:20.0590838Z ../drivers/tee/teei/400/tz_driver/teei_smc_call.c:22:9: warning: 'IMSG_TAG' macro redefined [-Wmacro-redefined]
2026-05-03T01:30:20.0591608Z #define IMSG_TAG "[tz_driver]"
2026-05-03T01:30:20.0591979Z         ^
2026-05-03T01:30:20.0592511Z ../drivers/tee/teei/400/common/include/imsg_log.h:12:9: note: previous definition is here
2026-05-03T01:30:20.0593133Z #define IMSG_TAG "[ISEE DRV]"
2026-05-03T01:30:20.0593464Z         ^
2026-05-03T01:30:20.0709985Z 1 warning generated.
2026-05-03T01:30:20.1620614Z   CC      drivers/thermal/mtk_thermal.o
2026-05-03T01:30:20.3025492Z   CC      drivers/misc/mediatek/lens/mtk/main/common/gt9772af/GT9772AF.o
2026-05-03T01:30:20.3340965Z ../drivers/tee/teei/400/tz_driver/teei_smc_call.c:22:9: warning: 'IMSG_TAG' macro redefined [-Wmacro-redefined]
2026-05-03T01:30:20.3370007Z #define IMSG_TAG "[tz_driver]"
2026-05-03T01:30:20.3370533Z         ^
2026-05-03T01:30:20.3400204Z ../drivers/tee/teei/400/common/include/imsg_log.h:12:9: note: previous definition is here
2026-05-03T01:30:20.3429950Z #define IMSG_TAG "[ISEE DRV]"
2026-05-03T01:30:20.3459935Z         ^
2026-05-03T01:30:20.3460376Z 1 warning generated.
2026-05-03T01:30:20.3490153Z   CC      drivers/tee/teei/400/tz_driver/tz_log.o
2026-05-03T01:30:20.5440582Z   CC      drivers/tty/serial/8250/8250_mtk.o
2026-05-03T01:30:20.5590533Z   AR      drivers/thermal/built-in.a
2026-05-03T01:30:20.5890260Z   CC      drivers/usb/common/common.o
2026-05-03T01:30:20.7290675Z   CC      drivers/misc/mediatek/lens/mtk/main/common/gt9764baf/GT9764BAF.o
2026-05-03T01:30:20.8400933Z ../drivers/tee/teei/400/tz_driver/tz_log.c:209:16: warning: unused variable 'flags' [-Wunused-variable]
2026-05-03T01:30:20.8430083Z         unsigned long flags;
2026-05-03T01:30:20.8459868Z                       ^
2026-05-03T01:30:20.8880711Z 1 warning generated.
2026-05-03T01:30:20.9191047Z   CC      drivers/tee/teei/400/tz_driver/switch_queue.o
2026-05-03T01:30:21.1533738Z   CC      drivers/misc/mediatek/lens/mtk/main/common/dw9800af/DW9800AF.o
2026-05-03T01:30:21.1920802Z   AR      drivers/tty/serial/8250/built-in.a
2026-05-03T01:30:21.2070291Z   CC      drivers/tty/serial/serial_core.o
2026-05-03T01:30:21.2420480Z   AR      drivers/usb/common/built-in.a
2026-05-03T01:30:21.2660457Z   CC      drivers/usb/core/usb.o
2026-05-03T01:30:21.3959683Z ../drivers/tee/teei/400/tz_driver/switch_queue.c:39:9: warning: 'IMSG_TAG' macro redefined [-Wmacro-redefined]
2026-05-03T01:30:21.3989960Z #define IMSG_TAG "[tz_driver]"
2026-05-03T01:30:21.4020094Z         ^
2026-05-03T01:30:21.4047876Z ../drivers/tee/teei/400/common/include/imsg_log.h:12:9: note: previous definition is here
2026-05-03T01:30:21.4079917Z #define IMSG_TAG "[ISEE DRV]"
2026-05-03T01:30:21.4109899Z         ^
2026-05-03T01:30:21.4140422Z ../drivers/tee/teei/400/tz_driver/switch_queue.c:154:26: warning: unused variable 's' [-Wunused-variable]
2026-05-03T01:30:21.4169996Z         struct tz_driver_state *s = get_tz_drv_state();
2026-05-03T01:30:21.4199916Z                                 ^
2026-05-03T01:30:21.4229933Z 2 warnings generated.
2026-05-03T01:30:21.4420335Z   CC      drivers/tee/teei/400/tz_driver/teei_keymaster.o
2026-05-03T01:30:21.6102431Z   AR      drivers/misc/mediatek/lens/mtk/main/built-in.a
2026-05-03T01:30:21.6360469Z   CC      drivers/misc/mediatek/lens/mtk/sub/sub_lens.o
2026-05-03T01:30:21.6840620Z   CC      drivers/tee/teei/400/tz_driver/teei_cancel_cmd.o
2026-05-03T01:30:22.1495263Z   CC      drivers/usb/core/hub.o
2026-05-03T01:30:22.1643295Z   CC      drivers/misc/mediatek/lens/mtk/sub/common/bu6424af/BU6424AF.o
2026-05-03T01:30:22.2291187Z   CC      drivers/tee/teei/400/tz_driver/teei_client_transfer_data.o
2026-05-03T01:30:22.3494879Z   CC      drivers/tty/serial/earlycon.o
2026-05-03T01:30:22.5470715Z   CC      drivers/tee/teei/400/tz_driver/sysfs.o
2026-05-03T01:30:22.5917721Z   CC      drivers/misc/mediatek/lens/mtk/sub/common/bu6429af/BU6429AF.o
2026-05-03T01:30:22.6150743Z ../drivers/usb/core/hub.c:3667:8: warning: variable 'status' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:22.6179945Z         int                     status;
2026-05-03T01:30:22.6199897Z                                 ^
2026-05-03T01:30:22.8586839Z   AR      drivers/tty/serial/built-in.a
2026-05-03T01:30:22.8803584Z   AR      drivers/tty/vt/built-in.a
2026-05-03T01:30:22.8910372Z   CC      drivers/tty/tty_io.o
2026-05-03T01:30:23.0360788Z   CC      drivers/misc/mediatek/lens/mtk/sub/common/dw9714af/DW9714AF.o
2026-05-03T01:30:23.1370495Z   CC      drivers/tee/teei/400/tz_driver/teei_task_link.o
2026-05-03T01:30:23.3480346Z 1 warning generated.
2026-05-03T01:30:23.4530596Z   AR      drivers/tee/teei/400/tz_driver/built-in.a
2026-05-03T01:30:23.4552972Z   CC      drivers/misc/mediatek/lens/mtk/sub/common/dw9814af/DW9814AF.o
2026-05-03T01:30:23.4760502Z   CC      drivers/tee/teei/400/tz_vfs/vfsFun.o
2026-05-03T01:30:23.6490382Z   CC      drivers/usb/core/hcd.o
2026-05-03T01:30:23.8913266Z   CC      drivers/misc/mediatek/lens/mtk/sub/common/dw9718af/DW9718AF.o
2026-05-03T01:30:24.0700611Z   CC      drivers/tee/teei/400/tz_vfs/fp_vendor.o
2026-05-03T01:30:24.0796601Z   CC      drivers/tty/n_tty.o
2026-05-03T01:30:24.3220890Z   CC      drivers/misc/mediatek/lens/mtk/sub/common/lc898214af/LC898214AF.o
2026-05-03T01:30:24.4620576Z   AR      drivers/tee/teei/400/tz_vfs/built-in.a
2026-05-03T01:30:24.4801867Z   CC      drivers/tee/teei/400/ut_keymaster/ut_keymaster.o
2026-05-03T01:30:24.7280533Z   CC      drivers/usb/core/urb.o
2026-05-03T01:30:24.7673369Z   CC      drivers/misc/mediatek/lens/mtk/sub/common/wv511aaf/WV511AAF.o
2026-05-03T01:30:25.0590771Z   AR      drivers/tee/teei/400/ut_keymaster/built-in.a
2026-05-03T01:30:25.0773091Z   AR      drivers/tee/teei/400/built-in.a
2026-05-03T01:30:25.0950233Z   AR      drivers/tee/teei/built-in.a
2026-05-03T01:30:25.1082197Z   AR      drivers/tee/built-in.a
2026-05-03T01:30:25.1376801Z   CC      drivers/usb/gadget/function/f_acm.o
2026-05-03T01:30:25.1907878Z   CC      drivers/misc/mediatek/lens/mtk/sub/common/ak7371af/AK7371AF.o
2026-05-03T01:30:25.2899620Z   CC      drivers/tty/tty_ioctl.o
2026-05-03T01:30:25.5827505Z   CC      drivers/usb/core/message.o
2026-05-03T01:30:25.6036499Z   CC      drivers/usb/gadget/function/u_serial.o
2026-05-03T01:30:25.6264109Z   AR      drivers/misc/mediatek/lens/mtk/sub/built-in.a
2026-05-03T01:30:25.6470462Z   CC      drivers/misc/mediatek/lens/mtk/sub2/sub2_lens.o
2026-05-03T01:30:26.1486438Z   AR      drivers/misc/mediatek/lens/mtk/sub2/built-in.a
2026-05-03T01:30:26.1641467Z   AR      drivers/misc/mediatek/lens/built-in.a
2026-05-03T01:30:26.1910479Z   CC      drivers/misc/mediatek/masp/asfv2/core/sec_boot_core.o
2026-05-03T01:30:26.2105828Z   CC      drivers/tty/tty_ldisc.o
2026-05-03T01:30:26.4820459Z   CC      drivers/usb/gadget/function/f_serial.o
2026-05-03T01:30:26.5314214Z   CC      drivers/misc/mediatek/masp/asfv2/core/sec_mod_core.o
2026-05-03T01:30:26.6882619Z   CC      drivers/usb/core/driver.o
2026-05-03T01:30:26.8851778Z   CC      drivers/misc/mediatek/masp/asfv2/core/sec_osal.o
2026-05-03T01:30:26.9590377Z   CC      drivers/tty/tty_buffer.o
2026-05-03T01:30:27.0050640Z   CC      drivers/usb/gadget/function/u_ether.o
2026-05-03T01:30:27.1190724Z ../drivers/usb/core/driver.c:508:21: warning: variable 'udev' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:27.1219953Z         struct usb_device *udev;
2026-05-03T01:30:27.1239898Z                            ^
2026-05-03T01:30:27.3320534Z 1 warning generated.
2026-05-03T01:30:27.4950713Z   CC      drivers/misc/mediatek/masp/asfv2/core/sec_legacy.o
2026-05-03T01:30:27.6240345Z   CC      drivers/usb/core/config.o
2026-05-03T01:30:27.6421136Z ../drivers/usb/gadget/function/u_ether.c:547:21: warning: variable 'net' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:27.6470142Z         struct net_device *net;
2026-05-03T01:30:27.6499926Z                            ^
2026-05-03T01:30:27.6510571Z ../drivers/usb/gadget/function/u_ether.c:720:16: warning: variable 'frag_total_len' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:27.6540053Z         unsigned int            frag_total_len = 0;
2026-05-03T01:30:27.6559887Z                                 ^
2026-05-03T01:30:27.6740450Z   CC      drivers/tty/tty_port.o
2026-05-03T01:30:27.8190679Z   CC      drivers/misc/mediatek/masp/asfv2/module/sec_mod.o
2026-05-03T01:30:27.8810788Z 2 warnings generated.
2026-05-03T01:30:28.2918187Z   CC      drivers/usb/gadget/function/f_rndis.o
2026-05-03T01:30:28.2965541Z   CC      drivers/usb/core/file.o
2026-05-03T01:30:28.3540862Z   CC      drivers/tty/tty_mutex.o
2026-05-03T01:30:28.6461811Z   CC      drivers/misc/mediatek/masp/asfv2/module/sec_clk.o
2026-05-03T01:30:28.9255362Z ../drivers/usb/gadget/function/f_rndis.c:514:28: warning: variable 'cdev' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:28.9276030Z         struct usb_composite_dev        *cdev;
2026-05-03T01:30:28.9293405Z                                          ^
2026-05-03T01:30:28.9336541Z ../drivers/usb/gadget/function/f_rndis.c:599:8: warning: variable 'MsgType' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:28.9389969Z                         u32 MsgType, MsgLength, MsgID;
2026-05-03T01:30:28.9420000Z                             ^
2026-05-03T01:30:28.9440616Z ../drivers/usb/gadget/function/f_rndis.c:599:17: warning: variable 'MsgLength' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:28.9466149Z                         u32 MsgType, MsgLength, MsgID;
2026-05-03T01:30:28.9470619Z                                      ^
2026-05-03T01:30:28.9474254Z ../drivers/usb/gadget/function/f_rndis.c:599:28: warning: variable 'MsgID' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:28.9475344Z                         u32 MsgType, MsgLength, MsgID;
2026-05-03T01:30:28.9476280Z                                                 ^
2026-05-03T01:30:28.9477067Z   CC      drivers/misc/mediatek/masp/asfv2/mach/hacc_lib.o
2026-05-03T01:30:28.9980347Z   CC      drivers/usb/core/buffer.o
2026-05-03T01:30:29.0020156Z   CC      drivers/tty/tty_ldsem.o
2026-05-03T01:30:29.0140212Z 4 warnings generated.
2026-05-03T01:30:29.2135244Z   CC      drivers/misc/mediatek/masp/asfv2/mach/hacc_export.o
2026-05-03T01:30:29.3940638Z   CC      drivers/usb/gadget/function/rndis.o
2026-05-03T01:30:29.4700906Z   CC      drivers/tty/tty_baudrate.o
2026-05-03T01:30:29.5040465Z   CC      drivers/usb/core/sysfs.o
2026-05-03T01:30:29.5787521Z   CC      drivers/misc/mediatek/masp/asfv2/mach/hacc_hk.o
2026-05-03T01:30:29.8833287Z   CC      drivers/misc/mediatek/masp/asfv2/mach/hacc_sk.o
2026-05-03T01:30:30.0827530Z   CC      drivers/tty/tty_jobctrl.o
2026-05-03T01:30:30.0840106Z   CC      drivers/usb/core/endpoint.o
2026-05-03T01:30:30.1560647Z   CC      drivers/misc/mediatek/masp/asfv2/mach/sec_lib.o
2026-05-03T01:30:30.4680786Z   CC      drivers/misc/mediatek/masp/asfv2/mach/mt6768/security_ao.o
2026-05-03T01:30:30.5570415Z   CC      drivers/usb/core/devio.o
2026-05-03T01:30:30.5798733Z   CC      drivers/usb/gadget/function/f_mass_storage.o
2026-05-03T01:30:30.8010405Z   CC      drivers/tty/n_null.o
2026-05-03T01:30:30.8710701Z   AR      drivers/misc/mediatek/masp/built-in.a
2026-05-03T01:30:30.8980709Z   CC      drivers/misc/mediatek/mdp/mdp_ioctl_ex.o
2026-05-03T01:30:31.1300891Z ../drivers/usb/gadget/function/f_mass_storage.c:977:16: warning: variable 'rc' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:31.1360015Z         unsigned long   rc;
2026-05-03T01:30:31.1419935Z                         ^
2026-05-03T01:30:31.2070588Z   CC      drivers/tty/pty.o
2026-05-03T01:30:31.5810391Z 1 warning generated.
2026-05-03T01:30:31.7030564Z   CC      drivers/usb/core/notify.o
2026-05-03T01:30:31.7910742Z   CC      drivers/misc/mediatek/mdp/mdp_m4u.o
2026-05-03T01:30:31.8138360Z   CC      drivers/tty/tty_audit.o
2026-05-03T01:30:31.9040801Z   CC      drivers/usb/gadget/function/storage_common.o
2026-05-03T01:30:32.3490549Z   CC      drivers/usb/core/generic.o
2026-05-03T01:30:32.3650390Z   CC      drivers/tty/sysrq.o
2026-05-03T01:30:32.3685726Z   AR      drivers/misc/mediatek/mdp/built-in.a
2026-05-03T01:30:32.3890668Z   CC      drivers/misc/mediatek/memory-amms/memory-amms.o
2026-05-03T01:30:32.7570587Z   CC      drivers/usb/gadget/function/f_fs.o
2026-05-03T01:30:32.9850438Z   CC      drivers/usb/core/quirks.o
2026-05-03T01:30:33.4290576Z   AR      drivers/tty/built-in.a
2026-05-03T01:30:33.4490459Z   AR      drivers/misc/mediatek/memory-amms/built-in.a
2026-05-03T01:30:33.4700550Z   CC      drivers/usb/host/ehci-hcd.o
2026-05-03T01:30:33.4730646Z   CC      drivers/misc/mediatek/mmdvfs/swpm_me.o
2026-05-03T01:30:33.5210402Z   CC      drivers/usb/core/devices.o
2026-05-03T01:30:33.7640900Z   CC      drivers/misc/mediatek/mmdvfs/mmdvfs_pmqos.o
2026-05-03T01:30:34.1439996Z   CC      drivers/usb/core/phy.o
2026-05-03T01:30:34.1750488Z   CC      drivers/usb/gadget/function/f_midi.o
2026-05-03T01:30:34.6459737Z   CC      drivers/usb/core/port.o
2026-05-03T01:30:34.8050686Z   CC      drivers/usb/gadget/function/f_hid.o
2026-05-03T01:30:34.9587173Z   CC      drivers/misc/mediatek/mmdvfs/mmdvfs_plat_default.o
2026-05-03T01:30:35.1587585Z   CC      drivers/usb/core/of.o
2026-05-03T01:30:35.2932679Z   AR      drivers/misc/mediatek/mmdvfs/built-in.a
2026-05-03T01:30:35.3203338Z   CC      drivers/misc/mediatek/mmp/src/mmprofile.o
2026-05-03T01:30:35.3910713Z   CC      drivers/usb/gadget/function/f_accessory.o
2026-05-03T01:30:35.4290326Z   CC      drivers/usb/host/ohci-hcd.o
2026-05-03T01:30:35.7880410Z   AR      drivers/usb/core/built-in.a
2026-05-03T01:30:35.8210343Z   CC      drivers/misc/mediatek/monitor_hang/monitor_hang.o
2026-05-03T01:30:36.3500945Z   CC      drivers/usb/gadget/function/f_audio_source.o
2026-05-03T01:30:36.5000543Z   AR      drivers/misc/mediatek/mmp/src/built-in.a
2026-05-03T01:30:36.5120521Z   AR      drivers/misc/mediatek/mmp/built-in.a
2026-05-03T01:30:36.5310564Z   AR      drivers/usb/gadget/legacy/built-in.a
2026-05-03T01:30:36.5460060Z   CC      drivers/usb/misc/trancevibrator.o
2026-05-03T01:30:36.7590445Z   AR      drivers/misc/mediatek/monitor_hang/built-in.a
2026-05-03T01:30:36.7786509Z   CC      drivers/misc/mediatek/mtprintk/mtk_printk_ctrl.o
2026-05-03T01:30:36.7923501Z   CC      drivers/usb/host/xhci.o
2026-05-03T01:30:36.9180107Z   CC      drivers/usb/gadget/function/f_mtp.o
2026-05-03T01:30:36.9430519Z   AR      drivers/usb/misc/built-in.a
2026-05-03T01:30:36.9600641Z   CC      drivers/misc/mediatek/mtprof/bootprof.o
2026-05-03T01:30:37.3340603Z   AR      drivers/misc/mediatek/mtprintk/built-in.a
2026-05-03T01:30:37.3550700Z   CC      drivers/usb/gadget/udc/core.o
2026-05-03T01:30:38.0812510Z   CC      drivers/usb/gadget/function/f_ptp.o
2026-05-03T01:30:38.2195709Z   AR      drivers/misc/mediatek/mtprof/built-in.a
2026-05-03T01:30:38.2438128Z   CC      drivers/misc/mediatek/perf_common/perf_common.o
2026-05-03T01:30:38.4630730Z   CC      drivers/usb/gadget/udc/trace.o
2026-05-03T01:30:38.5560417Z   AR      drivers/usb/gadget/function/built-in.a
2026-05-03T01:30:38.5868506Z   CC      drivers/usb/host/xhci-mem.o
2026-05-03T01:30:38.5930372Z   CC      drivers/video/backlight/backlight.o
2026-05-03T01:30:39.0853342Z   CC      drivers/misc/mediatek/perf_common/perf_tracker.o
2026-05-03T01:30:39.1438774Z   AR      drivers/usb/gadget/udc/built-in.a
2026-05-03T01:30:39.1560198Z   CC      drivers/usb/gadget/usbstring.o
2026-05-03T01:30:39.4140484Z   AR      drivers/video/backlight/built-in.a
2026-05-03T01:30:39.4410433Z   CC      drivers/video/fbdev/core/fb_cmdline.o
2026-05-03T01:30:39.8260631Z   CC      drivers/usb/gadget/config.o
2026-05-03T01:30:39.8410562Z   CC      drivers/usb/host/xhci-ext-caps.o
2026-05-03T01:30:40.1830356Z   CC      drivers/video/fbdev/core/fb_notify.o
2026-05-03T01:30:40.4794266Z   CC      drivers/usb/host/xhci-ring.o
2026-05-03T01:30:40.5924395Z   CC      drivers/usb/gadget/epautoconf.o
2026-05-03T01:30:40.6486423Z   AR      drivers/misc/mediatek/perf_common/built-in.a
2026-05-03T01:30:40.6753562Z   CC      drivers/misc/mediatek/performance/base/utility.o
2026-05-03T01:30:40.8730728Z   CC      drivers/video/fbdev/core/fbmem.o
2026-05-03T01:30:41.2340749Z   AR      drivers/misc/mediatek/performance/base/built-in.a
2026-05-03T01:30:41.2600502Z   CC      drivers/misc/mediatek/performance/boost_ctrl/cpu_ctrl/cpu_ctrl.o
2026-05-03T01:30:41.2980486Z   CC      drivers/usb/gadget/composite.o
2026-05-03T01:30:41.7954152Z   CC      drivers/usb/host/xhci-hub.o
2026-05-03T01:30:42.1860631Z   CC      drivers/video/fbdev/core/fbmon.o
2026-05-03T01:30:42.2780608Z   CC      drivers/misc/mediatek/performance/boost_ctrl/cpu_ctrl/cpu_ctrl_cfp.o
2026-05-03T01:30:42.4351962Z   CC      drivers/usb/gadget/functions.o
2026-05-03T01:30:42.6690616Z   CC      drivers/usb/host/xhci-dbg.o
2026-05-03T01:30:42.9680706Z   AR      drivers/misc/mediatek/performance/boost_ctrl/cpu_ctrl/built-in.a
2026-05-03T01:30:42.9892493Z   CC      drivers/misc/mediatek/performance/boost_ctrl/dram_ctrl/dram_ctrl.o
2026-05-03T01:30:43.1395907Z   CC      drivers/usb/gadget/configfs.o
2026-05-03T01:30:43.1718886Z   CC      drivers/video/fbdev/core/fbcmap.o
2026-05-03T01:30:43.3179835Z   CC      drivers/usb/host/xhci-trace.o
2026-05-03T01:30:43.4700657Z   AR      drivers/misc/mediatek/performance/boost_ctrl/dram_ctrl/built-in.a
2026-05-03T01:30:43.4930570Z   CC      drivers/misc/mediatek/performance/boost_ctrl/eas_ctrl/eas_ctrl.o
2026-05-03T01:30:43.9770465Z   CC      drivers/video/fbdev/core/fbsysfs.o
2026-05-03T01:30:44.1240647Z   CC      drivers/usb/gadget/u_f.o
2026-05-03T01:30:44.1420796Z   CC      drivers/misc/mediatek/performance/boost_ctrl/eas_ctrl/uclamp_ctrl.o
2026-05-03T01:30:44.4240798Z ../drivers/video/fbdev/core/fbsysfs.c:522:12: warning: variable 'err' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:44.4269894Z         int data, err;
2026-05-03T01:30:44.4280005Z                   ^
2026-05-03T01:30:44.5111090Z 1 warning generated.
2026-05-03T01:30:44.6250543Z   AR      drivers/usb/host/built-in.a
2026-05-03T01:30:44.6520248Z   CC      drivers/virtio/virtio.o
2026-05-03T01:30:44.7578987Z   CC      drivers/usb/gadget/meta.o
2026-05-03T01:30:44.7786457Z   CC      drivers/video/fbdev/core/modedb.o
2026-05-03T01:30:45.0580762Z   AR      drivers/misc/mediatek/performance/boost_ctrl/eas_ctrl/built-in.a
2026-05-03T01:30:45.0790644Z   CC      drivers/misc/mediatek/performance/boost_ctrl/topo_ctrl/topo_ctrl.o
2026-05-03T01:30:45.1750929Z ../drivers/usb/gadget/meta.c:758:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:45.1770224Z         int ret;
2026-05-03T01:30:45.1800070Z             ^
2026-05-03T01:30:45.2950654Z 1 warning generated.
2026-05-03T01:30:45.3376646Z   AR      drivers/usb/gadget/built-in.a
2026-05-03T01:30:45.3645695Z   CC      drivers/virtio/virtio_ring.o
2026-05-03T01:30:45.3810431Z   CC      drivers/usb/phy/phy.o
2026-05-03T01:30:45.6461050Z   CC      drivers/video/fbdev/core/fbcvt.o
2026-05-03T01:30:46.0640711Z   CC      drivers/usb/phy/of.o
2026-05-03T01:30:46.1380494Z   CC      drivers/video/fbdev/core/cfbfillrect.o
2026-05-03T01:30:46.4063581Z   AR      drivers/virtio/built-in.a
2026-05-03T01:30:46.4356899Z   AR      drivers/video/fbdev/omap2/omapfb/displays/built-in.a
2026-05-03T01:30:46.4385633Z   AR      drivers/misc/mediatek/performance/boost_ctrl/topo_ctrl/built-in.a
2026-05-03T01:30:46.4490373Z   CC      drivers/misc/mediatek/performance/boost_ctrl/boostctrl_main.o
2026-05-03T01:30:46.4520055Z   AR      drivers/video/fbdev/omap2/omapfb/dss/built-in.a
2026-05-03T01:30:46.4630921Z   AR      drivers/video/fbdev/omap2/omapfb/built-in.a
2026-05-03T01:30:46.4770179Z   AR      drivers/video/fbdev/omap2/built-in.a
2026-05-03T01:30:46.4970555Z   CC      drivers/watchdog/watchdog_core.o
2026-05-03T01:30:46.6900621Z   CC      drivers/usb/phy/phy-generic.o
2026-05-03T01:30:46.7680532Z   AR      drivers/misc/mediatek/performance/boost_ctrl/built-in.a
2026-05-03T01:30:46.7957439Z   CC      drivers/misc/mediatek/performance/fpsgo_v3_topology/base/src/fpsgo_base.o
2026-05-03T01:30:46.9100768Z   CC      drivers/video/fbdev/core/cfbcopyarea.o
2026-05-03T01:30:47.0370694Z   CC      drivers/watchdog/watchdog_dev.o
2026-05-03T01:30:47.4920506Z   AR      drivers/usb/phy/built-in.a
2026-05-03T01:30:47.5140540Z   CC      drivers/usb/roles/class.o
2026-05-03T01:30:47.5530401Z   CC      drivers/watchdog/mtk_wdt.o
2026-05-03T01:30:47.7310602Z   CC      drivers/video/fbdev/core/cfbimgblt.o
2026-05-03T01:30:47.7820792Z   CC      drivers/misc/mediatek/performance/fpsgo_v3_topology/base/src/fpsgo_sysfs.o
2026-05-03T01:30:47.9124235Z   AR      drivers/watchdog/built-in.a
2026-05-03T01:30:47.9331617Z   CC      drivers/video/logo/logo.o
2026-05-03T01:30:47.9745666Z   AR      drivers/usb/roles/built-in.a
2026-05-03T01:30:47.9970276Z   CC      drivers/usb/storage/scsiglue.o
2026-05-03T01:30:48.0370825Z   AR      drivers/misc/mediatek/performance/fpsgo_v3_topology/base/built-in.a
2026-05-03T01:30:48.0577877Z   CC      drivers/misc/mediatek/performance/fpsgo_v3_topology/composer/src/fps_composer.o
2026-05-03T01:30:48.3700449Z   LOGO    drivers/video/logo/logo_linux_mono.c
2026-05-03T01:30:48.3739980Z   LOGO    drivers/video/logo/logo_linux_vga16.c
2026-05-03T01:30:48.3759975Z   LOGO    drivers/video/logo/logo_linux_clut224.c
2026-05-03T01:30:48.3809993Z   LOGO    drivers/video/logo/logo_superh_mono.c
2026-05-03T01:30:48.3819933Z   LOGO    drivers/video/logo/clut_vga16.c
2026-05-03T01:30:48.3839967Z   LOGO    drivers/video/logo/logo_superh_vga16.c
2026-05-03T01:30:48.3870852Z   LOGO    drivers/video/logo/logo_dec_clut224.c
2026-05-03T01:30:48.3909977Z   LOGO    drivers/video/logo/logo_mac_clut224.c
2026-05-03T01:30:48.3960053Z   LOGO    drivers/video/logo/logo_parisc_clut224.c
2026-05-03T01:30:48.3999961Z   LOGO    drivers/video/logo/logo_sgi_clut224.c
2026-05-03T01:30:48.4040081Z   LOGO    drivers/video/logo/logo_spe_clut224.c
2026-05-03T01:30:48.4079999Z   LOGO    drivers/video/logo/logo_sun_clut224.c
2026-05-03T01:30:48.4110439Z   LOGO    drivers/video/logo/logo_superh_clut224.c
2026-05-03T01:30:48.4169956Z   CC      drivers/video/logo/logo_linux_mono.o
2026-05-03T01:30:48.4590409Z   CC      drivers/video/logo/logo_linux_vga16.o
2026-05-03T01:30:48.4890431Z   AR      drivers/video/fbdev/core/built-in.a
2026-05-03T01:30:48.5040347Z   CC      drivers/video/logo/logo_linux_clut224.o
2026-05-03T01:30:48.5130266Z   AR      drivers/video/fbdev/built-in.a
2026-05-03T01:30:48.5340342Z   CC      drivers/misc/mediatek/pidmap/pidmap.o
2026-05-03T01:30:48.5570490Z   AR      drivers/video/logo/built-in.a
2026-05-03T01:30:48.5730177Z   AR      drivers/video/built-in.a
2026-05-03T01:30:48.5900458Z   CC      drivers/usb/storage/protocol.o
2026-05-03T01:30:48.6084549Z   AR      drivers/misc/mediatek/performance/fpsgo_v3_topology/composer/built-in.a
2026-05-03T01:30:48.6301170Z   CC      drivers/misc/mediatek/performance/fpsgo_v3_topology/fbt/platform/mt6768/fbt_cpu_platform.o
2026-05-03T01:30:48.9370625Z   CC      drivers/misc/mediatek/performance/load_track/load_track.o
2026-05-03T01:30:49.0470875Z   CC      drivers/misc/mediatek/performance/fpsgo_v3_topology/fbt/src/fbt_cpu.o
2026-05-03T01:30:49.0999920Z   AR      drivers/misc/mediatek/pidmap/built-in.a
2026-05-03T01:30:49.1330460Z   CC      drivers/misc/mediatek/performance/observer/platform/mt6768/qos_pfm.o
2026-05-03T01:30:49.3480720Z   AR      drivers/misc/mediatek/performance/load_track/built-in.a
2026-05-03T01:30:49.3720448Z   AR      drivers/usb/typec/altmodes/built-in.a
2026-05-03T01:30:49.3890248Z   AR      drivers/usb/typec/fusb302/built-in.a
2026-05-03T01:30:49.4060257Z   AR      drivers/usb/typec/mux/built-in.a
2026-05-03T01:30:49.4160182Z   CC      drivers/usb/typec/class.o
2026-05-03T01:30:49.4880392Z   CC      drivers/usb/storage/transport.o
2026-05-03T01:30:49.6940817Z   CC      drivers/misc/mediatek/performance/observer/platform/mt6768/obpfm_qos_bound.o
2026-05-03T01:30:50.0661167Z   CC      drivers/usb/typec/mux.o
2026-05-03T01:30:50.2920815Z   AR      drivers/misc/mediatek/performance/observer/platform/mt6768/built-in.a
2026-05-03T01:30:50.3040336Z   CC      drivers/misc/mediatek/performance/observer/pob_main.o
2026-05-03T01:30:50.4948809Z   CC      drivers/usb/storage/usb.o
2026-05-03T01:30:50.6140400Z   CC      drivers/usb/typec/bus.o
2026-05-03T01:30:50.8030828Z   CC      drivers/misc/mediatek/performance/fpsgo_v3_topology/fbt/src/xgf.o
2026-05-03T01:30:50.8700697Z   CC      drivers/misc/mediatek/performance/observer/fpsgo_notify.o
2026-05-03T01:30:51.0710703Z   CC      drivers/misc/mediatek/performance/observer/qos_notify.o
2026-05-03T01:30:51.0950568Z   AR      drivers/usb/typec/built-in.a
2026-05-03T01:30:51.1210602Z   CC      drivers/misc/mediatek/performance/fpsgo_v3_topology/fstb/fstb.o
2026-05-03T01:30:51.4950642Z   CC      drivers/usb/storage/initializers.o
2026-05-03T01:30:51.6530781Z   CC      drivers/misc/mediatek/performance/observer/nn_notify.o
2026-05-03T01:30:51.8660732Z   CC      drivers/misc/mediatek/performance/observer/xpu_notify.o
2026-05-03T01:30:52.0724940Z   CC      drivers/usb/storage/sierra_ms.o
2026-05-03T01:30:52.0919764Z   AR      drivers/misc/mediatek/performance/fpsgo_v3_topology/fstb/built-in.a
2026-05-03T01:30:52.1201874Z   CC      drivers/misc/mediatek/pmic/common/upmu.o
2026-05-03T01:30:52.1463543Z   CC      drivers/misc/mediatek/performance/observer/eara_thrm_notify.o
2026-05-03T01:30:52.3240897Z   CC      drivers/misc/mediatek/performance/fpsgo_v3_topology/fbt/src/mini_top.o
2026-05-03T01:30:52.3270368Z   AR      drivers/misc/mediatek/performance/observer/built-in.a
2026-05-03T01:30:52.3530516Z   CC      drivers/misc/mediatek/pmic/mt6358/v1/pmic_ipi.o
2026-05-03T01:30:52.6851245Z   CC      drivers/misc/mediatek/pmic/mt6358/v1/mt6358_gauge.o
2026-05-03T01:30:52.6980437Z   CC      drivers/usb/storage/option_ms.o
2026-05-03T01:30:53.1020812Z   CC      drivers/misc/mediatek/pmic/common/upmu_regulator.o
2026-05-03T01:30:53.2130457Z   CC      drivers/usb/storage/usual-tables.o
2026-05-03T01:30:53.3795160Z   CC      drivers/misc/mediatek/performance/fpsgo_v3_topology/fbt/src/uboost.o
2026-05-03T01:30:53.6647361Z   CC      drivers/usb/storage/alauda.o
2026-05-03T01:30:53.8070736Z   CC      drivers/misc/mediatek/pmic/mt6358/v1/pmic.o
2026-05-03T01:30:53.8420767Z   CC      drivers/misc/mediatek/pmic/common/upmu_debugfs.o
2026-05-03T01:30:54.2161181Z ../drivers/usb/storage/alauda.c:455:6: warning: variable 'rc' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:54.2200087Z         int rc;
2026-05-03T01:30:54.2229905Z             ^
2026-05-03T01:30:54.2470437Z   AR      drivers/misc/mediatek/performance/fpsgo_v3_topology/fbt/built-in.a
2026-05-03T01:30:54.2560230Z   CC      drivers/misc/mediatek/performance/fpsgo_v3_topology/fpsgo_main.o
2026-05-03T01:30:54.4360479Z   CC      drivers/misc/mediatek/pmic/mt6358/v1/pmic_common.o
2026-05-03T01:30:54.4390465Z   CC      drivers/misc/mediatek/pmic/common/upmu_initial_setting.o
2026-05-03T01:30:54.5430381Z 1 warning generated.
2026-05-03T01:30:54.5760650Z   CC      drivers/usb/storage/cypress_atacb.o
2026-05-03T01:30:54.9262811Z   AR      drivers/misc/mediatek/performance/fpsgo_v3_topology/built-in.a
2026-05-03T01:30:54.9500441Z   CC      drivers/misc/mediatek/performance/perf_ioctl/perf_ioctl.o
2026-05-03T01:30:55.0010795Z   CC      drivers/misc/mediatek/pmic/common/upmu_lbat_service.o
2026-05-03T01:30:55.1600464Z   CC      drivers/misc/mediatek/pmic/mt6358/v1/pmic_debugfs.o
2026-05-03T01:30:55.2170649Z   CC      drivers/usb/storage/datafab.o
2026-05-03T01:30:55.5800683Z   AR      drivers/misc/mediatek/performance/perf_ioctl/built-in.a
2026-05-03T01:30:55.6131605Z   CC      drivers/misc/mediatek/performance/resym/platform/mt6768/rs_vpu_pfm.o
2026-05-03T01:30:55.6780786Z   CC      drivers/misc/mediatek/performance/resym/platform/mt6768/rs_mdla_pfm.o
2026-05-03T01:30:55.7180792Z   AR      drivers/misc/mediatek/performance/resym/platform/mt6768/built-in.a
2026-05-03T01:30:55.7236935Z   CC      drivers/misc/mediatek/pmic/mt6358/v1/pmic_irq.o
2026-05-03T01:30:55.7310493Z   CC      drivers/misc/mediatek/performance/resym/rs_trace.o
2026-05-03T01:30:55.7400581Z   AR      drivers/misc/mediatek/pmic/common/built-in.a
2026-05-03T01:30:55.7660505Z   CC      drivers/misc/mediatek/pmic_wrap/mt6768/pwrap_hal.o
2026-05-03T01:30:55.8380379Z   CC      drivers/usb/storage/freecom.o
2026-05-03T01:30:56.2991268Z   CC      drivers/misc/mediatek/performance/resym/rs_base.o
2026-05-03T01:30:56.3030185Z   AR      drivers/misc/mediatek/pmic_wrap/mt6768/built-in.a
2026-05-03T01:30:56.3120191Z   CC      drivers/misc/mediatek/pmic_wrap/mtk_pmic_wrap.o
2026-05-03T01:30:56.4240507Z   CC      drivers/misc/mediatek/pmic/mt6358/v1/pmic_initial_setting.o
2026-05-03T01:30:56.4750675Z   CC      drivers/usb/storage/isd200.o
2026-05-03T01:30:56.7311274Z   CC      drivers/misc/mediatek/performance/resym/rs_main.o
2026-05-03T01:30:57.0300644Z   CC      drivers/misc/mediatek/performance/resym/rs_usage.o
2026-05-03T01:30:57.0388967Z   AR      drivers/misc/mediatek/pmic_wrap/built-in.a
2026-05-03T01:30:57.0620543Z   CC      drivers/misc/mediatek/pmic/mt6358/v1/pmic_api.o
2026-05-03T01:30:57.0638213Z   CC      drivers/misc/mediatek/performance/syslimiter/syslimiter.o
2026-05-03T01:30:57.1375279Z   CC      drivers/usb/storage/jumpshot.o
2026-05-03T01:30:57.7070806Z   AR      drivers/misc/mediatek/performance/syslimiter/built-in.a
2026-05-03T01:30:57.7318360Z   CC      drivers/misc/mediatek/pmic/mt6370/v1/mt6370_pmu_i2c.o
2026-05-03T01:30:57.8150697Z   CC      drivers/usb/storage/karma.o
2026-05-03T01:30:58.0590985Z   CC      drivers/misc/mediatek/performance/resym/rs_state.o
2026-05-03T01:30:58.3660681Z   CC      drivers/misc/mediatek/performance/resym/rs_index.o
2026-05-03T01:30:58.4210745Z   CC      drivers/usb/storage/onetouch.o
2026-05-03T01:30:58.4660784Z   CC      drivers/misc/mediatek/pmic/mt6370/v1/mt6370_pmu_regmap.o
2026-05-03T01:30:59.0160605Z   CC      drivers/usb/storage/sddr09.o
2026-05-03T01:30:59.0650743Z   CC      drivers/misc/mediatek/pmic/mt6370/v1/mt6370_pmu_irq.o
2026-05-03T01:30:59.0665753Z   AR      drivers/misc/mediatek/performance/resym/built-in.a
2026-05-03T01:30:59.0941187Z   CC      drivers/misc/mediatek/performance/tchbst/user/utch.o
2026-05-03T01:30:59.5341336Z ../drivers/misc/mediatek/pmic/mt6370/v1/mt6370_pmu_irq.c:196:5: warning: variable 'irq_ind' set but not used [-Wunused-but-set-variable]
2026-05-03T01:30:59.5369202Z         u8 irq_ind = 0, data[16] = { 0 }, mask[16] = {
2026-05-03T01:30:59.5399902Z            ^
2026-05-03T01:30:59.5920453Z 1 warning generated.
2026-05-03T01:30:59.7621154Z   AR      drivers/misc/mediatek/performance/tchbst/user/built-in.a
2026-05-03T01:30:59.7830503Z   CC      drivers/misc/mediatek/performance/tchbst/tchbst_main.o
2026-05-03T01:30:59.8279743Z   CC      drivers/misc/mediatek/pmic/mt6370/v1/mt6370_pmu_subdevs.o
2026-05-03T01:30:59.9418294Z   CC      drivers/usb/storage/sddr55.o
2026-05-03T01:31:00.0820755Z   CC      drivers/misc/mediatek/pmic/mt6358/v1/pmic_auxadc.o
2026-05-03T01:31:00.3010788Z   AR      drivers/misc/mediatek/performance/tchbst/built-in.a
2026-05-03T01:31:00.3190565Z   CC      drivers/misc/mediatek/performance/uload_ind/uload_ind.o
2026-05-03T01:31:00.5061126Z   CC      drivers/misc/mediatek/pmic/mt6370/v1/mt6370_pmu_core.o
2026-05-03T01:31:00.6430679Z   CC      drivers/usb/storage/shuttle_usbat.o
2026-05-03T01:31:00.7460725Z   AR      drivers/misc/mediatek/performance/uload_ind/built-in.a
2026-05-03T01:31:00.7551001Z   CC      drivers/misc/mediatek/performance/perfmgr_main.o
2026-05-03T01:31:00.9176337Z   CC      drivers/misc/mediatek/pmic/mt6370/v1/mt6370_pmu_ldo.o
2026-05-03T01:31:01.0667037Z   CC      drivers/misc/mediatek/pmic/mt6358/v1/regulator_codegen.o
2026-05-03T01:31:01.3160935Z   AR      drivers/misc/mediatek/performance/built-in.a
2026-05-03T01:31:01.3469891Z   CC      drivers/misc/mediatek/power/mt6768/mtk_battery_intf.o
2026-05-03T01:31:01.3900567Z   AR      drivers/usb/storage/built-in.a
2026-05-03T01:31:01.4206460Z   AR      drivers/usb/built-in.a
2026-05-03T01:31:01.4440508Z   CC      drivers/misc/mediatek/pmic/mtk_battery_adc_intf.o
2026-05-03T01:31:01.5095065Z   CC      drivers/misc/mediatek/pmic/mt6370/v1/mt6370_pmu_dsv.o
2026-05-03T01:31:02.0712034Z   CC      drivers/misc/mediatek/pmic/mt6358/v1/pmic_lp_api.o
2026-05-03T01:31:02.1240781Z   CC      drivers/misc/mediatek/pmic/mt6370/v1/mt6370_pmu_dsv_debugfs.o
2026-05-03T01:31:02.2920766Z   CC      drivers/misc/mediatek/pmic/mt6370/v1/mt6370_pmu_fled.o
2026-05-03T01:31:02.5940462Z   AR      drivers/misc/mediatek/power/mt6768/built-in.a
2026-05-03T01:31:02.6024067Z   CC      drivers/misc/mediatek/pwm/mt6768/mtk_pwm_hal.o
2026-05-03T01:31:02.6082226Z   AR      drivers/misc/mediatek/power/built-in.a
2026-05-03T01:31:02.6270911Z   CC      drivers/misc/mediatek/rps/rps_perf.o
2026-05-03T01:31:02.6441427Z   CC      drivers/misc/mediatek/pmic/mt6358/v1/pmic_efuse.o
2026-05-03T01:31:02.6740449Z   CC      drivers/misc/mediatek/pmic/mt6370/v1/mt6370_pmu_bled.o
2026-05-03T01:31:02.8360798Z   CC      drivers/misc/mediatek/pmic/mt6358/v1/pmic_throttling_dlpt.o
2026-05-03T01:31:03.1355414Z   AR      drivers/misc/mediatek/pmic/mt6370/v1/built-in.a
2026-05-03T01:31:03.1519246Z   AR      drivers/misc/mediatek/pmic/mt6370/built-in.a
2026-05-03T01:31:03.1646218Z   CC      drivers/misc/mediatek/pwm/mtk_pwm.o
2026-05-03T01:31:03.1700940Z   AR      drivers/misc/mediatek/pwm/mt6768/built-in.a
2026-05-03T01:31:03.1895331Z   CC      drivers/misc/mediatek/rt-regmap/rt-regmap.o
2026-05-03T01:31:03.8280677Z   AR      drivers/misc/mediatek/pmic/mt6358/v1/built-in.a
2026-05-03T01:31:03.8414899Z   AR      drivers/misc/mediatek/pmic/mt6358/built-in.a
2026-05-03T01:31:03.8620051Z   AR      drivers/misc/mediatek/pmic/built-in.a
2026-05-03T01:31:03.8863973Z   AR      drivers/misc/mediatek/rps/built-in.a
2026-05-03T01:31:03.8883924Z   CC      drivers/misc/mediatek/rtc/mtk_rtc_debug_v1.o
2026-05-03T01:31:03.9140648Z   CC      drivers/misc/mediatek/scp/cm4/scp_feature_table.o
2026-05-03T01:31:04.0040518Z   AR      drivers/misc/mediatek/rt-regmap/built-in.a
2026-05-03T01:31:04.0410772Z   CC      drivers/misc/mediatek/sensors-1.0/accelerometer/accelhub/accelhub.o
2026-05-03T01:31:04.0670849Z   AR      drivers/misc/mediatek/pwm/built-in.a
2026-05-03T01:31:04.0940493Z   CC      drivers/misc/mediatek/sensors-1.0/alsps/alspshub/alspshub.o
2026-05-03T01:31:04.2230698Z   CC      drivers/misc/mediatek/scp/cm4/scp_awake.o
2026-05-03T01:31:04.3300671Z   AR      drivers/misc/mediatek/rtc/built-in.a
2026-05-03T01:31:04.3430696Z   CC      drivers/misc/mediatek/sensors-1.0/alsps/alsps.o
2026-05-03T01:31:04.6026835Z   AR      drivers/misc/mediatek/sensors-1.0/accelerometer/accelhub/built-in.a
2026-05-03T01:31:04.6117044Z   CC      drivers/misc/mediatek/sensors-1.0/accelerometer/accel.o
2026-05-03T01:31:04.9251534Z   AR      drivers/misc/mediatek/sensors-1.0/alsps/alspshub/built-in.a
2026-05-03T01:31:04.9361061Z   CC      drivers/misc/mediatek/sensors-1.0/alsps/alsps_factory.o
2026-05-03T01:31:05.0490152Z   CC      drivers/misc/mediatek/scp/cm4/scp_dvfs.o
2026-05-03T01:31:05.2009333Z   CC      drivers/misc/mediatek/sensors-1.0/gyroscope/gyrohub/gyrohub.o
2026-05-03T01:31:05.4120832Z   CC      drivers/misc/mediatek/sensors-1.0/accelerometer/accel_factory.o
2026-05-03T01:31:05.4660669Z   CC      drivers/misc/mediatek/sensors-1.0/alsps/aal_control.o
2026-05-03T01:31:05.7440857Z   AR      drivers/misc/mediatek/sensors-1.0/gyroscope/gyrohub/built-in.a
2026-05-03T01:31:05.7560467Z   CC      drivers/misc/mediatek/sensors-1.0/gyroscope/gyroscope.o
2026-05-03T01:31:05.8184651Z   CC      drivers/misc/mediatek/scp/cm4/./v01/scp_helper.o
2026-05-03T01:31:05.9270788Z   AR      drivers/misc/mediatek/sensors-1.0/accelerometer/built-in.a
2026-05-03T01:31:05.9438010Z   AR      drivers/misc/mediatek/sensors-1.0/alsps/built-in.a
2026-05-03T01:31:05.9480125Z   CC      drivers/misc/mediatek/smi/smi_drv.o
2026-05-03T01:31:05.9561364Z   CC      drivers/misc/mediatek/sensors-1.0/gyroscope/gyro_factory.o
2026-05-03T01:31:06.4810719Z   CC      drivers/misc/mediatek/spi_slave_drv/spi_slave.o
2026-05-03T01:31:06.5785233Z   AR      drivers/misc/mediatek/sensors-1.0/gyroscope/built-in.a
2026-05-03T01:31:06.6036107Z   CC      drivers/misc/mediatek/sensors-1.0/hwmon/hwmsen/hwmsen_helper.o
2026-05-03T01:31:06.9044560Z   CC      drivers/misc/mediatek/scp/cm4/./v01/scp_excep.o
2026-05-03T01:31:06.9910522Z   AR      drivers/misc/mediatek/spi_slave_drv/built-in.a
2026-05-03T01:31:07.0170711Z   CC      drivers/misc/mediatek/sensors-1.0/magnetometer/maghub/maghub.o
2026-05-03T01:31:07.1083720Z   AR      drivers/misc/mediatek/smi/built-in.a
2026-05-03T01:31:07.1310676Z   CC      drivers/misc/mediatek/sensors-1.0/hwmon/sensor_attributes/sensor_attr.o
2026-05-03T01:31:07.3246948Z   AR      drivers/misc/mediatek/sensors-1.0/hwmon/hwmsen/built-in.a
2026-05-03T01:31:07.3350984Z   CC      drivers/misc/mediatek/scp/cm4/./v01/scp_ipi.o
2026-05-03T01:31:07.3530843Z   CC      drivers/misc/mediatek/sensors-1.0/hwmon/sensor_dts/sensor_dts.o
2026-05-03T01:31:07.5363309Z   AR      drivers/misc/mediatek/sensors-1.0/magnetometer/maghub/built-in.a
2026-05-03T01:31:07.5450648Z   AR      drivers/misc/mediatek/sensors-1.0/hwmon/sensor_attributes/built-in.a
2026-05-03T01:31:07.5480182Z   CC      drivers/misc/mediatek/sensors-1.0/magnetometer/mag.o
2026-05-03T01:31:07.5650434Z   CC      drivers/misc/mediatek/sensors-1.0/sensorHub/SCP_nanoHub/SCP_nanoHub.o
2026-05-03T01:31:07.7702520Z   AR      drivers/misc/mediatek/sensors-1.0/hwmon/sensor_dts/built-in.a
2026-05-03T01:31:07.7890596Z   CC      drivers/misc/mediatek/sensors-1.0/hwmon/sensor_event/sensor_event.o
2026-05-03T01:31:07.8330781Z   CC      drivers/misc/mediatek/scp/cm4/./v01/scp_irq.o
2026-05-03T01:31:08.2680817Z   AR      drivers/misc/mediatek/sensors-1.0/hwmon/sensor_event/built-in.a
2026-05-03T01:31:08.2740142Z   CC      drivers/misc/mediatek/scp/cm4/./v01/scp_logger.o
2026-05-03T01:31:08.2801354Z   CC      drivers/misc/mediatek/sensors-1.0/hwmon/sensor_list/sensor_list.o
2026-05-03T01:31:08.3370789Z   CC      drivers/misc/mediatek/sensors-1.0/magnetometer/mag_factory.o
2026-05-03T01:31:08.4530889Z   AR      drivers/misc/mediatek/sensors-1.0/sensorHub/SCP_nanoHub/built-in.a
2026-05-03T01:31:08.4781798Z   CC      drivers/misc/mediatek/sensors-1.0/sensorHub/SCP_power_monitor/SCP_power_monitor.o
2026-05-03T01:31:08.7250753Z   AR      drivers/misc/mediatek/sensors-1.0/hwmon/sensor_list/built-in.a
2026-05-03T01:31:08.7420863Z   CC      drivers/misc/mediatek/sensors-1.0/hwmon/sensor_performance/sensor_performance.o
2026-05-03T01:31:08.7660764Z   CC      drivers/misc/mediatek/scp/cm4/./v01/scp_l1c.o
2026-05-03T01:31:08.7926503Z   AR      drivers/misc/mediatek/sensors-1.0/sensorHub/SCP_power_monitor/built-in.a
2026-05-03T01:31:08.8135741Z   CC      drivers/misc/mediatek/sensors-1.0/sensorHub/nanohub/main.o
2026-05-03T01:31:08.8250418Z   AR      drivers/misc/mediatek/sensors-1.0/magnetometer/built-in.a
2026-05-03T01:31:08.8515717Z   CC      drivers/misc/mediatek/sspm/v1/sspm_emi_mpu.o
2026-05-03T01:31:09.0886050Z drivers/misc/mediatek/sensors-1.0/hwmon/sensor_performance/.tmp_sensor_performance.o: no symbols
2026-05-03T01:31:09.0954518Z   AR      drivers/misc/mediatek/sensors-1.0/hwmon/sensor_performance/built-in.a
2026-05-03T01:31:09.1018760Z   CC      drivers/misc/mediatek/scp/cm4/./v01/scp_scpctl.o
2026-05-03T01:31:09.1094981Z   AR      drivers/misc/mediatek/sensors-1.0/hwmon/built-in.a
2026-05-03T01:31:09.1200389Z   CC      drivers/misc/mediatek/sspm/v1/sspm_ipi_timeout_cb.o
2026-05-03T01:31:09.3310737Z   AR      drivers/misc/mediatek/subpmic/built-in.a
2026-05-03T01:31:09.3430655Z   CC      drivers/misc/mediatek/sensors-1.0/sensorHub/nanohub/bl.o
2026-05-03T01:31:09.4008880Z   AR      drivers/misc/mediatek/scp/cm4/built-in.a
2026-05-03T01:31:09.4188273Z   AR      drivers/misc/mediatek/scp/built-in.a
2026-05-03T01:31:09.4410851Z   CC      drivers/misc/mediatek/sync/mtk_sync.o
2026-05-03T01:31:09.4570612Z   CC      drivers/misc/mediatek/sensors-1.0/sensorHub/nanohub/comms.o
2026-05-03T01:31:09.5681294Z   CC      drivers/misc/mediatek/sspm/v1/sspm_helper.o
2026-05-03T01:31:09.8640654Z   AR      drivers/misc/mediatek/sync/built-in.a
2026-05-03T01:31:09.8820688Z   CC      drivers/misc/mediatek/systracker/systracker_interface_v2.o
2026-05-03T01:31:09.8950967Z   CC      drivers/misc/mediatek/sensors-1.0/sensorHub/nanohub/nanohub-mtk.o
2026-05-03T01:31:10.0851072Z   CC      drivers/misc/mediatek/sensors-1.0/sensorfusion/uncali_acchub/uncali_acchub.o
2026-05-03T01:31:10.4570730Z   AR      drivers/misc/mediatek/sensors-1.0/sensorHub/nanohub/built-in.a
2026-05-03T01:31:10.4592451Z   AR      drivers/misc/mediatek/systracker/built-in.a
2026-05-03T01:31:10.4676607Z   CC      drivers/misc/mediatek/sspm/v1/sspm_irq.o
2026-05-03T01:31:10.4712900Z   AR      drivers/misc/mediatek/sensors-1.0/sensorHub/built-in.a
2026-05-03T01:31:10.4874376Z   AR      drivers/misc/mediatek/sensors-1.0/sensorfusion/uncali_acchub/built-in.a
2026-05-03T01:31:10.4910839Z   CC      drivers/misc/mediatek/sensors-1.0/situation/device_orientation/device_orientation.o
2026-05-03T01:31:10.4937249Z   CC      drivers/misc/mediatek/sensors-1.0/step_counter/stepsignhub/stepsignhub.o
2026-05-03T01:31:10.5090834Z   CC      drivers/misc/mediatek/sensors-1.0/sensorfusion/uncali_maghub/uncali_maghub.o
2026-05-03T01:31:10.9400589Z   CC      drivers/misc/mediatek/sspm/v1/sspm_sysfs.o
2026-05-03T01:31:10.9804368Z   AR      drivers/misc/mediatek/sensors-1.0/sensorfusion/uncali_maghub/built-in.a
2026-05-03T01:31:10.9860519Z   AR      drivers/misc/mediatek/sensors-1.0/situation/device_orientation/built-in.a
2026-05-03T01:31:10.9886450Z   CC      drivers/misc/mediatek/sensors-1.0/sensorfusion/fusion.o
2026-05-03T01:31:10.9920936Z   AR      drivers/misc/mediatek/sensors-1.0/step_counter/stepsignhub/built-in.a
2026-05-03T01:31:10.9992468Z   CC      drivers/misc/mediatek/sensors-1.0/situation/glance_gesture/glance_gesture.o
2026-05-03T01:31:11.0020280Z   CC      drivers/misc/mediatek/sensors-1.0/step_counter/step_counter.o
2026-05-03T01:31:11.4450828Z   CC      drivers/misc/mediatek/sspm/v1/sspm_reservedmem.o
2026-05-03T01:31:11.5020847Z   AR      drivers/misc/mediatek/sensors-1.0/situation/glance_gesture/built-in.a
2026-05-03T01:31:11.5231401Z   CC      drivers/misc/mediatek/sensors-1.0/situation/motion_detect/motion_detect.o
2026-05-03T01:31:11.5698076Z   AR      drivers/misc/mediatek/sensors-1.0/sensorfusion/built-in.a
2026-05-03T01:31:11.5900149Z   CC      drivers/misc/mediatek/sensors-1.0/situation/pickup_gesture/pickup_gesture.o
2026-05-03T01:31:11.6230204Z   AR      drivers/misc/mediatek/sensors-1.0/step_counter/built-in.a
2026-05-03T01:31:11.6440487Z   CC      drivers/misc/mediatek/task_turbo/task_turbo.o
2026-05-03T01:31:11.9993333Z   AR      drivers/misc/mediatek/sensors-1.0/situation/motion_detect/built-in.a
2026-05-03T01:31:12.0100619Z   CC      drivers/misc/mediatek/sspm/v1/sspm_plt.o
2026-05-03T01:31:12.0718913Z   AR      drivers/misc/mediatek/sensors-1.0/situation/pickup_gesture/built-in.a
2026-05-03T01:31:12.0930697Z   CC      drivers/misc/mediatek/sensors-1.0/situation/sar/sarhub.o
2026-05-03T01:31:12.3580851Z   CC      drivers/misc/mediatek/tee_sanity/tee_sanity.o
2026-05-03T01:31:12.3930610Z In file included from ../drivers/misc/mediatek/task_turbo/task_turbo.c:13:
2026-05-03T01:31:12.3931830Z ../drivers/misc/mediatek/task_turbo/task_turbo.h:16:8: warning: type specifier missing, defaults to 'int' [-Wimplicit-int]
2026-05-03T01:31:12.3960175Z extern sched_set_cpuprefer(pid_t pid, unsigned int prefer_type);
2026-05-03T01:31:12.3960734Z ~~~~~~ ^
2026-05-03T01:31:12.3960989Z int
2026-05-03T01:31:12.5760697Z   CC      drivers/misc/mediatek/sensors-1.0/situation/sar/sar_factory.o
2026-05-03T01:31:12.6046030Z   CC      drivers/misc/mediatek/sspm/v1/sspm_mbox.o
2026-05-03T01:31:12.6180392Z 1 warning generated.
2026-05-03T01:31:13.0616343Z   AR      drivers/misc/mediatek/sensors-1.0/situation/sar/built-in.a
2026-05-03T01:31:13.0675687Z   AR      drivers/misc/mediatek/tee_sanity/built-in.a
2026-05-03T01:31:13.0687305Z   AR      drivers/misc/mediatek/task_turbo/built-in.a
2026-05-03T01:31:13.0788238Z   CC      drivers/misc/mediatek/sensors-1.0/situation/sar_algo/saralgo.o
2026-05-03T01:31:13.0789330Z   CC      drivers/misc/mediatek/sspm/v1/sspm_ipi_mbox.o
2026-05-03T01:31:13.0921890Z   CC      drivers/misc/mediatek/sensors-1.0/situation/sar_algo/saralgo_factory.o
2026-05-03T01:31:13.1030991Z   CC      drivers/misc/mediatek/thermal/common/coolers/mtk_ta.o
2026-05-03T01:31:13.6121816Z   AR      drivers/misc/mediatek/sensors-1.0/situation/sar_algo/built-in.a
2026-05-03T01:31:13.6294975Z   CC      drivers/misc/mediatek/sensors-1.0/situation/sar_algo_top/saralgo_top.o
2026-05-03T01:31:13.6484160Z   CC      drivers/misc/mediatek/thermal/mt6768/src/mtk_tc.o
2026-05-03T01:31:13.9361386Z   CC      drivers/misc/mediatek/sspm/v1/sspm_logger_impl.o
2026-05-03T01:31:14.0370714Z   CC      drivers/misc/mediatek/thermal/common/coolers/mtk_cooler_mutt.o
2026-05-03T01:31:14.0580847Z   AR      drivers/misc/mediatek/sensors-1.0/situation/sar_algo_top/built-in.a
2026-05-03T01:31:14.0769632Z   CC      drivers/misc/mediatek/sensors-1.0/situation/stationary/stationary.o
2026-05-03T01:31:14.5540810Z   CC      drivers/misc/mediatek/sspm/v1/sspm_timesync.o
2026-05-03T01:31:14.5680637Z   AR      drivers/misc/mediatek/sensors-1.0/situation/stationary/built-in.a
2026-05-03T01:31:14.5860573Z   CC      drivers/misc/mediatek/sensors-1.0/situation/tilt_detector/tiltdetecthub.o
2026-05-03T01:31:14.6270572Z   CC      drivers/misc/mediatek/thermal/mt6768/src/mtk_pmic_efuse.o
2026-05-03T01:31:14.7460715Z   CC      drivers/misc/mediatek/thermal/common/coolers/mtk_cooler_bcct_v2.o
2026-05-03T01:31:15.0384104Z   AR      drivers/misc/mediatek/sensors-1.0/situation/tilt_detector/built-in.a
2026-05-03T01:31:15.0590824Z   CC      drivers/misc/mediatek/sensors-1.0/situation/wake_gesture/wake_gesture.o
2026-05-03T01:31:15.1270663Z   AR      drivers/misc/mediatek/sspm/v1/built-in.a
2026-05-03T01:31:15.1431755Z   AR      drivers/misc/mediatek/sspm/built-in.a
2026-05-03T01:31:15.1690654Z   CC      drivers/misc/mediatek/timer/timesync/archcounter_timesync.o
2026-05-03T01:31:15.2195345Z   CC      drivers/misc/mediatek/thermal/mt6768/src/mtk_ts_6358buck1.o
2026-05-03T01:31:15.5286472Z   AR      drivers/misc/mediatek/sensors-1.0/situation/wake_gesture/built-in.a
2026-05-03T01:31:15.5369990Z   CC      drivers/misc/mediatek/sensors-1.0/situation/situation.o
2026-05-03T01:31:15.6245255Z   AR      drivers/misc/mediatek/timer/timesync/built-in.a
2026-05-03T01:31:15.6370394Z   AR      drivers/misc/mediatek/timer/built-in.a
2026-05-03T01:31:15.6640892Z   CC      drivers/misc/mediatek/thermal/common/thermal_zones/mtk_ts_battery.o
2026-05-03T01:31:15.8040648Z   CC      drivers/misc/mediatek/thermal/common/coolers/mtk_cooler_atm.o
2026-05-03T01:31:15.8330428Z   CC      drivers/misc/mediatek/thermal/mt6768/src/mtk_ts_6358buck2.o
2026-05-03T01:31:16.3220802Z   CC      drivers/misc/mediatek/thermal/common/thermal_zones/mtk_ts_firecpu.o
2026-05-03T01:31:16.3430679Z   AR      drivers/misc/mediatek/sensors-1.0/situation/built-in.a
2026-05-03T01:31:16.3680445Z   AR      drivers/misc/mediatek/sensors-1.0/built-in.a
2026-05-03T01:31:16.3910485Z   CC      drivers/misc/mediatek/thermal/mtk_thermal_monitor.o
2026-05-03T01:31:16.4870610Z   CC      drivers/misc/mediatek/thermal/mt6768/src/mtk_ts_6358buck3.o
2026-05-03T01:31:16.9499082Z   CC      drivers/misc/mediatek/thermal/common/coolers/mtk_cooler_dtm.o
2026-05-03T01:31:17.0340897Z   CC      drivers/misc/mediatek/thermal/common/thermal_zones/mtk_ts_bts.o
2026-05-03T01:31:17.0400505Z   CC      drivers/misc/mediatek/thermal/mt6768/src/mtk_thermal_ipi.o
2026-05-03T01:31:17.4750889Z   CC      drivers/misc/mediatek/thermal/common/coolers/mtk_cooler_sysrst.o
2026-05-03T01:31:17.4800360Z   CC      drivers/misc/mediatek/thermal/common/mtk_thermal_platform.o
2026-05-03T01:31:17.5273431Z drivers/misc/mediatek/thermal/mt6768/src/.tmp_mtk_thermal_ipi.o: no symbols
2026-05-03T01:31:17.5327444Z   AR      drivers/misc/mediatek/thermal/mt6768/src/built-in.a
2026-05-03T01:31:17.5490230Z   AR      drivers/misc/mediatek/thermal/mt6768/built-in.a
2026-05-03T01:31:17.5610106Z TCORE_UT_TESTS_SUPPORT = n
2026-05-03T01:31:17.5639932Z TCORE_PROFILING_SUPPORT = n
2026-05-03T01:31:17.5669922Z TCORE_PROFILING_AUTO_DUMP = n
2026-05-03T01:31:17.5699968Z TCORE_MEMORY_LEAK_DETECTION_SUPPORT = n
2026-05-03T01:31:17.5730028Z   CC      drivers/misc/mediatek/trusted_mem/ssmr/memory_ssmr.o
2026-05-03T01:31:17.7430618Z   CC      drivers/misc/mediatek/thermal/common/thermal_zones/mtk_ts_btsmdpa.o
2026-05-03T01:31:18.0180737Z   CC      drivers/misc/mediatek/thermal/common/coolers/mtk_cooler_VR_FPS.o
2026-05-03T01:31:18.4160820Z   CC      drivers/misc/mediatek/thermal/common/thermal_zones/mtk_ts_btscharger.o
2026-05-03T01:31:18.4700563Z   CC      drivers/misc/mediatek/trusted_mem/dev_mgr.o
2026-05-03T01:31:18.4710563Z   CC      drivers/misc/mediatek/thermal/common/coolers/mtk_cooler_mutt_gen97.o
2026-05-03T01:31:18.4819717Z   CC      drivers/misc/mediatek/typec/switch/mux_switch.o
2026-05-03T01:31:18.9047754Z   CC      drivers/misc/mediatek/trusted_mem/entry.o
2026-05-03T01:31:19.0643168Z   CC      drivers/misc/mediatek/thermal/common/thermal_zones/mtk_ts_cpu_noBank.o
2026-05-03T01:31:19.1680472Z   CC      drivers/misc/mediatek/typec/switch/fusb304.o
2026-05-03T01:31:19.2910814Z   CC      drivers/misc/mediatek/thermal/common/coolers/mtk_cooler_gpu_cus.o
2026-05-03T01:31:19.4430743Z   CC      drivers/misc/mediatek/trusted_mem/region_mgr.o
2026-05-03T01:31:19.6220683Z   CC      drivers/misc/mediatek/typec/switch/ptn36241g.o
2026-05-03T01:31:19.7120423Z   CC      drivers/misc/mediatek/trusted_mem/ssmr_mgr.o
2026-05-03T01:31:19.8150829Z   CC      drivers/misc/mediatek/thermal/common/coolers/mtk_cooler_char_curr_cus.o
2026-05-03T01:31:20.0510490Z   CC      drivers/misc/mediatek/trusted_mem/peer_mgr.o
2026-05-03T01:31:20.0838596Z   CC      drivers/misc/mediatek/typec/switch/ps5169.o
2026-05-03T01:31:20.0980600Z   CC      drivers/misc/mediatek/thermal/common/thermal_zones/mtk_ts_pa.o
2026-05-03T01:31:20.2239323Z   CC      drivers/misc/mediatek/thermal/common/coolers/mtk_cooler_md_cus.o
2026-05-03T01:31:20.4700706Z   CC      drivers/misc/mediatek/trusted_mem/proc.o
2026-05-03T01:31:20.5500663Z   AR      drivers/misc/mediatek/typec/switch/built-in.a
2026-05-03T01:31:20.5990922Z   CC      drivers/misc/mediatek/typec/tcpc/tcpc_rt1711h.o
2026-05-03T01:31:20.7750751Z   AR      drivers/misc/mediatek/thermal/common/coolers/built-in.a
2026-05-03T01:31:20.7900734Z   CC      drivers/misc/mediatek/thermal/mtk_cooler_shutdown.o
2026-05-03T01:31:20.9592178Z   CC      drivers/misc/mediatek/thermal/common/thermal_zones/mtk_ts_pa_thput.o
2026-05-03T01:31:20.9860688Z   CC      drivers/misc/mediatek/trusted_mem/alloc_api.o
2026-05-03T01:31:21.2690663Z   AR      drivers/misc/mediatek/usb20/mt6768/built-in.a
2026-05-03T01:31:21.2810471Z   CC      drivers/misc/mediatek/usb20/musb_core.o
2026-05-03T01:31:21.3280589Z   CC      drivers/misc/mediatek/typec/tcpc/tcpc_wusb3801.o
2026-05-03T01:31:21.5261005Z   CC      drivers/misc/mediatek/trusted_mem/mpu_vio_checker.o
2026-05-03T01:31:21.9310805Z   CC      drivers/misc/mediatek/thermal/common/thermal_zones/mtk_ts_wmt.o
2026-05-03T01:31:21.9372693Z   CC      drivers/misc/mediatek/trusted_mem/tee_devices.o
2026-05-03T01:31:21.9390271Z   CC      drivers/misc/mediatek/typec/tcpc/tcpc_husb320.o
2026-05-03T01:31:22.3561207Z   CC      drivers/misc/mediatek/trusted_mem/tee_impl/tee_invoke.o
2026-05-03T01:31:22.6400621Z   CC      drivers/misc/mediatek/typec/tcpc/tcpci_core.o
2026-05-03T01:31:22.6720509Z   CC      drivers/misc/mediatek/usb20/musb_virthub.o
2026-05-03T01:31:22.7490771Z   CC      drivers/misc/mediatek/trusted_mem/tee_impl/tee_ops.o
2026-05-03T01:31:22.7880802Z   CC      drivers/misc/mediatek/thermal/common/thermal_zones/mtk_tsAll.o
2026-05-03T01:31:23.1911764Z   CC      drivers/misc/mediatek/trusted_mem/mtee_devices.o
2026-05-03T01:31:23.4170536Z   CC      drivers/misc/mediatek/typec/tcpc/tcpci_typec.o
2026-05-03T01:31:23.5670737Z   CC      drivers/misc/mediatek/trusted_mem/mtee_impl/mtee_ops.o
2026-05-03T01:31:23.6177352Z   CC      drivers/misc/mediatek/usb20/musb_host.o
2026-05-03T01:31:23.8826043Z   CC      drivers/misc/mediatek/thermal/common/thermal_zones/mtk_ts_imgsensor.o
2026-05-03T01:31:24.0750730Z   CC      drivers/misc/mediatek/trusted_mem/mtee_impl/mtee_invoke.o
2026-05-03T01:31:24.1253913Z   CC      drivers/misc/mediatek/typec/tcpc/tcpci_timer.o
2026-05-03T01:31:24.4580646Z   AR      drivers/misc/mediatek/trusted_mem/built-in.a
2026-05-03T01:31:24.4730482Z   CC      drivers/misc/mediatek/thermal/common/thermal_zones/mtk_ts_dctm.o
2026-05-03T01:31:24.6970461Z   CC      drivers/misc/mediatek/typec/tcpc/tcpm.o
2026-05-03T01:31:24.7782610Z   CC      drivers/misc/mediatek/usb20/musb_gadget_ep0.o
2026-05-03T01:31:25.0419677Z   CC      drivers/misc/mediatek/thermal/mtk_cooler_backlight_cus.o
2026-05-03T01:31:25.2370688Z   CC      drivers/misc/mediatek/thermal/common/thermal_zones/mtk_ts_pmic.o
2026-05-03T01:31:25.3320770Z   CC      drivers/misc/mediatek/typec/tcpc/tcpci.o
2026-05-03T01:31:25.3760762Z   CC      drivers/misc/mediatek/thermal/common/ap_thermal_limit.o
2026-05-03T01:31:25.4923739Z   CC      drivers/misc/mediatek/usb20/musb_gadget.o
2026-05-03T01:31:25.8757398Z   AR      drivers/misc/mediatek/thermal/common/thermal_zones/built-in.a
2026-05-03T01:31:25.8769941Z   CC      drivers/misc/mediatek/typec/tcpc/pd_dbg_info.o
2026-05-03T01:31:25.8871446Z   CC      drivers/misc/mediatek/thermal/common/mtk_thermal_timer.o
2026-05-03T01:31:26.1498751Z   CC      drivers/misc/mediatek/usb_boost/v1/usb_boost_plat.o
2026-05-03T01:31:26.2260642Z   CC      drivers/misc/mediatek/typec/tcpc/tcpci_alert.o
2026-05-03T01:31:26.4088008Z   AR      drivers/misc/mediatek/thermal/common/built-in.a
2026-05-03T01:31:26.4260274Z   CC      drivers/misc/mediatek/thermal/mtk_cooler_kshutdown.o
2026-05-03T01:31:26.5550689Z   AR      drivers/misc/mediatek/usb_boost/v1/built-in.a
2026-05-03T01:31:26.5650328Z   CC      drivers/misc/mediatek/usb_boost/usb_boost.o
2026-05-03T01:31:26.7093603Z   CC      drivers/misc/mediatek/usb20/musb_debugfs.o
2026-05-03T01:31:26.7150342Z   CC      drivers/misc/mediatek/typec/tcpc/rt_pd_manager.o
2026-05-03T01:31:26.7620637Z   CC      drivers/misc/mediatek/thermal/mtk_cooler_cam.o
2026-05-03T01:31:26.9430469Z   AR      drivers/misc/mediatek/usb_boost/built-in.a
2026-05-03T01:31:26.9690775Z   CC      drivers/misc/mediatek/vibrator/mt6768/vibrator.o
2026-05-03T01:31:27.2290434Z   CC      drivers/misc/mediatek/typec/tcpc/tcpci_event.o
2026-05-03T01:31:27.3130537Z   CC      drivers/misc/mediatek/thermal/mtk_cooler_flashlight_cus.o
2026-05-03T01:31:27.3580474Z   AR      drivers/misc/mediatek/vibrator/mt6768/built-in.a
2026-05-03T01:31:27.3670364Z   CC      drivers/misc/mediatek/vibrator/vibrator_drv.o
2026-05-03T01:31:27.3950715Z   CC      drivers/misc/mediatek/usb20/musb_dr.o
2026-05-03T01:31:27.6450681Z   AR      drivers/misc/mediatek/thermal/built-in.a
2026-05-03T01:31:27.6810708Z   CC      drivers/misc/mediatek/video/common/aal30/ddp_aal.o
2026-05-03T01:31:27.7530482Z   AR      drivers/misc/mediatek/vibrator/built-in.a
2026-05-03T01:31:27.7830697Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_ovl.o
2026-05-03T01:31:27.8150665Z   CC      drivers/misc/mediatek/typec/tcpc/pd_core.o
2026-05-03T01:31:28.3027832Z   CC      drivers/misc/mediatek/usb20/mtk_qmu.o
2026-05-03T01:31:28.3920600Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine.o
2026-05-03T01:31:28.4281037Z ../drivers/misc/mediatek/video/mt6768/dispsys/ddp_ovl.c:654:29: warning: mixing declarations and code is a C99 extension [-Wdeclaration-after-statement]
2026-05-03T01:31:28.4309959Z                 enum TRUSTED_MEM_REQ_TYPE mem_type;
2026-05-03T01:31:28.4339911Z                                           ^
2026-05-03T01:31:28.6420179Z   AR      drivers/misc/mediatek/video/common/aal30/built-in.a
2026-05-03T01:31:28.6630487Z   CC      drivers/misc/mediatek/video/common/color20/ddp_color.o
2026-05-03T01:31:28.8926542Z   CC      drivers/misc/mediatek/typec/tcpc/pd_process_evt.o
2026-05-03T01:31:29.1887419Z 1 warning generated.
2026-05-03T01:31:29.2280565Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_rdma_ex.o
2026-05-03T01:31:29.4093351Z   CC      drivers/misc/mediatek/typec/tcpc/pd_dpm_core.o
2026-05-03T01:31:29.4681067Z   AR      drivers/misc/mediatek/video/common/color20/built-in.a
2026-05-03T01:31:29.4858740Z   CC      drivers/misc/mediatek/video/common/corr10/ddp_dither.o
2026-05-03T01:31:29.6040572Z   CC      drivers/misc/mediatek/usb20/musb_qmu.o
2026-05-03T01:31:30.1476174Z   CC      drivers/misc/mediatek/typec/tcpc/pd_dpm_uvdm.o
2026-05-03T01:31:30.1790816Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_wdma_ex.o
2026-05-03T01:31:30.2722045Z   CC      drivers/misc/mediatek/video/common/corr10/ddp_gamma.o
2026-05-03T01:31:30.5500680Z   CC      drivers/misc/mediatek/usb20/musbhsdma.o
2026-05-03T01:31:30.5850622Z drivers/misc/mediatek/typec/tcpc/.tmp_pd_dpm_uvdm.o: no symbols
2026-05-03T01:31:30.5910077Z   CC      drivers/misc/mediatek/typec/tcpc/pd_dpm_alt_mode_dp.o
2026-05-03T01:31:31.1250767Z   AR      drivers/misc/mediatek/video/common/corr10/built-in.a
2026-05-03T01:31:31.1456304Z   CC      drivers/misc/mediatek/video/common/layering_rule_base/v1.1/layering_rule_base.o
2026-05-03T01:31:31.1493213Z   CC      drivers/misc/mediatek/typec/tcpc/pd_dpm_pdo_select.o
2026-05-03T01:31:31.1982725Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_dsi.o
2026-05-03T01:31:31.4910999Z   CC      drivers/misc/mediatek/usb20/mt6768/usb20.o
2026-05-03T01:31:31.5490617Z   CC      drivers/misc/mediatek/typec/tcpc/pd_dpm_reaction.o
2026-05-03T01:31:32.0739906Z   CC      drivers/misc/mediatek/typec/tcpc/pd_process_evt_snk.o
2026-05-03T01:31:32.1810891Z   AR      drivers/misc/mediatek/video/common/layering_rule_base/v1.1/built-in.a
2026-05-03T01:31:32.1936513Z   AR      drivers/misc/mediatek/video/common/layering_rule_base/built-in.a
2026-05-03T01:31:32.2129032Z   CC      drivers/misc/mediatek/video/common/pwm10/ddp_pwm.o
2026-05-03T01:31:32.5730733Z   CC      drivers/misc/mediatek/typec/tcpc/pd_process_evt_src.o
2026-05-03T01:31:32.6590484Z   CC      drivers/misc/mediatek/usb20/mt6768/usb20_host.o
2026-05-03T01:31:32.9740693Z   AR      drivers/misc/mediatek/video/common/pwm10/built-in.a
2026-05-03T01:31:32.9890595Z   AR      drivers/misc/mediatek/video/common/built-in.a
2026-05-03T01:31:33.0040882Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_clkmgr.o
2026-05-03T01:31:33.0500471Z   CC      drivers/misc/mediatek/typec/tcpc/pd_process_evt_vdm.o
2026-05-03T01:31:33.5995082Z   CC      drivers/misc/mediatek/typec/tcpc/pd_process_evt_drs.o
2026-05-03T01:31:33.6394227Z   AR      drivers/misc/mediatek/usb20/built-in.a
2026-05-03T01:31:33.6620699Z   CC      drivers/misc/mediatek/typec/tcpc/pd_process_evt_prs.o
2026-05-03T01:31:33.6685283Z   CC      drivers/misc/mediatek/video/mt6768/videox/mtkfb_console.o
2026-05-03T01:31:33.9801971Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_assert_layer.o
2026-05-03T01:31:34.0580617Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_rsz.o
2026-05-03T01:31:34.1298506Z   CC      drivers/misc/mediatek/typec/tcpc/pd_process_evt_vcs.o
2026-05-03T01:31:34.5927694Z   CC      drivers/misc/mediatek/video/mt6768/videox/mtkfb.o
2026-05-03T01:31:34.6064529Z   CC      drivers/misc/mediatek/typec/tcpc/pd_process_evt_dbg.o
2026-05-03T01:31:34.7802899Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_drv.o
2026-05-03T01:31:34.8825646Z   CC      drivers/misc/mediatek/video/mt6768/videox/mtkfb_fence.o
2026-05-03T01:31:35.0243495Z drivers/misc/mediatek/typec/tcpc/.tmp_pd_process_evt_dbg.o: no symbols
2026-05-03T01:31:35.0320229Z   CC      drivers/misc/mediatek/typec/tcpc/pd_process_evt_tcp.o
2026-05-03T01:31:35.5140692Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_path.o
2026-05-03T01:31:35.5440790Z   CC      drivers/misc/mediatek/typec/tcpc/pd_process_evt_com.o
2026-05-03T01:31:35.7090991Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_mutex.o
2026-05-03T01:31:36.0616376Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_src.o
2026-05-03T01:31:36.0730524Z   CC      drivers/misc/mediatek/video/mt6768/videox/fbconfig_kdebug.o
2026-05-03T01:31:36.2990665Z   CC      drivers/misc/mediatek/video/mt6768/videox/mtkfb_vsync.o
2026-05-03T01:31:36.3720767Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_m4u.o
2026-05-03T01:31:36.5210157Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_snk.o
2026-05-03T01:31:36.9550901Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_debug.o
2026-05-03T01:31:37.0020797Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_ufp.o
2026-05-03T01:31:37.0380554Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_dump.o
2026-05-03T01:31:37.2600705Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_cust.o
2026-05-03T01:31:37.4770483Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_vcs.o
2026-05-03T01:31:37.7180460Z   CC      drivers/misc/mediatek/video/mt6768/videox/debug.o
2026-05-03T01:31:37.8350841Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_dfp.o
2026-05-03T01:31:37.9141053Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_manager.o
2026-05-03T01:31:37.9170152Z   CC      drivers/misc/mediatek/video/mt6768/videox/primary_display.o
2026-05-03T01:31:38.2900573Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_dr.o
2026-05-03T01:31:38.6860786Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_irq.o
2026-05-03T01:31:38.7221151Z ../drivers/misc/mediatek/video/mt6768/videox/primary_display.c:9026:23: warning: unused variable 'm4uClient' [-Wunused-variable]
2026-05-03T01:31:38.7250004Z         struct m4u_client_t *m4uClient = NULL;
2026-05-03T01:31:38.7279904Z                              ^
2026-05-03T01:31:38.7295739Z ../drivers/misc/mediatek/video/mt6768/videox/primary_display.c:9025:6: warning: unused variable 'tmp' [-Wunused-variable]
2026-05-03T01:31:38.7297028Z         int tmp;
2026-05-03T01:31:38.7297597Z             ^
2026-05-03T01:31:38.7298364Z ../drivers/misc/mediatek/video/mt6768/videox/primary_display.c:9027:15: warning: unused variable 'mva' [-Wunused-variable]
2026-05-03T01:31:38.7299578Z         unsigned int mva = 0;
2026-05-03T01:31:38.7300055Z                      ^
2026-05-03T01:31:38.7301343Z ../drivers/misc/mediatek/video/mt6768/videox/primary_display.c:9023:6: warning: unused variable 'buffer_size' [-Wunused-variable]
2026-05-03T01:31:38.7302440Z         int buffer_size = h_yres * w_xres * pixel_byte;
2026-05-03T01:31:38.7303040Z             ^
2026-05-03T01:31:38.7303950Z ../drivers/misc/mediatek/video/mt6768/videox/primary_display.c:9024:24: warning: unused variable 'after_eng' [-Wunused-variable]
2026-05-03T01:31:38.7305109Z         enum DISP_MODULE_ENUM after_eng = DISP_MODULE_OVL0;
2026-05-03T01:31:38.7305710Z                               ^
2026-05-03T01:31:38.7590690Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_drs.o
2026-05-03T01:31:38.7781434Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_lowpower.o
2026-05-03T01:31:39.2390583Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_prs.o
2026-05-03T01:31:39.4090739Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_info.o
2026-05-03T01:31:39.5640502Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_recovery.o
2026-05-03T01:31:39.6920747Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_dbg.o
2026-05-03T01:31:39.8980535Z 5 warnings generated.
2026-05-03T01:31:39.9440701Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_color_format.o
2026-05-03T01:31:40.0140733Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_com.o
2026-05-03T01:31:40.1280832Z drivers/misc/mediatek/typec/tcpc/.tmp_pd_policy_engine_dbg.o: no symbols
2026-05-03T01:31:40.1370258Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_pwm_mux.o
2026-05-03T01:31:40.2930768Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_lcm.o
2026-05-03T01:31:40.4920554Z   CC      drivers/misc/mediatek/typec/tcpc/pd_dpm_alt_mode_dc.o
2026-05-03T01:31:40.5130509Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_utils.o
2026-05-03T01:31:40.7700789Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_disp_bdg.o
2026-05-03T01:31:41.0022945Z   AR      drivers/misc/mediatek/typec/tcpc/built-in.a
2026-05-03T01:31:41.0198403Z   AR      drivers/misc/mediatek/typec/built-in.a
2026-05-03T01:31:41.0270467Z   CC      drivers/misc/mediatek/video/mt6768/videox/mtk_disp_mgr.o
2026-05-03T01:31:41.0348630Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_mmp.o
2026-05-03T01:31:41.0820896Z   CC      drivers/misc/mediatek/video/mt6768/videox/compat_mtk_disp_mgr.o
2026-05-03T01:31:41.6680622Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_helper.o
2026-05-03T01:31:41.8930517Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_met.o
2026-05-03T01:31:42.2611033Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_dts_gpio.o
2026-05-03T01:31:42.2700528Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/display_recorder.o
2026-05-03T01:31:42.7740652Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_rect.o
2026-05-03T01:31:42.8169788Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_arr.o
2026-05-03T01:31:43.0230722Z   AR      drivers/misc/mediatek/video/mt6768/dispsys/built-in.a
2026-05-03T01:31:43.0380639Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_partial.o
2026-05-03T01:31:43.3520491Z   CC      drivers/misc/mediatek/video/mt6768/videox/mtk_ovl.o
2026-05-03T01:31:43.4150718Z   CC      drivers/misc/mediatek/video/mt6768/videox/layering_rule.o
2026-05-03T01:31:43.6390017Z   CC      drivers/misc/mediatek/video/mt6768/videox/frame_queue.o
2026-05-03T01:31:44.1636961Z   AR      drivers/misc/mediatek/video/mt6768/videox/built-in.a
2026-05-03T01:31:44.1730499Z   AR      drivers/misc/mediatek/video/mt6768/built-in.a
2026-05-03T01:31:44.1827386Z   AR      drivers/misc/mediatek/video/built-in.a
2026-05-03T01:31:44.1936636Z   AR      drivers/misc/mediatek/built-in.a
2026-05-03T01:31:44.2763505Z   AR      drivers/misc/built-in.a
2026-05-03T01:31:44.3096994Z   AR      drivers/built-in.a
2026-05-03T01:31:44.4292497Z   GEN     .version
2026-05-03T01:31:44.4559551Z   CHK     include/generated/compile.h
2026-05-03T01:31:44.4931393Z   AR      built-in.a
2026-05-03T01:31:47.5901554Z   LTO     vmlinux.o
2026-05-03T01:35:31.3660031Z   MODPOST vmlinux.o
2026-05-03T01:35:33.9017424Z ld.lld: error: undefined symbol: ksu_handle_slow_avc_audit_new
2026-05-03T01:35:33.9018590Z >>> referenced by avc.c:792 (/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/out/../security/selinux/avc.c:792)
2026-05-03T01:35:33.9019925Z >>>               vmlinux.o:(slow_avc_audit)
2026-05-03T01:35:34.3378506Z make[1]: *** [/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/Makefile:1160: vmlinux] Error 1
2026-05-03T01:35:34.3379284Z make[1]: Leaving directory '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/out'
2026-05-03T01:35:34.3383013Z make: *** [Makefile:146: sub-make] Error 2
2026-05-03T01:35:34.3388240Z BUILD FAILED! Image.gz-dtb not found
2026-05-03T01:35:34.3400702Z   CC      drivers/misc/mediatek/usb20/mt6768/usb20_host.o
2026-05-03T01:35:34.3401263Z   AR      drivers/misc/mediatek/video/common/pwm10/built-in.a
2026-05-03T01:35:34.3401782Z   AR      drivers/misc/mediatek/video/common/built-in.a
2026-05-03T01:35:34.3402158Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_clkmgr.o
2026-05-03T01:35:34.3402534Z   CC      drivers/misc/mediatek/typec/tcpc/pd_process_evt_vdm.o
2026-05-03T01:35:34.3402884Z   CC      drivers/misc/mediatek/typec/tcpc/pd_process_evt_drs.o
2026-05-03T01:35:34.3403198Z   AR      drivers/misc/mediatek/usb20/built-in.a
2026-05-03T01:35:34.3403521Z   CC      drivers/misc/mediatek/typec/tcpc/pd_process_evt_prs.o
2026-05-03T01:35:34.3404084Z   CC      drivers/misc/mediatek/video/mt6768/videox/mtkfb_console.o
2026-05-03T01:35:34.3404755Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_assert_layer.o
2026-05-03T01:35:34.3405327Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_rsz.o
2026-05-03T01:35:34.3405880Z   CC      drivers/misc/mediatek/typec/tcpc/pd_process_evt_vcs.o
2026-05-03T01:35:34.3406375Z   CC      drivers/misc/mediatek/video/mt6768/videox/mtkfb.o
2026-05-03T01:35:34.3406710Z   CC      drivers/misc/mediatek/typec/tcpc/pd_process_evt_dbg.o
2026-05-03T01:35:34.3407055Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_drv.o
2026-05-03T01:35:34.3407408Z   CC      drivers/misc/mediatek/video/mt6768/videox/mtkfb_fence.o
2026-05-03T01:35:34.3407808Z drivers/misc/mediatek/typec/tcpc/.tmp_pd_process_evt_dbg.o: no symbols
2026-05-03T01:35:34.3408207Z   CC      drivers/misc/mediatek/typec/tcpc/pd_process_evt_tcp.o
2026-05-03T01:35:34.3408544Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_path.o
2026-05-03T01:35:34.3408886Z   CC      drivers/misc/mediatek/typec/tcpc/pd_process_evt_com.o
2026-05-03T01:35:34.3409226Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_mutex.o
2026-05-03T01:35:34.3410300Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_src.o
2026-05-03T01:35:34.3410680Z   CC      drivers/misc/mediatek/video/mt6768/videox/fbconfig_kdebug.o
2026-05-03T01:35:34.3411043Z   CC      drivers/misc/mediatek/video/mt6768/videox/mtkfb_vsync.o
2026-05-03T01:35:34.3411382Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_m4u.o
2026-05-03T01:35:34.3411726Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_snk.o
2026-05-03T01:35:34.3412075Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_debug.o
2026-05-03T01:35:34.3412421Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_ufp.o
2026-05-03T01:35:34.3412757Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_dump.o
2026-05-03T01:35:34.3413095Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_cust.o
2026-05-03T01:35:34.3413673Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_vcs.o
2026-05-03T01:35:34.3414016Z   CC      drivers/misc/mediatek/video/mt6768/videox/debug.o
2026-05-03T01:35:34.3414345Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_dfp.o
2026-05-03T01:35:34.3414701Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_manager.o
2026-05-03T01:35:34.3415079Z   CC      drivers/misc/mediatek/video/mt6768/videox/primary_display.o
2026-05-03T01:35:34.3415450Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_dr.o
2026-05-03T01:35:34.3415943Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_irq.o
2026-05-03T01:35:34.3416528Z ../drivers/misc/mediatek/video/mt6768/videox/primary_display.c:9026:23: warning: unused variable 'm4uClient' [-Wunused-variable]
2026-05-03T01:35:34.3417073Z         struct m4u_client_t *m4uClient = NULL;
2026-05-03T01:35:34.3417330Z                              ^
2026-05-03T01:35:34.3417806Z ../drivers/misc/mediatek/video/mt6768/videox/primary_display.c:9025:6: warning: unused variable 'tmp' [-Wunused-variable]
2026-05-03T01:35:34.3418323Z         int tmp;
2026-05-03T01:35:34.3418505Z             ^
2026-05-03T01:35:34.3418965Z ../drivers/misc/mediatek/video/mt6768/videox/primary_display.c:9027:15: warning: unused variable 'mva' [-Wunused-variable]
2026-05-03T01:35:34.3419688Z         unsigned int mva = 0;
2026-05-03T01:35:34.3419915Z                      ^
2026-05-03T01:35:34.3420396Z ../drivers/misc/mediatek/video/mt6768/videox/primary_display.c:9023:6: warning: unused variable 'buffer_size' [-Wunused-variable]
2026-05-03T01:35:34.3420959Z         int buffer_size = h_yres * w_xres * pixel_byte;
2026-05-03T01:35:34.3421234Z             ^
2026-05-03T01:35:34.3421673Z ../drivers/misc/mediatek/video/mt6768/videox/primary_display.c:9024:24: warning: unused variable 'after_eng' [-Wunused-variable]
2026-05-03T01:35:34.3422241Z         enum DISP_MODULE_ENUM after_eng = DISP_MODULE_OVL0;
2026-05-03T01:35:34.3422525Z                               ^
2026-05-03T01:35:34.3422820Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_drs.o
2026-05-03T01:35:34.3423200Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_lowpower.o
2026-05-03T01:35:34.3423567Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_prs.o
2026-05-03T01:35:34.3423916Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_info.o
2026-05-03T01:35:34.3424268Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_recovery.o
2026-05-03T01:35:34.3424626Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_dbg.o
2026-05-03T01:35:34.3424917Z 5 warnings generated.
2026-05-03T01:35:34.3425203Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_color_format.o
2026-05-03T01:35:34.3425575Z   CC      drivers/misc/mediatek/typec/tcpc/pd_policy_engine_com.o
2026-05-03T01:35:34.3425973Z drivers/misc/mediatek/typec/tcpc/.tmp_pd_policy_engine_dbg.o: no symbols
2026-05-03T01:35:34.3426380Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_pwm_mux.o
2026-05-03T01:35:34.3426733Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_lcm.o
2026-05-03T01:35:34.3427078Z   CC      drivers/misc/mediatek/typec/tcpc/pd_dpm_alt_mode_dc.o
2026-05-03T01:35:34.3427423Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_utils.o
2026-05-03T01:35:34.3427781Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_disp_bdg.o
2026-05-03T01:35:34.3428111Z   AR      drivers/misc/mediatek/typec/tcpc/built-in.a
2026-05-03T01:35:34.3428416Z   AR      drivers/misc/mediatek/typec/built-in.a
2026-05-03T01:35:34.3428743Z   CC      drivers/misc/mediatek/video/mt6768/videox/mtk_disp_mgr.o
2026-05-03T01:35:34.3429100Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_mmp.o
2026-05-03T01:35:34.3429659Z   CC      drivers/misc/mediatek/video/mt6768/videox/compat_mtk_disp_mgr.o
2026-05-03T01:35:34.3430075Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_helper.o
2026-05-03T01:35:34.3430425Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/ddp_met.o
2026-05-03T01:35:34.3430938Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_dts_gpio.o
2026-05-03T01:35:34.3431338Z   CC      drivers/misc/mediatek/video/mt6768/dispsys/display_recorder.o
2026-05-03T01:35:34.3431715Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_rect.o
2026-05-03T01:35:34.3432065Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_arr.o
2026-05-03T01:35:34.3432407Z   AR      drivers/misc/mediatek/video/mt6768/dispsys/built-in.a
2026-05-03T01:35:34.3432757Z   CC      drivers/misc/mediatek/video/mt6768/videox/disp_partial.o
2026-05-03T01:35:34.3433228Z   CC      drivers/misc/mediatek/video/mt6768/videox/mtk_ovl.o
2026-05-03T01:35:34.3433596Z   CC      drivers/misc/mediatek/video/mt6768/videox/layering_rule.o
2026-05-03T01:35:34.3433969Z   CC      drivers/misc/mediatek/video/mt6768/videox/frame_queue.o
2026-05-03T01:35:34.3434317Z   AR      drivers/misc/mediatek/video/mt6768/videox/built-in.a
2026-05-03T01:35:34.3434647Z   AR      drivers/misc/mediatek/video/mt6768/built-in.a
2026-05-03T01:35:34.3434950Z   AR      drivers/misc/mediatek/video/built-in.a
2026-05-03T01:35:34.3435233Z   AR      drivers/misc/mediatek/built-in.a
2026-05-03T01:35:34.3435492Z   AR      drivers/misc/built-in.a
2026-05-03T01:35:34.3435725Z   AR      drivers/built-in.a
2026-05-03T01:35:34.3435935Z   GEN     .version
2026-05-03T01:35:34.3436141Z   CHK     include/generated/compile.h
2026-05-03T01:35:34.3436379Z   AR      built-in.a
2026-05-03T01:35:34.3436566Z   LTO     vmlinux.o
2026-05-03T01:35:34.3436763Z   MODPOST vmlinux.o
2026-05-03T01:35:34.3437016Z ld.lld: error: undefined symbol: ksu_handle_slow_avc_audit_new
2026-05-03T01:35:34.3437613Z >>> referenced by avc.c:792 (/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/out/../security/selinux/avc.c:792)
2026-05-03T01:35:34.3438143Z >>>               vmlinux.o:(slow_avc_audit)
2026-05-03T01:35:34.3438610Z make[1]: *** [/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/Makefile:1160: vmlinux] Error 1
2026-05-03T01:35:34.3439239Z make[1]: Leaving directory '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/out'
2026-05-03T01:35:34.3440203Z make: *** [Makefile:146: sub-make] Error 2
2026-05-03T01:35:34.3453010Z ##[error]Process completed with exit code 1.
2026-05-03T01:35:34.3557728Z Post job cleanup.
2026-05-03T01:35:34.4392176Z [command]/usr/bin/git version
2026-05-03T01:35:34.4429883Z git version 2.53.0
2026-05-03T01:35:34.4464261Z Temporarily overriding HOME='/home/runner/work/_temp/bda60066-7ecc-4dcb-b158-1d31fade75b7' before making global git config changes
2026-05-03T01:35:34.4465173Z Adding repository directory to the temporary git global config as a safe directory
2026-05-03T01:35:34.4469974Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN
2026-05-03T01:35:34.4507083Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-05-03T01:35:34.4539852Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-05-03T01:35:34.4762557Z fatal: No url found for submodule path 'temp_susfs' in .gitmodules
2026-05-03T01:35:34.4829300Z ##[warning]The process '/usr/bin/git' failed with exit code 128
2026-05-03T01:35:34.4956335Z Cleaning up orphan processes
2026-05-03T01:35:34.5242603Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
