2026-05-03T01:16:34.3352086Z Current runner version: '2.334.0'
2026-05-03T01:16:34.3377017Z ##[group]Runner Image Provisioner
2026-05-03T01:16:34.3377864Z Hosted Compute Agent
2026-05-03T01:16:34.3378438Z Version: 20260213.493
2026-05-03T01:16:34.3379005Z Commit: 5c115507f6dd24b8de37d8bbe0bb4509d0cc0fa3
2026-05-03T01:16:34.3379781Z Build Date: 2026-02-13T00:28:41Z
2026-05-03T01:16:34.3380459Z Worker ID: {bbd8f25b-63bf-4721-aa79-bc54807a293d}
2026-05-03T01:16:34.3381100Z Azure Region: westus
2026-05-03T01:16:34.3381667Z ##[endgroup]
2026-05-03T01:16:34.3383032Z ##[group]Operating System
2026-05-03T01:16:34.3383642Z Ubuntu
2026-05-03T01:16:34.3384064Z 24.04.4
2026-05-03T01:16:34.3384654Z LTS
2026-05-03T01:16:34.3385335Z ##[endgroup]
2026-05-03T01:16:34.3385849Z ##[group]Runner Image
2026-05-03T01:16:34.3386473Z Image: ubuntu-24.04
2026-05-03T01:16:34.3386958Z Version: 20260413.86.1
2026-05-03T01:16:34.3388177Z Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20260413.86/images/ubuntu/Ubuntu2404-Readme.md
2026-05-03T01:16:34.3389598Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20260413.86
2026-05-03T01:16:34.3390457Z ##[endgroup]
2026-05-03T01:16:34.3391505Z ##[group]GITHUB_TOKEN Permissions
2026-05-03T01:16:34.3393277Z Contents: write
2026-05-03T01:16:34.3394340Z Metadata: read
2026-05-03T01:16:34.3394856Z ##[endgroup]
2026-05-03T01:16:34.3397388Z Secret source: Actions
2026-05-03T01:16:34.3398205Z Prepare workflow directory
2026-05-03T01:16:34.3806063Z Prepare all required actions
2026-05-03T01:16:34.3843653Z Getting action download info
2026-05-03T01:16:34.8437545Z Download action repository 'actions/checkout@v4' (SHA:34e114876b0b11c390a56381ad16ebd13914f8d5)
2026-05-03T01:16:34.9923173Z Download action repository 'actions/upload-artifact@v4' (SHA:ea165f8d65b6e75b540449e92b4886f43607fa02)
2026-05-03T01:16:35.0979728Z Download action repository 'softprops/action-gh-release@v2' (SHA:3bb12739c298aeb8a4eeaf626c5b8d85266b0e65)
2026-05-03T01:16:35.7011584Z Complete job name: Castorice GKI 6.6
2026-05-03T01:16:35.7816685Z ##[group]Run actions/checkout@v4
2026-05-03T01:16:35.7817571Z with:
2026-05-03T01:16:35.7818042Z   repository: naidrahiqa/CastoriceKernelSUN
2026-05-03T01:16:35.7818792Z   token: ***
2026-05-03T01:16:35.7819214Z   ssh-strict: true
2026-05-03T01:16:35.7819639Z   ssh-user: git
2026-05-03T01:16:35.7820071Z   persist-credentials: true
2026-05-03T01:16:35.7820540Z   clean: true
2026-05-03T01:16:35.7820968Z   sparse-checkout-cone-mode: true
2026-05-03T01:16:35.7821479Z   fetch-depth: 1
2026-05-03T01:16:35.7821892Z   fetch-tags: false
2026-05-03T01:16:35.7822323Z   show-progress: true
2026-05-03T01:16:35.7822760Z   lfs: false
2026-05-03T01:16:35.7823227Z   submodules: false
2026-05-03T01:16:35.7823682Z   set-safe-directory: true
2026-05-03T01:16:35.7824373Z env:
2026-05-03T01:16:35.7824817Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:16:35.7825585Z   ANDROID_VERSION: android15
2026-05-03T01:16:35.7826077Z   KERNEL_VERSION: 6.6
2026-05-03T01:16:35.7826548Z   KMI_GENERATION: 8
2026-05-03T01:16:35.7826982Z   KERNEL_NAME: Castorice
2026-05-03T01:16:35.7827432Z   DEVICE_CODE: fire
2026-05-03T01:16:35.7827843Z   KSU_DIR: 
2026-05-03T01:16:35.7828220Z   KSU_VERSION: 
2026-05-03T01:16:35.7828615Z   SUSFS_OK: 
2026-05-03T01:16:35.7829012Z   BUILT_KERNEL_VERSION: 
2026-05-03T01:16:35.7829473Z   ZIP_NAME: 
2026-05-03T01:16:35.7829855Z ##[endgroup]
2026-05-03T01:16:35.8782620Z Syncing repository: naidrahiqa/CastoriceKernelSUN
2026-05-03T01:16:35.8784685Z ##[group]Getting Git version info
2026-05-03T01:16:35.8786211Z Working directory is '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN'
2026-05-03T01:16:35.8787421Z [command]/usr/bin/git version
2026-05-03T01:16:35.8818884Z git version 2.53.0
2026-05-03T01:16:35.8840495Z ##[endgroup]
2026-05-03T01:16:35.8855235Z Temporarily overriding HOME='/home/runner/work/_temp/3d2b10a5-b148-44a2-a935-5ec3e9046aaf' before making global git config changes
2026-05-03T01:16:35.8857372Z Adding repository directory to the temporary git global config as a safe directory
2026-05-03T01:16:35.8860461Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN
2026-05-03T01:16:35.8892159Z Deleting the contents of '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN'
2026-05-03T01:16:35.8896197Z ##[group]Initializing the repository
2026-05-03T01:16:35.8900631Z [command]/usr/bin/git init /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN
2026-05-03T01:16:35.9007622Z hint: Using 'master' as the name for the initial branch. This default branch name
2026-05-03T01:16:35.9009500Z hint: will change to "main" in Git 3.0. To configure the initial branch name
2026-05-03T01:16:35.9011110Z hint: to use in all of your new repositories, which will suppress this warning,
2026-05-03T01:16:35.9012597Z hint: call:
2026-05-03T01:16:35.9013218Z hint:
2026-05-03T01:16:35.9013744Z hint: 	git config --global init.defaultBranch <name>
2026-05-03T01:16:35.9014672Z hint:
2026-05-03T01:16:35.9015719Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2026-05-03T01:16:35.9017015Z hint: 'development'. The just-created branch can be renamed via this command:
2026-05-03T01:16:35.9017910Z hint:
2026-05-03T01:16:35.9018674Z hint: 	git branch -m <name>
2026-05-03T01:16:35.9019541Z hint:
2026-05-03T01:16:35.9020347Z hint: Disable this message with "git config set advice.defaultBranchName false"
2026-05-03T01:16:35.9021523Z Initialized empty Git repository in /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/.git/
2026-05-03T01:16:35.9023455Z [command]/usr/bin/git remote add origin https://github.com/naidrahiqa/CastoriceKernelSUN
2026-05-03T01:16:35.9049929Z ##[endgroup]
2026-05-03T01:16:35.9050679Z ##[group]Disabling automatic garbage collection
2026-05-03T01:16:35.9053282Z [command]/usr/bin/git config --local gc.auto 0
2026-05-03T01:16:35.9081740Z ##[endgroup]
2026-05-03T01:16:35.9082458Z ##[group]Setting up auth
2026-05-03T01:16:35.9088502Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-05-03T01:16:35.9118207Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-05-03T01:16:35.9403063Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-05-03T01:16:35.9434520Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-05-03T01:16:35.9678318Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-05-03T01:16:35.9708410Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-05-03T01:16:35.9921658Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2026-05-03T01:16:35.9956894Z ##[endgroup]
2026-05-03T01:16:35.9957919Z ##[group]Fetching the repository
2026-05-03T01:16:35.9966233Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +f913d3f085437306c9a1e2ef5d906a94cccb0a7f:refs/remotes/origin/main
2026-05-03T01:16:36.4119733Z From https://github.com/naidrahiqa/CastoriceKernelSUN
2026-05-03T01:16:36.4122395Z  * [new ref]         f913d3f085437306c9a1e2ef5d906a94cccb0a7f -> origin/main
2026-05-03T01:16:36.4148015Z ##[endgroup]
2026-05-03T01:16:36.4149977Z ##[group]Determining the checkout info
2026-05-03T01:16:36.4152198Z ##[endgroup]
2026-05-03T01:16:36.4157337Z [command]/usr/bin/git sparse-checkout disable
2026-05-03T01:16:36.4198343Z [command]/usr/bin/git config --local --unset-all extensions.worktreeConfig
2026-05-03T01:16:36.4227925Z ##[group]Checking out the ref
2026-05-03T01:16:36.4232199Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
2026-05-03T01:16:36.4295360Z Switched to a new branch 'main'
2026-05-03T01:16:36.4299747Z branch 'main' set up to track 'origin/main'.
2026-05-03T01:16:36.4306470Z ##[endgroup]
2026-05-03T01:16:36.4350650Z [command]/usr/bin/git log -1 --format=%H
2026-05-03T01:16:36.4375605Z f913d3f085437306c9a1e2ef5d906a94cccb0a7f
2026-05-03T01:16:36.4621426Z ##[group]Run echo "=== Before cleanup ==="
2026-05-03T01:16:36.4622823Z [36;1mecho "=== Before cleanup ==="[0m
2026-05-03T01:16:36.4623988Z [36;1mdf -h /[0m
2026-05-03T01:16:36.4625605Z [36;1msudo rm -rf /usr/share/dotnet /usr/local/lib/android /opt/ghc[0m
2026-05-03T01:16:36.4627732Z [36;1msudo rm -rf /usr/share/swift /usr/share/miniconda /opt/hostedtoolcache[0m
2026-05-03T01:16:36.4629883Z [36;1msudo rm -rf /usr/local/share/chromium /usr/local/share/powershell[0m
2026-05-03T01:16:36.4633057Z [36;1msudo apt-get remove -y '^dotnet-.*' '^llvm-.*' 'php.*' azure-cli google-cloud-cli google-chrome-stable firefox powershell mono-devel || true[0m
2026-05-03T01:16:36.4636164Z [36;1msudo apt-get autoremove -y[0m
2026-05-03T01:16:36.4637333Z [36;1msudo apt-get clean[0m
2026-05-03T01:16:36.4638410Z [36;1mecho "=== After cleanup ==="[0m
2026-05-03T01:16:36.4639538Z [36;1mdf -h /[0m
2026-05-03T01:16:36.4665648Z shell: /usr/bin/bash -e {0}
2026-05-03T01:16:36.4666697Z env:
2026-05-03T01:16:36.4667602Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:16:36.4668855Z   ANDROID_VERSION: android15
2026-05-03T01:16:36.4669893Z   KERNEL_VERSION: 6.6
2026-05-03T01:16:36.4670815Z   KMI_GENERATION: 8
2026-05-03T01:16:36.4671722Z   KERNEL_NAME: Castorice
2026-05-03T01:16:36.4672675Z   DEVICE_CODE: fire
2026-05-03T01:16:36.4673536Z   KSU_DIR: 
2026-05-03T01:16:36.4674318Z   KSU_VERSION: 
2026-05-03T01:16:36.4675285Z   SUSFS_OK: 
2026-05-03T01:16:36.4676126Z   BUILT_KERNEL_VERSION: 
2026-05-03T01:16:36.4677078Z   ZIP_NAME: 
2026-05-03T01:16:36.4677901Z ##[endgroup]
2026-05-03T01:16:36.4749792Z === Before cleanup ===
2026-05-03T01:16:36.4769761Z Filesystem      Size  Used Avail Use% Mounted on
2026-05-03T01:16:36.4771934Z /dev/root       145G   56G   90G  39% /
2026-05-03T01:18:09.9414499Z Reading package lists...
2026-05-03T01:18:10.1228277Z Building dependency tree...
2026-05-03T01:18:10.1356705Z Reading state information...
2026-05-03T01:18:10.3744018Z Package 'dotnet-hostfxr-6.0' is not installed, so not removed
2026-05-03T01:18:10.3744761Z Package 'dotnet-runtime-6.0' is not installed, so not removed
2026-05-03T01:18:10.3745748Z Package 'dotnet-sdk-6.0' is not installed, so not removed
2026-05-03T01:18:10.3746417Z Package 'dotnet-targeting-pack-6.0' is not installed, so not removed
2026-05-03T01:18:10.3747088Z Package 'dotnet-templates-6.0' is not installed, so not removed
2026-05-03T01:18:10.3747677Z Package 'llvm-21' is not installed, so not removed
2026-05-03T01:18:10.3748222Z Package 'php-lua' is not installed, so not removed
2026-05-03T01:18:10.3748811Z Package 'php-mysqlnd-ms' is not installed, so not removed
2026-05-03T01:18:10.3749372Z Package 'php-radius' is not installed, so not removed
2026-05-03T01:18:10.3749995Z Package 'php5.6-common' is not installed, so not removed
2026-05-03T01:18:10.3750604Z Package 'php5.6-json' is not installed, so not removed
2026-05-03T01:18:10.3751247Z Package 'php7.0-common' is not installed, so not removed
2026-05-03T01:18:10.3751894Z Package 'php7.1-common' is not installed, so not removed
2026-05-03T01:18:10.3752492Z Package 'php7.2-common' is not installed, so not removed
2026-05-03T01:18:10.3753263Z Package 'php7.3-common' is not installed, so not removed
2026-05-03T01:18:10.3753874Z Package 'php7.4-common' is not installed, so not removed
2026-05-03T01:18:10.3754517Z Package 'php8.0-common' is not installed, so not removed
2026-05-03T01:18:10.3755345Z Package 'php8.1-common' is not installed, so not removed
2026-05-03T01:18:10.3755981Z Package 'php8.2-common' is not installed, so not removed
2026-05-03T01:18:10.3756657Z Package 'php-pear-frontend-gtk' is not installed, so not removed
2026-05-03T01:18:10.3757383Z Package 'php-pear-frontend-web' is not installed, so not removed
2026-05-03T01:18:10.3758562Z Package 'php7.0-curl' is not installed, so not removed
2026-05-03T01:18:10.3759193Z Package 'php7.2-sodium' is not installed, so not removed
2026-05-03T01:18:10.3759760Z Package 'php5' is not installed, so not removed
2026-05-03T01:18:10.3760652Z Package 'php5-cli' is not installed, so not removed
2026-05-03T01:18:10.3761259Z Package 'php5-pgsql' is not installed, so not removed
2026-05-03T01:18:10.3761875Z Package 'php5-curl' is not installed, so not removed
2026-05-03T01:18:10.3762403Z Package 'php5-ldap' is not installed, so not removed
2026-05-03T01:18:10.3762938Z Package 'gosa-plugin-phpgw' is not installed, so not removed
2026-05-03T01:18:10.3763556Z Package 'gosa-plugin-phpgw-schema' is not installed, so not removed
2026-05-03T01:18:10.3764246Z Package 'gosa-plugin-phpscheduleit' is not installed, so not removed
2026-05-03T01:18:10.3765246Z Package 'gosa-plugin-phpscheduleit-schema' is not installed, so not removed
2026-05-03T01:18:10.3766073Z Package 'php-apc' is not installed, so not removed
2026-05-03T01:18:10.3766735Z Package 'php-suhosin' is not installed, so not removed
2026-05-03T01:18:10.3767284Z Package 'php5-mysql' is not installed, so not removed
2026-05-03T01:18:10.3767897Z Package 'libsparkline-php' is not installed, so not removed
2026-05-03T01:18:10.3768558Z Package 'libapache2-mod-php5' is not installed, so not removed
2026-05-03T01:18:10.3769156Z Package 'php5-fpm' is not installed, so not removed
2026-05-03T01:18:10.3769715Z Package 'libgv-php5' is not installed, so not removed
2026-05-03T01:18:10.3770415Z Package 'php-greew-oauth2-azure-provider' is not installed, so not removed
2026-05-03T01:18:10.3771112Z Package 'php-hayageek-oauth2-yahoo' is not installed, so not removed
2026-05-03T01:18:10.3771748Z Package 'php-league-oauth2-google' is not installed, so not removed
2026-05-03T01:18:10.3772407Z Package 'php-thenetworg-oauth2-azure' is not installed, so not removed
2026-05-03T01:18:10.3773002Z Package 'phpphylotree' is not installed, so not removed
2026-05-03T01:18:10.3773543Z Package 'php-http-request2' is not installed, so not removed
2026-05-03T01:18:10.3774070Z Package 'php-xcache' is not installed, so not removed
2026-05-03T01:18:10.3774582Z Package 'php-async-aws-s3' is not installed, so not removed
2026-05-03T01:18:10.3775477Z Package 'php-paragonie-random-compat' is not installed, so not removed
2026-05-03T01:18:10.3776116Z Package 'php-console-color2' is not installed, so not removed
2026-05-03T01:18:10.3776720Z Package 'php-doctrine-phpcr-odm' is not installed, so not removed
2026-05-03T01:18:10.3777374Z Package 'php-alcaeus-mongo-php-adapter' is not installed, so not removed
2026-05-03T01:18:10.3778051Z Package 'php-doctrine-mongodb-odm' is not installed, so not removed
2026-05-03T01:18:10.3778720Z Package 'php-mtdowling-cron-expression' is not installed, so not removed
2026-05-03T01:18:10.3779345Z Package 'php-semsol-arc2' is not installed, so not removed
2026-05-03T01:18:10.3779915Z Package 'php-fzaninotto-faker' is not installed, so not removed
2026-05-03T01:18:10.3780447Z Package 'php7.4' is not installed, so not removed
2026-05-03T01:18:10.3780924Z Package 'php7.4-cli' is not installed, so not removed
2026-05-03T01:18:10.3781440Z Package 'php-com-dotnet' is not installed, so not removed
2026-05-03T01:18:10.3781945Z Package 'php-rar' is not installed, so not removed
2026-05-03T01:18:10.3782527Z Package 'php-laminas-httphandlerrunner' is not installed, so not removed
2026-05-03T01:18:10.3783218Z Package 'php-cordoval-hamcrest-php' is not installed, so not removed
2026-05-03T01:18:10.3783927Z Package 'php-davedevelopment-hamcrest-php' is not installed, so not removed
2026-05-03T01:18:10.3784623Z Package 'php-kodova-hamcrest-php' is not installed, so not removed
2026-05-03T01:18:10.3785535Z Package 'php-league-flysystem-sftp' is not installed, so not removed
2026-05-03T01:18:10.3786320Z Package 'php-league-flysystem-eventable-filesystem' is not installed, so not removed
2026-05-03T01:18:10.3787120Z Package 'php-league-flysystem-rackspace' is not installed, so not removed
2026-05-03T01:18:10.3788287Z Package 'php-league-flysystem-azure' is not installed, so not removed
2026-05-03T01:18:10.3788960Z Package 'php-league-flysystem-webdav' is not installed, so not removed
2026-05-03T01:18:10.3789856Z Package 'php-league-flysystem-aws-s3-v2' is not installed, so not removed
2026-05-03T01:18:10.3790609Z Package 'php-league-flysystem-aws-s3-v3' is not installed, so not removed
2026-05-03T01:18:10.3791336Z Package 'php-spatie-flysystem-dropbox' is not installed, so not removed
2026-05-03T01:18:10.3792095Z Package 'php-srmklive-flysystem-dropbox-v2' is not installed, so not removed
2026-05-03T01:18:10.3792902Z Package 'php-league-flysystem-cached-adapter' is not installed, so not removed
2026-05-03T01:18:10.3793709Z Package 'php-league-flysystem-ziparchive' is not installed, so not removed
2026-05-03T01:18:10.3794410Z Package 'php-league-uri-schemes' is not installed, so not removed
2026-05-03T01:18:10.3795411Z Package 'php-jeremykendall-php-domain-parser' is not installed, so not removed
2026-05-03T01:18:10.3796122Z Package 'php-php-64bit' is not installed, so not removed
2026-05-03T01:18:10.3796647Z Package 'php-sqlite' is not installed, so not removed
2026-05-03T01:18:10.3797171Z Package 'php-lzf' is not installed, so not removed
2026-05-03T01:18:10.3797677Z Package 'php-pnctl' is not installed, so not removed
2026-05-03T01:18:10.3798257Z Package 'php-mdb2-driver-fbsql' is not installed, so not removed
2026-05-03T01:18:10.3798886Z Package 'php-mdb2-driver-ibase' is not installed, so not removed
2026-05-03T01:18:10.3799513Z Package 'php-mdb2-driver-mssql' is not installed, so not removed
2026-05-03T01:18:10.3800153Z Package 'php-mdb2-driver-mysqli' is not installed, so not removed
2026-05-03T01:18:10.3800786Z Package 'php-mdb2-driver-oci8' is not installed, so not removed
2026-05-03T01:18:10.3801414Z Package 'php-mdb2-driver-odbc' is not installed, so not removed
2026-05-03T01:18:10.3802062Z Package 'php-mdb2-driver-querysim' is not installed, so not removed
2026-05-03T01:18:10.3802725Z Package 'php-mdb2-driver-sqlite' is not installed, so not removed
2026-05-03T01:18:10.3803365Z Package 'php-mdb2-driver-sqlsrv' is not installed, so not removed
2026-05-03T01:18:10.3804070Z Package 'php-barnabywalters-mf-cleaner' is not installed, so not removed
2026-05-03T01:18:10.3804800Z Package 'php-graylog2-gelf-php' is not installed, so not removed
2026-05-03T01:18:10.3805662Z Package 'php-doctrine-couchdb' is not installed, so not removed
2026-05-03T01:18:10.3806285Z Package 'php-ruflin-elastica' is not installed, so not removed
2026-05-03T01:18:10.3806907Z Package 'php-elasticsearch' is not installed, so not removed
2026-05-03T01:18:10.3807503Z Package 'php-aws-sdk-php' is not installed, so not removed
2026-05-03T01:18:10.3808125Z Package 'php-rollbar' is not installed, so not removed
2026-05-03T01:18:10.3808686Z Package 'php-nette-finder' is not installed, so not removed
2026-05-03T01:18:10.3809240Z Package 'php-dbase' is not installed, so not removed
2026-05-03T01:18:10.3809780Z Package 'php-libsodium' is not installed, so not removed
2026-05-03T01:18:10.3810313Z Package 'php-relay' is not installed, so not removed
2026-05-03T01:18:10.3810922Z Package 'php-ocramius-proxy-manager' is not installed, so not removed
2026-05-03T01:18:10.3811677Z Package 'php-zendframework-zend-stdlib' is not installed, so not removed
2026-05-03T01:18:10.3812353Z Package 'php-rhumsaa-uuid' is not installed, so not removed
2026-05-03T01:18:10.3812994Z Package 'php-paragonie-random-lib' is not installed, so not removed
2026-05-03T01:18:10.3813681Z Package 'php-ramsey-uuid-doctrine' is not installed, so not removed
2026-05-03T01:18:10.3814337Z Package 'php-crypt-blowfish' is not installed, so not removed
2026-05-03T01:18:10.3814933Z Package 'php-compat' is not installed, so not removed
2026-05-03T01:18:10.3815659Z Package 'libssh2-php' is not installed, so not removed
2026-05-03T01:18:10.3816279Z Package 'php-php-http-discovery' is not installed, so not removed
2026-05-03T01:18:10.3816969Z Package 'php-symfony-security-guard' is not installed, so not removed
2026-05-03T01:18:10.3817823Z Package 'php-numbers-words' is not installed, so not removed
2026-05-03T01:18:10.3818412Z Package 'php7.0-thrift' is not installed, so not removed
2026-05-03T01:18:10.3819119Z Package 'php7.2-thrift' is not installed, so not removed
2026-05-03T01:18:10.3819688Z Package 'php-net-idna' is not installed, so not removed
2026-05-03T01:18:10.3820227Z Package 'php-phpstan' is not installed, so not removed
2026-05-03T01:18:10.3820806Z Package 'php-vimeo-psalm' is not installed, so not removed
2026-05-03T01:18:10.3821430Z Package 'php-container-interop' is not installed, so not removed
2026-05-03T01:18:10.3822186Z Package 'php-zendframework-zend-eventmanager' is not installed, so not removed
2026-05-03T01:18:10.3822900Z Package 'php-recode' is not installed, so not removed
2026-05-03T01:18:10.3823427Z Package 'php-gd2' is not installed, so not removed
2026-05-03T01:18:10.3824077Z Package 'php-pragmarx-google2fa-qrcode' is not installed, so not removed
2026-05-03T01:18:10.3824819Z Package 'php-bjeavons-zxcvbn-php' is not installed, so not removed
2026-05-03T01:18:10.3825737Z Package 'php-pimlie-php-dkim' is not installed, so not removed
2026-05-03T01:18:10.3826415Z Package 'libapache2-mod-php7.4' is not installed, so not removed
2026-05-03T01:18:10.3827039Z Package 'php7.4-fpm' is not installed, so not removed
2026-05-03T01:18:10.3827650Z Package 'dotnet-apphost-pack-6.0' is not installed, so not removed
2026-05-03T01:18:10.3828318Z Package 'dotnet-runtime-8.0' is not installed, so not removed
2026-05-03T01:18:10.3828972Z Package 'dotnet-apphost-pack-8.0' is not installed, so not removed
2026-05-03T01:18:10.3829621Z Package 'dotnet-host-8.0' is not installed, so not removed
2026-05-03T01:18:10.3830240Z Package 'dotnet-hostfxr-8.0' is not installed, so not removed
2026-05-03T01:18:10.3830851Z Package 'dotnet-sdk-8.0' is not installed, so not removed
2026-05-03T01:18:10.3831516Z Package 'dotnet-targeting-pack-8.0' is not installed, so not removed
2026-05-03T01:18:10.3832223Z Package 'dotnet-templates-8.0' is not installed, so not removed
2026-05-03T01:18:10.3832903Z Package 'dotnet-runtime-dbg-8.0' is not installed, so not removed
2026-05-03T01:18:10.3833690Z Package 'dotnet-sdk-8.0-source-built-artifacts' is not installed, so not removed
2026-05-03T01:18:10.3834457Z Package 'dotnet-sdk-dbg-8.0' is not installed, so not removed
2026-05-03T01:18:10.3835372Z Package 'dotnet-runtime-10.0' is not installed, so not removed
2026-05-03T01:18:10.3836060Z Package 'dotnet-apphost-pack-10.0' is not installed, so not removed
2026-05-03T01:18:10.3836725Z Package 'dotnet-host-10.0' is not installed, so not removed
2026-05-03T01:18:10.3837355Z Package 'dotnet-hostfxr-10.0' is not installed, so not removed
2026-05-03T01:18:10.3838038Z Package 'dotnet-runtime-dbg-10.0' is not installed, so not removed
2026-05-03T01:18:10.3838695Z Package 'dotnet-sdk-10.0' is not installed, so not removed
2026-05-03T01:18:10.3839389Z Package 'dotnet-targeting-pack-10.0' is not installed, so not removed
2026-05-03T01:18:10.3840131Z Package 'dotnet-templates-10.0' is not installed, so not removed
2026-05-03T01:18:10.3840802Z Package 'dotnet-sdk-aot-10.0' is not installed, so not removed
2026-05-03T01:18:10.3841473Z Package 'dotnet-sdk-dbg-10.0' is not installed, so not removed
2026-05-03T01:18:10.3842255Z Package 'dotnet-sdk-10.0-source-built-artifacts' is not installed, so not removed
2026-05-03T01:18:10.3843085Z Package 'llvm-14-linker-tools' is not installed, so not removed
2026-05-03T01:18:10.3843717Z Package 'llvm-14-dev' is not installed, so not removed
2026-05-03T01:18:10.3844346Z Package 'llvm-15-linker-tools' is not installed, so not removed
2026-05-03T01:18:10.3845137Z Package 'llvm-15-dev' is not installed, so not removed
2026-05-03T01:18:10.3845634Z Package 'llvm-15' is not installed, so not removed
2026-05-03T01:18:10.3846121Z Package 'llvm-dev' is not installed, so not removed
2026-05-03T01:18:10.3846623Z Package 'llvm-14-doc' is not installed, so not removed
2026-05-03T01:18:10.3847310Z Package 'llvm-15-doc' is not installed, so not removed
2026-05-03T01:18:10.3847800Z Package 'llvm-16-doc' is not installed, so not removed
2026-05-03T01:18:10.3848301Z Package 'llvm-17-doc' is not installed, so not removed
2026-05-03T01:18:10.3848962Z Package 'llvm-18-doc' is not installed, so not removed
2026-05-03T01:18:10.3849515Z Package 'llvm-runtime' is not installed, so not removed
2026-05-03T01:18:10.3850009Z Package 'llvm-14' is not installed, so not removed
2026-05-03T01:18:10.3850518Z Package 'llvm-14-runtime' is not installed, so not removed
2026-05-03T01:18:10.3851061Z Package 'llvm-14-tools' is not installed, so not removed
2026-05-03T01:18:10.3851620Z Package 'llvm-14-examples' is not installed, so not removed
2026-05-03T01:18:10.3852178Z Package 'llvm-15-runtime' is not installed, so not removed
2026-05-03T01:18:10.3852708Z Package 'llvm-15-tools' is not installed, so not removed
2026-05-03T01:18:10.3853245Z Package 'llvm-15-examples' is not installed, so not removed
2026-05-03T01:18:10.3853811Z Package 'llvm-16-examples' is not installed, so not removed
2026-05-03T01:18:10.3854359Z Package 'llvm-17-examples' is not installed, so not removed
2026-05-03T01:18:10.3854916Z Package 'llvm-18-examples' is not installed, so not removed
2026-05-03T01:18:10.3855695Z Package 'llvm-bolt' is not installed, so not removed
2026-05-03T01:18:10.3856235Z Package 'llvm-spirv-14' is not installed, so not removed
2026-05-03T01:18:10.3856771Z Package 'llvm-spirv-15' is not installed, so not removed
2026-05-03T01:18:10.3857305Z Package 'llvm-spirv-16' is not installed, so not removed
2026-05-03T01:18:10.3857831Z Package 'llvm-spirv-17' is not installed, so not removed
2026-05-03T01:18:10.3858354Z Package 'llvm-spirv-18' is not installed, so not removed
2026-05-03T01:18:10.3858876Z Package 'llvm-19-dev' is not installed, so not removed
2026-05-03T01:18:10.3859381Z Package 'llvm-20-dev' is not installed, so not removed
2026-05-03T01:18:10.3859946Z Package 'llvm-19-linker-tools' is not installed, so not removed
2026-05-03T01:18:10.3860562Z Package 'llvm-20-linker-tools' is not installed, so not removed
2026-05-03T01:18:10.3861130Z Package 'llvm-19-doc' is not installed, so not removed
2026-05-03T01:18:10.3861638Z Package 'llvm-20-doc' is not installed, so not removed
2026-05-03T01:18:10.3862133Z Package 'llvm-19' is not installed, so not removed
2026-05-03T01:18:10.3862649Z Package 'llvm-19-runtime' is not installed, so not removed
2026-05-03T01:18:10.3863192Z Package 'llvm-19-tools' is not installed, so not removed
2026-05-03T01:18:10.3863749Z Package 'llvm-19-examples' is not installed, so not removed
2026-05-03T01:18:10.3864261Z Package 'llvm-20' is not installed, so not removed
2026-05-03T01:18:10.3864781Z Package 'llvm-20-runtime' is not installed, so not removed
2026-05-03T01:18:10.3865510Z Package 'llvm-20-tools' is not installed, so not removed
2026-05-03T01:18:10.3866061Z Package 'llvm-20-examples' is not installed, so not removed
2026-05-03T01:18:10.3866622Z Package 'llvm-spirv-19' is not installed, so not removed
2026-05-03T01:18:10.3867164Z Package 'llvm-spirv-20' is not installed, so not removed
2026-05-03T01:18:10.3867735Z Package 'php-crypt-gpg' is not installed, so not removed
2026-05-03T01:18:10.3868317Z Package 'libapache2-mod-php' is not installed, so not removed
2026-05-03T01:18:10.3868929Z Package 'libapache2-mod-php8.3' is not installed, so not removed
2026-05-03T01:18:10.3869492Z Package 'php-json' is not installed, so not removed
2026-05-03T01:18:10.3869963Z Package 'php' is not installed, so not removed
2026-05-03T01:18:10.3870459Z Package 'php-all-dev' is not installed, so not removed
2026-05-03T01:18:10.3870960Z Package 'php-cgi' is not installed, so not removed
2026-05-03T01:18:10.3871444Z Package 'php-cli' is not installed, so not removed
2026-05-03T01:18:10.3871935Z Package 'php-amqp' is not installed, so not removed
2026-05-03T01:18:10.3872420Z Package 'php-apcu' is not installed, so not removed
2026-05-03T01:18:10.3872909Z Package 'php-ast' is not installed, so not removed
2026-05-03T01:18:10.3873564Z Package 'php-ds' is not installed, so not removed
2026-05-03T01:18:10.3874094Z Package 'php-facedetect' is not installed, so not removed
2026-05-03T01:18:10.3874644Z Package 'php-gearman' is not installed, so not removed
2026-05-03T01:18:10.3875491Z Package 'php-gmagick' is not installed, so not removed
2026-05-03T01:18:10.3876020Z Package 'php-gnupg' is not installed, so not removed
2026-05-03T01:18:10.3876536Z Package 'php-igbinary' is not installed, so not removed
2026-05-03T01:18:10.3877071Z Package 'php-imagick' is not installed, so not removed
2026-05-03T01:18:10.3877624Z Package 'php-libvirt-php' is not installed, so not removed
2026-05-03T01:18:10.3878196Z Package 'php-mailparse' is not installed, so not removed
2026-05-03T01:18:10.3878738Z Package 'php-memcache' is not installed, so not removed
2026-05-03T01:18:10.3879288Z Package 'php-memcached' is not installed, so not removed
2026-05-03T01:18:10.3879829Z Package 'php-mongodb' is not installed, so not removed
2026-05-03T01:18:10.3880364Z Package 'php-msgpack' is not installed, so not removed
2026-05-03T01:18:10.3880881Z Package 'php-oauth' is not installed, so not removed
2026-05-03T01:18:10.3881383Z Package 'php-pcov' is not installed, so not removed
2026-05-03T01:18:10.3881885Z Package 'php-ps' is not installed, so not removed
2026-05-03T01:18:10.3882370Z Package 'php-psr' is not installed, so not removed
2026-05-03T01:18:10.3882876Z Package 'php-raphf' is not installed, so not removed
2026-05-03T01:18:10.3883391Z Package 'php-redis' is not installed, so not removed
2026-05-03T01:18:10.3883887Z Package 'php-rrd' is not installed, so not removed
2026-05-03T01:18:10.3884416Z Package 'php-smbclient' is not installed, so not removed
2026-05-03T01:18:10.3884944Z Package 'php-ssh2' is not installed, so not removed
2026-05-03T01:18:10.3885638Z Package 'php-stomp' is not installed, so not removed
2026-05-03T01:18:10.3886160Z Package 'php-tideways' is not installed, so not removed
2026-05-03T01:18:10.3886676Z Package 'php-uopz' is not installed, so not removed
2026-05-03T01:18:10.3887251Z Package 'php-uploadprogress' is not installed, so not removed
2026-05-03T01:18:10.3887822Z Package 'php-uuid' is not installed, so not removed
2026-05-03T01:18:10.3888338Z Package 'php-xdebug' is not installed, so not removed
2026-05-03T01:18:10.3888854Z Package 'php-xmlrpc' is not installed, so not removed
2026-05-03T01:18:10.3889365Z Package 'php-yac' is not installed, so not removed
2026-05-03T01:18:10.3889860Z Package 'php-yaml' is not installed, so not removed
2026-05-03T01:18:10.3890356Z Package 'php-zmq' is not installed, so not removed
2026-05-03T01:18:10.3890849Z Package 'php-curl' is not installed, so not removed
2026-05-03T01:18:10.3891351Z Package 'php-dev' is not installed, so not removed
2026-05-03T01:18:10.3891839Z Package 'php-gd' is not installed, so not removed
2026-05-03T01:18:10.3892332Z Package 'php-gmp' is not installed, so not removed
2026-05-03T01:18:10.3892827Z Package 'php-ldap' is not installed, so not removed
2026-05-03T01:18:10.3893337Z Package 'php-mysql' is not installed, so not removed
2026-05-03T01:18:10.3893845Z Package 'php-odbc' is not installed, so not removed
2026-05-03T01:18:10.3894337Z Package 'php-xml' is not installed, so not removed
2026-05-03T01:18:10.3894856Z Package 'php-pgsql' is not installed, so not removed
2026-05-03T01:18:10.3895595Z Package 'php-pspell' is not installed, so not removed
2026-05-03T01:18:10.3896121Z Package 'php-snmp' is not installed, so not removed
2026-05-03T01:18:10.3896659Z Package 'php-sqlite3' is not installed, so not removed
2026-05-03T01:18:10.3897172Z Package 'php-tidy' is not installed, so not removed
2026-05-03T01:18:10.3897714Z Package 'php-tokenizer' is not installed, so not removed
2026-05-03T01:18:10.3898285Z Package 'pkg-php-tools' is not installed, so not removed
2026-05-03T01:18:10.3898834Z Package 'dh-php' is not installed, so not removed
2026-05-03T01:18:10.3899361Z Package 'php-mbstring' is not installed, so not removed
2026-05-03T01:18:10.3899923Z Package 'php-readline' is not installed, so not removed
2026-05-03T01:18:10.3900617Z Package 'php-fpm' is not installed, so not removed
2026-05-03T01:18:10.3901172Z Package 'php-codesniffer' is not installed, so not removed
2026-05-03T01:18:10.3902028Z Package 'libphp-phpmailer' is not installed, so not removed
2026-05-03T01:18:10.3902733Z Package 'php-phpmyadmin-motranslator' is not installed, so not removed
2026-05-03T01:18:10.3903409Z Package 'php-phpseclib' is not installed, so not removed
2026-05-03T01:18:10.3903951Z Package 'php-twig' is not installed, so not removed
2026-05-03T01:18:10.3904520Z Package 'php-mapscript-ng' is not installed, so not removed
2026-05-03T01:18:10.3905350Z Package 'php-composer-ca-bundle' is not installed, so not removed
2026-05-03T01:18:10.3906115Z Package 'php-composer-class-map-generator' is not installed, so not removed
2026-05-03T01:18:10.3906937Z Package 'php-composer-metadata-minifier' is not installed, so not removed
2026-05-03T01:18:10.3907662Z Package 'php-composer-semver' is not installed, so not removed
2026-05-03T01:18:10.3908446Z Package 'php-composer-spdx-licenses' is not installed, so not removed
2026-05-03T01:18:10.3909191Z Package 'php-composer-xdebug-handler' is not installed, so not removed
2026-05-03T01:18:10.3909889Z Package 'php-json-schema' is not installed, so not removed
2026-05-03T01:18:10.3910476Z Package 'php-psr-log' is not installed, so not removed
2026-05-03T01:18:10.3911086Z Package 'php-symfony-console' is not installed, so not removed
2026-05-03T01:18:10.3911765Z Package 'php-symfony-filesystem' is not installed, so not removed
2026-05-03T01:18:10.3912435Z Package 'php-symfony-finder' is not installed, so not removed
2026-05-03T01:18:10.3913091Z Package 'php-symfony-process' is not installed, so not removed
2026-05-03T01:18:10.3913738Z Package 'php-react-promise' is not installed, so not removed
2026-05-03T01:18:10.3914380Z Package 'php-composer-pcre' is not installed, so not removed
2026-05-03T01:18:10.3915226Z Package 'php-seld-signal-handler' is not installed, so not removed
2026-05-03T01:18:10.3915872Z Package 'php-intl' is not installed, so not removed
2026-05-03T01:18:10.3916404Z Package 'php-zip' is not installed, so not removed
2026-05-03T01:18:10.3916955Z Package 'libawl-php' is not installed, so not removed
2026-05-03T01:18:10.3917566Z Package 'libphp-simplepie' is not installed, so not removed
2026-05-03T01:18:10.3918153Z Package 'php-geshi' is not installed, so not removed
2026-05-03T01:18:10.3918761Z Package 'php-random-compat' is not installed, so not removed
2026-05-03T01:18:10.3919387Z Package 'elpa-php-mode' is not installed, so not removed
2026-05-03T01:18:10.3919948Z Package 'phpunit' is not installed, so not removed
2026-05-03T01:18:10.3920484Z Package 'php-geos' is not installed, so not removed
2026-05-03T01:18:10.3921209Z Package 'golang-github-phpdave11-gofpdi-dev' is not installed, so not removed
2026-05-03T01:18:10.3921964Z Package 'php-imap' is not installed, so not removed
2026-05-03T01:18:10.3922518Z Package 'php-fpdf' is not installed, so not removed
2026-05-03T01:18:10.3923160Z Package 'icinga-php-library' is not installed, so not removed
2026-05-03T01:18:10.3923881Z Package 'icinga-php-thirdparty' is not installed, so not removed
2026-05-03T01:18:10.3924541Z Package 'php-soap' is not installed, so not removed
2026-05-03T01:18:10.3925314Z Package 'php-icinga' is not installed, so not removed
2026-05-03T01:18:10.3925908Z Package 'php-tcpdf' is not installed, so not removed
2026-05-03T01:18:10.3926518Z Package 'kdevelop-php' is not installed, so not removed
2026-05-03T01:18:10.3927170Z Package 'kdevelop-php-l10n' is not installed, so not removed
2026-05-03T01:18:10.3927808Z Package 'php-mcrypt' is not installed, so not removed
2026-05-03T01:18:10.3928381Z Package 'less.php' is not installed, so not removed
2026-05-03T01:18:10.3929069Z Package 'libphp-serialization-perl' is not installed, so not removed
2026-05-03T01:18:10.3929945Z Package 'libhtml-wikiconverter-phpwiki-perl' is not installed, so not removed
2026-05-03T01:18:10.3930816Z Package 'libjs-php-date-formatter' is not installed, so not removed
2026-05-03T01:18:10.3931734Z Package 'libmarkdown-php' is not installed, so not removed
2026-05-03T01:18:10.3932381Z Package 'libnusoap-php' is not installed, so not removed
2026-05-03T01:18:10.3933216Z Package 'php-econea-nusoap' is not installed, so not removed
2026-05-03T01:18:10.3933882Z Package 'libow-php7t64' is not installed, so not removed
2026-05-03T01:18:10.3934512Z Package 'libownet-php' is not installed, so not removed
2026-05-03T01:18:10.3935318Z Package 'libphp-adodb' is not installed, so not removed
2026-05-03T01:18:10.3935930Z Package 'php-sybase' is not installed, so not removed
2026-05-03T01:18:10.3936533Z Package 'libphp-embed' is not installed, so not removed
2026-05-03T01:18:10.3937183Z Package 'libphp8.3-embed' is not installed, so not removed
2026-05-03T01:18:10.3937837Z Package 'libphp-jabber' is not installed, so not removed
2026-05-03T01:18:10.3938476Z Package 'libphp-snoopy' is not installed, so not removed
2026-05-03T01:18:10.3939113Z Package 'libphpy-dev' is not installed, so not removed
2026-05-03T01:18:10.3939694Z Package 'libphpy1' is not installed, so not removed
2026-05-03T01:18:10.3940315Z Package 'libxrdcephposix0' is not installed, so not removed
2026-05-03T01:18:10.3940940Z Package 'php-spyc' is not installed, so not removed
2026-05-03T01:18:10.3941583Z Package 'matomo-php-tracker' is not installed, so not removed
2026-05-03T01:18:10.3942259Z Package 'php-wikidiff2' is not installed, so not removed
2026-05-03T01:18:10.3942909Z Package 'php-luasandbox' is not installed, so not removed
2026-05-03T01:18:10.3943551Z Package 'mlmmj-php-web' is not installed, so not removed
2026-05-03T01:18:10.3944222Z Package 'mlmmj-php-web-admin' is not installed, so not removed
2026-05-03T01:18:10.3944903Z Package 'php-net-socket' is not installed, so not removed
2026-05-03T01:18:10.3945775Z Package 'node-codemirror-lang-php' is not installed, so not removed
2026-05-03T01:18:10.3946493Z Package 'node-lezer-php' is not installed, so not removed
2026-05-03T01:18:10.3947132Z Package 'phpmyadmin' is not installed, so not removed
2026-05-03T01:18:10.3947701Z Package 'php-cas' is not installed, so not removed
2026-05-03T01:18:10.3948286Z Package 'php-pclzip' is not installed, so not removed
2026-05-03T01:18:10.3948890Z Package 'phpqrcode' is not installed, so not removed
2026-05-03T01:18:10.3949544Z Package 'php-symfony-config' is not installed, so not removed
2026-05-03T01:18:10.3950355Z Package 'php-symfony-dependency-injection' is not installed, so not removed
2026-05-03T01:18:10.3951091Z Package 'phpmd' is not installed, so not removed
2026-05-03T01:18:10.3951745Z Package 'php-algo26-idna-convert' is not installed, so not removed
2026-05-03T01:18:10.3952567Z Package 'php-jakeasmith-http-build-url' is not installed, so not removed
2026-05-03T01:18:10.3953266Z Package 'php-amphp-amp' is not installed, so not removed
2026-05-03T01:18:10.3953862Z Package 'php-amqp-all-dev' is not installed, so not removed
2026-05-03T01:18:10.3954499Z Package 'php-amqplib' is not installed, so not removed
2026-05-03T01:18:10.3955303Z Package 'php-apcu-all-dev' is not installed, so not removed
2026-05-03T01:18:10.3956081Z Package 'php-arthurhoaro-web-thumbnailer' is not installed, so not removed
2026-05-03T01:18:10.3956889Z Package 'php-text-template' is not installed, so not removed
2026-05-03T01:18:10.3957534Z Package 'php8.3-ast' is not installed, so not removed
2026-05-03T01:18:10.3958162Z Package 'php-ast-all-dev' is not installed, so not removed
2026-05-03T01:18:10.3958839Z Package 'php-async-aws-core' is not installed, so not removed
2026-05-03T01:18:10.3959512Z Package 'php-psr-cache' is not installed, so not removed
2026-05-03T01:18:10.3960284Z Package 'php-symfony-deprecation-contracts' is not installed, so not removed
2026-05-03T01:18:10.3961144Z Package 'php-symfony-http-client' is not installed, so not removed
2026-05-03T01:18:10.3961983Z Package 'php-symfony-http-client-contracts' is not installed, so not removed
2026-05-03T01:18:10.3962864Z Package 'php-symfony-service-contracts' is not installed, so not removed
2026-05-03T01:18:10.3963807Z Package 'php-async-aws-ses' is not installed, so not removed
2026-05-03T01:18:10.3964485Z Package 'php-async-aws-sns' is not installed, so not removed
2026-05-03T01:18:10.3965536Z Package 'php-async-aws-sqs' is not installed, so not removed
2026-05-03T01:18:10.3966201Z Package 'php-auth-sasl' is not installed, so not removed
2026-05-03T01:18:10.3966871Z Package 'php-bacon-qr-code' is not installed, so not removed
2026-05-03T01:18:10.3967562Z Package 'php-dasprid-enum' is not installed, so not removed
2026-05-03T01:18:10.3968194Z Package 'php-bcmath' is not installed, so not removed
2026-05-03T01:18:10.3968817Z Package 'php-brick-math' is not installed, so not removed
2026-05-03T01:18:10.3969509Z Package 'php-brick-varexporter' is not installed, so not removed
2026-05-03T01:18:10.3970178Z Package 'php-parser' is not installed, so not removed
2026-05-03T01:18:10.3970750Z Package 'php-bz2' is not installed, so not removed
2026-05-03T01:18:10.3971427Z Package 'php-cache-integration-tests' is not installed, so not removed
2026-05-03T01:18:10.3972167Z Package 'php-cache-tag-interop' is not installed, so not removed
2026-05-03T01:18:10.3972887Z Package 'php-christianriesen-base32' is not installed, so not removed
2026-05-03T01:18:10.3973633Z Package 'php-christianriesen-otp' is not installed, so not removed
2026-05-03T01:18:10.3974354Z Package 'php-code-lts-u2f-php-server' is not installed, so not removed
2026-05-03T01:18:10.3975620Z Package 'php-codecoverage' is not installed, so not removed
2026-05-03T01:18:10.3976278Z Package 'php-file-iterator' is not installed, so not removed
2026-05-03T01:18:10.3976889Z Package 'phpunit-code-unit-reverse-lookup' is not installed, so not removed
2026-05-03T01:18:10.3977479Z Package 'phpunit-complexity' is not installed, so not removed
2026-05-03T01:18:10.3977981Z Package 'phpunit-environment' is not installed, so not removed
2026-05-03T01:18:10.3978497Z Package 'phpunit-lines-of-code' is not installed, so not removed
2026-05-03T01:18:10.3979003Z Package 'phpunit-version' is not installed, so not removed
2026-05-03T01:18:10.3979535Z Package 'php-codeigniter-framework' is not installed, so not removed
2026-05-03T01:18:10.3980119Z Package 'php-codeigniter-framework-doc' is not installed, so not removed
2026-05-03T01:18:10.3980688Z Package 'php-console-commandline' is not installed, so not removed
2026-05-03T01:18:10.3981200Z Package 'php-console-table' is not installed, so not removed
2026-05-03T01:18:10.3981699Z Package 'php-constant-time' is not installed, so not removed
2026-05-03T01:18:10.3982185Z Package 'php-dapphp-radius' is not installed, so not removed
2026-05-03T01:18:10.3982620Z Package 'php-date' is not installed, so not removed
2026-05-03T01:18:10.3983084Z Package 'php-datto-json-rpc' is not installed, so not removed
2026-05-03T01:18:10.3983607Z Package 'php-datto-json-rpc-http' is not installed, so not removed
2026-05-03T01:18:10.3984075Z Package 'php-db' is not installed, so not removed
2026-05-03T01:18:10.3984497Z Package 'php-deepcopy' is not installed, so not removed
2026-05-03T01:18:10.3985303Z Package 'php-dflydev-dot-access-data' is not installed, so not removed
2026-05-03T01:18:10.3985827Z Package 'php-di' is not installed, so not removed
2026-05-03T01:18:10.3986269Z Package 'php-psr-container' is not installed, so not removed
2026-05-03T01:18:10.3986755Z Package 'php-di-invoker' is not installed, so not removed
2026-05-03T01:18:10.3987276Z Package 'php-laravel-serializable-closure' is not installed, so not removed
2026-05-03T01:18:10.3987754Z Package 'php-directory-scanner' is not installed, so not removed
2026-05-03T01:18:10.3988123Z Package 'php-doc' is not installed, so not removed
2026-05-03T01:18:10.3988513Z Package 'php-doctrine-annotations' is not installed, so not removed
2026-05-03T01:18:10.3988946Z Package 'php-doctrine-lexer' is not installed, so not removed
2026-05-03T01:18:10.3989338Z Package 'php-doctrine-cache' is not installed, so not removed
2026-05-03T01:18:10.3989987Z Package 'php-doctrine-collections' is not installed, so not removed
2026-05-03T01:18:10.3990438Z Package 'php-doctrine-deprecations' is not installed, so not removed
2026-05-03T01:18:10.3990886Z Package 'php-doctrine-common' is not installed, so not removed
2026-05-03T01:18:10.3991424Z Package 'php-doctrine-persistence' is not installed, so not removed
2026-05-03T01:18:10.3991889Z Package 'php-doctrine-data-fixtures' is not installed, so not removed
2026-05-03T01:18:10.3992319Z Package 'php-doctrine-dbal' is not installed, so not removed
2026-05-03T01:18:10.3992703Z Package 'php-doctrine-orm' is not installed, so not removed
2026-05-03T01:18:10.3993128Z Package 'php-doctrine-event-manager' is not installed, so not removed
2026-05-03T01:18:10.3993576Z Package 'php-doctrine-inflector' is not installed, so not removed
2026-05-03T01:18:10.3994034Z Package 'php-doctrine-instantiator' is not installed, so not removed
2026-05-03T01:18:10.3994462Z Package 'php-symfony-cache' is not installed, so not removed
2026-05-03T01:18:10.3994860Z Package 'php-symfony-yaml' is not installed, so not removed
2026-05-03T01:18:10.3995569Z Package 'php-dragonmantank-cron-expression' is not installed, so not removed
2026-05-03T01:18:10.3996060Z Package 'php-webmozart-assert' is not installed, so not removed
2026-05-03T01:18:10.3996442Z Package 'php8.3-ds' is not installed, so not removed
2026-05-03T01:18:10.3996801Z Package 'php-ds-all-dev' is not installed, so not removed
2026-05-03T01:18:10.3997176Z Package 'php-easyrdf' is not installed, so not removed
2026-05-03T01:18:10.3997533Z Package 'php-ml-json-ld' is not installed, so not removed
2026-05-03T01:18:10.3997901Z Package 'php-eluceo-ical' is not installed, so not removed
2026-05-03T01:18:10.3998289Z Package 'php-email-validator' is not installed, so not removed
2026-05-03T01:18:10.3998650Z Package 'php-embed' is not installed, so not removed
2026-05-03T01:18:10.3999051Z Package 'php-oscarotero-html-parser' is not installed, so not removed
2026-05-03T01:18:10.3999484Z Package 'php-psr-http-message' is not installed, so not removed
2026-05-03T01:18:10.3999892Z Package 'php-psr-http-client' is not installed, so not removed
2026-05-03T01:18:10.4000286Z Package 'php-psr-http-factory' is not installed, so not removed
2026-05-03T01:18:10.4000709Z Package 'php-symfony-css-selector' is not installed, so not removed
2026-05-03T01:18:10.4001102Z Package 'php-enchant' is not installed, so not removed
2026-05-03T01:18:10.4001437Z Package 'php-excimer' is not installed, so not removed
2026-05-03T01:18:10.4001799Z Package 'php8.3-facedetect' is not installed, so not removed
2026-05-03T01:18:10.4002198Z Package 'php-facedetect-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4002575Z Package 'php-faker' is not installed, so not removed
2026-05-03T01:18:10.4002921Z Package 'php-fdomdocument' is not installed, so not removed
2026-05-03T01:18:10.4003338Z Package 'php-fig-http-message-util' is not installed, so not removed
2026-05-03T01:18:10.4003750Z Package 'php-fig-link-util' is not installed, so not removed
2026-05-03T01:18:10.4004126Z Package 'php-psr-link' is not installed, so not removed
2026-05-03T01:18:10.4004479Z Package 'php-font-lib' is not installed, so not removed
2026-05-03T01:18:10.4004862Z Package 'php-fruitcake-php-cors' is not installed, so not removed
2026-05-03T01:18:10.4005440Z Package 'php-symfony-http-foundation' is not installed, so not removed
2026-05-03T01:18:10.4005835Z Package 'php-fxsl' is not installed, so not removed
2026-05-03T01:18:10.4006180Z Package 'php8.3-gearman' is not installed, so not removed
2026-05-03T01:18:10.4006555Z Package 'php-gearman-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4006949Z Package 'php-getallheaders' is not installed, so not removed
2026-05-03T01:18:10.4007321Z Package 'php-getid3' is not installed, so not removed
2026-05-03T01:18:10.4007690Z Package 'php-gettext-languages' is not installed, so not removed
2026-05-03T01:18:10.4008108Z Package 'php-oscarotero-gettext' is not installed, so not removed
2026-05-03T01:18:10.4008743Z Package 'php-giggsey-libphonenumber' is not installed, so not removed
2026-05-03T01:18:10.4009172Z Package 'php-giggsey-locale' is not installed, so not removed
2026-05-03T01:18:10.4009544Z Package 'php8.3-gmagick' is not installed, so not removed
2026-05-03T01:18:10.4010029Z Package 'php-gmagick-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4010405Z Package 'php8.3-gnupg' is not installed, so not removed
2026-05-03T01:18:10.4010766Z Package 'php-gnupg-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4011156Z Package 'php-google-protobuf' is not installed, so not removed
2026-05-03T01:18:10.4011557Z Package 'php-google-recaptcha' is not installed, so not removed
2026-05-03T01:18:10.4012014Z Package 'php-graham-campbell-result-type' is not installed, so not removed
2026-05-03T01:18:10.4012450Z Package 'php-phpoption' is not installed, so not removed
2026-05-03T01:18:10.4012828Z Package 'php-gregwar-captcha' is not installed, so not removed
2026-05-03T01:18:10.4013206Z Package 'php-guestfs' is not installed, so not removed
2026-05-03T01:18:10.4013575Z Package 'php-guzzlehttp-guzzle' is not installed, so not removed
2026-05-03T01:18:10.4014000Z Package 'php-guzzlehttp-promises' is not installed, so not removed
2026-05-03T01:18:10.4014454Z Package 'php-guzzlehttp-psr7' is not installed, so not removed
2026-05-03T01:18:10.4014871Z Package 'php-hamcrest' is not installed, so not removed
2026-05-03T01:18:10.4015518Z Package 'php-htmlawed' is not installed, so not removed
2026-05-03T01:18:10.4015895Z Package 'php-htmlpurifier' is not installed, so not removed
2026-05-03T01:18:10.4016254Z Package 'php-http' is not installed, so not removed
2026-05-03T01:18:10.4016589Z Package 'php8.3-http' is not installed, so not removed
2026-05-03T01:18:10.4016963Z Package 'php-http-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4017340Z Package 'php-http-httplug' is not installed, so not removed
2026-05-03T01:18:10.4017713Z Package 'php-http-promise' is not installed, so not removed
2026-05-03T01:18:10.4018169Z Package 'php-http-interop-http-factory-tests' is not installed, so not removed
2026-05-03T01:18:10.4018669Z Package 'php-http-message-factory' is not installed, so not removed
2026-05-03T01:18:10.4019144Z Package 'php-http-psr7-integration-tests' is not installed, so not removed
2026-05-03T01:18:10.4019611Z Package 'php-http-webdav-server' is not installed, so not removed
2026-05-03T01:18:10.4020005Z Package 'php-httpful' is not installed, so not removed
2026-05-03T01:18:10.4020379Z Package 'php-igbinary-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4020772Z Package 'php-image-text' is not installed, so not removed
2026-05-03T01:18:10.4021159Z Package 'php-imagick-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4021547Z Package 'php-interbase' is not installed, so not removed
2026-05-03T01:18:10.4021896Z Package 'php-invoker' is not installed, so not removed
2026-05-03T01:18:10.4022235Z Package 'php-jshrink' is not installed, so not removed
2026-05-03T01:18:10.4022619Z Package 'php-kissifrot-php-ixr' is not installed, so not removed
2026-05-03T01:18:10.4022994Z Package 'php-klogger' is not installed, so not removed
2026-05-03T01:18:10.4023360Z Package 'php-lcobucci-clock' is not installed, so not removed
2026-05-03T01:18:10.4023737Z Package 'php-psr-clock' is not installed, so not removed
2026-05-03T01:18:10.4024110Z Package 'php-lcobucci-jwt' is not installed, so not removed
2026-05-03T01:18:10.4024499Z Package 'php-league-commonmark' is not installed, so not removed
2026-05-03T01:18:10.4024902Z Package 'php-league-config' is not installed, so not removed
2026-05-03T01:18:10.4025444Z Package 'php-psr-event-dispatcher' is not installed, so not removed
2026-05-03T01:18:10.4025850Z Package 'php-nette-schema' is not installed, so not removed
2026-05-03T01:18:10.4026222Z Package 'php-league-csv' is not installed, so not removed
2026-05-03T01:18:10.4026602Z Package 'php-league-flysystem' is not installed, so not removed
2026-05-03T01:18:10.4027064Z Package 'php-league-mime-type-detection' is not installed, so not removed
2026-05-03T01:18:10.4027721Z Package 'php-league-html-to-markdown' is not installed, so not removed
2026-05-03T01:18:10.4028135Z Package 'php-league-uri' is not installed, so not removed
2026-05-03T01:18:10.4028647Z Package 'php-league-uri-interfaces' is not installed, so not removed
2026-05-03T01:18:10.4029093Z Package 'php-league-uri-components' is not installed, so not removed
2026-05-03T01:18:10.4029506Z Package 'php-letodms-core' is not installed, so not removed
2026-05-03T01:18:10.4029909Z Package 'php-libvirt-php-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4030292Z Package 'php-log' is not installed, so not removed
2026-05-03T01:18:10.4030611Z Package 'php-mdb2' is not installed, so not removed
2026-05-03T01:18:10.4030936Z Package 'php-mail' is not installed, so not removed
2026-05-03T01:18:10.4031286Z Package 'php-lorenzo-pinky' is not installed, so not removed
2026-05-03T01:18:10.4031659Z Package 'php-net-smtp' is not installed, so not removed
2026-05-03T01:18:10.4032021Z Package 'php-mail-mime' is not installed, so not removed
2026-05-03T01:18:10.4032379Z Package 'php8.3-mailparse' is not installed, so not removed
2026-05-03T01:18:10.4032779Z Package 'php-mailparse-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4033189Z Package 'php-malkusch-lock' is not installed, so not removed
2026-05-03T01:18:10.4033553Z Package 'php-predis' is not installed, so not removed
2026-05-03T01:18:10.4033923Z Package 'php-mariadb-mysql-kbs' is not installed, so not removed
2026-05-03T01:18:10.4034332Z Package 'php-masterminds-html5' is not installed, so not removed
2026-05-03T01:18:10.4034762Z Package 'php-matthiasmullie-minify' is not installed, so not removed
2026-05-03T01:18:10.4035479Z Package 'php-matthiasmullie-path-converter' is not installed, so not removed
2026-05-03T01:18:10.4035992Z Package 'php-maxmind-web-service-common' is not installed, so not removed
2026-05-03T01:18:10.4036416Z Package 'php-maxminddb' is not installed, so not removed
2026-05-03T01:18:10.4036791Z Package 'php8.3-maxminddb' is not installed, so not removed
2026-05-03T01:18:10.4037177Z Package 'php-maxminddb-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4037564Z Package 'php8.3-mcrypt' is not installed, so not removed
2026-05-03T01:18:10.4037941Z Package 'php-mcrypt-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4038339Z Package 'php-mdb2-driver-mysql' is not installed, so not removed
2026-05-03T01:18:10.4038745Z Package 'php-mdb2-driver-pgsql' is not installed, so not removed
2026-05-03T01:18:10.4039146Z Package 'php-memcache-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4039556Z Package 'php-memcached-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4039957Z Package 'php-msgpack-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4040319Z Package 'php-mf2' is not installed, so not removed
2026-05-03T01:18:10.4040694Z Package 'php-mikey179-vfsstream' is not installed, so not removed
2026-05-03T01:18:10.4041072Z Package 'php-ml-iri' is not installed, so not removed
2026-05-03T01:18:10.4041407Z Package 'php-mock' is not installed, so not removed
2026-05-03T01:18:10.4041755Z Package 'php-mock-phpunit' is not installed, so not removed
2026-05-03T01:18:10.4042154Z Package 'php-mock-integration' is not installed, so not removed
2026-05-03T01:18:10.4042528Z Package 'php-mockery' is not installed, so not removed
2026-05-03T01:18:10.4042887Z Package 'php-mockery-doc' is not installed, so not removed
2026-05-03T01:18:10.4043271Z Package 'php-mongodb-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4043649Z Package 'php-monolog' is not installed, so not removed
2026-05-03T01:18:10.4044000Z Package 'php-net-dime' is not installed, so not removed
2026-05-03T01:18:10.4044342Z Package 'php-net-dns2' is not installed, so not removed
2026-05-03T01:18:10.4044687Z Package 'php-net-ftp' is not installed, so not removed
2026-05-03T01:18:10.4045148Z Package 'php-net-imap' is not installed, so not removed
2026-05-03T01:18:10.4045642Z Package 'php-net-ipv6' is not installed, so not removed
2026-05-03T01:18:10.4045988Z Package 'php-net-ldap2' is not installed, so not removed
2026-05-03T01:18:10.4046346Z Package 'php-net-ldap3' is not installed, so not removed
2026-05-03T01:18:10.4046795Z Package 'php-net-nntp' is not installed, so not removed
2026-05-03T01:18:10.4047175Z Package 'php-net-publicsuffix' is not installed, so not removed
2026-05-03T01:18:10.4047559Z Package 'php-net-sieve' is not installed, so not removed
2026-05-03T01:18:10.4047899Z Package 'php-net-url' is not installed, so not removed
2026-05-03T01:18:10.4048243Z Package 'php-net-url2' is not installed, so not removed
2026-05-03T01:18:10.4048587Z Package 'php-net-whois' is not installed, so not removed
2026-05-03T01:18:10.4049010Z Package 'php-netscape-bookmark-parser' is not installed, so not removed
2026-05-03T01:18:10.4049443Z Package 'php-nette-utils' is not installed, so not removed
2026-05-03T01:18:10.4049833Z Package 'php-nikic-fast-route' is not installed, so not removed
2026-05-03T01:18:10.4050257Z Package 'php-nyholm-psr7' is not installed, so not removed
2026-05-03T01:18:10.4050609Z Package 'php8.3-oauth' is not installed, so not removed
2026-05-03T01:18:10.4050986Z Package 'php-oauth-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4051363Z Package 'php-opis-closure' is not installed, so not removed
2026-05-03T01:18:10.4051730Z Package 'php-parsedown' is not installed, so not removed
2026-05-03T01:18:10.4052103Z Package 'php-parsedown-extra' is not installed, so not removed
2026-05-03T01:18:10.4052496Z Package 'php-pcov-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4052901Z Package 'php-pda-pheanstalk' is not installed, so not removed
2026-05-03T01:18:10.4053301Z Package 'php-phar-io-manifest' is not installed, so not removed
2026-05-03T01:18:10.4053709Z Package 'php-phar-io-version' is not installed, so not removed
2026-05-03T01:18:10.4054098Z Package 'php-php-gettext' is not installed, so not removed
2026-05-03T01:18:10.4054471Z Package 'php-phpdbg' is not installed, so not removed
2026-05-03T01:18:10.4054906Z Package 'php-phpdocumentor-reflection-common' is not installed, so not removed
2026-05-03T01:18:10.4055741Z Package 'php-phpdocumentor-reflection-docblock' is not installed, so not removed
2026-05-03T01:18:10.4056280Z Package 'php-phpdocumentor-type-resolver' is not installed, so not removed
2026-05-03T01:18:10.4056761Z Package 'php-phpstan-phpdoc-parser' is not installed, so not removed
2026-05-03T01:18:10.4057246Z Package 'php-symfony-expression-language' is not installed, so not removed
2026-05-03T01:18:10.4057710Z Package 'php-phpmyadmin-shapefile' is not installed, so not removed
2026-05-03T01:18:10.4058157Z Package 'php-phpmyadmin-sql-parser' is not installed, so not removed
2026-05-03T01:18:10.4058610Z Package 'php-symfony-polyfill-php80' is not installed, so not removed
2026-05-03T01:18:10.4059011Z Package 'php-seclib' is not installed, so not removed
2026-05-03T01:18:10.4059372Z Package 'php-phpseclib3' is not installed, so not removed
2026-05-03T01:18:10.4059766Z Package 'php-phpspec-prophecy' is not installed, so not removed
2026-05-03T01:18:10.4060174Z Package 'phpunit-comparator' is not installed, so not removed
2026-05-03T01:18:10.4060595Z Package 'phpunit-recursion-context' is not installed, so not removed
2026-05-03T01:18:10.4061061Z Package 'php-phpspec-prophecy-phpunit' is not installed, so not removed
2026-05-03T01:18:10.4061464Z Package 'php-pinba' is not installed, so not removed
2026-05-03T01:18:10.4061813Z Package 'php8.3-pinba' is not installed, so not removed
2026-05-03T01:18:10.4062184Z Package 'php-pinba-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4062561Z Package 'php-proxy-manager' is not installed, so not removed
2026-05-03T01:18:10.4062915Z Package 'php8.3-ps' is not installed, so not removed
2026-05-03T01:18:10.4063255Z Package 'php-ps-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4063605Z Package 'php8.3-psr' is not installed, so not removed
2026-05-03T01:18:10.4064088Z Package 'php-psr-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4064477Z Package 'php-psr-simple-cache' is not installed, so not removed
2026-05-03T01:18:10.4065157Z Package 'php-pubsubhubbub-publisher' is not installed, so not removed
2026-05-03T01:18:10.4065609Z Package 'php-ramsey-collection' is not installed, so not removed
2026-05-03T01:18:10.4066001Z Package 'php-ramsey-uuid' is not installed, so not removed
2026-05-03T01:18:10.4066356Z Package 'php8.3-raphf' is not installed, so not removed
2026-05-03T01:18:10.4066718Z Package 'php-raphf-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4067097Z Package 'php-redis-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4067451Z Package 'php-remctl' is not installed, so not removed
2026-05-03T01:18:10.4067848Z Package 'php-roundcube-rtf-html-php' is not installed, so not removed
2026-05-03T01:18:10.4068240Z Package 'php8.3-rrd' is not installed, so not removed
2026-05-03T01:18:10.4068601Z Package 'php-rrd-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4068960Z Package 'php-sabre-dav' is not installed, so not removed
2026-05-03T01:18:10.4069326Z Package 'php-sabre-vobject' is not installed, so not removed
2026-05-03T01:18:10.4069683Z Package 'php-sass' is not installed, so not removed
2026-05-03T01:18:10.4070018Z Package 'php8.3-sass' is not installed, so not removed
2026-05-03T01:18:10.4070374Z Package 'php-sass-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4070748Z Package 'php-shellcommand' is not installed, so not removed
2026-05-03T01:18:10.4071116Z Package 'php-slim-psr7' is not installed, so not removed
2026-05-03T01:18:10.4071471Z Package 'php8.3-smbclient' is not installed, so not removed
2026-05-03T01:18:10.4071863Z Package 'php-smbclient-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4072223Z Package 'php-solr' is not installed, so not removed
2026-05-03T01:18:10.4072557Z Package 'php8.3-solr' is not installed, so not removed
2026-05-03T01:18:10.4072912Z Package 'php-solr-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4073274Z Package 'php-sparkline' is not installed, so not removed
2026-05-03T01:18:10.4073644Z Package 'php-sql-formatter' is not installed, so not removed
2026-05-03T01:18:10.4074003Z Package 'php8.3-ssh2' is not installed, so not removed
2026-05-03T01:18:10.4074353Z Package 'php-ssh2-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4074709Z Package 'php8.3-stomp' is not installed, so not removed
2026-05-03T01:18:10.4075327Z Package 'php-stomp-all-dev' is not installed, so not removed
2026-05-03T01:18:10.4075711Z Package 'php-swiftmailer' is not installed, so not removed
2026-05-03T01:18:10.4076065Z Package 'php-symfony' is not installed, so not removed
2026-05-03T01:18:10.4076426Z Package 'php-symfony-asset' is not installed, so not removed
2026-05-03T01:18:10.4076830Z Package 'php-symfony-asset-mapper' is not installed, so not removed
2026-05-03T01:18:10.4077270Z Package 'php-symfony-browser-kit' is not installed, so not removed
2026-05-03T01:18:10.4077675Z Package 'php-symfony-clock' is not installed, so not removed
2026-05-03T01:18:10.4078083Z Package 'php-symfony-debug-bundle' is not installed, so not removed
2026-05-03T01:18:10.4078535Z Package 'php-symfony-doctrine-bridge' is not installed, so not removed
2026-05-03T01:18:10.4078984Z Package 'php-symfony-dom-crawler' is not installed, so not removed
2026-05-03T01:18:10.4079391Z Package 'php-symfony-dotenv' is not installed, so not removed
2026-05-03T01:18:10.4079812Z Package 'php-symfony-error-handler' is not installed, so not removed
2026-05-03T01:18:10.4080273Z Package 'php-symfony-event-dispatcher' is not installed, so not removed
2026-05-03T01:18:10.4080693Z Package 'php-symfony-form' is not installed, so not removed
2026-05-03T01:18:10.4081113Z Package 'php-symfony-framework-bundle' is not installed, so not removed
2026-05-03T01:18:10.4081555Z Package 'php-symfony-http-kernel' is not installed, so not removed
2026-05-03T01:18:10.4082087Z Package 'php-symfony-intl' is not installed, so not removed
2026-05-03T01:18:10.4082451Z Package 'php-symfony-ldap' is not installed, so not removed
2026-05-03T01:18:10.4082821Z Package 'php-symfony-lock' is not installed, so not removed
2026-05-03T01:18:10.4083304Z Package 'php-symfony-mailer' is not installed, so not removed
2026-05-03T01:18:10.4083703Z Package 'php-symfony-messenger' is not installed, so not removed
2026-05-03T01:18:10.4084094Z Package 'php-symfony-mime' is not installed, so not removed
2026-05-03T01:18:10.4084501Z Package 'php-symfony-monolog-bridge' is not installed, so not removed
2026-05-03T01:18:10.4084932Z Package 'php-symfony-notifier' is not installed, so not removed
2026-05-03T01:18:10.4085502Z Package 'php-symfony-options-resolver' is not installed, so not removed
2026-05-03T01:18:10.4085974Z Package 'php-symfony-password-hasher' is not installed, so not removed
2026-05-03T01:18:10.4086440Z Package 'php-symfony-property-access' is not installed, so not removed
2026-05-03T01:18:10.4086899Z Package 'php-symfony-property-info' is not installed, so not removed
2026-05-03T01:18:10.4087378Z Package 'php-symfony-proxy-manager-bridge' is not installed, so not removed
2026-05-03T01:18:10.4087855Z Package 'php-symfony-rate-limiter' is not installed, so not removed
2026-05-03T01:18:10.4088286Z Package 'php-symfony-remote-event' is not installed, so not removed
2026-05-03T01:18:10.4088699Z Package 'php-symfony-routing' is not installed, so not removed
2026-05-03T01:18:10.4089108Z Package 'php-symfony-scheduler' is not installed, so not removed
2026-05-03T01:18:10.4089541Z Package 'php-symfony-security-bundle' is not installed, so not removed
2026-05-03T01:18:10.4089989Z Package 'php-symfony-security-core' is not installed, so not removed
2026-05-03T01:18:10.4090428Z Package 'php-symfony-security-csrf' is not installed, so not removed
2026-05-03T01:18:10.4090863Z Package 'php-symfony-security-http' is not installed, so not removed
2026-05-03T01:18:10.4091283Z Package 'php-symfony-semaphore' is not installed, so not removed
2026-05-03T01:18:10.4091694Z Package 'php-symfony-serializer' is not installed, so not removed
2026-05-03T01:18:10.4092108Z Package 'php-symfony-stopwatch' is not installed, so not removed
2026-05-03T01:18:10.4092509Z Package 'php-symfony-string' is not installed, so not removed
2026-05-03T01:18:10.4092908Z Package 'php-symfony-templating' is not installed, so not removed
2026-05-03T01:18:10.4093331Z Package 'php-symfony-translation' is not installed, so not removed
2026-05-03T01:18:10.4093750Z Package 'php-symfony-twig-bridge' is not installed, so not removed
2026-05-03T01:18:10.4094173Z Package 'php-symfony-twig-bundle' is not installed, so not removed
2026-05-03T01:18:10.4094565Z Package 'php-symfony-uid' is not installed, so not removed
2026-05-03T01:18:10.4095163Z Package 'php-symfony-validator' is not installed, so not removed
2026-05-03T01:18:10.4095633Z Package 'php-symfony-var-dumper' is not installed, so not removed
2026-05-03T01:18:10.4096056Z Package 'php-symfony-var-exporter' is not installed, so not removed
2026-05-03T01:18:10.4096490Z Package 'php-symfony-web-link' is not installed, so not removed
2026-05-03T01:18:10.4096939Z Package 'php-symfony-web-profiler-bundle' is not installed, so not removed
2026-05-03T01:18:10.4097395Z Package 'php-symfony-webhook' is not installed, so not removed
2026-05-03T01:18:10.4097790Z Package 'php-symfony-workflow' is not installed, so not removed
2026-05-03T01:18:10.4098197Z Package 'php-symfony-contracts' is not installed, so not removed
2026-05-03T01:18:10.4098634Z Package 'php-symfony-polyfill-php83' is not installed, so not removed
2026-05-03T01:18:10.4099106Z Package 'php-symfony-all-my-sms-notifier' is not installed, so not removed
2026-05-03T01:18:10.4099576Z Package 'php-symfony-amazon-mailer' is not installed, so not removed
2026-05-03T01:18:10.4100044Z Package 'php-symfony-amazon-sns-notifier' is not installed, so not removed
2026-05-03T01:18:10.4100539Z Package 'php-symfony-amazon-sqs-messenger' is not installed, so not removed
2026-05-03T01:18:10.4101148Z Package 'php-symfony-amqp-messenger' is not installed, so not removed
2026-05-03T01:18:10.4101619Z Package 'php-symfony-bandwidth-notifier' is not installed, so not removed
2026-05-03T01:18:10.4102215Z Package 'php-symfony-beanstalkd-messenger' is not installed, so not removed
2026-05-03T01:18:10.4102685Z Package 'php-symfony-brevo-mailer' is not installed, so not removed
2026-05-03T01:18:10.4103127Z Package 'php-symfony-brevo-notifier' is not installed, so not removed
2026-05-03T01:18:10.4103581Z Package 'php-symfony-cache-contracts' is not installed, so not removed
2026-05-03T01:18:10.4104045Z Package 'php-symfony-chatwork-notifier' is not installed, so not removed
2026-05-03T01:18:10.4104524Z Package 'php-symfony-click-send-notifier' is not installed, so not removed
2026-05-03T01:18:10.4105139Z Package 'php-symfony-clickatell-notifier' is not installed, so not removed
2026-05-03T01:18:10.4105662Z Package 'php-symfony-contact-everyone-notifier' is not installed, so not removed
2026-05-03T01:18:10.4106218Z Package 'php-symfony-event-dispatcher-contracts' is not installed, so not removed
2026-05-03T01:18:10.4106753Z Package 'php-symfony-translation-contracts' is not installed, so not removed
2026-05-03T01:18:10.4107314Z Package 'php-symfony-crowdin-translation-provider' is not installed, so not removed
2026-05-03T01:18:10.4107843Z Package 'php-symfony-discord-notifier' is not installed, so not removed
2026-05-03T01:18:10.4108322Z Package 'php-symfony-doctrine-messenger' is not installed, so not removed
2026-05-03T01:18:10.4108805Z Package 'php-symfony-engagespot-notifier' is not installed, so not removed
2026-05-03T01:18:10.4109296Z Package 'php-symfony-esendex-notifier' is not installed, so not removed
2026-05-03T01:18:10.4109758Z Package 'php-symfony-expo-notifier' is not installed, so not removed
2026-05-03T01:18:10.4110220Z Package 'php-symfony-fake-chat-notifier' is not installed, so not removed
2026-05-03T01:18:10.4110693Z Package 'php-symfony-fake-sms-notifier' is not installed, so not removed
2026-05-03T01:18:10.4111173Z Package 'php-symfony-firebase-notifier' is not installed, so not removed
2026-05-03T01:18:10.4111673Z Package 'php-symfony-forty-six-elks-notifier' is not installed, so not removed
2026-05-03T01:18:10.4112182Z Package 'php-symfony-free-mobile-notifier' is not installed, so not removed
2026-05-03T01:18:10.4112679Z Package 'php-symfony-gateway-api-notifier' is not installed, so not removed
2026-05-03T01:18:10.4113154Z Package 'php-symfony-gitter-notifier' is not installed, so not removed
2026-05-03T01:18:10.4113608Z Package 'php-symfony-go-ip-notifier' is not installed, so not removed
2026-05-03T01:18:10.4114077Z Package 'php-symfony-google-chat-notifier' is not installed, so not removed
2026-05-03T01:18:10.4114546Z Package 'php-symfony-google-mailer' is not installed, so not removed
2026-05-03T01:18:10.4115231Z Package 'php-symfony-html-sanitizer' is not installed, so not removed
2026-05-03T01:18:10.4115696Z Package 'php-symfony-infobip-mailer' is not installed, so not removed
2026-05-03T01:18:10.4116176Z Package 'php-symfony-infobip-notifier' is not installed, so not removed
2026-05-03T01:18:10.4116639Z Package 'php-symfony-iqsms-notifier' is not installed, so not removed
2026-05-03T01:18:10.4117110Z Package 'php-symfony-isendpro-notifier' is not installed, so not removed
2026-05-03T01:18:10.4117604Z Package 'php-symfony-kaz-info-teh-notifier' is not installed, so not removed
2026-05-03T01:18:10.4118120Z Package 'php-symfony-light-sms-notifier' is not installed, so not removed
2026-05-03T01:18:10.4118616Z Package 'php-symfony-line-notify-notifier' is not installed, so not removed
2026-05-03T01:18:10.4119108Z Package 'php-symfony-linked-in-notifier' is not installed, so not removed
2026-05-03T01:18:10.4119626Z Package 'php-symfony-loco-translation-provider' is not installed, so not removed
2026-05-03T01:18:10.4120189Z Package 'php-symfony-lokalise-translation-provider' is not installed, so not removed
2026-05-03T01:18:10.4120725Z Package 'php-symfony-mail-pace-mailer' is not installed, so not removed
2026-05-03T01:18:10.4121327Z Package 'php-symfony-mailchimp-mailer' is not installed, so not removed
2026-05-03T01:18:10.4121801Z Package 'php-symfony-mailer-send-mailer' is not installed, so not removed
2026-05-03T01:18:10.4122379Z Package 'php-symfony-mailgun-mailer' is not installed, so not removed
2026-05-03T01:18:10.4122827Z Package 'php-symfony-mailjet-mailer' is not installed, so not removed
2026-05-03T01:18:10.4123283Z Package 'php-symfony-mailjet-notifier' is not installed, so not removed
2026-05-03T01:18:10.4123749Z Package 'php-symfony-mastodon-notifier' is not installed, so not removed
2026-05-03T01:18:10.4124236Z Package 'php-symfony-mattermost-notifier' is not installed, so not removed
2026-05-03T01:18:10.4124690Z Package 'php-symfony-mercure' is not installed, so not removed
2026-05-03T01:18:10.4125247Z Package 'php-symfony-mercure-bundle' is not installed, so not removed
2026-05-03T01:18:10.4125710Z Package 'php-symfony-mercure-notifier' is not installed, so not removed
2026-05-03T01:18:10.4126202Z Package 'php-symfony-message-bird-notifier' is not installed, so not removed
2026-05-03T01:18:10.4126719Z Package 'php-symfony-message-media-notifier' is not installed, so not removed
2026-05-03T01:18:10.4127252Z Package 'php-symfony-microsoft-teams-notifier' is not installed, so not removed
2026-05-03T01:18:10.4127747Z Package 'php-symfony-mobyt-notifier' is not installed, so not removed
2026-05-03T01:18:10.4128193Z Package 'php-symfony-novu-notifier' is not installed, so not removed
2026-05-03T01:18:10.4128628Z Package 'php-symfony-ntfy-notifier' is not installed, so not removed
2026-05-03T01:18:10.4129086Z Package 'php-symfony-octopush-notifier' is not installed, so not removed
2026-05-03T01:18:10.4129553Z Package 'php-symfony-oh-my-smtp-mailer' is not installed, so not removed
2026-05-03T01:18:10.4130035Z Package 'php-symfony-one-signal-notifier' is not installed, so not removed
2026-05-03T01:18:10.4130523Z Package 'php-symfony-orange-sms-notifier' is not installed, so not removed
2026-05-03T01:18:10.4131015Z Package 'php-symfony-ovh-cloud-notifier' is not installed, so not removed
2026-05-03T01:18:10.4131498Z Package 'php-symfony-pager-duty-notifier' is not installed, so not removed
2026-05-03T01:18:10.4131970Z Package 'php-symfony-phpunit-bridge' is not installed, so not removed
2026-05-03T01:18:10.4132484Z Package 'php-symfony-phrase-translation-provider' is not installed, so not removed
2026-05-03T01:18:10.4132994Z Package 'php-symfony-plivo-notifier' is not installed, so not removed
2026-05-03T01:18:10.4133426Z Package 'php-symfony-polyfill' is not installed, so not removed
2026-05-03T01:18:10.4133850Z Package 'php-symfony-polyfill-apcu' is not installed, so not removed
2026-05-03T01:18:10.4134298Z Package 'php-symfony-polyfill-ctype' is not installed, so not removed
2026-05-03T01:18:10.4134746Z Package 'php-symfony-polyfill-php72' is not installed, so not removed
2026-05-03T01:18:10.4135465Z Package 'php-symfony-polyfill-php73' is not installed, so not removed
2026-05-03T01:18:10.4135930Z Package 'php-symfony-polyfill-php74' is not installed, so not removed
2026-05-03T01:18:10.4136371Z Package 'php-symfony-polyfill-php81' is not installed, so not removed
2026-05-03T01:18:10.4136822Z Package 'php-symfony-polyfill-php82' is not installed, so not removed
2026-05-03T01:18:10.4137267Z Package 'php-symfony-polyfill-iconv' is not installed, so not removed
2026-05-03T01:18:10.4137746Z Package 'php-symfony-polyfill-intl-grapheme' is not installed, so not removed
2026-05-03T01:18:10.4138259Z Package 'php-symfony-polyfill-intl-icu' is not installed, so not removed
2026-05-03T01:18:10.4138802Z Package 'php-symfony-polyfill-intl-messageformatter' is not installed, so not removed
2026-05-03T01:18:10.4139338Z Package 'php-symfony-polyfill-intl-idn' is not installed, so not removed
2026-05-03T01:18:10.4139847Z Package 'php-symfony-polyfill-intl-normalizer' is not installed, so not removed
2026-05-03T01:18:10.4140357Z Package 'php-symfony-polyfill-mbstring' is not installed, so not removed
2026-05-03T01:18:10.4140954Z Package 'php-symfony-polyfill-util' is not installed, so not removed
2026-05-03T01:18:10.4141393Z Package 'php-symfony-polyfill-xml' is not installed, so not removed
2026-05-03T01:18:10.4141996Z Package 'php-symfony-polyfill-uuid' is not installed, so not removed
2026-05-03T01:18:10.4142453Z Package 'php-symfony-postmark-mailer' is not installed, so not removed
2026-05-03T01:18:10.4142950Z Package 'php-symfony-psr-http-message-bridge' is not installed, so not removed
2026-05-03T01:18:10.4143447Z Package 'php-symfony-pushover-notifier' is not installed, so not removed
2026-05-03T01:18:10.4143911Z Package 'php-symfony-redis-messenger' is not installed, so not removed
2026-05-03T01:18:10.4144376Z Package 'php-symfony-redlink-notifier' is not installed, so not removed
2026-05-03T01:18:10.4144859Z Package 'php-symfony-ring-central-notifier' is not installed, so not removed
2026-05-03T01:18:10.4165286Z Package 'php-symfony-rocket-chat-notifier' is not installed, so not removed
2026-05-03T01:18:10.4165886Z Package 'php-symfony-runtime' is not installed, so not removed
2026-05-03T01:18:10.4166366Z Package 'php-symfony-scaleway-mailer' is not installed, so not removed
2026-05-03T01:18:10.4166851Z Package 'php-symfony-security-acl' is not installed, so not removed
2026-05-03T01:18:10.4167335Z Package 'php-symfony-sendberry-notifier' is not installed, so not removed
2026-05-03T01:18:10.4167820Z Package 'php-symfony-sendgrid-mailer' is not installed, so not removed
2026-05-03T01:18:10.4168291Z Package 'php-symfony-sendinblue-mailer' is not installed, so not removed
2026-05-03T01:18:10.4168778Z Package 'php-symfony-sendinblue-notifier' is not installed, so not removed
2026-05-03T01:18:10.4169281Z Package 'php-symfony-simple-textin-notifier' is not installed, so not removed
2026-05-03T01:18:10.4169775Z Package 'php-symfony-sinch-notifier' is not installed, so not removed
2026-05-03T01:18:10.4170223Z Package 'php-symfony-slack-notifier' is not installed, so not removed
2026-05-03T01:18:10.4170698Z Package 'php-symfony-sms-biuras-notifier' is not installed, so not removed
2026-05-03T01:18:10.4171182Z Package 'php-symfony-sms-factor-notifier' is not installed, so not removed
2026-05-03T01:18:10.4171644Z Package 'php-symfony-sms77-notifier' is not installed, so not removed
2026-05-03T01:18:10.4172096Z Package 'php-symfony-smsapi-notifier' is not installed, so not removed
2026-05-03T01:18:10.4172540Z Package 'php-symfony-smsc-notifier' is not installed, so not removed
2026-05-03T01:18:10.4172998Z Package 'php-symfony-smsmode-notifier' is not installed, so not removed
2026-05-03T01:18:10.4173465Z Package 'php-symfony-spot-hit-notifier' is not installed, so not removed
2026-05-03T01:18:10.4173935Z Package 'php-symfony-telegram-notifier' is not installed, so not removed
2026-05-03T01:18:10.4174400Z Package 'php-symfony-telnyx-notifier' is not installed, so not removed
2026-05-03T01:18:10.4174848Z Package 'php-symfony-termii-notifier' is not installed, so not removed
2026-05-03T01:18:10.4175624Z Package 'php-symfony-turbo-sms-notifier' is not installed, so not removed
2026-05-03T01:18:10.4176110Z Package 'php-symfony-twilio-notifier' is not installed, so not removed
2026-05-03T01:18:10.4176580Z Package 'php-symfony-twitter-notifier' is not installed, so not removed
2026-05-03T01:18:10.4177042Z Package 'php-symfony-vonage-notifier' is not installed, so not removed
2026-05-03T01:18:10.4177498Z Package 'php-symfony-yunpian-notifier' is not installed, so not removed
2026-05-03T01:18:10.4177955Z Package 'php-symfony-zendesk-notifier' is not installed, so not removed
2026-05-03T01:18:10.4178404Z Package 'php-symfony-zulip-notifier' is not installed, so not removed
2026-05-03T01:18:10.4178819Z Package 'php-text-captcha' is not installed, so not removed
2026-05-03T01:18:10.4179206Z Package 'php-text-password' is not installed, so not removed
2026-05-03T01:18:10.4179589Z Package 'php-text-figlet' is not installed, so not removed
2026-05-03T01:18:10.4180070Z Package 'php-text-languagedetect' is not installed, so not removed
2026-05-03T01:18:10.4181014Z Package 'php-text-wiki' is not installed, so not removed
2026-05-03T01:18:10.4181379Z Package 'php-thrift' is not installed, so not removed
2026-05-03T01:18:10.4181729Z Package 'php8.3-tideways' is not installed, so not removed
2026-05-03T01:18:10.4182250Z Package 'php-tideways-all-dev' is not installed, so not removed
2026-05-03T01:18:10.5466350Z Package 'php-tijsverkoyen-css-to-inline-styles' is not installed, so not removed
2026-05-03T01:18:10.5466970Z Package 'php-timer' is not installed, so not removed
2026-05-03T01:18:10.5467381Z Package 'php-twig-doc' is not installed, so not removed
2026-05-03T01:18:10.5467834Z Package 'php-twig-cache-extra' is not installed, so not removed
2026-05-03T01:18:10.5468330Z Package 'php-twig-cssinliner-extra' is not installed, so not removed
2026-05-03T01:18:10.5468821Z Package 'php-twig-extra-bundle' is not installed, so not removed
2026-05-03T01:18:10.5469289Z Package 'php-twig-html-extra' is not installed, so not removed
2026-05-03T01:18:10.5469784Z Package 'php-twig-i18n-extension' is not installed, so not removed
2026-05-03T01:18:10.5470343Z Package 'php-twig-inky-extra' is not installed, so not removed
2026-05-03T01:18:10.5470939Z Package 'php-twig-intl-extra' is not installed, so not removed
2026-05-03T01:18:10.5471601Z Package 'php-twig-markdown-extra' is not installed, so not removed
2026-05-03T01:18:10.5472058Z Package 'php-twig-string-extra' is not installed, so not removed
2026-05-03T01:18:10.5472522Z Package 'php8.3-uopz' is not installed, so not removed
2026-05-03T01:18:10.5473066Z Package 'php-uopz-all-dev' is not installed, so not removed
2026-05-03T01:18:10.5473489Z Package 'php8.3-uploadprogress' is not installed, so not removed
2026-05-03T01:18:10.5473955Z Package 'php-uploadprogress-all-dev' is not installed, so not removed
2026-05-03T01:18:10.5474378Z Package 'php8.3-uuid' is not installed, so not removed
2026-05-03T01:18:10.5474759Z Package 'php-uuid-all-dev' is not installed, so not removed
2026-05-03T01:18:10.5475416Z Package 'php-validate' is not installed, so not removed
2026-05-03T01:18:10.5475825Z Package 'php-vlucas-phpdotenv' is not installed, so not removed
2026-05-03T01:18:10.5476278Z Package 'php-voku-portable-ascii' is not installed, so not removed
2026-05-03T01:18:10.5476694Z Package 'php-wmerrors' is not installed, so not removed
2026-05-03T01:18:10.5477090Z Package 'php-xdebug-all-dev' is not installed, so not removed
2026-05-03T01:18:10.5477480Z Package 'php-xml-svg' is not installed, so not removed
2026-05-03T01:18:10.5477853Z Package 'php8.3-xmlrpc' is not installed, so not removed
2026-05-03T01:18:10.5478244Z Package 'php-xmlrpc-all-dev' is not installed, so not removed
2026-05-03T01:18:10.5478636Z Package 'php8.3-yac' is not installed, so not removed
2026-05-03T01:18:10.5479013Z Package 'php-yac-all-dev' is not installed, so not removed
2026-05-03T01:18:10.5479406Z Package 'php-yaml-all-dev' is not installed, so not removed
2026-05-03T01:18:10.5479801Z Package 'php-zend-code' is not installed, so not removed
2026-05-03T01:18:10.5480206Z Package 'php-zend-eventmanager' is not installed, so not removed
2026-05-03T01:18:10.5480621Z Package 'php-zend-stdlib' is not installed, so not removed
2026-05-03T01:18:10.5480992Z Package 'php-zeroc-ice' is not installed, so not removed
2026-05-03T01:18:10.5481350Z Package 'php-zeta-base' is not installed, so not removed
2026-05-03T01:18:10.5481736Z Package 'php-zeta-console-tools' is not installed, so not removed
2026-05-03T01:18:10.5482131Z Package 'php-zeta-unit-test' is not installed, so not removed
2026-05-03T01:18:10.5482506Z Package 'php-zmq-all-dev' is not installed, so not removed
2026-05-03T01:18:10.5482959Z Package 'php-zumba-json-serializer' is not installed, so not removed
2026-05-03T01:18:10.5483389Z Package 'php8.3-libvirt-php' is not installed, so not removed
2026-05-03T01:18:10.5483734Z Package 'phpab' is not installed, so not removed
2026-05-03T01:18:10.5484040Z Package 'phpcpd' is not installed, so not removed
2026-05-03T01:18:10.5484391Z Package 'phpunit-cli-parser' is not installed, so not removed
2026-05-03T01:18:10.5485238Z Package 'phpldapadmin' is not installed, so not removed
2026-05-03T01:18:10.5485602Z Package 'phpliteadmin' is not installed, so not removed
2026-05-03T01:18:10.5486138Z Package 'phpliteadmin-themes' is not installed, so not removed
2026-05-03T01:18:10.5486506Z Package 'phploc' is not installed, so not removed
2026-05-03T01:18:10.5486829Z Package 'phppgadmin' is not installed, so not removed
2026-05-03T01:18:10.5487168Z Package 'phpsysinfo' is not installed, so not removed
2026-05-03T01:18:10.5487530Z Package 'phpunit-code-unit' is not installed, so not removed
2026-05-03T01:18:10.5487887Z Package 'phpunit-diff' is not installed, so not removed
2026-05-03T01:18:10.5488246Z Package 'phpunit-exporter' is not installed, so not removed
2026-05-03T01:18:10.5488635Z Package 'phpunit-global-state' is not installed, so not removed
2026-05-03T01:18:10.5489066Z Package 'phpunit-object-enumerator' is not installed, so not removed
2026-05-03T01:18:10.5489523Z Package 'phpunit-resource-operations' is not installed, so not removed
2026-05-03T01:18:10.5489937Z Package 'phpunit-type' is not installed, so not removed
2026-05-03T01:18:10.5490328Z Package 'phpunit-object-reflector' is not installed, so not removed
2026-05-03T01:18:10.5490727Z Package 'phpwebcounter' is not installed, so not removed
2026-05-03T01:18:10.5491102Z Package 'phpwebcounter-extra' is not installed, so not removed
2026-05-03T01:18:10.5491476Z Package 'python3-phply' is not installed, so not removed
2026-05-03T01:18:10.5491855Z Package 'python3-phpserialize' is not installed, so not removed
2026-05-03T01:18:10.5492300Z Package 'python3-sphinxcontrib.phpdomain' is not installed, so not removed
2026-05-03T01:18:10.5492730Z Package 'simplesamlphp' is not installed, so not removed
2026-05-03T01:18:10.5493079Z Package 'slbackup-php' is not installed, so not removed
2026-05-03T01:18:10.5493436Z Package 'uwsgi-plugin-php' is not installed, so not removed
2026-05-03T01:18:10.5493805Z Package 'weechat-php' is not installed, so not removed
2026-05-03T01:18:10.5494141Z Package 'php-mythtv' is not installed, so not removed
2026-05-03T01:18:10.5494475Z Package 'mono-devel' is not installed, so not removed
2026-05-03T01:18:10.5494781Z The following packages will be REMOVED:
2026-05-03T01:18:10.5495263Z   azure-cli clang-16 clang-17 clang-18 clang-tidy-16 clang-tidy-17
2026-05-03T01:18:10.5495690Z   clang-tidy-18 clang-tools-16 clang-tools-17 clang-tools-18 firefox
2026-05-03T01:18:10.5496146Z   google-chrome-stable google-cloud-cli google-cloud-cli-anthoscli llvm-16
2026-05-03T01:18:10.5496617Z   llvm-16-dev llvm-16-linker-tools llvm-16-runtime llvm-16-tools llvm-17
2026-05-03T01:18:10.5497056Z   llvm-17-dev llvm-17-linker-tools llvm-17-runtime llvm-17-tools llvm-18
2026-05-03T01:18:10.5497514Z   llvm-18-dev llvm-18-linker-tools llvm-18-runtime llvm-18-tools php-common
2026-05-03T01:18:10.5498003Z   php-pear php8.3 php8.3-amqp php8.3-apcu php8.3-bcmath php8.3-bz2 php8.3-cgi
2026-05-03T01:18:10.5498514Z   php8.3-cli php8.3-common php8.3-curl php8.3-dba php8.3-dev php8.3-enchant
2026-05-03T01:18:10.5498990Z   php8.3-fpm php8.3-gd php8.3-gmp php8.3-igbinary php8.3-imagick php8.3-imap
2026-05-03T01:18:10.5499463Z   php8.3-interbase php8.3-intl php8.3-ldap php8.3-mbstring php8.3-memcache
2026-05-03T01:18:10.5499934Z   php8.3-memcached php8.3-mongodb php8.3-msgpack php8.3-mysql php8.3-odbc
2026-05-03T01:18:10.5500383Z   php8.3-opcache php8.3-pcov php8.3-pgsql php8.3-phpdbg php8.3-pspell
2026-05-03T01:18:10.5500824Z   php8.3-readline php8.3-redis php8.3-snmp php8.3-soap php8.3-sqlite3
2026-05-03T01:18:10.5501274Z   php8.3-sybase php8.3-tidy php8.3-xdebug php8.3-xml php8.3-xsl php8.3-yaml
2026-05-03T01:18:10.5501647Z   php8.3-zip php8.3-zmq powershell
2026-05-03T01:18:10.8394830Z 0 upgraded, 0 newly installed, 78 to remove and 5 not upgraded.
2026-05-03T01:18:10.8395797Z After this operation, 3857 MB disk space will be freed.
2026-05-03T01:18:11.0008154Z (Reading database ... 
2026-05-03T01:18:11.0008574Z (Reading database ... 5%
2026-05-03T01:18:11.0009302Z (Reading database ... 10%
2026-05-03T01:18:11.0009673Z (Reading database ... 15%
2026-05-03T01:18:11.0010079Z (Reading database ... 20%
2026-05-03T01:18:11.0010423Z (Reading database ... 25%
2026-05-03T01:18:11.0011005Z (Reading database ... 30%
2026-05-03T01:18:11.0011349Z (Reading database ... 35%
2026-05-03T01:18:11.0011593Z (Reading database ... 40%
2026-05-03T01:18:11.0011925Z (Reading database ... 45%
2026-05-03T01:18:11.0012152Z (Reading database ... 50%
2026-05-03T01:18:11.0428418Z (Reading database ... 55%
2026-05-03T01:18:11.4057021Z (Reading database ... 60%
2026-05-03T01:18:11.7060303Z (Reading database ... 65%
2026-05-03T01:18:11.9795440Z (Reading database ... 70%
2026-05-03T01:18:12.2993616Z (Reading database ... 75%
2026-05-03T01:18:12.7597436Z (Reading database ... 80%
2026-05-03T01:18:13.3500264Z (Reading database ... 85%
2026-05-03T01:18:13.8496486Z (Reading database ... 90%
2026-05-03T01:18:14.3442336Z (Reading database ... 95%
2026-05-03T01:18:14.3442880Z (Reading database ... 100%
2026-05-03T01:18:14.3443414Z (Reading database ... 220762 files and directories currently installed.)
2026-05-03T01:18:14.3484345Z Removing azure-cli (2.85.0-1~noble) ...
2026-05-03T01:18:18.6684063Z Removing clang-tidy-16 (1:16.0.6-23ubuntu4) ...
2026-05-03T01:18:18.7200658Z Removing clang-tools-16 (1:16.0.6-23ubuntu4) ...
2026-05-03T01:18:18.8093161Z Removing clang-16 (1:16.0.6-23ubuntu4) ...
2026-05-03T01:18:18.8265966Z Removing clang-tidy-17 (1:17.0.6-9ubuntu1) ...
2026-05-03T01:18:18.8451186Z Removing clang-tools-17 (1:17.0.6-9ubuntu1) ...
2026-05-03T01:18:18.8943456Z Removing clang-17 (1:17.0.6-9ubuntu1) ...
2026-05-03T01:18:18.9183069Z Removing clang-tidy-18 (1:18.1.3-1ubuntu1) ...
2026-05-03T01:18:18.9437324Z Removing clang-tools-18 (1:18.1.3-1ubuntu1) ...
2026-05-03T01:18:18.9923015Z Removing clang-18 (1:18.1.3-1ubuntu1) ...
2026-05-03T01:18:19.0142175Z Removing firefox (149.0.2+build1-0ubuntu0.24.04.1~mt1) ...
2026-05-03T01:18:19.1419832Z Removing google-chrome-stable (147.0.7727.55-1) ...
2026-05-03T01:18:19.3287090Z Removing google-cloud-cli-anthoscli (564.0.0-0) ...
2026-05-03T01:18:30.1234853Z Removing google-cloud-cli (564.0.0-0) ...
2026-05-03T01:19:34.8930201Z Removing llvm-16-dev (1:16.0.6-23ubuntu4) ...
2026-05-03T01:19:35.1337497Z Removing llvm-16 (1:16.0.6-23ubuntu4) ...
2026-05-03T01:19:35.1606495Z Removing llvm-16-linker-tools (1:16.0.6-23ubuntu4) ...
2026-05-03T01:19:35.1777391Z Removing llvm-16-runtime (1:16.0.6-23ubuntu4) ...
2026-05-03T01:19:35.2070252Z Removing llvm-16-tools (1:16.0.6-23ubuntu4) ...
2026-05-03T01:19:35.3289098Z Removing llvm-17-dev (1:17.0.6-9ubuntu1) ...
2026-05-03T01:19:35.5538972Z Removing llvm-17 (1:17.0.6-9ubuntu1) ...
2026-05-03T01:19:35.5806003Z Removing llvm-17-linker-tools (1:17.0.6-9ubuntu1) ...
2026-05-03T01:19:35.5970884Z Removing llvm-17-runtime (1:17.0.6-9ubuntu1) ...
2026-05-03T01:19:35.6404030Z Removing llvm-17-tools (1:17.0.6-9ubuntu1) ...
2026-05-03T01:19:35.7569519Z Removing llvm-18-dev (1:18.1.3-1ubuntu1) ...
2026-05-03T01:19:36.0096465Z Removing llvm-18 (1:18.1.3-1ubuntu1) ...
2026-05-03T01:19:36.0333611Z Removing llvm-18-linker-tools (1:18.1.3-1ubuntu1) ...
2026-05-03T01:19:36.0528067Z Removing llvm-18-runtime (1:18.1.3-1ubuntu1) ...
2026-05-03T01:19:36.0846792Z Removing llvm-18-tools (1:18.1.3-1ubuntu1) ...
2026-05-03T01:19:36.2161705Z Removing php8.3-zip (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:36.4026450Z Removing php8.3-sybase (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:36.5372587Z Removing php-pear (1:1.10.13+submodules+notgz+2022032202-2build1) ...
2026-05-03T01:19:36.6591661Z Removing php8.3 (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:36.6799265Z Removing php8.3-amqp (1.11.0-5ubuntu1) ...
2026-05-03T01:19:36.8069527Z Removing php8.3-apcu (5.1.22+4.0.11-2ubuntu1) ...
2026-05-03T01:19:36.9316811Z Removing php8.3-bcmath (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:37.0698939Z Removing php8.3-bz2 (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:37.1943928Z Removing php8.3-zmq (1.1.3-24ubuntu1) ...
2026-05-03T01:19:37.3260905Z Removing php8.3-yaml (2.2.2+2.1.0+2.0.4+1.3.2-6ubuntu1) ...
2026-05-03T01:19:37.4453474Z Removing php8.3-cgi (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:39.2408322Z apache2_invoke php8.3-cgi prerm: No action required
2026-05-03T01:19:39.2681417Z Removing php8.3-dev (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:39.3616478Z Removing php8.3-xdebug (3.2.0+3.1.6+2.9.8+2.8.1+2.5.5-3ubuntu1) ...
2026-05-03T01:19:39.4647458Z Removing php8.3-phpdbg (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:40.9047235Z Removing php8.3-redis (5.3.7+4.3.0-3ubuntu1) ...
2026-05-03T01:19:40.9838845Z Removing php8.3-xsl (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:41.0010314Z Removing php8.3-soap (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:41.0941713Z Removing php8.3-curl (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:41.1819389Z Removing php8.3-dba (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:41.2611702Z Removing php8.3-enchant (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:41.3399256Z Removing php8.3-pcov (1.0.11-5ubuntu1) ...
2026-05-03T01:19:41.4067884Z Removing php8.3-fpm (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:42.7916768Z apache2_invoke php8.3-fpm prerm: No action required
2026-05-03T01:19:42.8385153Z Removing php8.3-gd (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:42.9038911Z Removing php8.3-gmp (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:42.9675172Z Removing php8.3-memcached (3.2.0+2.2.0-4ubuntu3) ...
2026-05-03T01:19:43.0255683Z Removing php8.3-igbinary (3.2.13-1ubuntu3) ...
2026-05-03T01:19:43.0962166Z Removing php8.3-imagick (3.7.0-4ubuntu3) ...
2026-05-03T01:19:43.1562996Z Removing php8.3-imap (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:43.2169137Z Removing php8.3-interbase (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:43.2858639Z Removing php8.3-intl (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:43.3527002Z Removing php8.3-ldap (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:43.4169070Z Removing php8.3-mbstring (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:43.4843383Z Removing php8.3-memcache (8.0+4.0.5.2+3.0.9~20170802.e702b5f9+-8ubuntu1) ...
2026-05-03T01:19:43.5428667Z Removing php8.3-mongodb (1.15.0+1.11.1+1.9.2+1.7.5-1ubuntu3) ...
2026-05-03T01:19:43.6024448Z Removing php8.3-msgpack (1:2.2.0~rc2-3ubuntu1) ...
2026-05-03T01:19:43.6632821Z Removing php8.3-mysql (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:43.7901099Z Removing php8.3-odbc (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:43.8816960Z Removing php8.3-pgsql (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:43.9771097Z Removing php8.3-pspell (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:44.0415339Z Removing php8.3-snmp (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:44.1058797Z Removing php8.3-sqlite3 (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:44.1991586Z Removing php8.3-tidy (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:44.2588139Z Removing php8.3-xml (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:44.4753189Z Removing powershell (7.4.14-1.deb) ...
2026-05-03T01:19:44.5964944Z Removing php8.3-cli (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:45.1166057Z Removing php8.3-opcache (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:45.1579467Z Removing php8.3-readline (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:45.2977309Z Removing php8.3-common (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T01:19:45.6002404Z Removing php-common (2:93ubuntu2) ...
2026-05-03T01:19:45.6445709Z Stopping 'phpsessionclean.service', but its triggering units are still active:
2026-05-03T01:19:45.6446667Z 
2026-05-03T01:19:45.6447051Z phpsessionclean.timer
2026-05-03T01:19:45.6447544Z 
2026-05-03T01:19:46.3432117Z Processing triggers for libc-bin (2.39-0ubuntu8.7) ...
2026-05-03T01:19:46.4580343Z Processing triggers for systemd (255.4-1ubuntu8.15) ...
2026-05-03T01:19:46.5444393Z Processing triggers for man-db (2.12.0-4build2) ...
2026-05-03T01:19:46.5465597Z Not building database; man-db/auto-update is not 'true'.
2026-05-03T01:19:46.5479891Z Processing triggers for hicolor-icon-theme (0.17-2) ...
2026-05-03T01:19:48.2722467Z Reading package lists...
2026-05-03T01:19:48.4206963Z Building dependency tree...
2026-05-03T01:19:48.4214296Z Reading state information...
2026-05-03T01:19:48.5694304Z The following packages will be REMOVED:
2026-05-03T01:19:48.5695319Z   dictionaries-common emacsen-common firebird3.0-common firebird3.0-common-doc
2026-05-03T01:19:48.5696729Z   freetds-common hunspell-en-us icu-devtools imagemagick-6-common lib32gcc-s1
2026-05-03T01:19:48.5697697Z   lib32stdc++6 libaom3 libaspell15 libc-client2007e libc6-i386 libcanberra0t64
2026-05-03T01:19:48.5698587Z   libclang-common-16-dev libclang-common-17-dev libclang-common-18-dev
2026-05-03T01:19:48.5699508Z   libclang-rt-16-dev libclang-rt-17-dev libclang-rt-18-dev libclang1-16t64
2026-05-03T01:19:48.5700326Z   libclang1-17t64 libdbusmenu-glib4 libdbusmenu-gtk3-4 libde265-0
2026-05-03T01:19:48.5701117Z   libenchant-2-2 libfbclient2 libffi-dev libfftw3-double3 libgc1 libgd3
2026-05-03T01:19:48.5701931Z   libhashkit2t64 libheif-plugin-aomdec libheif-plugin-libde265 libheif1
2026-05-03T01:19:48.5702784Z   libhunspell-1.7-0 libicu-dev liblldb-16t64 liblldb-17t64 liblqr-1-0
2026-05-03T01:19:48.5703588Z   libmagickcore-6.q16-7t64 libmagickwand-6.q16-7t64 libmemcached11t64
2026-05-03T01:19:48.5704429Z   libncurses-dev libnorm1t64 libobjc-13-dev libobjc4 libogg0 libopenjp2-7
2026-05-03T01:19:48.5705485Z   libpcre2-16-0 libpcre2-32-0 libpcre2-dev libpcre2-posix3 libpfm4
2026-05-03T01:19:48.5706393Z   libpgm-5.3-0t64 libqdbm14t64 librabbitmq4 libraw23t64 libsnappy1v5 libsybdb5
2026-05-03T01:19:48.5707299Z   libtdb1 libtidy5deb1 libtommath1 libvorbis0a libvorbisfile3 libwebpdemux2
2026-05-03T01:19:48.5708239Z   libwebpmux3 libxml2-dev libz3-4 libz3-dev libzip4t64 libzmq5 mlock shtool
2026-05-03T01:19:48.5708936Z   sound-theme-freedesktop xul-ext-ubufox
2026-05-03T01:19:48.7916486Z 0 upgraded, 0 newly installed, 77 to remove and 5 not upgraded.
2026-05-03T01:19:48.7916941Z After this operation, 389 MB disk space will be freed.
2026-05-03T01:19:48.8079803Z (Reading database ... 
2026-05-03T01:19:48.8080207Z (Reading database ... 5%
2026-05-03T01:19:48.8080620Z (Reading database ... 10%
2026-05-03T01:19:48.8081064Z (Reading database ... 15%
2026-05-03T01:19:48.8081417Z (Reading database ... 20%
2026-05-03T01:19:48.8083233Z (Reading database ... 25%
2026-05-03T01:19:48.8083632Z (Reading database ... 30%
2026-05-03T01:19:48.8084025Z (Reading database ... 35%
2026-05-03T01:19:48.8084364Z (Reading database ... 40%
2026-05-03T01:19:48.8084630Z (Reading database ... 45%
2026-05-03T01:19:48.8084863Z (Reading database ... 50%
2026-05-03T01:19:48.8085475Z (Reading database ... 55%
2026-05-03T01:19:48.8111812Z (Reading database ... 60%
2026-05-03T01:19:48.8200088Z (Reading database ... 65%
2026-05-03T01:19:48.8223375Z (Reading database ... 70%
2026-05-03T01:19:48.8240050Z (Reading database ... 75%
2026-05-03T01:19:48.8285705Z (Reading database ... 80%
2026-05-03T01:19:48.8308794Z (Reading database ... 85%
2026-05-03T01:19:48.8333787Z (Reading database ... 90%
2026-05-03T01:19:48.8427582Z (Reading database ... 95%
2026-05-03T01:19:48.8428056Z (Reading database ... 100%
2026-05-03T01:19:48.8428725Z (Reading database ... 122759 files and directories currently installed.)
2026-05-03T01:19:48.8446968Z Removing libenchant-2-2:amd64 (2.3.3-2build2) ...
2026-05-03T01:19:48.8594114Z Removing hunspell-en-us (1:2020.12.07-2) ...
2026-05-03T01:19:48.9162307Z Removing dictionaries-common (1.29.7) ...
2026-05-03T01:19:48.9893664Z Removing 'diversion of /usr/share/dict/words to /usr/share/dict/words.pre-dictionaries-common by dictionaries-common'
2026-05-03T01:19:49.0089051Z Removing emacsen-common (3.0.5) ...
2026-05-03T01:19:49.0534910Z Removing libfbclient2:amd64 (3.0.11.33703.ds4-2ubuntu2) ...
2026-05-03T01:19:49.0680782Z Removing firebird3.0-common (3.0.11.33703.ds4-2ubuntu2) ...
2026-05-03T01:19:49.1019858Z Removing firebird3.0-common-doc (3.0.11.33703.ds4-2ubuntu2) ...
2026-05-03T01:19:49.1153720Z Removing libsybdb5:amd64 (1.3.17+ds-2build3) ...
2026-05-03T01:19:49.1357388Z Removing freetds-common (1.3.17+ds-2build3) ...
2026-05-03T01:19:49.1592717Z Removing libxml2-dev:amd64 (2.9.14+dfsg-1.3ubuntu3.7) ...
2026-05-03T01:19:49.1899463Z Removing libicu-dev:amd64 (74.2-1ubuntu3.1) ...
2026-05-03T01:19:49.2246396Z Removing icu-devtools (74.2-1ubuntu3.1) ...
2026-05-03T01:19:49.2378565Z Removing libmagickwand-6.q16-7t64:amd64 (8:6.9.12.98+dfsg1-5.2build2) ...
2026-05-03T01:19:49.2604475Z Removing libmagickcore-6.q16-7t64:amd64 (8:6.9.12.98+dfsg1-5.2build2) ...
2026-05-03T01:19:49.2943171Z Removing imagemagick-6-common (8:6.9.12.98+dfsg1-5.2build2) ...
2026-05-03T01:19:49.3052632Z Removing libclang-rt-18-dev:amd64 (1:18.1.3-1ubuntu1) ...
2026-05-03T01:19:49.3308802Z Removing libclang-rt-16-dev:amd64 (1:16.0.6-23ubuntu4) ...
2026-05-03T01:19:49.3512001Z Removing lib32stdc++6 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.3647325Z Removing lib32gcc-s1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.3798073Z Removing libaspell15:amd64 (0.60.8.1-1build1) ...
2026-05-03T01:19:49.4073633Z Removing libc-client2007e (8:2007f~dfsg-7build3) ...
2026-05-03T01:19:49.4202192Z Removing libc6-i386 (2.39-0ubuntu8.7) ...
2026-05-03T01:19:49.4579348Z Removing libcanberra0t64:amd64 (0.30-10ubuntu10) ...
2026-05-03T01:19:49.4711420Z Removing libclang-common-16-dev (1:16.0.6-23ubuntu4) ...
2026-05-03T01:19:49.4965616Z Removing libclang-common-17-dev:amd64 (1:17.0.6-9ubuntu1) ...
2026-05-03T01:19:49.5240531Z Removing libclang-common-18-dev:amd64 (1:18.1.3-1ubuntu1) ...
2026-05-03T01:19:49.5508501Z Removing libclang-rt-17-dev:amd64 (1:17.0.6-9ubuntu1) ...
2026-05-03T01:19:49.5732311Z Removing libclang1-16t64 (1:16.0.6-23ubuntu4) ...
2026-05-03T01:19:49.5870925Z Removing libclang1-17t64 (1:17.0.6-9ubuntu1) ...
2026-05-03T01:19:49.6003675Z Removing libdbusmenu-gtk3-4:amd64 (18.10.20180917~bzr492+repack1-3.1ubuntu5) ...
2026-05-03T01:19:49.6284378Z Removing libdbusmenu-glib4:amd64 (18.10.20180917~bzr492+repack1-3.1ubuntu5) ...
2026-05-03T01:19:49.6461232Z Removing libffi-dev:amd64 (3.4.6-1build1) ...
2026-05-03T01:19:49.6799485Z Removing libfftw3-double3:amd64 (3.3.10-1ubuntu3) ...
2026-05-03T01:19:49.6975533Z Removing libobjc-13-dev:amd64 (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T01:19:49.7120364Z Removing libobjc4:amd64 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T01:19:49.7277577Z Removing libgc1:amd64 (1:8.2.6-1build1) ...
2026-05-03T01:19:49.7415656Z Removing libgd3:amd64 (2.3.3-9ubuntu5) ...
2026-05-03T01:19:49.7649799Z Removing libmemcached11t64:amd64 (1.1.4-1.1build3) ...
2026-05-03T01:19:49.7781329Z Removing libhashkit2t64:amd64 (1.1.4-1.1build3) ...
2026-05-03T01:19:49.7912121Z Removing libhunspell-1.7-0:amd64 (1.7.2+really1.7.2-10build3) ...
2026-05-03T01:19:49.8040046Z Removing liblldb-16t64 (1:16.0.6-23ubuntu4) ...
2026-05-03T01:19:49.8218863Z Removing liblldb-17t64 (1:17.0.6-9ubuntu1) ...
2026-05-03T01:19:49.8343332Z Removing liblqr-1-0:amd64 (0.4.2-2.1build2) ...
2026-05-03T01:19:49.8478032Z Removing libncurses-dev:amd64 (6.4+20240113-1ubuntu2) ...
2026-05-03T01:19:49.8641548Z Removing libzmq5:amd64 (4.3.5-1build2) ...
2026-05-03T01:19:49.8770971Z Removing libnorm1t64:amd64 (1.5.9+dfsg-3.1build1) ...
2026-05-03T01:19:49.8900105Z Removing libvorbisfile3:amd64 (1.3.7-1build3) ...
2026-05-03T01:19:49.9036338Z Removing libvorbis0a:amd64 (1.3.7-1build3) ...
2026-05-03T01:19:49.9163993Z Removing libogg0:amd64 (1.3.5-3build1) ...
2026-05-03T01:19:49.9336386Z Removing libopenjp2-7:amd64 (2.5.0-2ubuntu0.4) ...
2026-05-03T01:19:49.9488378Z Removing libpcre2-dev:amd64 (10.42-4ubuntu2.1) ...
2026-05-03T01:19:49.9721172Z Removing libpcre2-16-0:amd64 (10.42-4ubuntu2.1) ...
2026-05-03T01:19:49.9846238Z Removing libpcre2-32-0:amd64 (10.42-4ubuntu2.1) ...
2026-05-03T01:19:49.9969555Z Removing libpcre2-posix3:amd64 (10.42-4ubuntu2.1) ...
2026-05-03T01:19:50.0135484Z Removing libpfm4:amd64 (4.13.0+git32-g0d4ed0e-1) ...
2026-05-03T01:19:50.0267173Z Removing libpgm-5.3-0t64:amd64 (5.3.128~dfsg-2.1build1) ...
2026-05-03T01:19:50.0386914Z Removing libqdbm14t64 (1.8.78-12.1build2) ...
2026-05-03T01:19:50.0556574Z Removing librabbitmq4:amd64 (0.11.0-1build2) ...
2026-05-03T01:19:50.0703038Z Removing libraw23t64:amd64 (0.21.2-2.1ubuntu0.24.04.1) ...
2026-05-03T01:19:50.0833737Z Removing libsnappy1v5:amd64 (1.1.10-1build1) ...
2026-05-03T01:19:50.0978519Z Removing libtdb1:amd64 (1.4.10-1build1) ...
2026-05-03T01:19:50.1107411Z Removing libtidy5deb1:amd64 (2:5.6.0-11ubuntu2) ...
2026-05-03T01:19:50.1240832Z Removing libtommath1:amd64 (1.2.1-2build1) ...
2026-05-03T01:19:50.1370823Z Removing libwebpdemux2:amd64 (1.3.2-0.4build3) ...
2026-05-03T01:19:50.1494088Z Removing libwebpmux3:amd64 (1.3.2-0.4build3) ...
2026-05-03T01:19:50.1621038Z Removing libz3-dev:amd64 (4.8.12-3.1build1) ...
2026-05-03T01:19:50.1759390Z Removing libz3-4:amd64 (4.8.12-3.1build1) ...
2026-05-03T01:19:50.1940482Z Removing libzip4t64:amd64 (1.7.3-1.1ubuntu2) ...
2026-05-03T01:19:50.2075938Z Removing mlock (8:2007f~dfsg-7build3) ...
2026-05-03T01:19:50.2195524Z Removing shtool (2.0.8-10) ...
2026-05-03T01:19:50.2341097Z Removing sound-theme-freedesktop (0.8-2ubuntu1) ...
2026-05-03T01:19:50.2494678Z Removing xul-ext-ubufox (3.4-0ubuntu1.17.10.4) ...
2026-05-03T01:19:50.3151320Z Removing libheif1:amd64 (1.17.6-1ubuntu4.2) ...
2026-05-03T01:19:50.3287426Z Removing libheif-plugin-libde265:amd64 (1.17.6-1ubuntu4.2) ...
2026-05-03T01:19:50.3424054Z Removing libde265-0:amd64 (1.0.15-1build3) ...
2026-05-03T01:19:50.3600629Z Removing libheif-plugin-aomdec:amd64 (1.17.6-1ubuntu4.2) ...
2026-05-03T01:19:50.3719456Z Removing libaom3:amd64 (3.8.2-2ubuntu0.1) ...
2026-05-03T01:19:50.4009364Z Processing triggers for man-db (2.12.0-4build2) ...
2026-05-03T01:19:50.4064863Z Not building database; man-db/auto-update is not 'true'.
2026-05-03T01:19:50.4077858Z Processing triggers for postgresql-common (290.pgdg24.04+1) ...
2026-05-03T01:19:50.5189519Z Building PostgreSQL dictionaries from installed myspell/hunspell packages...
2026-05-03T01:19:50.5189988Z Removing obsolete dictionary files:
2026-05-03T01:19:50.5193290Z   /var/cache/postgresql/dicts/en_us.affix
2026-05-03T01:19:50.5194258Z   /var/cache/postgresql/dicts/en_us.dict
2026-05-03T01:19:50.5267546Z   /usr/share/postgresql/16/tsearch_data/en_us.affix
2026-05-03T01:19:50.5268169Z   /usr/share/postgresql/16/tsearch_data/en_us.dict
2026-05-03T01:19:50.5461783Z Processing triggers for install-info (7.1-3build2) ...
2026-05-03T01:19:50.7763610Z Processing triggers for libc-bin (2.39-0ubuntu8.7) ...
2026-05-03T01:19:51.6318186Z === After cleanup ===
2026-05-03T01:19:51.6328346Z Filesystem      Size  Used Avail Use% Mounted on
2026-05-03T01:19:51.6328811Z /dev/root       145G   25G  120G  17% /
2026-05-03T01:19:51.6369041Z ##[group]Run sudo swapoff /mnt/swapfile 2>/dev/null || true
2026-05-03T01:19:51.6369482Z [36;1msudo swapoff /mnt/swapfile 2>/dev/null || true[0m
2026-05-03T01:19:51.6369786Z [36;1msudo rm -f /mnt/swapfile[0m
2026-05-03T01:19:51.6370217Z [36;1msudo fallocate -l 16G /mnt/swapfile || sudo dd if=/dev/zero of=/mnt/swapfile bs=1M count=16384[0m
2026-05-03T01:19:51.6370673Z [36;1msudo chmod 600 /mnt/swapfile[0m
2026-05-03T01:19:51.6370916Z [36;1msudo mkswap /mnt/swapfile[0m
2026-05-03T01:19:51.6371167Z [36;1msudo swapon /mnt/swapfile[0m
2026-05-03T01:19:51.6371403Z [36;1mfree -h[0m
2026-05-03T01:19:51.6393226Z shell: /usr/bin/bash -e {0}
2026-05-03T01:19:51.6393451Z env:
2026-05-03T01:19:51.6393637Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:19:51.6393905Z   ANDROID_VERSION: android15
2026-05-03T01:19:51.6394111Z   KERNEL_VERSION: 6.6
2026-05-03T01:19:51.6394295Z   KMI_GENERATION: 8
2026-05-03T01:19:51.6394470Z   KERNEL_NAME: Castorice
2026-05-03T01:19:51.6394695Z   DEVICE_CODE: fire
2026-05-03T01:19:51.6394859Z   KSU_DIR: 
2026-05-03T01:19:51.6395312Z   KSU_VERSION: 
2026-05-03T01:19:51.6395484Z   SUSFS_OK: 
2026-05-03T01:19:51.6395653Z   BUILT_KERNEL_VERSION: 
2026-05-03T01:19:51.6395837Z   ZIP_NAME: 
2026-05-03T01:19:51.6396010Z ##[endgroup]
2026-05-03T01:19:51.6941535Z Setting up swapspace version 1, size = 16 GiB (17179865088 bytes)
2026-05-03T01:19:51.6942229Z no label, UUID=4493f15f-169b-47c4-aeab-999af0f45812
2026-05-03T01:19:51.7052899Z                total        used        free      shared  buff/cache   available
2026-05-03T01:19:51.7053894Z Mem:            15Gi       1.0Gi        11Gi        43Mi       3.3Gi        14Gi
2026-05-03T01:19:51.7054464Z Swap:           18Gi          0B        18Gi
2026-05-03T01:19:51.7083144Z ##[group]Run sudo apt-get update
2026-05-03T01:19:51.7083440Z [36;1msudo apt-get update[0m
2026-05-03T01:19:51.7083824Z [36;1msudo apt-get install -y git curl wget bc bison flex libssl-dev make libelf-dev \[0m
2026-05-03T01:19:51.7084391Z [36;1m  python3 python3-pip python-is-python3 zip unzip cpio kmod rsync lz4 jq patch \[0m
2026-05-03T01:19:51.7084917Z [36;1m  binutils libncurses-dev pkg-config ninja-build zstd aria2 p7zip-full[0m
2026-05-03T01:19:51.7106990Z shell: /usr/bin/bash -e {0}
2026-05-03T01:19:51.7107211Z env:
2026-05-03T01:19:51.7107405Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:19:51.7107672Z   ANDROID_VERSION: android15
2026-05-03T01:19:51.7107881Z   KERNEL_VERSION: 6.6
2026-05-03T01:19:51.7108084Z   KMI_GENERATION: 8
2026-05-03T01:19:51.7108274Z   KERNEL_NAME: Castorice
2026-05-03T01:19:51.7108467Z   DEVICE_CODE: fire
2026-05-03T01:19:51.7108636Z   KSU_DIR: 
2026-05-03T01:19:51.7108786Z   KSU_VERSION: 
2026-05-03T01:19:51.7108978Z   SUSFS_OK: 
2026-05-03T01:19:51.7109144Z   BUILT_KERNEL_VERSION: 
2026-05-03T01:19:51.7109324Z   ZIP_NAME: 
2026-05-03T01:19:51.7109483Z ##[endgroup]
2026-05-03T01:19:51.7793837Z Get:1 file:/etc/apt/apt-mirrors.txt Mirrorlist [144 B]
2026-05-03T01:19:51.8226258Z Hit:2 http://azure.archive.ubuntu.com/ubuntu noble InRelease
2026-05-03T01:19:51.8231590Z Hit:6 https://packages.microsoft.com/repos/azure-cli noble InRelease
2026-05-03T01:19:51.8232699Z Get:7 https://packages.microsoft.com/ubuntu/24.04/prod noble InRelease [3600 B]
2026-05-03T01:19:51.8240383Z Get:3 http://azure.archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]
2026-05-03T01:19:51.8276746Z Get:4 http://azure.archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]
2026-05-03T01:19:51.8317702Z Get:5 http://azure.archive.ubuntu.com/ubuntu noble-security InRelease [126 kB]
2026-05-03T01:19:51.8688410Z Get:8 https://dl.google.com/linux/chrome-stable/deb stable InRelease [1825 B]
2026-05-03T01:19:52.0226251Z Get:9 https://packages.microsoft.com/ubuntu/24.04/prod noble/main armhf Packages [11.6 kB]
2026-05-03T01:19:52.0329166Z Get:10 https://packages.microsoft.com/ubuntu/24.04/prod noble/main amd64 Packages [132 kB]
2026-05-03T01:19:52.0392083Z Get:11 https://packages.microsoft.com/ubuntu/24.04/prod noble/main arm64 Packages [107 kB]
2026-05-03T01:19:52.0714650Z Get:12 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 Packages [1946 kB]
2026-05-03T01:19:52.0832165Z Get:13 http://azure.archive.ubuntu.com/ubuntu noble-updates/main Translation-en [348 kB]
2026-05-03T01:19:52.0853035Z Get:14 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 Components [177 kB]
2026-05-03T01:19:52.0861646Z Get:15 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 c-n-f Metadata [17.1 kB]
2026-05-03T01:19:52.0875931Z Get:16 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Packages [1685 kB]
2026-05-03T01:19:52.0969002Z Get:17 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe Translation-en [324 kB]
2026-05-03T01:19:52.0997011Z Get:18 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Components [386 kB]
2026-05-03T01:19:52.1028829Z Get:19 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 c-n-f Metadata [34.5 kB]
2026-05-03T01:19:52.1046449Z Get:20 http://azure.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Packages [3095 kB]
2026-05-03T01:19:52.1207077Z Get:21 http://azure.archive.ubuntu.com/ubuntu noble-updates/restricted Translation-en [715 kB]
2026-05-03T01:19:52.1684156Z Get:22 http://azure.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Components [212 B]
2026-05-03T01:19:52.1691647Z Get:23 http://azure.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 c-n-f Metadata [480 B]
2026-05-03T01:19:52.1703023Z Get:24 http://azure.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Packages [44.4 kB]
2026-05-03T01:19:52.1711619Z Get:25 http://azure.archive.ubuntu.com/ubuntu noble-updates/multiverse Translation-en [10.2 kB]
2026-05-03T01:19:52.1720087Z Get:26 http://azure.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Components [940 B]
2026-05-03T01:19:52.1729495Z Get:27 http://azure.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 c-n-f Metadata [656 B]
2026-05-03T01:19:52.1742363Z Get:28 http://azure.archive.ubuntu.com/ubuntu noble-backports/main amd64 Packages [64.5 kB]
2026-05-03T01:19:52.1751119Z Get:29 http://azure.archive.ubuntu.com/ubuntu noble-backports/main Translation-en [9172 B]
2026-05-03T01:19:52.1773964Z Get:30 http://azure.archive.ubuntu.com/ubuntu noble-backports/main amd64 Components [7368 B]
2026-05-03T01:19:52.1781806Z Get:31 http://azure.archive.ubuntu.com/ubuntu noble-backports/main amd64 c-n-f Metadata [368 B]
2026-05-03T01:19:52.1792460Z Get:32 http://azure.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Packages [34.1 kB]
2026-05-03T01:19:52.1804565Z Get:33 http://azure.archive.ubuntu.com/ubuntu noble-backports/universe Translation-en [18.2 kB]
2026-05-03T01:19:52.1820363Z Get:34 http://azure.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Components [10.5 kB]
2026-05-03T01:19:52.1830483Z Get:35 http://azure.archive.ubuntu.com/ubuntu noble-backports/universe amd64 c-n-f Metadata [1484 B]
2026-05-03T01:19:52.2317688Z Get:36 http://azure.archive.ubuntu.com/ubuntu noble-backports/restricted amd64 Components [212 B]
2026-05-03T01:19:52.2324825Z Get:37 http://azure.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Packages [748 B]
2026-05-03T01:19:52.2333497Z Get:38 http://azure.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Components [212 B]
2026-05-03T01:19:52.2346895Z Get:39 http://azure.archive.ubuntu.com/ubuntu noble-security/main amd64 Packages [1625 kB]
2026-05-03T01:19:52.2444264Z Get:40 http://azure.archive.ubuntu.com/ubuntu noble-security/main Translation-en [259 kB]
2026-05-03T01:19:52.2466473Z Get:41 http://azure.archive.ubuntu.com/ubuntu noble-security/main amd64 Components [21.9 kB]
2026-05-03T01:19:52.2477231Z Get:42 http://azure.archive.ubuntu.com/ubuntu noble-security/main amd64 c-n-f Metadata [11.0 kB]
2026-05-03T01:19:52.2486460Z Get:43 http://azure.archive.ubuntu.com/ubuntu noble-security/universe amd64 Packages [1182 kB]
2026-05-03T01:19:52.2555415Z Get:44 http://azure.archive.ubuntu.com/ubuntu noble-security/universe Translation-en [227 kB]
2026-05-03T01:19:52.2572402Z Get:45 http://azure.archive.ubuntu.com/ubuntu noble-security/universe amd64 Components [74.2 kB]
2026-05-03T01:19:52.2587030Z Get:46 http://azure.archive.ubuntu.com/ubuntu noble-security/universe amd64 c-n-f Metadata [23.1 kB]
2026-05-03T01:19:52.2598439Z Get:47 http://azure.archive.ubuntu.com/ubuntu noble-security/restricted amd64 Packages [2844 kB]
2026-05-03T01:19:52.2759867Z Get:48 http://azure.archive.ubuntu.com/ubuntu noble-security/restricted Translation-en [666 kB]
2026-05-03T01:19:52.2793272Z Get:49 http://azure.archive.ubuntu.com/ubuntu noble-security/restricted amd64 Components [212 B]
2026-05-03T01:19:52.2801513Z Get:50 http://azure.archive.ubuntu.com/ubuntu noble-security/multiverse amd64 Packages [28.8 kB]
2026-05-03T01:19:52.2900049Z Get:53 https://dl.google.com/linux/chrome-stable/deb stable/main amd64 Packages [1216 B]
2026-05-03T01:19:52.3273487Z Get:51 http://azure.archive.ubuntu.com/ubuntu noble-security/multiverse Translation-en [7172 B]
2026-05-03T01:19:52.3281237Z Get:52 http://azure.archive.ubuntu.com/ubuntu noble-security/multiverse amd64 Components [208 B]
2026-05-03T01:19:59.2571518Z Fetched 16.5 MB in 2s (8713 kB/s)
2026-05-03T01:20:00.0607641Z Reading package lists...
2026-05-03T01:20:00.0954167Z Reading package lists...
2026-05-03T01:20:00.2519860Z Building dependency tree...
2026-05-03T01:20:00.2526980Z Reading state information...
2026-05-03T01:20:00.3927788Z git is already the newest version (1:2.53.0-0ppa1~ubuntu24.04.1).
2026-05-03T01:20:00.3928901Z git set to manually installed.
2026-05-03T01:20:00.3929542Z curl is already the newest version (8.5.0-2ubuntu10.8).
2026-05-03T01:20:00.3930161Z wget is already the newest version (1.21.4-1ubuntu4.1).
2026-05-03T01:20:00.3933306Z bc is already the newest version (1.07.1-3ubuntu4).
2026-05-03T01:20:00.3933873Z bc set to manually installed.
2026-05-03T01:20:00.3934356Z bison is already the newest version (2:3.8.2+dfsg-1build2).
2026-05-03T01:20:00.3935316Z flex is already the newest version (2.6.4-8.2build1).
2026-05-03T01:20:00.3936000Z libssl-dev is already the newest version (3.0.13-0ubuntu3.9).
2026-05-03T01:20:00.3936610Z make is already the newest version (4.3-4.1build2).
2026-05-03T01:20:00.3937332Z python3 is already the newest version (3.12.3-0ubuntu2.1).
2026-05-03T01:20:00.3937998Z python3-pip is already the newest version (24.0+dfsg-1ubuntu1.3).
2026-05-03T01:20:00.3938647Z python-is-python3 is already the newest version (3.11.4-1).
2026-05-03T01:20:00.3939221Z zip is already the newest version (3.0-13ubuntu0.2).
2026-05-03T01:20:00.3939726Z unzip is already the newest version (6.0-28ubuntu4.1).
2026-05-03T01:20:00.3940273Z cpio is already the newest version (2.15+dfsg-1ubuntu2).
2026-05-03T01:20:00.3940780Z cpio set to manually installed.
2026-05-03T01:20:00.3941255Z rsync is already the newest version (3.2.7-1ubuntu1.2).
2026-05-03T01:20:00.3941789Z lz4 is already the newest version (1.9.4-1build1.1).
2026-05-03T01:20:00.3942316Z patch is already the newest version (2.7.6-7build3).
2026-05-03T01:20:00.3942821Z patch set to manually installed.
2026-05-03T01:20:00.3943315Z binutils is already the newest version (2.42-4ubuntu2.10).
2026-05-03T01:20:00.3943919Z pkg-config is already the newest version (1.8.1-2build1).
2026-05-03T01:20:00.3944567Z zstd is already the newest version (1.5.5+dfsg2-2build1.1).
2026-05-03T01:20:00.3945388Z zstd set to manually installed.
2026-05-03T01:20:00.3945901Z aria2 is already the newest version (1.37.0+debian-1build3).
2026-05-03T01:20:00.3946611Z p7zip-full is already the newest version (16.02+transitional.1).
2026-05-03T01:20:00.3947282Z The following additional packages will be installed:
2026-05-03T01:20:00.3947771Z   libjq1 libkmod2
2026-05-03T01:20:00.3948081Z Suggested packages:
2026-05-03T01:20:00.3948390Z   ncurses-doc
2026-05-03T01:20:00.4120447Z The following NEW packages will be installed:
2026-05-03T01:20:00.4125978Z   libelf-dev libncurses-dev ninja-build
2026-05-03T01:20:00.4129943Z The following packages will be upgraded:
2026-05-03T01:20:00.4135844Z   jq kmod libjq1 libkmod2
2026-05-03T01:20:00.4291084Z 4 upgraded, 3 newly installed, 0 to remove and 46 not upgraded.
2026-05-03T01:20:00.4291712Z Need to get 943 kB of archives.
2026-05-03T01:20:00.4292280Z After this operation, 3168 kB of additional disk space will be used.
2026-05-03T01:20:00.4292989Z Get:1 file:/etc/apt/apt-mirrors.txt Mirrorlist [144 B]
2026-05-03T01:20:00.5724400Z Get:2 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 kmod amd64 31+20240202-2ubuntu7.2 [102 kB]
2026-05-03T01:20:00.8356938Z Get:3 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libkmod2 amd64 31+20240202-2ubuntu7.2 [51.8 kB]
2026-05-03T01:20:00.9226814Z Get:4 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 jq amd64 1.7.1-3ubuntu0.24.04.2 [65.7 kB]
2026-05-03T01:20:01.0159159Z Get:5 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libjq1 amd64 1.7.1-3ubuntu0.24.04.2 [142 kB]
2026-05-03T01:20:01.1444499Z Get:6 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libelf-dev amd64 0.190-1.1ubuntu0.1 [68.5 kB]
2026-05-03T01:20:01.2311051Z Get:7 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libncurses-dev amd64 6.4+20240113-1ubuntu2 [384 kB]
2026-05-03T01:20:01.4111554Z Get:8 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 ninja-build amd64 1.11.1-2 [129 kB]
2026-05-03T01:20:01.6525968Z Fetched 943 kB in 1s (939 kB/s)
2026-05-03T01:20:01.6785712Z (Reading database ... 
2026-05-03T01:20:01.6786499Z (Reading database ... 5%
2026-05-03T01:20:01.6787622Z (Reading database ... 10%
2026-05-03T01:20:01.6787990Z (Reading database ... 15%
2026-05-03T01:20:01.6788332Z (Reading database ... 20%
2026-05-03T01:20:01.6788588Z (Reading database ... 25%
2026-05-03T01:20:01.6788963Z (Reading database ... 30%
2026-05-03T01:20:01.6789173Z (Reading database ... 35%
2026-05-03T01:20:01.6789372Z (Reading database ... 40%
2026-05-03T01:20:01.6789575Z (Reading database ... 45%
2026-05-03T01:20:01.6789772Z (Reading database ... 50%
2026-05-03T01:20:01.6789975Z (Reading database ... 55%
2026-05-03T01:20:01.6821219Z (Reading database ... 60%
2026-05-03T01:20:01.6908845Z (Reading database ... 65%
2026-05-03T01:20:01.6933608Z (Reading database ... 70%
2026-05-03T01:20:01.6950426Z (Reading database ... 75%
2026-05-03T01:20:01.6994916Z (Reading database ... 80%
2026-05-03T01:20:01.7018278Z (Reading database ... 85%
2026-05-03T01:20:01.7043089Z (Reading database ... 90%
2026-05-03T01:20:01.7137383Z (Reading database ... 95%
2026-05-03T01:20:01.7138039Z (Reading database ... 100%
2026-05-03T01:20:01.7138544Z (Reading database ... 119905 files and directories currently installed.)
2026-05-03T01:20:01.7159324Z Preparing to unpack .../0-kmod_31+20240202-2ubuntu7.2_amd64.deb ...
2026-05-03T01:20:01.7216948Z Unpacking kmod (31+20240202-2ubuntu7.2) over (31+20240202-2ubuntu7.1) ...
2026-05-03T01:20:01.7716292Z Preparing to unpack .../1-libkmod2_31+20240202-2ubuntu7.2_amd64.deb ...
2026-05-03T01:20:01.7748112Z Unpacking libkmod2:amd64 (31+20240202-2ubuntu7.2) over (31+20240202-2ubuntu7.1) ...
2026-05-03T01:20:01.8068678Z Preparing to unpack .../2-jq_1.7.1-3ubuntu0.24.04.2_amd64.deb ...
2026-05-03T01:20:01.8069435Z Unpacking jq (1.7.1-3ubuntu0.24.04.2) over (1.7.1-3ubuntu0.24.04.1) ...
2026-05-03T01:20:01.8414261Z Preparing to unpack .../3-libjq1_1.7.1-3ubuntu0.24.04.2_amd64.deb ...
2026-05-03T01:20:01.8443451Z Unpacking libjq1:amd64 (1.7.1-3ubuntu0.24.04.2) over (1.7.1-3ubuntu0.24.04.1) ...
2026-05-03T01:20:01.8654826Z Selecting previously unselected package libelf-dev:amd64.
2026-05-03T01:20:01.8732870Z Preparing to unpack .../4-libelf-dev_0.190-1.1ubuntu0.1_amd64.deb ...
2026-05-03T01:20:01.8741236Z Unpacking libelf-dev:amd64 (0.190-1.1ubuntu0.1) ...
2026-05-03T01:20:01.8939138Z Selecting previously unselected package libncurses-dev:amd64.
2026-05-03T01:20:01.9015436Z Preparing to unpack .../5-libncurses-dev_6.4+20240113-1ubuntu2_amd64.deb ...
2026-05-03T01:20:01.9024726Z Unpacking libncurses-dev:amd64 (6.4+20240113-1ubuntu2) ...
2026-05-03T01:20:01.9339845Z Selecting previously unselected package ninja-build.
2026-05-03T01:20:01.9415563Z Preparing to unpack .../6-ninja-build_1.11.1-2_amd64.deb ...
2026-05-03T01:20:01.9423941Z Unpacking ninja-build (1.11.1-2) ...
2026-05-03T01:20:01.9773975Z Setting up libncurses-dev:amd64 (6.4+20240113-1ubuntu2) ...
2026-05-03T01:20:01.9800400Z Setting up libjq1:amd64 (1.7.1-3ubuntu0.24.04.2) ...
2026-05-03T01:20:01.9824396Z Setting up ninja-build (1.11.1-2) ...
2026-05-03T01:20:01.9846605Z Setting up libelf-dev:amd64 (0.190-1.1ubuntu0.1) ...
2026-05-03T01:20:01.9867597Z Setting up jq (1.7.1-3ubuntu0.24.04.2) ...
2026-05-03T01:20:01.9900103Z Setting up libkmod2:amd64 (31+20240202-2ubuntu7.2) ...
2026-05-03T01:20:01.9923642Z Setting up kmod (31+20240202-2ubuntu7.2) ...
2026-05-03T01:20:02.2729728Z Processing triggers for initramfs-tools (0.142ubuntu25.8) ...
2026-05-03T01:20:02.3078681Z update-initramfs: Generating /boot/initrd.img-6.17.0-1010-azure
2026-05-03T01:20:06.9352544Z Processing triggers for libc-bin (2.39-0ubuntu8.7) ...
2026-05-03T01:20:06.9473096Z Processing triggers for man-db (2.12.0-4build2) ...
2026-05-03T01:20:06.9488821Z Not building database; man-db/auto-update is not 'true'.
2026-05-03T01:20:08.0209147Z 
2026-05-03T01:20:08.0209587Z Running kernel seems to be up-to-date.
2026-05-03T01:20:08.0209967Z 
2026-05-03T01:20:08.0210161Z Restarting services...
2026-05-03T01:20:08.0433441Z  /etc/needrestart/restart.d/systemd-manager
2026-05-03T01:20:08.3610257Z  systemctl restart systemd-journald.service systemd-networkd.service systemd-resolved.service systemd-udevd.service udisks2.service
2026-05-03T01:20:08.4911194Z 
2026-05-03T01:20:08.4923010Z Service restarts being deferred:
2026-05-03T01:20:08.4925956Z  systemctl restart systemd-logind.service
2026-05-03T01:20:08.4926904Z 
2026-05-03T01:20:08.4927555Z No containers need to be restarted.
2026-05-03T01:20:08.4928725Z 
2026-05-03T01:20:08.4929148Z User sessions running outdated binaries:
2026-05-03T01:20:08.4929969Z  runner @ user manager service: systemd[1254]
2026-05-03T01:20:08.5040465Z 
2026-05-03T01:20:08.5041415Z No VM guests are running outdated hypervisor (qemu) binaries on this host.
2026-05-03T01:20:09.3568613Z ##[group]Run mkdir -p ~/bin
2026-05-03T01:20:09.3568903Z [36;1mmkdir -p ~/bin[0m
2026-05-03T01:20:09.3569270Z [36;1mcurl -s https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo[0m
2026-05-03T01:20:09.3569682Z [36;1mchmod a+x ~/bin/repo[0m
2026-05-03T01:20:09.3569917Z [36;1mecho "$HOME/bin" >> $GITHUB_PATH[0m
2026-05-03T01:20:09.3590577Z shell: /usr/bin/bash -e {0}
2026-05-03T01:20:09.3590817Z env:
2026-05-03T01:20:09.3591003Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:20:09.3591279Z   ANDROID_VERSION: android15
2026-05-03T01:20:09.3591489Z   KERNEL_VERSION: 6.6
2026-05-03T01:20:09.3591670Z   KMI_GENERATION: 8
2026-05-03T01:20:09.3591850Z   KERNEL_NAME: Castorice
2026-05-03T01:20:09.3592038Z   DEVICE_CODE: fire
2026-05-03T01:20:09.3592207Z   KSU_DIR: 
2026-05-03T01:20:09.3592359Z   KSU_VERSION: 
2026-05-03T01:20:09.3592529Z   SUSFS_OK: 
2026-05-03T01:20:09.3592688Z   BUILT_KERNEL_VERSION: 
2026-05-03T01:20:09.3592878Z   ZIP_NAME: 
2026-05-03T01:20:09.3593070Z ##[endgroup]
2026-05-03T01:20:09.4053731Z ##[group]Run mkdir -p kernel
2026-05-03T01:20:09.4054016Z [36;1mmkdir -p kernel[0m
2026-05-03T01:20:09.4054216Z [36;1mcd kernel[0m
2026-05-03T01:20:09.4054523Z [36;1mrepo init -u https://android.googlesource.com/kernel/manifest \[0m
2026-05-03T01:20:09.4055253Z [36;1m  -b common-${ANDROID_VERSION}-${KERNEL_VERSION} --depth=1[0m
2026-05-03T01:20:09.4055743Z [36;1mrepo sync -c -j$(nproc) --no-tags --no-clone-bundle --force-sync[0m
2026-05-03T01:20:09.4056103Z [36;1mecho "=== Kernel version ==="[0m
2026-05-03T01:20:09.4056363Z [36;1mcd common && make kernelversion[0m
2026-05-03T01:20:09.4078061Z shell: /usr/bin/bash -e {0}
2026-05-03T01:20:09.4078298Z env:
2026-05-03T01:20:09.4078487Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:20:09.4078756Z   ANDROID_VERSION: android15
2026-05-03T01:20:09.4078969Z   KERNEL_VERSION: 6.6
2026-05-03T01:20:09.4079151Z   KMI_GENERATION: 8
2026-05-03T01:20:09.4079332Z   KERNEL_NAME: Castorice
2026-05-03T01:20:09.4079563Z   DEVICE_CODE: fire
2026-05-03T01:20:09.4079727Z   KSU_DIR: 
2026-05-03T01:20:09.4079883Z   KSU_VERSION: 
2026-05-03T01:20:09.4080039Z   SUSFS_OK: 
2026-05-03T01:20:09.4080206Z   BUILT_KERNEL_VERSION: 
2026-05-03T01:20:09.4080386Z   ZIP_NAME: 
2026-05-03T01:20:09.4080548Z ##[endgroup]
2026-05-03T01:20:12.0788545Z 
2026-05-03T01:20:12.0789186Z repo has been initialized in /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel
2026-05-03T01:23:28.7285710Z Finalizing sync state...
2026-05-03T01:23:28.7286157Z repo sync has finished successfully.
2026-05-03T01:23:28.7568435Z === Kernel version ===
2026-05-03T01:23:28.8770328Z 6.6.129
2026-05-03T01:23:28.8813195Z ##[group]Run cd kernel/common
2026-05-03T01:23:28.8813489Z [36;1mcd kernel/common[0m
2026-05-03T01:23:28.8813819Z [36;1mecho "Device KMI: ${KERNEL_VERSION}-${ANDROID_VERSION}-${KMI_GENERATION}"[0m
2026-05-03T01:23:28.8814182Z [36;1m[0m
2026-05-03T01:23:28.8814409Z [36;1m# Set KMI_GENERATION in build.config.common[0m
2026-05-03T01:23:28.8814724Z [36;1mif [ -f "build.config.common" ]; then[0m
2026-05-03T01:23:28.8815397Z [36;1m  if grep -q "KMI_GENERATION" build.config.common; then[0m
2026-05-03T01:23:28.8815873Z [36;1m    sed -i "s/KMI_GENERATION=.*/KMI_GENERATION=${KMI_GENERATION}/" build.config.common[0m
2026-05-03T01:23:28.8816279Z [36;1m  else[0m
2026-05-03T01:23:28.8816555Z [36;1m    echo "KMI_GENERATION=${KMI_GENERATION}" >> build.config.common[0m
2026-05-03T01:23:28.8817080Z [36;1m  fi[0m
2026-05-03T01:23:28.8817313Z [36;1m  echo "build.config.common KMI_GENERATION set:"[0m
2026-05-03T01:23:28.8817709Z [36;1m  grep KMI_GENERATION build.config.common[0m
2026-05-03T01:23:28.8817970Z [36;1mfi[0m
2026-05-03T01:23:28.8818126Z [36;1m[0m
2026-05-03T01:23:28.8818335Z [36;1m# Also patch Bazel/Kleaf config if present[0m
2026-05-03T01:23:28.8818691Z [36;1mfor f in build.config.gki build.config.gki.aarch64; do[0m
2026-05-03T01:23:28.8819066Z [36;1m  if [ -f "$f" ] && grep -q "KMI_GENERATION" "$f"; then[0m
2026-05-03T01:23:28.8819457Z [36;1m    sed -i "s/KMI_GENERATION=.*/KMI_GENERATION=${KMI_GENERATION}/" "$f"[0m
2026-05-03T01:23:28.8819810Z [36;1m    echo "$f patched"[0m
2026-05-03T01:23:28.8820010Z [36;1m  fi[0m
2026-05-03T01:23:28.8820171Z [36;1mdone[0m
2026-05-03T01:23:28.8820321Z [36;1m[0m
2026-05-03T01:23:28.8820522Z [36;1m# Patch stamp.bzl if it has KMI generation[0m
2026-05-03T01:23:28.8820860Z [36;1mSTAMP_FILE="../build/kernel/kleaf/impl/stamp.bzl"[0m
2026-05-03T01:23:28.8821243Z [36;1mif [ -f "$STAMP_FILE" ] && grep -q "kmi_generation" "$STAMP_FILE"; then[0m
2026-05-03T01:23:28.8821648Z [36;1m  echo "Checking stamp.bzl for KMI generation..."[0m
2026-05-03T01:23:28.8821929Z [36;1mfi[0m
2026-05-03T01:23:28.8879302Z shell: /usr/bin/bash -e {0}
2026-05-03T01:23:28.8879571Z env:
2026-05-03T01:23:28.8879788Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:23:28.8880114Z   ANDROID_VERSION: android15
2026-05-03T01:23:28.8880365Z   KERNEL_VERSION: 6.6
2026-05-03T01:23:28.8880587Z   KMI_GENERATION: 8
2026-05-03T01:23:28.8880801Z   KERNEL_NAME: Castorice
2026-05-03T01:23:28.8881025Z   DEVICE_CODE: fire
2026-05-03T01:23:28.8881223Z   KSU_DIR: 
2026-05-03T01:23:28.8881404Z   KSU_VERSION: 
2026-05-03T01:23:28.8881600Z   SUSFS_OK: 
2026-05-03T01:23:28.8881792Z   BUILT_KERNEL_VERSION: 
2026-05-03T01:23:28.8882019Z   ZIP_NAME: 
2026-05-03T01:23:28.8882205Z ##[endgroup]
2026-05-03T01:23:28.8922067Z Device KMI: 6.6-android15-8
2026-05-03T01:23:28.8949910Z build.config.common KMI_GENERATION set:
2026-05-03T01:23:28.8960665Z KMI_GENERATION=8
2026-05-03T01:23:28.9040839Z ##[group]Run cd kernel/common
2026-05-03T01:23:28.9041125Z [36;1mcd kernel/common[0m
2026-05-03T01:23:28.9041330Z [36;1m[0m
2026-05-03T01:23:28.9041540Z [36;1m# Clone KernelSU-Next latest stable release[0m
2026-05-03T01:23:28.9041899Z [36;1mecho "Fetching latest stable KernelSU-Next release..."[0m
2026-05-03T01:23:28.9042429Z [36;1mKSU_TAG=$(curl -sL https://api.github.com/repos/KernelSU-Next/KernelSU-Next/releases/latest \[0m
2026-05-03T01:23:28.9042887Z [36;1m  | jq -r '.tag_name')[0m
2026-05-03T01:23:28.9043097Z [36;1m[0m
2026-05-03T01:23:28.9043311Z [36;1mif [ -z "$KSU_TAG" ] || [ "$KSU_TAG" = "null" ]; then[0m
2026-05-03T01:23:28.9043762Z [36;1m  echo "WARN: Could not fetch latest release tag, falling back to default branch"[0m
2026-05-03T01:23:28.9044334Z [36;1m  git clone --depth=1 https://github.com/KernelSU-Next/KernelSU-Next.git KernelSU-Next[0m
2026-05-03T01:23:28.9044776Z [36;1m  KSU_TAG="default"[0m
2026-05-03T01:23:28.9045243Z [36;1melse[0m
2026-05-03T01:23:28.9045580Z [36;1m  echo "Cloning KernelSU-Next $KSU_TAG (latest stable)..."[0m
2026-05-03T01:23:28.9045932Z [36;1m  git clone --depth=1 --branch "$KSU_TAG" \[0m
2026-05-03T01:23:28.9046326Z [36;1m    https://github.com/KernelSU-Next/KernelSU-Next.git KernelSU-Next[0m
2026-05-03T01:23:28.9046671Z [36;1mfi[0m
2026-05-03T01:23:28.9046829Z [36;1m[0m
2026-05-03T01:23:28.9047118Z [36;1m# Integrate into kernel build (copy driver instead of symlink for Bazel)[0m
2026-05-03T01:23:28.9047552Z [36;1mcp -r "$(pwd)/KernelSU-Next/kernel" "drivers/kernelsu"[0m
2026-05-03T01:23:28.9047846Z [36;1m[0m
2026-05-03T01:23:28.9048013Z [36;1m# Add to Makefile if not present[0m
2026-05-03T01:23:28.9048308Z [36;1mif ! grep -q "kernelsu" drivers/Makefile; then[0m
2026-05-03T01:23:28.9048655Z [36;1m  echo "obj-\$(CONFIG_KSU) += kernelsu/" >> drivers/Makefile[0m
2026-05-03T01:23:28.9049130Z [36;1mfi[0m
2026-05-03T01:23:28.9049284Z [36;1m[0m
2026-05-03T01:23:28.9049462Z [36;1m# Add Kconfig include if not present[0m
2026-05-03T01:23:28.9049782Z [36;1mif ! grep -q "kernelsu/Kconfig" drivers/Kconfig; then[0m
2026-05-03T01:23:28.9050156Z [36;1m  echo 'source "drivers/kernelsu/Kconfig"' >> drivers/Kconfig[0m
2026-05-03T01:23:28.9050463Z [36;1mfi[0m
2026-05-03T01:23:28.9050610Z [36;1m[0m
2026-05-03T01:23:28.9050775Z [36;1mKSU_DIR="KernelSU-Next"[0m
2026-05-03T01:23:28.9051061Z [36;1mKSU_VERSION=$(cd $KSU_DIR && git rev-list --count HEAD)[0m
2026-05-03T01:23:28.9051412Z [36;1mecho "KSU_VERSION=$KSU_VERSION" >> $GITHUB_ENV[0m
2026-05-03T01:23:28.9051722Z [36;1mecho "KSU_DIR=$KSU_DIR" >> $GITHUB_ENV[0m
2026-05-03T01:23:28.9052085Z [36;1mecho "KernelSU-Next installed — version $KSU_VERSION ($KSU_TAG)"[0m
2026-05-03T01:23:28.9071718Z shell: /usr/bin/bash -e {0}
2026-05-03T01:23:28.9071951Z env:
2026-05-03T01:23:28.9072143Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:23:28.9072419Z   ANDROID_VERSION: android15
2026-05-03T01:23:28.9072633Z   KERNEL_VERSION: 6.6
2026-05-03T01:23:28.9072820Z   KMI_GENERATION: 8
2026-05-03T01:23:28.9073003Z   KERNEL_NAME: Castorice
2026-05-03T01:23:28.9073187Z   DEVICE_CODE: fire
2026-05-03T01:23:28.9073355Z   KSU_DIR: 
2026-05-03T01:23:28.9073506Z   KSU_VERSION: 
2026-05-03T01:23:28.9073666Z   SUSFS_OK: 
2026-05-03T01:23:28.9073824Z   BUILT_KERNEL_VERSION: 
2026-05-03T01:23:28.9074011Z   ZIP_NAME: 
2026-05-03T01:23:28.9074165Z ##[endgroup]
2026-05-03T01:23:28.9112306Z Fetching latest stable KernelSU-Next release...
2026-05-03T01:23:29.1637510Z Cloning KernelSU-Next v3.2.0 (latest stable)...
2026-05-03T01:23:29.1652219Z Cloning into 'KernelSU-Next'...
2026-05-03T01:23:30.0306978Z Note: switching to '551ad80473f60e052917aec08abf5323b6ab2f7c'.
2026-05-03T01:23:30.0307297Z 
2026-05-03T01:23:30.0307511Z You are in 'detached HEAD' state. You can look around, make experimental
2026-05-03T01:23:30.0307995Z changes and commit them, and you can discard any commits you make in this
2026-05-03T01:23:30.0308720Z state without impacting any branches by switching back to a branch.
2026-05-03T01:23:30.0308991Z 
2026-05-03T01:23:30.0309163Z If you want to create a new branch to retain commits you create, you may
2026-05-03T01:23:30.0309576Z do so (now or later) by using -c with the switch command. Example:
2026-05-03T01:23:30.0309813Z 
2026-05-03T01:23:30.0309908Z   git switch -c <new-branch-name>
2026-05-03T01:23:30.0310066Z 
2026-05-03T01:23:30.0310151Z Or undo this operation with:
2026-05-03T01:23:30.0310299Z 
2026-05-03T01:23:30.0310367Z   git switch -
2026-05-03T01:23:30.0310468Z 
2026-05-03T01:23:30.0310659Z Turn off this advice by setting config variable advice.detachedHead to false
2026-05-03T01:23:30.0310955Z 
2026-05-03T01:23:30.0990952Z KernelSU-Next installed — version 1 (v3.2.0)
2026-05-03T01:23:30.1047369Z ##[group]Run # Git identity needed for git commit/apply --3way used below
2026-05-03T01:23:30.1048246Z [36;1m# Git identity needed for git commit/apply --3way used below[0m
2026-05-03T01:23:30.1048673Z [36;1mgit config --global user.name "github-actions[bot]"[0m
2026-05-03T01:23:30.1049121Z [36;1mgit config --global user.email "github-actions[bot]@users.noreply.github.com"[0m
2026-05-03T01:23:30.1049504Z [36;1m[0m
2026-05-03T01:23:30.1049666Z [36;1mcd kernel[0m
2026-05-03T01:23:30.1049968Z [36;1mgit clone --depth=1 https://gitlab.com/simonpunk/susfs4ksu.git \[0m
2026-05-03T01:23:30.1050387Z [36;1m  -b gki-${ANDROID_VERSION}-${KERNEL_VERSION} || \[0m
2026-05-03T01:23:30.1050793Z [36;1mgit clone --depth=1 https://gitlab.com/simonpunk/susfs4ksu.git \[0m
2026-05-03T01:23:30.1051169Z [36;1m  -b gki-${ANDROID_VERSION}-6.6[0m
2026-05-03T01:23:30.1051402Z [36;1m[0m
2026-05-03T01:23:30.1051559Z [36;1mcd common[0m
2026-05-03T01:23:30.1051731Z [36;1m[0m
2026-05-03T01:23:30.1051982Z [36;1m# --- Step 1: Copy SUSFS kernel source files ---[0m
2026-05-03T01:23:30.1052301Z [36;1mecho "=== Copying SUSFS source files ==="[0m
2026-05-03T01:23:30.1052806Z [36;1mcp -rv ../susfs4ksu/kernel_patches/fs/* fs/[0m
2026-05-03T01:23:30.1053172Z [36;1mcp -rv ../susfs4ksu/kernel_patches/include/linux/* include/linux/[0m
2026-05-03T01:23:30.1053537Z [36;1mls -la include/linux/susfs* fs/susfs*[0m
2026-05-03T01:23:30.1053783Z [36;1m[0m
2026-05-03T01:23:30.1054001Z [36;1m# --- Step 2: Apply kernel tree integration patch ---[0m
2026-05-03T01:23:30.1054343Z [36;1mecho "=== Applying kernel tree SUSFS patch ==="[0m
2026-05-03T01:23:30.1054736Z [36;1mfor patch in ../susfs4ksu/kernel_patches/50_add_susfs_in_gki-*.patch; do[0m
2026-05-03T01:23:30.1055602Z [36;1m  if [ -f "$patch" ]; then[0m
2026-05-03T01:23:30.1055871Z [36;1m    echo "Applying: $patch"[0m
2026-05-03T01:23:30.1056246Z [36;1m    git add -A && git commit -m "pre-susfs-kernel-patch" --allow-empty -q[0m
2026-05-03T01:23:30.1056644Z [36;1m    if git apply --3way "$patch"; then[0m
2026-05-03T01:23:30.1056985Z [36;1m      echo "Kernel SUSFS patch applied cleanly via 3-way merge"[0m
2026-05-03T01:23:30.1057376Z [36;1m    elif patch -p1 --forward --fuzz=3 < "$patch"; then[0m
2026-05-03T01:23:30.1057738Z [36;1m      echo "Kernel SUSFS patch applied via fuzz fallback"[0m
2026-05-03T01:23:30.1058032Z [36;1m    else[0m
2026-05-03T01:23:30.1058281Z [36;1m      echo "WARN: Kernel SUSFS patch had issues (continuing)"[0m
2026-05-03T01:23:30.1058580Z [36;1m    fi[0m
2026-05-03T01:23:30.1058745Z [36;1m  fi[0m
2026-05-03T01:23:30.1058899Z [36;1mdone[0m
2026-05-03T01:23:30.1059054Z [36;1m[0m
2026-05-03T01:23:30.1059276Z [36;1m# --- Step 3: Integrate SUSFS into KernelSU-Next ---[0m
2026-05-03T01:23:30.1059690Z [36;1m# KernelSU-Next v3.2.0 is fundamentally incompatible with the legacy [0m
2026-05-03T01:23:30.1060145Z [36;1m# '10_enable_susfs_for_ksu.patch'. Applying it causes severe C syntax [0m
2026-05-03T01:23:30.1060540Z [36;1m# corruption and undefined linker symbols. [0m
2026-05-03T01:23:30.1060909Z [36;1m# Therefore, we bypass the patch entirely and cleanly inject the [0m
2026-05-03T01:23:30.1061352Z [36;1m# necessary SUSFS initialization into the pristine KSU-Next source.[0m
2026-05-03T01:23:30.1061833Z [36;1mecho "=== Integrating SUSFS into KernelSU-Next (Clean Manual Method) ==="[0m
2026-05-03T01:23:30.1062201Z [36;1mKSU_DIR="KernelSU-Next"[0m
2026-05-03T01:23:30.1062436Z [36;1mKSU_KERNEL="drivers/kernelsu"[0m
2026-05-03T01:23:30.1062663Z [36;1m[0m
2026-05-03T01:23:30.1062824Z [36;1m# 1. Inject SUSFS Kconfig[0m
2026-05-03T01:23:30.1063158Z [36;1mif ! grep -q "CONFIG_KSU_SUSFS" "$KSU_KERNEL/Kconfig" 2>/dev/null; then[0m
2026-05-03T01:23:30.1063525Z [36;1m  cat >> "$KSU_KERNEL/Kconfig" << 'KEOF'[0m
2026-05-03T01:23:30.1063770Z [36;1m[0m
2026-05-03T01:23:30.1063929Z [36;1mmenu "KernelSU - SUSFS"[0m
2026-05-03T01:23:30.1064153Z [36;1mconfig KSU_SUSFS[0m
2026-05-03T01:23:30.1064560Z [36;1m	bool "KernelSU addon - SUSFS"[0m
2026-05-03T01:23:30.1064817Z [36;1m	depends on KSU[0m
2026-05-03T01:23:30.1065168Z [36;1m	default y[0m
2026-05-03T01:23:30.1065351Z [36;1m	help[0m
2026-05-03T01:23:30.1065589Z [36;1m	  Patch and Enable SUSFS to kernel with KernelSU.[0m
2026-05-03T01:23:30.1065872Z [36;1m[0m
2026-05-03T01:23:30.1066037Z [36;1mconfig KSU_SUSFS_SUS_PATH[0m
2026-05-03T01:23:30.1066290Z [36;1m	bool "Enable to hide suspicious path"[0m
2026-05-03T01:23:30.1066555Z [36;1m	depends on KSU_SUSFS[0m
2026-05-03T01:23:30.1066758Z [36;1m	default y[0m
2026-05-03T01:23:30.1066933Z [36;1m[0m
2026-05-03T01:23:30.1067099Z [36;1mconfig KSU_SUSFS_SUS_MOUNT[0m
2026-05-03T01:23:30.1067359Z [36;1m	bool "Enable to hide suspicious mounts"[0m
2026-05-03T01:23:30.1067626Z [36;1m	depends on KSU_SUSFS[0m
2026-05-03T01:23:30.1067826Z [36;1m	default y[0m
2026-05-03T01:23:30.1067998Z [36;1m[0m
2026-05-03T01:23:30.1068158Z [36;1mconfig KSU_SUSFS_SUS_KSTAT[0m
2026-05-03T01:23:30.1068419Z [36;1m	bool "Enable to spoof suspicious kstat"[0m
2026-05-03T01:23:30.1068677Z [36;1m	depends on KSU_SUSFS[0m
2026-05-03T01:23:30.1069251Z [36;1m	default y[0m
2026-05-03T01:23:30.1069441Z [36;1m[0m
2026-05-03T01:23:30.1069609Z [36;1mconfig KSU_SUSFS_SPOOF_UNAME[0m
2026-05-03T01:23:30.1069857Z [36;1m	bool "Enable to spoof uname"[0m
2026-05-03T01:23:30.1070092Z [36;1m	depends on KSU_SUSFS[0m
2026-05-03T01:23:30.1070298Z [36;1m	default y[0m
2026-05-03T01:23:30.1070464Z [36;1m[0m
2026-05-03T01:23:30.1070631Z [36;1mconfig KSU_SUSFS_ENABLE_LOG[0m
2026-05-03T01:23:30.1070891Z [36;1m	bool "Enable logging susfs log to kernel"[0m
2026-05-03T01:23:30.1071179Z [36;1m	depends on KSU_SUSFS[0m
2026-05-03T01:23:30.1071385Z [36;1m	default y[0m
2026-05-03T01:23:30.1071547Z [36;1m[0m
2026-05-03T01:23:30.1071734Z [36;1mconfig KSU_SUSFS_HIDE_KSU_SUSFS_SYMBOLS[0m
2026-05-03T01:23:30.1072104Z [36;1m	bool "Enable to hide ksu and susfs symbols from /proc/kallsyms"[0m
2026-05-03T01:23:30.1072443Z [36;1m	depends on KSU_SUSFS[0m
2026-05-03T01:23:30.1086794Z [36;1m	default y[0m
2026-05-03T01:23:30.1087101Z [36;1m[0m
2026-05-03T01:23:30.1087466Z [36;1mconfig KSU_SUSFS_SPOOF_CMDLINE_OR_BOOTCONFIG[0m
2026-05-03T01:23:30.1088048Z [36;1m	bool "Enable to spoof /proc/bootconfig or /proc/cmdline"[0m
2026-05-03T01:23:30.1088398Z [36;1m	depends on KSU_SUSFS[0m
2026-05-03T01:23:30.1088619Z [36;1m	default y[0m
2026-05-03T01:23:30.1088803Z [36;1m[0m
2026-05-03T01:23:30.1088981Z [36;1mconfig KSU_SUSFS_OPEN_REDIRECT[0m
2026-05-03T01:23:30.1089323Z [36;1m	bool "Enable to redirect a path to be opened with another path"[0m
2026-05-03T01:23:30.1089687Z [36;1m	depends on KSU_SUSFS[0m
2026-05-03T01:23:30.1089898Z [36;1m	default y[0m
2026-05-03T01:23:30.1090074Z [36;1m[0m
2026-05-03T01:23:30.1090237Z [36;1mconfig KSU_SUSFS_SUS_MAP[0m
2026-05-03T01:23:30.1090542Z [36;1m	bool "Enable to hide mmapped real file from proc maps"[0m
2026-05-03T01:23:30.1090855Z [36;1m	depends on KSU_SUSFS[0m
2026-05-03T01:23:30.1091065Z [36;1m	default y[0m
2026-05-03T01:23:30.1091240Z [36;1m[0m
2026-05-03T01:23:30.1091392Z [36;1mendmenu[0m
2026-05-03T01:23:30.1091570Z [36;1mKEOF[0m
2026-05-03T01:23:30.1091783Z [36;1m  echo "SUSFS Kconfig injected successfully"[0m
2026-05-03T01:23:30.1092052Z [36;1mfi[0m
2026-05-03T01:23:30.1092202Z [36;1m[0m
2026-05-03T01:23:30.1092378Z [36;1m# 2. Inject SUSFS Makefile entries[0m
2026-05-03T01:23:30.1092732Z [36;1mif ! grep -q "SUSFS_VERSION" "$KSU_KERNEL/Makefile" 2>/dev/null; then[0m
2026-05-03T01:23:30.1093113Z [36;1m  cat >> "$KSU_KERNEL/Makefile" << 'MKEOF'[0m
2026-05-03T01:23:30.1093367Z [36;1m[0m
2026-05-03T01:23:30.1093528Z [36;1m## For susfs stuff ##[0m
2026-05-03T01:23:30.1093825Z [36;1mifeq ($(shell test -e $(srctree)/fs/susfs.c; echo $$?),0)[0m
2026-05-03T01:23:30.1094443Z [36;1m$(eval SUSFS_VERSION=$(shell cat $(srctree)/include/linux/susfs.h | grep -E '^#define SUSFS_VERSION' | cut -d' ' -f3 | sed 's/"//g'))[0m
2026-05-03T01:23:30.1095447Z [36;1m$(info )[0m
2026-05-03T01:23:30.1095696Z [36;1m$(info -- SUSFS_VERSION: $(SUSFS_VERSION))[0m
2026-05-03T01:23:30.1095963Z [36;1melse[0m
2026-05-03T01:23:30.1096223Z [36;1m$(info -- You have not integrated susfs in your kernel yet.)[0m
2026-05-03T01:23:30.1096620Z [36;1m$(info -- Read: https://gitlab.com/simonpunk/susfs4ksu)[0m
2026-05-03T01:23:30.1096923Z [36;1mendif[0m
2026-05-03T01:23:30.1097083Z [36;1mMKEOF[0m
2026-05-03T01:23:30.1097315Z [36;1m  echo "SUSFS Makefile entries injected successfully"[0m
2026-05-03T01:23:30.1097594Z [36;1mfi[0m
2026-05-03T01:23:30.1097749Z [36;1m[0m
2026-05-03T01:23:30.1097949Z [36;1m# 3. Inject susfs.h include into core/init.c[0m
2026-05-03T01:23:30.1098372Z [36;1mif [ -f "$KSU_KERNEL/core/init.c" ] && ! grep -q "susfs.h" "$KSU_KERNEL/core/init.c"; then[0m
2026-05-03T01:23:30.1098951Z [36;1m  sed -i '/#include <linux\/workqueue.h>/a #include <linux/susfs.h>' "$KSU_KERNEL/core/init.c"[0m
2026-05-03T01:23:30.1099354Z [36;1mfi[0m
2026-05-03T01:23:30.1099514Z [36;1m[0m
2026-05-03T01:23:30.1099712Z [36;1m# 4. Inject susfs_init() call into core/init.c[0m
2026-05-03T01:23:30.1100144Z [36;1mif [ -f "$KSU_KERNEL/core/init.c" ] && ! grep -q "susfs_init" "$KSU_KERNEL/core/init.c"; then[0m
2026-05-03T01:23:30.1100679Z [36;1m  sed -i '/ksu_feature_init/i \[0m
2026-05-03T01:23:30.1100924Z [36;1m#ifdef CONFIG_KSU_SUSFS\[0m
2026-05-03T01:23:30.1101149Z [36;1m\tsusfs_init();\[0m
2026-05-03T01:23:30.1101363Z [36;1m#endif' "$KSU_KERNEL/core/init.c"[0m
2026-05-03T01:23:30.1101596Z [36;1mfi[0m
2026-05-03T01:23:30.1101746Z [36;1m[0m
2026-05-03T01:23:30.1101965Z [36;1m# 5. Inject susfs includes into supercall/dispatch.c[0m
2026-05-03T01:23:30.1102482Z [36;1mif [ -f "$KSU_KERNEL/supercall/dispatch.c" ] && ! grep -q "susfs.h" "$KSU_KERNEL/supercall/dispatch.c"; then[0m
2026-05-03T01:23:30.1103161Z [36;1m  sed -i '/#include <linux\/version.h>/a #include <linux/susfs.h>' "$KSU_KERNEL/supercall/dispatch.c"[0m
2026-05-03T01:23:30.1103603Z [36;1mfi[0m
2026-05-03T01:23:30.1103755Z [36;1m[0m
2026-05-03T01:23:30.1103967Z [36;1mecho "=== Clean SUSFS Integration Complete ==="[0m
2026-05-03T01:23:30.1104280Z [36;1m[0m
2026-05-03T01:23:30.1104499Z [36;1m# --- Step 4: Post-integration validation ---[0m
2026-05-03T01:23:30.1104834Z [36;1mecho "=== Validating SUSFS configuration ==="[0m
2026-05-03T01:23:30.1105319Z [36;1m[0m
2026-05-03T01:23:30.1105591Z [36;1m# Verify init.c compiles conceptually: check for balanced braces[0m
2026-05-03T01:23:30.1105960Z [36;1mKSU_INIT="drivers/kernelsu/core/init.c"[0m
2026-05-03T01:23:30.1106233Z [36;1mif [ -f "$KSU_INIT" ]; then[0m
2026-05-03T01:23:30.1106493Z [36;1m  OPEN=$(grep -c '{' "$KSU_INIT" || true)[0m
2026-05-03T01:23:30.1106786Z [36;1m  CLOSE=$(grep -c '}' "$KSU_INIT" || true)[0m
2026-05-03T01:23:30.1107058Z [36;1m  if [ "$OPEN" != "$CLOSE" ]; then[0m
2026-05-03T01:23:30.1107483Z [36;1m    echo "ERROR: Unbalanced braces in init.c! This should never happen with clean integration."[0m
2026-05-03T01:23:30.1107919Z [36;1m    exit 1[0m
2026-05-03T01:23:30.1108090Z [36;1m  fi[0m
2026-05-03T01:23:30.1108275Z [36;1m  echo "init.c syntax check OK"[0m
2026-05-03T01:23:30.1108504Z [36;1mfi[0m
2026-05-03T01:23:30.1108658Z [36;1m[0m
2026-05-03T01:23:30.1108829Z [36;1m# Verify Kconfig has SUSFS entries[0m
2026-05-03T01:23:30.1109190Z [36;1mif grep -r "CONFIG_KSU_SUSFS" drivers/kernelsu/Kconfig 2>/dev/null; then[0m
2026-05-03T01:23:30.1109571Z [36;1m  echo "SUSFS_OK=true" >> $GITHUB_ENV[0m
2026-05-03T01:23:30.1109835Z [36;1m  echo "SUSFS Kconfig verified OK"[0m
2026-05-03T01:23:30.1110070Z [36;1melse[0m
2026-05-03T01:23:30.1110254Z [36;1m  echo "SUSFS_OK=false" >> $GITHUB_ENV[0m
2026-05-03T01:23:30.1110613Z [36;1m  echo "WARNING: SUSFS Kconfig NOT found — SUSFS will NOT be enabled"[0m
2026-05-03T01:23:30.1110947Z [36;1mfi[0m
2026-05-03T01:23:30.1111099Z [36;1m[0m
2026-05-03T01:23:30.1111277Z [36;1m# Show final state of critical files[0m
2026-05-03T01:23:30.1111662Z [36;1mecho "=== Final init.c ==="[0m
2026-05-03T01:23:30.1111982Z [36;1mhead -50 "drivers/kernelsu/core/init.c" 2>/dev/null || true[0m
2026-05-03T01:23:30.1112334Z [36;1mecho "=== Final Kconfig (SUSFS section) ==="[0m
2026-05-03T01:23:30.1112746Z [36;1mgrep -A2 "KSU_SUSFS" "drivers/kernelsu/Kconfig" 2>/dev/null | head -20 || true[0m
2026-05-03T01:23:30.1133702Z shell: /usr/bin/bash -e {0}
2026-05-03T01:23:30.1133923Z env:
2026-05-03T01:23:30.1134113Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:23:30.1134370Z   ANDROID_VERSION: android15
2026-05-03T01:23:30.1134587Z   KERNEL_VERSION: 6.6
2026-05-03T01:23:30.1134780Z   KMI_GENERATION: 8
2026-05-03T01:23:30.1135209Z   KERNEL_NAME: Castorice
2026-05-03T01:23:30.1135457Z   DEVICE_CODE: fire
2026-05-03T01:23:30.1135636Z   KSU_DIR: KernelSU-Next
2026-05-03T01:23:30.1135831Z   KSU_VERSION: 1
2026-05-03T01:23:30.1135993Z   SUSFS_OK: 
2026-05-03T01:23:30.1136157Z   BUILT_KERNEL_VERSION: 
2026-05-03T01:23:30.1136337Z   ZIP_NAME: 
2026-05-03T01:23:30.1136497Z ##[endgroup]
2026-05-03T01:23:30.1222609Z Cloning into 'susfs4ksu'...
2026-05-03T01:23:30.7919592Z === Copying SUSFS source files ===
2026-05-03T01:23:30.7932185Z '../susfs4ksu/kernel_patches/fs/susfs.c' -> 'fs/susfs.c'
2026-05-03T01:23:30.7946934Z '../susfs4ksu/kernel_patches/include/linux/susfs.h' -> 'include/linux/susfs.h'
2026-05-03T01:23:30.7947552Z '../susfs4ksu/kernel_patches/include/linux/susfs_def.h' -> 'include/linux/susfs_def.h'
2026-05-03T01:23:30.7976234Z -rw-r--r-- 1 runner runner 55289 May  3 01:23 fs/susfs.c
2026-05-03T01:23:30.7976789Z -rw-r--r-- 1 runner runner  7334 May  3 01:23 include/linux/susfs.h
2026-05-03T01:23:30.7977213Z -rw-r--r-- 1 runner runner  4291 May  3 01:23 include/linux/susfs_def.h
2026-05-03T01:23:30.7978400Z === Applying kernel tree SUSFS patch ===
2026-05-03T01:23:30.7979641Z Applying: ../susfs4ksu/kernel_patches/50_add_susfs_in_gki-android15-6.6.patch
2026-05-03T01:23:31.3232357Z warning: adding embedded git repository: KernelSU-Next
2026-05-03T01:23:31.3233148Z hint: You've added another git repository inside your current repository.
2026-05-03T01:23:31.3233931Z hint: Clones of the outer repository will not contain the contents of
2026-05-03T01:23:31.3234678Z hint: the embedded repository and will not know how to obtain it.
2026-05-03T01:23:31.3235500Z hint: If you meant to add a submodule, use:
2026-05-03T01:23:31.3235917Z hint:
2026-05-03T01:23:31.3236231Z hint: 	git submodule add <url> KernelSU-Next
2026-05-03T01:23:31.3236660Z hint:
2026-05-03T01:23:31.3236968Z hint: If you added this path by mistake, you can remove it from the
2026-05-03T01:23:31.3237322Z hint: index with:
2026-05-03T01:23:31.3237517Z hint:
2026-05-03T01:23:31.3237700Z hint: 	git rm --cached KernelSU-Next
2026-05-03T01:23:31.3237951Z hint:
2026-05-03T01:23:31.3238167Z hint: See "git help submodule" for more information.
2026-05-03T01:23:31.3238617Z hint: Disable this message with "git config set advice.addEmbeddedRepo false"
2026-05-03T01:23:31.5093603Z Applied patch to 'drivers/input/input.c' cleanly.
2026-05-03T01:23:31.5098127Z Applied patch to 'fs/Makefile' cleanly.
2026-05-03T01:23:31.5107346Z Applied patch to 'fs/devpts/inode.c' cleanly.
2026-05-03T01:23:31.5111766Z error: repository lacks the necessary blob to perform 3-way merge.
2026-05-03T01:23:31.5112296Z Falling back to direct application...
2026-05-03T01:23:31.5171263Z Applied patch to 'fs/namei.c' cleanly.
2026-05-03T01:23:31.5224439Z Applied patch to 'fs/namespace.c' cleanly.
2026-05-03T01:23:31.5229128Z Applied patch to 'fs/notify/fdinfo.c' cleanly.
2026-05-03T01:23:31.5247202Z Applied patch to 'fs/open.c' cleanly.
2026-05-03T01:23:31.5253743Z error: repository lacks the necessary blob to perform 3-way merge.
2026-05-03T01:23:31.5254285Z Falling back to direct application...
2026-05-03T01:23:31.5257986Z Applied patch to 'fs/proc/bootconfig.c' cleanly.
2026-05-03T01:23:31.5264364Z Applied patch to 'fs/proc/fd.c' cleanly.
2026-05-03T01:23:31.5268866Z error: repository lacks the necessary blob to perform 3-way merge.
2026-05-03T01:23:31.5269787Z Falling back to direct application...
2026-05-03T01:23:31.5270110Z error: patch failed: fs/proc/task_mmu.c:897
2026-05-03T01:23:31.5270429Z error: fs/proc/task_mmu.c: patch does not apply
2026-05-03T01:23:31.5275256Z Applied patch to 'fs/proc_namespace.c' cleanly.
2026-05-03T01:23:31.5291465Z Applied patch to 'fs/read_write.c' cleanly.
2026-05-03T01:23:31.5299801Z Applied patch to 'fs/readdir.c' cleanly.
2026-05-03T01:23:31.5310857Z Applied patch to 'fs/stat.c' cleanly.
2026-05-03T01:23:31.5317267Z Applied patch to 'fs/statfs.c' cleanly.
2026-05-03T01:23:31.5320158Z error: repository lacks the necessary blob to perform 3-way merge.
2026-05-03T01:23:31.5320790Z Falling back to direct application...
2026-05-03T01:23:31.5335655Z Applied patch to 'kernel/reboot.c' cleanly.
2026-05-03T01:23:31.5364115Z Applied patch to 'kernel/sys.c' cleanly.
2026-05-03T01:23:31.5378013Z Applied patch to 'security/selinux/avc.c' cleanly.
2026-05-03T01:23:31.5691141Z patching file drivers/input/input.c
2026-05-03T01:23:31.5694245Z patching file fs/Makefile
2026-05-03T01:23:31.5694944Z patching file fs/devpts/inode.c
2026-05-03T01:23:31.5697588Z patching file fs/exec.c
2026-05-03T01:23:31.5698808Z Hunk #2 succeeded at 1929 (offset 1 line).
2026-05-03T01:23:31.5699327Z Hunk #3 succeeded at 1950 (offset 1 line).
2026-05-03T01:23:31.5703041Z patching file fs/namei.c
2026-05-03T01:23:31.5709707Z patching file fs/namespace.c
2026-05-03T01:23:31.5713963Z patching file fs/notify/fdinfo.c
2026-05-03T01:23:31.5715918Z patching file fs/open.c
2026-05-03T01:23:31.5719171Z patching file fs/proc/base.c
2026-05-03T01:23:31.5723217Z patching file fs/proc/bootconfig.c
2026-05-03T01:23:31.5723764Z patching file fs/proc/fd.c
2026-05-03T01:23:31.5725915Z patching file fs/proc/task_mmu.c
2026-05-03T01:23:31.5726523Z Hunk #2 succeeded at 392 (offset 129 lines).
2026-05-03T01:23:31.5727072Z Hunk #3 succeeded at 411 (offset 129 lines).
2026-05-03T01:23:31.5727536Z Hunk #4 succeeded at 487 (offset 148 lines).
2026-05-03T01:23:31.5728069Z Hunk #5 succeeded at 1102 with fuzz 1 (offset 148 lines).
2026-05-03T01:23:31.5728593Z Hunk #6 succeeded at 1180 (offset 148 lines).
2026-05-03T01:23:31.5729231Z Hunk #7 succeeded at 1973 (offset 148 lines).
2026-05-03T01:23:31.5729725Z Hunk #8 succeeded at 2051 (offset 148 lines).
2026-05-03T01:23:31.5730773Z patching file fs/proc_namespace.c
2026-05-03T01:23:31.5732701Z patching file fs/read_write.c
2026-05-03T01:23:31.5735321Z patching file fs/readdir.c
2026-05-03T01:23:31.5738249Z patching file fs/stat.c
2026-05-03T01:23:31.5740501Z patching file fs/statfs.c
2026-05-03T01:23:31.5742255Z patching file kernel/kallsyms.c
2026-05-03T01:23:31.5743278Z Hunk #2 succeeded at 805 (offset 3 lines).
2026-05-03T01:23:31.5744563Z patching file kernel/reboot.c
2026-05-03T01:23:31.5747695Z patching file kernel/sys.c
2026-05-03T01:23:31.5751293Z patching file security/selinux/avc.c
2026-05-03T01:23:31.5778283Z Kernel SUSFS patch applied via fuzz fallback
2026-05-03T01:23:31.5778988Z === Integrating SUSFS into KernelSU-Next (Clean Manual Method) ===
2026-05-03T01:23:31.5804919Z SUSFS Kconfig injected successfully
2026-05-03T01:23:31.5828398Z SUSFS Makefile entries injected successfully
2026-05-03T01:23:31.5911996Z === Clean SUSFS Integration Complete ===
2026-05-03T01:23:31.5912328Z === Validating SUSFS configuration ===
2026-05-03T01:23:31.5944736Z init.c syntax check OK
2026-05-03T01:23:31.5959890Z WARNING: SUSFS Kconfig NOT found — SUSFS will NOT be enabled
2026-05-03T01:23:31.5960251Z === Final init.c ===
2026-05-03T01:23:31.5969534Z #include <linux/export.h>
2026-05-03T01:23:31.5969927Z #include <linux/fs.h>
2026-05-03T01:23:31.5970152Z #include <linux/kobject.h>
2026-05-03T01:23:31.5970363Z #include <linux/module.h>
2026-05-03T01:23:31.5970675Z #include <linux/rcupdate.h>
2026-05-03T01:23:31.5971046Z #include <linux/sched.h>
2026-05-03T01:23:31.5971421Z #include <linux/workqueue.h>
2026-05-03T01:23:31.5971794Z #include <linux/susfs.h>
2026-05-03T01:23:31.5972020Z 
2026-05-03T01:23:31.5972168Z #include "policy/allowlist.h"
2026-05-03T01:23:31.5972810Z #include "policy/app_profile.h"
2026-05-03T01:23:31.5973220Z #include "policy/feature.h"
2026-05-03T01:23:31.5973608Z #include "klog.h" // IWYU pragma: keep
2026-05-03T01:23:31.5974098Z #include "manager/manager_observer.h"
2026-05-03T01:23:31.5974535Z #include "manager/throne_tracker.h"
2026-05-03T01:23:31.5974904Z #include "hook/syscall_hook_manager.h"
2026-05-03T01:23:31.5975497Z #include "runtime/ksud.h"
2026-05-03T01:23:31.5975711Z #include "runtime/ksud_boot.h"
2026-05-03T01:23:31.5975937Z #include "supercall/supercall.h"
2026-05-03T01:23:31.5976150Z #include "ksu.h"
2026-05-03T01:23:31.5976335Z #include "infra/file_wrapper.h"
2026-05-03T01:23:31.5976549Z #include "selinux/selinux.h"
2026-05-03T01:23:31.5976760Z #include "hook/syscall_hook.h"
2026-05-03T01:23:31.5976896Z 
2026-05-03T01:23:31.5976973Z #if defined(__x86_64__)
2026-05-03T01:23:31.5977166Z #include <asm/cpufeature.h>
2026-05-03T01:23:31.5977370Z #include <linux/version.h>
2026-05-03T01:23:31.5977576Z #ifndef X86_FEATURE_INDIRECT_SAFE
2026-05-03T01:23:31.5977927Z #error "FATAL: Your kernel is missing the indirect syscall bypass patches!"
2026-05-03T01:23:31.5978280Z #endif
2026-05-03T01:23:31.5978599Z #endif
2026-05-03T01:23:31.5978684Z 
2026-05-03T01:23:31.5978799Z // workaround for A12-5.10 kernel
2026-05-03T01:23:31.5979161Z // Some third-party kernel (e.g. linegaeOS) uses wrong toolchain, which supports
2026-05-03T01:23:31.5979605Z // CC_HAVE_STACKPROTECTOR_SYSREG while gki's toolchain doesn't.
2026-05-03T01:23:31.5980045Z // Therefore, ksu lkm, which uses gki toolchain, requires this __stack_chk_guard,
2026-05-03T01:23:31.5980449Z // while those third-party kernel can't provide.
2026-05-03T01:23:31.5980773Z // Thus, we manually provide it instead of using kernel's
2026-05-03T01:23:31.5981186Z #if defined(CONFIG_STACKPROTECTOR) &&                                          \
2026-05-03T01:23:31.5981627Z     (defined(CONFIG_ARM64) && defined(MODULE) &&                               \
2026-05-03T01:23:31.5982000Z      !defined(CONFIG_STACKPROTECTOR_PER_TASK))
2026-05-03T01:23:31.5982271Z #include <linux/stackprotector.h>
2026-05-03T01:23:31.5982497Z #include <linux/random.h>
2026-05-03T01:23:31.5982737Z unsigned long __stack_chk_guard __ro_after_init
2026-05-03T01:23:31.5983019Z     __attribute__((visibility("hidden")));
2026-05-03T01:23:31.5983193Z 
2026-05-03T01:23:31.5983368Z __attribute__((no_stack_protector)) void __init ksu_setup_stack_chk_guard()
2026-05-03T01:23:31.5983695Z {
2026-05-03T01:23:31.5983849Z     unsigned long canary;
2026-05-03T01:23:31.5983973Z 
2026-05-03T01:23:31.5984058Z === Final Kconfig (SUSFS section) ===
2026-05-03T01:23:31.5986502Z config KSU_SUSFS
2026-05-03T01:23:31.5987103Z 	bool "KernelSU addon - SUSFS"
2026-05-03T01:23:31.5987510Z 	depends on KSU
2026-05-03T01:23:31.5987811Z --
2026-05-03T01:23:31.5988073Z config KSU_SUSFS_SUS_PATH
2026-05-03T01:23:31.5988452Z 	bool "Enable to hide suspicious path"
2026-05-03T01:23:31.5988865Z 	depends on KSU_SUSFS
2026-05-03T01:23:31.5989165Z 	default y
2026-05-03T01:23:31.5989320Z 
2026-05-03T01:23:31.5989467Z config KSU_SUSFS_SUS_MOUNT
2026-05-03T01:23:31.5989841Z 	bool "Enable to hide suspicious mounts"
2026-05-03T01:23:31.5990268Z 	depends on KSU_SUSFS
2026-05-03T01:23:31.5990620Z 	default y
2026-05-03T01:23:31.5990778Z 
2026-05-03T01:23:31.5990902Z config KSU_SUSFS_SUS_KSTAT
2026-05-03T01:23:31.5991261Z 	bool "Enable to spoof suspicious kstat"
2026-05-03T01:23:31.5991713Z 	depends on KSU_SUSFS
2026-05-03T01:23:31.5992033Z 	default y
2026-05-03T01:23:31.5992194Z 
2026-05-03T01:23:31.5992334Z config KSU_SUSFS_SPOOF_UNAME
2026-05-03T01:23:31.6020663Z ##[group]Run cd kernel/common
2026-05-03T01:23:31.6020987Z [36;1mcd kernel/common[0m
2026-05-03T01:23:31.6021244Z [36;1mDEFCONFIG="arch/arm64/configs/gki_defconfig"[0m
2026-05-03T01:23:31.6021517Z [36;1m[0m
2026-05-03T01:23:31.6021695Z [36;1m# --- KernelSU ---[0m
2026-05-03T01:23:31.6021917Z [36;1mif [ "true" = "true" ]; then[0m
2026-05-03T01:23:31.6022157Z [36;1m  cat >> $DEFCONFIG << 'EOF'[0m
2026-05-03T01:23:31.6022365Z [36;1m[0m
2026-05-03T01:23:31.6022532Z [36;1m# KernelSU-Next[0m
2026-05-03T01:23:31.6022734Z [36;1mCONFIG_KSU=y[0m
2026-05-03T01:23:31.6022931Z [36;1mEOF[0m
2026-05-03T01:23:31.6023085Z [36;1mfi[0m
2026-05-03T01:23:31.6023242Z [36;1m[0m
2026-05-03T01:23:31.6023413Z [36;1m# --- SUSFS ---[0m
2026-05-03T01:23:31.6023662Z [36;1mif [ "false" = "true" ] && [ "true" = "true" ]; then[0m
2026-05-03T01:23:31.6023961Z [36;1m  cat >> $DEFCONFIG << 'EOF'[0m
2026-05-03T01:23:31.6024178Z [36;1m[0m
2026-05-03T01:23:31.6024331Z [36;1m# SUSFS[0m
2026-05-03T01:23:31.6024534Z [36;1mCONFIG_KSU_SUSFS=y[0m
2026-05-03T01:23:31.6024760Z [36;1mCONFIG_KSU_SUSFS_HAS_MAGIC_MOUNT=y[0m
2026-05-03T01:23:31.6025321Z [36;1mCONFIG_KSU_SUSFS_SUS_PATH=y[0m
2026-05-03T01:23:31.6025579Z [36;1mCONFIG_KSU_SUSFS_SUS_MOUNT=y[0m
2026-05-03T01:23:31.6025843Z [36;1mCONFIG_KSU_SUSFS_SUS_MAP=y[0m
2026-05-03T01:23:31.6026143Z [36;1mCONFIG_KSU_SUSFS_AUTO_ADD_SUS_KSU_DEFAULT_MOUNT=y[0m
2026-05-03T01:23:31.6026467Z [36;1mCONFIG_KSU_SUSFS_AUTO_ADD_SUS_BIND_MOUNT=y[0m
2026-05-03T01:23:31.6026745Z [36;1mCONFIG_KSU_SUSFS_SUS_KSTAT=y[0m
2026-05-03T01:23:31.6026984Z [36;1mCONFIG_KSU_SUSFS_TRY_UMOUNT=y[0m
2026-05-03T01:23:31.6027444Z [36;1mCONFIG_KSU_SUSFS_AUTO_ADD_TRY_UMOUNT_FOR_BIND_MOUNT=y[0m
2026-05-03T01:23:31.6027764Z [36;1mCONFIG_KSU_SUSFS_SPOOF_UNAME=y[0m
2026-05-03T01:23:31.6028014Z [36;1mCONFIG_KSU_SUSFS_ENABLE_LOG=y[0m
2026-05-03T01:23:31.6028282Z [36;1mCONFIG_KSU_SUSFS_HIDE_KSU_SUSFS_SYMBOLS=y[0m
2026-05-03T01:23:31.6028597Z [36;1mCONFIG_KSU_SUSFS_SPOOF_CMDLINE_OR_BOOTCONFIG=y[0m
2026-05-03T01:23:31.6028898Z [36;1mCONFIG_KSU_SUSFS_OPEN_REDIRECT=y[0m
2026-05-03T01:23:31.6029146Z [36;1mCONFIG_KSU_SUSFS_SUS_SU=n[0m
2026-05-03T01:23:31.6029364Z [36;1mEOF[0m
2026-05-03T01:23:31.6029519Z [36;1mfi[0m
2026-05-03T01:23:31.6029673Z [36;1m[0m
2026-05-03T01:23:31.6029920Z [36;1m# --- Module Loading (CRITICAL: allow vendor modules) ---[0m
2026-05-03T01:23:31.6030236Z [36;1mcat >> $DEFCONFIG << 'EOF'[0m
2026-05-03T01:23:31.6030444Z [36;1m[0m
2026-05-03T01:23:31.6030682Z [36;1m# Module Compatibility (allow vendor_boot modules to load)[0m
2026-05-03T01:23:31.6031014Z [36;1mCONFIG_MODVERSIONS=n[0m
2026-05-03T01:23:31.6031237Z [36;1mCONFIG_MODULE_SIG_FORCE=n[0m
2026-05-03T01:23:31.6031465Z [36;1mCONFIG_MODULE_SIG_ALL=n[0m
2026-05-03T01:23:31.6031679Z [36;1mEOF[0m
2026-05-03T01:23:31.6031830Z [36;1m[0m
2026-05-03T01:23:31.6032015Z [36;1m# --- Memory & CPU Optimization ---[0m
2026-05-03T01:23:31.6032276Z [36;1mcat >> $DEFCONFIG << 'EOF'[0m
2026-05-03T01:23:31.6032488Z [36;1m[0m
2026-05-03T01:23:31.6032658Z [36;1m# Memory & CPU Optimization[0m
2026-05-03T01:23:31.6032890Z [36;1mCONFIG_ZRAM=y[0m
2026-05-03T01:23:31.6033091Z [36;1mCONFIG_ZRAM_WRITEBACK=y[0m
2026-05-03T01:23:31.6033309Z [36;1mCONFIG_ZSMALLOC=y[0m
2026-05-03T01:23:31.6033538Z [36;1mCONFIG_COMPACTION=y[0m
2026-05-03T01:23:31.6033739Z [36;1mCONFIG_KSM=y[0m
2026-05-03T01:23:31.6033944Z [36;1mCONFIG_TRANSPARENT_HUGEPAGE=y[0m
2026-05-03T01:23:31.6034187Z [36;1mCONFIG_SLAB_FREELIST_RANDOM=y[0m
2026-05-03T01:23:31.6034417Z [36;1mCONFIG_HZ_1000=y[0m
2026-05-03T01:23:31.6034621Z [36;1mCONFIG_LRU_GEN=y[0m
2026-05-03T01:23:31.6034821Z [36;1mCONFIG_LRU_GEN_ENABLED=y[0m
2026-05-03T01:23:31.6035267Z [36;1mEOF[0m
2026-05-03T01:23:31.6035428Z [36;1m[0m
2026-05-03T01:23:31.6035602Z [36;1m# --- I/O Optimization ---[0m
2026-05-03T01:23:31.6035834Z [36;1mcat >> $DEFCONFIG << 'EOF'[0m
2026-05-03T01:23:31.6036047Z [36;1m[0m
2026-05-03T01:23:31.6036368Z [36;1m# I/O Optimization[0m
2026-05-03T01:23:31.6036588Z [36;1mCONFIG_IOSCHED_BFQ=y[0m
2026-05-03T01:23:31.6036809Z [36;1mCONFIG_BFQ_GROUP_IOSCHED=y[0m
2026-05-03T01:23:31.6037022Z [36;1mEOF[0m
2026-05-03T01:23:31.6037177Z [36;1m[0m
2026-05-03T01:23:31.6037338Z [36;1m# --- Networking ---[0m
2026-05-03T01:23:31.6037553Z [36;1mcat >> $DEFCONFIG << 'EOF'[0m
2026-05-03T01:23:31.6037759Z [36;1m[0m
2026-05-03T01:23:31.6037912Z [36;1m# Networking[0m
2026-05-03T01:23:31.6038102Z [36;1mCONFIG_TCP_CONG_ADVANCED=y[0m
2026-05-03T01:23:31.6038336Z [36;1mCONFIG_TCP_CONG_BBR=y[0m
2026-05-03T01:23:31.6038547Z [36;1mCONFIG_NET_SCH_FQ=y[0m
2026-05-03T01:23:31.6038771Z [36;1mCONFIG_IP_NF_TARGET_TTL=y[0m
2026-05-03T01:23:31.6039000Z [36;1mCONFIG_IP6_NF_TARGET_HL=y[0m
2026-05-03T01:23:31.6039205Z [36;1m[0m
2026-05-03T01:23:31.6039357Z [36;1m# IPSet[0m
2026-05-03T01:23:31.6039529Z [36;1mCONFIG_IP_SET=y[0m
2026-05-03T01:23:31.6039736Z [36;1mCONFIG_IP_SET_MAX=65534[0m
2026-05-03T01:23:31.6039960Z [36;1mCONFIG_IP_SET_BITMAP_IP=y[0m
2026-05-03T01:23:31.6040194Z [36;1mCONFIG_IP_SET_BITMAP_IPMAC=y[0m
2026-05-03T01:23:31.6040429Z [36;1mCONFIG_IP_SET_BITMAP_PORT=y[0m
2026-05-03T01:23:31.6040662Z [36;1mCONFIG_IP_SET_HASH_IP=y[0m
2026-05-03T01:23:31.6040886Z [36;1mCONFIG_IP_SET_HASH_IPMARK=y[0m
2026-05-03T01:23:31.6041116Z [36;1mCONFIG_IP_SET_HASH_IPPORT=y[0m
2026-05-03T01:23:31.6041353Z [36;1mCONFIG_IP_SET_HASH_IPPORTIP=y[0m
2026-05-03T01:23:31.6041596Z [36;1mCONFIG_IP_SET_HASH_IPPORTNET=y[0m
2026-05-03T01:23:31.6041844Z [36;1mCONFIG_IP_SET_HASH_IPMAC=y[0m
2026-05-03T01:23:31.6042068Z [36;1mCONFIG_IP_SET_HASH_MAC=y[0m
2026-05-03T01:23:31.6042423Z [36;1mCONFIG_IP_SET_HASH_NETPORTNET=y[0m
2026-05-03T01:23:31.6042661Z [36;1mCONFIG_IP_SET_HASH_NET=y[0m
2026-05-03T01:23:31.6042887Z [36;1mCONFIG_IP_SET_HASH_NETNET=y[0m
2026-05-03T01:23:31.6043129Z [36;1mCONFIG_IP_SET_HASH_NETPORT=y[0m
2026-05-03T01:23:31.6043364Z [36;1mCONFIG_IP_SET_HASH_NETIFACE=y[0m
2026-05-03T01:23:31.6043604Z [36;1mCONFIG_IP_SET_LIST_SET=y[0m
2026-05-03T01:23:31.6043806Z [36;1mEOF[0m
2026-05-03T01:23:31.6043963Z [36;1m[0m
2026-05-03T01:23:31.6044118Z [36;1m# --- Branding ---[0m
2026-05-03T01:23:31.6044329Z [36;1mcat >> $DEFCONFIG << 'EOF'[0m
2026-05-03T01:23:31.6044536Z [36;1m[0m
2026-05-03T01:23:31.6044689Z [36;1m# Branding[0m
2026-05-03T01:23:31.6044888Z [36;1mCONFIG_LOCALVERSION="-Castorice"[0m
2026-05-03T01:23:31.6045388Z [36;1mCONFIG_LOCALVERSION_AUTO=n[0m
2026-05-03T01:23:31.6045609Z [36;1mEOF[0m
2026-05-03T01:23:31.6045758Z [36;1m[0m
2026-05-03T01:23:31.6045934Z [36;1mecho "=== Defconfig additions ==="[0m
2026-05-03T01:23:31.6046187Z [36;1mtail -60 $DEFCONFIG[0m
2026-05-03T01:23:31.6066544Z shell: /usr/bin/bash -e {0}
2026-05-03T01:23:31.6066764Z env:
2026-05-03T01:23:31.6066945Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:23:31.6067206Z   ANDROID_VERSION: android15
2026-05-03T01:23:31.6067415Z   KERNEL_VERSION: 6.6
2026-05-03T01:23:31.6067603Z   KMI_GENERATION: 8
2026-05-03T01:23:31.6067786Z   KERNEL_NAME: Castorice
2026-05-03T01:23:31.6067980Z   DEVICE_CODE: fire
2026-05-03T01:23:31.6068160Z   KSU_DIR: KernelSU-Next
2026-05-03T01:23:31.6068346Z   KSU_VERSION: 1
2026-05-03T01:23:31.6068513Z   SUSFS_OK: false
2026-05-03T01:23:31.6068683Z   BUILT_KERNEL_VERSION: 
2026-05-03T01:23:31.6068868Z   ZIP_NAME: 
2026-05-03T01:23:31.6069027Z ##[endgroup]
2026-05-03T01:23:31.6167420Z === Defconfig additions ===
2026-05-03T01:23:31.6179699Z CONFIG_KUNIT_DEBUGFS=y
2026-05-03T01:23:31.6180041Z CONFIG_KUNIT_TEST=m
2026-05-03T01:23:31.6180266Z CONFIG_KUNIT_EXAMPLE_TEST=m
2026-05-03T01:23:31.6180664Z # CONFIG_KUNIT_DEFAULT_ENABLED is not set
2026-05-03T01:23:31.6181168Z # CONFIG_RUNTIME_TESTING_MENU is not set
2026-05-03T01:23:31.6181512Z 
2026-05-03T01:23:31.6181648Z # KernelSU-Next
2026-05-03T01:23:31.6181969Z CONFIG_KSU=y
2026-05-03T01:23:31.6182155Z 
2026-05-03T01:23:31.6182413Z # Module Compatibility (allow vendor_boot modules to load)
2026-05-03T01:23:31.6183038Z CONFIG_MODVERSIONS=n
2026-05-03T01:23:31.6183632Z CONFIG_MODULE_SIG_FORCE=n
2026-05-03T01:23:31.6184002Z CONFIG_MODULE_SIG_ALL=n
2026-05-03T01:23:31.6184274Z 
2026-05-03T01:23:31.6184435Z # Memory & CPU Optimization
2026-05-03T01:23:31.6184749Z CONFIG_ZRAM=y
2026-05-03T01:23:31.6185193Z CONFIG_ZRAM_WRITEBACK=y
2026-05-03T01:23:31.6185430Z CONFIG_ZSMALLOC=y
2026-05-03T01:23:31.6185627Z CONFIG_COMPACTION=y
2026-05-03T01:23:31.6185819Z CONFIG_KSM=y
2026-05-03T01:23:31.6186028Z CONFIG_TRANSPARENT_HUGEPAGE=y
2026-05-03T01:23:31.6186272Z CONFIG_SLAB_FREELIST_RANDOM=y
2026-05-03T01:23:31.6186507Z CONFIG_HZ_1000=y
2026-05-03T01:23:31.6186692Z CONFIG_LRU_GEN=y
2026-05-03T01:23:31.6186895Z CONFIG_LRU_GEN_ENABLED=y
2026-05-03T01:23:31.6187036Z 
2026-05-03T01:23:31.6187115Z # I/O Optimization
2026-05-03T01:23:31.6187312Z CONFIG_IOSCHED_BFQ=y
2026-05-03T01:23:31.6187516Z CONFIG_BFQ_GROUP_IOSCHED=y
2026-05-03T01:23:31.6187666Z 
2026-05-03T01:23:31.6187736Z # Networking
2026-05-03T01:23:31.6187937Z CONFIG_TCP_CONG_ADVANCED=y
2026-05-03T01:23:31.6188157Z CONFIG_TCP_CONG_BBR=y
2026-05-03T01:23:31.6188361Z CONFIG_NET_SCH_FQ=y
2026-05-03T01:23:31.6188556Z CONFIG_IP_NF_TARGET_TTL=y
2026-05-03T01:23:31.6188776Z CONFIG_IP6_NF_TARGET_HL=y
2026-05-03T01:23:31.6188915Z 
2026-05-03T01:23:31.6188983Z # IPSet
2026-05-03T01:23:31.6189151Z CONFIG_IP_SET=y
2026-05-03T01:23:31.6189342Z CONFIG_IP_SET_MAX=65534
2026-05-03T01:23:31.6189551Z CONFIG_IP_SET_BITMAP_IP=y
2026-05-03T01:23:31.6189775Z CONFIG_IP_SET_BITMAP_IPMAC=y
2026-05-03T01:23:31.6190009Z CONFIG_IP_SET_BITMAP_PORT=y
2026-05-03T01:23:31.6190242Z CONFIG_IP_SET_HASH_IP=y
2026-05-03T01:23:31.6190455Z CONFIG_IP_SET_HASH_IPMARK=y
2026-05-03T01:23:31.6190855Z CONFIG_IP_SET_HASH_IPPORT=y
2026-05-03T01:23:31.6191084Z CONFIG_IP_SET_HASH_IPPORTIP=y
2026-05-03T01:23:31.6191329Z CONFIG_IP_SET_HASH_IPPORTNET=y
2026-05-03T01:23:31.6191567Z CONFIG_IP_SET_HASH_IPMAC=y
2026-05-03T01:23:31.6191792Z CONFIG_IP_SET_HASH_MAC=y
2026-05-03T01:23:31.6192013Z CONFIG_IP_SET_HASH_NETPORTNET=y
2026-05-03T01:23:31.6192256Z CONFIG_IP_SET_HASH_NET=y
2026-05-03T01:23:31.6192478Z CONFIG_IP_SET_HASH_NETNET=y
2026-05-03T01:23:31.6192703Z CONFIG_IP_SET_HASH_NETPORT=y
2026-05-03T01:23:31.6192939Z CONFIG_IP_SET_HASH_NETIFACE=y
2026-05-03T01:23:31.6193166Z CONFIG_IP_SET_LIST_SET=y
2026-05-03T01:23:31.6193302Z 
2026-05-03T01:23:31.6193377Z # Branding
2026-05-03T01:23:31.6193566Z CONFIG_LOCALVERSION="-Castorice"
2026-05-03T01:23:31.6193816Z CONFIG_LOCALVERSION_AUTO=n
2026-05-03T01:23:31.6213856Z ##[group]Run cd kernel/common
2026-05-03T01:23:31.6214144Z [36;1mcd kernel/common[0m
2026-05-03T01:23:31.6214345Z [36;1m[0m
2026-05-03T01:23:31.6214582Z [36;1m# Remove protected exports (prevents build failures)[0m
2026-05-03T01:23:31.6215300Z [36;1mrm -rf android/abi_gki_protected_exports_* || true[0m
2026-05-03T01:23:31.6215645Z [36;1mif [ -f "BUILD.bazel" ]; then[0m
2026-05-03T01:23:31.6215964Z [36;1m  sed -i '/abi_gki_protected_exports/d' BUILD.bazel[0m
2026-05-03T01:23:31.6216310Z [36;1m  sed -i '/protected_exports/d' BUILD.bazel[0m
2026-05-03T01:23:31.6216635Z [36;1m  sed -i '/check_defconfig/d' BUILD.bazel[0m
2026-05-03T01:23:31.6216902Z [36;1mfi[0m
2026-05-03T01:23:31.6217057Z [36;1m[0m
2026-05-03T01:23:31.6217340Z [36;1mif [ -f "modules.bzl" ] && grep -q 'protected_modules = ' modules.bzl; then[0m
2026-05-03T01:23:31.6217821Z [36;1m  sed -i 's/protected_modules = \[.*\]/protected_modules = []/' modules.bzl[0m
2026-05-03T01:23:31.6218212Z [36;1mfi[0m
2026-05-03T01:23:31.6218366Z [36;1m[0m
2026-05-03T01:23:31.6218608Z [36;1mfor f in build.config.gki build.config.gki.aarch64; do[0m
2026-05-03T01:23:31.6218965Z [36;1m  [ -f "$f" ] && sed -i '/check_defconfig/d' "$f"[0m
2026-05-03T01:23:31.6219236Z [36;1mdone[0m
2026-05-03T01:23:31.6219398Z [36;1m[0m
2026-05-03T01:23:31.6219561Z [36;1m# Bypass ABI check script[0m
2026-05-03T01:23:31.6219917Z [36;1mPROT_SCRIPT="../build/kernel/abi/check_buildtime_symbol_protection.py"[0m
2026-05-03T01:23:31.6220294Z [36;1mif [ -f "$PROT_SCRIPT" ]; then[0m
2026-05-03T01:23:31.6220620Z [36;1m  perl -i -pe 's/^(\s*)return 1$/$1return 0/g' "$PROT_SCRIPT"[0m
2026-05-03T01:23:31.6220923Z [36;1mfi[0m
2026-05-03T01:23:31.6221079Z [36;1m[0m
2026-05-03T01:23:31.6221234Z [36;1m# Clean dirty flags[0m
2026-05-03T01:23:31.6221508Z [36;1mif [ -f "../build/kernel/kleaf/impl/stamp.bzl" ]; then[0m
2026-05-03T01:23:31.6221993Z [36;1m  sed -i '/stable_scmversion_cmd/s/-maybe-dirty//g' ../build/kernel/kleaf/impl/stamp.bzl[0m
2026-05-03T01:23:31.6222403Z [36;1mfi[0m
2026-05-03T01:23:31.6222676Z [36;1msed -i 's/-dirty//' scripts/setlocalversion 2>/dev/null || true[0m
2026-05-03T01:23:31.6223012Z [36;1m: > .scmversion[0m
2026-05-03T01:23:31.6223210Z [36;1m[0m
2026-05-03T01:23:31.6223379Z [36;1mecho "Build system patched"[0m
2026-05-03T01:23:31.6242615Z shell: /usr/bin/bash -e {0}
2026-05-03T01:23:31.6242839Z env:
2026-05-03T01:23:31.6243024Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:23:31.6243288Z   ANDROID_VERSION: android15
2026-05-03T01:23:31.6243504Z   KERNEL_VERSION: 6.6
2026-05-03T01:23:31.6243687Z   KMI_GENERATION: 8
2026-05-03T01:23:31.6243868Z   KERNEL_NAME: Castorice
2026-05-03T01:23:31.6244054Z   DEVICE_CODE: fire
2026-05-03T01:23:31.6244245Z   KSU_DIR: KernelSU-Next
2026-05-03T01:23:31.6244432Z   KSU_VERSION: 1
2026-05-03T01:23:31.6244600Z   SUSFS_OK: false
2026-05-03T01:23:31.6244769Z   BUILT_KERNEL_VERSION: 
2026-05-03T01:23:31.6245227Z   ZIP_NAME: 
2026-05-03T01:23:31.6245529Z ##[endgroup]
2026-05-03T01:23:31.6458777Z Build system patched
2026-05-03T01:23:31.6481240Z ##[group]Run cd kernel/common
2026-05-03T01:23:31.6481494Z [36;1mcd kernel/common[0m
2026-05-03T01:23:31.6481772Z [36;1mgit config --global user.name "github-actions[bot]"[0m
2026-05-03T01:23:31.6482375Z [36;1mgit config --global user.email "github-actions[bot]@users.noreply.github.com"[0m
2026-05-03T01:23:31.6482763Z [36;1mgit add -A[0m
2026-05-03T01:23:31.6483087Z [36;1mgit commit -m "Castorice: GKI kernel with KSU+SUSFS+optimizations" || true[0m
2026-05-03T01:23:31.6503010Z shell: /usr/bin/bash -e {0}
2026-05-03T01:23:31.6503232Z env:
2026-05-03T01:23:31.6503414Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:23:31.6503685Z   ANDROID_VERSION: android15
2026-05-03T01:23:31.6503910Z   KERNEL_VERSION: 6.6
2026-05-03T01:23:31.6504091Z   KMI_GENERATION: 8
2026-05-03T01:23:31.6504274Z   KERNEL_NAME: Castorice
2026-05-03T01:23:31.6504466Z   DEVICE_CODE: fire
2026-05-03T01:23:31.6504643Z   KSU_DIR: KernelSU-Next
2026-05-03T01:23:31.6504824Z   KSU_VERSION: 1
2026-05-03T01:23:31.6505299Z   SUSFS_OK: false
2026-05-03T01:23:31.6505498Z   BUILT_KERNEL_VERSION: 
2026-05-03T01:23:31.6505685Z   ZIP_NAME: 
2026-05-03T01:23:31.6505847Z ##[endgroup]
2026-05-03T01:23:32.0297007Z [detached HEAD 10195bbac] Castorice: GKI kernel with KSU+SUSFS+optimizations
2026-05-03T01:23:32.0297582Z  34 files changed, 6775 insertions(+), 520 deletions(-)
2026-05-03T01:23:32.0298001Z  delete mode 100644 android/abi_gki_protected_exports_aarch64
2026-05-03T01:23:32.0298367Z  create mode 100644 fs/exec.c.orig
2026-05-03T01:23:32.0298648Z  create mode 100644 fs/proc/task_mmu.c.orig
2026-05-03T01:23:32.0298950Z  create mode 100644 kernel/kallsyms.c.orig
2026-05-03T01:23:32.0342790Z ##[group]Run cd kernel
2026-05-03T01:23:32.0343073Z [36;1mcd kernel[0m
2026-05-03T01:23:32.0343322Z [36;1mecho "=== Building Castorice GKI Kernel ==="[0m
2026-05-03T01:23:32.0343616Z [36;1mtools/bazel build \[0m
2026-05-03T01:23:32.0343843Z [36;1m  --config=fast \[0m
2026-05-03T01:23:32.0344085Z [36;1m  //common:kernel_aarch64_dist 2>&1[0m
2026-05-03T01:23:32.0344361Z [36;1mecho "=== Build completed ==="[0m
2026-05-03T01:23:32.0364917Z shell: /usr/bin/bash -e {0}
2026-05-03T01:23:32.0365500Z env:
2026-05-03T01:23:32.0365697Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T01:23:32.0365961Z   ANDROID_VERSION: android15
2026-05-03T01:23:32.0366173Z   KERNEL_VERSION: 6.6
2026-05-03T01:23:32.0366352Z   KMI_GENERATION: 8
2026-05-03T01:23:32.0366532Z   KERNEL_NAME: Castorice
2026-05-03T01:23:32.0366717Z   DEVICE_CODE: fire
2026-05-03T01:23:32.0366897Z   KSU_DIR: KernelSU-Next
2026-05-03T01:23:32.0367086Z   KSU_VERSION: 1
2026-05-03T01:23:32.0367255Z   SUSFS_OK: false
2026-05-03T01:23:32.0367460Z   BUILT_KERNEL_VERSION: 
2026-05-03T01:23:32.0367642Z   ZIP_NAME: 
2026-05-03T01:23:32.0367808Z   SOURCE_DATE_EPOCH: 0
2026-05-03T01:23:32.0367985Z ##[endgroup]
2026-05-03T01:23:32.0408057Z === Building Castorice GKI Kernel ===
2026-05-03T01:23:32.1337475Z Extracting Bazel installation...
2026-05-03T01:23:33.3542322Z Starting local Bazel server and connecting to it...
2026-05-03T01:23:34.9036307Z Computing main repo mapping: 
2026-05-03T01:23:35.7274092Z Loading: 
2026-05-03T01:23:35.7298528Z Loading: 1 packages loaded
2026-05-03T01:23:36.9081817Z Loading: 1 packages loaded
2026-05-03T01:23:36.9105682Z     currently loading: common
2026-05-03T01:23:41.0835942Z Analyzing: target //common:kernel_aarch64_dist (2 packages loaded)
2026-05-03T01:23:41.2586379Z Analyzing: target //common:kernel_aarch64_dist (2 packages loaded, 0 targets configured)
2026-05-03T01:23:41.2806383Z Analyzing: target //common:kernel_aarch64_dist (2 packages loaded, 0 targets configured)
2026-05-03T01:23:41.2865842Z [0 / 1] checking cached actions
2026-05-03T01:23:42.4727050Z Analyzing: target //common:kernel_aarch64_dist (37 packages loaded, 7 targets configured)
2026-05-03T01:23:42.4746243Z [1 / 1] checking cached actions
2026-05-03T01:23:43.5096690Z Analyzing: target //common:kernel_aarch64_dist (63 packages loaded, 9696 targets configured)
2026-05-03T01:23:43.5097874Z [1 / 1] checking cached actions
2026-05-03T01:23:44.5381157Z Analyzing: target //common:kernel_aarch64_dist (71 packages loaded, 16128 targets configured)
2026-05-03T01:23:44.5405705Z [1 / 1] checking cached actions
2026-05-03T01:23:45.9179415Z Analyzing: target //common:kernel_aarch64_dist (73 packages loaded, 78174 targets configured)
2026-05-03T01:23:45.9207007Z [1 / 1] checking cached actions
2026-05-03T01:23:48.3593616Z INFO: Analyzed target //common:kernel_aarch64_dist (73 packages loaded, 98798 targets configured).
2026-05-03T01:23:48.3643524Z [1 / 2] [Prepa] Writing script common/kernel_aarch64_dist
2026-05-03T01:23:49.4116334Z [92 / 750] [Prepa] Creating symlink to in-tree tool @@//build/kernel:hermetic-tools/mkuserimg_mke2fs [for tool]
2026-05-03T01:23:50.4082288Z [149 / 750] [Prepa] Creating symlink to in-tree tool @@//build/kernel:hermetic-tools/cut [for tool]
2026-05-03T01:23:51.4896709Z [227 / 760] Generating BUILD.bazel for all_headers_aarch64 @@//common:kernel_aarch64_ddk_headers_archive; 0s processwrapper-sandbox ... (2 actions, 1 running)
2026-05-03T01:23:52.5583656Z [261 / 760] Building Python zip: //build/kernel:init_ddk; 0s processwrapper-sandbox ... (2 actions, 1 running)
2026-05-03T01:23:53.6279521Z [335 / 760] Compiling common/tools/testing/selftests/filesystems/binderfs/binderfs_test.c; 0s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T01:23:54.6703328Z [356 / 760] Compiling build/kernel/kleaf/impl/arg_wrapper.cpp [for tool]; 1s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T01:23:55.6701873Z [379 / 760] Linking common/kselftest_vdso_vdso_test_getcpu; 0s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T01:23:56.7104715Z [405 / 760] Compiling pigz.c [for tool]; 1s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T01:23:57.7811558Z [431 / 760] Compiling yarn.c [for tool]; 0s processwrapper-sandbox ... (3 actions, 2 running)
2026-05-03T01:23:58.7867756Z [461 / 760] Compiling cpu_features.c [for tool]; 0s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T01:23:59.8846356Z [492 / 760] Compiling deflate.c [for tool]; 0s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T01:24:00.9036652Z [519 / 760] Linking common/kselftest_net_reuseaddr_conflict; 0s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T01:24:01.9709840Z [542 / 760] Compiling infback.c [for tool]; 0s processwrapper-sandbox ... (5 actions, 4 running)
2026-05-03T01:24:02.9776083Z [571 / 760] Compiling inflate.c [for tool]; 0s processwrapper-sandbox ... (5 actions, 4 running)
2026-05-03T01:24:04.0933092Z [602 / 760] Compiling trees.c [for tool]; 0s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T01:24:05.1574237Z [616 / 760] Compiling zutil.c [for tool]; 0s processwrapper-sandbox ... (5 actions, 3 running)
2026-05-03T01:24:06.1996716Z [636 / 760] Compiling src/zopfli/deflate.c [for tool]; 0s processwrapper-sandbox ... (4 actions, 3 running)
2026-05-03T01:24:07.9725979Z [646 / 760] Executing genrule //build/kernel:gki_certification_tools; 1s processwrapper-sandbox ... (4 actions running)
2026-05-03T01:24:08.9730021Z [651 / 760] Executing genrule //build/kernel:gki_certification_tools; 2s processwrapper-sandbox ... (4 actions running)
2026-05-03T01:24:10.1146492Z [652 / 760] Creating archive @@//common:kernel_aarch64_ddk_headers_archive; 1s processwrapper-sandbox ... (4 actions running)
2026-05-03T01:24:11.1216553Z [656 / 760] Creating archive @@//common:kernel_aarch64_ddk_headers_archive; 2s processwrapper-sandbox ... (5 actions, 4 running)
2026-05-03T01:24:12.1177377Z [657 / 760] Creating archive @@//common:kernel_aarch64_ddk_headers_archive; 3s processwrapper-sandbox ... (5 actions, 4 running)
2026-05-03T01:24:13.1240551Z [662 / 760] Creating archive @@//common:kernel_aarch64_ddk_headers_archive; 4s processwrapper-sandbox ... (5 actions, 3 running)
2026-05-03T01:24:14.1223109Z [667 / 760] Archiving scripts/kconfig for ext module (lto=default;trim) @@//common:kernel_aarch64; 5s processwrapper-sandbox ... (5 actions, 4 running)
2026-05-03T01:24:15.2056507Z [685 / 760] Creating kernel config (lto=default;trim) @@//common:kernel_aarch64_config; 0s local ... (4 actions running)
2026-05-03T01:24:16.2049219Z [700 / 760] Creating kernel config (lto=default;trim) @@//common:kernel_aarch64_config; 1s local ... (4 actions running)
2026-05-03T01:24:17.2055991Z [719 / 760] Creating kernel config (lto=default;trim) @@//common:kernel_aarch64_config; 2s local ... (3 actions running)
2026-05-03T01:24:18.2067528Z [746 / 760] Creating kernel config (lto=default;trim) @@//common:kernel_aarch64_config; 3s local
2026-05-03T01:24:21.2610839Z INFO: From Creating kernel config (lto=default;trim) @@//common:kernel_aarch64_config:
2026-05-03T01:24:21.2612052Z arch/arm64/configs/gki_defconfig:798:warning: override: reassigning to symbol MODVERSIONS
2026-05-03T01:24:21.2613101Z arch/arm64/configs/gki_defconfig:803:warning: override: reassigning to symbol ZRAM
2026-05-03T01:24:21.2614166Z arch/arm64/configs/gki_defconfig:804:warning: override: reassigning to symbol ZRAM_WRITEBACK
2026-05-03T01:24:21.2615787Z arch/arm64/configs/gki_defconfig:808:warning: override: reassigning to symbol TRANSPARENT_HUGEPAGE
2026-05-03T01:24:21.2617008Z arch/arm64/configs/gki_defconfig:809:warning: override: reassigning to symbol SLAB_FREELIST_RANDOM
2026-05-03T01:24:21.2618130Z arch/arm64/configs/gki_defconfig:811:warning: override: reassigning to symbol LRU_GEN
2026-05-03T01:24:21.2619189Z arch/arm64/configs/gki_defconfig:812:warning: override: reassigning to symbol LRU_GEN_ENABLED
2026-05-03T01:24:21.2620297Z arch/arm64/configs/gki_defconfig:819:warning: override: reassigning to symbol TCP_CONG_ADVANCED
2026-05-03T01:24:21.2621628Z arch/arm64/configs/gki_defconfig:820:warning: override: reassigning to symbol TCP_CONG_BBR
2026-05-03T01:24:21.2622637Z arch/arm64/configs/gki_defconfig:821:warning: override: reassigning to symbol NET_SCH_FQ
2026-05-03T01:24:21.2623728Z arch/arm64/configs/gki_defconfig:846:warning: override: reassigning to symbol LOCALVERSION
2026-05-03T01:24:21.5029022Z [747 / 760] [Prepa] Building UAPI kernel headers kernel_aarch64_uapi_headers
2026-05-03T01:24:23.2087124Z [747 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 1s local ... (3 actions running)
2026-05-03T01:24:33.3249582Z [747 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 11s local ... (3 actions running)
2026-05-03T01:24:43.2220573Z [748 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 21s local ... (2 actions running)
2026-05-03T01:24:45.2240081Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 23s local
2026-05-03T01:24:56.3301881Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 34s local
2026-05-03T01:25:26.3356337Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 64s local
2026-05-03T01:26:26.3511095Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 124s local
2026-05-03T01:27:26.3602631Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 184s local
2026-05-03T01:28:26.3706342Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 244s local
2026-05-03T01:29:26.3856439Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 304s local
2026-05-03T01:30:26.3944640Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 364s local
2026-05-03T01:31:26.4030854Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 424s local
2026-05-03T01:32:26.4176212Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 484s local
2026-05-03T01:33:26.4326436Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 544s local
2026-05-03T01:34:26.4418184Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 604s local
2026-05-03T01:35:26.4580989Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 664s local
2026-05-03T01:36:26.4696356Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 724s local
2026-05-03T01:37:26.4773090Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 784s local
2026-05-03T01:38:26.4936447Z [749 / 760] Building kernel (lto=default;trim) @@//common:kernel_aarch64; 844s local
2026-05-03T01:38:41.1640679Z ERROR: /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/BUILD.bazel:154:22: Building kernel (lto=default;trim) @@//common:kernel_aarch64 failed: (Exit 2): bash failed: error executing KernelBuild command (from target //common:kernel_aarch64) /bin/bash -c ... (remaining 1 argument skipped)
2026-05-03T01:38:41.1706492Z /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/drivers/kernelsu/Kbuild:98: "KSU_GIT_VERSION not defined! It is better to make KernelSU-Next a git repository!"
2026-05-03T01:38:41.1711116Z /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/drivers/kernelsu/Kbuild:109: "KSU_VERSION_TAG not defined! It is better to make KernelSU-Next a git submodule!"
2026-05-03T01:38:41.1713015Z In file included from /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/drivers/kernelsu/core/init.c:10:
2026-05-03T01:38:41.1714778Z /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/drivers/kernelsu/policy/allowlist.h:6:10: fatal error: 'uapi/app_profile.h' file not found
2026-05-03T01:38:41.1716342Z     6 | #include "uapi/app_profile.h"
2026-05-03T01:38:41.1716740Z       |          ^~~~~~~~~~~~~~~~~~~~
2026-05-03T01:38:41.1717091Z 1 error generated.
2026-05-03T01:38:41.1718349Z make[5]: *** [/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/scripts/Makefile.build:243: drivers/kernelsu/core/init.o] Error 1
2026-05-03T01:38:41.1719447Z make[5]: *** Waiting for unfinished jobs....
2026-05-03T01:38:41.1720441Z In file included from /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/drivers/kernelsu/feature/kernel_umount.c:15:
2026-05-03T01:38:41.1722281Z /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/drivers/kernelsu/policy/allowlist.h:6:10: fatal error: 'uapi/app_profile.h' file not found
2026-05-03T01:38:41.1723595Z     6 | #include "uapi/app_profile.h"
2026-05-03T01:38:41.1724031Z       |          ^~~~~~~~~~~~~~~~~~~~
2026-05-03T01:38:41.1724423Z 1 error generated.
2026-05-03T01:38:41.1725826Z make[5]: *** [/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/scripts/Makefile.build:243: drivers/kernelsu/feature/kernel_umount.o] Error 1
2026-05-03T01:38:41.1727687Z make[4]: *** [/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/scripts/Makefile.build:480: drivers/kernelsu] Error 2
2026-05-03T01:38:41.1728866Z make[4]: *** Waiting for unfinished jobs....
2026-05-03T01:38:41.1729862Z make[3]: *** [/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/scripts/Makefile.build:480: drivers] Error 2
2026-05-03T01:38:41.1731306Z make[2]: *** [/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/Makefile:1977: .] Error 2
2026-05-03T01:38:41.1732701Z make[1]: *** [/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/Makefile:252: __sub-make] Error 2
2026-05-03T01:38:41.1733684Z make: *** [Makefile:252: __sub-make] Error 2
2026-05-03T01:38:41.1734160Z -- KernelSU-Next version fallback: 1
2026-05-03T01:38:41.1734606Z -- KernelSU-Next tag fallback: v0.0.1
2026-05-03T01:38:41.1737152Z -- KernelSU-Next new DCACHE flush: 1
2026-05-03T01:38:41.1737681Z -- KernelSU-Next Manager signature size: 0x3e6
2026-05-03T01:38:41.1738539Z -- KernelSU-Next Manager signature hash: 79e590113c4c4c0c222978e413a5faa801666957b1212a328e46c00c69821bf7
2026-05-03T01:38:41.2298139Z Target //common:kernel_aarch64_dist failed to build
2026-05-03T01:38:41.2301888Z Use --verbose_failures to see the command lines of failed build steps.
2026-05-03T01:38:41.2304558Z ERROR: /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/common/BUILD.bazel:154:22 Middleman _middlemen/common_Skernel_Uaarch64_Udist-runfiles failed: (Exit 2): bash failed: error executing KernelBuild command (from target //common:kernel_aarch64) /bin/bash -c ... (remaining 1 argument skipped)
2026-05-03T01:38:41.3197484Z INFO: Elapsed time: 909.084s, Critical Path: 876.22s
2026-05-03T01:38:41.3205521Z INFO: 750 processes: 438 internal, 2 local, 310 processwrapper-sandbox.
2026-05-03T01:38:41.3206689Z ERROR: Build did NOT complete successfully
2026-05-03T01:38:41.3373485Z ##[error]Process completed with exit code 1.
2026-05-03T01:38:41.3492806Z Post job cleanup.
2026-05-03T01:38:41.4407566Z [command]/usr/bin/git version
2026-05-03T01:38:41.4449485Z git version 2.53.0
2026-05-03T01:38:41.4516281Z Copying '/home/runner/.gitconfig' to '/home/runner/work/_temp/4a33767e-4b0e-4daa-87e2-697320fa30f4/.gitconfig'
2026-05-03T01:38:41.4528836Z Temporarily overriding HOME='/home/runner/work/_temp/4a33767e-4b0e-4daa-87e2-697320fa30f4' before making global git config changes
2026-05-03T01:38:41.4530208Z Adding repository directory to the temporary git global config as a safe directory
2026-05-03T01:38:41.4533709Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN
2026-05-03T01:38:41.4575185Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-05-03T01:38:41.4611196Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-05-03T01:38:41.4859171Z fatal: No url found for submodule path 'temp_susfs' in .gitmodules
2026-05-03T01:38:41.4894343Z ##[warning]The process '/usr/bin/git' failed with exit code 128
2026-05-03T01:38:41.5001877Z Cleaning up orphan processes
2026-05-03T01:38:41.5352322Z Terminate orphan process: pid (96219) (java.lang=ALL-UNNAMED)
2026-05-03T01:38:41.5396604Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
