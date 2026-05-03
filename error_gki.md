2026-05-03T00:38:23.6007622Z Current runner version: '2.334.0'
2026-05-03T00:38:23.6032925Z ##[group]Runner Image Provisioner
2026-05-03T00:38:23.6033853Z Hosted Compute Agent
2026-05-03T00:38:23.6034427Z Version: 20260213.493
2026-05-03T00:38:23.6035201Z Commit: 5c115507f6dd24b8de37d8bbe0bb4509d0cc0fa3
2026-05-03T00:38:23.6036009Z Build Date: 2026-02-13T00:28:41Z
2026-05-03T00:38:23.6036696Z Worker ID: {130795ca-ed1c-443b-ac1d-8b64a51af948}
2026-05-03T00:38:23.6037493Z Azure Region: eastus
2026-05-03T00:38:23.6038080Z ##[endgroup]
2026-05-03T00:38:23.6040111Z ##[group]Operating System
2026-05-03T00:38:23.6040862Z Ubuntu
2026-05-03T00:38:23.6041481Z 24.04.4
2026-05-03T00:38:23.6041976Z LTS
2026-05-03T00:38:23.6042540Z ##[endgroup]
2026-05-03T00:38:23.6043129Z ##[group]Runner Image
2026-05-03T00:38:23.6043756Z Image: ubuntu-24.04
2026-05-03T00:38:23.6044380Z Version: 20260413.86.1
2026-05-03T00:38:23.6045669Z Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20260413.86/images/ubuntu/Ubuntu2404-Readme.md
2026-05-03T00:38:23.6047178Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20260413.86
2026-05-03T00:38:23.6048143Z ##[endgroup]
2026-05-03T00:38:23.6049383Z ##[group]GITHUB_TOKEN Permissions
2026-05-03T00:38:23.6051977Z Contents: write
2026-05-03T00:38:23.6052587Z Metadata: read
2026-05-03T00:38:23.6053201Z ##[endgroup]
2026-05-03T00:38:23.6055404Z Secret source: Actions
2026-05-03T00:38:23.6056448Z Prepare workflow directory
2026-05-03T00:38:23.6452109Z Prepare all required actions
2026-05-03T00:38:23.6489352Z Getting action download info
2026-05-03T00:38:23.9652002Z Download action repository 'actions/checkout@v4' (SHA:34e114876b0b11c390a56381ad16ebd13914f8d5)
2026-05-03T00:38:24.1005629Z Download action repository 'actions/upload-artifact@v4' (SHA:ea165f8d65b6e75b540449e92b4886f43607fa02)
2026-05-03T00:38:24.2071260Z Download action repository 'softprops/action-gh-release@v2' (SHA:3bb12739c298aeb8a4eeaf626c5b8d85266b0e65)
2026-05-03T00:38:24.5193958Z Complete job name: Castorice GKI 6.6
2026-05-03T00:38:24.5977593Z ##[group]Run actions/checkout@v4
2026-05-03T00:38:24.5978422Z with:
2026-05-03T00:38:24.5979315Z   repository: naidrahiqa/CastoriceKernelSUN
2026-05-03T00:38:24.5980015Z   token: ***
2026-05-03T00:38:24.5980376Z   ssh-strict: true
2026-05-03T00:38:24.5980793Z   ssh-user: git
2026-05-03T00:38:24.5981204Z   persist-credentials: true
2026-05-03T00:38:24.5981640Z   clean: true
2026-05-03T00:38:24.5982023Z   sparse-checkout-cone-mode: true
2026-05-03T00:38:24.5982535Z   fetch-depth: 1
2026-05-03T00:38:24.5982899Z   fetch-tags: false
2026-05-03T00:38:24.5983282Z   show-progress: true
2026-05-03T00:38:24.5983662Z   lfs: false
2026-05-03T00:38:24.5984005Z   submodules: false
2026-05-03T00:38:24.5984390Z   set-safe-directory: true
2026-05-03T00:38:24.5985136Z env:
2026-05-03T00:38:24.5985531Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:38:24.5986048Z   ANDROID_VERSION: android15
2026-05-03T00:38:24.5986483Z   KERNEL_VERSION: 6.6
2026-05-03T00:38:24.5986933Z   KMI_GENERATION: 8
2026-05-03T00:38:24.5987324Z   KERNEL_NAME: Castorice
2026-05-03T00:38:24.5987721Z   DEVICE_CODE: fire
2026-05-03T00:38:24.5988074Z   KSU_DIR: 
2026-05-03T00:38:24.5988431Z   KSU_VERSION: 
2026-05-03T00:38:24.5989018Z   SUSFS_OK: 
2026-05-03T00:38:24.5989390Z   BUILT_KERNEL_VERSION: 
2026-05-03T00:38:24.5989789Z   ZIP_NAME: 
2026-05-03T00:38:24.5990132Z ##[endgroup]
2026-05-03T00:38:24.7010250Z Syncing repository: naidrahiqa/CastoriceKernelSUN
2026-05-03T00:38:24.7012143Z ##[group]Getting Git version info
2026-05-03T00:38:24.7012955Z Working directory is '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN'
2026-05-03T00:38:24.7014072Z [command]/usr/bin/git version
2026-05-03T00:38:24.7055296Z git version 2.53.0
2026-05-03T00:38:24.7077765Z ##[endgroup]
2026-05-03T00:38:24.7092074Z Temporarily overriding HOME='/home/runner/work/_temp/b741c51a-db9a-4c7f-9d73-f92ce8ad07e9' before making global git config changes
2026-05-03T00:38:24.7097654Z Adding repository directory to the temporary git global config as a safe directory
2026-05-03T00:38:24.7099720Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN
2026-05-03T00:38:24.7130496Z Deleting the contents of '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN'
2026-05-03T00:38:24.7134351Z ##[group]Initializing the repository
2026-05-03T00:38:24.7138821Z [command]/usr/bin/git init /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN
2026-05-03T00:38:24.7240301Z hint: Using 'master' as the name for the initial branch. This default branch name
2026-05-03T00:38:24.7241868Z hint: will change to "main" in Git 3.0. To configure the initial branch name
2026-05-03T00:38:24.7243491Z hint: to use in all of your new repositories, which will suppress this warning,
2026-05-03T00:38:24.7244789Z hint: call:
2026-05-03T00:38:24.7245483Z hint:
2026-05-03T00:38:24.7246339Z hint: 	git config --global init.defaultBranch <name>
2026-05-03T00:38:24.7247386Z hint:
2026-05-03T00:38:24.7248399Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2026-05-03T00:38:24.7250265Z hint: 'development'. The just-created branch can be renamed via this command:
2026-05-03T00:38:24.7251452Z hint:
2026-05-03T00:38:24.7252110Z hint: 	git branch -m <name>
2026-05-03T00:38:24.7252937Z hint:
2026-05-03T00:38:24.7254071Z hint: Disable this message with "git config set advice.defaultBranchName false"
2026-05-03T00:38:24.7256046Z Initialized empty Git repository in /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/.git/
2026-05-03T00:38:24.7259284Z [command]/usr/bin/git remote add origin https://github.com/naidrahiqa/CastoriceKernelSUN
2026-05-03T00:38:24.7286792Z ##[endgroup]
2026-05-03T00:38:24.7288032Z ##[group]Disabling automatic garbage collection
2026-05-03T00:38:24.7291622Z [command]/usr/bin/git config --local gc.auto 0
2026-05-03T00:38:24.7319632Z ##[endgroup]
2026-05-03T00:38:24.7320413Z ##[group]Setting up auth
2026-05-03T00:38:24.7326483Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-05-03T00:38:24.7356529Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-05-03T00:38:24.7643090Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-05-03T00:38:24.7672999Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-05-03T00:38:24.7887803Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-05-03T00:38:24.7918880Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-05-03T00:38:24.8134482Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2026-05-03T00:38:24.8167760Z ##[endgroup]
2026-05-03T00:38:24.8169261Z ##[group]Fetching the repository
2026-05-03T00:38:24.8178203Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +99b81c0a3ce3d33fcaf1bb4bb561d5e42ec54f8f:refs/remotes/origin/main
2026-05-03T00:38:24.9690414Z From https://github.com/naidrahiqa/CastoriceKernelSUN
2026-05-03T00:38:24.9692519Z  * [new ref]         99b81c0a3ce3d33fcaf1bb4bb561d5e42ec54f8f -> origin/main
2026-05-03T00:38:24.9695758Z ##[endgroup]
2026-05-03T00:38:24.9697082Z ##[group]Determining the checkout info
2026-05-03T00:38:24.9699127Z ##[endgroup]
2026-05-03T00:38:24.9700160Z [command]/usr/bin/git sparse-checkout disable
2026-05-03T00:38:24.9703738Z [command]/usr/bin/git config --local --unset-all extensions.worktreeConfig
2026-05-03T00:38:24.9730753Z ##[group]Checking out the ref
2026-05-03T00:38:24.9735430Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
2026-05-03T00:38:24.9779255Z Switched to a new branch 'main'
2026-05-03T00:38:24.9782143Z branch 'main' set up to track 'origin/main'.
2026-05-03T00:38:24.9789764Z ##[endgroup]
2026-05-03T00:38:24.9864267Z [command]/usr/bin/git log -1 --format=%H
2026-05-03T00:38:24.9887978Z 99b81c0a3ce3d33fcaf1bb4bb561d5e42ec54f8f
2026-05-03T00:38:25.0109400Z ##[group]Run echo "=== Before cleanup ==="
2026-05-03T00:38:25.0110791Z [36;1mecho "=== Before cleanup ==="[0m
2026-05-03T00:38:25.0111910Z [36;1mdf -h /[0m
2026-05-03T00:38:25.0113148Z [36;1msudo rm -rf /usr/share/dotnet /usr/local/lib/android /opt/ghc[0m
2026-05-03T00:38:25.0115201Z [36;1msudo rm -rf /usr/share/swift /usr/share/miniconda /opt/hostedtoolcache[0m
2026-05-03T00:38:25.0117322Z [36;1msudo rm -rf /usr/local/share/chromium /usr/local/share/powershell[0m
2026-05-03T00:38:25.0120674Z [36;1msudo apt-get remove -y '^dotnet-.*' '^llvm-.*' 'php.*' azure-cli google-cloud-cli google-chrome-stable firefox powershell mono-devel || true[0m
2026-05-03T00:38:25.0123447Z [36;1msudo apt-get autoremove -y[0m
2026-05-03T00:38:25.0124576Z [36;1msudo apt-get clean[0m
2026-05-03T00:38:25.0125613Z [36;1mecho "=== After cleanup ==="[0m
2026-05-03T00:38:25.0126673Z [36;1mdf -h /[0m
2026-05-03T00:38:25.0152733Z shell: /usr/bin/bash -e {0}
2026-05-03T00:38:25.0153736Z env:
2026-05-03T00:38:25.0154600Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:38:25.0155764Z   ANDROID_VERSION: android15
2026-05-03T00:38:25.0156755Z   KERNEL_VERSION: 6.6
2026-05-03T00:38:25.0157636Z   KMI_GENERATION: 8
2026-05-03T00:38:25.0158441Z   KERNEL_NAME: Castorice
2026-05-03T00:38:25.0159508Z   DEVICE_CODE: fire
2026-05-03T00:38:25.0160277Z   KSU_DIR: 
2026-05-03T00:38:25.0160986Z   KSU_VERSION: 
2026-05-03T00:38:25.0161710Z   SUSFS_OK: 
2026-05-03T00:38:25.0162443Z   BUILT_KERNEL_VERSION: 
2026-05-03T00:38:25.0163260Z   ZIP_NAME: 
2026-05-03T00:38:25.0163951Z ##[endgroup]
2026-05-03T00:38:25.0233522Z === Before cleanup ===
2026-05-03T00:38:25.0251499Z Filesystem      Size  Used Avail Use% Mounted on
2026-05-03T00:38:25.0253501Z /dev/root       145G   56G   90G  39% /
2026-05-03T00:39:22.1468838Z Reading package lists...
2026-05-03T00:39:22.3633916Z Building dependency tree...
2026-05-03T00:39:22.3653435Z Reading state information...
2026-05-03T00:39:22.6849570Z Package 'dotnet-hostfxr-6.0' is not installed, so not removed
2026-05-03T00:39:22.6850323Z Package 'dotnet-runtime-6.0' is not installed, so not removed
2026-05-03T00:39:22.6851012Z Package 'dotnet-sdk-6.0' is not installed, so not removed
2026-05-03T00:39:22.6851808Z Package 'dotnet-targeting-pack-6.0' is not installed, so not removed
2026-05-03T00:39:22.6859657Z Package 'dotnet-templates-6.0' is not installed, so not removed
2026-05-03T00:39:22.6860328Z Package 'llvm-21' is not installed, so not removed
2026-05-03T00:39:22.6860976Z Package 'php-lua' is not installed, so not removed
2026-05-03T00:39:22.6861596Z Package 'php-mysqlnd-ms' is not installed, so not removed
2026-05-03T00:39:22.6862216Z Package 'php-radius' is not installed, so not removed
2026-05-03T00:39:22.6862791Z Package 'php5.6-common' is not installed, so not removed
2026-05-03T00:39:22.6863399Z Package 'php5.6-json' is not installed, so not removed
2026-05-03T00:39:22.6864082Z Package 'php7.0-common' is not installed, so not removed
2026-05-03T00:39:22.6864708Z Package 'php7.1-common' is not installed, so not removed
2026-05-03T00:39:22.6865328Z Package 'php7.2-common' is not installed, so not removed
2026-05-03T00:39:22.6865875Z Package 'php7.3-common' is not installed, so not removed
2026-05-03T00:39:22.6866403Z Package 'php7.4-common' is not installed, so not removed
2026-05-03T00:39:22.6866923Z Package 'php8.0-common' is not installed, so not removed
2026-05-03T00:39:22.6867456Z Package 'php8.1-common' is not installed, so not removed
2026-05-03T00:39:22.6867979Z Package 'php8.2-common' is not installed, so not removed
2026-05-03T00:39:22.6868564Z Package 'php-pear-frontend-gtk' is not installed, so not removed
2026-05-03T00:39:22.6869438Z Package 'php-pear-frontend-web' is not installed, so not removed
2026-05-03T00:39:22.6870536Z Package 'php7.0-curl' is not installed, so not removed
2026-05-03T00:39:22.6871103Z Package 'php7.2-sodium' is not installed, so not removed
2026-05-03T00:39:22.6871648Z Package 'php5' is not installed, so not removed
2026-05-03T00:39:22.6872454Z Package 'php5-cli' is not installed, so not removed
2026-05-03T00:39:22.6872987Z Package 'php5-pgsql' is not installed, so not removed
2026-05-03T00:39:22.6873530Z Package 'php5-curl' is not installed, so not removed
2026-05-03T00:39:22.6874058Z Package 'php5-ldap' is not installed, so not removed
2026-05-03T00:39:22.6874559Z Package 'gosa-plugin-phpgw' is not installed, so not removed
2026-05-03T00:39:22.6875156Z Package 'gosa-plugin-phpgw-schema' is not installed, so not removed
2026-05-03T00:39:22.6875782Z Package 'gosa-plugin-phpscheduleit' is not installed, so not removed
2026-05-03T00:39:22.6876458Z Package 'gosa-plugin-phpscheduleit-schema' is not installed, so not removed
2026-05-03T00:39:22.6877041Z Package 'php-apc' is not installed, so not removed
2026-05-03T00:39:22.6877533Z Package 'php-suhosin' is not installed, so not removed
2026-05-03T00:39:22.6878007Z Package 'php5-mysql' is not installed, so not removed
2026-05-03T00:39:22.6879048Z Package 'libsparkline-php' is not installed, so not removed
2026-05-03T00:39:22.6879620Z Package 'libapache2-mod-php5' is not installed, so not removed
2026-05-03T00:39:22.6880127Z Package 'php5-fpm' is not installed, so not removed
2026-05-03T00:39:22.6880595Z Package 'libgv-php5' is not installed, so not removed
2026-05-03T00:39:22.6881172Z Package 'php-greew-oauth2-azure-provider' is not installed, so not removed
2026-05-03T00:39:22.6881846Z Package 'php-hayageek-oauth2-yahoo' is not installed, so not removed
2026-05-03T00:39:22.6882470Z Package 'php-league-oauth2-google' is not installed, so not removed
2026-05-03T00:39:22.6883160Z Package 'php-thenetworg-oauth2-azure' is not installed, so not removed
2026-05-03T00:39:22.6883744Z Package 'phpphylotree' is not installed, so not removed
2026-05-03T00:39:22.6884261Z Package 'php-http-request2' is not installed, so not removed
2026-05-03T00:39:22.6884780Z Package 'php-xcache' is not installed, so not removed
2026-05-03T00:39:22.6885278Z Package 'php-async-aws-s3' is not installed, so not removed
2026-05-03T00:39:22.6885883Z Package 'php-paragonie-random-compat' is not installed, so not removed
2026-05-03T00:39:22.6886500Z Package 'php-console-color2' is not installed, so not removed
2026-05-03T00:39:22.6887086Z Package 'php-doctrine-phpcr-odm' is not installed, so not removed
2026-05-03T00:39:22.6887737Z Package 'php-alcaeus-mongo-php-adapter' is not installed, so not removed
2026-05-03T00:39:22.6888392Z Package 'php-doctrine-mongodb-odm' is not installed, so not removed
2026-05-03T00:39:22.6889314Z Package 'php-mtdowling-cron-expression' is not installed, so not removed
2026-05-03T00:39:22.6889924Z Package 'php-semsol-arc2' is not installed, so not removed
2026-05-03T00:39:22.6890476Z Package 'php-fzaninotto-faker' is not installed, so not removed
2026-05-03T00:39:22.6891004Z Package 'php7.4' is not installed, so not removed
2026-05-03T00:39:22.6891458Z Package 'php7.4-cli' is not installed, so not removed
2026-05-03T00:39:22.6891956Z Package 'php-com-dotnet' is not installed, so not removed
2026-05-03T00:39:22.6892441Z Package 'php-rar' is not installed, so not removed
2026-05-03T00:39:22.6893024Z Package 'php-laminas-httphandlerrunner' is not installed, so not removed
2026-05-03T00:39:22.6893686Z Package 'php-cordoval-hamcrest-php' is not installed, so not removed
2026-05-03T00:39:22.6894378Z Package 'php-davedevelopment-hamcrest-php' is not installed, so not removed
2026-05-03T00:39:22.6895057Z Package 'php-kodova-hamcrest-php' is not installed, so not removed
2026-05-03T00:39:22.6895685Z Package 'php-league-flysystem-sftp' is not installed, so not removed
2026-05-03T00:39:22.6896428Z Package 'php-league-flysystem-eventable-filesystem' is not installed, so not removed
2026-05-03T00:39:22.6897226Z Package 'php-league-flysystem-rackspace' is not installed, so not removed
2026-05-03T00:39:22.6898155Z Package 'php-league-flysystem-azure' is not installed, so not removed
2026-05-03T00:39:22.6899009Z Package 'php-league-flysystem-webdav' is not installed, so not removed
2026-05-03T00:39:22.6899888Z Package 'php-league-flysystem-aws-s3-v2' is not installed, so not removed
2026-05-03T00:39:22.6900623Z Package 'php-league-flysystem-aws-s3-v3' is not installed, so not removed
2026-05-03T00:39:22.6901332Z Package 'php-spatie-flysystem-dropbox' is not installed, so not removed
2026-05-03T00:39:22.6902080Z Package 'php-srmklive-flysystem-dropbox-v2' is not installed, so not removed
2026-05-03T00:39:22.6902879Z Package 'php-league-flysystem-cached-adapter' is not installed, so not removed
2026-05-03T00:39:22.6903650Z Package 'php-league-flysystem-ziparchive' is not installed, so not removed
2026-05-03T00:39:22.6904344Z Package 'php-league-uri-schemes' is not installed, so not removed
2026-05-03T00:39:22.6905059Z Package 'php-jeremykendall-php-domain-parser' is not installed, so not removed
2026-05-03T00:39:22.6905743Z Package 'php-php-64bit' is not installed, so not removed
2026-05-03T00:39:22.6906260Z Package 'php-sqlite' is not installed, so not removed
2026-05-03T00:39:22.6906761Z Package 'php-lzf' is not installed, so not removed
2026-05-03T00:39:22.6907262Z Package 'php-pnctl' is not installed, so not removed
2026-05-03T00:39:22.6907829Z Package 'php-mdb2-driver-fbsql' is not installed, so not removed
2026-05-03T00:39:22.6908471Z Package 'php-mdb2-driver-ibase' is not installed, so not removed
2026-05-03T00:39:22.6909282Z Package 'php-mdb2-driver-mssql' is not installed, so not removed
2026-05-03T00:39:22.6909909Z Package 'php-mdb2-driver-mysqli' is not installed, so not removed
2026-05-03T00:39:22.6910522Z Package 'php-mdb2-driver-oci8' is not installed, so not removed
2026-05-03T00:39:22.6911130Z Package 'php-mdb2-driver-odbc' is not installed, so not removed
2026-05-03T00:39:22.6911754Z Package 'php-mdb2-driver-querysim' is not installed, so not removed
2026-05-03T00:39:22.6912415Z Package 'php-mdb2-driver-sqlite' is not installed, so not removed
2026-05-03T00:39:22.6913049Z Package 'php-mdb2-driver-sqlsrv' is not installed, so not removed
2026-05-03T00:39:22.6913733Z Package 'php-barnabywalters-mf-cleaner' is not installed, so not removed
2026-05-03T00:39:22.6914428Z Package 'php-graylog2-gelf-php' is not installed, so not removed
2026-05-03T00:39:22.6915046Z Package 'php-doctrine-couchdb' is not installed, so not removed
2026-05-03T00:39:22.6915654Z Package 'php-ruflin-elastica' is not installed, so not removed
2026-05-03T00:39:22.6916244Z Package 'php-elasticsearch' is not installed, so not removed
2026-05-03T00:39:22.6916829Z Package 'php-aws-sdk-php' is not installed, so not removed
2026-05-03T00:39:22.6917377Z Package 'php-rollbar' is not installed, so not removed
2026-05-03T00:39:22.6917923Z Package 'php-nette-finder' is not installed, so not removed
2026-05-03T00:39:22.6918468Z Package 'php-dbase' is not installed, so not removed
2026-05-03T00:39:22.6919220Z Package 'php-libsodium' is not installed, so not removed
2026-05-03T00:39:22.6919755Z Package 'php-relay' is not installed, so not removed
2026-05-03T00:39:22.6920355Z Package 'php-ocramius-proxy-manager' is not installed, so not removed
2026-05-03T00:39:22.6921089Z Package 'php-zendframework-zend-stdlib' is not installed, so not removed
2026-05-03T00:39:22.6921753Z Package 'php-rhumsaa-uuid' is not installed, so not removed
2026-05-03T00:39:22.6922380Z Package 'php-paragonie-random-lib' is not installed, so not removed
2026-05-03T00:39:22.6923054Z Package 'php-ramsey-uuid-doctrine' is not installed, so not removed
2026-05-03T00:39:22.6923685Z Package 'php-crypt-blowfish' is not installed, so not removed
2026-05-03T00:39:22.6924246Z Package 'php-compat' is not installed, so not removed
2026-05-03T00:39:22.6924763Z Package 'libssh2-php' is not installed, so not removed
2026-05-03T00:39:22.6925357Z Package 'php-php-http-discovery' is not installed, so not removed
2026-05-03T00:39:22.6926035Z Package 'php-symfony-security-guard' is not installed, so not removed
2026-05-03T00:39:22.6926846Z Package 'php-numbers-words' is not installed, so not removed
2026-05-03T00:39:22.6927416Z Package 'php7.0-thrift' is not installed, so not removed
2026-05-03T00:39:22.6928104Z Package 'php7.2-thrift' is not installed, so not removed
2026-05-03T00:39:22.6928850Z Package 'php-net-idna' is not installed, so not removed
2026-05-03T00:39:22.6929391Z Package 'php-phpstan' is not installed, so not removed
2026-05-03T00:39:22.6929957Z Package 'php-vimeo-psalm' is not installed, so not removed
2026-05-03T00:39:22.6930573Z Package 'php-container-interop' is not installed, so not removed
2026-05-03T00:39:22.6931306Z Package 'php-zendframework-zend-eventmanager' is not installed, so not removed
2026-05-03T00:39:22.6931997Z Package 'php-recode' is not installed, so not removed
2026-05-03T00:39:22.6932506Z Package 'php-gd2' is not installed, so not removed
2026-05-03T00:39:22.6933132Z Package 'php-pragmarx-google2fa-qrcode' is not installed, so not removed
2026-05-03T00:39:22.6933850Z Package 'php-bjeavons-zxcvbn-php' is not installed, so not removed
2026-05-03T00:39:22.6934507Z Package 'php-pimlie-php-dkim' is not installed, so not removed
2026-05-03T00:39:22.6935151Z Package 'libapache2-mod-php7.4' is not installed, so not removed
2026-05-03T00:39:22.6935756Z Package 'php7.4-fpm' is not installed, so not removed
2026-05-03T00:39:22.6936362Z Package 'dotnet-apphost-pack-6.0' is not installed, so not removed
2026-05-03T00:39:22.6937005Z Package 'dotnet-runtime-8.0' is not installed, so not removed
2026-05-03T00:39:22.6937644Z Package 'dotnet-apphost-pack-8.0' is not installed, so not removed
2026-05-03T00:39:22.6938264Z Package 'dotnet-host-8.0' is not installed, so not removed
2026-05-03T00:39:22.6939037Z Package 'dotnet-hostfxr-8.0' is not installed, so not removed
2026-05-03T00:39:22.6939619Z Package 'dotnet-sdk-8.0' is not installed, so not removed
2026-05-03T00:39:22.6940259Z Package 'dotnet-targeting-pack-8.0' is not installed, so not removed
2026-05-03T00:39:22.6940949Z Package 'dotnet-templates-8.0' is not installed, so not removed
2026-05-03T00:39:22.6941610Z Package 'dotnet-runtime-dbg-8.0' is not installed, so not removed
2026-05-03T00:39:22.6942385Z Package 'dotnet-sdk-8.0-source-built-artifacts' is not installed, so not removed
2026-05-03T00:39:22.6943127Z Package 'dotnet-sdk-dbg-8.0' is not installed, so not removed
2026-05-03T00:39:22.6943756Z Package 'dotnet-runtime-10.0' is not installed, so not removed
2026-05-03T00:39:22.6944422Z Package 'dotnet-apphost-pack-10.0' is not installed, so not removed
2026-05-03T00:39:22.6945074Z Package 'dotnet-host-10.0' is not installed, so not removed
2026-05-03T00:39:22.6945687Z Package 'dotnet-hostfxr-10.0' is not installed, so not removed
2026-05-03T00:39:22.6946343Z Package 'dotnet-runtime-dbg-10.0' is not installed, so not removed
2026-05-03T00:39:22.6946986Z Package 'dotnet-sdk-10.0' is not installed, so not removed
2026-05-03T00:39:22.6947657Z Package 'dotnet-targeting-pack-10.0' is not installed, so not removed
2026-05-03T00:39:22.6948366Z Package 'dotnet-templates-10.0' is not installed, so not removed
2026-05-03T00:39:22.6949201Z Package 'dotnet-sdk-aot-10.0' is not installed, so not removed
2026-05-03T00:39:22.6949844Z Package 'dotnet-sdk-dbg-10.0' is not installed, so not removed
2026-05-03T00:39:22.6950610Z Package 'dotnet-sdk-10.0-source-built-artifacts' is not installed, so not removed
2026-05-03T00:39:22.6951398Z Package 'llvm-14-linker-tools' is not installed, so not removed
2026-05-03T00:39:22.6951981Z Package 'llvm-14-dev' is not installed, so not removed
2026-05-03T00:39:22.6952529Z Package 'llvm-15-linker-tools' is not installed, so not removed
2026-05-03T00:39:22.6953069Z Package 'llvm-15-dev' is not installed, so not removed
2026-05-03T00:39:22.6953553Z Package 'llvm-15' is not installed, so not removed
2026-05-03T00:39:22.6954013Z Package 'llvm-dev' is not installed, so not removed
2026-05-03T00:39:22.6954497Z Package 'llvm-14-doc' is not installed, so not removed
2026-05-03T00:39:22.6955170Z Package 'llvm-15-doc' is not installed, so not removed
2026-05-03T00:39:22.6955656Z Package 'llvm-16-doc' is not installed, so not removed
2026-05-03T00:39:22.6956139Z Package 'llvm-17-doc' is not installed, so not removed
2026-05-03T00:39:22.6956762Z Package 'llvm-18-doc' is not installed, so not removed
2026-05-03T00:39:22.6957272Z Package 'llvm-runtime' is not installed, so not removed
2026-05-03T00:39:22.6957744Z Package 'llvm-14' is not installed, so not removed
2026-05-03T00:39:22.6958246Z Package 'llvm-14-runtime' is not installed, so not removed
2026-05-03T00:39:22.6959020Z Package 'llvm-14-tools' is not installed, so not removed
2026-05-03T00:39:22.6959581Z Package 'llvm-14-examples' is not installed, so not removed
2026-05-03T00:39:22.6960130Z Package 'llvm-15-runtime' is not installed, so not removed
2026-05-03T00:39:22.6960718Z Package 'llvm-15-tools' is not installed, so not removed
2026-05-03T00:39:22.6961251Z Package 'llvm-15-examples' is not installed, so not removed
2026-05-03T00:39:22.6961794Z Package 'llvm-16-examples' is not installed, so not removed
2026-05-03T00:39:22.6962334Z Package 'llvm-17-examples' is not installed, so not removed
2026-05-03T00:39:22.6962864Z Package 'llvm-18-examples' is not installed, so not removed
2026-05-03T00:39:22.6963383Z Package 'llvm-bolt' is not installed, so not removed
2026-05-03T00:39:22.6963884Z Package 'llvm-spirv-14' is not installed, so not removed
2026-05-03T00:39:22.6964396Z Package 'llvm-spirv-15' is not installed, so not removed
2026-05-03T00:39:22.6964912Z Package 'llvm-spirv-16' is not installed, so not removed
2026-05-03T00:39:22.6965421Z Package 'llvm-spirv-17' is not installed, so not removed
2026-05-03T00:39:22.6965954Z Package 'llvm-spirv-18' is not installed, so not removed
2026-05-03T00:39:22.6966457Z Package 'llvm-19-dev' is not installed, so not removed
2026-05-03T00:39:22.6966953Z Package 'llvm-20-dev' is not installed, so not removed
2026-05-03T00:39:22.6967490Z Package 'llvm-19-linker-tools' is not installed, so not removed
2026-05-03T00:39:22.6968092Z Package 'llvm-20-linker-tools' is not installed, so not removed
2026-05-03T00:39:22.6968835Z Package 'llvm-19-doc' is not installed, so not removed
2026-05-03T00:39:22.6969340Z Package 'llvm-20-doc' is not installed, so not removed
2026-05-03T00:39:22.6969822Z Package 'llvm-19' is not installed, so not removed
2026-05-03T00:39:22.6970319Z Package 'llvm-19-runtime' is not installed, so not removed
2026-05-03T00:39:22.6970857Z Package 'llvm-19-tools' is not installed, so not removed
2026-05-03T00:39:22.6971389Z Package 'llvm-19-examples' is not installed, so not removed
2026-05-03T00:39:22.6971891Z Package 'llvm-20' is not installed, so not removed
2026-05-03T00:39:22.6972398Z Package 'llvm-20-runtime' is not installed, so not removed
2026-05-03T00:39:22.6972922Z Package 'llvm-20-tools' is not installed, so not removed
2026-05-03T00:39:22.6973458Z Package 'llvm-20-examples' is not installed, so not removed
2026-05-03T00:39:22.6973992Z Package 'llvm-spirv-19' is not installed, so not removed
2026-05-03T00:39:22.6974518Z Package 'llvm-spirv-20' is not installed, so not removed
2026-05-03T00:39:22.6975032Z Package 'php-crypt-gpg' is not installed, so not removed
2026-05-03T00:39:22.6975598Z Package 'libapache2-mod-php' is not installed, so not removed
2026-05-03T00:39:22.6976228Z Package 'libapache2-mod-php8.3' is not installed, so not removed
2026-05-03T00:39:22.6976784Z Package 'php-json' is not installed, so not removed
2026-05-03T00:39:22.6977246Z Package 'php' is not installed, so not removed
2026-05-03T00:39:22.6977726Z Package 'php-all-dev' is not installed, so not removed
2026-05-03T00:39:22.6978211Z Package 'php-cgi' is not installed, so not removed
2026-05-03T00:39:22.6978857Z Package 'php-cli' is not installed, so not removed
2026-05-03T00:39:22.6979337Z Package 'php-amqp' is not installed, so not removed
2026-05-03T00:39:22.6979816Z Package 'php-apcu' is not installed, so not removed
2026-05-03T00:39:22.6980291Z Package 'php-ast' is not installed, so not removed
2026-05-03T00:39:22.6980938Z Package 'php-ds' is not installed, so not removed
2026-05-03T00:39:22.6981456Z Package 'php-facedetect' is not installed, so not removed
2026-05-03T00:39:22.6981993Z Package 'php-gearman' is not installed, so not removed
2026-05-03T00:39:22.6982648Z Package 'php-gmagick' is not installed, so not removed
2026-05-03T00:39:22.6983158Z Package 'php-gnupg' is not installed, so not removed
2026-05-03T00:39:22.6983667Z Package 'php-igbinary' is not installed, so not removed
2026-05-03T00:39:22.6984181Z Package 'php-imagick' is not installed, so not removed
2026-05-03T00:39:22.6984715Z Package 'php-libvirt-php' is not installed, so not removed
2026-05-03T00:39:22.6985265Z Package 'php-mailparse' is not installed, so not removed
2026-05-03T00:39:22.6985788Z Package 'php-memcache' is not installed, so not removed
2026-05-03T00:39:22.6986314Z Package 'php-memcached' is not installed, so not removed
2026-05-03T00:39:22.6986833Z Package 'php-mongodb' is not installed, so not removed
2026-05-03T00:39:22.6987348Z Package 'php-msgpack' is not installed, so not removed
2026-05-03T00:39:22.6987846Z Package 'php-oauth' is not installed, so not removed
2026-05-03T00:39:22.6988349Z Package 'php-pcov' is not installed, so not removed
2026-05-03T00:39:22.6989018Z Package 'php-ps' is not installed, so not removed
2026-05-03T00:39:22.6989487Z Package 'php-psr' is not installed, so not removed
2026-05-03T00:39:22.6989985Z Package 'php-raphf' is not installed, so not removed
2026-05-03T00:39:22.6990474Z Package 'php-redis' is not installed, so not removed
2026-05-03T00:39:22.6990959Z Package 'php-rrd' is not installed, so not removed
2026-05-03T00:39:22.6991463Z Package 'php-smbclient' is not installed, so not removed
2026-05-03T00:39:22.6991974Z Package 'php-ssh2' is not installed, so not removed
2026-05-03T00:39:22.6992463Z Package 'php-stomp' is not installed, so not removed
2026-05-03T00:39:22.6992976Z Package 'php-tideways' is not installed, so not removed
2026-05-03T00:39:22.6993475Z Package 'php-uopz' is not installed, so not removed
2026-05-03T00:39:22.6994030Z Package 'php-uploadprogress' is not installed, so not removed
2026-05-03T00:39:22.6994583Z Package 'php-uuid' is not installed, so not removed
2026-05-03T00:39:22.6995085Z Package 'php-xdebug' is not installed, so not removed
2026-05-03T00:39:22.6995599Z Package 'php-xmlrpc' is not installed, so not removed
2026-05-03T00:39:22.6996087Z Package 'php-yac' is not installed, so not removed
2026-05-03T00:39:22.6996570Z Package 'php-yaml' is not installed, so not removed
2026-05-03T00:39:22.6997050Z Package 'php-zmq' is not installed, so not removed
2026-05-03T00:39:22.6997516Z Package 'php-curl' is not installed, so not removed
2026-05-03T00:39:22.6997996Z Package 'php-dev' is not installed, so not removed
2026-05-03T00:39:22.6998461Z Package 'php-gd' is not installed, so not removed
2026-05-03T00:39:22.6999132Z Package 'php-gmp' is not installed, so not removed
2026-05-03T00:39:22.6999613Z Package 'php-ldap' is not installed, so not removed
2026-05-03T00:39:22.7000126Z Package 'php-mysql' is not installed, so not removed
2026-05-03T00:39:22.7000618Z Package 'php-odbc' is not installed, so not removed
2026-05-03T00:39:22.7001100Z Package 'php-xml' is not installed, so not removed
2026-05-03T00:39:22.7001602Z Package 'php-pgsql' is not installed, so not removed
2026-05-03T00:39:22.7002105Z Package 'php-pspell' is not installed, so not removed
2026-05-03T00:39:22.7002611Z Package 'php-snmp' is not installed, so not removed
2026-05-03T00:39:22.7003115Z Package 'php-sqlite3' is not installed, so not removed
2026-05-03T00:39:22.7003625Z Package 'php-tidy' is not installed, so not removed
2026-05-03T00:39:22.7004127Z Package 'php-tokenizer' is not installed, so not removed
2026-05-03T00:39:22.7004670Z Package 'pkg-php-tools' is not installed, so not removed
2026-05-03T00:39:22.7005177Z Package 'dh-php' is not installed, so not removed
2026-05-03T00:39:22.7005683Z Package 'php-mbstring' is not installed, so not removed
2026-05-03T00:39:22.7006211Z Package 'php-readline' is not installed, so not removed
2026-05-03T00:39:22.7006894Z Package 'php-fpm' is not installed, so not removed
2026-05-03T00:39:22.7007436Z Package 'php-codesniffer' is not installed, so not removed
2026-05-03T00:39:22.7008158Z Package 'libphp-phpmailer' is not installed, so not removed
2026-05-03T00:39:22.7009019Z Package 'php-phpmyadmin-motranslator' is not installed, so not removed
2026-05-03T00:39:22.7009668Z Package 'php-phpseclib' is not installed, so not removed
2026-05-03T00:39:22.7010188Z Package 'php-twig' is not installed, so not removed
2026-05-03T00:39:22.7010725Z Package 'php-mapscript-ng' is not installed, so not removed
2026-05-03T00:39:22.7011337Z Package 'php-composer-ca-bundle' is not installed, so not removed
2026-05-03T00:39:22.7012046Z Package 'php-composer-class-map-generator' is not installed, so not removed
2026-05-03T00:39:22.7012809Z Package 'php-composer-metadata-minifier' is not installed, so not removed
2026-05-03T00:39:22.7013497Z Package 'php-composer-semver' is not installed, so not removed
2026-05-03T00:39:22.7014149Z Package 'php-composer-spdx-licenses' is not installed, so not removed
2026-05-03T00:39:22.7014862Z Package 'php-composer-xdebug-handler' is not installed, so not removed
2026-05-03T00:39:22.7015517Z Package 'php-json-schema' is not installed, so not removed
2026-05-03T00:39:22.7016070Z Package 'php-psr-log' is not installed, so not removed
2026-05-03T00:39:22.7016653Z Package 'php-symfony-console' is not installed, so not removed
2026-05-03T00:39:22.7017283Z Package 'php-symfony-filesystem' is not installed, so not removed
2026-05-03T00:39:22.7017910Z Package 'php-symfony-finder' is not installed, so not removed
2026-05-03T00:39:22.7018510Z Package 'php-symfony-process' is not installed, so not removed
2026-05-03T00:39:22.7019312Z Package 'php-react-promise' is not installed, so not removed
2026-05-03T00:39:22.7019919Z Package 'php-composer-pcre' is not installed, so not removed
2026-05-03T00:39:22.7020548Z Package 'php-seld-signal-handler' is not installed, so not removed
2026-05-03T00:39:22.7021144Z Package 'php-intl' is not installed, so not removed
2026-05-03T00:39:22.7021635Z Package 'php-zip' is not installed, so not removed
2026-05-03T00:39:22.7022150Z Package 'libawl-php' is not installed, so not removed
2026-05-03T00:39:22.7022710Z Package 'libphp-simplepie' is not installed, so not removed
2026-05-03T00:39:22.7023259Z Package 'php-geshi' is not installed, so not removed
2026-05-03T00:39:22.7023797Z Package 'php-random-compat' is not installed, so not removed
2026-05-03T00:39:22.7024379Z Package 'elpa-php-mode' is not installed, so not removed
2026-05-03T00:39:22.7024906Z Package 'phpunit' is not installed, so not removed
2026-05-03T00:39:22.7025393Z Package 'php-geos' is not installed, so not removed
2026-05-03T00:39:22.7026056Z Package 'golang-github-phpdave11-gofpdi-dev' is not installed, so not removed
2026-05-03T00:39:22.7026774Z Package 'php-imap' is not installed, so not removed
2026-05-03T00:39:22.7027267Z Package 'php-fpdf' is not installed, so not removed
2026-05-03T00:39:22.7027816Z Package 'icinga-php-library' is not installed, so not removed
2026-05-03T00:39:22.7028449Z Package 'icinga-php-thirdparty' is not installed, so not removed
2026-05-03T00:39:22.7029212Z Package 'php-soap' is not installed, so not removed
2026-05-03T00:39:22.7029729Z Package 'php-icinga' is not installed, so not removed
2026-05-03T00:39:22.7030252Z Package 'php-tcpdf' is not installed, so not removed
2026-05-03T00:39:22.7030781Z Package 'kdevelop-php' is not installed, so not removed
2026-05-03T00:39:22.7031360Z Package 'kdevelop-php-l10n' is not installed, so not removed
2026-05-03T00:39:22.7031912Z Package 'php-mcrypt' is not installed, so not removed
2026-05-03T00:39:22.7032424Z Package 'less.php' is not installed, so not removed
2026-05-03T00:39:22.7033026Z Package 'libphp-serialization-perl' is not installed, so not removed
2026-05-03T00:39:22.7033789Z Package 'libhtml-wikiconverter-phpwiki-perl' is not installed, so not removed
2026-05-03T00:39:22.7034561Z Package 'libjs-php-date-formatter' is not installed, so not removed
2026-05-03T00:39:22.7035390Z Package 'libmarkdown-php' is not installed, so not removed
2026-05-03T00:39:22.7035974Z Package 'libnusoap-php' is not installed, so not removed
2026-05-03T00:39:22.7036704Z Package 'php-econea-nusoap' is not installed, so not removed
2026-05-03T00:39:22.7037359Z Package 'libow-php7t64' is not installed, so not removed
2026-05-03T00:39:22.7037961Z Package 'libownet-php' is not installed, so not removed
2026-05-03T00:39:22.7038560Z Package 'libphp-adodb' is not installed, so not removed
2026-05-03T00:39:22.7039393Z Package 'php-sybase' is not installed, so not removed
2026-05-03T00:39:22.7039988Z Package 'libphp-embed' is not installed, so not removed
2026-05-03T00:39:22.7040617Z Package 'libphp8.3-embed' is not installed, so not removed
2026-05-03T00:39:22.7041252Z Package 'libphp-jabber' is not installed, so not removed
2026-05-03T00:39:22.7041877Z Package 'libphp-snoopy' is not installed, so not removed
2026-05-03T00:39:22.7042495Z Package 'libphpy-dev' is not installed, so not removed
2026-05-03T00:39:22.7043077Z Package 'libphpy1' is not installed, so not removed
2026-05-03T00:39:22.7043687Z Package 'libxrdcephposix0' is not installed, so not removed
2026-05-03T00:39:22.7044299Z Package 'php-spyc' is not installed, so not removed
2026-05-03T00:39:22.7044926Z Package 'matomo-php-tracker' is not installed, so not removed
2026-05-03T00:39:22.7045583Z Package 'php-wikidiff2' is not installed, so not removed
2026-05-03T00:39:22.7046220Z Package 'php-luasandbox' is not installed, so not removed
2026-05-03T00:39:22.7046848Z Package 'mlmmj-php-web' is not installed, so not removed
2026-05-03T00:39:22.7047515Z Package 'mlmmj-php-web-admin' is not installed, so not removed
2026-05-03T00:39:22.7048180Z Package 'php-net-socket' is not installed, so not removed
2026-05-03T00:39:22.7049088Z Package 'node-codemirror-lang-php' is not installed, so not removed
2026-05-03T00:39:22.7049800Z Package 'node-lezer-php' is not installed, so not removed
2026-05-03T00:39:22.7050423Z Package 'phpmyadmin' is not installed, so not removed
2026-05-03T00:39:22.7050997Z Package 'php-cas' is not installed, so not removed
2026-05-03T00:39:22.7051572Z Package 'php-pclzip' is not installed, so not removed
2026-05-03T00:39:22.7052169Z Package 'phpqrcode' is not installed, so not removed
2026-05-03T00:39:22.7052799Z Package 'php-symfony-config' is not installed, so not removed
2026-05-03T00:39:22.7053599Z Package 'php-symfony-dependency-injection' is not installed, so not removed
2026-05-03T00:39:22.7054334Z Package 'phpmd' is not installed, so not removed
2026-05-03T00:39:22.7054980Z Package 'php-algo26-idna-convert' is not installed, so not removed
2026-05-03T00:39:22.7055795Z Package 'php-jakeasmith-http-build-url' is not installed, so not removed
2026-05-03T00:39:22.7056548Z Package 'php-amphp-amp' is not installed, so not removed
2026-05-03T00:39:22.7057200Z Package 'php-amqp-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7057836Z Package 'php-amqplib' is not installed, so not removed
2026-05-03T00:39:22.7058478Z Package 'php-apcu-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7059436Z Package 'php-arthurhoaro-web-thumbnailer' is not installed, so not removed
2026-05-03T00:39:22.7060226Z Package 'php-text-template' is not installed, so not removed
2026-05-03T00:39:22.7060937Z Package 'php8.3-ast' is not installed, so not removed
2026-05-03T00:39:22.7061570Z Package 'php-ast-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7062260Z Package 'php-async-aws-core' is not installed, so not removed
2026-05-03T00:39:22.7062930Z Package 'php-psr-cache' is not installed, so not removed
2026-05-03T00:39:22.7063706Z Package 'php-symfony-deprecation-contracts' is not installed, so not removed
2026-05-03T00:39:22.7064567Z Package 'php-symfony-http-client' is not installed, so not removed
2026-05-03T00:39:22.7065391Z Package 'php-symfony-http-client-contracts' is not installed, so not removed
2026-05-03T00:39:22.7066269Z Package 'php-symfony-service-contracts' is not installed, so not removed
2026-05-03T00:39:22.7067283Z Package 'php-async-aws-ses' is not installed, so not removed
2026-05-03T00:39:22.7067966Z Package 'php-async-aws-sns' is not installed, so not removed
2026-05-03T00:39:22.7068962Z Package 'php-async-aws-sqs' is not installed, so not removed
2026-05-03T00:39:22.7069638Z Package 'php-auth-sasl' is not installed, so not removed
2026-05-03T00:39:22.7070292Z Package 'php-bacon-qr-code' is not installed, so not removed
2026-05-03T00:39:22.7070996Z Package 'php-dasprid-enum' is not installed, so not removed
2026-05-03T00:39:22.7071629Z Package 'php-bcmath' is not installed, so not removed
2026-05-03T00:39:22.7072236Z Package 'php-brick-math' is not installed, so not removed
2026-05-03T00:39:22.7072925Z Package 'php-brick-varexporter' is not installed, so not removed
2026-05-03T00:39:22.7073588Z Package 'php-parser' is not installed, so not removed
2026-05-03T00:39:22.7074164Z Package 'php-bz2' is not installed, so not removed
2026-05-03T00:39:22.7074856Z Package 'php-cache-integration-tests' is not installed, so not removed
2026-05-03T00:39:22.7075539Z Package 'php-cache-tag-interop' is not installed, so not removed
2026-05-03T00:39:22.7076235Z Package 'php-christianriesen-base32' is not installed, so not removed
2026-05-03T00:39:22.7076988Z Package 'php-christianriesen-otp' is not installed, so not removed
2026-05-03T00:39:22.7077770Z Package 'php-code-lts-u2f-php-server' is not installed, so not removed
2026-05-03T00:39:22.7078507Z Package 'php-codecoverage' is not installed, so not removed
2026-05-03T00:39:22.7079493Z Package 'php-file-iterator' is not installed, so not removed
2026-05-03T00:39:22.7080266Z Package 'phpunit-code-unit-reverse-lookup' is not installed, so not removed
2026-05-03T00:39:22.7081086Z Package 'phpunit-complexity' is not installed, so not removed
2026-05-03T00:39:22.7081774Z Package 'phpunit-environment' is not installed, so not removed
2026-05-03T00:39:22.7082494Z Package 'phpunit-lines-of-code' is not installed, so not removed
2026-05-03T00:39:22.7083194Z Package 'phpunit-version' is not installed, so not removed
2026-05-03T00:39:22.7083911Z Package 'php-codeigniter-framework' is not installed, so not removed
2026-05-03T00:39:22.7084737Z Package 'php-codeigniter-framework-doc' is not installed, so not removed
2026-05-03T00:39:22.7085542Z Package 'php-console-commandline' is not installed, so not removed
2026-05-03T00:39:22.7086257Z Package 'php-console-table' is not installed, so not removed
2026-05-03T00:39:22.7086924Z Package 'php-constant-time' is not installed, so not removed
2026-05-03T00:39:22.7087590Z Package 'php-dapphp-radius' is not installed, so not removed
2026-05-03T00:39:22.7088200Z Package 'php-date' is not installed, so not removed
2026-05-03T00:39:22.7089025Z Package 'php-datto-json-rpc' is not installed, so not removed
2026-05-03T00:39:22.7089753Z Package 'php-datto-json-rpc-http' is not installed, so not removed
2026-05-03T00:39:22.7090402Z Package 'php-db' is not installed, so not removed
2026-05-03T00:39:22.7090995Z Package 'php-deepcopy' is not installed, so not removed
2026-05-03T00:39:22.7091701Z Package 'php-dflydev-dot-access-data' is not installed, so not removed
2026-05-03T00:39:22.7092386Z Package 'php-di' is not installed, so not removed
2026-05-03T00:39:22.7093017Z Package 'php-psr-container' is not installed, so not removed
2026-05-03T00:39:22.7093681Z Package 'php-di-invoker' is not installed, so not removed
2026-05-03T00:39:22.7094443Z Package 'php-laravel-serializable-closure' is not installed, so not removed
2026-05-03T00:39:22.7095245Z Package 'php-directory-scanner' is not installed, so not removed
2026-05-03T00:39:22.7095855Z Package 'php-doc' is not installed, so not removed
2026-05-03T00:39:22.7096482Z Package 'php-doctrine-annotations' is not installed, so not removed
2026-05-03T00:39:22.7097176Z Package 'php-doctrine-lexer' is not installed, so not removed
2026-05-03T00:39:22.7097799Z Package 'php-doctrine-cache' is not installed, so not removed
2026-05-03T00:39:22.7098873Z Package 'php-doctrine-collections' is not installed, so not removed
2026-05-03T00:39:22.7099595Z Package 'php-doctrine-deprecations' is not installed, so not removed
2026-05-03T00:39:22.7100283Z Package 'php-doctrine-common' is not installed, so not removed
2026-05-03T00:39:22.7101127Z Package 'php-doctrine-persistence' is not installed, so not removed
2026-05-03T00:39:22.7101866Z Package 'php-doctrine-data-fixtures' is not installed, so not removed
2026-05-03T00:39:22.7102546Z Package 'php-doctrine-dbal' is not installed, so not removed
2026-05-03T00:39:22.7103139Z Package 'php-doctrine-orm' is not installed, so not removed
2026-05-03T00:39:22.7103819Z Package 'php-doctrine-event-manager' is not installed, so not removed
2026-05-03T00:39:22.7104520Z Package 'php-doctrine-inflector' is not installed, so not removed
2026-05-03T00:39:22.7105224Z Package 'php-doctrine-instantiator' is not installed, so not removed
2026-05-03T00:39:22.7105897Z Package 'php-symfony-cache' is not installed, so not removed
2026-05-03T00:39:22.7106506Z Package 'php-symfony-yaml' is not installed, so not removed
2026-05-03T00:39:22.7107229Z Package 'php-dragonmantank-cron-expression' is not installed, so not removed
2026-05-03T00:39:22.7107981Z Package 'php-webmozart-assert' is not installed, so not removed
2026-05-03T00:39:22.7108585Z Package 'php8.3-ds' is not installed, so not removed
2026-05-03T00:39:22.7109316Z Package 'php-ds-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7109907Z Package 'php-easyrdf' is not installed, so not removed
2026-05-03T00:39:22.7110495Z Package 'php-ml-json-ld' is not installed, so not removed
2026-05-03T00:39:22.7111089Z Package 'php-eluceo-ical' is not installed, so not removed
2026-05-03T00:39:22.7111716Z Package 'php-email-validator' is not installed, so not removed
2026-05-03T00:39:22.7112293Z Package 'php-embed' is not installed, so not removed
2026-05-03T00:39:22.7112935Z Package 'php-oscarotero-html-parser' is not installed, so not removed
2026-05-03T00:39:22.7113649Z Package 'php-psr-http-message' is not installed, so not removed
2026-05-03T00:39:22.7114320Z Package 'php-psr-http-client' is not installed, so not removed
2026-05-03T00:39:22.7114978Z Package 'php-psr-http-factory' is not installed, so not removed
2026-05-03T00:39:22.7115666Z Package 'php-symfony-css-selector' is not installed, so not removed
2026-05-03T00:39:22.7116303Z Package 'php-enchant' is not installed, so not removed
2026-05-03T00:39:22.7116858Z Package 'php-excimer' is not installed, so not removed
2026-05-03T00:39:22.7117508Z Package 'php8.3-facedetect' is not installed, so not removed
2026-05-03T00:39:22.7118159Z Package 'php-facedetect-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7118961Z Package 'php-faker' is not installed, so not removed
2026-05-03T00:39:22.7119540Z Package 'php-fdomdocument' is not installed, so not removed
2026-05-03T00:39:22.7120213Z Package 'php-fig-http-message-util' is not installed, so not removed
2026-05-03T00:39:22.7120902Z Package 'php-fig-link-util' is not installed, so not removed
2026-05-03T00:39:22.7121501Z Package 'php-psr-link' is not installed, so not removed
2026-05-03T00:39:22.7122062Z Package 'php-font-lib' is not installed, so not removed
2026-05-03T00:39:22.7122706Z Package 'php-fruitcake-php-cors' is not installed, so not removed
2026-05-03T00:39:22.7123443Z Package 'php-symfony-http-foundation' is not installed, so not removed
2026-05-03T00:39:22.7124082Z Package 'php-fxsl' is not installed, so not removed
2026-05-03T00:39:22.7124642Z Package 'php8.3-gearman' is not installed, so not removed
2026-05-03T00:39:22.7125273Z Package 'php-gearman-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7125906Z Package 'php-getallheaders' is not installed, so not removed
2026-05-03T00:39:22.7126502Z Package 'php-getid3' is not installed, so not removed
2026-05-03T00:39:22.7127103Z Package 'php-gettext-languages' is not installed, so not removed
2026-05-03T00:39:22.7127782Z Package 'php-oscarotero-gettext' is not installed, so not removed
2026-05-03T00:39:22.7128881Z Package 'php-giggsey-libphonenumber' is not installed, so not removed
2026-05-03T00:39:22.7129598Z Package 'php-giggsey-locale' is not installed, so not removed
2026-05-03T00:39:22.7130218Z Package 'php8.3-gmagick' is not installed, so not removed
2026-05-03T00:39:22.7131000Z Package 'php-gmagick-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7131632Z Package 'php8.3-gnupg' is not installed, so not removed
2026-05-03T00:39:22.7132230Z Package 'php-gnupg-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7132872Z Package 'php-google-protobuf' is not installed, so not removed
2026-05-03T00:39:22.7133531Z Package 'php-google-recaptcha' is not installed, so not removed
2026-05-03T00:39:22.7134274Z Package 'php-graham-campbell-result-type' is not installed, so not removed
2026-05-03T00:39:22.7134989Z Package 'php-phpoption' is not installed, so not removed
2026-05-03T00:39:22.7135609Z Package 'php-gregwar-captcha' is not installed, so not removed
2026-05-03T00:39:22.7136228Z Package 'php-guestfs' is not installed, so not removed
2026-05-03T00:39:22.7136837Z Package 'php-guzzlehttp-guzzle' is not installed, so not removed
2026-05-03T00:39:22.7137537Z Package 'php-guzzlehttp-promises' is not installed, so not removed
2026-05-03T00:39:22.7138229Z Package 'php-guzzlehttp-psr7' is not installed, so not removed
2026-05-03T00:39:22.7139402Z Package 'php-hamcrest' is not installed, so not removed
2026-05-03T00:39:22.7139886Z Package 'php-htmlawed' is not installed, so not removed
2026-05-03T00:39:22.7140292Z Package 'php-htmlpurifier' is not installed, so not removed
2026-05-03T00:39:22.7140668Z Package 'php-http' is not installed, so not removed
2026-05-03T00:39:22.7141014Z Package 'php8.3-http' is not installed, so not removed
2026-05-03T00:39:22.7141392Z Package 'php-http-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7141779Z Package 'php-http-httplug' is not installed, so not removed
2026-05-03T00:39:22.7142168Z Package 'php-http-promise' is not installed, so not removed
2026-05-03T00:39:22.7142665Z Package 'php-http-interop-http-factory-tests' is not installed, so not removed
2026-05-03T00:39:22.7143199Z Package 'php-http-message-factory' is not installed, so not removed
2026-05-03T00:39:22.7143712Z Package 'php-http-psr7-integration-tests' is not installed, so not removed
2026-05-03T00:39:22.7144202Z Package 'php-http-webdav-server' is not installed, so not removed
2026-05-03T00:39:22.7144617Z Package 'php-httpful' is not installed, so not removed
2026-05-03T00:39:22.7145019Z Package 'php-igbinary-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7145437Z Package 'php-image-text' is not installed, so not removed
2026-05-03T00:39:22.7145851Z Package 'php-imagick-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7146252Z Package 'php-interbase' is not installed, so not removed
2026-05-03T00:39:22.7146629Z Package 'php-invoker' is not installed, so not removed
2026-05-03T00:39:22.7146985Z Package 'php-jshrink' is not installed, so not removed
2026-05-03T00:39:22.7147391Z Package 'php-kissifrot-php-ixr' is not installed, so not removed
2026-05-03T00:39:22.7147787Z Package 'php-klogger' is not installed, so not removed
2026-05-03T00:39:22.7148178Z Package 'php-lcobucci-clock' is not installed, so not removed
2026-05-03T00:39:22.7148574Z Package 'php-psr-clock' is not installed, so not removed
2026-05-03T00:39:22.7149262Z Package 'php-lcobucci-jwt' is not installed, so not removed
2026-05-03T00:39:22.7149690Z Package 'php-league-commonmark' is not installed, so not removed
2026-05-03T00:39:22.7150117Z Package 'php-league-config' is not installed, so not removed
2026-05-03T00:39:22.7150557Z Package 'php-psr-event-dispatcher' is not installed, so not removed
2026-05-03T00:39:22.7150982Z Package 'php-nette-schema' is not installed, so not removed
2026-05-03T00:39:22.7151377Z Package 'php-league-csv' is not installed, so not removed
2026-05-03T00:39:22.7151781Z Package 'php-league-flysystem' is not installed, so not removed
2026-05-03T00:39:22.7152255Z Package 'php-league-mime-type-detection' is not installed, so not removed
2026-05-03T00:39:22.7153000Z Package 'php-league-html-to-markdown' is not installed, so not removed
2026-05-03T00:39:22.7153446Z Package 'php-league-uri' is not installed, so not removed
2026-05-03T00:39:22.7154059Z Package 'php-league-uri-interfaces' is not installed, so not removed
2026-05-03T00:39:22.7154506Z Package 'php-league-uri-components' is not installed, so not removed
2026-05-03T00:39:22.7154917Z Package 'php-letodms-core' is not installed, so not removed
2026-05-03T00:39:22.7155324Z Package 'php-libvirt-php-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7155704Z Package 'php-log' is not installed, so not removed
2026-05-03T00:39:22.7156029Z Package 'php-mdb2' is not installed, so not removed
2026-05-03T00:39:22.7156347Z Package 'php-mail' is not installed, so not removed
2026-05-03T00:39:22.7156705Z Package 'php-lorenzo-pinky' is not installed, so not removed
2026-05-03T00:39:22.7157073Z Package 'php-net-smtp' is not installed, so not removed
2026-05-03T00:39:22.7157446Z Package 'php-mail-mime' is not installed, so not removed
2026-05-03T00:39:22.7157808Z Package 'php8.3-mailparse' is not installed, so not removed
2026-05-03T00:39:22.7158213Z Package 'php-mailparse-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7158843Z Package 'php-malkusch-lock' is not installed, so not removed
2026-05-03T00:39:22.7159267Z Package 'php-predis' is not installed, so not removed
2026-05-03T00:39:22.7159650Z Package 'php-mariadb-mysql-kbs' is not installed, so not removed
2026-05-03T00:39:22.7160058Z Package 'php-masterminds-html5' is not installed, so not removed
2026-05-03T00:39:22.7160491Z Package 'php-matthiasmullie-minify' is not installed, so not removed
2026-05-03T00:39:22.7160974Z Package 'php-matthiasmullie-path-converter' is not installed, so not removed
2026-05-03T00:39:22.7161484Z Package 'php-maxmind-web-service-common' is not installed, so not removed
2026-05-03T00:39:22.7161908Z Package 'php-maxminddb' is not installed, so not removed
2026-05-03T00:39:22.7162303Z Package 'php8.3-maxminddb' is not installed, so not removed
2026-05-03T00:39:22.7162709Z Package 'php-maxminddb-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7163110Z Package 'php8.3-mcrypt' is not installed, so not removed
2026-05-03T00:39:22.7163495Z Package 'php-mcrypt-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7163899Z Package 'php-mdb2-driver-mysql' is not installed, so not removed
2026-05-03T00:39:22.7164311Z Package 'php-mdb2-driver-pgsql' is not installed, so not removed
2026-05-03T00:39:22.7164717Z Package 'php-memcache-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7165133Z Package 'php-memcached-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7165543Z Package 'php-msgpack-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7165904Z Package 'php-mf2' is not installed, so not removed
2026-05-03T00:39:22.7166281Z Package 'php-mikey179-vfsstream' is not installed, so not removed
2026-05-03T00:39:22.7166665Z Package 'php-ml-iri' is not installed, so not removed
2026-05-03T00:39:22.7167003Z Package 'php-mock' is not installed, so not removed
2026-05-03T00:39:22.7167356Z Package 'php-mock-phpunit' is not installed, so not removed
2026-05-03T00:39:22.7167759Z Package 'php-mock-integration' is not installed, so not removed
2026-05-03T00:39:22.7168142Z Package 'php-mockery' is not installed, so not removed
2026-05-03T00:39:22.7168501Z Package 'php-mockery-doc' is not installed, so not removed
2026-05-03T00:39:22.7169124Z Package 'php-mongodb-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7169500Z Package 'php-monolog' is not installed, so not removed
2026-05-03T00:39:22.7169850Z Package 'php-net-dime' is not installed, so not removed
2026-05-03T00:39:22.7170197Z Package 'php-net-dns2' is not installed, so not removed
2026-05-03T00:39:22.7170545Z Package 'php-net-ftp' is not installed, so not removed
2026-05-03T00:39:22.7170891Z Package 'php-net-imap' is not installed, so not removed
2026-05-03T00:39:22.7171385Z Package 'php-net-ipv6' is not installed, so not removed
2026-05-03T00:39:22.7171736Z Package 'php-net-ldap2' is not installed, so not removed
2026-05-03T00:39:22.7172089Z Package 'php-net-ldap3' is not installed, so not removed
2026-05-03T00:39:22.7172543Z Package 'php-net-nntp' is not installed, so not removed
2026-05-03T00:39:22.7172917Z Package 'php-net-publicsuffix' is not installed, so not removed
2026-05-03T00:39:22.7173312Z Package 'php-net-sieve' is not installed, so not removed
2026-05-03T00:39:22.7173655Z Package 'php-net-url' is not installed, so not removed
2026-05-03T00:39:22.7174000Z Package 'php-net-url2' is not installed, so not removed
2026-05-03T00:39:22.7174347Z Package 'php-net-whois' is not installed, so not removed
2026-05-03T00:39:22.7174766Z Package 'php-netscape-bookmark-parser' is not installed, so not removed
2026-05-03T00:39:22.7175198Z Package 'php-nette-utils' is not installed, so not removed
2026-05-03T00:39:22.7175582Z Package 'php-nikic-fast-route' is not installed, so not removed
2026-05-03T00:39:22.7175983Z Package 'php-nyholm-psr7' is not installed, so not removed
2026-05-03T00:39:22.7176336Z Package 'php8.3-oauth' is not installed, so not removed
2026-05-03T00:39:22.7176710Z Package 'php-oauth-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7177099Z Package 'php-opis-closure' is not installed, so not removed
2026-05-03T00:39:22.7177458Z Package 'php-parsedown' is not installed, so not removed
2026-05-03T00:39:22.7177839Z Package 'php-parsedown-extra' is not installed, so not removed
2026-05-03T00:39:22.7178225Z Package 'php-pcov-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7178786Z Package 'php-pda-pheanstalk' is not installed, so not removed
2026-05-03T00:39:22.7179194Z Package 'php-phar-io-manifest' is not installed, so not removed
2026-05-03T00:39:22.7179601Z Package 'php-phar-io-version' is not installed, so not removed
2026-05-03T00:39:22.7179990Z Package 'php-php-gettext' is not installed, so not removed
2026-05-03T00:39:22.7180351Z Package 'php-phpdbg' is not installed, so not removed
2026-05-03T00:39:22.7180800Z Package 'php-phpdocumentor-reflection-common' is not installed, so not removed
2026-05-03T00:39:22.7181351Z Package 'php-phpdocumentor-reflection-docblock' is not installed, so not removed
2026-05-03T00:39:22.7181890Z Package 'php-phpdocumentor-type-resolver' is not installed, so not removed
2026-05-03T00:39:22.7182375Z Package 'php-phpstan-phpdoc-parser' is not installed, so not removed
2026-05-03T00:39:22.7182855Z Package 'php-symfony-expression-language' is not installed, so not removed
2026-05-03T00:39:22.7183332Z Package 'php-phpmyadmin-shapefile' is not installed, so not removed
2026-05-03T00:39:22.7183778Z Package 'php-phpmyadmin-sql-parser' is not installed, so not removed
2026-05-03T00:39:22.7184241Z Package 'php-symfony-polyfill-php80' is not installed, so not removed
2026-05-03T00:39:22.7184639Z Package 'php-seclib' is not installed, so not removed
2026-05-03T00:39:22.7184999Z Package 'php-phpseclib3' is not installed, so not removed
2026-05-03T00:39:22.7185389Z Package 'php-phpspec-prophecy' is not installed, so not removed
2026-05-03T00:39:22.7185799Z Package 'phpunit-comparator' is not installed, so not removed
2026-05-03T00:39:22.7186224Z Package 'phpunit-recursion-context' is not installed, so not removed
2026-05-03T00:39:22.7186702Z Package 'php-phpspec-prophecy-phpunit' is not installed, so not removed
2026-05-03T00:39:22.7187118Z Package 'php-pinba' is not installed, so not removed
2026-05-03T00:39:22.7187461Z Package 'php8.3-pinba' is not installed, so not removed
2026-05-03T00:39:22.7187833Z Package 'php-pinba-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7188211Z Package 'php-proxy-manager' is not installed, so not removed
2026-05-03T00:39:22.7188732Z Package 'php8.3-ps' is not installed, so not removed
2026-05-03T00:39:22.7189088Z Package 'php-ps-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7189443Z Package 'php8.3-psr' is not installed, so not removed
2026-05-03T00:39:22.7189927Z Package 'php-psr-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7190316Z Package 'php-psr-simple-cache' is not installed, so not removed
2026-05-03T00:39:22.7190862Z Package 'php-pubsubhubbub-publisher' is not installed, so not removed
2026-05-03T00:39:22.7191306Z Package 'php-ramsey-collection' is not installed, so not removed
2026-05-03T00:39:22.7191701Z Package 'php-ramsey-uuid' is not installed, so not removed
2026-05-03T00:39:22.7192056Z Package 'php8.3-raphf' is not installed, so not removed
2026-05-03T00:39:22.7192423Z Package 'php-raphf-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7192803Z Package 'php-redis-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7193164Z Package 'php-remctl' is not installed, so not removed
2026-05-03T00:39:22.7193566Z Package 'php-roundcube-rtf-html-php' is not installed, so not removed
2026-05-03T00:39:22.7193967Z Package 'php8.3-rrd' is not installed, so not removed
2026-05-03T00:39:22.7194336Z Package 'php-rrd-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7194701Z Package 'php-sabre-dav' is not installed, so not removed
2026-05-03T00:39:22.7195073Z Package 'php-sabre-vobject' is not installed, so not removed
2026-05-03T00:39:22.7195431Z Package 'php-sass' is not installed, so not removed
2026-05-03T00:39:22.7195762Z Package 'php8.3-sass' is not installed, so not removed
2026-05-03T00:39:22.7196126Z Package 'php-sass-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7196498Z Package 'php-shellcommand' is not installed, so not removed
2026-05-03T00:39:22.7196867Z Package 'php-slim-psr7' is not installed, so not removed
2026-05-03T00:39:22.7197230Z Package 'php8.3-smbclient' is not installed, so not removed
2026-05-03T00:39:22.7197631Z Package 'php-smbclient-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7197997Z Package 'php-solr' is not installed, so not removed
2026-05-03T00:39:22.7198334Z Package 'php8.3-solr' is not installed, so not removed
2026-05-03T00:39:22.7198975Z Package 'php-solr-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7199350Z Package 'php-sparkline' is not installed, so not removed
2026-05-03T00:39:22.7199722Z Package 'php-sql-formatter' is not installed, so not removed
2026-05-03T00:39:22.7200088Z Package 'php8.3-ssh2' is not installed, so not removed
2026-05-03T00:39:22.7200449Z Package 'php-ssh2-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7200804Z Package 'php8.3-stomp' is not installed, so not removed
2026-05-03T00:39:22.7201174Z Package 'php-stomp-all-dev' is not installed, so not removed
2026-05-03T00:39:22.7201554Z Package 'php-swiftmailer' is not installed, so not removed
2026-05-03T00:39:22.7201905Z Package 'php-symfony' is not installed, so not removed
2026-05-03T00:39:22.7202266Z Package 'php-symfony-asset' is not installed, so not removed
2026-05-03T00:39:22.7202679Z Package 'php-symfony-asset-mapper' is not installed, so not removed
2026-05-03T00:39:22.7203133Z Package 'php-symfony-browser-kit' is not installed, so not removed
2026-05-03T00:39:22.7203540Z Package 'php-symfony-clock' is not installed, so not removed
2026-05-03T00:39:22.7203947Z Package 'php-symfony-debug-bundle' is not installed, so not removed
2026-05-03T00:39:22.7204408Z Package 'php-symfony-doctrine-bridge' is not installed, so not removed
2026-05-03T00:39:22.7204853Z Package 'php-symfony-dom-crawler' is not installed, so not removed
2026-05-03T00:39:22.7205267Z Package 'php-symfony-dotenv' is not installed, so not removed
2026-05-03T00:39:22.7205688Z Package 'php-symfony-error-handler' is not installed, so not removed
2026-05-03T00:39:22.7206155Z Package 'php-symfony-event-dispatcher' is not installed, so not removed
2026-05-03T00:39:22.7206576Z Package 'php-symfony-form' is not installed, so not removed
2026-05-03T00:39:22.7207009Z Package 'php-symfony-framework-bundle' is not installed, so not removed
2026-05-03T00:39:22.7207459Z Package 'php-symfony-http-kernel' is not installed, so not removed
2026-05-03T00:39:22.7208013Z Package 'php-symfony-intl' is not installed, so not removed
2026-05-03T00:39:22.7208390Z Package 'php-symfony-ldap' is not installed, so not removed
2026-05-03T00:39:22.7208981Z Package 'php-symfony-lock' is not installed, so not removed
2026-05-03T00:39:22.7209502Z Package 'php-symfony-mailer' is not installed, so not removed
2026-05-03T00:39:22.7209917Z Package 'php-symfony-messenger' is not installed, so not removed
2026-05-03T00:39:22.7210315Z Package 'php-symfony-mime' is not installed, so not removed
2026-05-03T00:39:22.7210735Z Package 'php-symfony-monolog-bridge' is not installed, so not removed
2026-05-03T00:39:22.7211164Z Package 'php-symfony-notifier' is not installed, so not removed
2026-05-03T00:39:22.7211600Z Package 'php-symfony-options-resolver' is not installed, so not removed
2026-05-03T00:39:22.7212073Z Package 'php-symfony-password-hasher' is not installed, so not removed
2026-05-03T00:39:22.7212531Z Package 'php-symfony-property-access' is not installed, so not removed
2026-05-03T00:39:22.7212984Z Package 'php-symfony-property-info' is not installed, so not removed
2026-05-03T00:39:22.7213462Z Package 'php-symfony-proxy-manager-bridge' is not installed, so not removed
2026-05-03T00:39:22.7213945Z Package 'php-symfony-rate-limiter' is not installed, so not removed
2026-05-03T00:39:22.7214376Z Package 'php-symfony-remote-event' is not installed, so not removed
2026-05-03T00:39:22.7214800Z Package 'php-symfony-routing' is not installed, so not removed
2026-05-03T00:39:22.7215199Z Package 'php-symfony-scheduler' is not installed, so not removed
2026-05-03T00:39:22.7215634Z Package 'php-symfony-security-bundle' is not installed, so not removed
2026-05-03T00:39:22.7216078Z Package 'php-symfony-security-core' is not installed, so not removed
2026-05-03T00:39:22.7216517Z Package 'php-symfony-security-csrf' is not installed, so not removed
2026-05-03T00:39:22.7216957Z Package 'php-symfony-security-http' is not installed, so not removed
2026-05-03T00:39:22.7217381Z Package 'php-symfony-semaphore' is not installed, so not removed
2026-05-03T00:39:22.7217802Z Package 'php-symfony-serializer' is not installed, so not removed
2026-05-03T00:39:22.7218209Z Package 'php-symfony-stopwatch' is not installed, so not removed
2026-05-03T00:39:22.7218744Z Package 'php-symfony-string' is not installed, so not removed
2026-05-03T00:39:22.7219152Z Package 'php-symfony-templating' is not installed, so not removed
2026-05-03T00:39:22.7219575Z Package 'php-symfony-translation' is not installed, so not removed
2026-05-03T00:39:22.7220002Z Package 'php-symfony-twig-bridge' is not installed, so not removed
2026-05-03T00:39:22.7220423Z Package 'php-symfony-twig-bundle' is not installed, so not removed
2026-05-03T00:39:22.7220825Z Package 'php-symfony-uid' is not installed, so not removed
2026-05-03T00:39:22.7221216Z Package 'php-symfony-validator' is not installed, so not removed
2026-05-03T00:39:22.7221627Z Package 'php-symfony-var-dumper' is not installed, so not removed
2026-05-03T00:39:22.7222054Z Package 'php-symfony-var-exporter' is not installed, so not removed
2026-05-03T00:39:22.7222485Z Package 'php-symfony-web-link' is not installed, so not removed
2026-05-03T00:39:22.7222941Z Package 'php-symfony-web-profiler-bundle' is not installed, so not removed
2026-05-03T00:39:22.7223404Z Package 'php-symfony-webhook' is not installed, so not removed
2026-05-03T00:39:22.7223808Z Package 'php-symfony-workflow' is not installed, so not removed
2026-05-03T00:39:22.7224209Z Package 'php-symfony-contracts' is not installed, so not removed
2026-05-03T00:39:22.7224642Z Package 'php-symfony-polyfill-php83' is not installed, so not removed
2026-05-03T00:39:22.7225112Z Package 'php-symfony-all-my-sms-notifier' is not installed, so not removed
2026-05-03T00:39:22.7225588Z Package 'php-symfony-amazon-mailer' is not installed, so not removed
2026-05-03T00:39:22.7226058Z Package 'php-symfony-amazon-sns-notifier' is not installed, so not removed
2026-05-03T00:39:22.7226552Z Package 'php-symfony-amazon-sqs-messenger' is not installed, so not removed
2026-05-03T00:39:22.7227170Z Package 'php-symfony-amqp-messenger' is not installed, so not removed
2026-05-03T00:39:22.7227643Z Package 'php-symfony-bandwidth-notifier' is not installed, so not removed
2026-05-03T00:39:22.7228243Z Package 'php-symfony-beanstalkd-messenger' is not installed, so not removed
2026-05-03T00:39:22.7228845Z Package 'php-symfony-brevo-mailer' is not installed, so not removed
2026-05-03T00:39:22.7229293Z Package 'php-symfony-brevo-notifier' is not installed, so not removed
2026-05-03T00:39:22.7229753Z Package 'php-symfony-cache-contracts' is not installed, so not removed
2026-05-03T00:39:22.7230215Z Package 'php-symfony-chatwork-notifier' is not installed, so not removed
2026-05-03T00:39:22.7230704Z Package 'php-symfony-click-send-notifier' is not installed, so not removed
2026-05-03T00:39:22.7231189Z Package 'php-symfony-clickatell-notifier' is not installed, so not removed
2026-05-03T00:39:22.7231715Z Package 'php-symfony-contact-everyone-notifier' is not installed, so not removed
2026-05-03T00:39:22.7232277Z Package 'php-symfony-event-dispatcher-contracts' is not installed, so not removed
2026-05-03T00:39:22.7232821Z Package 'php-symfony-translation-contracts' is not installed, so not removed
2026-05-03T00:39:22.7233387Z Package 'php-symfony-crowdin-translation-provider' is not installed, so not removed
2026-05-03T00:39:22.7233914Z Package 'php-symfony-discord-notifier' is not installed, so not removed
2026-05-03T00:39:22.7234403Z Package 'php-symfony-doctrine-messenger' is not installed, so not removed
2026-05-03T00:39:22.7234894Z Package 'php-symfony-engagespot-notifier' is not installed, so not removed
2026-05-03T00:39:22.7235381Z Package 'php-symfony-esendex-notifier' is not installed, so not removed
2026-05-03T00:39:22.7235832Z Package 'php-symfony-expo-notifier' is not installed, so not removed
2026-05-03T00:39:22.7236291Z Package 'php-symfony-fake-chat-notifier' is not installed, so not removed
2026-05-03T00:39:22.7236763Z Package 'php-symfony-fake-sms-notifier' is not installed, so not removed
2026-05-03T00:39:22.7237239Z Package 'php-symfony-firebase-notifier' is not installed, so not removed
2026-05-03T00:39:22.7237742Z Package 'php-symfony-forty-six-elks-notifier' is not installed, so not removed
2026-05-03T00:39:22.7238450Z Package 'php-symfony-free-mobile-notifier' is not installed, so not removed
2026-05-03T00:39:22.7239331Z Package 'php-symfony-gateway-api-notifier' is not installed, so not removed
2026-05-03T00:39:22.7239820Z Package 'php-symfony-gitter-notifier' is not installed, so not removed
2026-05-03T00:39:22.7240576Z Package 'php-symfony-go-ip-notifier' is not installed, so not removed
2026-05-03T00:39:22.7241185Z Package 'php-symfony-google-chat-notifier' is not installed, so not removed
2026-05-03T00:39:22.7241853Z Package 'php-symfony-google-mailer' is not installed, so not removed
2026-05-03T00:39:22.7242533Z Package 'php-symfony-html-sanitizer' is not installed, so not removed
2026-05-03T00:39:22.7243228Z Package 'php-symfony-infobip-mailer' is not installed, so not removed
2026-05-03T00:39:22.7243983Z Package 'php-symfony-infobip-notifier' is not installed, so not removed
2026-05-03T00:39:22.7244716Z Package 'php-symfony-iqsms-notifier' is not installed, so not removed
2026-05-03T00:39:22.7245468Z Package 'php-symfony-isendpro-notifier' is not installed, so not removed
2026-05-03T00:39:22.7245976Z Package 'php-symfony-kaz-info-teh-notifier' is not installed, so not removed
2026-05-03T00:39:22.7246476Z Package 'php-symfony-light-sms-notifier' is not installed, so not removed
2026-05-03T00:39:22.7246984Z Package 'php-symfony-line-notify-notifier' is not installed, so not removed
2026-05-03T00:39:22.7247474Z Package 'php-symfony-linked-in-notifier' is not installed, so not removed
2026-05-03T00:39:22.7248000Z Package 'php-symfony-loco-translation-provider' is not installed, so not removed
2026-05-03T00:39:22.7248571Z Package 'php-symfony-lokalise-translation-provider' is not installed, so not removed
2026-05-03T00:39:22.7249560Z Package 'php-symfony-mail-pace-mailer' is not installed, so not removed
2026-05-03T00:39:22.7250240Z Package 'php-symfony-mailchimp-mailer' is not installed, so not removed
2026-05-03T00:39:22.7250713Z Package 'php-symfony-mailer-send-mailer' is not installed, so not removed
2026-05-03T00:39:22.7251295Z Package 'php-symfony-mailgun-mailer' is not installed, so not removed
2026-05-03T00:39:22.7251756Z Package 'php-symfony-mailjet-mailer' is not installed, so not removed
2026-05-03T00:39:22.7252221Z Package 'php-symfony-mailjet-notifier' is not installed, so not removed
2026-05-03T00:39:22.7252697Z Package 'php-symfony-mastodon-notifier' is not installed, so not removed
2026-05-03T00:39:22.7253189Z Package 'php-symfony-mattermost-notifier' is not installed, so not removed
2026-05-03T00:39:22.7253647Z Package 'php-symfony-mercure' is not installed, so not removed
2026-05-03T00:39:22.7254072Z Package 'php-symfony-mercure-bundle' is not installed, so not removed
2026-05-03T00:39:22.7254535Z Package 'php-symfony-mercure-notifier' is not installed, so not removed
2026-05-03T00:39:22.7255028Z Package 'php-symfony-message-bird-notifier' is not installed, so not removed
2026-05-03T00:39:22.7255549Z Package 'php-symfony-message-media-notifier' is not installed, so not removed
2026-05-03T00:39:22.7256085Z Package 'php-symfony-microsoft-teams-notifier' is not installed, so not removed
2026-05-03T00:39:22.7256577Z Package 'php-symfony-mobyt-notifier' is not installed, so not removed
2026-05-03T00:39:22.7257024Z Package 'php-symfony-novu-notifier' is not installed, so not removed
2026-05-03T00:39:22.7257464Z Package 'php-symfony-ntfy-notifier' is not installed, so not removed
2026-05-03T00:39:22.7257926Z Package 'php-symfony-octopush-notifier' is not installed, so not removed
2026-05-03T00:39:22.7258401Z Package 'php-symfony-oh-my-smtp-mailer' is not installed, so not removed
2026-05-03T00:39:22.7259139Z Package 'php-symfony-one-signal-notifier' is not installed, so not removed
2026-05-03T00:39:22.7259645Z Package 'php-symfony-orange-sms-notifier' is not installed, so not removed
2026-05-03T00:39:22.7260135Z Package 'php-symfony-ovh-cloud-notifier' is not installed, so not removed
2026-05-03T00:39:22.7260626Z Package 'php-symfony-pager-duty-notifier' is not installed, so not removed
2026-05-03T00:39:22.7261100Z Package 'php-symfony-phpunit-bridge' is not installed, so not removed
2026-05-03T00:39:22.7261622Z Package 'php-symfony-phrase-translation-provider' is not installed, so not removed
2026-05-03T00:39:22.7262149Z Package 'php-symfony-plivo-notifier' is not installed, so not removed
2026-05-03T00:39:22.7262587Z Package 'php-symfony-polyfill' is not installed, so not removed
2026-05-03T00:39:22.7263026Z Package 'php-symfony-polyfill-apcu' is not installed, so not removed
2026-05-03T00:39:22.7263489Z Package 'php-symfony-polyfill-ctype' is not installed, so not removed
2026-05-03T00:39:22.7263944Z Package 'php-symfony-polyfill-php72' is not installed, so not removed
2026-05-03T00:39:22.7264391Z Package 'php-symfony-polyfill-php73' is not installed, so not removed
2026-05-03T00:39:22.7264844Z Package 'php-symfony-polyfill-php74' is not installed, so not removed
2026-05-03T00:39:22.7265295Z Package 'php-symfony-polyfill-php81' is not installed, so not removed
2026-05-03T00:39:22.7265743Z Package 'php-symfony-polyfill-php82' is not installed, so not removed
2026-05-03T00:39:22.7266186Z Package 'php-symfony-polyfill-iconv' is not installed, so not removed
2026-05-03T00:39:22.7266666Z Package 'php-symfony-polyfill-intl-grapheme' is not installed, so not removed
2026-05-03T00:39:22.7267175Z Package 'php-symfony-polyfill-intl-icu' is not installed, so not removed
2026-05-03T00:39:22.7267708Z Package 'php-symfony-polyfill-intl-messageformatter' is not installed, so not removed
2026-05-03T00:39:22.7268256Z Package 'php-symfony-polyfill-intl-idn' is not installed, so not removed
2026-05-03T00:39:22.7268986Z Package 'php-symfony-polyfill-intl-normalizer' is not installed, so not removed
2026-05-03T00:39:22.7269504Z Package 'php-symfony-polyfill-mbstring' is not installed, so not removed
2026-05-03T00:39:22.7270118Z Package 'php-symfony-polyfill-util' is not installed, so not removed
2026-05-03T00:39:22.7270558Z Package 'php-symfony-polyfill-xml' is not installed, so not removed
2026-05-03T00:39:22.7271109Z Package 'php-symfony-polyfill-uuid' is not installed, so not removed
2026-05-03T00:39:22.7271564Z Package 'php-symfony-postmark-mailer' is not installed, so not removed
2026-05-03T00:39:22.7272067Z Package 'php-symfony-psr-http-message-bridge' is not installed, so not removed
2026-05-03T00:39:22.7272573Z Package 'php-symfony-pushover-notifier' is not installed, so not removed
2026-05-03T00:39:22.7273033Z Package 'php-symfony-redis-messenger' is not installed, so not removed
2026-05-03T00:39:22.7273498Z Package 'php-symfony-redlink-notifier' is not installed, so not removed
2026-05-03T00:39:22.7273983Z Package 'php-symfony-ring-central-notifier' is not installed, so not removed
2026-05-03T00:39:22.7274501Z Package 'php-symfony-rocket-chat-notifier' is not installed, so not removed
2026-05-03T00:39:22.7274959Z Package 'php-symfony-runtime' is not installed, so not removed
2026-05-03T00:39:22.7275390Z Package 'php-symfony-scaleway-mailer' is not installed, so not removed
2026-05-03T00:39:22.7275849Z Package 'php-symfony-security-acl' is not installed, so not removed
2026-05-03T00:39:22.7276312Z Package 'php-symfony-sendberry-notifier' is not installed, so not removed
2026-05-03T00:39:22.7276784Z Package 'php-symfony-sendgrid-mailer' is not installed, so not removed
2026-05-03T00:39:22.7277248Z Package 'php-symfony-sendinblue-mailer' is not installed, so not removed
2026-05-03T00:39:22.7277737Z Package 'php-symfony-sendinblue-notifier' is not installed, so not removed
2026-05-03T00:39:22.7278238Z Package 'php-symfony-simple-textin-notifier' is not installed, so not removed
2026-05-03T00:39:22.7278986Z Package 'php-symfony-sinch-notifier' is not installed, so not removed
2026-05-03T00:39:22.7279449Z Package 'php-symfony-slack-notifier' is not installed, so not removed
2026-05-03T00:39:22.7279921Z Package 'php-symfony-sms-biuras-notifier' is not installed, so not removed
2026-05-03T00:39:22.7280413Z Package 'php-symfony-sms-factor-notifier' is not installed, so not removed
2026-05-03T00:39:22.7281167Z Package 'php-symfony-sms77-notifier' is not installed, so not removed
2026-05-03T00:39:22.7301071Z Package 'php-symfony-smsapi-notifier' is not installed, so not removed
2026-05-03T00:39:22.7301595Z Package 'php-symfony-smsc-notifier' is not installed, so not removed
2026-05-03T00:39:22.7302085Z Package 'php-symfony-smsmode-notifier' is not installed, so not removed
2026-05-03T00:39:22.7302580Z Package 'php-symfony-spot-hit-notifier' is not installed, so not removed
2026-05-03T00:39:22.7303068Z Package 'php-symfony-telegram-notifier' is not installed, so not removed
2026-05-03T00:39:22.7303543Z Package 'php-symfony-telnyx-notifier' is not installed, so not removed
2026-05-03T00:39:22.7304000Z Package 'php-symfony-termii-notifier' is not installed, so not removed
2026-05-03T00:39:22.7304477Z Package 'php-symfony-turbo-sms-notifier' is not installed, so not removed
2026-05-03T00:39:22.7304980Z Package 'php-symfony-twilio-notifier' is not installed, so not removed
2026-05-03T00:39:22.7305442Z Package 'php-symfony-twitter-notifier' is not installed, so not removed
2026-05-03T00:39:22.7305916Z Package 'php-symfony-vonage-notifier' is not installed, so not removed
2026-05-03T00:39:22.7306379Z Package 'php-symfony-yunpian-notifier' is not installed, so not removed
2026-05-03T00:39:22.7306853Z Package 'php-symfony-zendesk-notifier' is not installed, so not removed
2026-05-03T00:39:22.7307316Z Package 'php-symfony-zulip-notifier' is not installed, so not removed
2026-05-03T00:39:22.7307748Z Package 'php-text-captcha' is not installed, so not removed
2026-05-03T00:39:22.7308148Z Package 'php-text-password' is not installed, so not removed
2026-05-03T00:39:22.7308530Z Package 'php-text-figlet' is not installed, so not removed
2026-05-03T00:39:22.7309094Z Package 'php-text-languagedetect' is not installed, so not removed
2026-05-03T00:39:22.7309718Z Package 'php-text-wiki' is not installed, so not removed
2026-05-03T00:39:22.7310079Z Package 'php-thrift' is not installed, so not removed
2026-05-03T00:39:22.7310436Z Package 'php8.3-tideways' is not installed, so not removed
2026-05-03T00:39:22.7311010Z Package 'php-tideways-all-dev' is not installed, so not removed
2026-05-03T00:39:22.8670782Z Package 'php-tijsverkoyen-css-to-inline-styles' is not installed, so not removed
2026-05-03T00:39:22.8671612Z Package 'php-timer' is not installed, so not removed
2026-05-03T00:39:22.8672182Z Package 'php-twig-doc' is not installed, so not removed
2026-05-03T00:39:22.8672666Z Package 'php-twig-cache-extra' is not installed, so not removed
2026-05-03T00:39:22.8673117Z Package 'php-twig-cssinliner-extra' is not installed, so not removed
2026-05-03T00:39:22.8673536Z Package 'php-twig-extra-bundle' is not installed, so not removed
2026-05-03T00:39:22.8673943Z Package 'php-twig-html-extra' is not installed, so not removed
2026-05-03T00:39:22.8674356Z Package 'php-twig-i18n-extension' is not installed, so not removed
2026-05-03T00:39:22.8674779Z Package 'php-twig-inky-extra' is not installed, so not removed
2026-05-03T00:39:22.8675170Z Package 'php-twig-intl-extra' is not installed, so not removed
2026-05-03T00:39:22.8675565Z Package 'php-twig-markdown-extra' is not installed, so not removed
2026-05-03T00:39:22.8675992Z Package 'php-twig-string-extra' is not installed, so not removed
2026-05-03T00:39:22.8676359Z Package 'php8.3-uopz' is not installed, so not removed
2026-05-03T00:39:22.8676713Z Package 'php-uopz-all-dev' is not installed, so not removed
2026-05-03T00:39:22.8677088Z Package 'php8.3-uploadprogress' is not installed, so not removed
2026-05-03T00:39:22.8677518Z Package 'php-uploadprogress-all-dev' is not installed, so not removed
2026-05-03T00:39:22.8677914Z Package 'php8.3-uuid' is not installed, so not removed
2026-05-03T00:39:22.8678258Z Package 'php-uuid-all-dev' is not installed, so not removed
2026-05-03T00:39:22.8679014Z Package 'php-validate' is not installed, so not removed
2026-05-03T00:39:22.8679633Z Package 'php-vlucas-phpdotenv' is not installed, so not removed
2026-05-03T00:39:22.8680140Z Package 'php-voku-portable-ascii' is not installed, so not removed
2026-05-03T00:39:22.8680768Z Package 'php-wmerrors' is not installed, so not removed
2026-05-03T00:39:22.8681374Z Package 'php-xdebug-all-dev' is not installed, so not removed
2026-05-03T00:39:22.8681796Z Package 'php-xml-svg' is not installed, so not removed
2026-05-03T00:39:22.8682135Z Package 'php8.3-xmlrpc' is not installed, so not removed
2026-05-03T00:39:22.8682499Z Package 'php-xmlrpc-all-dev' is not installed, so not removed
2026-05-03T00:39:22.8682856Z Package 'php8.3-yac' is not installed, so not removed
2026-05-03T00:39:22.8683485Z Package 'php-yac-all-dev' is not installed, so not removed
2026-05-03T00:39:22.8684074Z Package 'php-yaml-all-dev' is not installed, so not removed
2026-05-03T00:39:22.8684450Z Package 'php-zend-code' is not installed, so not removed
2026-05-03T00:39:22.8684816Z Package 'php-zend-eventmanager' is not installed, so not removed
2026-05-03T00:39:22.8685200Z Package 'php-zend-stdlib' is not installed, so not removed
2026-05-03T00:39:22.8685558Z Package 'php-zeroc-ice' is not installed, so not removed
2026-05-03T00:39:22.8685896Z Package 'php-zeta-base' is not installed, so not removed
2026-05-03T00:39:22.8686279Z Package 'php-zeta-console-tools' is not installed, so not removed
2026-05-03T00:39:22.8686676Z Package 'php-zeta-unit-test' is not installed, so not removed
2026-05-03T00:39:22.8687045Z Package 'php-zmq-all-dev' is not installed, so not removed
2026-05-03T00:39:22.8687444Z Package 'php-zumba-json-serializer' is not installed, so not removed
2026-05-03T00:39:22.8687863Z Package 'php8.3-libvirt-php' is not installed, so not removed
2026-05-03T00:39:22.8688206Z Package 'phpab' is not installed, so not removed
2026-05-03T00:39:22.8688506Z Package 'phpcpd' is not installed, so not removed
2026-05-03T00:39:22.8689134Z Package 'phpunit-cli-parser' is not installed, so not removed
2026-05-03T00:39:22.8689829Z Package 'phpldapadmin' is not installed, so not removed
2026-05-03T00:39:22.8690168Z Package 'phpliteadmin' is not installed, so not removed
2026-05-03T00:39:22.8690709Z Package 'phpliteadmin-themes' is not installed, so not removed
2026-05-03T00:39:22.8691066Z Package 'phploc' is not installed, so not removed
2026-05-03T00:39:22.8691375Z Package 'phppgadmin' is not installed, so not removed
2026-05-03T00:39:22.8691696Z Package 'phpsysinfo' is not installed, so not removed
2026-05-03T00:39:22.8692044Z Package 'phpunit-code-unit' is not installed, so not removed
2026-05-03T00:39:22.8692389Z Package 'phpunit-diff' is not installed, so not removed
2026-05-03T00:39:22.8692743Z Package 'phpunit-exporter' is not installed, so not removed
2026-05-03T00:39:22.8693116Z Package 'phpunit-global-state' is not installed, so not removed
2026-05-03T00:39:22.8693526Z Package 'phpunit-object-enumerator' is not installed, so not removed
2026-05-03T00:39:22.8693967Z Package 'phpunit-resource-operations' is not installed, so not removed
2026-05-03T00:39:22.8694358Z Package 'phpunit-type' is not installed, so not removed
2026-05-03T00:39:22.8694737Z Package 'phpunit-object-reflector' is not installed, so not removed
2026-05-03T00:39:22.8695127Z Package 'phpwebcounter' is not installed, so not removed
2026-05-03T00:39:22.8695494Z Package 'phpwebcounter-extra' is not installed, so not removed
2026-05-03T00:39:22.8695871Z Package 'python3-phply' is not installed, so not removed
2026-05-03T00:39:22.8696245Z Package 'python3-phpserialize' is not installed, so not removed
2026-05-03T00:39:22.8696674Z Package 'python3-sphinxcontrib.phpdomain' is not installed, so not removed
2026-05-03T00:39:22.8697091Z Package 'simplesamlphp' is not installed, so not removed
2026-05-03T00:39:22.8697431Z Package 'slbackup-php' is not installed, so not removed
2026-05-03T00:39:22.8697787Z Package 'uwsgi-plugin-php' is not installed, so not removed
2026-05-03T00:39:22.8698147Z Package 'weechat-php' is not installed, so not removed
2026-05-03T00:39:22.8698482Z Package 'php-mythtv' is not installed, so not removed
2026-05-03T00:39:22.8698958Z Package 'mono-devel' is not installed, so not removed
2026-05-03T00:39:22.8699251Z The following packages will be REMOVED:
2026-05-03T00:39:22.8699670Z   azure-cli clang-16 clang-17 clang-18 clang-tidy-16 clang-tidy-17
2026-05-03T00:39:22.8700084Z   clang-tidy-18 clang-tools-16 clang-tools-17 clang-tools-18 firefox
2026-05-03T00:39:22.8700528Z   google-chrome-stable google-cloud-cli google-cloud-cli-anthoscli llvm-16
2026-05-03T00:39:22.8700997Z   llvm-16-dev llvm-16-linker-tools llvm-16-runtime llvm-16-tools llvm-17
2026-05-03T00:39:22.8701429Z   llvm-17-dev llvm-17-linker-tools llvm-17-runtime llvm-17-tools llvm-18
2026-05-03T00:39:22.8701880Z   llvm-18-dev llvm-18-linker-tools llvm-18-runtime llvm-18-tools php-common
2026-05-03T00:39:22.8702358Z   php-pear php8.3 php8.3-amqp php8.3-apcu php8.3-bcmath php8.3-bz2 php8.3-cgi
2026-05-03T00:39:22.8702845Z   php8.3-cli php8.3-common php8.3-curl php8.3-dba php8.3-dev php8.3-enchant
2026-05-03T00:39:22.8703308Z   php8.3-fpm php8.3-gd php8.3-gmp php8.3-igbinary php8.3-imagick php8.3-imap
2026-05-03T00:39:22.8703768Z   php8.3-interbase php8.3-intl php8.3-ldap php8.3-mbstring php8.3-memcache
2026-05-03T00:39:22.8704230Z   php8.3-memcached php8.3-mongodb php8.3-msgpack php8.3-mysql php8.3-odbc
2026-05-03T00:39:22.8704667Z   php8.3-opcache php8.3-pcov php8.3-pgsql php8.3-phpdbg php8.3-pspell
2026-05-03T00:39:22.8705102Z   php8.3-readline php8.3-redis php8.3-snmp php8.3-soap php8.3-sqlite3
2026-05-03T00:39:22.8705535Z   php8.3-sybase php8.3-tidy php8.3-xdebug php8.3-xml php8.3-xsl php8.3-yaml
2026-05-03T00:39:22.8705897Z   php8.3-zip php8.3-zmq powershell
2026-05-03T00:39:23.3299484Z 0 upgraded, 0 newly installed, 78 to remove and 5 not upgraded.
2026-05-03T00:39:23.3300197Z After this operation, 3857 MB disk space will be freed.
2026-05-03T00:39:23.3890292Z (Reading database ... 
2026-05-03T00:39:23.3890712Z (Reading database ... 5%
2026-05-03T00:39:23.3891405Z (Reading database ... 10%
2026-05-03T00:39:23.3891747Z (Reading database ... 15%
2026-05-03T00:39:23.3892207Z (Reading database ... 20%
2026-05-03T00:39:23.3892538Z (Reading database ... 25%
2026-05-03T00:39:23.3893083Z (Reading database ... 30%
2026-05-03T00:39:23.3893422Z (Reading database ... 35%
2026-05-03T00:39:23.3893756Z (Reading database ... 40%
2026-05-03T00:39:23.3894097Z (Reading database ... 45%
2026-05-03T00:39:23.3894359Z (Reading database ... 50%
2026-05-03T00:39:23.4009551Z (Reading database ... 55%
2026-05-03T00:39:23.5141729Z (Reading database ... 60%
2026-05-03T00:39:23.6663208Z (Reading database ... 65%
2026-05-03T00:39:23.8584162Z (Reading database ... 70%
2026-05-03T00:39:24.0589536Z (Reading database ... 75%
2026-05-03T00:39:24.2163876Z (Reading database ... 80%
2026-05-03T00:39:24.3590206Z (Reading database ... 85%
2026-05-03T00:39:24.4919635Z (Reading database ... 90%
2026-05-03T00:39:24.6164448Z (Reading database ... 95%
2026-05-03T00:39:24.6165039Z (Reading database ... 100%
2026-05-03T00:39:24.6165727Z (Reading database ... 220762 files and directories currently installed.)
2026-05-03T00:39:24.6208112Z Removing azure-cli (2.85.0-1~noble) ...
2026-05-03T00:39:29.2732563Z Removing clang-tidy-16 (1:16.0.6-23ubuntu4) ...
2026-05-03T00:39:29.2994948Z Removing clang-tools-16 (1:16.0.6-23ubuntu4) ...
2026-05-03T00:39:29.3404275Z Removing clang-16 (1:16.0.6-23ubuntu4) ...
2026-05-03T00:39:29.3580050Z Removing clang-tidy-17 (1:17.0.6-9ubuntu1) ...
2026-05-03T00:39:29.3765204Z Removing clang-tools-17 (1:17.0.6-9ubuntu1) ...
2026-05-03T00:39:29.4100055Z Removing clang-17 (1:17.0.6-9ubuntu1) ...
2026-05-03T00:39:29.4307196Z Removing clang-tidy-18 (1:18.1.3-1ubuntu1) ...
2026-05-03T00:39:29.4537502Z Removing clang-tools-18 (1:18.1.3-1ubuntu1) ...
2026-05-03T00:39:29.4964413Z Removing clang-18 (1:18.1.3-1ubuntu1) ...
2026-05-03T00:39:29.5136378Z Removing firefox (149.0.2+build1-0ubuntu0.24.04.1~mt1) ...
2026-05-03T00:39:29.6202913Z Removing google-chrome-stable (147.0.7727.55-1) ...
2026-05-03T00:39:29.8022057Z Removing google-cloud-cli-anthoscli (564.0.0-0) ...
2026-05-03T00:39:40.0138962Z Removing google-cloud-cli (564.0.0-0) ...
2026-05-03T00:40:44.5990250Z Removing llvm-16-dev (1:16.0.6-23ubuntu4) ...
2026-05-03T00:40:44.8376857Z Removing llvm-16 (1:16.0.6-23ubuntu4) ...
2026-05-03T00:40:44.8644893Z Removing llvm-16-linker-tools (1:16.0.6-23ubuntu4) ...
2026-05-03T00:40:44.8812212Z Removing llvm-16-runtime (1:16.0.6-23ubuntu4) ...
2026-05-03T00:40:44.9082545Z Removing llvm-16-tools (1:16.0.6-23ubuntu4) ...
2026-05-03T00:40:45.0304412Z Removing llvm-17-dev (1:17.0.6-9ubuntu1) ...
2026-05-03T00:40:45.2452934Z Removing llvm-17 (1:17.0.6-9ubuntu1) ...
2026-05-03T00:40:45.2722020Z Removing llvm-17-linker-tools (1:17.0.6-9ubuntu1) ...
2026-05-03T00:40:45.2868000Z Removing llvm-17-runtime (1:17.0.6-9ubuntu1) ...
2026-05-03T00:40:45.3165075Z Removing llvm-17-tools (1:17.0.6-9ubuntu1) ...
2026-05-03T00:40:45.4315950Z Removing llvm-18-dev (1:18.1.3-1ubuntu1) ...
2026-05-03T00:40:45.6707512Z Removing llvm-18 (1:18.1.3-1ubuntu1) ...
2026-05-03T00:40:45.6946656Z Removing llvm-18-linker-tools (1:18.1.3-1ubuntu1) ...
2026-05-03T00:40:45.7141529Z Removing llvm-18-runtime (1:18.1.3-1ubuntu1) ...
2026-05-03T00:40:45.7446709Z Removing llvm-18-tools (1:18.1.3-1ubuntu1) ...
2026-05-03T00:40:45.8696441Z Removing php8.3-zip (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:46.0494456Z Removing php8.3-sybase (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:46.1870832Z Removing php-pear (1:1.10.13+submodules+notgz+2022032202-2build1) ...
2026-05-03T00:40:46.2890839Z Removing php8.3 (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:46.3086985Z Removing php8.3-amqp (1.11.0-5ubuntu1) ...
2026-05-03T00:40:46.4394226Z Removing php8.3-apcu (5.1.22+4.0.11-2ubuntu1) ...
2026-05-03T00:40:46.5617155Z Removing php8.3-bcmath (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:46.6934125Z Removing php8.3-bz2 (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:46.8182421Z Removing php8.3-zmq (1.1.3-24ubuntu1) ...
2026-05-03T00:40:46.9492901Z Removing php8.3-yaml (2.2.2+2.1.0+2.0.4+1.3.2-6ubuntu1) ...
2026-05-03T00:40:47.0716025Z Removing php8.3-cgi (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:48.8233300Z apache2_invoke php8.3-cgi prerm: No action required
2026-05-03T00:40:48.8502210Z Removing php8.3-dev (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:48.9466435Z Removing php8.3-xdebug (3.2.0+3.1.6+2.9.8+2.8.1+2.5.5-3ubuntu1) ...
2026-05-03T00:40:49.0509387Z Removing php8.3-phpdbg (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:50.4896430Z Removing php8.3-redis (5.3.7+4.3.0-3ubuntu1) ...
2026-05-03T00:40:50.5690515Z Removing php8.3-xsl (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:50.5832558Z Removing php8.3-soap (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:50.6779607Z Removing php8.3-curl (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:50.7592164Z Removing php8.3-dba (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:50.8397856Z Removing php8.3-enchant (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:50.9243950Z Removing php8.3-pcov (1.0.11-5ubuntu1) ...
2026-05-03T00:40:50.9924279Z Removing php8.3-fpm (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:52.3638842Z apache2_invoke php8.3-fpm prerm: No action required
2026-05-03T00:40:52.3971109Z Removing php8.3-gd (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:52.4623545Z Removing php8.3-gmp (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:52.5275674Z Removing php8.3-memcached (3.2.0+2.2.0-4ubuntu3) ...
2026-05-03T00:40:52.5866072Z Removing php8.3-igbinary (3.2.13-1ubuntu3) ...
2026-05-03T00:40:52.6503140Z Removing php8.3-imagick (3.7.0-4ubuntu3) ...
2026-05-03T00:40:52.7102231Z Removing php8.3-imap (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:52.7693988Z Removing php8.3-interbase (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:52.8381436Z Removing php8.3-intl (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:52.9023919Z Removing php8.3-ldap (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:52.9669194Z Removing php8.3-mbstring (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:53.0375072Z Removing php8.3-memcache (8.0+4.0.5.2+3.0.9~20170802.e702b5f9+-8ubuntu1) ...
2026-05-03T00:40:53.0963745Z Removing php8.3-mongodb (1.15.0+1.11.1+1.9.2+1.7.5-1ubuntu3) ...
2026-05-03T00:40:53.1558550Z Removing php8.3-msgpack (1:2.2.0~rc2-3ubuntu1) ...
2026-05-03T00:40:53.2166428Z Removing php8.3-mysql (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:53.3451549Z Removing php8.3-odbc (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:53.4389686Z Removing php8.3-pgsql (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:53.5346537Z Removing php8.3-pspell (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:53.6001015Z Removing php8.3-snmp (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:53.6668310Z Removing php8.3-sqlite3 (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:53.7601125Z Removing php8.3-tidy (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:53.8195441Z Removing php8.3-xml (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:54.0400844Z Removing powershell (7.4.14-1.deb) ...
2026-05-03T00:40:54.2109437Z Removing php8.3-cli (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:54.7426479Z Removing php8.3-opcache (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:54.7838214Z Removing php8.3-readline (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:54.8330832Z Removing php8.3-common (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:55.0039395Z Removing php-common (2:93ubuntu2) ...
2026-05-03T00:40:55.0348095Z Stopping 'phpsessionclean.service', but its triggering units are still active:
2026-05-03T00:40:55.0349968Z 
2026-05-03T00:40:55.0350465Z phpsessionclean.timer
2026-05-03T00:40:55.0351070Z 
2026-05-03T00:40:55.6015885Z Processing triggers for libc-bin (2.39-0ubuntu8.7) ...
2026-05-03T00:40:55.6316652Z Processing triggers for systemd (255.4-1ubuntu8.15) ...
2026-05-03T00:40:55.6645870Z Processing triggers for man-db (2.12.0-4build2) ...
2026-05-03T00:40:55.6670301Z Not building database; man-db/auto-update is not 'true'.
2026-05-03T00:40:55.6684843Z Processing triggers for hicolor-icon-theme (0.17-2) ...
2026-05-03T00:40:56.9409893Z Reading package lists...
2026-05-03T00:40:57.1157185Z Building dependency tree...
2026-05-03T00:40:57.1164980Z Reading state information...
2026-05-03T00:40:57.2767922Z The following packages will be REMOVED:
2026-05-03T00:40:57.2769130Z   dictionaries-common emacsen-common firebird3.0-common firebird3.0-common-doc
2026-05-03T00:40:57.2770726Z   freetds-common hunspell-en-us icu-devtools imagemagick-6-common lib32gcc-s1
2026-05-03T00:40:57.2771840Z   lib32stdc++6 libaom3 libaspell15 libc-client2007e libc6-i386 libcanberra0t64
2026-05-03T00:40:57.2772868Z   libclang-common-16-dev libclang-common-17-dev libclang-common-18-dev
2026-05-03T00:40:57.2773834Z   libclang-rt-16-dev libclang-rt-17-dev libclang-rt-18-dev libclang1-16t64
2026-05-03T00:40:57.2774766Z   libclang1-17t64 libdbusmenu-glib4 libdbusmenu-gtk3-4 libde265-0
2026-05-03T00:40:57.2775658Z   libenchant-2-2 libfbclient2 libffi-dev libfftw3-double3 libgc1 libgd3
2026-05-03T00:40:57.2776650Z   libhashkit2t64 libheif-plugin-aomdec libheif-plugin-libde265 libheif1
2026-05-03T00:40:57.2777612Z   libhunspell-1.7-0 libicu-dev liblldb-16t64 liblldb-17t64 liblqr-1-0
2026-05-03T00:40:57.2778527Z   libmagickcore-6.q16-7t64 libmagickwand-6.q16-7t64 libmemcached11t64
2026-05-03T00:40:57.2779738Z   libncurses-dev libnorm1t64 libobjc-13-dev libobjc4 libogg0 libopenjp2-7
2026-05-03T00:40:57.2780406Z   libpcre2-16-0 libpcre2-32-0 libpcre2-dev libpcre2-posix3 libpfm4
2026-05-03T00:40:57.2780864Z   libpgm-5.3-0t64 libqdbm14t64 librabbitmq4 libraw23t64 libsnappy1v5 libsybdb5
2026-05-03T00:40:57.2781345Z   libtdb1 libtidy5deb1 libtommath1 libvorbis0a libvorbisfile3 libwebpdemux2
2026-05-03T00:40:57.2781807Z   libwebpmux3 libxml2-dev libz3-4 libz3-dev libzip4t64 libzmq5 mlock shtool
2026-05-03T00:40:57.2782185Z   sound-theme-freedesktop xul-ext-ubufox
2026-05-03T00:40:57.5007243Z 0 upgraded, 0 newly installed, 77 to remove and 5 not upgraded.
2026-05-03T00:40:57.5007841Z After this operation, 389 MB disk space will be freed.
2026-05-03T00:40:57.5173506Z (Reading database ... 
2026-05-03T00:40:57.5174435Z (Reading database ... 5%
2026-05-03T00:40:57.5175311Z (Reading database ... 10%
2026-05-03T00:40:57.5175658Z (Reading database ... 15%
2026-05-03T00:40:57.5175989Z (Reading database ... 20%
2026-05-03T00:40:57.5176308Z (Reading database ... 25%
2026-05-03T00:40:57.5176632Z (Reading database ... 30%
2026-05-03T00:40:57.5176970Z (Reading database ... 35%
2026-05-03T00:40:57.5177294Z (Reading database ... 40%
2026-05-03T00:40:57.5177614Z (Reading database ... 45%
2026-05-03T00:40:57.5177940Z (Reading database ... 50%
2026-05-03T00:40:57.5178266Z (Reading database ... 55%
2026-05-03T00:40:57.5208917Z (Reading database ... 60%
2026-05-03T00:40:57.5298304Z (Reading database ... 65%
2026-05-03T00:40:57.5320711Z (Reading database ... 70%
2026-05-03T00:40:57.5364092Z (Reading database ... 75%
2026-05-03T00:40:57.5383859Z (Reading database ... 80%
2026-05-03T00:40:57.5408249Z (Reading database ... 85%
2026-05-03T00:40:57.5432104Z (Reading database ... 90%
2026-05-03T00:40:57.5525943Z (Reading database ... 95%
2026-05-03T00:40:57.5526394Z (Reading database ... 100%
2026-05-03T00:40:57.5527037Z (Reading database ... 122759 files and directories currently installed.)
2026-05-03T00:40:57.5546623Z Removing libenchant-2-2:amd64 (2.3.3-2build2) ...
2026-05-03T00:40:57.5692183Z Removing hunspell-en-us (1:2020.12.07-2) ...
2026-05-03T00:40:57.6219473Z Removing dictionaries-common (1.29.7) ...
2026-05-03T00:40:57.6785256Z Removing 'diversion of /usr/share/dict/words to /usr/share/dict/words.pre-dictionaries-common by dictionaries-common'
2026-05-03T00:40:57.6966610Z Removing emacsen-common (3.0.5) ...
2026-05-03T00:40:57.7386006Z Removing libfbclient2:amd64 (3.0.11.33703.ds4-2ubuntu2) ...
2026-05-03T00:40:57.7549926Z Removing firebird3.0-common (3.0.11.33703.ds4-2ubuntu2) ...
2026-05-03T00:40:57.7757322Z Removing firebird3.0-common-doc (3.0.11.33703.ds4-2ubuntu2) ...
2026-05-03T00:40:57.7879002Z Removing libsybdb5:amd64 (1.3.17+ds-2build3) ...
2026-05-03T00:40:57.8061227Z Removing freetds-common (1.3.17+ds-2build3) ...
2026-05-03T00:40:57.8295627Z Removing libxml2-dev:amd64 (2.9.14+dfsg-1.3ubuntu3.7) ...
2026-05-03T00:40:57.8502653Z Removing libicu-dev:amd64 (74.2-1ubuntu3.1) ...
2026-05-03T00:40:57.8865717Z Removing icu-devtools (74.2-1ubuntu3.1) ...
2026-05-03T00:40:57.9001019Z Removing libmagickwand-6.q16-7t64:amd64 (8:6.9.12.98+dfsg1-5.2build2) ...
2026-05-03T00:40:57.9208325Z Removing libmagickcore-6.q16-7t64:amd64 (8:6.9.12.98+dfsg1-5.2build2) ...
2026-05-03T00:40:57.9554947Z Removing imagemagick-6-common (8:6.9.12.98+dfsg1-5.2build2) ...
2026-05-03T00:40:57.9665802Z Removing libclang-rt-18-dev:amd64 (1:18.1.3-1ubuntu1) ...
2026-05-03T00:40:57.9921256Z Removing libclang-rt-16-dev:amd64 (1:16.0.6-23ubuntu4) ...
2026-05-03T00:40:58.0140065Z Removing lib32stdc++6 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:58.0273880Z Removing lib32gcc-s1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:58.0422728Z Removing libaspell15:amd64 (0.60.8.1-1build1) ...
2026-05-03T00:40:58.0698559Z Removing libc-client2007e (8:2007f~dfsg-7build3) ...
2026-05-03T00:40:58.0835825Z Removing libc6-i386 (2.39-0ubuntu8.7) ...
2026-05-03T00:40:58.1223911Z Removing libcanberra0t64:amd64 (0.30-10ubuntu10) ...
2026-05-03T00:40:58.1356286Z Removing libclang-common-16-dev (1:16.0.6-23ubuntu4) ...
2026-05-03T00:40:58.1608276Z Removing libclang-common-17-dev:amd64 (1:17.0.6-9ubuntu1) ...
2026-05-03T00:40:58.1875428Z Removing libclang-common-18-dev:amd64 (1:18.1.3-1ubuntu1) ...
2026-05-03T00:40:58.2140266Z Removing libclang-rt-17-dev:amd64 (1:17.0.6-9ubuntu1) ...
2026-05-03T00:40:58.2363299Z Removing libclang1-16t64 (1:16.0.6-23ubuntu4) ...
2026-05-03T00:40:58.2491622Z Removing libclang1-17t64 (1:17.0.6-9ubuntu1) ...
2026-05-03T00:40:58.2620534Z Removing libdbusmenu-gtk3-4:amd64 (18.10.20180917~bzr492+repack1-3.1ubuntu5) ...
2026-05-03T00:40:58.2825101Z Removing libdbusmenu-glib4:amd64 (18.10.20180917~bzr492+repack1-3.1ubuntu5) ...
2026-05-03T00:40:58.3011928Z Removing libffi-dev:amd64 (3.4.6-1build1) ...
2026-05-03T00:40:58.3237633Z Removing libfftw3-double3:amd64 (3.3.10-1ubuntu3) ...
2026-05-03T00:40:58.3411555Z Removing libobjc-13-dev:amd64 (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T00:40:58.3564608Z Removing libobjc4:amd64 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:58.3691342Z Removing libgc1:amd64 (1:8.2.6-1build1) ...
2026-05-03T00:40:58.3841355Z Removing libgd3:amd64 (2.3.3-9ubuntu5) ...
2026-05-03T00:40:58.4083252Z Removing libmemcached11t64:amd64 (1.1.4-1.1build3) ...
2026-05-03T00:40:58.4213287Z Removing libhashkit2t64:amd64 (1.1.4-1.1build3) ...
2026-05-03T00:40:58.4335950Z Removing libhunspell-1.7-0:amd64 (1.7.2+really1.7.2-10build3) ...
2026-05-03T00:40:58.4462033Z Removing liblldb-16t64 (1:16.0.6-23ubuntu4) ...
2026-05-03T00:40:58.4590195Z Removing liblldb-17t64 (1:17.0.6-9ubuntu1) ...
2026-05-03T00:40:58.4719872Z Removing liblqr-1-0:amd64 (0.4.2-2.1build2) ...
2026-05-03T00:40:58.4849465Z Removing libncurses-dev:amd64 (6.4+20240113-1ubuntu2) ...
2026-05-03T00:40:58.5002967Z Removing libzmq5:amd64 (4.3.5-1build2) ...
2026-05-03T00:40:58.5132882Z Removing libnorm1t64:amd64 (1.5.9+dfsg-3.1build1) ...
2026-05-03T00:40:58.5263879Z Removing libvorbisfile3:amd64 (1.3.7-1build3) ...
2026-05-03T00:40:58.5389526Z Removing libvorbis0a:amd64 (1.3.7-1build3) ...
2026-05-03T00:40:58.5509394Z Removing libogg0:amd64 (1.3.5-3build1) ...
2026-05-03T00:40:58.5685978Z Removing libopenjp2-7:amd64 (2.5.0-2ubuntu0.4) ...
2026-05-03T00:40:58.5825566Z Removing libpcre2-dev:amd64 (10.42-4ubuntu2.1) ...
2026-05-03T00:40:58.6056032Z Removing libpcre2-16-0:amd64 (10.42-4ubuntu2.1) ...
2026-05-03T00:40:58.6188354Z Removing libpcre2-32-0:amd64 (10.42-4ubuntu2.1) ...
2026-05-03T00:40:58.6320130Z Removing libpcre2-posix3:amd64 (10.42-4ubuntu2.1) ...
2026-05-03T00:40:58.6501631Z Removing libpfm4:amd64 (4.13.0+git32-g0d4ed0e-1) ...
2026-05-03T00:40:58.6638944Z Removing libpgm-5.3-0t64:amd64 (5.3.128~dfsg-2.1build1) ...
2026-05-03T00:40:58.6769721Z Removing libqdbm14t64 (1.8.78-12.1build2) ...
2026-05-03T00:40:58.6939201Z Removing librabbitmq4:amd64 (0.11.0-1build2) ...
2026-05-03T00:40:58.7083956Z Removing libraw23t64:amd64 (0.21.2-2.1ubuntu0.24.04.1) ...
2026-05-03T00:40:58.7225125Z Removing libsnappy1v5:amd64 (1.1.10-1build1) ...
2026-05-03T00:40:58.7348130Z Removing libtdb1:amd64 (1.4.10-1build1) ...
2026-05-03T00:40:58.7489594Z Removing libtidy5deb1:amd64 (2:5.6.0-11ubuntu2) ...
2026-05-03T00:40:58.7620388Z Removing libtommath1:amd64 (1.2.1-2build1) ...
2026-05-03T00:40:58.7741192Z Removing libwebpdemux2:amd64 (1.3.2-0.4build3) ...
2026-05-03T00:40:58.7897021Z Removing libwebpmux3:amd64 (1.3.2-0.4build3) ...
2026-05-03T00:40:58.8028344Z Removing libz3-dev:amd64 (4.8.12-3.1build1) ...
2026-05-03T00:40:58.8175143Z Removing libz3-4:amd64 (4.8.12-3.1build1) ...
2026-05-03T00:40:58.8300596Z Removing libzip4t64:amd64 (1.7.3-1.1ubuntu2) ...
2026-05-03T00:40:58.8432037Z Removing mlock (8:2007f~dfsg-7build3) ...
2026-05-03T00:40:58.8561184Z Removing shtool (2.0.8-10) ...
2026-05-03T00:40:58.8712158Z Removing sound-theme-freedesktop (0.8-2ubuntu1) ...
2026-05-03T00:40:58.8869249Z Removing xul-ext-ubufox (3.4-0ubuntu1.17.10.4) ...
2026-05-03T00:40:58.9527316Z Removing libheif1:amd64 (1.17.6-1ubuntu4.2) ...
2026-05-03T00:40:58.9663197Z Removing libheif-plugin-libde265:amd64 (1.17.6-1ubuntu4.2) ...
2026-05-03T00:40:58.9807877Z Removing libde265-0:amd64 (1.0.15-1build3) ...
2026-05-03T00:40:58.9987557Z Removing libheif-plugin-aomdec:amd64 (1.17.6-1ubuntu4.2) ...
2026-05-03T00:40:59.0126700Z Removing libaom3:amd64 (3.8.2-2ubuntu0.1) ...
2026-05-03T00:40:59.0439598Z Processing triggers for man-db (2.12.0-4build2) ...
2026-05-03T00:40:59.0457904Z Not building database; man-db/auto-update is not 'true'.
2026-05-03T00:40:59.0473397Z Processing triggers for postgresql-common (290.pgdg24.04+1) ...
2026-05-03T00:40:59.1559407Z Building PostgreSQL dictionaries from installed myspell/hunspell packages...
2026-05-03T00:40:59.1560063Z Removing obsolete dictionary files:
2026-05-03T00:40:59.1563221Z   /var/cache/postgresql/dicts/en_us.affix
2026-05-03T00:40:59.1563822Z   /var/cache/postgresql/dicts/en_us.dict
2026-05-03T00:40:59.1622361Z   /usr/share/postgresql/16/tsearch_data/en_us.affix
2026-05-03T00:40:59.1623456Z   /usr/share/postgresql/16/tsearch_data/en_us.dict
2026-05-03T00:40:59.1820506Z Processing triggers for install-info (7.1-3build2) ...
2026-05-03T00:40:59.2791327Z Processing triggers for libc-bin (2.39-0ubuntu8.7) ...
2026-05-03T00:41:00.1941481Z === After cleanup ===
2026-05-03T00:41:00.1950929Z Filesystem      Size  Used Avail Use% Mounted on
2026-05-03T00:41:00.1951368Z /dev/root       145G   25G  120G  17% /
2026-05-03T00:41:00.1990747Z ##[group]Run sudo swapoff /mnt/swapfile 2>/dev/null || true
2026-05-03T00:41:00.1991166Z [36;1msudo swapoff /mnt/swapfile 2>/dev/null || true[0m
2026-05-03T00:41:00.1991471Z [36;1msudo rm -f /mnt/swapfile[0m
2026-05-03T00:41:00.1991882Z [36;1msudo fallocate -l 16G /mnt/swapfile || sudo dd if=/dev/zero of=/mnt/swapfile bs=1M count=16384[0m
2026-05-03T00:41:00.1992330Z [36;1msudo chmod 600 /mnt/swapfile[0m
2026-05-03T00:41:00.1992560Z [36;1msudo mkswap /mnt/swapfile[0m
2026-05-03T00:41:00.1992803Z [36;1msudo swapon /mnt/swapfile[0m
2026-05-03T00:41:00.1993025Z [36;1mfree -h[0m
2026-05-03T00:41:00.2014839Z shell: /usr/bin/bash -e {0}
2026-05-03T00:41:00.2015064Z env:
2026-05-03T00:41:00.2015247Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:41:00.2015510Z   ANDROID_VERSION: android15
2026-05-03T00:41:00.2015715Z   KERNEL_VERSION: 6.6
2026-05-03T00:41:00.2015898Z   KMI_GENERATION: 8
2026-05-03T00:41:00.2016068Z   KERNEL_NAME: Castorice
2026-05-03T00:41:00.2016297Z   DEVICE_CODE: fire
2026-05-03T00:41:00.2016457Z   KSU_DIR: 
2026-05-03T00:41:00.2016606Z   KSU_VERSION: 
2026-05-03T00:41:00.2016760Z   SUSFS_OK: 
2026-05-03T00:41:00.2016922Z   BUILT_KERNEL_VERSION: 
2026-05-03T00:41:00.2017101Z   ZIP_NAME: 
2026-05-03T00:41:00.2017269Z ##[endgroup]
2026-05-03T00:41:00.2572709Z Setting up swapspace version 1, size = 16 GiB (17179865088 bytes)
2026-05-03T00:41:00.2573338Z no label, UUID=5566d09a-5870-4132-8557-567607f238cb
2026-05-03T00:41:00.2686628Z                total        used        free      shared  buff/cache   available
2026-05-03T00:41:00.2687351Z Mem:            15Gi       1.0Gi        11Gi        41Mi       3.3Gi        14Gi
2026-05-03T00:41:00.2687735Z Swap:           18Gi          0B        18Gi
2026-05-03T00:41:00.2717885Z ##[group]Run sudo apt-get update
2026-05-03T00:41:00.2718192Z [36;1msudo apt-get update[0m
2026-05-03T00:41:00.2718563Z [36;1msudo apt-get install -y git curl wget bc bison flex libssl-dev make libelf-dev \[0m
2026-05-03T00:41:00.2719776Z [36;1m  python3 python3-pip python-is-python3 zip unzip cpio kmod rsync lz4 jq patch \[0m
2026-05-03T00:41:00.2720325Z [36;1m  binutils libncurses-dev pkg-config ninja-build zstd aria2 p7zip-full[0m
2026-05-03T00:41:00.2742083Z shell: /usr/bin/bash -e {0}
2026-05-03T00:41:00.2742308Z env:
2026-05-03T00:41:00.2742495Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:41:00.2742766Z   ANDROID_VERSION: android15
2026-05-03T00:41:00.2742980Z   KERNEL_VERSION: 6.6
2026-05-03T00:41:00.2743159Z   KMI_GENERATION: 8
2026-05-03T00:41:00.2743348Z   KERNEL_NAME: Castorice
2026-05-03T00:41:00.2743531Z   DEVICE_CODE: fire
2026-05-03T00:41:00.2743692Z   KSU_DIR: 
2026-05-03T00:41:00.2743837Z   KSU_VERSION: 
2026-05-03T00:41:00.2744030Z   SUSFS_OK: 
2026-05-03T00:41:00.2744188Z   BUILT_KERNEL_VERSION: 
2026-05-03T00:41:00.2744375Z   ZIP_NAME: 
2026-05-03T00:41:00.2744530Z ##[endgroup]
2026-05-03T00:41:00.3487159Z Get:1 file:/etc/apt/apt-mirrors.txt Mirrorlist [144 B]
2026-05-03T00:41:00.3957501Z Hit:6 https://packages.microsoft.com/repos/azure-cli noble InRelease
2026-05-03T00:41:00.3959843Z Get:7 https://packages.microsoft.com/ubuntu/24.04/prod noble InRelease [3600 B]
2026-05-03T00:41:00.4187037Z Get:8 https://dl.google.com/linux/chrome-stable/deb stable InRelease [1825 B]
2026-05-03T00:41:00.5222184Z Get:9 https://packages.microsoft.com/ubuntu/24.04/prod noble/main arm64 Packages [107 kB]
2026-05-03T00:41:00.5352261Z Hit:2 http://azure.archive.ubuntu.com/ubuntu noble InRelease
2026-05-03T00:41:00.5366421Z Get:3 http://azure.archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]
2026-05-03T00:41:00.5380076Z Get:10 https://packages.microsoft.com/ubuntu/24.04/prod noble/main amd64 Packages [132 kB]
2026-05-03T00:41:00.5424717Z Get:4 http://azure.archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]
2026-05-03T00:41:00.5445799Z Get:11 https://packages.microsoft.com/ubuntu/24.04/prod noble/main armhf Packages [11.6 kB]
2026-05-03T00:41:00.5448280Z Get:5 http://azure.archive.ubuntu.com/ubuntu noble-security InRelease [126 kB]
2026-05-03T00:41:00.5874783Z Get:12 https://dl.google.com/linux/chrome-stable/deb stable/main amd64 Packages [1216 B]
2026-05-03T00:41:00.6723080Z Get:13 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 Packages [1946 kB]
2026-05-03T00:41:00.6831288Z Get:14 http://azure.archive.ubuntu.com/ubuntu noble-updates/main Translation-en [348 kB]
2026-05-03T00:41:00.6866166Z Get:15 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 Components [177 kB]
2026-05-03T00:41:00.6872416Z Get:16 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 c-n-f Metadata [17.1 kB]
2026-05-03T00:41:00.6884231Z Get:17 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Packages [1685 kB]
2026-05-03T00:41:00.6985449Z Get:18 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe Translation-en [324 kB]
2026-05-03T00:41:00.7009132Z Get:19 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Components [386 kB]
2026-05-03T00:41:00.7036820Z Get:20 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 c-n-f Metadata [34.5 kB]
2026-05-03T00:41:00.7049449Z Get:21 http://azure.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Packages [3095 kB]
2026-05-03T00:41:00.7192726Z Get:22 http://azure.archive.ubuntu.com/ubuntu noble-updates/restricted Translation-en [715 kB]
2026-05-03T00:41:00.7664056Z Get:23 http://azure.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Components [212 B]
2026-05-03T00:41:00.7674459Z Get:24 http://azure.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 c-n-f Metadata [480 B]
2026-05-03T00:41:00.7690944Z Get:25 http://azure.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Packages [44.4 kB]
2026-05-03T00:41:00.7703267Z Get:26 http://azure.archive.ubuntu.com/ubuntu noble-updates/multiverse Translation-en [10.2 kB]
2026-05-03T00:41:00.7714578Z Get:27 http://azure.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Components [940 B]
2026-05-03T00:41:00.7720505Z Get:28 http://azure.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 c-n-f Metadata [656 B]
2026-05-03T00:41:00.7730356Z Get:29 http://azure.archive.ubuntu.com/ubuntu noble-backports/main amd64 Packages [64.5 kB]
2026-05-03T00:41:00.7744201Z Get:30 http://azure.archive.ubuntu.com/ubuntu noble-backports/main Translation-en [9172 B]
2026-05-03T00:41:00.7759245Z Get:31 http://azure.archive.ubuntu.com/ubuntu noble-backports/main amd64 Components [7368 B]
2026-05-03T00:41:00.7773026Z Get:32 http://azure.archive.ubuntu.com/ubuntu noble-backports/main amd64 c-n-f Metadata [368 B]
2026-05-03T00:41:00.7785787Z Get:33 http://azure.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Packages [34.1 kB]
2026-05-03T00:41:00.7800705Z Get:34 http://azure.archive.ubuntu.com/ubuntu noble-backports/universe Translation-en [18.2 kB]
2026-05-03T00:41:00.7816344Z Get:35 http://azure.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Components [10.5 kB]
2026-05-03T00:41:00.7829848Z Get:36 http://azure.archive.ubuntu.com/ubuntu noble-backports/universe amd64 c-n-f Metadata [1484 B]
2026-05-03T00:41:00.8261444Z Get:37 http://azure.archive.ubuntu.com/ubuntu noble-backports/restricted amd64 Components [212 B]
2026-05-03T00:41:00.8269883Z Get:38 http://azure.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Packages [748 B]
2026-05-03T00:41:00.8279411Z Get:39 http://azure.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Components [212 B]
2026-05-03T00:41:00.8290204Z Get:40 http://azure.archive.ubuntu.com/ubuntu noble-security/main amd64 Packages [1625 kB]
2026-05-03T00:41:00.8373396Z Get:41 http://azure.archive.ubuntu.com/ubuntu noble-security/main Translation-en [259 kB]
2026-05-03T00:41:00.8392520Z Get:42 http://azure.archive.ubuntu.com/ubuntu noble-security/main amd64 Components [21.9 kB]
2026-05-03T00:41:00.8401677Z Get:43 http://azure.archive.ubuntu.com/ubuntu noble-security/main amd64 c-n-f Metadata [11.0 kB]
2026-05-03T00:41:00.8411957Z Get:44 http://azure.archive.ubuntu.com/ubuntu noble-security/universe amd64 Packages [1182 kB]
2026-05-03T00:41:00.8471746Z Get:45 http://azure.archive.ubuntu.com/ubuntu noble-security/universe Translation-en [227 kB]
2026-05-03T00:41:00.8491298Z Get:46 http://azure.archive.ubuntu.com/ubuntu noble-security/universe amd64 Components [74.2 kB]
2026-05-03T00:41:00.8505082Z Get:47 http://azure.archive.ubuntu.com/ubuntu noble-security/universe amd64 c-n-f Metadata [23.1 kB]
2026-05-03T00:41:00.8516252Z Get:48 http://azure.archive.ubuntu.com/ubuntu noble-security/restricted amd64 Packages [2844 kB]
2026-05-03T00:41:00.8651586Z Get:49 http://azure.archive.ubuntu.com/ubuntu noble-security/restricted Translation-en [666 kB]
2026-05-03T00:41:00.8686499Z Get:50 http://azure.archive.ubuntu.com/ubuntu noble-security/restricted amd64 Components [212 B]
2026-05-03T00:41:00.8694626Z Get:51 http://azure.archive.ubuntu.com/ubuntu noble-security/multiverse amd64 Packages [28.8 kB]
2026-05-03T00:41:00.9142478Z Get:52 http://azure.archive.ubuntu.com/ubuntu noble-security/multiverse Translation-en [7172 B]
2026-05-03T00:41:00.9150862Z Get:53 http://azure.archive.ubuntu.com/ubuntu noble-security/multiverse amd64 Components [208 B]
2026-05-03T00:41:07.6273790Z Fetched 16.5 MB in 2s (8596 kB/s)
2026-05-03T00:41:08.4822620Z Reading package lists...
2026-05-03T00:41:08.5179649Z Reading package lists...
2026-05-03T00:41:08.7074783Z Building dependency tree...
2026-05-03T00:41:08.7081468Z Reading state information...
2026-05-03T00:41:08.8847288Z git is already the newest version (1:2.53.0-0ppa1~ubuntu24.04.1).
2026-05-03T00:41:08.8848952Z git set to manually installed.
2026-05-03T00:41:08.8849337Z curl is already the newest version (8.5.0-2ubuntu10.8).
2026-05-03T00:41:08.8849682Z wget is already the newest version (1.21.4-1ubuntu4.1).
2026-05-03T00:41:08.8850244Z bc is already the newest version (1.07.1-3ubuntu4).
2026-05-03T00:41:08.8850541Z bc set to manually installed.
2026-05-03T00:41:08.8850818Z bison is already the newest version (2:3.8.2+dfsg-1build2).
2026-05-03T00:41:08.8851166Z flex is already the newest version (2.6.4-8.2build1).
2026-05-03T00:41:08.8851514Z libssl-dev is already the newest version (3.0.13-0ubuntu3.9).
2026-05-03T00:41:08.8851861Z make is already the newest version (4.3-4.1build2).
2026-05-03T00:41:08.8852474Z python3 is already the newest version (3.12.3-0ubuntu2.1).
2026-05-03T00:41:08.8853140Z python3-pip is already the newest version (24.0+dfsg-1ubuntu1.3).
2026-05-03T00:41:08.8853596Z python-is-python3 is already the newest version (3.11.4-1).
2026-05-03T00:41:08.8853946Z zip is already the newest version (3.0-13ubuntu0.2).
2026-05-03T00:41:08.8854292Z unzip is already the newest version (6.0-28ubuntu4.1).
2026-05-03T00:41:08.8854627Z cpio is already the newest version (2.15+dfsg-1ubuntu2).
2026-05-03T00:41:08.8854933Z cpio set to manually installed.
2026-05-03T00:41:08.8855201Z rsync is already the newest version (3.2.7-1ubuntu1.2).
2026-05-03T00:41:08.8855530Z lz4 is already the newest version (1.9.4-1build1.1).
2026-05-03T00:41:08.8855843Z patch is already the newest version (2.7.6-7build3).
2026-05-03T00:41:08.8856137Z patch set to manually installed.
2026-05-03T00:41:08.8856432Z binutils is already the newest version (2.42-4ubuntu2.10).
2026-05-03T00:41:08.8856797Z pkg-config is already the newest version (1.8.1-2build1).
2026-05-03T00:41:08.8857163Z zstd is already the newest version (1.5.5+dfsg2-2build1.1).
2026-05-03T00:41:08.8857475Z zstd set to manually installed.
2026-05-03T00:41:08.8857770Z aria2 is already the newest version (1.37.0+debian-1build3).
2026-05-03T00:41:08.8858166Z p7zip-full is already the newest version (16.02+transitional.1).
2026-05-03T00:41:08.8858557Z The following additional packages will be installed:
2026-05-03T00:41:08.8859003Z   libjq1 libkmod2
2026-05-03T00:41:08.8859811Z Suggested packages:
2026-05-03T00:41:08.8860151Z   ncurses-doc
2026-05-03T00:41:08.9063621Z The following NEW packages will be installed:
2026-05-03T00:41:08.9070740Z   libelf-dev libncurses-dev ninja-build
2026-05-03T00:41:08.9075510Z The following packages will be upgraded:
2026-05-03T00:41:08.9081561Z   jq kmod libjq1 libkmod2
2026-05-03T00:41:08.9244503Z 4 upgraded, 3 newly installed, 0 to remove and 46 not upgraded.
2026-05-03T00:41:08.9245125Z Need to get 943 kB of archives.
2026-05-03T00:41:08.9245682Z After this operation, 3168 kB of additional disk space will be used.
2026-05-03T00:41:08.9246348Z Get:1 file:/etc/apt/apt-mirrors.txt Mirrorlist [144 B]
2026-05-03T00:41:08.9570929Z Get:2 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 kmod amd64 31+20240202-2ubuntu7.2 [102 kB]
2026-05-03T00:41:08.9678935Z Get:3 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libkmod2 amd64 31+20240202-2ubuntu7.2 [51.8 kB]
2026-05-03T00:41:08.9765246Z Get:4 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 jq amd64 1.7.1-3ubuntu0.24.04.2 [65.7 kB]
2026-05-03T00:41:08.9860310Z Get:5 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libjq1 amd64 1.7.1-3ubuntu0.24.04.2 [142 kB]
2026-05-03T00:41:08.9979244Z Get:6 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libelf-dev amd64 0.190-1.1ubuntu0.1 [68.5 kB]
2026-05-03T00:41:09.0089532Z Get:7 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libncurses-dev amd64 6.4+20240113-1ubuntu2 [384 kB]
2026-05-03T00:41:09.0263700Z Get:8 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 ninja-build amd64 1.11.1-2 [129 kB]
2026-05-03T00:41:09.2734758Z Fetched 943 kB in 0s (8210 kB/s)
2026-05-03T00:41:09.2986464Z (Reading database ... 
2026-05-03T00:41:09.2987172Z (Reading database ... 5%
2026-05-03T00:41:09.2987892Z (Reading database ... 10%
2026-05-03T00:41:09.2988267Z (Reading database ... 15%
2026-05-03T00:41:09.2988818Z (Reading database ... 20%
2026-05-03T00:41:09.2989126Z (Reading database ... 25%
2026-05-03T00:41:09.2989517Z (Reading database ... 30%
2026-05-03T00:41:09.2989733Z (Reading database ... 35%
2026-05-03T00:41:09.2989921Z (Reading database ... 40%
2026-05-03T00:41:09.2990116Z (Reading database ... 45%
2026-05-03T00:41:09.2990306Z (Reading database ... 50%
2026-05-03T00:41:09.2990496Z (Reading database ... 55%
2026-05-03T00:41:09.3014654Z (Reading database ... 60%
2026-05-03T00:41:09.3098568Z (Reading database ... 65%
2026-05-03T00:41:09.3124278Z (Reading database ... 70%
2026-05-03T00:41:09.3140371Z (Reading database ... 75%
2026-05-03T00:41:09.3182803Z (Reading database ... 80%
2026-05-03T00:41:09.3206947Z (Reading database ... 85%
2026-05-03T00:41:09.3229625Z (Reading database ... 90%
2026-05-03T00:41:09.3322224Z (Reading database ... 95%
2026-05-03T00:41:09.3322544Z (Reading database ... 100%
2026-05-03T00:41:09.3322985Z (Reading database ... 119905 files and directories currently installed.)
2026-05-03T00:41:09.3346069Z Preparing to unpack .../0-kmod_31+20240202-2ubuntu7.2_amd64.deb ...
2026-05-03T00:41:09.3403358Z Unpacking kmod (31+20240202-2ubuntu7.2) over (31+20240202-2ubuntu7.1) ...
2026-05-03T00:41:09.3906766Z Preparing to unpack .../1-libkmod2_31+20240202-2ubuntu7.2_amd64.deb ...
2026-05-03T00:41:09.3943165Z Unpacking libkmod2:amd64 (31+20240202-2ubuntu7.2) over (31+20240202-2ubuntu7.1) ...
2026-05-03T00:41:09.4199878Z Preparing to unpack .../2-jq_1.7.1-3ubuntu0.24.04.2_amd64.deb ...
2026-05-03T00:41:09.4225332Z Unpacking jq (1.7.1-3ubuntu0.24.04.2) over (1.7.1-3ubuntu0.24.04.1) ...
2026-05-03T00:41:09.4596434Z Preparing to unpack .../3-libjq1_1.7.1-3ubuntu0.24.04.2_amd64.deb ...
2026-05-03T00:41:09.4623313Z Unpacking libjq1:amd64 (1.7.1-3ubuntu0.24.04.2) over (1.7.1-3ubuntu0.24.04.1) ...
2026-05-03T00:41:09.4815691Z Selecting previously unselected package libelf-dev:amd64.
2026-05-03T00:41:09.4892000Z Preparing to unpack .../4-libelf-dev_0.190-1.1ubuntu0.1_amd64.deb ...
2026-05-03T00:41:09.4900577Z Unpacking libelf-dev:amd64 (0.190-1.1ubuntu0.1) ...
2026-05-03T00:41:09.5092442Z Selecting previously unselected package libncurses-dev:amd64.
2026-05-03T00:41:09.5167070Z Preparing to unpack .../5-libncurses-dev_6.4+20240113-1ubuntu2_amd64.deb ...
2026-05-03T00:41:09.5174947Z Unpacking libncurses-dev:amd64 (6.4+20240113-1ubuntu2) ...
2026-05-03T00:41:09.5489744Z Selecting previously unselected package ninja-build.
2026-05-03T00:41:09.5565565Z Preparing to unpack .../6-ninja-build_1.11.1-2_amd64.deb ...
2026-05-03T00:41:09.5627421Z Unpacking ninja-build (1.11.1-2) ...
2026-05-03T00:41:09.5924155Z Setting up libncurses-dev:amd64 (6.4+20240113-1ubuntu2) ...
2026-05-03T00:41:09.5947496Z Setting up libjq1:amd64 (1.7.1-3ubuntu0.24.04.2) ...
2026-05-03T00:41:09.5969611Z Setting up ninja-build (1.11.1-2) ...
2026-05-03T00:41:09.5991994Z Setting up libelf-dev:amd64 (0.190-1.1ubuntu0.1) ...
2026-05-03T00:41:09.6013146Z Setting up jq (1.7.1-3ubuntu0.24.04.2) ...
2026-05-03T00:41:09.6035326Z Setting up libkmod2:amd64 (31+20240202-2ubuntu7.2) ...
2026-05-03T00:41:09.6056617Z Setting up kmod (31+20240202-2ubuntu7.2) ...
2026-05-03T00:41:09.8762358Z Processing triggers for initramfs-tools (0.142ubuntu25.8) ...
2026-05-03T00:41:09.9229226Z update-initramfs: Generating /boot/initrd.img-6.17.0-1010-azure
2026-05-03T00:41:15.3916080Z Processing triggers for libc-bin (2.39-0ubuntu8.7) ...
2026-05-03T00:41:15.4040409Z Processing triggers for man-db (2.12.0-4build2) ...
2026-05-03T00:41:15.4056293Z Not building database; man-db/auto-update is not 'true'.
2026-05-03T00:41:16.0181437Z 
2026-05-03T00:41:16.0181861Z Running kernel seems to be up-to-date.
2026-05-03T00:41:16.0182239Z 
2026-05-03T00:41:16.0182357Z Restarting services...
2026-05-03T00:41:16.0403868Z  /etc/needrestart/restart.d/systemd-manager
2026-05-03T00:41:16.3478408Z  systemctl restart systemd-journald.service systemd-networkd.service systemd-resolved.service systemd-udevd.service udisks2.service
2026-05-03T00:41:16.5031452Z 
2026-05-03T00:41:16.5032077Z Service restarts being deferred:
2026-05-03T00:41:16.5032590Z  systemctl restart systemd-logind.service
2026-05-03T00:41:16.5033268Z 
2026-05-03T00:41:16.5033445Z No containers need to be restarted.
2026-05-03T00:41:16.5033974Z 
2026-05-03T00:41:16.5034154Z User sessions running outdated binaries:
2026-05-03T00:41:16.5034616Z  runner @ user manager service: systemd[1124]
2026-05-03T00:41:16.5126623Z 
2026-05-03T00:41:16.5127217Z No VM guests are running outdated hypervisor (qemu) binaries on this host.
2026-05-03T00:41:17.4734567Z ##[group]Run mkdir -p ~/bin
2026-05-03T00:41:17.4734858Z [36;1mmkdir -p ~/bin[0m
2026-05-03T00:41:17.4735221Z [36;1mcurl -s https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo[0m
2026-05-03T00:41:17.4735619Z [36;1mchmod a+x ~/bin/repo[0m
2026-05-03T00:41:17.4735842Z [36;1mecho "$HOME/bin" >> $GITHUB_PATH[0m
2026-05-03T00:41:17.4756972Z shell: /usr/bin/bash -e {0}
2026-05-03T00:41:17.4757205Z env:
2026-05-03T00:41:17.4757393Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:41:17.4757661Z   ANDROID_VERSION: android15
2026-05-03T00:41:17.4757875Z   KERNEL_VERSION: 6.6
2026-05-03T00:41:17.4758051Z   KMI_GENERATION: 8
2026-05-03T00:41:17.4758226Z   KERNEL_NAME: Castorice
2026-05-03T00:41:17.4758413Z   DEVICE_CODE: fire
2026-05-03T00:41:17.4758576Z   KSU_DIR: 
2026-05-03T00:41:17.4759021Z   KSU_VERSION: 
2026-05-03T00:41:17.4759186Z   SUSFS_OK: 
2026-05-03T00:41:17.4759341Z   BUILT_KERNEL_VERSION: 
2026-05-03T00:41:17.4759524Z   ZIP_NAME: 
2026-05-03T00:41:17.4759715Z ##[endgroup]
2026-05-03T00:41:17.5295497Z ##[group]Run mkdir -p kernel
2026-05-03T00:41:17.5295783Z [36;1mmkdir -p kernel[0m
2026-05-03T00:41:17.5295976Z [36;1mcd kernel[0m
2026-05-03T00:41:17.5296293Z [36;1mrepo init -u https://android.googlesource.com/kernel/manifest \[0m
2026-05-03T00:41:17.5296736Z [36;1m  -b common-${ANDROID_VERSION}-${KERNEL_VERSION} --depth=1[0m
2026-05-03T00:41:17.5297163Z [36;1mrepo sync -c -j$(nproc) --no-tags --no-clone-bundle --force-sync[0m
2026-05-03T00:41:17.5297509Z [36;1mecho "=== Kernel version ==="[0m
2026-05-03T00:41:17.5297757Z [36;1mcd common && make kernelversion[0m
2026-05-03T00:41:17.5321393Z shell: /usr/bin/bash -e {0}
2026-05-03T00:41:17.5321625Z env:
2026-05-03T00:41:17.5321808Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:41:17.5322080Z   ANDROID_VERSION: android15
2026-05-03T00:41:17.5322291Z   KERNEL_VERSION: 6.6
2026-05-03T00:41:17.5322467Z   KMI_GENERATION: 8
2026-05-03T00:41:17.5322648Z   KERNEL_NAME: Castorice
2026-05-03T00:41:17.5322877Z   DEVICE_CODE: fire
2026-05-03T00:41:17.5323039Z   KSU_DIR: 
2026-05-03T00:41:17.5323191Z   KSU_VERSION: 
2026-05-03T00:41:17.5323343Z   SUSFS_OK: 
2026-05-03T00:41:17.5323501Z   BUILT_KERNEL_VERSION: 
2026-05-03T00:41:17.5323677Z   ZIP_NAME: 
2026-05-03T00:41:17.5323834Z ##[endgroup]
2026-05-03T00:41:19.2512677Z 
2026-05-03T00:41:19.2513426Z repo has been initialized in /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel
2026-05-03T00:42:21.2146037Z Finalizing sync state...
2026-05-03T00:42:21.2146468Z repo sync has finished successfully.
2026-05-03T00:42:21.3291295Z === Kernel version ===
2026-05-03T00:42:21.5686081Z 6.6.129
2026-05-03T00:42:21.5719206Z ##[group]Run cd kernel/common
2026-05-03T00:42:21.5719523Z [36;1mcd kernel/common[0m
2026-05-03T00:42:21.5719851Z [36;1mecho "Device KMI: ${KERNEL_VERSION}-${ANDROID_VERSION}-${KMI_GENERATION}"[0m
2026-05-03T00:42:21.5720208Z [36;1m[0m
2026-05-03T00:42:21.5720438Z [36;1m# Set KMI_GENERATION in build.config.common[0m
2026-05-03T00:42:21.5720745Z [36;1mif [ -f "build.config.common" ]; then[0m
2026-05-03T00:42:21.5721059Z [36;1m  if grep -q "KMI_GENERATION" build.config.common; then[0m
2026-05-03T00:42:21.5721512Z [36;1m    sed -i "s/KMI_GENERATION=.*/KMI_GENERATION=${KMI_GENERATION}/" build.config.common[0m
2026-05-03T00:42:21.5721891Z [36;1m  else[0m
2026-05-03T00:42:21.5722155Z [36;1m    echo "KMI_GENERATION=${KMI_GENERATION}" >> build.config.common[0m
2026-05-03T00:42:21.5722671Z [36;1m  fi[0m
2026-05-03T00:42:21.5722893Z [36;1m  echo "build.config.common KMI_GENERATION set:"[0m
2026-05-03T00:42:21.5723243Z [36;1m  grep KMI_GENERATION build.config.common[0m
2026-05-03T00:42:21.5723503Z [36;1mfi[0m
2026-05-03T00:42:21.5723661Z [36;1m[0m
2026-05-03T00:42:21.5723860Z [36;1m# Also patch Bazel/Kleaf config if present[0m
2026-05-03T00:42:21.5724207Z [36;1mfor f in build.config.gki build.config.gki.aarch64; do[0m
2026-05-03T00:42:21.5724576Z [36;1m  if [ -f "$f" ] && grep -q "KMI_GENERATION" "$f"; then[0m
2026-05-03T00:42:21.5724971Z [36;1m    sed -i "s/KMI_GENERATION=.*/KMI_GENERATION=${KMI_GENERATION}/" "$f"[0m
2026-05-03T00:42:21.5725326Z [36;1m    echo "$f patched"[0m
2026-05-03T00:42:21.5725527Z [36;1m  fi[0m
2026-05-03T00:42:21.5725682Z [36;1mdone[0m
2026-05-03T00:42:21.5725826Z [36;1m[0m
2026-05-03T00:42:21.5726018Z [36;1m# Patch stamp.bzl if it has KMI generation[0m
2026-05-03T00:42:21.5726355Z [36;1mSTAMP_FILE="../build/kernel/kleaf/impl/stamp.bzl"[0m
2026-05-03T00:42:21.5726751Z [36;1mif [ -f "$STAMP_FILE" ] && grep -q "kmi_generation" "$STAMP_FILE"; then[0m
2026-05-03T00:42:21.5727148Z [36;1m  echo "Checking stamp.bzl for KMI generation..."[0m
2026-05-03T00:42:21.5727421Z [36;1mfi[0m
2026-05-03T00:42:21.5775718Z shell: /usr/bin/bash -e {0}
2026-05-03T00:42:21.5775941Z env:
2026-05-03T00:42:21.5776136Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:42:21.5776403Z   ANDROID_VERSION: android15
2026-05-03T00:42:21.5776606Z   KERNEL_VERSION: 6.6
2026-05-03T00:42:21.5776788Z   KMI_GENERATION: 8
2026-05-03T00:42:21.5776968Z   KERNEL_NAME: Castorice
2026-05-03T00:42:21.5777148Z   DEVICE_CODE: fire
2026-05-03T00:42:21.5777310Z   KSU_DIR: 
2026-05-03T00:42:21.5777456Z   KSU_VERSION: 
2026-05-03T00:42:21.5777613Z   SUSFS_OK: 
2026-05-03T00:42:21.5777768Z   BUILT_KERNEL_VERSION: 
2026-05-03T00:42:21.5777948Z   ZIP_NAME: 
2026-05-03T00:42:21.5778097Z ##[endgroup]
2026-05-03T00:42:21.5816821Z Device KMI: 6.6-android15-8
2026-05-03T00:42:21.5845155Z build.config.common KMI_GENERATION set:
2026-05-03T00:42:21.5855578Z KMI_GENERATION=8
2026-05-03T00:42:21.5935530Z ##[group]Run cd kernel/common
2026-05-03T00:42:21.5935812Z [36;1mcd kernel/common[0m
2026-05-03T00:42:21.5936010Z [36;1m[0m
2026-05-03T00:42:21.5936218Z [36;1m# Clone KernelSU-Next latest stable release[0m
2026-05-03T00:42:21.5936578Z [36;1mecho "Fetching latest stable KernelSU-Next release..."[0m
2026-05-03T00:42:21.5937121Z [36;1mKSU_TAG=$(curl -sL https://api.github.com/repos/KernelSU-Next/KernelSU-Next/releases/latest \[0m
2026-05-03T00:42:21.5937568Z [36;1m  | jq -r '.tag_name')[0m
2026-05-03T00:42:21.5937764Z [36;1m[0m
2026-05-03T00:42:21.5937980Z [36;1mif [ -z "$KSU_TAG" ] || [ "$KSU_TAG" = "null" ]; then[0m
2026-05-03T00:42:21.5938403Z [36;1m  echo "WARN: Could not fetch latest release tag, falling back to default branch"[0m
2026-05-03T00:42:21.5939228Z [36;1m  git clone --depth=1 https://github.com/KernelSU-Next/KernelSU-Next.git KernelSU-Next[0m
2026-05-03T00:42:21.5939656Z [36;1m  KSU_TAG="default"[0m
2026-05-03T00:42:21.5939846Z [36;1melse[0m
2026-05-03T00:42:21.5940129Z [36;1m  echo "Cloning KernelSU-Next $KSU_TAG (latest stable)..."[0m
2026-05-03T00:42:21.5940493Z [36;1m  git clone --depth=1 --branch "$KSU_TAG" \[0m
2026-05-03T00:42:21.5940878Z [36;1m    https://github.com/KernelSU-Next/KernelSU-Next.git KernelSU-Next[0m
2026-05-03T00:42:21.5941215Z [36;1mfi[0m
2026-05-03T00:42:21.5941365Z [36;1m[0m
2026-05-03T00:42:21.5941599Z [36;1m# Integrate into kernel build (symlink driver)[0m
2026-05-03T00:42:21.5941950Z [36;1mln -sf "$(pwd)/KernelSU-Next/kernel" "drivers/kernelsu"[0m
2026-05-03T00:42:21.5942233Z [36;1m[0m
2026-05-03T00:42:21.5942401Z [36;1m# Add to Makefile if not present[0m
2026-05-03T00:42:21.5942688Z [36;1mif ! grep -q "kernelsu" drivers/Makefile; then[0m
2026-05-03T00:42:21.5943047Z [36;1m  echo "obj-\$(CONFIG_KSU) += kernelsu/" >> drivers/Makefile[0m
2026-05-03T00:42:21.5943512Z [36;1mfi[0m
2026-05-03T00:42:21.5943655Z [36;1m[0m
2026-05-03T00:42:21.5943832Z [36;1m# Add Kconfig include if not present[0m
2026-05-03T00:42:21.5944154Z [36;1mif ! grep -q "kernelsu/Kconfig" drivers/Kconfig; then[0m
2026-05-03T00:42:21.5944563Z [36;1m  sed -i '/endmenu/i source "drivers/kernelsu/Kconfig"' drivers/Kconfig[0m
2026-05-03T00:42:21.5944901Z [36;1mfi[0m
2026-05-03T00:42:21.5945050Z [36;1m[0m
2026-05-03T00:42:21.5945223Z [36;1mKSU_DIR="KernelSU-Next"[0m
2026-05-03T00:42:21.5945507Z [36;1mKSU_VERSION=$(cd $KSU_DIR && git rev-list --count HEAD)[0m
2026-05-03T00:42:21.5945858Z [36;1mecho "KSU_VERSION=$KSU_VERSION" >> $GITHUB_ENV[0m
2026-05-03T00:42:21.5946154Z [36;1mecho "KSU_DIR=$KSU_DIR" >> $GITHUB_ENV[0m
2026-05-03T00:42:21.5946522Z [36;1mecho "KernelSU-Next installed — version $KSU_VERSION ($KSU_TAG)"[0m
2026-05-03T00:42:21.5965972Z shell: /usr/bin/bash -e {0}
2026-05-03T00:42:21.5966188Z env:
2026-05-03T00:42:21.5966378Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:42:21.5966647Z   ANDROID_VERSION: android15
2026-05-03T00:42:21.5966855Z   KERNEL_VERSION: 6.6
2026-05-03T00:42:21.5967037Z   KMI_GENERATION: 8
2026-05-03T00:42:21.5967215Z   KERNEL_NAME: Castorice
2026-05-03T00:42:21.5967395Z   DEVICE_CODE: fire
2026-05-03T00:42:21.5967560Z   KSU_DIR: 
2026-05-03T00:42:21.5967705Z   KSU_VERSION: 
2026-05-03T00:42:21.5967862Z   SUSFS_OK: 
2026-05-03T00:42:21.5968016Z   BUILT_KERNEL_VERSION: 
2026-05-03T00:42:21.5968196Z   ZIP_NAME: 
2026-05-03T00:42:21.5968345Z ##[endgroup]
2026-05-03T00:42:21.6009034Z Fetching latest stable KernelSU-Next release...
2026-05-03T00:42:21.7332220Z Cloning KernelSU-Next v3.2.0 (latest stable)...
2026-05-03T00:42:21.7345498Z Cloning into 'KernelSU-Next'...
2026-05-03T00:42:22.1257188Z Note: switching to '551ad80473f60e052917aec08abf5323b6ab2f7c'.
2026-05-03T00:42:22.1257514Z 
2026-05-03T00:42:22.1257705Z You are in 'detached HEAD' state. You can look around, make experimental
2026-05-03T00:42:22.1258152Z changes and commit them, and you can discard any commits you make in this
2026-05-03T00:42:22.1258613Z state without impacting any branches by switching back to a branch.
2026-05-03T00:42:22.1259318Z 
2026-05-03T00:42:22.1259501Z If you want to create a new branch to retain commits you create, you may
2026-05-03T00:42:22.1259907Z do so (now or later) by using -c with the switch command. Example:
2026-05-03T00:42:22.1260141Z 
2026-05-03T00:42:22.1260226Z   git switch -c <new-branch-name>
2026-05-03T00:42:22.1260385Z 
2026-05-03T00:42:22.1260465Z Or undo this operation with:
2026-05-03T00:42:22.1260602Z 
2026-05-03T00:42:22.1260668Z   git switch -
2026-05-03T00:42:22.1260775Z 
2026-05-03T00:42:22.1260973Z Turn off this advice by setting config variable advice.detachedHead to false
2026-05-03T00:42:22.1261265Z 
2026-05-03T00:42:22.1914429Z KernelSU-Next installed — version 1 (v3.2.0)
2026-05-03T00:42:22.1971403Z ##[group]Run # Git identity needed for git commit/apply --3way used below
2026-05-03T00:42:22.1972295Z [36;1m# Git identity needed for git commit/apply --3way used below[0m
2026-05-03T00:42:22.1972738Z [36;1mgit config --global user.name "github-actions[bot]"[0m
2026-05-03T00:42:22.1973203Z [36;1mgit config --global user.email "github-actions[bot]@users.noreply.github.com"[0m
2026-05-03T00:42:22.1973587Z [36;1m[0m
2026-05-03T00:42:22.1973745Z [36;1mcd kernel[0m
2026-05-03T00:42:22.1974046Z [36;1mgit clone --depth=1 https://gitlab.com/simonpunk/susfs4ksu.git \[0m
2026-05-03T00:42:22.1974468Z [36;1m  -b gki-${ANDROID_VERSION}-${KERNEL_VERSION} || \[0m
2026-05-03T00:42:22.1974872Z [36;1mgit clone --depth=1 https://gitlab.com/simonpunk/susfs4ksu.git \[0m
2026-05-03T00:42:22.1975236Z [36;1m  -b gki-${ANDROID_VERSION}-6.6[0m
2026-05-03T00:42:22.1975480Z [36;1m[0m
2026-05-03T00:42:22.1975627Z [36;1mcd common[0m
2026-05-03T00:42:22.1975796Z [36;1m[0m
2026-05-03T00:42:22.1976038Z [36;1m# --- Step 1: Copy SUSFS kernel source files ---[0m
2026-05-03T00:42:22.1976353Z [36;1mecho "=== Copying SUSFS source files ==="[0m
2026-05-03T00:42:22.1976851Z [36;1mcp -rv ../susfs4ksu/kernel_patches/fs/* fs/[0m
2026-05-03T00:42:22.1977224Z [36;1mcp -rv ../susfs4ksu/kernel_patches/include/linux/* include/linux/[0m
2026-05-03T00:42:22.1977596Z [36;1mls -la include/linux/susfs* fs/susfs*[0m
2026-05-03T00:42:22.1977840Z [36;1m[0m
2026-05-03T00:42:22.1978060Z [36;1m# --- Step 2: Apply kernel tree integration patch ---[0m
2026-05-03T00:42:22.1978411Z [36;1mecho "=== Applying kernel tree SUSFS patch ==="[0m
2026-05-03T00:42:22.1979105Z [36;1mfor patch in ../susfs4ksu/kernel_patches/50_add_susfs_in_gki-*.patch; do[0m
2026-05-03T00:42:22.1979487Z [36;1m  if [ -f "$patch" ]; then[0m
2026-05-03T00:42:22.1979729Z [36;1m    echo "Applying: $patch"[0m
2026-05-03T00:42:22.1980073Z [36;1m    git add -A && git commit -m "pre-susfs-kernel-patch" --allow-empty -q[0m
2026-05-03T00:42:22.1980467Z [36;1m    if git apply --3way "$patch"; then[0m
2026-05-03T00:42:22.1980817Z [36;1m      echo "Kernel SUSFS patch applied cleanly via 3-way merge"[0m
2026-05-03T00:42:22.1981231Z [36;1m    elif patch -p1 --forward --fuzz=3 < "$patch"; then[0m
2026-05-03T00:42:22.1981600Z [36;1m      echo "Kernel SUSFS patch applied via fuzz fallback"[0m
2026-05-03T00:42:22.1981895Z [36;1m    else[0m
2026-05-03T00:42:22.1982163Z [36;1m      echo "WARN: Kernel SUSFS patch had issues (continuing)"[0m
2026-05-03T00:42:22.1982483Z [36;1m    fi[0m
2026-05-03T00:42:22.1982645Z [36;1m  fi[0m
2026-05-03T00:42:22.1982799Z [36;1mdone[0m
2026-05-03T00:42:22.1982950Z [36;1m[0m
2026-05-03T00:42:22.1983168Z [36;1m# --- Step 3: Integrate SUSFS into KernelSU-Next ---[0m
2026-05-03T00:42:22.1983581Z [36;1m# KernelSU-Next v3.2.0 is fundamentally incompatible with the legacy [0m
2026-05-03T00:42:22.1984047Z [36;1m# '10_enable_susfs_for_ksu.patch'. Applying it causes severe C syntax [0m
2026-05-03T00:42:22.1984445Z [36;1m# corruption and undefined linker symbols. [0m
2026-05-03T00:42:22.1984816Z [36;1m# Therefore, we bypass the patch entirely and cleanly inject the [0m
2026-05-03T00:42:22.1985262Z [36;1m# necessary SUSFS initialization into the pristine KSU-Next source.[0m
2026-05-03T00:42:22.1985737Z [36;1mecho "=== Integrating SUSFS into KernelSU-Next (Clean Manual Method) ==="[0m
2026-05-03T00:42:22.1986110Z [36;1mKSU_DIR="KernelSU-Next"[0m
2026-05-03T00:42:22.1986332Z [36;1mKSU_KERNEL="$KSU_DIR/kernel"[0m
2026-05-03T00:42:22.1986549Z [36;1m[0m
2026-05-03T00:42:22.1986704Z [36;1m# 1. Inject SUSFS Kconfig[0m
2026-05-03T00:42:22.1987036Z [36;1mif ! grep -q "CONFIG_KSU_SUSFS" "$KSU_KERNEL/Kconfig" 2>/dev/null; then[0m
2026-05-03T00:42:22.1987405Z [36;1m  cat >> "$KSU_KERNEL/Kconfig" << 'KEOF'[0m
2026-05-03T00:42:22.1987649Z [36;1m[0m
2026-05-03T00:42:22.1987807Z [36;1mmenu "KernelSU - SUSFS"[0m
2026-05-03T00:42:22.1988027Z [36;1mconfig KSU_SUSFS[0m
2026-05-03T00:42:22.1988447Z [36;1m	bool "KernelSU addon - SUSFS"[0m
2026-05-03T00:42:22.1988928Z [36;1m	depends on KSU[0m
2026-05-03T00:42:22.1989128Z [36;1m	default y[0m
2026-05-03T00:42:22.1989299Z [36;1m	help[0m
2026-05-03T00:42:22.1989550Z [36;1m	  Patch and Enable SUSFS to kernel with KernelSU.[0m
2026-05-03T00:42:22.1989833Z [36;1m[0m
2026-05-03T00:42:22.1989993Z [36;1mconfig KSU_SUSFS_SUS_PATH[0m
2026-05-03T00:42:22.1990246Z [36;1m	bool "Enable to hide suspicious path"[0m
2026-05-03T00:42:22.1990512Z [36;1m	depends on KSU_SUSFS[0m
2026-05-03T00:42:22.1990717Z [36;1m	default y[0m
2026-05-03T00:42:22.1990879Z [36;1m[0m
2026-05-03T00:42:22.1991039Z [36;1mconfig KSU_SUSFS_SUS_MOUNT[0m
2026-05-03T00:42:22.1991289Z [36;1m	bool "Enable to hide suspicious mounts"[0m
2026-05-03T00:42:22.1991552Z [36;1m	depends on KSU_SUSFS[0m
2026-05-03T00:42:22.1991753Z [36;1m	default y[0m
2026-05-03T00:42:22.1991926Z [36;1m[0m
2026-05-03T00:42:22.1992082Z [36;1mconfig KSU_SUSFS_SUS_KSTAT[0m
2026-05-03T00:42:22.1992350Z [36;1m	bool "Enable to spoof suspicious kstat"[0m
2026-05-03T00:42:22.1992612Z [36;1m	depends on KSU_SUSFS[0m
2026-05-03T00:42:22.1992817Z [36;1m	default y[0m
2026-05-03T00:42:22.1993119Z [36;1m[0m
2026-05-03T00:42:22.1993274Z [36;1mconfig KSU_SUSFS_SPOOF_UNAME[0m
2026-05-03T00:42:22.1993518Z [36;1m	bool "Enable to spoof uname"[0m
2026-05-03T00:42:22.1993746Z [36;1m	depends on KSU_SUSFS[0m
2026-05-03T00:42:22.1993944Z [36;1m	default y[0m
2026-05-03T00:42:22.1994102Z [36;1m[0m
2026-05-03T00:42:22.1994263Z [36;1mconfig KSU_SUSFS_ENABLE_LOG[0m
2026-05-03T00:42:22.1994519Z [36;1m	bool "Enable logging susfs log to kernel"[0m
2026-05-03T00:42:22.1994786Z [36;1m	depends on KSU_SUSFS[0m
2026-05-03T00:42:22.1994988Z [36;1m	default y[0m
2026-05-03T00:42:22.1995146Z [36;1m[0m
2026-05-03T00:42:22.1995329Z [36;1mconfig KSU_SUSFS_HIDE_KSU_SUSFS_SYMBOLS[0m
2026-05-03T00:42:22.1995680Z [36;1m	bool "Enable to hide ksu and susfs symbols from /proc/kallsyms"[0m
2026-05-03T00:42:22.1996019Z [36;1m	depends on KSU_SUSFS[0m
2026-05-03T00:42:22.1996216Z [36;1m	default y[0m
2026-05-03T00:42:22.1996379Z [36;1m[0m
2026-05-03T00:42:22.1996572Z [36;1mconfig KSU_SUSFS_SPOOF_CMDLINE_OR_BOOTCONFIG[0m
2026-05-03T00:42:22.1996924Z [36;1m	bool "Enable to spoof /proc/bootconfig or /proc/cmdline"[0m
2026-05-03T00:42:22.1997238Z [36;1m	depends on KSU_SUSFS[0m
2026-05-03T00:42:22.1997434Z [36;1m	default y[0m
2026-05-03T00:42:22.1997596Z [36;1m[0m
2026-05-03T00:42:22.1997755Z [36;1mconfig KSU_SUSFS_OPEN_REDIRECT[0m
2026-05-03T00:42:22.1998088Z [36;1m	bool "Enable to redirect a path to be opened with another path"[0m
2026-05-03T00:42:22.1998428Z [36;1m	depends on KSU_SUSFS[0m
2026-05-03T00:42:22.1998862Z [36;1m	default y[0m
2026-05-03T00:42:22.1999061Z [36;1m[0m
2026-05-03T00:42:22.1999224Z [36;1mconfig KSU_SUSFS_SUS_MAP[0m
2026-05-03T00:42:22.1999521Z [36;1m	bool "Enable to hide mmapped real file from proc maps"[0m
2026-05-03T00:42:22.1999823Z [36;1m	depends on KSU_SUSFS[0m
2026-05-03T00:42:22.2000032Z [36;1m	default y[0m
2026-05-03T00:42:22.2000191Z [36;1m[0m
2026-05-03T00:42:22.2000337Z [36;1mendmenu[0m
2026-05-03T00:42:22.2000492Z [36;1mKEOF[0m
2026-05-03T00:42:22.2000703Z [36;1m  echo "SUSFS Kconfig injected successfully"[0m
2026-05-03T00:42:22.2000958Z [36;1mfi[0m
2026-05-03T00:42:22.2001105Z [36;1m[0m
2026-05-03T00:42:22.2001276Z [36;1m# 2. Inject SUSFS Makefile entries[0m
2026-05-03T00:42:22.2001623Z [36;1mif ! grep -q "SUSFS_VERSION" "$KSU_KERNEL/Makefile" 2>/dev/null; then[0m
2026-05-03T00:42:22.2001992Z [36;1m  cat >> "$KSU_KERNEL/Makefile" << 'MKEOF'[0m
2026-05-03T00:42:22.2002235Z [36;1m[0m
2026-05-03T00:42:22.2002388Z [36;1m## For susfs stuff ##[0m
2026-05-03T00:42:22.2002663Z [36;1mifeq ($(shell test -e $(srctree)/fs/susfs.c; echo $$?),0)[0m
2026-05-03T00:42:22.2003282Z [36;1m$(eval SUSFS_VERSION=$(shell cat $(srctree)/include/linux/susfs.h | grep -E '^#define SUSFS_VERSION' | cut -d' ' -f3 | sed 's/"//g'))[0m
2026-05-03T00:42:22.2003818Z [36;1m$(info )[0m
2026-05-03T00:42:22.2004160Z [36;1m$(info -- SUSFS_VERSION: $(SUSFS_VERSION))[0m
2026-05-03T00:42:22.2004431Z [36;1melse[0m
2026-05-03T00:42:22.2004678Z [36;1m$(info -- You have not integrated susfs in your kernel yet.)[0m
2026-05-03T00:42:22.2005074Z [36;1m$(info -- Read: https://gitlab.com/simonpunk/susfs4ksu)[0m
2026-05-03T00:42:22.2005368Z [36;1mendif[0m
2026-05-03T00:42:22.2005528Z [36;1mMKEOF[0m
2026-05-03T00:42:22.2005754Z [36;1m  echo "SUSFS Makefile entries injected successfully"[0m
2026-05-03T00:42:22.2006039Z [36;1mfi[0m
2026-05-03T00:42:22.2006189Z [36;1m[0m
2026-05-03T00:42:22.2006373Z [36;1m# 3. Inject susfs.h include into core/init.c[0m
2026-05-03T00:42:22.2006806Z [36;1mif [ -f "$KSU_KERNEL/core/init.c" ] && ! grep -q "susfs.h" "$KSU_KERNEL/core/init.c"; then[0m
2026-05-03T00:42:22.2007380Z [36;1m  sed -i '/#include <linux\/workqueue.h>/a #include <linux/susfs.h>' "$KSU_KERNEL/core/init.c"[0m
2026-05-03T00:42:22.2007786Z [36;1mfi[0m
2026-05-03T00:42:22.2007936Z [36;1m[0m
2026-05-03T00:42:22.2008131Z [36;1m# 4. Inject susfs_init() call into core/init.c[0m
2026-05-03T00:42:22.2008567Z [36;1mif [ -f "$KSU_KERNEL/core/init.c" ] && ! grep -q "susfs_init" "$KSU_KERNEL/core/init.c"; then[0m
2026-05-03T00:42:22.2009453Z [36;1m  sed -i '/ksu_feature_init/i \[0m
2026-05-03T00:42:22.2009704Z [36;1m#ifdef CONFIG_KSU_SUSFS\[0m
2026-05-03T00:42:22.2009926Z [36;1m\tsusfs_init();\[0m
2026-05-03T00:42:22.2010146Z [36;1m#endif' "$KSU_KERNEL/core/init.c"[0m
2026-05-03T00:42:22.2010374Z [36;1mfi[0m
2026-05-03T00:42:22.2010528Z [36;1m[0m
2026-05-03T00:42:22.2010748Z [36;1m# 5. Inject susfs includes into supercall/dispatch.c[0m
2026-05-03T00:42:22.2011277Z [36;1mif [ -f "$KSU_KERNEL/supercall/dispatch.c" ] && ! grep -q "susfs.h" "$KSU_KERNEL/supercall/dispatch.c"; then[0m
2026-05-03T00:42:22.2011943Z [36;1m  sed -i '/#include <linux\/version.h>/a #include <linux/susfs.h>' "$KSU_KERNEL/supercall/dispatch.c"[0m
2026-05-03T00:42:22.2012373Z [36;1mfi[0m
2026-05-03T00:42:22.2012530Z [36;1m[0m
2026-05-03T00:42:22.2012746Z [36;1mecho "=== Clean SUSFS Integration Complete ==="[0m
2026-05-03T00:42:22.2013015Z [36;1m[0m
2026-05-03T00:42:22.2013227Z [36;1m# --- Step 4: Post-integration validation ---[0m
2026-05-03T00:42:22.2013544Z [36;1mecho "=== Validating SUSFS configuration ==="[0m
2026-05-03T00:42:22.2013801Z [36;1m[0m
2026-05-03T00:42:22.2014052Z [36;1m# Verify init.c compiles conceptually: check for balanced braces[0m
2026-05-03T00:42:22.2014420Z [36;1mKSU_INIT="$KSU_DIR/kernel/core/init.c"[0m
2026-05-03T00:42:22.2014677Z [36;1mif [ -f "$KSU_INIT" ]; then[0m
2026-05-03T00:42:22.2014935Z [36;1m  OPEN=$(grep -c '{' "$KSU_INIT" || true)[0m
2026-05-03T00:42:22.2015223Z [36;1m  CLOSE=$(grep -c '}' "$KSU_INIT" || true)[0m
2026-05-03T00:42:22.2015488Z [36;1m  if [ "$OPEN" != "$CLOSE" ]; then[0m
2026-05-03T00:42:22.2015916Z [36;1m    echo "ERROR: Unbalanced braces in init.c! This should never happen with clean integration."[0m
2026-05-03T00:42:22.2016340Z [36;1m    exit 1[0m
2026-05-03T00:42:22.2016509Z [36;1m  fi[0m
2026-05-03T00:42:22.2016679Z [36;1m  echo "init.c syntax check OK"[0m
2026-05-03T00:42:22.2016906Z [36;1mfi[0m
2026-05-03T00:42:22.2017049Z [36;1m[0m
2026-05-03T00:42:22.2017212Z [36;1m# Verify Kconfig has SUSFS entries[0m
2026-05-03T00:42:22.2017570Z [36;1mif grep -r "CONFIG_KSU_SUSFS" $KSU_DIR/kernel/Kconfig 2>/dev/null; then[0m
2026-05-03T00:42:22.2017937Z [36;1m  echo "SUSFS_OK=true" >> $GITHUB_ENV[0m
2026-05-03T00:42:22.2018200Z [36;1m  echo "SUSFS Kconfig verified OK"[0m
2026-05-03T00:42:22.2018424Z [36;1melse[0m
2026-05-03T00:42:22.2018818Z [36;1m  echo "SUSFS_OK=false" >> $GITHUB_ENV[0m
2026-05-03T00:42:22.2019196Z [36;1m  echo "WARNING: SUSFS Kconfig NOT found — SUSFS will NOT be enabled"[0m
2026-05-03T00:42:22.2019532Z [36;1mfi[0m
2026-05-03T00:42:22.2019678Z [36;1m[0m
2026-05-03T00:42:22.2019847Z [36;1m# Show final state of critical files[0m
2026-05-03T00:42:22.2020103Z [36;1mecho "=== Final init.c ==="[0m
2026-05-03T00:42:22.2020556Z [36;1mhead -50 "$KSU_DIR/kernel/core/init.c" 2>/dev/null || true[0m
2026-05-03T00:42:22.2020920Z [36;1mecho "=== Final Kconfig (SUSFS section) ==="[0m
2026-05-03T00:42:22.2021310Z [36;1mgrep -A2 "KSU_SUSFS" "$KSU_DIR/kernel/Kconfig" 2>/dev/null | head -20 || true[0m
2026-05-03T00:42:22.2042134Z shell: /usr/bin/bash -e {0}
2026-05-03T00:42:22.2042357Z env:
2026-05-03T00:42:22.2042541Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:42:22.2042803Z   ANDROID_VERSION: android15
2026-05-03T00:42:22.2043015Z   KERNEL_VERSION: 6.6
2026-05-03T00:42:22.2043190Z   KMI_GENERATION: 8
2026-05-03T00:42:22.2043365Z   KERNEL_NAME: Castorice
2026-05-03T00:42:22.2043545Z   DEVICE_CODE: fire
2026-05-03T00:42:22.2043715Z   KSU_DIR: KernelSU-Next
2026-05-03T00:42:22.2043894Z   KSU_VERSION: 1
2026-05-03T00:42:22.2044055Z   SUSFS_OK: 
2026-05-03T00:42:22.2044208Z   BUILT_KERNEL_VERSION: 
2026-05-03T00:42:22.2044386Z   ZIP_NAME: 
2026-05-03T00:42:22.2044537Z ##[endgroup]
2026-05-03T00:42:22.2128900Z Cloning into 'susfs4ksu'...
2026-05-03T00:42:22.6991358Z === Copying SUSFS source files ===
2026-05-03T00:42:22.7014645Z '../susfs4ksu/kernel_patches/fs/susfs.c' -> 'fs/susfs.c'
2026-05-03T00:42:22.7029249Z '../susfs4ksu/kernel_patches/include/linux/susfs.h' -> 'include/linux/susfs.h'
2026-05-03T00:42:22.7029814Z '../susfs4ksu/kernel_patches/include/linux/susfs_def.h' -> 'include/linux/susfs_def.h'
2026-05-03T00:42:22.7057314Z -rw-r--r-- 1 runner runner 55289 May  3 00:42 fs/susfs.c
2026-05-03T00:42:22.7057893Z -rw-r--r-- 1 runner runner  7334 May  3 00:42 include/linux/susfs.h
2026-05-03T00:42:22.7058304Z -rw-r--r-- 1 runner runner  4291 May  3 00:42 include/linux/susfs_def.h
2026-05-03T00:42:22.7072567Z === Applying kernel tree SUSFS patch ===
2026-05-03T00:42:22.7073472Z Applying: ../susfs4ksu/kernel_patches/50_add_susfs_in_gki-android15-6.6.patch
2026-05-03T00:42:23.0401232Z warning: adding embedded git repository: KernelSU-Next
2026-05-03T00:42:23.0401995Z hint: You've added another git repository inside your current repository.
2026-05-03T00:42:23.0402811Z hint: Clones of the outer repository will not contain the contents of
2026-05-03T00:42:23.0403528Z hint: the embedded repository and will not know how to obtain it.
2026-05-03T00:42:23.0404102Z hint: If you meant to add a submodule, use:
2026-05-03T00:42:23.0404498Z hint:
2026-05-03T00:42:23.0404797Z hint: 	git submodule add <url> KernelSU-Next
2026-05-03T00:42:23.0405199Z hint:
2026-05-03T00:42:23.0405597Z hint: If you added this path by mistake, you can remove it from the
2026-05-03T00:42:23.0406152Z hint: index with:
2026-05-03T00:42:23.0406433Z hint:
2026-05-03T00:42:23.0406726Z hint: 	git rm --cached KernelSU-Next
2026-05-03T00:42:23.0407105Z hint:
2026-05-03T00:42:23.0407442Z hint: See "git help submodule" for more information.
2026-05-03T00:42:23.0408129Z hint: Disable this message with "git config set advice.addEmbeddedRepo false"
2026-05-03T00:42:23.2206895Z Applied patch to 'drivers/input/input.c' cleanly.
2026-05-03T00:42:23.2211796Z Applied patch to 'fs/Makefile' cleanly.
2026-05-03T00:42:23.2221342Z Applied patch to 'fs/devpts/inode.c' cleanly.
2026-05-03T00:42:23.2226083Z error: repository lacks the necessary blob to perform 3-way merge.
2026-05-03T00:42:23.2226724Z Falling back to direct application...
2026-05-03T00:42:23.2294543Z Applied patch to 'fs/namei.c' cleanly.
2026-05-03T00:42:23.2352684Z Applied patch to 'fs/namespace.c' cleanly.
2026-05-03T00:42:23.2357851Z Applied patch to 'fs/notify/fdinfo.c' cleanly.
2026-05-03T00:42:23.2377794Z Applied patch to 'fs/open.c' cleanly.
2026-05-03T00:42:23.2384559Z error: repository lacks the necessary blob to perform 3-way merge.
2026-05-03T00:42:23.2385180Z Falling back to direct application...
2026-05-03T00:42:23.2389907Z Applied patch to 'fs/proc/bootconfig.c' cleanly.
2026-05-03T00:42:23.2396642Z Applied patch to 'fs/proc/fd.c' cleanly.
2026-05-03T00:42:23.2401790Z error: repository lacks the necessary blob to perform 3-way merge.
2026-05-03T00:42:23.2402672Z Falling back to direct application...
2026-05-03T00:42:23.2403134Z error: patch failed: fs/proc/task_mmu.c:897
2026-05-03T00:42:23.2403627Z error: fs/proc/task_mmu.c: patch does not apply
2026-05-03T00:42:23.2409190Z Applied patch to 'fs/proc_namespace.c' cleanly.
2026-05-03T00:42:23.2426412Z Applied patch to 'fs/read_write.c' cleanly.
2026-05-03T00:42:23.2434833Z Applied patch to 'fs/readdir.c' cleanly.
2026-05-03T00:42:23.2446291Z Applied patch to 'fs/stat.c' cleanly.
2026-05-03T00:42:23.2452613Z Applied patch to 'fs/statfs.c' cleanly.
2026-05-03T00:42:23.2455542Z error: repository lacks the necessary blob to perform 3-way merge.
2026-05-03T00:42:23.2456165Z Falling back to direct application...
2026-05-03T00:42:23.2471048Z Applied patch to 'kernel/reboot.c' cleanly.
2026-05-03T00:42:23.2499853Z Applied patch to 'kernel/sys.c' cleanly.
2026-05-03T00:42:23.2513942Z Applied patch to 'security/selinux/avc.c' cleanly.
2026-05-03T00:42:23.2904545Z patching file drivers/input/input.c
2026-05-03T00:42:23.2907690Z patching file fs/Makefile
2026-05-03T00:42:23.2908498Z patching file fs/devpts/inode.c
2026-05-03T00:42:23.2911188Z patching file fs/exec.c
2026-05-03T00:42:23.2912315Z Hunk #2 succeeded at 1929 (offset 1 line).
2026-05-03T00:42:23.2913020Z Hunk #3 succeeded at 1950 (offset 1 line).
2026-05-03T00:42:23.2916613Z patching file fs/namei.c
2026-05-03T00:42:23.2923323Z patching file fs/namespace.c
2026-05-03T00:42:23.2927573Z patching file fs/notify/fdinfo.c
2026-05-03T00:42:23.2929583Z patching file fs/open.c
2026-05-03T00:42:23.2932830Z patching file fs/proc/base.c
2026-05-03T00:42:23.2936108Z patching file fs/proc/bootconfig.c
2026-05-03T00:42:23.2936822Z patching file fs/proc/fd.c
2026-05-03T00:42:23.2939024Z patching file fs/proc/task_mmu.c
2026-05-03T00:42:23.2939519Z Hunk #2 succeeded at 392 (offset 129 lines).
2026-05-03T00:42:23.2939929Z Hunk #3 succeeded at 411 (offset 129 lines).
2026-05-03T00:42:23.2943573Z Hunk #4 succeeded at 487 (offset 148 lines).
2026-05-03T00:42:23.2944166Z Hunk #5 succeeded at 1102 with fuzz 1 (offset 148 lines).
2026-05-03T00:42:23.2944718Z Hunk #6 succeeded at 1180 (offset 148 lines).
2026-05-03T00:42:23.2945205Z Hunk #7 succeeded at 1973 (offset 148 lines).
2026-05-03T00:42:23.2945691Z Hunk #8 succeeded at 2051 (offset 148 lines).
2026-05-03T00:42:23.2946170Z patching file fs/proc_namespace.c
2026-05-03T00:42:23.2946599Z patching file fs/read_write.c
2026-05-03T00:42:23.2946997Z patching file fs/readdir.c
2026-05-03T00:42:23.2948199Z patching file fs/stat.c
2026-05-03T00:42:23.2950673Z patching file fs/statfs.c
2026-05-03T00:42:23.2952230Z patching file kernel/kallsyms.c
2026-05-03T00:42:23.2952768Z Hunk #2 succeeded at 805 (offset 3 lines).
2026-05-03T00:42:23.2954280Z patching file kernel/reboot.c
2026-05-03T00:42:23.2956475Z patching file kernel/sys.c
2026-05-03T00:42:23.2959065Z patching file security/selinux/avc.c
2026-05-03T00:42:23.2978668Z Kernel SUSFS patch applied via fuzz fallback
2026-05-03T00:42:23.2979618Z === Integrating SUSFS into KernelSU-Next (Clean Manual Method) ===
2026-05-03T00:42:23.3006397Z SUSFS Kconfig injected successfully
2026-05-03T00:42:23.3030370Z SUSFS Makefile entries injected successfully
2026-05-03T00:42:23.3114227Z === Clean SUSFS Integration Complete ===
2026-05-03T00:42:23.3114736Z === Validating SUSFS configuration ===
2026-05-03T00:42:23.3147277Z init.c syntax check OK
2026-05-03T00:42:23.3162556Z WARNING: SUSFS Kconfig NOT found — SUSFS will NOT be enabled
2026-05-03T00:42:23.3163229Z === Final init.c ===
2026-05-03T00:42:23.3171849Z #include <linux/export.h>
2026-05-03T00:42:23.3172342Z #include <linux/fs.h>
2026-05-03T00:42:23.3172670Z #include <linux/kobject.h>
2026-05-03T00:42:23.3173009Z #include <linux/module.h>
2026-05-03T00:42:23.3173350Z #include <linux/rcupdate.h>
2026-05-03T00:42:23.3173692Z #include <linux/sched.h>
2026-05-03T00:42:23.3174070Z #include <linux/workqueue.h>
2026-05-03T00:42:23.3174565Z #include <linux/susfs.h>
2026-05-03T00:42:23.3174888Z 
2026-05-03T00:42:23.3175024Z #include "policy/allowlist.h"
2026-05-03T00:42:23.3175641Z #include "policy/app_profile.h"
2026-05-03T00:42:23.3176179Z #include "policy/feature.h"
2026-05-03T00:42:23.3176701Z #include "klog.h" // IWYU pragma: keep
2026-05-03T00:42:23.3177141Z #include "manager/manager_observer.h"
2026-05-03T00:42:23.3177588Z #include "manager/throne_tracker.h"
2026-05-03T00:42:23.3177987Z #include "hook/syscall_hook_manager.h"
2026-05-03T00:42:23.3178367Z #include "runtime/ksud.h"
2026-05-03T00:42:23.3178859Z #include "runtime/ksud_boot.h"
2026-05-03T00:42:23.3179245Z #include "supercall/supercall.h"
2026-05-03T00:42:23.3179623Z #include "ksu.h"
2026-05-03T00:42:23.3179930Z #include "infra/file_wrapper.h"
2026-05-03T00:42:23.3180324Z #include "selinux/selinux.h"
2026-05-03T00:42:23.3180699Z #include "hook/syscall_hook.h"
2026-05-03T00:42:23.3180952Z 
2026-05-03T00:42:23.3181073Z #if defined(__x86_64__)
2026-05-03T00:42:23.3181400Z #include <asm/cpufeature.h>
2026-05-03T00:42:23.3181862Z #include <linux/version.h>
2026-05-03T00:42:23.3182224Z #ifndef X86_FEATURE_INDIRECT_SAFE
2026-05-03T00:42:23.3182827Z #error "FATAL: Your kernel is missing the indirect syscall bypass patches!"
2026-05-03T00:42:23.3183428Z #endif
2026-05-03T00:42:23.3183677Z #endif
2026-05-03T00:42:23.3184049Z 
2026-05-03T00:42:23.3184197Z // workaround for A12-5.10 kernel
2026-05-03T00:42:23.3184817Z // Some third-party kernel (e.g. linegaeOS) uses wrong toolchain, which supports
2026-05-03T00:42:23.3185610Z // CC_HAVE_STACKPROTECTOR_SYSREG while gki's toolchain doesn't.
2026-05-03T00:42:23.3186360Z // Therefore, ksu lkm, which uses gki toolchain, requires this __stack_chk_guard,
2026-05-03T00:42:23.3187070Z // while those third-party kernel can't provide.
2026-05-03T00:42:23.3187656Z // Thus, we manually provide it instead of using kernel's
2026-05-03T00:42:23.3188339Z #if defined(CONFIG_STACKPROTECTOR) &&                                          \
2026-05-03T00:42:23.3189223Z     (defined(CONFIG_ARM64) && defined(MODULE) &&                               \
2026-05-03T00:42:23.3189608Z      !defined(CONFIG_STACKPROTECTOR_PER_TASK))
2026-05-03T00:42:23.3189893Z #include <linux/stackprotector.h>
2026-05-03T00:42:23.3190129Z #include <linux/random.h>
2026-05-03T00:42:23.3190366Z unsigned long __stack_chk_guard __ro_after_init
2026-05-03T00:42:23.3190676Z     __attribute__((visibility("hidden")));
2026-05-03T00:42:23.3190852Z 
2026-05-03T00:42:23.3191106Z __attribute__((no_stack_protector)) void __init ksu_setup_stack_chk_guard()
2026-05-03T00:42:23.3191878Z {
2026-05-03T00:42:23.3192139Z     unsigned long canary;
2026-05-03T00:42:23.3192362Z 
2026-05-03T00:42:23.3192506Z === Final Kconfig (SUSFS section) ===
2026-05-03T00:42:23.3192897Z config KSU_SUSFS
2026-05-03T00:42:23.3193162Z 	bool "KernelSU addon - SUSFS"
2026-05-03T00:42:23.3193379Z 	depends on KSU
2026-05-03T00:42:23.3193543Z --
2026-05-03T00:42:23.3193690Z config KSU_SUSFS_SUS_PATH
2026-05-03T00:42:23.3193910Z 	bool "Enable to hide suspicious path"
2026-05-03T00:42:23.3194154Z 	depends on KSU_SUSFS
2026-05-03T00:42:23.3194326Z 	default y
2026-05-03T00:42:23.3194414Z 
2026-05-03T00:42:23.3194500Z config KSU_SUSFS_SUS_MOUNT
2026-05-03T00:42:23.3194715Z 	bool "Enable to hide suspicious mounts"
2026-05-03T00:42:23.3194953Z 	depends on KSU_SUSFS
2026-05-03T00:42:23.3195126Z 	default y
2026-05-03T00:42:23.3195216Z 
2026-05-03T00:42:23.3195288Z config KSU_SUSFS_SUS_KSTAT
2026-05-03T00:42:23.3195502Z 	bool "Enable to spoof suspicious kstat"
2026-05-03T00:42:23.3195734Z 	depends on KSU_SUSFS
2026-05-03T00:42:23.3195901Z 	default y
2026-05-03T00:42:23.3195985Z 
2026-05-03T00:42:23.3196064Z config KSU_SUSFS_SPOOF_UNAME
2026-05-03T00:42:23.3223087Z ##[group]Run cd kernel/common
2026-05-03T00:42:23.3223418Z [36;1mcd kernel/common[0m
2026-05-03T00:42:23.3223678Z [36;1mDEFCONFIG="arch/arm64/configs/gki_defconfig"[0m
2026-05-03T00:42:23.3223945Z [36;1m[0m
2026-05-03T00:42:23.3224111Z [36;1m# --- KernelSU ---[0m
2026-05-03T00:42:23.3224324Z [36;1mif [ "true" = "true" ]; then[0m
2026-05-03T00:42:23.3224562Z [36;1m  cat >> $DEFCONFIG << 'EOF'[0m
2026-05-03T00:42:23.3224768Z [36;1m[0m
2026-05-03T00:42:23.3224925Z [36;1m# KernelSU-Next[0m
2026-05-03T00:42:23.3225117Z [36;1mCONFIG_KSU=y[0m
2026-05-03T00:42:23.3225292Z [36;1mEOF[0m
2026-05-03T00:42:23.3225445Z [36;1mfi[0m
2026-05-03T00:42:23.3225593Z [36;1m[0m
2026-05-03T00:42:23.3225748Z [36;1m# --- SUSFS ---[0m
2026-05-03T00:42:23.3226002Z [36;1mif [ "false" = "true" ] && [ "true" = "true" ]; then[0m
2026-05-03T00:42:23.3226298Z [36;1m  cat >> $DEFCONFIG << 'EOF'[0m
2026-05-03T00:42:23.3226504Z [36;1m[0m
2026-05-03T00:42:23.3226647Z [36;1m# SUSFS[0m
2026-05-03T00:42:23.3226845Z [36;1mCONFIG_KSU_SUSFS=y[0m
2026-05-03T00:42:23.3227068Z [36;1mCONFIG_KSU_SUSFS_HAS_MAGIC_MOUNT=y[0m
2026-05-03T00:42:23.3227325Z [36;1mCONFIG_KSU_SUSFS_SUS_PATH=y[0m
2026-05-03T00:42:23.3227564Z [36;1mCONFIG_KSU_SUSFS_SUS_MOUNT=y[0m
2026-05-03T00:42:23.3227803Z [36;1mCONFIG_KSU_SUSFS_SUS_MAP=y[0m
2026-05-03T00:42:23.3228109Z [36;1mCONFIG_KSU_SUSFS_AUTO_ADD_SUS_KSU_DEFAULT_MOUNT=y[0m
2026-05-03T00:42:23.3228447Z [36;1mCONFIG_KSU_SUSFS_AUTO_ADD_SUS_BIND_MOUNT=y[0m
2026-05-03T00:42:23.3229001Z [36;1mCONFIG_KSU_SUSFS_SUS_KSTAT=y[0m
2026-05-03T00:42:23.3229251Z [36;1mCONFIG_KSU_SUSFS_TRY_UMOUNT=y[0m
2026-05-03T00:42:23.3229731Z [36;1mCONFIG_KSU_SUSFS_AUTO_ADD_TRY_UMOUNT_FOR_BIND_MOUNT=y[0m
2026-05-03T00:42:23.3230047Z [36;1mCONFIG_KSU_SUSFS_SPOOF_UNAME=y[0m
2026-05-03T00:42:23.3230293Z [36;1mCONFIG_KSU_SUSFS_ENABLE_LOG=y[0m
2026-05-03T00:42:23.3230561Z [36;1mCONFIG_KSU_SUSFS_HIDE_KSU_SUSFS_SYMBOLS=y[0m
2026-05-03T00:42:23.3230876Z [36;1mCONFIG_KSU_SUSFS_SPOOF_CMDLINE_OR_BOOTCONFIG=y[0m
2026-05-03T00:42:23.3231181Z [36;1mCONFIG_KSU_SUSFS_OPEN_REDIRECT=y[0m
2026-05-03T00:42:23.3231424Z [36;1mCONFIG_KSU_SUSFS_SUS_SU=n[0m
2026-05-03T00:42:23.3231636Z [36;1mEOF[0m
2026-05-03T00:42:23.3231783Z [36;1mfi[0m
2026-05-03T00:42:23.3231935Z [36;1m[0m
2026-05-03T00:42:23.3232163Z [36;1m# --- Module Loading (CRITICAL: allow vendor modules) ---[0m
2026-05-03T00:42:23.3232481Z [36;1mcat >> $DEFCONFIG << 'EOF'[0m
2026-05-03T00:42:23.3232696Z [36;1m[0m
2026-05-03T00:42:23.3232927Z [36;1m# Module Compatibility (allow vendor_boot modules to load)[0m
2026-05-03T00:42:23.3233251Z [36;1mCONFIG_MODVERSIONS=n[0m
2026-05-03T00:42:23.3233469Z [36;1mCONFIG_MODULE_SIG_FORCE=n[0m
2026-05-03T00:42:23.3233697Z [36;1mCONFIG_MODULE_SIG_ALL=n[0m
2026-05-03T00:42:23.3233901Z [36;1mEOF[0m
2026-05-03T00:42:23.3234065Z [36;1m[0m
2026-05-03T00:42:23.3234235Z [36;1m# --- Memory & CPU Optimization ---[0m
2026-05-03T00:42:23.3234488Z [36;1mcat >> $DEFCONFIG << 'EOF'[0m
2026-05-03T00:42:23.3234697Z [36;1m[0m
2026-05-03T00:42:23.3234857Z [36;1m# Memory & CPU Optimization[0m
2026-05-03T00:42:23.3235087Z [36;1mCONFIG_ZRAM=y[0m
2026-05-03T00:42:23.3235277Z [36;1mCONFIG_ZRAM_WRITEBACK=y[0m
2026-05-03T00:42:23.3235498Z [36;1mCONFIG_ZSMALLOC=y[0m
2026-05-03T00:42:23.3235703Z [36;1mCONFIG_COMPACTION=y[0m
2026-05-03T00:42:23.3235910Z [36;1mCONFIG_KSM=y[0m
2026-05-03T00:42:23.3236110Z [36;1mCONFIG_TRANSPARENT_HUGEPAGE=y[0m
2026-05-03T00:42:23.3236355Z [36;1mCONFIG_SLAB_FREELIST_RANDOM=y[0m
2026-05-03T00:42:23.3236601Z [36;1mCONFIG_HZ_1000=y[0m
2026-05-03T00:42:23.3236791Z [36;1mCONFIG_LRU_GEN=y[0m
2026-05-03T00:42:23.3236997Z [36;1mCONFIG_LRU_GEN_ENABLED=y[0m
2026-05-03T00:42:23.3237200Z [36;1mEOF[0m
2026-05-03T00:42:23.3237354Z [36;1m[0m
2026-05-03T00:42:23.3237512Z [36;1m# --- I/O Optimization ---[0m
2026-05-03T00:42:23.3237738Z [36;1mcat >> $DEFCONFIG << 'EOF'[0m
2026-05-03T00:42:23.3237938Z [36;1m[0m
2026-05-03T00:42:23.3238245Z [36;1m# I/O Optimization[0m
2026-05-03T00:42:23.3238454Z [36;1mCONFIG_IOSCHED_BFQ=y[0m
2026-05-03T00:42:23.3239114Z [36;1mCONFIG_BFQ_GROUP_IOSCHED=y[0m
2026-05-03T00:42:23.3239358Z [36;1mEOF[0m
2026-05-03T00:42:23.3239507Z [36;1m[0m
2026-05-03T00:42:23.3239669Z [36;1m# --- Networking ---[0m
2026-05-03T00:42:23.3239878Z [36;1mcat >> $DEFCONFIG << 'EOF'[0m
2026-05-03T00:42:23.3240085Z [36;1m[0m
2026-05-03T00:42:23.3240231Z [36;1m# Networking[0m
2026-05-03T00:42:23.3240423Z [36;1mCONFIG_TCP_CONG_ADVANCED=y[0m
2026-05-03T00:42:23.3240647Z [36;1mCONFIG_TCP_CONG_BBR=y[0m
2026-05-03T00:42:23.3240859Z [36;1mCONFIG_NET_SCH_FQ=y[0m
2026-05-03T00:42:23.3241077Z [36;1mCONFIG_IP_NF_TARGET_TTL=y[0m
2026-05-03T00:42:23.3241297Z [36;1mCONFIG_IP6_NF_TARGET_HL=y[0m
2026-05-03T00:42:23.3241503Z [36;1m[0m
2026-05-03T00:42:23.3241646Z [36;1m# IPSet[0m
2026-05-03T00:42:23.3241819Z [36;1mCONFIG_IP_SET=y[0m
2026-05-03T00:42:23.3242014Z [36;1mCONFIG_IP_SET_MAX=65534[0m
2026-05-03T00:42:23.3242237Z [36;1mCONFIG_IP_SET_BITMAP_IP=y[0m
2026-05-03T00:42:23.3242461Z [36;1mCONFIG_IP_SET_BITMAP_IPMAC=y[0m
2026-05-03T00:42:23.3242700Z [36;1mCONFIG_IP_SET_BITMAP_PORT=y[0m
2026-05-03T00:42:23.3242924Z [36;1mCONFIG_IP_SET_HASH_IP=y[0m
2026-05-03T00:42:23.3243149Z [36;1mCONFIG_IP_SET_HASH_IPMARK=y[0m
2026-05-03T00:42:23.3243380Z [36;1mCONFIG_IP_SET_HASH_IPPORT=y[0m
2026-05-03T00:42:23.3243610Z [36;1mCONFIG_IP_SET_HASH_IPPORTIP=y[0m
2026-05-03T00:42:23.3243856Z [36;1mCONFIG_IP_SET_HASH_IPPORTNET=y[0m
2026-05-03T00:42:23.3244097Z [36;1mCONFIG_IP_SET_HASH_IPMAC=y[0m
2026-05-03T00:42:23.3244326Z [36;1mCONFIG_IP_SET_HASH_MAC=y[0m
2026-05-03T00:42:23.3244701Z [36;1mCONFIG_IP_SET_HASH_NETPORTNET=y[0m
2026-05-03T00:42:23.3244947Z [36;1mCONFIG_IP_SET_HASH_NET=y[0m
2026-05-03T00:42:23.3245169Z [36;1mCONFIG_IP_SET_HASH_NETNET=y[0m
2026-05-03T00:42:23.3245395Z [36;1mCONFIG_IP_SET_HASH_NETPORT=y[0m
2026-05-03T00:42:23.3245632Z [36;1mCONFIG_IP_SET_HASH_NETIFACE=y[0m
2026-05-03T00:42:23.3245863Z [36;1mCONFIG_IP_SET_LIST_SET=y[0m
2026-05-03T00:42:23.3246067Z [36;1mEOF[0m
2026-05-03T00:42:23.3246212Z [36;1m[0m
2026-05-03T00:42:23.3246369Z [36;1m# --- Branding ---[0m
2026-05-03T00:42:23.3246577Z [36;1mcat >> $DEFCONFIG << 'EOF'[0m
2026-05-03T00:42:23.3246786Z [36;1m[0m
2026-05-03T00:42:23.3246929Z [36;1m# Branding[0m
2026-05-03T00:42:23.3247124Z [36;1mCONFIG_LOCALVERSION="-Castorice"[0m
2026-05-03T00:42:23.3247375Z [36;1mCONFIG_LOCALVERSION_AUTO=n[0m
2026-05-03T00:42:23.3247590Z [36;1mEOF[0m
2026-05-03T00:42:23.3247744Z [36;1m[0m
2026-05-03T00:42:23.3247911Z [36;1mecho "=== Defconfig additions ==="[0m
2026-05-03T00:42:23.3248166Z [36;1mtail -60 $DEFCONFIG[0m
2026-05-03T00:42:23.3269190Z shell: /usr/bin/bash -e {0}
2026-05-03T00:42:23.3269415Z env:
2026-05-03T00:42:23.3269603Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:42:23.3269862Z   ANDROID_VERSION: android15
2026-05-03T00:42:23.3270068Z   KERNEL_VERSION: 6.6
2026-05-03T00:42:23.3270247Z   KMI_GENERATION: 8
2026-05-03T00:42:23.3270430Z   KERNEL_NAME: Castorice
2026-05-03T00:42:23.3270613Z   DEVICE_CODE: fire
2026-05-03T00:42:23.3270785Z   KSU_DIR: KernelSU-Next
2026-05-03T00:42:23.3270969Z   KSU_VERSION: 1
2026-05-03T00:42:23.3271128Z   SUSFS_OK: false
2026-05-03T00:42:23.3271302Z   BUILT_KERNEL_VERSION: 
2026-05-03T00:42:23.3271485Z   ZIP_NAME: 
2026-05-03T00:42:23.3271647Z ##[endgroup]
2026-05-03T00:42:23.3370745Z === Defconfig additions ===
2026-05-03T00:42:23.3384075Z CONFIG_KUNIT_DEBUGFS=y
2026-05-03T00:42:23.3384454Z CONFIG_KUNIT_TEST=m
2026-05-03T00:42:23.3384770Z CONFIG_KUNIT_EXAMPLE_TEST=m
2026-05-03T00:42:23.3385143Z # CONFIG_KUNIT_DEFAULT_ENABLED is not set
2026-05-03T00:42:23.3385446Z # CONFIG_RUNTIME_TESTING_MENU is not set
2026-05-03T00:42:23.3385627Z 
2026-05-03T00:42:23.3385703Z # KernelSU-Next
2026-05-03T00:42:23.3385874Z CONFIG_KSU=y
2026-05-03T00:42:23.3385973Z 
2026-05-03T00:42:23.3386121Z # Module Compatibility (allow vendor_boot modules to load)
2026-05-03T00:42:23.3386438Z CONFIG_MODVERSIONS=n
2026-05-03T00:42:23.3387061Z CONFIG_MODULE_SIG_FORCE=n
2026-05-03T00:42:23.3387416Z CONFIG_MODULE_SIG_ALL=n
2026-05-03T00:42:23.3387624Z 
2026-05-03T00:42:23.3387745Z # Memory & CPU Optimization
2026-05-03T00:42:23.3388066Z CONFIG_ZRAM=y
2026-05-03T00:42:23.3388347Z CONFIG_ZRAM_WRITEBACK=y
2026-05-03T00:42:23.3388839Z CONFIG_ZSMALLOC=y
2026-05-03T00:42:23.3389033Z CONFIG_COMPACTION=y
2026-05-03T00:42:23.3389212Z CONFIG_KSM=y
2026-05-03T00:42:23.3389387Z CONFIG_TRANSPARENT_HUGEPAGE=y
2026-05-03T00:42:23.3389614Z CONFIG_SLAB_FREELIST_RANDOM=y
2026-05-03T00:42:23.3389823Z CONFIG_HZ_1000=y
2026-05-03T00:42:23.3389997Z CONFIG_LRU_GEN=y
2026-05-03T00:42:23.3390175Z CONFIG_LRU_GEN_ENABLED=y
2026-05-03T00:42:23.3390308Z 
2026-05-03T00:42:23.3390380Z # I/O Optimization
2026-05-03T00:42:23.3390554Z CONFIG_IOSCHED_BFQ=y
2026-05-03T00:42:23.3390743Z CONFIG_BFQ_GROUP_IOSCHED=y
2026-05-03T00:42:23.3390875Z 
2026-05-03T00:42:23.3390970Z # Networking
2026-05-03T00:42:23.3391140Z CONFIG_TCP_CONG_ADVANCED=y
2026-05-03T00:42:23.3391349Z CONFIG_TCP_CONG_BBR=y
2026-05-03T00:42:23.3391532Z CONFIG_NET_SCH_FQ=y
2026-05-03T00:42:23.3391715Z CONFIG_IP_NF_TARGET_TTL=y
2026-05-03T00:42:23.3391914Z CONFIG_IP6_NF_TARGET_HL=y
2026-05-03T00:42:23.3392042Z 
2026-05-03T00:42:23.3392109Z # IPSet
2026-05-03T00:42:23.3392260Z CONFIG_IP_SET=y
2026-05-03T00:42:23.3392433Z CONFIG_IP_SET_MAX=65534
2026-05-03T00:42:23.3392627Z CONFIG_IP_SET_BITMAP_IP=y
2026-05-03T00:42:23.3392834Z CONFIG_IP_SET_BITMAP_IPMAC=y
2026-05-03T00:42:23.3393047Z CONFIG_IP_SET_BITMAP_PORT=y
2026-05-03T00:42:23.3393259Z CONFIG_IP_SET_HASH_IP=y
2026-05-03T00:42:23.3393459Z CONFIG_IP_SET_HASH_IPMARK=y
2026-05-03T00:42:23.3393834Z CONFIG_IP_SET_HASH_IPPORT=y
2026-05-03T00:42:23.3394047Z CONFIG_IP_SET_HASH_IPPORTIP=y
2026-05-03T00:42:23.3394271Z CONFIG_IP_SET_HASH_IPPORTNET=y
2026-05-03T00:42:23.3394499Z CONFIG_IP_SET_HASH_IPMAC=y
2026-05-03T00:42:23.3394703Z CONFIG_IP_SET_HASH_MAC=y
2026-05-03T00:42:23.3394907Z CONFIG_IP_SET_HASH_NETPORTNET=y
2026-05-03T00:42:23.3395128Z CONFIG_IP_SET_HASH_NET=y
2026-05-03T00:42:23.3395332Z CONFIG_IP_SET_HASH_NETNET=y
2026-05-03T00:42:23.3395543Z CONFIG_IP_SET_HASH_NETPORT=y
2026-05-03T00:42:23.3395755Z CONFIG_IP_SET_HASH_NETIFACE=y
2026-05-03T00:42:23.3395970Z CONFIG_IP_SET_LIST_SET=y
2026-05-03T00:42:23.3396096Z 
2026-05-03T00:42:23.3396165Z # Branding
2026-05-03T00:42:23.3396339Z CONFIG_LOCALVERSION="-Castorice"
2026-05-03T00:42:23.3396574Z CONFIG_LOCALVERSION_AUTO=n
2026-05-03T00:42:23.3417169Z ##[group]Run cd kernel/common
2026-05-03T00:42:23.3417446Z [36;1mcd kernel/common[0m
2026-05-03T00:42:23.3417640Z [36;1m[0m
2026-05-03T00:42:23.3417868Z [36;1m# Remove protected exports (prevents build failures)[0m
2026-05-03T00:42:23.3418252Z [36;1mrm -rf android/abi_gki_protected_exports_* || true[0m
2026-05-03T00:42:23.3418554Z [36;1mif [ -f "BUILD.bazel" ]; then[0m
2026-05-03T00:42:23.3419198Z [36;1m  sed -i '/abi_gki_protected_exports/d' BUILD.bazel[0m
2026-05-03T00:42:23.3419542Z [36;1m  sed -i '/protected_exports/d' BUILD.bazel[0m
2026-05-03T00:42:23.3419841Z [36;1m  sed -i '/check_defconfig/d' BUILD.bazel[0m
2026-05-03T00:42:23.3420095Z [36;1mfi[0m
2026-05-03T00:42:23.3420244Z [36;1m[0m
2026-05-03T00:42:23.3420514Z [36;1mif [ -f "modules.bzl" ] && grep -q 'protected_modules = ' modules.bzl; then[0m
2026-05-03T00:42:23.3420983Z [36;1m  sed -i 's/protected_modules = \[.*\]/protected_modules = []/' modules.bzl[0m
2026-05-03T00:42:23.3421355Z [36;1mfi[0m
2026-05-03T00:42:23.3421500Z [36;1m[0m
2026-05-03T00:42:23.3421734Z [36;1mfor f in build.config.gki build.config.gki.aarch64; do[0m
2026-05-03T00:42:23.3422074Z [36;1m  [ -f "$f" ] && sed -i '/check_defconfig/d' "$f"[0m
2026-05-03T00:42:23.3422336Z [36;1mdone[0m
2026-05-03T00:42:23.3422489Z [36;1m[0m
2026-05-03T00:42:23.3422643Z [36;1m# Bypass ABI check script[0m
2026-05-03T00:42:23.3422994Z [36;1mPROT_SCRIPT="../build/kernel/abi/check_buildtime_symbol_protection.py"[0m
2026-05-03T00:42:23.3423381Z [36;1mif [ -f "$PROT_SCRIPT" ]; then[0m
2026-05-03T00:42:23.3423703Z [36;1m  perl -i -pe 's/^(\s*)return 1$/$1return 0/g' "$PROT_SCRIPT"[0m
2026-05-03T00:42:23.3424000Z [36;1mfi[0m
2026-05-03T00:42:23.3424148Z [36;1m[0m
2026-05-03T00:42:23.3424299Z [36;1m# Clean dirty flags[0m
2026-05-03T00:42:23.3424572Z [36;1mif [ -f "../build/kernel/kleaf/impl/stamp.bzl" ]; then[0m
2026-05-03T00:42:23.3425040Z [36;1m  sed -i '/stable_scmversion_cmd/s/-maybe-dirty//g' ../build/kernel/kleaf/impl/stamp.bzl[0m
2026-05-03T00:42:23.3425437Z [36;1mfi[0m
2026-05-03T00:42:23.3425688Z [36;1msed -i 's/-dirty//' scripts/setlocalversion 2>/dev/null || true[0m
2026-05-03T00:42:23.3426011Z [36;1m: > .scmversion[0m
2026-05-03T00:42:23.3426203Z [36;1m[0m
2026-05-03T00:42:23.3426363Z [36;1mecho "Build system patched"[0m
2026-05-03T00:42:23.3445404Z shell: /usr/bin/bash -e {0}
2026-05-03T00:42:23.3445620Z env:
2026-05-03T00:42:23.3445799Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:42:23.3446059Z   ANDROID_VERSION: android15
2026-05-03T00:42:23.3446270Z   KERNEL_VERSION: 6.6
2026-05-03T00:42:23.3446445Z   KMI_GENERATION: 8
2026-05-03T00:42:23.3446619Z   KERNEL_NAME: Castorice
2026-05-03T00:42:23.3446802Z   DEVICE_CODE: fire
2026-05-03T00:42:23.3446978Z   KSU_DIR: KernelSU-Next
2026-05-03T00:42:23.3447160Z   KSU_VERSION: 1
2026-05-03T00:42:23.3447324Z   SUSFS_OK: false
2026-05-03T00:42:23.3447493Z   BUILT_KERNEL_VERSION: 
2026-05-03T00:42:23.3447679Z   ZIP_NAME: 
2026-05-03T00:42:23.3447840Z ##[endgroup]
2026-05-03T00:42:23.3662942Z Build system patched
2026-05-03T00:42:23.3688527Z ##[group]Run cd kernel/common
2026-05-03T00:42:23.3689110Z [36;1mcd kernel/common[0m
2026-05-03T00:42:23.3689388Z [36;1mgit config --global user.name "github-actions[bot]"[0m
2026-05-03T00:42:23.3690018Z [36;1mgit config --global user.email "github-actions[bot]@users.noreply.github.com"[0m
2026-05-03T00:42:23.3690400Z [36;1mgit add -A[0m
2026-05-03T00:42:23.3690755Z [36;1mgit commit -m "Castorice: GKI kernel with KSU+SUSFS+optimizations" || true[0m
2026-05-03T00:42:23.3710217Z shell: /usr/bin/bash -e {0}
2026-05-03T00:42:23.3710435Z env:
2026-05-03T00:42:23.3710618Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:42:23.3710885Z   ANDROID_VERSION: android15
2026-05-03T00:42:23.3711098Z   KERNEL_VERSION: 6.6
2026-05-03T00:42:23.3711275Z   KMI_GENERATION: 8
2026-05-03T00:42:23.3711454Z   KERNEL_NAME: Castorice
2026-05-03T00:42:23.3711634Z   DEVICE_CODE: fire
2026-05-03T00:42:23.3711808Z   KSU_DIR: KernelSU-Next
2026-05-03T00:42:23.3711985Z   KSU_VERSION: 1
2026-05-03T00:42:23.3712176Z   SUSFS_OK: false
2026-05-03T00:42:23.3712342Z   BUILT_KERNEL_VERSION: 
2026-05-03T00:42:23.3712521Z   ZIP_NAME: 
2026-05-03T00:42:23.3712672Z ##[endgroup]
2026-05-03T00:42:23.7467477Z [detached HEAD cdce43a61] Castorice: GKI kernel with KSU+SUSFS+optimizations
2026-05-03T00:42:23.7468306Z  30 files changed, 6705 insertions(+), 519 deletions(-)
2026-05-03T00:42:23.7469055Z  delete mode 100644 android/abi_gki_protected_exports_aarch64
2026-05-03T00:42:23.7469462Z  create mode 100644 fs/exec.c.orig
2026-05-03T00:42:23.7469768Z  create mode 100644 fs/proc/task_mmu.c.orig
2026-05-03T00:42:23.7470081Z  create mode 100644 kernel/kallsyms.c.orig
2026-05-03T00:42:23.7503453Z ##[group]Run cd kernel
2026-05-03T00:42:23.7503711Z [36;1mcd kernel[0m
2026-05-03T00:42:23.7503936Z [36;1mecho "=== Building Castorice GKI Kernel ==="[0m
2026-05-03T00:42:23.7504228Z [36;1mtools/bazel build \[0m
2026-05-03T00:42:23.7504434Z [36;1m  --config=fast \[0m
2026-05-03T00:42:23.7504664Z [36;1m  //common:kernel_aarch64_dist 2>&1[0m
2026-05-03T00:42:23.7504937Z [36;1mecho "=== Build completed ==="[0m
2026-05-03T00:42:23.7525609Z shell: /usr/bin/bash -e {0}
2026-05-03T00:42:23.7525848Z env:
2026-05-03T00:42:23.7526034Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:42:23.7526296Z   ANDROID_VERSION: android15
2026-05-03T00:42:23.7526510Z   KERNEL_VERSION: 6.6
2026-05-03T00:42:23.7526692Z   KMI_GENERATION: 8
2026-05-03T00:42:23.7526878Z   KERNEL_NAME: Castorice
2026-05-03T00:42:23.7527073Z   DEVICE_CODE: fire
2026-05-03T00:42:23.7527258Z   KSU_DIR: KernelSU-Next
2026-05-03T00:42:23.7527444Z   KSU_VERSION: 1
2026-05-03T00:42:23.7527616Z   SUSFS_OK: false
2026-05-03T00:42:23.7527816Z   BUILT_KERNEL_VERSION: 
2026-05-03T00:42:23.7527994Z   ZIP_NAME: 
2026-05-03T00:42:23.7528158Z   SOURCE_DATE_EPOCH: 0
2026-05-03T00:42:23.7528337Z ##[endgroup]
2026-05-03T00:42:23.7568146Z === Building Castorice GKI Kernel ===
2026-05-03T00:42:23.8514482Z Extracting Bazel installation...
2026-05-03T00:42:25.0278480Z Starting local Bazel server and connecting to it...
2026-05-03T00:42:26.4285005Z Computing main repo mapping: 
2026-05-03T00:42:27.1979731Z Loading: 
2026-05-03T00:42:27.1990814Z Loading: 1 packages loaded
2026-05-03T00:42:28.4297367Z Loading: 1 packages loaded
2026-05-03T00:42:28.4299523Z     currently loading: common
2026-05-03T00:42:32.4048863Z Analyzing: target //common:kernel_aarch64_dist (2 packages loaded)
2026-05-03T00:42:32.5828435Z Analyzing: target //common:kernel_aarch64_dist (2 packages loaded, 0 targets configured)
2026-05-03T00:42:32.6013716Z Analyzing: target //common:kernel_aarch64_dist (2 packages loaded, 0 targets configured)
2026-05-03T00:42:32.6028985Z [0 / 1] checking cached actions
2026-05-03T00:42:33.6140243Z Analyzing: target //common:kernel_aarch64_dist (59 packages loaded, 304 targets configured)
2026-05-03T00:42:33.6280660Z [1 / 1] checking cached actions
2026-05-03T00:42:34.7766056Z Analyzing: target //common:kernel_aarch64_dist (66 packages loaded, 14952 targets configured)
2026-05-03T00:42:34.7789500Z [1 / 1] checking cached actions
2026-05-03T00:42:36.4430303Z Analyzing: target //common:kernel_aarch64_dist (73 packages loaded, 64405 targets configured)
2026-05-03T00:42:36.4439610Z [1 / 1] checking cached actions
2026-05-03T00:42:39.0659656Z INFO: Analyzed target //common:kernel_aarch64_dist (73 packages loaded, 98802 targets configured).
2026-05-03T00:42:39.0722086Z [1 / 2] [Prepa] Writing script common/kernel_aarch64_dist
2026-05-03T00:42:40.0900152Z [90 / 496] [Prepa] Writing repo mapping manifest for //build/kernel:abi_flatten_symbol_list [for tool]
2026-05-03T00:42:41.0922986Z [104 / 760] [Prepa] Creating symlink to in-tree tool @@//build/kernel:hermetic-tools/runextractor [for tool]
2026-05-03T00:42:42.4452663Z [267 / 760] checking cached actions
2026-05-03T00:42:43.7328936Z [332 / 760] Building Python zip: //build/kernel:init_ddk; 1s processwrapper-sandbox ... (3 actions, 2 running)
2026-05-03T00:42:44.7640150Z [337 / 760] Compiling build/kernel/kleaf/impl/arg_wrapper.cpp [for tool]; 1s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T00:42:45.8030091Z [364 / 760] Compiling pigz.c [for tool]; 0s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T00:42:46.8590244Z [387 / 760] Compiling pigz.c [for tool]; 1s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T00:42:47.8783671Z [408 / 760] Compiling common/tools/testing/selftests/futex/functional/futex_wait.c; 0s processwrapper-sandbox ... (3 actions, 2 running)
2026-05-03T00:42:48.8800084Z [425 / 760] Compiling src/zopfli/lz77.c [for tool]; 0s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T00:42:49.9740435Z [443 / 760] Compiling crc32.c [for tool]; 0s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T00:42:51.0260165Z [467 / 760] Compiling common/tools/testing/selftests/futex/functional/futex_wait_timeout.c; 0s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T00:42:52.1763475Z [495 / 760] Compiling common/tools/testing/selftests/timers/nsleep-lat.c; 0s processwrapper-sandbox ... (3 actions, 2 running)
2026-05-03T00:42:53.2094818Z [501 / 760] Compiling trees.c [for tool]; 1s processwrapper-sandbox ... (5 actions, 3 running)
2026-05-03T00:42:54.2673386Z [512 / 760] Compiling inffast.c [for tool]; 0s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T00:42:55.2783474Z [537 / 760] Linking external/_main~_repo_rules~pigz/pigz [for tool]; 0s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T00:42:56.3184012Z [564 / 760] Creating build environment (lto=default;trim) @@//common:kernel_aarch64_env; 0s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T00:42:57.4520445Z [590 / 760] Creating abi_symbollist and report @@//common:kernel_aarch64_kmi_symbol_list; 0s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T00:42:58.4620633Z [614 / 760] Creating abi_symbollist.raw @@//common:kernel_aarch64_raw_kmi_symbol_list; 0s processwrapper-sandbox ... (5 actions, 4 running)
2026-05-03T00:42:59.4542452Z [635 / 760] Determining scmversion @@//common:kernel_aarch64_config; 0s processwrapper-sandbox ... (5 actions, 4 running)
2026-05-03T00:43:00.4544832Z [661 / 760] Creating kernel config (lto=default;trim) @@//common:kernel_aarch64_config; 0s local ... (5 actions, 4 running)
2026-05-03T00:43:01.5719049Z [667 / 760] Creating kernel config (lto=default;trim) @@//common:kernel_aarch64_config; 1s local ... (5 actions, 4 running)
2026-05-03T00:43:02.6000212Z [677 / 760] Creating kernel config (lto=default;trim) @@//common:kernel_aarch64_config; 2s local ... (5 actions, 4 running)
2026-05-03T00:43:03.5980043Z [684 / 760] Creating kernel config (lto=default;trim) @@//common:kernel_aarch64_config; 3s local ... (5 actions, 4 running)
2026-05-03T00:43:04.7327092Z [695 / 760] Creating kernel config (lto=default;trim) @@//common:kernel_aarch64_config; 4s local ... (4 actions, 3 running)
2026-05-03T00:43:05.9060357Z [704 / 760] Creating kernel config (lto=default;trim) @@//common:kernel_aarch64_config; 6s local ... (4 actions, 3 running)
2026-05-03T00:43:06.9401223Z [734 / 760] Creating kernel config (lto=default;trim) @@//common:kernel_aarch64_config; 7s local ... (4 actions, 3 running)
2026-05-03T00:43:08.5979676Z [746 / 760] Creating kernel config (lto=default;trim) @@//common:kernel_aarch64_config; 8s local
2026-05-03T00:43:09.2405135Z INFO: From Creating kernel config (lto=default;trim) @@//common:kernel_aarch64_config:
2026-05-03T00:43:09.2408592Z arch/arm64/configs/gki_defconfig:798:warning: override: reassigning to symbol MODVERSIONS
2026-05-03T00:43:09.2409872Z arch/arm64/configs/gki_defconfig:803:warning: override: reassigning to symbol ZRAM
2026-05-03T00:43:09.2410932Z arch/arm64/configs/gki_defconfig:804:warning: override: reassigning to symbol ZRAM_WRITEBACK
2026-05-03T00:43:09.2411944Z arch/arm64/configs/gki_defconfig:808:warning: override: reassigning to symbol TRANSPARENT_HUGEPAGE
2026-05-03T00:43:09.2412983Z arch/arm64/configs/gki_defconfig:809:warning: override: reassigning to symbol SLAB_FREELIST_RANDOM
2026-05-03T00:43:09.2413954Z arch/arm64/configs/gki_defconfig:811:warning: override: reassigning to symbol LRU_GEN
2026-05-03T00:43:09.2414924Z arch/arm64/configs/gki_defconfig:812:warning: override: reassigning to symbol LRU_GEN_ENABLED
2026-05-03T00:43:09.2415804Z arch/arm64/configs/gki_defconfig:819:warning: override: reassigning to symbol TCP_CONG_ADVANCED
2026-05-03T00:43:09.2416398Z arch/arm64/configs/gki_defconfig:820:warning: override: reassigning to symbol TCP_CONG_BBR
2026-05-03T00:43:09.2416958Z arch/arm64/configs/gki_defconfig:821:warning: override: reassigning to symbol NET_SCH_FQ
2026-05-03T00:43:09.2417512Z arch/arm64/configs/gki_defconfig:846:warning: override: reassigning to symbol LOCALVERSION
2026-05-03T00:43:10.6014411Z [747 / 760] Building UAPI kernel headers kernel_aarch64_uapi_headers; 1s processwrapper-sandbox ... (3 actions running)
2026-05-03T00:43:20.6340353Z [747 / 760] Building UAPI kernel headers kernel_aarch64_uapi_headers; 11s processwrapper-sandbox ... (3 actions running)
2026-05-03T00:43:29.6149280Z [748 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 20s local ... (2 actions running)
2026-05-03T00:43:32.6184399Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 23s local
2026-05-03T00:43:43.6480047Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 34s local
2026-05-03T00:44:13.6470134Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 64s local
2026-05-03T00:45:13.7442149Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 124s local
2026-05-03T00:46:13.7530001Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 184s local
2026-05-03T00:47:13.7700529Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 244s local
2026-05-03T00:48:13.7745009Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 304s local
2026-05-03T00:49:13.7856312Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 364s local
2026-05-03T00:50:13.7970031Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 424s local
2026-05-03T00:51:13.8024449Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 484s local
2026-05-03T00:52:13.8118225Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 544s local
2026-05-03T00:53:13.8289910Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 604s local
2026-05-03T00:54:13.8389429Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 664s local
2026-05-03T00:55:13.8469898Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 724s local
2026-05-03T00:56:13.8598410Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 784s local
2026-05-03T00:57:13.8709884Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 844s local
2026-05-03T00:57:28.1759079Z ERROR: /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/BUILD.bazel:154:22: Building kernel (lto=default;trim) @@//common:kernel_aarch64 failed: (Exit 2): bash failed: error executing KernelBuild command (from target //common:kernel_aarch64) /bin/bash -c ... (remaining 1 argument skipped)
2026-05-03T00:57:28.1838060Z ld.lld: error: undefined symbol: susfs_is_current_ksu_domain
2026-05-03T00:57:28.1839450Z >>> referenced by proc_namespace.c:120 (/proc/self/cwd/common/fs/proc_namespace.c:120)
2026-05-03T00:57:28.1840565Z >>>               fs/proc_namespace.o:(show_vfsmnt) in archive vmlinux.a
2026-05-03T00:57:28.1841606Z >>> referenced by proc_namespace.c:163 (/proc/self/cwd/common/fs/proc_namespace.c:163)
2026-05-03T00:57:28.1842709Z >>>               fs/proc_namespace.o:(show_mountinfo) in archive vmlinux.a
2026-05-03T00:57:28.1843802Z >>> referenced by proc_namespace.c:234 (/proc/self/cwd/common/fs/proc_namespace.c:234)
2026-05-03T00:57:28.1844861Z >>>               fs/proc_namespace.o:(show_vfsstat) in archive vmlinux.a
2026-05-03T00:57:28.1845618Z >>> referenced 6 more times
2026-05-03T00:57:28.1846128Z 
2026-05-03T00:57:28.1846565Z ld.lld: error: undefined symbol: ksu_is_input_hook_enabled
2026-05-03T00:57:28.1847400Z >>> referenced by input.c
2026-05-03T00:57:28.1848132Z >>>               drivers/input/input.o:(__jump_table+0x8) in archive vmlinux.a
2026-05-03T00:57:28.1849166Z >>> referenced by input.c
2026-05-03T00:57:28.1849907Z >>>               drivers/input/input.o:(__jump_table+0x18) in archive vmlinux.a
2026-05-03T00:57:28.1850747Z >>> referenced by input.c
2026-05-03T00:57:28.1851495Z >>>               drivers/input/input.o:(__jump_table+0x28) in archive vmlinux.a
2026-05-03T00:57:28.1852399Z >>> referenced 4 more times
2026-05-03T00:57:28.1853209Z 
2026-05-03T00:57:28.1853631Z ld.lld: error: undefined symbol: susfs_ksu_sid
2026-05-03T00:57:28.1854506Z >>> referenced by avc.c:731 (/proc/self/cwd/common/security/selinux/avc.c:731)
2026-05-03T00:57:28.1855624Z >>>               security/selinux/avc.o:(avc_audit_post_callback) in archive vmlinux.a
2026-05-03T00:57:28.1856672Z >>> referenced by avc.c:731 (/proc/self/cwd/common/security/selinux/avc.c:731)
2026-05-03T00:57:28.1857712Z >>>               security/selinux/avc.o:(avc_audit_post_callback) in archive vmlinux.a
2026-05-03T00:57:28.1858523Z 
2026-05-03T00:57:28.1859215Z ld.lld: error: undefined symbol: susfs_priv_app_sid
2026-05-03T00:57:28.1860164Z >>> referenced by avc.c:733 (/proc/self/cwd/common/security/selinux/avc.c:733)
2026-05-03T00:57:28.1861193Z >>>               security/selinux/avc.o:(avc_audit_post_callback) in archive vmlinux.a
2026-05-03T00:57:28.1862291Z >>> referenced by avc.c:733 (/proc/self/cwd/common/security/selinux/avc.c:733)
2026-05-03T00:57:28.1863210Z >>>               security/selinux/avc.o:(avc_audit_post_callback) in archive vmlinux.a
2026-05-03T00:57:28.1863962Z 
2026-05-03T00:57:28.1864357Z ld.lld: error: undefined symbol: ksu_handle_devpts
2026-05-03T00:57:28.1865289Z >>> referenced by inode.c:600 (/proc/self/cwd/common/fs/devpts/inode.c:600)
2026-05-03T00:57:28.1866272Z >>>               fs/devpts/inode.o:(devpts_get_priv) in archive vmlinux.a
2026-05-03T00:57:28.1866938Z 
2026-05-03T00:57:28.1867292Z ld.lld: error: undefined symbol: ksu_handle_vfs_fstat
2026-05-03T00:57:28.1867819Z >>> referenced by stat.c:232 (/proc/self/cwd/common/fs/stat.c:232)
2026-05-03T00:57:28.1868488Z >>>               fs/stat.o:(vfs_fstat) in archive vmlinux.a
2026-05-03T00:57:28.1869603Z >>> referenced by stat.c:232 (/proc/self/cwd/common/fs/stat.c:232)
2026-05-03T00:57:28.1870498Z >>>               fs/stat.o:(vfs_fstatat) in archive vmlinux.a
2026-05-03T00:57:28.1871369Z >>> referenced by stat.c:232 (/proc/self/cwd/common/fs/stat.c:232)
2026-05-03T00:57:28.1872296Z >>>               fs/stat.o:(__arm64_sys_newfstat) in archive vmlinux.a
2026-05-03T00:57:28.1873059Z >>> referenced 2 more times
2026-05-03T00:57:28.1873469Z 
2026-05-03T00:57:28.1873896Z ld.lld: error: undefined symbol: ksu_handle_execveat_sucompat
2026-05-03T00:57:28.1874788Z >>> referenced by exec.c:1961 (/proc/self/cwd/common/fs/exec.c:1961)
2026-05-03T00:57:28.1875671Z >>>               fs/exec.o:(do_execveat_common) in archive vmlinux.a
2026-05-03T00:57:28.1876322Z 
2026-05-03T00:57:28.1876698Z ld.lld: error: undefined symbol: ksu_handle_execveat
2026-05-03T00:57:28.1877912Z >>> referenced by exec.c:1959 (/proc/self/cwd/common/fs/exec.c:1959)
2026-05-03T00:57:28.1879163Z >>>               fs/exec.o:(do_execveat_common) in archive vmlinux.a
2026-05-03T00:57:28.1879770Z 
2026-05-03T00:57:28.1880221Z ld.lld: error: undefined symbol: ksu_is_init_rc_hook_enabled
2026-05-03T00:57:28.1880988Z >>> referenced by stat.c
2026-05-03T00:57:28.1881636Z >>>               fs/stat.o:(__jump_table+0x8) in archive vmlinux.a
2026-05-03T00:57:28.1882369Z >>> referenced by stat.c
2026-05-03T00:57:28.1883020Z >>>               fs/stat.o:(__jump_table+0x18) in archive vmlinux.a
2026-05-03T00:57:28.1883734Z >>> referenced by stat.c
2026-05-03T00:57:28.1884384Z >>>               fs/stat.o:(__jump_table+0x38) in archive vmlinux.a
2026-05-03T00:57:28.1885119Z >>> referenced 3 more times
2026-05-03T00:57:28.1885558Z 
2026-05-03T00:57:28.1885990Z ld.lld: error: undefined symbol: ksu_handle_sys_read
2026-05-03T00:57:28.1886966Z >>> referenced by read_write.c:631 (/proc/self/cwd/common/fs/read_write.c:631)
2026-05-03T00:57:28.1887929Z >>>               fs/read_write.o:(__arm64_sys_read) in archive vmlinux.a
2026-05-03T00:57:28.1888573Z 
2026-05-03T00:57:28.1889319Z ld.lld: error: undefined symbol: ksu_handle_sys_reboot
2026-05-03T00:57:28.1890225Z >>> referenced by reboot.c:715 (/proc/self/cwd/common/kernel/reboot.c:715)
2026-05-03T00:57:28.1891285Z >>>               kernel/reboot.o:(__arm64_sys_reboot) in archive vmlinux.a
2026-05-03T00:57:28.1892316Z pahole: .tmp_vmlinux.btf: Invalid argument
2026-05-03T00:57:28.1893047Z ld.lld: error: .btf.vmlinux.bin.o: unknown file type
2026-05-03T00:57:28.1894232Z make[3]: *** [/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/scripts/Makefile.vmlinux:37: vmlinux] Error 1
2026-05-03T00:57:28.1895828Z make[2]: *** [/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/Makefile:1237: vmlinux] Error 2
2026-05-03T00:57:28.1897331Z make[1]: *** [/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/Makefile:252: __sub-make] Error 2
2026-05-03T00:57:28.1898338Z make: *** [Makefile:252: __sub-make] Error 2
2026-05-03T00:57:28.1899567Z -- KernelSU-Next Git repo detected at: /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/KernelSU-Next
2026-05-03T00:57:28.1900541Z -- KernelSU-Next version: 33129
2026-05-03T00:57:28.1901043Z -- KernelSU-Next tag: v3.2.0
2026-05-03T00:57:28.1901646Z -- KernelSU-Next new DCACHE flush: 1
2026-05-03T00:57:28.1902339Z -- KernelSU-Next Manager signature size: 0x3e6
2026-05-03T00:57:28.1903370Z -- KernelSU-Next Manager signature hash: 79e590113c4c4c0c222978e413a5faa801666957b1212a328e46c00c69821bf7
2026-05-03T00:57:28.2366713Z Target //common:kernel_aarch64_dist failed to build
2026-05-03T00:57:28.2367775Z Use --verbose_failures to see the command lines of failed build steps.
2026-05-03T00:57:28.2370440Z ERROR: /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/BUILD.bazel:154:22 Middleman _middlemen/common_Skernel_Uaarch64_Udist-runfiles failed: (Exit 2): bash failed: error executing KernelBuild command (from target //common:kernel_aarch64) /bin/bash -c ... (remaining 1 argument skipped)
2026-05-03T00:57:28.3221539Z INFO: Elapsed time: 904.374s, Critical Path: 873.74s
2026-05-03T00:57:28.3226702Z INFO: 750 processes: 438 internal, 2 local, 310 processwrapper-sandbox.
2026-05-03T00:57:28.3227669Z ERROR: Build did NOT complete successfully
2026-05-03T00:57:28.3393228Z ##[error]Process completed with exit code 1.
2026-05-03T00:57:28.3513601Z Post job cleanup.
2026-05-03T00:57:28.4417094Z [command]/usr/bin/git version
2026-05-03T00:57:28.4459203Z git version 2.53.0
2026-05-03T00:57:28.4491647Z Copying '/home/runner/.gitconfig' to '/home/runner/work/_temp/474a7232-c1f5-452c-8af0-0018390841e5/.gitconfig'
2026-05-03T00:57:28.4501789Z Temporarily overriding HOME='/home/runner/work/_temp/474a7232-c1f5-452c-8af0-0018390841e5' before making global git config changes
2026-05-03T00:57:28.4503137Z Adding repository directory to the temporary git global config as a safe directory
2026-05-03T00:57:28.4508382Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN
2026-05-03T00:57:28.4546105Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-05-03T00:57:28.4581449Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-05-03T00:57:28.4846353Z fatal: No url found for submodule path 'temp_susfs' in .gitmodules
2026-05-03T00:57:28.4919355Z ##[warning]The process '/usr/bin/git' failed with exit code 128
2026-05-03T00:57:28.5024265Z Cleaning up orphan processes
2026-05-03T00:57:28.5401457Z Terminate orphan process: pid (96235) (java.lang=ALL-UNNAMED)
2026-05-03T00:57:28.5474227Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
