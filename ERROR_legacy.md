2026-05-03T00:38:15.0416211Z Current runner version: '2.334.0'
2026-05-03T00:38:15.0441486Z ##[group]Runner Image Provisioner
2026-05-03T00:38:15.0442273Z Hosted Compute Agent
2026-05-03T00:38:15.0442945Z Version: 20260213.493
2026-05-03T00:38:15.0443515Z Commit: 5c115507f6dd24b8de37d8bbe0bb4509d0cc0fa3
2026-05-03T00:38:15.0444237Z Build Date: 2026-02-13T00:28:41Z
2026-05-03T00:38:15.0445348Z Worker ID: {de4e8cb0-8629-4e91-a965-369611c6e063}
2026-05-03T00:38:15.0446050Z Azure Region: centralus
2026-05-03T00:38:15.0446575Z ##[endgroup]
2026-05-03T00:38:15.0448693Z ##[group]Operating System
2026-05-03T00:38:15.0449326Z Ubuntu
2026-05-03T00:38:15.0449866Z 24.04.4
2026-05-03T00:38:15.0450431Z LTS
2026-05-03T00:38:15.0450869Z ##[endgroup]
2026-05-03T00:38:15.0451384Z ##[group]Runner Image
2026-05-03T00:38:15.0451917Z Image: ubuntu-24.04
2026-05-03T00:38:15.0452464Z Version: 20260413.86.1
2026-05-03T00:38:15.0453969Z Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20260413.86/images/ubuntu/Ubuntu2404-Readme.md
2026-05-03T00:38:15.0455455Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20260413.86
2026-05-03T00:38:15.0456369Z ##[endgroup]
2026-05-03T00:38:15.0457441Z ##[group]GITHUB_TOKEN Permissions
2026-05-03T00:38:15.0459810Z Contents: write
2026-05-03T00:38:15.0460451Z Metadata: read
2026-05-03T00:38:15.0460980Z ##[endgroup]
2026-05-03T00:38:15.0463018Z Secret source: Actions
2026-05-03T00:38:15.0464030Z Prepare workflow directory
2026-05-03T00:38:15.0851057Z Prepare all required actions
2026-05-03T00:38:15.0888715Z Getting action download info
2026-05-03T00:38:15.4718253Z Download action repository 'actions/checkout@v4' (SHA:34e114876b0b11c390a56381ad16ebd13914f8d5)
2026-05-03T00:38:15.5636351Z Download action repository 'actions/upload-artifact@v4' (SHA:ea165f8d65b6e75b540449e92b4886f43607fa02)
2026-05-03T00:38:15.6789207Z Download action repository 'softprops/action-gh-release@v2' (SHA:3bb12739c298aeb8a4eeaf626c5b8d85266b0e65)
2026-05-03T00:38:16.2762982Z Complete job name: Castorice Legacy 4.19
2026-05-03T00:38:16.3525183Z ##[group]Run actions/checkout@v4
2026-05-03T00:38:16.3526005Z with:
2026-05-03T00:38:16.3526433Z   repository: naidrahiqa/CastoriceKernelSUN
2026-05-03T00:38:16.3527180Z   token: ***
2026-05-03T00:38:16.3527591Z   ssh-strict: true
2026-05-03T00:38:16.3528017Z   ssh-user: git
2026-05-03T00:38:16.3528755Z   persist-credentials: true
2026-05-03T00:38:16.3529222Z   clean: true
2026-05-03T00:38:16.3529657Z   sparse-checkout-cone-mode: true
2026-05-03T00:38:16.3530154Z   fetch-depth: 1
2026-05-03T00:38:16.3530568Z   fetch-tags: false
2026-05-03T00:38:16.3530983Z   show-progress: true
2026-05-03T00:38:16.3531400Z   lfs: false
2026-05-03T00:38:16.3531772Z   submodules: false
2026-05-03T00:38:16.3532189Z   set-safe-directory: true
2026-05-03T00:38:16.3532866Z env:
2026-05-03T00:38:16.3533253Z   KERNEL_NAME: Castorice
2026-05-03T00:38:16.3533685Z   DEVICE_CODE: fire
2026-05-03T00:38:16.3534130Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:38:16.3534677Z   CLANG_VERSION: 
2026-05-03T00:38:16.3535130Z   LLD_VERSION: 
2026-05-03T00:38:16.3535515Z   KERNEL_HEAD_HASH: 
2026-05-03T00:38:16.3535916Z   KSU_DIR: 
2026-05-03T00:38:16.3536273Z   KSU_VERSION: 
2026-05-03T00:38:16.3536666Z   KERNEL_VERSION: 
2026-05-03T00:38:16.3537093Z   ZIP_NAME: 
2026-05-03T00:38:16.3537485Z ##[endgroup]
2026-05-03T00:38:16.4509994Z Syncing repository: naidrahiqa/CastoriceKernelSUN
2026-05-03T00:38:16.4511857Z ##[group]Getting Git version info
2026-05-03T00:38:16.4512643Z Working directory is '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN'
2026-05-03T00:38:16.4513777Z [command]/usr/bin/git version
2026-05-03T00:38:16.4537350Z git version 2.53.0
2026-05-03T00:38:16.4587424Z ##[endgroup]
2026-05-03T00:38:16.4601241Z Temporarily overriding HOME='/home/runner/work/_temp/3472f48f-fb82-4772-9c26-dc371f61912b' before making global git config changes
2026-05-03T00:38:16.4602679Z Adding repository directory to the temporary git global config as a safe directory
2026-05-03T00:38:16.4606661Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN
2026-05-03T00:38:16.4640956Z Deleting the contents of '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN'
2026-05-03T00:38:16.4644513Z ##[group]Initializing the repository
2026-05-03T00:38:16.4649204Z [command]/usr/bin/git init /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN
2026-05-03T00:38:16.4711061Z hint: Using 'master' as the name for the initial branch. This default branch name
2026-05-03T00:38:16.4712808Z hint: will change to "main" in Git 3.0. To configure the initial branch name
2026-05-03T00:38:16.4714108Z hint: to use in all of your new repositories, which will suppress this warning,
2026-05-03T00:38:16.4714985Z hint: call:
2026-05-03T00:38:16.4717246Z hint:
2026-05-03T00:38:16.4717971Z hint: 	git config --global init.defaultBranch <name>
2026-05-03T00:38:16.4718919Z hint:
2026-05-03T00:38:16.4719540Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2026-05-03T00:38:16.4720730Z hint: 'development'. The just-created branch can be renamed via this command:
2026-05-03T00:38:16.4722017Z hint:
2026-05-03T00:38:16.4722646Z hint: 	git branch -m <name>
2026-05-03T00:38:16.4723382Z hint:
2026-05-03T00:38:16.4724363Z hint: Disable this message with "git config set advice.defaultBranchName false"
2026-05-03T00:38:16.4726029Z Initialized empty Git repository in /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/.git/
2026-05-03T00:38:16.4728133Z [command]/usr/bin/git remote add origin https://github.com/naidrahiqa/CastoriceKernelSUN
2026-05-03T00:38:16.4755215Z ##[endgroup]
2026-05-03T00:38:16.4756358Z ##[group]Disabling automatic garbage collection
2026-05-03T00:38:16.4758275Z [command]/usr/bin/git config --local gc.auto 0
2026-05-03T00:38:16.4787543Z ##[endgroup]
2026-05-03T00:38:16.4788798Z ##[group]Setting up auth
2026-05-03T00:38:16.4793508Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-05-03T00:38:16.4825862Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-05-03T00:38:16.5104083Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-05-03T00:38:16.5135905Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-05-03T00:38:16.5365652Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-05-03T00:38:16.5397822Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-05-03T00:38:16.5628365Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2026-05-03T00:38:16.5663332Z ##[endgroup]
2026-05-03T00:38:16.5664649Z ##[group]Fetching the repository
2026-05-03T00:38:16.5673645Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +99b81c0a3ce3d33fcaf1bb4bb561d5e42ec54f8f:refs/remotes/origin/main
2026-05-03T00:38:16.8024174Z From https://github.com/naidrahiqa/CastoriceKernelSUN
2026-05-03T00:38:16.8025823Z  * [new ref]         99b81c0a3ce3d33fcaf1bb4bb561d5e42ec54f8f -> origin/main
2026-05-03T00:38:16.8052994Z ##[endgroup]
2026-05-03T00:38:16.8053936Z ##[group]Determining the checkout info
2026-05-03T00:38:16.8055480Z ##[endgroup]
2026-05-03T00:38:16.8060849Z [command]/usr/bin/git sparse-checkout disable
2026-05-03T00:38:16.8099440Z [command]/usr/bin/git config --local --unset-all extensions.worktreeConfig
2026-05-03T00:38:16.8127551Z ##[group]Checking out the ref
2026-05-03T00:38:16.8131337Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
2026-05-03T00:38:16.8175153Z Switched to a new branch 'main'
2026-05-03T00:38:16.8177403Z branch 'main' set up to track 'origin/main'.
2026-05-03T00:38:16.8183700Z ##[endgroup]
2026-05-03T00:38:16.8226168Z [command]/usr/bin/git log -1 --format=%H
2026-05-03T00:38:16.8249995Z 99b81c0a3ce3d33fcaf1bb4bb561d5e42ec54f8f
2026-05-03T00:38:16.8475679Z ##[group]Run echo "=== Before cleanup ==="
2026-05-03T00:38:16.8476998Z [36;1mecho "=== Before cleanup ==="[0m
2026-05-03T00:38:16.8478117Z [36;1mdf -h /[0m
2026-05-03T00:38:16.8479596Z [36;1msudo rm -rf /usr/share/dotnet /usr/local/lib/android /opt/ghc[0m
2026-05-03T00:38:16.8481569Z [36;1msudo rm -rf /usr/share/swift /usr/share/miniconda /opt/hostedtoolcache[0m
2026-05-03T00:38:16.8483591Z [36;1msudo rm -rf /usr/local/share/chromium /usr/local/share/powershell[0m
2026-05-03T00:38:16.8486538Z [36;1msudo apt-get remove -y '^dotnet-.*' '^llvm-.*' 'php.*' azure-cli google-cloud-cli google-chrome-stable firefox powershell mono-devel || true[0m
2026-05-03T00:38:16.8489200Z [36;1msudo apt-get autoremove -y[0m
2026-05-03T00:38:16.8490307Z [36;1msudo apt-get clean[0m
2026-05-03T00:38:16.8491340Z [36;1mecho "=== After cleanup ==="[0m
2026-05-03T00:38:16.8492376Z [36;1mdf -h /[0m
2026-05-03T00:38:16.8519561Z shell: /usr/bin/bash -e {0}
2026-05-03T00:38:16.8520538Z env:
2026-05-03T00:38:16.8521334Z   KERNEL_NAME: Castorice
2026-05-03T00:38:16.8522253Z   DEVICE_CODE: fire
2026-05-03T00:38:16.8523164Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:38:16.8524307Z   CLANG_VERSION: 
2026-05-03T00:38:16.8525103Z   LLD_VERSION: 
2026-05-03T00:38:16.8525887Z   KERNEL_HEAD_HASH: 
2026-05-03T00:38:16.8526718Z   KSU_DIR: 
2026-05-03T00:38:16.8527442Z   KSU_VERSION: 
2026-05-03T00:38:16.8528222Z   KERNEL_VERSION: 
2026-05-03T00:38:16.8529143Z   ZIP_NAME: 
2026-05-03T00:38:16.8529882Z ##[endgroup]
2026-05-03T00:38:16.8602251Z === Before cleanup ===
2026-05-03T00:38:16.8617357Z Filesystem      Size  Used Avail Use% Mounted on
2026-05-03T00:38:16.8619206Z /dev/root       145G   56G   90G  39% /
2026-05-03T00:38:44.5241122Z Reading package lists...
2026-05-03T00:38:44.7780221Z Building dependency tree...
2026-05-03T00:38:44.7795369Z Reading state information...
2026-05-03T00:38:45.2200746Z Package 'dotnet-hostfxr-6.0' is not installed, so not removed
2026-05-03T00:38:45.2203131Z Package 'dotnet-runtime-6.0' is not installed, so not removed
2026-05-03T00:38:45.2203885Z Package 'dotnet-sdk-6.0' is not installed, so not removed
2026-05-03T00:38:45.2302778Z Package 'dotnet-targeting-pack-6.0' is not installed, so not removed
2026-05-03T00:38:45.2303821Z Package 'dotnet-templates-6.0' is not installed, so not removed
2026-05-03T00:38:45.2304419Z Package 'llvm-21' is not installed, so not removed
2026-05-03T00:38:45.2304931Z Package 'php-lua' is not installed, so not removed
2026-05-03T00:38:45.2305536Z Package 'php-mysqlnd-ms' is not installed, so not removed
2026-05-03T00:38:45.2306109Z Package 'php-radius' is not installed, so not removed
2026-05-03T00:38:45.2306720Z Package 'php5.6-common' is not installed, so not removed
2026-05-03T00:38:45.2307274Z Package 'php5.6-json' is not installed, so not removed
2026-05-03T00:38:45.2308064Z Package 'php7.0-common' is not installed, so not removed
2026-05-03T00:38:45.2308869Z Package 'php7.1-common' is not installed, so not removed
2026-05-03T00:38:45.2309448Z Package 'php7.2-common' is not installed, so not removed
2026-05-03T00:38:45.2310000Z Package 'php7.3-common' is not installed, so not removed
2026-05-03T00:38:45.2310528Z Package 'php7.4-common' is not installed, so not removed
2026-05-03T00:38:45.2311068Z Package 'php8.0-common' is not installed, so not removed
2026-05-03T00:38:45.2311690Z Package 'php8.1-common' is not installed, so not removed
2026-05-03T00:38:45.2312217Z Package 'php8.2-common' is not installed, so not removed
2026-05-03T00:38:45.2312895Z Package 'php-pear-frontend-gtk' is not installed, so not removed
2026-05-03T00:38:45.2313523Z Package 'php-pear-frontend-web' is not installed, so not removed
2026-05-03T00:38:45.2314113Z Package 'php7.0-curl' is not installed, so not removed
2026-05-03T00:38:45.2315160Z Package 'php7.2-sodium' is not installed, so not removed
2026-05-03T00:38:45.2315704Z Package 'php5' is not installed, so not removed
2026-05-03T00:38:45.2316217Z Package 'php5-cli' is not installed, so not removed
2026-05-03T00:38:45.2317151Z Package 'php5-pgsql' is not installed, so not removed
2026-05-03T00:38:45.2318216Z Package 'php5-curl' is not installed, so not removed
2026-05-03T00:38:45.2318996Z Package 'php5-ldap' is not installed, so not removed
2026-05-03T00:38:45.2319569Z Package 'gosa-plugin-phpgw' is not installed, so not removed
2026-05-03T00:38:45.2320191Z Package 'gosa-plugin-phpgw-schema' is not installed, so not removed
2026-05-03T00:38:45.2320850Z Package 'gosa-plugin-phpscheduleit' is not installed, so not removed
2026-05-03T00:38:45.2321551Z Package 'gosa-plugin-phpscheduleit-schema' is not installed, so not removed
2026-05-03T00:38:45.2322156Z Package 'php-apc' is not installed, so not removed
2026-05-03T00:38:45.2322661Z Package 'php-suhosin' is not installed, so not removed
2026-05-03T00:38:45.2323237Z Package 'php5-mysql' is not installed, so not removed
2026-05-03T00:38:45.2323766Z Package 'libsparkline-php' is not installed, so not removed
2026-05-03T00:38:45.2324347Z Package 'libapache2-mod-php5' is not installed, so not removed
2026-05-03T00:38:45.2324912Z Package 'php5-fpm' is not installed, so not removed
2026-05-03T00:38:45.2325474Z Package 'libgv-php5' is not installed, so not removed
2026-05-03T00:38:45.2326080Z Package 'php-greew-oauth2-azure-provider' is not installed, so not removed
2026-05-03T00:38:45.2326766Z Package 'php-hayageek-oauth2-yahoo' is not installed, so not removed
2026-05-03T00:38:45.2327401Z Package 'php-league-oauth2-google' is not installed, so not removed
2026-05-03T00:38:45.2328053Z Package 'php-thenetworg-oauth2-azure' is not installed, so not removed
2026-05-03T00:38:45.2329457Z Package 'phpphylotree' is not installed, so not removed
2026-05-03T00:38:45.2330046Z Package 'php-http-request2' is not installed, so not removed
2026-05-03T00:38:45.2330607Z Package 'php-xcache' is not installed, so not removed
2026-05-03T00:38:45.2331151Z Package 'php-async-aws-s3' is not installed, so not removed
2026-05-03T00:38:45.2331777Z Package 'php-paragonie-random-compat' is not installed, so not removed
2026-05-03T00:38:45.2332406Z Package 'php-console-color2' is not installed, so not removed
2026-05-03T00:38:45.2333004Z Package 'php-doctrine-phpcr-odm' is not installed, so not removed
2026-05-03T00:38:45.2333650Z Package 'php-alcaeus-mongo-php-adapter' is not installed, so not removed
2026-05-03T00:38:45.2334320Z Package 'php-doctrine-mongodb-odm' is not installed, so not removed
2026-05-03T00:38:45.2334968Z Package 'php-mtdowling-cron-expression' is not installed, so not removed
2026-05-03T00:38:45.2335595Z Package 'php-semsol-arc2' is not installed, so not removed
2026-05-03T00:38:45.2336169Z Package 'php-fzaninotto-faker' is not installed, so not removed
2026-05-03T00:38:45.2336698Z Package 'php7.4' is not installed, so not removed
2026-05-03T00:38:45.2337184Z Package 'php7.4-cli' is not installed, so not removed
2026-05-03T00:38:45.2337707Z Package 'php-com-dotnet' is not installed, so not removed
2026-05-03T00:38:45.2338220Z Package 'php-rar' is not installed, so not removed
2026-05-03T00:38:45.2338967Z Package 'php-laminas-httphandlerrunner' is not installed, so not removed
2026-05-03T00:38:45.2339643Z Package 'php-cordoval-hamcrest-php' is not installed, so not removed
2026-05-03T00:38:45.2340341Z Package 'php-davedevelopment-hamcrest-php' is not installed, so not removed
2026-05-03T00:38:45.2341024Z Package 'php-kodova-hamcrest-php' is not installed, so not removed
2026-05-03T00:38:45.2341671Z Package 'php-league-flysystem-sftp' is not installed, so not removed
2026-05-03T00:38:45.2342398Z Package 'php-league-flysystem-eventable-filesystem' is not installed, so not removed
2026-05-03T00:38:45.2343244Z Package 'php-league-flysystem-rackspace' is not installed, so not removed
2026-05-03T00:38:45.2343970Z Package 'php-league-flysystem-azure' is not installed, so not removed
2026-05-03T00:38:45.2344871Z Package 'php-league-flysystem-webdav' is not installed, so not removed
2026-05-03T00:38:45.2345567Z Package 'php-league-flysystem-aws-s3-v2' is not installed, so not removed
2026-05-03T00:38:45.2346460Z Package 'php-league-flysystem-aws-s3-v3' is not installed, so not removed
2026-05-03T00:38:45.2347187Z Package 'php-spatie-flysystem-dropbox' is not installed, so not removed
2026-05-03T00:38:45.2347919Z Package 'php-srmklive-flysystem-dropbox-v2' is not installed, so not removed
2026-05-03T00:38:45.2348847Z Package 'php-league-flysystem-cached-adapter' is not installed, so not removed
2026-05-03T00:38:45.2349617Z Package 'php-league-flysystem-ziparchive' is not installed, so not removed
2026-05-03T00:38:45.2350304Z Package 'php-league-uri-schemes' is not installed, so not removed
2026-05-03T00:38:45.2351016Z Package 'php-jeremykendall-php-domain-parser' is not installed, so not removed
2026-05-03T00:38:45.2351694Z Package 'php-php-64bit' is not installed, so not removed
2026-05-03T00:38:45.2352238Z Package 'php-sqlite' is not installed, so not removed
2026-05-03T00:38:45.2352756Z Package 'php-lzf' is not installed, so not removed
2026-05-03T00:38:45.2353266Z Package 'php-pnctl' is not installed, so not removed
2026-05-03T00:38:45.2353853Z Package 'php-mdb2-driver-fbsql' is not installed, so not removed
2026-05-03T00:38:45.2354465Z Package 'php-mdb2-driver-ibase' is not installed, so not removed
2026-05-03T00:38:45.2355075Z Package 'php-mdb2-driver-mssql' is not installed, so not removed
2026-05-03T00:38:45.2355681Z Package 'php-mdb2-driver-mysqli' is not installed, so not removed
2026-05-03T00:38:45.2356304Z Package 'php-mdb2-driver-oci8' is not installed, so not removed
2026-05-03T00:38:45.2356913Z Package 'php-mdb2-driver-odbc' is not installed, so not removed
2026-05-03T00:38:45.2357538Z Package 'php-mdb2-driver-querysim' is not installed, so not removed
2026-05-03T00:38:45.2358176Z Package 'php-mdb2-driver-sqlite' is not installed, so not removed
2026-05-03T00:38:45.2358952Z Package 'php-mdb2-driver-sqlsrv' is not installed, so not removed
2026-05-03T00:38:45.2359628Z Package 'php-barnabywalters-mf-cleaner' is not installed, so not removed
2026-05-03T00:38:45.2360310Z Package 'php-graylog2-gelf-php' is not installed, so not removed
2026-05-03T00:38:45.2360934Z Package 'php-doctrine-couchdb' is not installed, so not removed
2026-05-03T00:38:45.2361552Z Package 'php-ruflin-elastica' is not installed, so not removed
2026-05-03T00:38:45.2362144Z Package 'php-elasticsearch' is not installed, so not removed
2026-05-03T00:38:45.2362734Z Package 'php-aws-sdk-php' is not installed, so not removed
2026-05-03T00:38:45.2363275Z Package 'php-rollbar' is not installed, so not removed
2026-05-03T00:38:45.2363839Z Package 'php-nette-finder' is not installed, so not removed
2026-05-03T00:38:45.2364374Z Package 'php-dbase' is not installed, so not removed
2026-05-03T00:38:45.2364909Z Package 'php-libsodium' is not installed, so not removed
2026-05-03T00:38:45.2365445Z Package 'php-relay' is not installed, so not removed
2026-05-03T00:38:45.2366056Z Package 'php-ocramius-proxy-manager' is not installed, so not removed
2026-05-03T00:38:45.2366782Z Package 'php-zendframework-zend-stdlib' is not installed, so not removed
2026-05-03T00:38:45.2367432Z Package 'php-rhumsaa-uuid' is not installed, so not removed
2026-05-03T00:38:45.2368067Z Package 'php-paragonie-random-lib' is not installed, so not removed
2026-05-03T00:38:45.2368916Z Package 'php-ramsey-uuid-doctrine' is not installed, so not removed
2026-05-03T00:38:45.2369542Z Package 'php-crypt-blowfish' is not installed, so not removed
2026-05-03T00:38:45.2370106Z Package 'php-compat' is not installed, so not removed
2026-05-03T00:38:45.2370621Z Package 'libssh2-php' is not installed, so not removed
2026-05-03T00:38:45.2371214Z Package 'php-php-http-discovery' is not installed, so not removed
2026-05-03T00:38:45.2371872Z Package 'php-symfony-security-guard' is not installed, so not removed
2026-05-03T00:38:45.2372506Z Package 'php-numbers-words' is not installed, so not removed
2026-05-03T00:38:45.2373287Z Package 'php7.0-thrift' is not installed, so not removed
2026-05-03T00:38:45.2373831Z Package 'php7.2-thrift' is not installed, so not removed
2026-05-03T00:38:45.2374568Z Package 'php-net-idna' is not installed, so not removed
2026-05-03T00:38:45.2375109Z Package 'php-phpstan' is not installed, so not removed
2026-05-03T00:38:45.2375673Z Package 'php-vimeo-psalm' is not installed, so not removed
2026-05-03T00:38:45.2376266Z Package 'php-container-interop' is not installed, so not removed
2026-05-03T00:38:45.2376976Z Package 'php-zendframework-zend-eventmanager' is not installed, so not removed
2026-05-03T00:38:45.2377619Z Package 'php-recode' is not installed, so not removed
2026-05-03T00:38:45.2378126Z Package 'php-gd2' is not installed, so not removed
2026-05-03T00:38:45.2378884Z Package 'php-pragmarx-google2fa-qrcode' is not installed, so not removed
2026-05-03T00:38:45.2379570Z Package 'php-bjeavons-zxcvbn-php' is not installed, so not removed
2026-05-03T00:38:45.2380217Z Package 'php-pimlie-php-dkim' is not installed, so not removed
2026-05-03T00:38:45.2380831Z Package 'libapache2-mod-php7.4' is not installed, so not removed
2026-05-03T00:38:45.2381411Z Package 'php7.4-fpm' is not installed, so not removed
2026-05-03T00:38:45.2381985Z Package 'dotnet-apphost-pack-6.0' is not installed, so not removed
2026-05-03T00:38:45.2382612Z Package 'dotnet-runtime-8.0' is not installed, so not removed
2026-05-03T00:38:45.2383230Z Package 'dotnet-apphost-pack-8.0' is not installed, so not removed
2026-05-03T00:38:45.2383834Z Package 'dotnet-host-8.0' is not installed, so not removed
2026-05-03T00:38:45.2384418Z Package 'dotnet-hostfxr-8.0' is not installed, so not removed
2026-05-03T00:38:45.2384994Z Package 'dotnet-sdk-8.0' is not installed, so not removed
2026-05-03T00:38:45.2385608Z Package 'dotnet-targeting-pack-8.0' is not installed, so not removed
2026-05-03T00:38:45.2386256Z Package 'dotnet-templates-8.0' is not installed, so not removed
2026-05-03T00:38:45.2386883Z Package 'dotnet-runtime-dbg-8.0' is not installed, so not removed
2026-05-03T00:38:45.2387605Z Package 'dotnet-sdk-8.0-source-built-artifacts' is not installed, so not removed
2026-05-03T00:38:45.2388312Z Package 'dotnet-sdk-dbg-8.0' is not installed, so not removed
2026-05-03T00:38:45.2389045Z Package 'dotnet-runtime-10.0' is not installed, so not removed
2026-05-03T00:38:45.2389669Z Package 'dotnet-apphost-pack-10.0' is not installed, so not removed
2026-05-03T00:38:45.2390267Z Package 'dotnet-host-10.0' is not installed, so not removed
2026-05-03T00:38:45.2390844Z Package 'dotnet-hostfxr-10.0' is not installed, so not removed
2026-05-03T00:38:45.2391452Z Package 'dotnet-runtime-dbg-10.0' is not installed, so not removed
2026-05-03T00:38:45.2392039Z Package 'dotnet-sdk-10.0' is not installed, so not removed
2026-05-03T00:38:45.2392640Z Package 'dotnet-targeting-pack-10.0' is not installed, so not removed
2026-05-03T00:38:45.2393287Z Package 'dotnet-templates-10.0' is not installed, so not removed
2026-05-03T00:38:45.2393904Z Package 'dotnet-sdk-aot-10.0' is not installed, so not removed
2026-05-03T00:38:45.2394484Z Package 'dotnet-sdk-dbg-10.0' is not installed, so not removed
2026-05-03T00:38:45.2395188Z Package 'dotnet-sdk-10.0-source-built-artifacts' is not installed, so not removed
2026-05-03T00:38:45.2395882Z Package 'llvm-14-linker-tools' is not installed, so not removed
2026-05-03T00:38:45.2396440Z Package 'llvm-14-dev' is not installed, so not removed
2026-05-03T00:38:45.2396994Z Package 'llvm-15-linker-tools' is not installed, so not removed
2026-05-03T00:38:45.2397549Z Package 'llvm-15-dev' is not installed, so not removed
2026-05-03T00:38:45.2398048Z Package 'llvm-15' is not installed, so not removed
2026-05-03T00:38:45.2398671Z Package 'llvm-dev' is not installed, so not removed
2026-05-03T00:38:45.2399175Z Package 'llvm-14-doc' is not installed, so not removed
2026-05-03T00:38:45.2399675Z Package 'llvm-15-doc' is not installed, so not removed
2026-05-03T00:38:45.2400182Z Package 'llvm-16-doc' is not installed, so not removed
2026-05-03T00:38:45.2400949Z Package 'llvm-17-doc' is not installed, so not removed
2026-05-03T00:38:45.2401452Z Package 'llvm-18-doc' is not installed, so not removed
2026-05-03T00:38:45.2402138Z Package 'llvm-runtime' is not installed, so not removed
2026-05-03T00:38:45.2402642Z Package 'llvm-14' is not installed, so not removed
2026-05-03T00:38:45.2403157Z Package 'llvm-14-runtime' is not installed, so not removed
2026-05-03T00:38:45.2403698Z Package 'llvm-14-tools' is not installed, so not removed
2026-05-03T00:38:45.2404256Z Package 'llvm-14-examples' is not installed, so not removed
2026-05-03T00:38:45.2404807Z Package 'llvm-15-runtime' is not installed, so not removed
2026-05-03T00:38:45.2405348Z Package 'llvm-15-tools' is not installed, so not removed
2026-05-03T00:38:45.2405881Z Package 'llvm-15-examples' is not installed, so not removed
2026-05-03T00:38:45.2406431Z Package 'llvm-16-examples' is not installed, so not removed
2026-05-03T00:38:45.2406987Z Package 'llvm-17-examples' is not installed, so not removed
2026-05-03T00:38:45.2407547Z Package 'llvm-18-examples' is not installed, so not removed
2026-05-03T00:38:45.2408088Z Package 'llvm-bolt' is not installed, so not removed
2026-05-03T00:38:45.2408794Z Package 'llvm-spirv-14' is not installed, so not removed
2026-05-03T00:38:45.2409324Z Package 'llvm-spirv-15' is not installed, so not removed
2026-05-03T00:38:45.2409848Z Package 'llvm-spirv-16' is not installed, so not removed
2026-05-03T00:38:45.2410383Z Package 'llvm-spirv-17' is not installed, so not removed
2026-05-03T00:38:45.2410914Z Package 'llvm-spirv-18' is not installed, so not removed
2026-05-03T00:38:45.2411420Z Package 'llvm-19-dev' is not installed, so not removed
2026-05-03T00:38:45.2411935Z Package 'llvm-20-dev' is not installed, so not removed
2026-05-03T00:38:45.2412482Z Package 'llvm-19-linker-tools' is not installed, so not removed
2026-05-03T00:38:45.2413081Z Package 'llvm-20-linker-tools' is not installed, so not removed
2026-05-03T00:38:45.2413649Z Package 'llvm-19-doc' is not installed, so not removed
2026-05-03T00:38:45.2414172Z Package 'llvm-20-doc' is not installed, so not removed
2026-05-03T00:38:45.2414663Z Package 'llvm-19' is not installed, so not removed
2026-05-03T00:38:45.2415187Z Package 'llvm-19-runtime' is not installed, so not removed
2026-05-03T00:38:45.2415731Z Package 'llvm-19-tools' is not installed, so not removed
2026-05-03T00:38:45.2416262Z Package 'llvm-19-examples' is not installed, so not removed
2026-05-03T00:38:45.2416839Z Package 'llvm-20' is not installed, so not removed
2026-05-03T00:38:45.2417354Z Package 'llvm-20-runtime' is not installed, so not removed
2026-05-03T00:38:45.2417892Z Package 'llvm-20-tools' is not installed, so not removed
2026-05-03T00:38:45.2418581Z Package 'llvm-20-examples' is not installed, so not removed
2026-05-03T00:38:45.2419131Z Package 'llvm-spirv-19' is not installed, so not removed
2026-05-03T00:38:45.2419654Z Package 'llvm-spirv-20' is not installed, so not removed
2026-05-03T00:38:45.2420198Z Package 'php-crypt-gpg' is not installed, so not removed
2026-05-03T00:38:45.2420764Z Package 'libapache2-mod-php' is not installed, so not removed
2026-05-03T00:38:45.2421416Z Package 'libapache2-mod-php8.3' is not installed, so not removed
2026-05-03T00:38:45.2421996Z Package 'php-json' is not installed, so not removed
2026-05-03T00:38:45.2422501Z Package 'php' is not installed, so not removed
2026-05-03T00:38:45.2422995Z Package 'php-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2423501Z Package 'php-cgi' is not installed, so not removed
2026-05-03T00:38:45.2423985Z Package 'php-cli' is not installed, so not removed
2026-05-03T00:38:45.2424465Z Package 'php-amqp' is not installed, so not removed
2026-05-03T00:38:45.2424965Z Package 'php-apcu' is not installed, so not removed
2026-05-03T00:38:45.2425441Z Package 'php-ast' is not installed, so not removed
2026-05-03T00:38:45.2425928Z Package 'php-ds' is not installed, so not removed
2026-05-03T00:38:45.2426469Z Package 'php-facedetect' is not installed, so not removed
2026-05-03T00:38:45.2427237Z Package 'php-gearman' is not installed, so not removed
2026-05-03T00:38:45.2427755Z Package 'php-gmagick' is not installed, so not removed
2026-05-03T00:38:45.2428568Z Package 'php-gnupg' is not installed, so not removed
2026-05-03T00:38:45.2429108Z Package 'php-igbinary' is not installed, so not removed
2026-05-03T00:38:45.2429623Z Package 'php-imagick' is not installed, so not removed
2026-05-03T00:38:45.2430163Z Package 'php-libvirt-php' is not installed, so not removed
2026-05-03T00:38:45.2430708Z Package 'php-mailparse' is not installed, so not removed
2026-05-03T00:38:45.2431241Z Package 'php-memcache' is not installed, so not removed
2026-05-03T00:38:45.2431768Z Package 'php-memcached' is not installed, so not removed
2026-05-03T00:38:45.2432292Z Package 'php-mongodb' is not installed, so not removed
2026-05-03T00:38:45.2432809Z Package 'php-msgpack' is not installed, so not removed
2026-05-03T00:38:45.2433313Z Package 'php-oauth' is not installed, so not removed
2026-05-03T00:38:45.2433836Z Package 'php-pcov' is not installed, so not removed
2026-05-03T00:38:45.2434324Z Package 'php-ps' is not installed, so not removed
2026-05-03T00:38:45.2434823Z Package 'php-psr' is not installed, so not removed
2026-05-03T00:38:45.2435305Z Package 'php-raphf' is not installed, so not removed
2026-05-03T00:38:45.2435795Z Package 'php-redis' is not installed, so not removed
2026-05-03T00:38:45.2436282Z Package 'php-rrd' is not installed, so not removed
2026-05-03T00:38:45.2436788Z Package 'php-smbclient' is not installed, so not removed
2026-05-03T00:38:45.2437304Z Package 'php-ssh2' is not installed, so not removed
2026-05-03T00:38:45.2437781Z Package 'php-stomp' is not installed, so not removed
2026-05-03T00:38:45.2438297Z Package 'php-tideways' is not installed, so not removed
2026-05-03T00:38:45.2438946Z Package 'php-uopz' is not installed, so not removed
2026-05-03T00:38:45.2439496Z Package 'php-uploadprogress' is not installed, so not removed
2026-05-03T00:38:45.2440046Z Package 'php-uuid' is not installed, so not removed
2026-05-03T00:38:45.2440545Z Package 'php-xdebug' is not installed, so not removed
2026-05-03T00:38:45.2441070Z Package 'php-xmlrpc' is not installed, so not removed
2026-05-03T00:38:45.2441567Z Package 'php-yac' is not installed, so not removed
2026-05-03T00:38:45.2442057Z Package 'php-yaml' is not installed, so not removed
2026-05-03T00:38:45.2442538Z Package 'php-zmq' is not installed, so not removed
2026-05-03T00:38:45.2443027Z Package 'php-curl' is not installed, so not removed
2026-05-03T00:38:45.2443498Z Package 'php-dev' is not installed, so not removed
2026-05-03T00:38:45.2443982Z Package 'php-gd' is not installed, so not removed
2026-05-03T00:38:45.2444457Z Package 'php-gmp' is not installed, so not removed
2026-05-03T00:38:45.2444937Z Package 'php-ldap' is not installed, so not removed
2026-05-03T00:38:45.2445429Z Package 'php-mysql' is not installed, so not removed
2026-05-03T00:38:45.2445915Z Package 'php-odbc' is not installed, so not removed
2026-05-03T00:38:45.2446412Z Package 'php-xml' is not installed, so not removed
2026-05-03T00:38:45.2446898Z Package 'php-pgsql' is not installed, so not removed
2026-05-03T00:38:45.2447420Z Package 'php-pspell' is not installed, so not removed
2026-05-03T00:38:45.2447915Z Package 'php-snmp' is not installed, so not removed
2026-05-03T00:38:45.2448615Z Package 'php-sqlite3' is not installed, so not removed
2026-05-03T00:38:45.2449609Z Package 'php-tidy' is not installed, so not removed
2026-05-03T00:38:45.2450099Z Package 'php-tokenizer' is not installed, so not removed
2026-05-03T00:38:45.2450557Z Package 'pkg-php-tools' is not installed, so not removed
2026-05-03T00:38:45.2450944Z Package 'dh-php' is not installed, so not removed
2026-05-03T00:38:45.2451338Z Package 'php-mbstring' is not installed, so not removed
2026-05-03T00:38:45.2451722Z Package 'php-readline' is not installed, so not removed
2026-05-03T00:38:45.2452092Z Package 'php-fpm' is not installed, so not removed
2026-05-03T00:38:45.2452744Z Package 'php-codesniffer' is not installed, so not removed
2026-05-03T00:38:45.2453168Z Package 'libphp-phpmailer' is not installed, so not removed
2026-05-03T00:38:45.2453774Z Package 'php-phpmyadmin-motranslator' is not installed, so not removed
2026-05-03T00:38:45.2454243Z Package 'php-phpseclib' is not installed, so not removed
2026-05-03T00:38:45.2454635Z Package 'php-twig' is not installed, so not removed
2026-05-03T00:38:45.2455024Z Package 'php-mapscript-ng' is not installed, so not removed
2026-05-03T00:38:45.2455463Z Package 'php-composer-ca-bundle' is not installed, so not removed
2026-05-03T00:38:45.2455967Z Package 'php-composer-class-map-generator' is not installed, so not removed
2026-05-03T00:38:45.2456512Z Package 'php-composer-metadata-minifier' is not installed, so not removed
2026-05-03T00:38:45.2456998Z Package 'php-composer-semver' is not installed, so not removed
2026-05-03T00:38:45.2457469Z Package 'php-composer-spdx-licenses' is not installed, so not removed
2026-05-03T00:38:45.2457981Z Package 'php-composer-xdebug-handler' is not installed, so not removed
2026-05-03T00:38:45.2458589Z Package 'php-json-schema' is not installed, so not removed
2026-05-03T00:38:45.2459059Z Package 'php-psr-log' is not installed, so not removed
2026-05-03T00:38:45.2459473Z Package 'php-symfony-console' is not installed, so not removed
2026-05-03T00:38:45.2459922Z Package 'php-symfony-filesystem' is not installed, so not removed
2026-05-03T00:38:45.2460369Z Package 'php-symfony-finder' is not installed, so not removed
2026-05-03T00:38:45.2460792Z Package 'php-symfony-process' is not installed, so not removed
2026-05-03T00:38:45.2461222Z Package 'php-react-promise' is not installed, so not removed
2026-05-03T00:38:45.2461643Z Package 'php-composer-pcre' is not installed, so not removed
2026-05-03T00:38:45.2462089Z Package 'php-seld-signal-handler' is not installed, so not removed
2026-05-03T00:38:45.2462501Z Package 'php-intl' is not installed, so not removed
2026-05-03T00:38:45.2462875Z Package 'php-zip' is not installed, so not removed
2026-05-03T00:38:45.2463259Z Package 'libawl-php' is not installed, so not removed
2026-05-03T00:38:45.2463664Z Package 'libphp-simplepie' is not installed, so not removed
2026-05-03T00:38:45.2464066Z Package 'php-geshi' is not installed, so not removed
2026-05-03T00:38:45.2464464Z Package 'php-random-compat' is not installed, so not removed
2026-05-03T00:38:45.2464881Z Package 'elpa-php-mode' is not installed, so not removed
2026-05-03T00:38:45.2465251Z Package 'phpunit' is not installed, so not removed
2026-05-03T00:38:45.2465617Z Package 'php-geos' is not installed, so not removed
2026-05-03T00:38:45.2466085Z Package 'golang-github-phpdave11-gofpdi-dev' is not installed, so not removed
2026-05-03T00:38:45.2466544Z Package 'php-imap' is not installed, so not removed
2026-05-03T00:38:45.2466907Z Package 'php-fpdf' is not installed, so not removed
2026-05-03T00:38:45.2467291Z Package 'icinga-php-library' is not installed, so not removed
2026-05-03T00:38:45.2467739Z Package 'icinga-php-thirdparty' is not installed, so not removed
2026-05-03T00:38:45.2468136Z Package 'php-soap' is not installed, so not removed
2026-05-03T00:38:45.2468630Z Package 'php-icinga' is not installed, so not removed
2026-05-03T00:38:45.2469001Z Package 'php-tcpdf' is not installed, so not removed
2026-05-03T00:38:45.2469384Z Package 'kdevelop-php' is not installed, so not removed
2026-05-03T00:38:45.2469786Z Package 'kdevelop-php-l10n' is not installed, so not removed
2026-05-03T00:38:45.2470176Z Package 'php-mcrypt' is not installed, so not removed
2026-05-03T00:38:45.2470543Z Package 'less.php' is not installed, so not removed
2026-05-03T00:38:45.2470963Z Package 'libphp-serialization-perl' is not installed, so not removed
2026-05-03T00:38:45.2471483Z Package 'libhtml-wikiconverter-phpwiki-perl' is not installed, so not removed
2026-05-03T00:38:45.2472000Z Package 'libjs-php-date-formatter' is not installed, so not removed
2026-05-03T00:38:45.2472449Z Package 'libmarkdown-php' is not installed, so not removed
2026-05-03T00:38:45.2472997Z Package 'libnusoap-php' is not installed, so not removed
2026-05-03T00:38:45.2473395Z Package 'php-econea-nusoap' is not installed, so not removed
2026-05-03T00:38:45.2473914Z Package 'libow-php7t64' is not installed, so not removed
2026-05-03T00:38:45.2474304Z Package 'libownet-php' is not installed, so not removed
2026-05-03T00:38:45.2474688Z Package 'libphp-adodb' is not installed, so not removed
2026-05-03T00:38:45.2475052Z Package 'php-sybase' is not installed, so not removed
2026-05-03T00:38:45.2475429Z Package 'libphp-embed' is not installed, so not removed
2026-05-03T00:38:45.2475814Z Package 'libphp8.3-embed' is not installed, so not removed
2026-05-03T00:38:45.2476207Z Package 'libphp-jabber' is not installed, so not removed
2026-05-03T00:38:45.2476594Z Package 'libphp-snoopy' is not installed, so not removed
2026-05-03T00:38:45.2476969Z Package 'libphpy-dev' is not installed, so not removed
2026-05-03T00:38:45.2477332Z Package 'libphpy1' is not installed, so not removed
2026-05-03T00:38:45.2477726Z Package 'libxrdcephposix0' is not installed, so not removed
2026-05-03T00:38:45.2478117Z Package 'php-spyc' is not installed, so not removed
2026-05-03T00:38:45.2478612Z Package 'matomo-php-tracker' is not installed, so not removed
2026-05-03T00:38:45.2479029Z Package 'php-wikidiff2' is not installed, so not removed
2026-05-03T00:38:45.2479421Z Package 'php-luasandbox' is not installed, so not removed
2026-05-03T00:38:45.2479816Z Package 'mlmmj-php-web' is not installed, so not removed
2026-05-03T00:38:45.2480224Z Package 'mlmmj-php-web-admin' is not installed, so not removed
2026-05-03T00:38:45.2480629Z Package 'php-net-socket' is not installed, so not removed
2026-05-03T00:38:45.2481060Z Package 'node-codemirror-lang-php' is not installed, so not removed
2026-05-03T00:38:45.2481487Z Package 'node-lezer-php' is not installed, so not removed
2026-05-03T00:38:45.2481869Z Package 'phpmyadmin' is not installed, so not removed
2026-05-03T00:38:45.2482231Z Package 'php-cas' is not installed, so not removed
2026-05-03T00:38:45.2482606Z Package 'php-pclzip' is not installed, so not removed
2026-05-03T00:38:45.2482978Z Package 'phpqrcode' is not installed, so not removed
2026-05-03T00:38:45.2483375Z Package 'php-symfony-config' is not installed, so not removed
2026-05-03T00:38:45.2483859Z Package 'php-symfony-dependency-injection' is not installed, so not removed
2026-05-03T00:38:45.2484300Z Package 'phpmd' is not installed, so not removed
2026-05-03T00:38:45.2484712Z Package 'php-algo26-idna-convert' is not installed, so not removed
2026-05-03T00:38:45.2485202Z Package 'php-jakeasmith-http-build-url' is not installed, so not removed
2026-05-03T00:38:45.2485658Z Package 'php-amphp-amp' is not installed, so not removed
2026-05-03T00:38:45.2486059Z Package 'php-amqp-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2486450Z Package 'php-amqplib' is not installed, so not removed
2026-05-03T00:38:45.2486839Z Package 'php-apcu-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2487314Z Package 'php-arthurhoaro-web-thumbnailer' is not installed, so not removed
2026-05-03T00:38:45.2487797Z Package 'php-text-template' is not installed, so not removed
2026-05-03T00:38:45.2488191Z Package 'php8.3-ast' is not installed, so not removed
2026-05-03T00:38:45.2488718Z Package 'php-ast-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2489140Z Package 'php-async-aws-core' is not installed, so not removed
2026-05-03T00:38:45.2489548Z Package 'php-psr-cache' is not installed, so not removed
2026-05-03T00:38:45.2490027Z Package 'php-symfony-deprecation-contracts' is not installed, so not removed
2026-05-03T00:38:45.2490534Z Package 'php-symfony-http-client' is not installed, so not removed
2026-05-03T00:38:45.2491037Z Package 'php-symfony-http-client-contracts' is not installed, so not removed
2026-05-03T00:38:45.2491553Z Package 'php-symfony-service-contracts' is not installed, so not removed
2026-05-03T00:38:45.2492019Z Package 'php-async-aws-ses' is not installed, so not removed
2026-05-03T00:38:45.2492591Z Package 'php-async-aws-sns' is not installed, so not removed
2026-05-03T00:38:45.2492994Z Package 'php-async-aws-sqs' is not installed, so not removed
2026-05-03T00:38:45.2493514Z Package 'php-auth-sasl' is not installed, so not removed
2026-05-03T00:38:45.2493909Z Package 'php-bacon-qr-code' is not installed, so not removed
2026-05-03T00:38:45.2494329Z Package 'php-dasprid-enum' is not installed, so not removed
2026-05-03T00:38:45.2494725Z Package 'php-bcmath' is not installed, so not removed
2026-05-03T00:38:45.2495145Z Package 'php-brick-math' is not installed, so not removed
2026-05-03T00:38:45.2495576Z Package 'php-brick-varexporter' is not installed, so not removed
2026-05-03T00:38:45.2495986Z Package 'php-parser' is not installed, so not removed
2026-05-03T00:38:45.2496352Z Package 'php-bz2' is not installed, so not removed
2026-05-03T00:38:45.2496772Z Package 'php-cache-integration-tests' is not installed, so not removed
2026-05-03T00:38:45.2497255Z Package 'php-cache-tag-interop' is not installed, so not removed
2026-05-03T00:38:45.2497715Z Package 'php-christianriesen-base32' is not installed, so not removed
2026-05-03T00:38:45.2498200Z Package 'php-christianriesen-otp' is not installed, so not removed
2026-05-03T00:38:45.2498774Z Package 'php-code-lts-u2f-php-server' is not installed, so not removed
2026-05-03T00:38:45.2499219Z Package 'php-codecoverage' is not installed, so not removed
2026-05-03T00:38:45.2499636Z Package 'php-file-iterator' is not installed, so not removed
2026-05-03T00:38:45.2500104Z Package 'phpunit-code-unit-reverse-lookup' is not installed, so not removed
2026-05-03T00:38:45.2500584Z Package 'phpunit-complexity' is not installed, so not removed
2026-05-03T00:38:45.2501004Z Package 'phpunit-environment' is not installed, so not removed
2026-05-03T00:38:45.2501444Z Package 'phpunit-lines-of-code' is not installed, so not removed
2026-05-03T00:38:45.2501869Z Package 'phpunit-version' is not installed, so not removed
2026-05-03T00:38:45.2502316Z Package 'php-codeigniter-framework' is not installed, so not removed
2026-05-03T00:38:45.2502812Z Package 'php-codeigniter-framework-doc' is not installed, so not removed
2026-05-03T00:38:45.2503299Z Package 'php-console-commandline' is not installed, so not removed
2026-05-03T00:38:45.2503741Z Package 'php-console-table' is not installed, so not removed
2026-05-03T00:38:45.2504147Z Package 'php-constant-time' is not installed, so not removed
2026-05-03T00:38:45.2504559Z Package 'php-dapphp-radius' is not installed, so not removed
2026-05-03T00:38:45.2504951Z Package 'php-date' is not installed, so not removed
2026-05-03T00:38:45.2505339Z Package 'php-datto-json-rpc' is not installed, so not removed
2026-05-03T00:38:45.2505776Z Package 'php-datto-json-rpc-http' is not installed, so not removed
2026-05-03T00:38:45.2506177Z Package 'php-db' is not installed, so not removed
2026-05-03T00:38:45.2506558Z Package 'php-deepcopy' is not installed, so not removed
2026-05-03T00:38:45.2506995Z Package 'php-dflydev-dot-access-data' is not installed, so not removed
2026-05-03T00:38:45.2507425Z Package 'php-di' is not installed, so not removed
2026-05-03T00:38:45.2507807Z Package 'php-psr-container' is not installed, so not removed
2026-05-03T00:38:45.2508213Z Package 'php-di-invoker' is not installed, so not removed
2026-05-03T00:38:45.2508805Z Package 'php-laravel-serializable-closure' is not installed, so not removed
2026-05-03T00:38:45.2509297Z Package 'php-directory-scanner' is not installed, so not removed
2026-05-03T00:38:45.2509701Z Package 'php-doc' is not installed, so not removed
2026-05-03T00:38:45.2510111Z Package 'php-doctrine-annotations' is not installed, so not removed
2026-05-03T00:38:45.2510557Z Package 'php-doctrine-lexer' is not installed, so not removed
2026-05-03T00:38:45.2510968Z Package 'php-doctrine-cache' is not installed, so not removed
2026-05-03T00:38:45.2511433Z Package 'php-doctrine-collections' is not installed, so not removed
2026-05-03T00:38:45.2511895Z Package 'php-doctrine-deprecations' is not installed, so not removed
2026-05-03T00:38:45.2512498Z Package 'php-doctrine-common' is not installed, so not removed
2026-05-03T00:38:45.2513111Z Package 'php-doctrine-persistence' is not installed, so not removed
2026-05-03T00:38:45.2513605Z Package 'php-doctrine-data-fixtures' is not installed, so not removed
2026-05-03T00:38:45.2514061Z Package 'php-doctrine-dbal' is not installed, so not removed
2026-05-03T00:38:45.2514482Z Package 'php-doctrine-orm' is not installed, so not removed
2026-05-03T00:38:45.2514934Z Package 'php-doctrine-event-manager' is not installed, so not removed
2026-05-03T00:38:45.2515398Z Package 'php-doctrine-inflector' is not installed, so not removed
2026-05-03T00:38:45.2515871Z Package 'php-doctrine-instantiator' is not installed, so not removed
2026-05-03T00:38:45.2516320Z Package 'php-symfony-cache' is not installed, so not removed
2026-05-03T00:38:45.2516748Z Package 'php-symfony-yaml' is not installed, so not removed
2026-05-03T00:38:45.2517233Z Package 'php-dragonmantank-cron-expression' is not installed, so not removed
2026-05-03T00:38:45.2517750Z Package 'php-webmozart-assert' is not installed, so not removed
2026-05-03T00:38:45.2518167Z Package 'php8.3-ds' is not installed, so not removed
2026-05-03T00:38:45.2518653Z Package 'php-ds-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2519046Z Package 'php-easyrdf' is not installed, so not removed
2026-05-03T00:38:45.2519428Z Package 'php-ml-json-ld' is not installed, so not removed
2026-05-03T00:38:45.2519831Z Package 'php-eluceo-ical' is not installed, so not removed
2026-05-03T00:38:45.2520247Z Package 'php-email-validator' is not installed, so not removed
2026-05-03T00:38:45.2520651Z Package 'php-embed' is not installed, so not removed
2026-05-03T00:38:45.2521089Z Package 'php-oscarotero-html-parser' is not installed, so not removed
2026-05-03T00:38:45.2521552Z Package 'php-psr-http-message' is not installed, so not removed
2026-05-03T00:38:45.2521991Z Package 'php-psr-http-client' is not installed, so not removed
2026-05-03T00:38:45.2522419Z Package 'php-psr-http-factory' is not installed, so not removed
2026-05-03T00:38:45.2522872Z Package 'php-symfony-css-selector' is not installed, so not removed
2026-05-03T00:38:45.2523297Z Package 'php-enchant' is not installed, so not removed
2026-05-03T00:38:45.2523676Z Package 'php-excimer' is not installed, so not removed
2026-05-03T00:38:45.2524065Z Package 'php8.3-facedetect' is not installed, so not removed
2026-05-03T00:38:45.2524500Z Package 'php-facedetect-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2524908Z Package 'php-faker' is not installed, so not removed
2026-05-03T00:38:45.2525303Z Package 'php-fdomdocument' is not installed, so not removed
2026-05-03T00:38:45.2525768Z Package 'php-fig-http-message-util' is not installed, so not removed
2026-05-03T00:38:45.2526220Z Package 'php-fig-link-util' is not installed, so not removed
2026-05-03T00:38:45.2526632Z Package 'php-psr-link' is not installed, so not removed
2026-05-03T00:38:45.2527021Z Package 'php-font-lib' is not installed, so not removed
2026-05-03T00:38:45.2527448Z Package 'php-fruitcake-php-cors' is not installed, so not removed
2026-05-03T00:38:45.2527943Z Package 'php-symfony-http-foundation' is not installed, so not removed
2026-05-03T00:38:45.2528378Z Package 'php-fxsl' is not installed, so not removed
2026-05-03T00:38:45.2528888Z Package 'php8.3-gearman' is not installed, so not removed
2026-05-03T00:38:45.2529303Z Package 'php-gearman-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2529726Z Package 'php-getallheaders' is not installed, so not removed
2026-05-03T00:38:45.2530117Z Package 'php-getid3' is not installed, so not removed
2026-05-03T00:38:45.2530531Z Package 'php-gettext-languages' is not installed, so not removed
2026-05-03T00:38:45.2530982Z Package 'php-oscarotero-gettext' is not installed, so not removed
2026-05-03T00:38:45.2531448Z Package 'php-giggsey-libphonenumber' is not installed, so not removed
2026-05-03T00:38:45.2531907Z Package 'php-giggsey-locale' is not installed, so not removed
2026-05-03T00:38:45.2532465Z Package 'php8.3-gmagick' is not installed, so not removed
2026-05-03T00:38:45.2532995Z Package 'php-gmagick-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2533400Z Package 'php8.3-gnupg' is not installed, so not removed
2026-05-03T00:38:45.2533802Z Package 'php-gnupg-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2534222Z Package 'php-google-protobuf' is not installed, so not removed
2026-05-03T00:38:45.2534648Z Package 'php-google-recaptcha' is not installed, so not removed
2026-05-03T00:38:45.2535133Z Package 'php-graham-campbell-result-type' is not installed, so not removed
2026-05-03T00:38:45.2535600Z Package 'php-phpoption' is not installed, so not removed
2026-05-03T00:38:45.2536019Z Package 'php-gregwar-captcha' is not installed, so not removed
2026-05-03T00:38:45.2536415Z Package 'php-guestfs' is not installed, so not removed
2026-05-03T00:38:45.2536827Z Package 'php-guzzlehttp-guzzle' is not installed, so not removed
2026-05-03T00:38:45.2537292Z Package 'php-guzzlehttp-promises' is not installed, so not removed
2026-05-03T00:38:45.2537730Z Package 'php-guzzlehttp-psr7' is not installed, so not removed
2026-05-03T00:38:45.2538148Z Package 'php-hamcrest' is not installed, so not removed
2026-05-03T00:38:45.2538673Z Package 'php-htmlawed' is not installed, so not removed
2026-05-03T00:38:45.2539074Z Package 'php-htmlpurifier' is not installed, so not removed
2026-05-03T00:38:45.2539458Z Package 'php-http' is not installed, so not removed
2026-05-03T00:38:45.2539833Z Package 'php8.3-http' is not installed, so not removed
2026-05-03T00:38:45.2540219Z Package 'php-http-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2540635Z Package 'php-http-httplug' is not installed, so not removed
2026-05-03T00:38:45.2541042Z Package 'php-http-promise' is not installed, so not removed
2026-05-03T00:38:45.2541527Z Package 'php-http-interop-http-factory-tests' is not installed, so not removed
2026-05-03T00:38:45.2542063Z Package 'php-http-message-factory' is not installed, so not removed
2026-05-03T00:38:45.2542553Z Package 'php-http-psr7-integration-tests' is not installed, so not removed
2026-05-03T00:38:45.2543047Z Package 'php-http-webdav-server' is not installed, so not removed
2026-05-03T00:38:45.2543458Z Package 'php-httpful' is not installed, so not removed
2026-05-03T00:38:45.2543872Z Package 'php-igbinary-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2544297Z Package 'php-image-text' is not installed, so not removed
2026-05-03T00:38:45.2544706Z Package 'php-imagick-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2545119Z Package 'php-interbase' is not installed, so not removed
2026-05-03T00:38:45.2545495Z Package 'php-invoker' is not installed, so not removed
2026-05-03T00:38:45.2545868Z Package 'php-jshrink' is not installed, so not removed
2026-05-03T00:38:45.2546265Z Package 'php-kissifrot-php-ixr' is not installed, so not removed
2026-05-03T00:38:45.2546671Z Package 'php-klogger' is not installed, so not removed
2026-05-03T00:38:45.2547074Z Package 'php-lcobucci-clock' is not installed, so not removed
2026-05-03T00:38:45.2547483Z Package 'php-psr-clock' is not installed, so not removed
2026-05-03T00:38:45.2547881Z Package 'php-lcobucci-jwt' is not installed, so not removed
2026-05-03T00:38:45.2548295Z Package 'php-league-commonmark' is not installed, so not removed
2026-05-03T00:38:45.2548839Z Package 'php-league-config' is not installed, so not removed
2026-05-03T00:38:45.2549274Z Package 'php-psr-event-dispatcher' is not installed, so not removed
2026-05-03T00:38:45.2549711Z Package 'php-nette-schema' is not installed, so not removed
2026-05-03T00:38:45.2550118Z Package 'php-league-csv' is not installed, so not removed
2026-05-03T00:38:45.2550524Z Package 'php-league-flysystem' is not installed, so not removed
2026-05-03T00:38:45.2551000Z Package 'php-league-mime-type-detection' is not installed, so not removed
2026-05-03T00:38:45.2551499Z Package 'php-league-html-to-markdown' is not installed, so not removed
2026-05-03T00:38:45.2552111Z Package 'php-league-uri' is not installed, so not removed
2026-05-03T00:38:45.2552655Z Package 'php-league-uri-interfaces' is not installed, so not removed
2026-05-03T00:38:45.2553130Z Package 'php-league-uri-components' is not installed, so not removed
2026-05-03T00:38:45.2553565Z Package 'php-letodms-core' is not installed, so not removed
2026-05-03T00:38:45.2554001Z Package 'php-libvirt-php-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2554425Z Package 'php-log' is not installed, so not removed
2026-05-03T00:38:45.2554796Z Package 'php-mdb2' is not installed, so not removed
2026-05-03T00:38:45.2555162Z Package 'php-mail' is not installed, so not removed
2026-05-03T00:38:45.2555540Z Package 'php-lorenzo-pinky' is not installed, so not removed
2026-05-03T00:38:45.2555939Z Package 'php-net-smtp' is not installed, so not removed
2026-05-03T00:38:45.2556340Z Package 'php-mail-mime' is not installed, so not removed
2026-05-03T00:38:45.2556768Z Package 'php8.3-mailparse' is not installed, so not removed
2026-05-03T00:38:45.2557209Z Package 'php-mailparse-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2557654Z Package 'php-malkusch-lock' is not installed, so not removed
2026-05-03T00:38:45.2558059Z Package 'php-predis' is not installed, so not removed
2026-05-03T00:38:45.2558563Z Package 'php-mariadb-mysql-kbs' is not installed, so not removed
2026-05-03T00:38:45.2559014Z Package 'php-masterminds-html5' is not installed, so not removed
2026-05-03T00:38:45.2559478Z Package 'php-matthiasmullie-minify' is not installed, so not removed
2026-05-03T00:38:45.2560013Z Package 'php-matthiasmullie-path-converter' is not installed, so not removed
2026-05-03T00:38:45.2560557Z Package 'php-maxmind-web-service-common' is not installed, so not removed
2026-05-03T00:38:45.2561007Z Package 'php-maxminddb' is not installed, so not removed
2026-05-03T00:38:45.2561414Z Package 'php8.3-maxminddb' is not installed, so not removed
2026-05-03T00:38:45.2561843Z Package 'php-maxminddb-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2562260Z Package 'php8.3-mcrypt' is not installed, so not removed
2026-05-03T00:38:45.2562676Z Package 'php-mcrypt-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2563108Z Package 'php-mdb2-driver-mysql' is not installed, so not removed
2026-05-03T00:38:45.2563660Z Package 'php-mdb2-driver-pgsql' is not installed, so not removed
2026-05-03T00:38:45.2564326Z Package 'php-memcache-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2564902Z Package 'php-memcached-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2565343Z Package 'php-msgpack-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2565747Z Package 'php-mf2' is not installed, so not removed
2026-05-03T00:38:45.2566156Z Package 'php-mikey179-vfsstream' is not installed, so not removed
2026-05-03T00:38:45.2566577Z Package 'php-ml-iri' is not installed, so not removed
2026-05-03T00:38:45.2566952Z Package 'php-mock' is not installed, so not removed
2026-05-03T00:38:45.2567352Z Package 'php-mock-phpunit' is not installed, so not removed
2026-05-03T00:38:45.2567789Z Package 'php-mock-integration' is not installed, so not removed
2026-05-03T00:38:45.2568199Z Package 'php-mockery' is not installed, so not removed
2026-05-03T00:38:45.2568722Z Package 'php-mockery-doc' is not installed, so not removed
2026-05-03T00:38:45.2569134Z Package 'php-mongodb-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2569541Z Package 'php-monolog' is not installed, so not removed
2026-05-03T00:38:45.2569917Z Package 'php-net-dime' is not installed, so not removed
2026-05-03T00:38:45.2570301Z Package 'php-net-dns2' is not installed, so not removed
2026-05-03T00:38:45.2570684Z Package 'php-net-ftp' is not installed, so not removed
2026-05-03T00:38:45.2571057Z Package 'php-net-imap' is not installed, so not removed
2026-05-03T00:38:45.2571434Z Package 'php-net-ipv6' is not installed, so not removed
2026-05-03T00:38:45.2571973Z Package 'php-net-ldap2' is not installed, so not removed
2026-05-03T00:38:45.2572371Z Package 'php-net-ldap3' is not installed, so not removed
2026-05-03T00:38:45.2572869Z Package 'php-net-nntp' is not installed, so not removed
2026-05-03T00:38:45.2573279Z Package 'php-net-publicsuffix' is not installed, so not removed
2026-05-03T00:38:45.2573695Z Package 'php-net-sieve' is not installed, so not removed
2026-05-03T00:38:45.2574064Z Package 'php-net-url' is not installed, so not removed
2026-05-03T00:38:45.2574439Z Package 'php-net-url2' is not installed, so not removed
2026-05-03T00:38:45.2574811Z Package 'php-net-whois' is not installed, so not removed
2026-05-03T00:38:45.2575263Z Package 'php-netscape-bookmark-parser' is not installed, so not removed
2026-05-03T00:38:45.2575718Z Package 'php-nette-utils' is not installed, so not removed
2026-05-03T00:38:45.2576145Z Package 'php-nikic-fast-route' is not installed, so not removed
2026-05-03T00:38:45.2576564Z Package 'php-nyholm-psr7' is not installed, so not removed
2026-05-03T00:38:45.2576960Z Package 'php8.3-oauth' is not installed, so not removed
2026-05-03T00:38:45.2577362Z Package 'php-oauth-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2577782Z Package 'php-opis-closure' is not installed, so not removed
2026-05-03T00:38:45.2578184Z Package 'php-parsedown' is not installed, so not removed
2026-05-03T00:38:45.2578689Z Package 'php-parsedown-extra' is not installed, so not removed
2026-05-03T00:38:45.2579111Z Package 'php-pcov-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2579529Z Package 'php-pda-pheanstalk' is not installed, so not removed
2026-05-03T00:38:45.2579963Z Package 'php-phar-io-manifest' is not installed, so not removed
2026-05-03T00:38:45.2580395Z Package 'php-phar-io-version' is not installed, so not removed
2026-05-03T00:38:45.2580802Z Package 'php-php-gettext' is not installed, so not removed
2026-05-03T00:38:45.2581197Z Package 'php-phpdbg' is not installed, so not removed
2026-05-03T00:38:45.2581660Z Package 'php-phpdocumentor-reflection-common' is not installed, so not removed
2026-05-03T00:38:45.2582245Z Package 'php-phpdocumentor-reflection-docblock' is not installed, so not removed
2026-05-03T00:38:45.2582803Z Package 'php-phpdocumentor-type-resolver' is not installed, so not removed
2026-05-03T00:38:45.2583320Z Package 'php-phpstan-phpdoc-parser' is not installed, so not removed
2026-05-03T00:38:45.2583823Z Package 'php-symfony-expression-language' is not installed, so not removed
2026-05-03T00:38:45.2584315Z Package 'php-phpmyadmin-shapefile' is not installed, so not removed
2026-05-03T00:38:45.2584797Z Package 'php-phpmyadmin-sql-parser' is not installed, so not removed
2026-05-03T00:38:45.2585280Z Package 'php-symfony-polyfill-php80' is not installed, so not removed
2026-05-03T00:38:45.2585717Z Package 'php-seclib' is not installed, so not removed
2026-05-03T00:38:45.2586103Z Package 'php-phpseclib3' is not installed, so not removed
2026-05-03T00:38:45.2586524Z Package 'php-phpspec-prophecy' is not installed, so not removed
2026-05-03T00:38:45.2586965Z Package 'phpunit-comparator' is not installed, so not removed
2026-05-03T00:38:45.2587411Z Package 'phpunit-recursion-context' is not installed, so not removed
2026-05-03T00:38:45.2587917Z Package 'php-phpspec-prophecy-phpunit' is not installed, so not removed
2026-05-03T00:38:45.2588357Z Package 'php-pinba' is not installed, so not removed
2026-05-03T00:38:45.2588849Z Package 'php8.3-pinba' is not installed, so not removed
2026-05-03T00:38:45.2589250Z Package 'php-pinba-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2589667Z Package 'php-proxy-manager' is not installed, so not removed
2026-05-03T00:38:45.2590055Z Package 'php8.3-ps' is not installed, so not removed
2026-05-03T00:38:45.2590435Z Package 'php-ps-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2590829Z Package 'php8.3-psr' is not installed, so not removed
2026-05-03T00:38:45.2591211Z Package 'php-psr-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2591786Z Package 'php-psr-simple-cache' is not installed, so not removed
2026-05-03T00:38:45.2592244Z Package 'php-pubsubhubbub-publisher' is not installed, so not removed
2026-05-03T00:38:45.2592830Z Package 'php-ramsey-collection' is not installed, so not removed
2026-05-03T00:38:45.2593256Z Package 'php-ramsey-uuid' is not installed, so not removed
2026-05-03T00:38:45.2593649Z Package 'php8.3-raphf' is not installed, so not removed
2026-05-03T00:38:45.2594047Z Package 'php-raphf-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2594448Z Package 'php-redis-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2594838Z Package 'php-remctl' is not installed, so not removed
2026-05-03T00:38:45.2595293Z Package 'php-roundcube-rtf-html-php' is not installed, so not removed
2026-05-03T00:38:45.2595726Z Package 'php8.3-rrd' is not installed, so not removed
2026-05-03T00:38:45.2596107Z Package 'php-rrd-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2596505Z Package 'php-sabre-dav' is not installed, so not removed
2026-05-03T00:38:45.2596915Z Package 'php-sabre-vobject' is not installed, so not removed
2026-05-03T00:38:45.2597292Z Package 'php-sass' is not installed, so not removed
2026-05-03T00:38:45.2597677Z Package 'php8.3-sass' is not installed, so not removed
2026-05-03T00:38:45.2598064Z Package 'php-sass-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2598591Z Package 'php-shellcommand' is not installed, so not removed
2026-05-03T00:38:45.2598980Z Package 'php-slim-psr7' is not installed, so not removed
2026-05-03T00:38:45.2599377Z Package 'php8.3-smbclient' is not installed, so not removed
2026-05-03T00:38:45.2599798Z Package 'php-smbclient-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2600193Z Package 'php-solr' is not installed, so not removed
2026-05-03T00:38:45.2600560Z Package 'php8.3-solr' is not installed, so not removed
2026-05-03T00:38:45.2600946Z Package 'php-solr-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2601341Z Package 'php-sparkline' is not installed, so not removed
2026-05-03T00:38:45.2601736Z Package 'php-sql-formatter' is not installed, so not removed
2026-05-03T00:38:45.2602132Z Package 'php8.3-ssh2' is not installed, so not removed
2026-05-03T00:38:45.2602520Z Package 'php-ssh2-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2602904Z Package 'php8.3-stomp' is not installed, so not removed
2026-05-03T00:38:45.2603295Z Package 'php-stomp-all-dev' is not installed, so not removed
2026-05-03T00:38:45.2603694Z Package 'php-swiftmailer' is not installed, so not removed
2026-05-03T00:38:45.2604080Z Package 'php-symfony' is not installed, so not removed
2026-05-03T00:38:45.2604459Z Package 'php-symfony-asset' is not installed, so not removed
2026-05-03T00:38:45.2604905Z Package 'php-symfony-asset-mapper' is not installed, so not removed
2026-05-03T00:38:45.2605389Z Package 'php-symfony-browser-kit' is not installed, so not removed
2026-05-03T00:38:45.2605842Z Package 'php-symfony-clock' is not installed, so not removed
2026-05-03T00:38:45.2606294Z Package 'php-symfony-debug-bundle' is not installed, so not removed
2026-05-03T00:38:45.2606773Z Package 'php-symfony-doctrine-bridge' is not installed, so not removed
2026-05-03T00:38:45.2607251Z Package 'php-symfony-dom-crawler' is not installed, so not removed
2026-05-03T00:38:45.2607687Z Package 'php-symfony-dotenv' is not installed, so not removed
2026-05-03T00:38:45.2608136Z Package 'php-symfony-error-handler' is not installed, so not removed
2026-05-03T00:38:45.2608734Z Package 'php-symfony-event-dispatcher' is not installed, so not removed
2026-05-03T00:38:45.2609194Z Package 'php-symfony-form' is not installed, so not removed
2026-05-03T00:38:45.2609641Z Package 'php-symfony-framework-bundle' is not installed, so not removed
2026-05-03T00:38:45.2610105Z Package 'php-symfony-http-kernel' is not installed, so not removed
2026-05-03T00:38:45.2610535Z Package 'php-symfony-intl' is not installed, so not removed
2026-05-03T00:38:45.2610931Z Package 'php-symfony-ldap' is not installed, so not removed
2026-05-03T00:38:45.2611474Z Package 'php-symfony-lock' is not installed, so not removed
2026-05-03T00:38:45.2611885Z Package 'php-symfony-mailer' is not installed, so not removed
2026-05-03T00:38:45.2612496Z Package 'php-symfony-messenger' is not installed, so not removed
2026-05-03T00:38:45.2612927Z Package 'php-symfony-mime' is not installed, so not removed
2026-05-03T00:38:45.2613375Z Package 'php-symfony-monolog-bridge' is not installed, so not removed
2026-05-03T00:38:45.2613845Z Package 'php-symfony-notifier' is not installed, so not removed
2026-05-03T00:38:45.2614315Z Package 'php-symfony-options-resolver' is not installed, so not removed
2026-05-03T00:38:45.2614827Z Package 'php-symfony-password-hasher' is not installed, so not removed
2026-05-03T00:38:45.2615317Z Package 'php-symfony-property-access' is not installed, so not removed
2026-05-03T00:38:45.2615805Z Package 'php-symfony-property-info' is not installed, so not removed
2026-05-03T00:38:45.2616315Z Package 'php-symfony-proxy-manager-bridge' is not installed, so not removed
2026-05-03T00:38:45.2616826Z Package 'php-symfony-rate-limiter' is not installed, so not removed
2026-05-03T00:38:45.2617304Z Package 'php-symfony-remote-event' is not installed, so not removed
2026-05-03T00:38:45.2617747Z Package 'php-symfony-routing' is not installed, so not removed
2026-05-03T00:38:45.2618185Z Package 'php-symfony-scheduler' is not installed, so not removed
2026-05-03T00:38:45.2618764Z Package 'php-symfony-security-bundle' is not installed, so not removed
2026-05-03T00:38:45.2619245Z Package 'php-symfony-security-core' is not installed, so not removed
2026-05-03T00:38:45.2619706Z Package 'php-symfony-security-csrf' is not installed, so not removed
2026-05-03T00:38:45.2620155Z Package 'php-symfony-security-http' is not installed, so not removed
2026-05-03T00:38:45.2620607Z Package 'php-symfony-semaphore' is not installed, so not removed
2026-05-03T00:38:45.2621050Z Package 'php-symfony-serializer' is not installed, so not removed
2026-05-03T00:38:45.2621508Z Package 'php-symfony-stopwatch' is not installed, so not removed
2026-05-03T00:38:45.2621933Z Package 'php-symfony-string' is not installed, so not removed
2026-05-03T00:38:45.2622373Z Package 'php-symfony-templating' is not installed, so not removed
2026-05-03T00:38:45.2622828Z Package 'php-symfony-translation' is not installed, so not removed
2026-05-03T00:38:45.2623278Z Package 'php-symfony-twig-bridge' is not installed, so not removed
2026-05-03T00:38:45.2623729Z Package 'php-symfony-twig-bundle' is not installed, so not removed
2026-05-03T00:38:45.2624146Z Package 'php-symfony-uid' is not installed, so not removed
2026-05-03T00:38:45.2624580Z Package 'php-symfony-validator' is not installed, so not removed
2026-05-03T00:38:45.2625012Z Package 'php-symfony-var-dumper' is not installed, so not removed
2026-05-03T00:38:45.2625462Z Package 'php-symfony-var-exporter' is not installed, so not removed
2026-05-03T00:38:45.2625911Z Package 'php-symfony-web-link' is not installed, so not removed
2026-05-03T00:38:45.2626393Z Package 'php-symfony-web-profiler-bundle' is not installed, so not removed
2026-05-03T00:38:45.2626875Z Package 'php-symfony-webhook' is not installed, so not removed
2026-05-03T00:38:45.2627302Z Package 'php-symfony-workflow' is not installed, so not removed
2026-05-03T00:38:45.2627735Z Package 'php-symfony-contracts' is not installed, so not removed
2026-05-03T00:38:45.2628189Z Package 'php-symfony-polyfill-php83' is not installed, so not removed
2026-05-03T00:38:45.2628797Z Package 'php-symfony-all-my-sms-notifier' is not installed, so not removed
2026-05-03T00:38:45.2629294Z Package 'php-symfony-amazon-mailer' is not installed, so not removed
2026-05-03T00:38:45.2629771Z Package 'php-symfony-amazon-sns-notifier' is not installed, so not removed
2026-05-03T00:38:45.2630287Z Package 'php-symfony-amazon-sqs-messenger' is not installed, so not removed
2026-05-03T00:38:45.2630783Z Package 'php-symfony-amqp-messenger' is not installed, so not removed
2026-05-03T00:38:45.2631431Z Package 'php-symfony-bandwidth-notifier' is not installed, so not removed
2026-05-03T00:38:45.2631949Z Package 'php-symfony-beanstalkd-messenger' is not installed, so not removed
2026-05-03T00:38:45.2632561Z Package 'php-symfony-brevo-mailer' is not installed, so not removed
2026-05-03T00:38:45.2633036Z Package 'php-symfony-brevo-notifier' is not installed, so not removed
2026-05-03T00:38:45.2633510Z Package 'php-symfony-cache-contracts' is not installed, so not removed
2026-05-03T00:38:45.2634006Z Package 'php-symfony-chatwork-notifier' is not installed, so not removed
2026-05-03T00:38:45.2634502Z Package 'php-symfony-click-send-notifier' is not installed, so not removed
2026-05-03T00:38:45.2635010Z Package 'php-symfony-clickatell-notifier' is not installed, so not removed
2026-05-03T00:38:45.2635551Z Package 'php-symfony-contact-everyone-notifier' is not installed, so not removed
2026-05-03T00:38:45.2636135Z Package 'php-symfony-event-dispatcher-contracts' is not installed, so not removed
2026-05-03T00:38:45.2636710Z Package 'php-symfony-translation-contracts' is not installed, so not removed
2026-05-03T00:38:45.2637273Z Package 'php-symfony-crowdin-translation-provider' is not installed, so not removed
2026-05-03T00:38:45.2637833Z Package 'php-symfony-discord-notifier' is not installed, so not removed
2026-05-03T00:38:45.2638332Z Package 'php-symfony-doctrine-messenger' is not installed, so not removed
2026-05-03T00:38:45.2639272Z Package 'php-symfony-engagespot-notifier' is not installed, so not removed
2026-05-03T00:38:45.2639782Z Package 'php-symfony-esendex-notifier' is not installed, so not removed
2026-05-03T00:38:45.2640263Z Package 'php-symfony-expo-notifier' is not installed, so not removed
2026-05-03T00:38:45.2640750Z Package 'php-symfony-fake-chat-notifier' is not installed, so not removed
2026-05-03T00:38:45.2641244Z Package 'php-symfony-fake-sms-notifier' is not installed, so not removed
2026-05-03T00:38:45.2641737Z Package 'php-symfony-firebase-notifier' is not installed, so not removed
2026-05-03T00:38:45.2642261Z Package 'php-symfony-forty-six-elks-notifier' is not installed, so not removed
2026-05-03T00:38:45.2642802Z Package 'php-symfony-free-mobile-notifier' is not installed, so not removed
2026-05-03T00:38:45.2643329Z Package 'php-symfony-gateway-api-notifier' is not installed, so not removed
2026-05-03T00:38:45.2643828Z Package 'php-symfony-gitter-notifier' is not installed, so not removed
2026-05-03T00:38:45.2644308Z Package 'php-symfony-go-ip-notifier' is not installed, so not removed
2026-05-03T00:38:45.2644799Z Package 'php-symfony-google-chat-notifier' is not installed, so not removed
2026-05-03T00:38:45.2645287Z Package 'php-symfony-google-mailer' is not installed, so not removed
2026-05-03T00:38:45.2645750Z Package 'php-symfony-html-sanitizer' is not installed, so not removed
2026-05-03T00:38:45.2646222Z Package 'php-symfony-infobip-mailer' is not installed, so not removed
2026-05-03T00:38:45.2646699Z Package 'php-symfony-infobip-notifier' is not installed, so not removed
2026-05-03T00:38:45.2647186Z Package 'php-symfony-iqsms-notifier' is not installed, so not removed
2026-05-03T00:38:45.2647670Z Package 'php-symfony-isendpro-notifier' is not installed, so not removed
2026-05-03T00:38:45.2648181Z Package 'php-symfony-kaz-info-teh-notifier' is not installed, so not removed
2026-05-03T00:38:45.2648844Z Package 'php-symfony-light-sms-notifier' is not installed, so not removed
2026-05-03T00:38:45.2649377Z Package 'php-symfony-line-notify-notifier' is not installed, so not removed
2026-05-03T00:38:45.2649899Z Package 'php-symfony-linked-in-notifier' is not installed, so not removed
2026-05-03T00:38:45.2650435Z Package 'php-symfony-loco-translation-provider' is not installed, so not removed
2026-05-03T00:38:45.2651027Z Package 'php-symfony-lokalise-translation-provider' is not installed, so not removed
2026-05-03T00:38:45.2651586Z Package 'php-symfony-mail-pace-mailer' is not installed, so not removed
2026-05-03T00:38:45.2652070Z Package 'php-symfony-mailchimp-mailer' is not installed, so not removed
2026-05-03T00:38:45.2652784Z Package 'php-symfony-mailer-send-mailer' is not installed, so not removed
2026-05-03T00:38:45.2653283Z Package 'php-symfony-mailgun-mailer' is not installed, so not removed
2026-05-03T00:38:45.2653872Z Package 'php-symfony-mailjet-mailer' is not installed, so not removed
2026-05-03T00:38:45.2654370Z Package 'php-symfony-mailjet-notifier' is not installed, so not removed
2026-05-03T00:38:45.2654861Z Package 'php-symfony-mastodon-notifier' is not installed, so not removed
2026-05-03T00:38:45.2655372Z Package 'php-symfony-mattermost-notifier' is not installed, so not removed
2026-05-03T00:38:45.2655848Z Package 'php-symfony-mercure' is not installed, so not removed
2026-05-03T00:38:45.2656308Z Package 'php-symfony-mercure-bundle' is not installed, so not removed
2026-05-03T00:38:45.2656797Z Package 'php-symfony-mercure-notifier' is not installed, so not removed
2026-05-03T00:38:45.2657299Z Package 'php-symfony-message-bird-notifier' is not installed, so not removed
2026-05-03T00:38:45.2657851Z Package 'php-symfony-message-media-notifier' is not installed, so not removed
2026-05-03T00:38:45.2658515Z Package 'php-symfony-microsoft-teams-notifier' is not installed, so not removed
2026-05-03T00:38:45.2659061Z Package 'php-symfony-mobyt-notifier' is not installed, so not removed
2026-05-03T00:38:45.2659534Z Package 'php-symfony-novu-notifier' is not installed, so not removed
2026-05-03T00:38:45.2659997Z Package 'php-symfony-ntfy-notifier' is not installed, so not removed
2026-05-03T00:38:45.2660477Z Package 'php-symfony-octopush-notifier' is not installed, so not removed
2026-05-03T00:38:45.2660964Z Package 'php-symfony-oh-my-smtp-mailer' is not installed, so not removed
2026-05-03T00:38:45.2661469Z Package 'php-symfony-one-signal-notifier' is not installed, so not removed
2026-05-03T00:38:45.2661975Z Package 'php-symfony-orange-sms-notifier' is not installed, so not removed
2026-05-03T00:38:45.2662483Z Package 'php-symfony-ovh-cloud-notifier' is not installed, so not removed
2026-05-03T00:38:45.2662992Z Package 'php-symfony-pager-duty-notifier' is not installed, so not removed
2026-05-03T00:38:45.2663488Z Package 'php-symfony-phpunit-bridge' is not installed, so not removed
2026-05-03T00:38:45.2664037Z Package 'php-symfony-phrase-translation-provider' is not installed, so not removed
2026-05-03T00:38:45.2664569Z Package 'php-symfony-plivo-notifier' is not installed, so not removed
2026-05-03T00:38:45.2665034Z Package 'php-symfony-polyfill' is not installed, so not removed
2026-05-03T00:38:45.2665491Z Package 'php-symfony-polyfill-apcu' is not installed, so not removed
2026-05-03T00:38:45.2665965Z Package 'php-symfony-polyfill-ctype' is not installed, so not removed
2026-05-03T00:38:45.2666430Z Package 'php-symfony-polyfill-php72' is not installed, so not removed
2026-05-03T00:38:45.2666903Z Package 'php-symfony-polyfill-php73' is not installed, so not removed
2026-05-03T00:38:45.2667373Z Package 'php-symfony-polyfill-php74' is not installed, so not removed
2026-05-03T00:38:45.2667851Z Package 'php-symfony-polyfill-php81' is not installed, so not removed
2026-05-03T00:38:45.2668320Z Package 'php-symfony-polyfill-php82' is not installed, so not removed
2026-05-03T00:38:45.2668885Z Package 'php-symfony-polyfill-iconv' is not installed, so not removed
2026-05-03T00:38:45.2669393Z Package 'php-symfony-polyfill-intl-grapheme' is not installed, so not removed
2026-05-03T00:38:45.2669924Z Package 'php-symfony-polyfill-intl-icu' is not installed, so not removed
2026-05-03T00:38:45.2670479Z Package 'php-symfony-polyfill-intl-messageformatter' is not installed, so not removed
2026-05-03T00:38:45.2671043Z Package 'php-symfony-polyfill-intl-idn' is not installed, so not removed
2026-05-03T00:38:45.2671560Z Package 'php-symfony-polyfill-intl-normalizer' is not installed, so not removed
2026-05-03T00:38:45.2672083Z Package 'php-symfony-polyfill-mbstring' is not installed, so not removed
2026-05-03T00:38:45.2672557Z Package 'php-symfony-polyfill-util' is not installed, so not removed
2026-05-03T00:38:45.2673191Z Package 'php-symfony-polyfill-xml' is not installed, so not removed
2026-05-03T00:38:45.2673662Z Package 'php-symfony-polyfill-uuid' is not installed, so not removed
2026-05-03T00:38:45.2674309Z Package 'php-symfony-postmark-mailer' is not installed, so not removed
2026-05-03T00:38:45.2674835Z Package 'php-symfony-psr-http-message-bridge' is not installed, so not removed
2026-05-03T00:38:45.2675353Z Package 'php-symfony-pushover-notifier' is not installed, so not removed
2026-05-03T00:38:45.2675839Z Package 'php-symfony-redis-messenger' is not installed, so not removed
2026-05-03T00:38:45.2676316Z Package 'php-symfony-redlink-notifier' is not installed, so not removed
2026-05-03T00:38:45.2676824Z Package 'php-symfony-ring-central-notifier' is not installed, so not removed
2026-05-03T00:38:45.2677353Z Package 'php-symfony-rocket-chat-notifier' is not installed, so not removed
2026-05-03T00:38:45.2677831Z Package 'php-symfony-runtime' is not installed, so not removed
2026-05-03T00:38:45.2678302Z Package 'php-symfony-scaleway-mailer' is not installed, so not removed
2026-05-03T00:38:45.2678872Z Package 'php-symfony-security-acl' is not installed, so not removed
2026-05-03T00:38:45.2679366Z Package 'php-symfony-sendberry-notifier' is not installed, so not removed
2026-05-03T00:38:45.2679859Z Package 'php-symfony-sendgrid-mailer' is not installed, so not removed
2026-05-03T00:38:45.2680346Z Package 'php-symfony-sendinblue-mailer' is not installed, so not removed
2026-05-03T00:38:45.2680854Z Package 'php-symfony-sendinblue-notifier' is not installed, so not removed
2026-05-03T00:38:45.2681369Z Package 'php-symfony-simple-textin-notifier' is not installed, so not removed
2026-05-03T00:38:45.2681877Z Package 'php-symfony-sinch-notifier' is not installed, so not removed
2026-05-03T00:38:45.2682342Z Package 'php-symfony-slack-notifier' is not installed, so not removed
2026-05-03T00:38:45.2682827Z Package 'php-symfony-sms-biuras-notifier' is not installed, so not removed
2026-05-03T00:38:45.2683322Z Package 'php-symfony-sms-factor-notifier' is not installed, so not removed
2026-05-03T00:38:45.2683816Z Package 'php-symfony-sms77-notifier' is not installed, so not removed
2026-05-03T00:38:45.2684301Z Package 'php-symfony-smsapi-notifier' is not installed, so not removed
2026-05-03T00:38:45.2684763Z Package 'php-symfony-smsc-notifier' is not installed, so not removed
2026-05-03T00:38:45.2685243Z Package 'php-symfony-smsmode-notifier' is not installed, so not removed
2026-05-03T00:38:45.2685724Z Package 'php-symfony-spot-hit-notifier' is not installed, so not removed
2026-05-03T00:38:45.2686213Z Package 'php-symfony-telegram-notifier' is not installed, so not removed
2026-05-03T00:38:45.2686690Z Package 'php-symfony-telnyx-notifier' is not installed, so not removed
2026-05-03T00:38:45.2687165Z Package 'php-symfony-termii-notifier' is not installed, so not removed
2026-05-03T00:38:45.2687657Z Package 'php-symfony-turbo-sms-notifier' is not installed, so not removed
2026-05-03T00:38:45.2688141Z Package 'php-symfony-twilio-notifier' is not installed, so not removed
2026-05-03T00:38:45.2688764Z Package 'php-symfony-twitter-notifier' is not installed, so not removed
2026-05-03T00:38:45.2689253Z Package 'php-symfony-vonage-notifier' is not installed, so not removed
2026-05-03T00:38:45.2689736Z Package 'php-symfony-yunpian-notifier' is not installed, so not removed
2026-05-03T00:38:45.2690227Z Package 'php-symfony-zendesk-notifier' is not installed, so not removed
2026-05-03T00:38:45.2690700Z Package 'php-symfony-zulip-notifier' is not installed, so not removed
2026-05-03T00:38:45.2691146Z Package 'php-text-captcha' is not installed, so not removed
2026-05-03T00:38:45.2691566Z Package 'php-text-password' is not installed, so not removed
2026-05-03T00:38:45.2691982Z Package 'php-text-figlet' is not installed, so not removed
2026-05-03T00:38:45.2692421Z Package 'php-text-languagedetect' is not installed, so not removed
2026-05-03T00:38:45.2692857Z Package 'php-text-wiki' is not installed, so not removed
2026-05-03T00:38:45.2693382Z Package 'php-thrift' is not installed, so not removed
2026-05-03T00:38:45.2693779Z Package 'php8.3-tideways' is not installed, so not removed
2026-05-03T00:38:45.2694320Z Package 'php-tideways-all-dev' is not installed, so not removed
2026-05-03T00:38:45.4550924Z Package 'php-tijsverkoyen-css-to-inline-styles' is not installed, so not removed
2026-05-03T00:38:45.4551885Z Package 'php-timer' is not installed, so not removed
2026-05-03T00:38:45.4552538Z Package 'php-twig-doc' is not installed, so not removed
2026-05-03T00:38:45.4553250Z Package 'php-twig-cache-extra' is not installed, so not removed
2026-05-03T00:38:45.4554040Z Package 'php-twig-cssinliner-extra' is not installed, so not removed
2026-05-03T00:38:45.4554973Z Package 'php-twig-extra-bundle' is not installed, so not removed
2026-05-03T00:38:45.4555780Z Package 'php-twig-html-extra' is not installed, so not removed
2026-05-03T00:38:45.4556616Z Package 'php-twig-i18n-extension' is not installed, so not removed
2026-05-03T00:38:45.4557394Z Package 'php-twig-inky-extra' is not installed, so not removed
2026-05-03T00:38:45.4558181Z Package 'php-twig-intl-extra' is not installed, so not removed
2026-05-03T00:38:45.4559170Z Package 'php-twig-markdown-extra' is not installed, so not removed
2026-05-03T00:38:45.4559947Z Package 'php-twig-string-extra' is not installed, so not removed
2026-05-03T00:38:45.4560651Z Package 'php8.3-uopz' is not installed, so not removed
2026-05-03T00:38:45.4561317Z Package 'php-uopz-all-dev' is not installed, so not removed
2026-05-03T00:38:45.4562018Z Package 'php8.3-uploadprogress' is not installed, so not removed
2026-05-03T00:38:45.4562838Z Package 'php-uploadprogress-all-dev' is not installed, so not removed
2026-05-03T00:38:45.4563592Z Package 'php8.3-uuid' is not installed, so not removed
2026-05-03T00:38:45.4564251Z Package 'php-uuid-all-dev' is not installed, so not removed
2026-05-03T00:38:45.4564890Z Package 'php-validate' is not installed, so not removed
2026-05-03T00:38:45.4565587Z Package 'php-vlucas-phpdotenv' is not installed, so not removed
2026-05-03T00:38:45.4566373Z Package 'php-voku-portable-ascii' is not installed, so not removed
2026-05-03T00:38:45.4567138Z Package 'php-wmerrors' is not installed, so not removed
2026-05-03T00:38:45.4567817Z Package 'php-xdebug-all-dev' is not installed, so not removed
2026-05-03T00:38:45.4568662Z Package 'php-xml-svg' is not installed, so not removed
2026-05-03T00:38:45.4569298Z Package 'php8.3-xmlrpc' is not installed, so not removed
2026-05-03T00:38:45.4569977Z Package 'php-xmlrpc-all-dev' is not installed, so not removed
2026-05-03T00:38:45.4570672Z Package 'php8.3-yac' is not installed, so not removed
2026-05-03T00:38:45.4571326Z Package 'php-yac-all-dev' is not installed, so not removed
2026-05-03T00:38:45.4572038Z Package 'php-yaml-all-dev' is not installed, so not removed
2026-05-03T00:38:45.4572694Z Package 'php-zend-code' is not installed, so not removed
2026-05-03T00:38:45.4573420Z Package 'php-zend-eventmanager' is not installed, so not removed
2026-05-03T00:38:45.4574196Z Package 'php-zend-stdlib' is not installed, so not removed
2026-05-03T00:38:45.4574853Z Package 'php-zeroc-ice' is not installed, so not removed
2026-05-03T00:38:45.4575504Z Package 'php-zeta-base' is not installed, so not removed
2026-05-03T00:38:45.4576195Z Package 'php-zeta-console-tools' is not installed, so not removed
2026-05-03T00:38:45.4576940Z Package 'php-zeta-unit-test' is not installed, so not removed
2026-05-03T00:38:45.4577587Z Package 'php-zmq-all-dev' is not installed, so not removed
2026-05-03T00:38:45.4578248Z Package 'php-zumba-json-serializer' is not installed, so not removed
2026-05-03T00:38:45.4579697Z Package 'php8.3-libvirt-php' is not installed, so not removed
2026-05-03T00:38:45.4580276Z Package 'phpab' is not installed, so not removed
2026-05-03T00:38:45.4580784Z Package 'phpcpd' is not installed, so not removed
2026-05-03T00:38:45.4581384Z Package 'phpunit-cli-parser' is not installed, so not removed
2026-05-03T00:38:45.4582008Z Package 'phpldapadmin' is not installed, so not removed
2026-05-03T00:38:45.4583059Z Package 'phpliteadmin' is not installed, so not removed
2026-05-03T00:38:45.4583725Z Package 'phpliteadmin-themes' is not installed, so not removed
2026-05-03T00:38:45.4584535Z Package 'phploc' is not installed, so not removed
2026-05-03T00:38:45.4585123Z Package 'phppgadmin' is not installed, so not removed
2026-05-03T00:38:45.4585699Z Package 'phpsysinfo' is not installed, so not removed
2026-05-03T00:38:45.4586350Z Package 'phpunit-code-unit' is not installed, so not removed
2026-05-03T00:38:45.4587031Z Package 'phpunit-diff' is not installed, so not removed
2026-05-03T00:38:45.4587688Z Package 'phpunit-exporter' is not installed, so not removed
2026-05-03T00:38:45.4588379Z Package 'phpunit-global-state' is not installed, so not removed
2026-05-03T00:38:45.4589333Z Package 'phpunit-object-enumerator' is not installed, so not removed
2026-05-03T00:38:45.4590141Z Package 'phpunit-resource-operations' is not installed, so not removed
2026-05-03T00:38:45.4590852Z Package 'phpunit-type' is not installed, so not removed
2026-05-03T00:38:45.4591521Z Package 'phpunit-object-reflector' is not installed, so not removed
2026-05-03T00:38:45.4592206Z Package 'phpwebcounter' is not installed, so not removed
2026-05-03T00:38:45.4592852Z Package 'phpwebcounter-extra' is not installed, so not removed
2026-05-03T00:38:45.4593486Z Package 'python3-phply' is not installed, so not removed
2026-05-03T00:38:45.4594119Z Package 'python3-phpserialize' is not installed, so not removed
2026-05-03T00:38:45.4594910Z Package 'python3-sphinxcontrib.phpdomain' is not installed, so not removed
2026-05-03T00:38:45.4595713Z Package 'simplesamlphp' is not installed, so not removed
2026-05-03T00:38:45.4596337Z Package 'slbackup-php' is not installed, so not removed
2026-05-03T00:38:45.4597040Z Package 'uwsgi-plugin-php' is not installed, so not removed
2026-05-03T00:38:45.4597687Z Package 'weechat-php' is not installed, so not removed
2026-05-03T00:38:45.4598291Z Package 'php-mythtv' is not installed, so not removed
2026-05-03T00:38:45.4599050Z Package 'mono-devel' is not installed, so not removed
2026-05-03T00:38:45.4599551Z The following packages will be REMOVED:
2026-05-03T00:38:45.4600122Z   azure-cli clang-16 clang-17 clang-18 clang-tidy-16 clang-tidy-17
2026-05-03T00:38:45.4600792Z   clang-tidy-18 clang-tools-16 clang-tools-17 clang-tools-18 firefox
2026-05-03T00:38:45.4601597Z   google-chrome-stable google-cloud-cli google-cloud-cli-anthoscli llvm-16
2026-05-03T00:38:45.4602404Z   llvm-16-dev llvm-16-linker-tools llvm-16-runtime llvm-16-tools llvm-17
2026-05-03T00:38:45.4603173Z   llvm-17-dev llvm-17-linker-tools llvm-17-runtime llvm-17-tools llvm-18
2026-05-03T00:38:45.4604009Z   llvm-18-dev llvm-18-linker-tools llvm-18-runtime llvm-18-tools php-common
2026-05-03T00:38:45.4604830Z   php-pear php8.3 php8.3-amqp php8.3-apcu php8.3-bcmath php8.3-bz2 php8.3-cgi
2026-05-03T00:38:45.4605565Z   php8.3-cli php8.3-common php8.3-curl php8.3-dba php8.3-dev php8.3-enchant
2026-05-03T00:38:45.4606298Z   php8.3-fpm php8.3-gd php8.3-gmp php8.3-igbinary php8.3-imagick php8.3-imap
2026-05-03T00:38:45.4607059Z   php8.3-interbase php8.3-intl php8.3-ldap php8.3-mbstring php8.3-memcache
2026-05-03T00:38:45.4607803Z   php8.3-memcached php8.3-mongodb php8.3-msgpack php8.3-mysql php8.3-odbc
2026-05-03T00:38:45.4608683Z   php8.3-opcache php8.3-pcov php8.3-pgsql php8.3-phpdbg php8.3-pspell
2026-05-03T00:38:45.4609361Z   php8.3-readline php8.3-redis php8.3-snmp php8.3-soap php8.3-sqlite3
2026-05-03T00:38:45.4610049Z   php8.3-sybase php8.3-tidy php8.3-xdebug php8.3-xml php8.3-xsl php8.3-yaml
2026-05-03T00:38:45.4610639Z   php8.3-zip php8.3-zmq powershell
2026-05-03T00:38:46.0679086Z 0 upgraded, 0 newly installed, 78 to remove and 5 not upgraded.
2026-05-03T00:38:46.0679819Z After this operation, 3857 MB disk space will be freed.
2026-05-03T00:38:46.1121300Z (Reading database ... 
2026-05-03T00:38:46.1121715Z (Reading database ... 5%
2026-05-03T00:38:46.1122045Z (Reading database ... 10%
2026-05-03T00:38:46.1122383Z (Reading database ... 15%
2026-05-03T00:38:46.1123108Z (Reading database ... 20%
2026-05-03T00:38:46.1123426Z (Reading database ... 25%
2026-05-03T00:38:46.1123760Z (Reading database ... 30%
2026-05-03T00:38:46.1124346Z (Reading database ... 35%
2026-05-03T00:38:46.1124801Z (Reading database ... 40%
2026-05-03T00:38:46.1125158Z (Reading database ... 45%
2026-05-03T00:38:46.1125615Z (Reading database ... 50%
2026-05-03T00:38:46.1210906Z (Reading database ... 55%
2026-05-03T00:38:46.2459962Z (Reading database ... 60%
2026-05-03T00:38:46.3854594Z (Reading database ... 65%
2026-05-03T00:38:46.5898637Z (Reading database ... 70%
2026-05-03T00:38:46.7933925Z (Reading database ... 75%
2026-05-03T00:38:46.9834700Z (Reading database ... 80%
2026-05-03T00:38:47.1430678Z (Reading database ... 85%
2026-05-03T00:38:47.2947416Z (Reading database ... 90%
2026-05-03T00:38:47.4462242Z (Reading database ... 95%
2026-05-03T00:38:47.4462702Z (Reading database ... 100%
2026-05-03T00:38:47.4463088Z (Reading database ... 220762 files and directories currently installed.)
2026-05-03T00:38:47.4515507Z Removing azure-cli (2.85.0-1~noble) ...
2026-05-03T00:38:49.4048754Z Removing clang-tidy-16 (1:16.0.6-23ubuntu4) ...
2026-05-03T00:38:49.4218676Z Removing clang-tools-16 (1:16.0.6-23ubuntu4) ...
2026-05-03T00:38:49.4484108Z Removing clang-16 (1:16.0.6-23ubuntu4) ...
2026-05-03T00:38:49.4640474Z Removing clang-tidy-17 (1:17.0.6-9ubuntu1) ...
2026-05-03T00:38:49.4804251Z Removing clang-tools-17 (1:17.0.6-9ubuntu1) ...
2026-05-03T00:38:49.5064554Z Removing clang-17 (1:17.0.6-9ubuntu1) ...
2026-05-03T00:38:49.5225798Z Removing clang-tidy-18 (1:18.1.3-1ubuntu1) ...
2026-05-03T00:38:49.5381628Z Removing clang-tools-18 (1:18.1.3-1ubuntu1) ...
2026-05-03T00:38:49.5632112Z Removing clang-18 (1:18.1.3-1ubuntu1) ...
2026-05-03T00:38:49.5803396Z Removing firefox (149.0.2+build1-0ubuntu0.24.04.1~mt1) ...
2026-05-03T00:38:49.6445394Z Removing google-chrome-stable (147.0.7727.55-1) ...
2026-05-03T00:38:49.8186189Z Removing google-cloud-cli-anthoscli (564.0.0-0) ...
2026-05-03T00:38:51.4769525Z Removing google-cloud-cli (564.0.0-0) ...
2026-05-03T00:40:00.6190950Z Removing llvm-16-dev (1:16.0.6-23ubuntu4) ...
2026-05-03T00:40:00.7494981Z Removing llvm-16 (1:16.0.6-23ubuntu4) ...
2026-05-03T00:40:00.7730228Z Removing llvm-16-linker-tools (1:16.0.6-23ubuntu4) ...
2026-05-03T00:40:00.7879341Z Removing llvm-16-runtime (1:16.0.6-23ubuntu4) ...
2026-05-03T00:40:00.8152418Z Removing llvm-16-tools (1:16.0.6-23ubuntu4) ...
2026-05-03T00:40:00.8702731Z Removing llvm-17-dev (1:17.0.6-9ubuntu1) ...
2026-05-03T00:40:00.9982723Z Removing llvm-17 (1:17.0.6-9ubuntu1) ...
2026-05-03T00:40:01.0222471Z Removing llvm-17-linker-tools (1:17.0.6-9ubuntu1) ...
2026-05-03T00:40:01.0375582Z Removing llvm-17-runtime (1:17.0.6-9ubuntu1) ...
2026-05-03T00:40:01.0695262Z Removing llvm-17-tools (1:17.0.6-9ubuntu1) ...
2026-05-03T00:40:01.1310534Z Removing llvm-18-dev (1:18.1.3-1ubuntu1) ...
2026-05-03T00:40:01.2740709Z Removing llvm-18 (1:18.1.3-1ubuntu1) ...
2026-05-03T00:40:01.2986187Z Removing llvm-18-linker-tools (1:18.1.3-1ubuntu1) ...
2026-05-03T00:40:01.3163186Z Removing llvm-18-runtime (1:18.1.3-1ubuntu1) ...
2026-05-03T00:40:01.3494027Z Removing llvm-18-tools (1:18.1.3-1ubuntu1) ...
2026-05-03T00:40:01.4114502Z Removing php8.3-zip (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:01.5611129Z Removing php8.3-sybase (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:01.6964694Z Removing php-pear (1:1.10.13+submodules+notgz+2022032202-2build1) ...
2026-05-03T00:40:01.7696894Z Removing php8.3 (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:01.7837647Z Removing php8.3-amqp (1.11.0-5ubuntu1) ...
2026-05-03T00:40:01.9196453Z Removing php8.3-apcu (5.1.22+4.0.11-2ubuntu1) ...
2026-05-03T00:40:02.0507628Z Removing php8.3-bcmath (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:02.1829656Z Removing php8.3-bz2 (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:02.3152859Z Removing php8.3-zmq (1.1.3-24ubuntu1) ...
2026-05-03T00:40:02.4535624Z Removing php8.3-yaml (2.2.2+2.1.0+2.0.4+1.3.2-6ubuntu1) ...
2026-05-03T00:40:02.5783393Z Removing php8.3-cgi (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:04.3610444Z apache2_invoke php8.3-cgi prerm: No action required
2026-05-03T00:40:04.3875373Z Removing php8.3-dev (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:04.4374460Z Removing php8.3-xdebug (3.2.0+3.1.6+2.9.8+2.8.1+2.5.5-3ubuntu1) ...
2026-05-03T00:40:04.5417389Z Removing php8.3-phpdbg (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:06.0619942Z Removing php8.3-redis (5.3.7+4.3.0-3ubuntu1) ...
2026-05-03T00:40:06.1479602Z Removing php8.3-xsl (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:06.1622568Z Removing php8.3-soap (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:06.2504036Z Removing php8.3-curl (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:06.3397469Z Removing php8.3-dba (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:06.4226533Z Removing php8.3-enchant (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:06.5054387Z Removing php8.3-pcov (1.0.11-5ubuntu1) ...
2026-05-03T00:40:06.5734143Z Removing php8.3-fpm (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:08.0131892Z apache2_invoke php8.3-fpm prerm: No action required
2026-05-03T00:40:08.0455687Z Removing php8.3-gd (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:08.1060632Z Removing php8.3-gmp (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:08.1720082Z Removing php8.3-memcached (3.2.0+2.2.0-4ubuntu3) ...
2026-05-03T00:40:08.2326478Z Removing php8.3-igbinary (3.2.13-1ubuntu3) ...
2026-05-03T00:40:08.2929690Z Removing php8.3-imagick (3.7.0-4ubuntu3) ...
2026-05-03T00:40:08.3538322Z Removing php8.3-imap (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:08.4141518Z Removing php8.3-interbase (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:08.4789975Z Removing php8.3-intl (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:08.5428864Z Removing php8.3-ldap (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:08.6036287Z Removing php8.3-mbstring (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:08.6679133Z Removing php8.3-memcache (8.0+4.0.5.2+3.0.9~20170802.e702b5f9+-8ubuntu1) ...
2026-05-03T00:40:08.7279292Z Removing php8.3-mongodb (1.15.0+1.11.1+1.9.2+1.7.5-1ubuntu3) ...
2026-05-03T00:40:08.7872767Z Removing php8.3-msgpack (1:2.2.0~rc2-3ubuntu1) ...
2026-05-03T00:40:08.8483027Z Removing php8.3-mysql (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:08.9805180Z Removing php8.3-odbc (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:09.0762636Z Removing php8.3-pgsql (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:09.1735323Z Removing php8.3-pspell (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:09.2353422Z Removing php8.3-snmp (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:09.3002503Z Removing php8.3-sqlite3 (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:09.3948284Z Removing php8.3-tidy (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:09.4552389Z Removing php8.3-xml (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:09.6887649Z Removing powershell (7.4.14-1.deb) ...
2026-05-03T00:40:09.8033884Z Removing php8.3-cli (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:10.3560281Z Removing php8.3-opcache (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:10.3908072Z Removing php8.3-readline (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:10.4291647Z Removing php8.3-common (8.3.6-0ubuntu0.24.04.8) ...
2026-05-03T00:40:10.6074519Z Removing php-common (2:93ubuntu2) ...
2026-05-03T00:40:10.6365145Z Stopping 'phpsessionclean.service', but its triggering units are still active:
2026-05-03T00:40:10.6365739Z 
2026-05-03T00:40:10.6365876Z phpsessionclean.timer
2026-05-03T00:40:10.6366093Z 
2026-05-03T00:40:11.2397166Z Processing triggers for libc-bin (2.39-0ubuntu8.7) ...
2026-05-03T00:40:11.2662836Z Processing triggers for systemd (255.4-1ubuntu8.15) ...
2026-05-03T00:40:11.2946540Z Processing triggers for man-db (2.12.0-4build2) ...
2026-05-03T00:40:11.2964886Z Not building database; man-db/auto-update is not 'true'.
2026-05-03T00:40:11.2977209Z Processing triggers for hicolor-icon-theme (0.17-2) ...
2026-05-03T00:40:12.4520002Z Reading package lists...
2026-05-03T00:40:12.6472498Z Building dependency tree...
2026-05-03T00:40:12.6479934Z Reading state information...
2026-05-03T00:40:12.8185725Z The following packages will be REMOVED:
2026-05-03T00:40:12.8186583Z   dictionaries-common emacsen-common firebird3.0-common firebird3.0-common-doc
2026-05-03T00:40:12.8187934Z   freetds-common hunspell-en-us icu-devtools imagemagick-6-common lib32gcc-s1
2026-05-03T00:40:12.8189137Z   lib32stdc++6 libaom3 libaspell15 libc-client2007e libc6-i386 libcanberra0t64
2026-05-03T00:40:12.8190034Z   libclang-common-16-dev libclang-common-17-dev libclang-common-18-dev
2026-05-03T00:40:12.8190924Z   libclang-rt-16-dev libclang-rt-17-dev libclang-rt-18-dev libclang1-16t64
2026-05-03T00:40:12.8191754Z   libclang1-17t64 libdbusmenu-glib4 libdbusmenu-gtk3-4 libde265-0
2026-05-03T00:40:12.8192547Z   libenchant-2-2 libfbclient2 libffi-dev libfftw3-double3 libgc1 libgd3
2026-05-03T00:40:12.8193380Z   libhashkit2t64 libheif-plugin-aomdec libheif-plugin-libde265 libheif1
2026-05-03T00:40:12.8194196Z   libhunspell-1.7-0 libicu-dev liblldb-16t64 liblldb-17t64 liblqr-1-0
2026-05-03T00:40:12.8194997Z   libmagickcore-6.q16-7t64 libmagickwand-6.q16-7t64 libmemcached11t64
2026-05-03T00:40:12.8195852Z   libncurses-dev libnorm1t64 libobjc-13-dev libobjc4 libogg0 libopenjp2-7
2026-05-03T00:40:12.8196661Z   libpcre2-16-0 libpcre2-32-0 libpcre2-dev libpcre2-posix3 libpfm4
2026-05-03T00:40:12.8197560Z   libpgm-5.3-0t64 libqdbm14t64 librabbitmq4 libraw23t64 libsnappy1v5 libsybdb5
2026-05-03T00:40:12.8198662Z   libtdb1 libtidy5deb1 libtommath1 libvorbis0a libvorbisfile3 libwebpdemux2
2026-05-03T00:40:12.8199582Z   libwebpmux3 libxml2-dev libz3-4 libz3-dev libzip4t64 libzmq5 mlock shtool
2026-05-03T00:40:12.8200286Z   sound-theme-freedesktop xul-ext-ubufox
2026-05-03T00:40:13.0520205Z 0 upgraded, 0 newly installed, 77 to remove and 5 not upgraded.
2026-05-03T00:40:13.0520663Z After this operation, 389 MB disk space will be freed.
2026-05-03T00:40:13.0691434Z (Reading database ... 
2026-05-03T00:40:13.0691824Z (Reading database ... 5%
2026-05-03T00:40:13.0692579Z (Reading database ... 10%
2026-05-03T00:40:13.0692993Z (Reading database ... 15%
2026-05-03T00:40:13.0693355Z (Reading database ... 20%
2026-05-03T00:40:13.0693668Z (Reading database ... 25%
2026-05-03T00:40:13.0693967Z (Reading database ... 30%
2026-05-03T00:40:13.0694272Z (Reading database ... 35%
2026-05-03T00:40:13.0694591Z (Reading database ... 40%
2026-05-03T00:40:13.0694895Z (Reading database ... 45%
2026-05-03T00:40:13.0695180Z (Reading database ... 50%
2026-05-03T00:40:13.0695383Z (Reading database ... 55%
2026-05-03T00:40:13.0730908Z (Reading database ... 60%
2026-05-03T00:40:13.0823958Z (Reading database ... 65%
2026-05-03T00:40:13.0847938Z (Reading database ... 70%
2026-05-03T00:40:13.0895142Z (Reading database ... 75%
2026-05-03T00:40:13.0917376Z (Reading database ... 80%
2026-05-03T00:40:13.0943909Z (Reading database ... 85%
2026-05-03T00:40:13.0970499Z (Reading database ... 90%
2026-05-03T00:40:13.1075159Z (Reading database ... 95%
2026-05-03T00:40:13.1075533Z (Reading database ... 100%
2026-05-03T00:40:13.1076040Z (Reading database ... 122759 files and directories currently installed.)
2026-05-03T00:40:13.1097876Z Removing libenchant-2-2:amd64 (2.3.3-2build2) ...
2026-05-03T00:40:13.1217667Z Removing hunspell-en-us (1:2020.12.07-2) ...
2026-05-03T00:40:13.1722503Z Removing dictionaries-common (1.29.7) ...
2026-05-03T00:40:13.2148374Z Removing 'diversion of /usr/share/dict/words to /usr/share/dict/words.pre-dictionaries-common by dictionaries-common'
2026-05-03T00:40:13.2307835Z Removing emacsen-common (3.0.5) ...
2026-05-03T00:40:13.2714612Z Removing libfbclient2:amd64 (3.0.11.33703.ds4-2ubuntu2) ...
2026-05-03T00:40:13.2842761Z Removing firebird3.0-common (3.0.11.33703.ds4-2ubuntu2) ...
2026-05-03T00:40:13.3047190Z Removing firebird3.0-common-doc (3.0.11.33703.ds4-2ubuntu2) ...
2026-05-03T00:40:13.3160133Z Removing libsybdb5:amd64 (1.3.17+ds-2build3) ...
2026-05-03T00:40:13.3272463Z Removing freetds-common (1.3.17+ds-2build3) ...
2026-05-03T00:40:13.3488847Z Removing libxml2-dev:amd64 (2.9.14+dfsg-1.3ubuntu3.7) ...
2026-05-03T00:40:13.3628537Z Removing libicu-dev:amd64 (74.2-1ubuntu3.1) ...
2026-05-03T00:40:13.3845292Z Removing icu-devtools (74.2-1ubuntu3.1) ...
2026-05-03T00:40:13.3961855Z Removing libmagickwand-6.q16-7t64:amd64 (8:6.9.12.98+dfsg1-5.2build2) ...
2026-05-03T00:40:13.4163844Z Removing libmagickcore-6.q16-7t64:amd64 (8:6.9.12.98+dfsg1-5.2build2) ...
2026-05-03T00:40:13.4516223Z Removing imagemagick-6-common (8:6.9.12.98+dfsg1-5.2build2) ...
2026-05-03T00:40:13.4620714Z Removing libclang-rt-18-dev:amd64 (1:18.1.3-1ubuntu1) ...
2026-05-03T00:40:13.4791177Z Removing libclang-rt-16-dev:amd64 (1:16.0.6-23ubuntu4) ...
2026-05-03T00:40:13.4993418Z Removing lib32stdc++6 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:13.5108281Z Removing lib32gcc-s1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:13.5233871Z Removing libaspell15:amd64 (0.60.8.1-1build1) ...
2026-05-03T00:40:13.5388264Z Removing libc-client2007e (8:2007f~dfsg-7build3) ...
2026-05-03T00:40:13.5531818Z Removing libc6-i386 (2.39-0ubuntu8.7) ...
2026-05-03T00:40:13.5838942Z Removing libcanberra0t64:amd64 (0.30-10ubuntu10) ...
2026-05-03T00:40:13.5953336Z Removing libclang-common-16-dev (1:16.0.6-23ubuntu4) ...
2026-05-03T00:40:13.6164388Z Removing libclang-common-17-dev:amd64 (1:17.0.6-9ubuntu1) ...
2026-05-03T00:40:13.6414832Z Removing libclang-common-18-dev:amd64 (1:18.1.3-1ubuntu1) ...
2026-05-03T00:40:13.6642088Z Removing libclang-rt-17-dev:amd64 (1:17.0.6-9ubuntu1) ...
2026-05-03T00:40:13.6796181Z Removing libclang1-16t64 (1:16.0.6-23ubuntu4) ...
2026-05-03T00:40:13.6920539Z Removing libclang1-17t64 (1:17.0.6-9ubuntu1) ...
2026-05-03T00:40:13.7029675Z Removing libdbusmenu-gtk3-4:amd64 (18.10.20180917~bzr492+repack1-3.1ubuntu5) ...
2026-05-03T00:40:13.7139012Z Removing libdbusmenu-glib4:amd64 (18.10.20180917~bzr492+repack1-3.1ubuntu5) ...
2026-05-03T00:40:13.7289062Z Removing libffi-dev:amd64 (3.4.6-1build1) ...
2026-05-03T00:40:13.7433184Z Removing libfftw3-double3:amd64 (3.3.10-1ubuntu3) ...
2026-05-03T00:40:13.7587777Z Removing libobjc-13-dev:amd64 (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T00:40:13.7709942Z Removing libobjc4:amd64 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:13.7819034Z Removing libgc1:amd64 (1:8.2.6-1build1) ...
2026-05-03T00:40:13.7930269Z Removing libgd3:amd64 (2.3.3-9ubuntu5) ...
2026-05-03T00:40:13.8144725Z Removing libmemcached11t64:amd64 (1.1.4-1.1build3) ...
2026-05-03T00:40:13.8255638Z Removing libhashkit2t64:amd64 (1.1.4-1.1build3) ...
2026-05-03T00:40:13.8360141Z Removing libhunspell-1.7-0:amd64 (1.7.2+really1.7.2-10build3) ...
2026-05-03T00:40:13.8471077Z Removing liblldb-16t64 (1:16.0.6-23ubuntu4) ...
2026-05-03T00:40:13.8576654Z Removing liblldb-17t64 (1:17.0.6-9ubuntu1) ...
2026-05-03T00:40:13.8684013Z Removing liblqr-1-0:amd64 (0.4.2-2.1build2) ...
2026-05-03T00:40:13.8793284Z Removing libncurses-dev:amd64 (6.4+20240113-1ubuntu2) ...
2026-05-03T00:40:13.8945065Z Removing libzmq5:amd64 (4.3.5-1build2) ...
2026-05-03T00:40:13.9053296Z Removing libnorm1t64:amd64 (1.5.9+dfsg-3.1build1) ...
2026-05-03T00:40:13.9159204Z Removing libvorbisfile3:amd64 (1.3.7-1build3) ...
2026-05-03T00:40:13.9269077Z Removing libvorbis0a:amd64 (1.3.7-1build3) ...
2026-05-03T00:40:13.9397094Z Removing libogg0:amd64 (1.3.5-3build1) ...
2026-05-03T00:40:13.9513938Z Removing libopenjp2-7:amd64 (2.5.0-2ubuntu0.4) ...
2026-05-03T00:40:13.9675378Z Removing libpcre2-dev:amd64 (10.42-4ubuntu2.1) ...
2026-05-03T00:40:13.9833437Z Removing libpcre2-16-0:amd64 (10.42-4ubuntu2.1) ...
2026-05-03T00:40:13.9949363Z Removing libpcre2-32-0:amd64 (10.42-4ubuntu2.1) ...
2026-05-03T00:40:14.0065755Z Removing libpcre2-posix3:amd64 (10.42-4ubuntu2.1) ...
2026-05-03T00:40:14.0220340Z Removing libpfm4:amd64 (4.13.0+git32-g0d4ed0e-1) ...
2026-05-03T00:40:14.0336954Z Removing libpgm-5.3-0t64:amd64 (5.3.128~dfsg-2.1build1) ...
2026-05-03T00:40:14.0455334Z Removing libqdbm14t64 (1.8.78-12.1build2) ...
2026-05-03T00:40:14.0609300Z Removing librabbitmq4:amd64 (0.11.0-1build2) ...
2026-05-03T00:40:14.0730000Z Removing libraw23t64:amd64 (0.21.2-2.1ubuntu0.24.04.1) ...
2026-05-03T00:40:14.0855235Z Removing libsnappy1v5:amd64 (1.1.10-1build1) ...
2026-05-03T00:40:14.0996785Z Removing libtdb1:amd64 (1.4.10-1build1) ...
2026-05-03T00:40:14.1122969Z Removing libtidy5deb1:amd64 (2:5.6.0-11ubuntu2) ...
2026-05-03T00:40:14.1237716Z Removing libtommath1:amd64 (1.2.1-2build1) ...
2026-05-03T00:40:14.1350479Z Removing libwebpdemux2:amd64 (1.3.2-0.4build3) ...
2026-05-03T00:40:14.1478733Z Removing libwebpmux3:amd64 (1.3.2-0.4build3) ...
2026-05-03T00:40:14.1597285Z Removing libz3-dev:amd64 (4.8.12-3.1build1) ...
2026-05-03T00:40:14.1722436Z Removing libz3-4:amd64 (4.8.12-3.1build1) ...
2026-05-03T00:40:14.1832900Z Removing libzip4t64:amd64 (1.7.3-1.1ubuntu2) ...
2026-05-03T00:40:14.1960660Z Removing mlock (8:2007f~dfsg-7build3) ...
2026-05-03T00:40:14.2065520Z Removing shtool (2.0.8-10) ...
2026-05-03T00:40:14.2194858Z Removing sound-theme-freedesktop (0.8-2ubuntu1) ...
2026-05-03T00:40:14.2319449Z Removing xul-ext-ubufox (3.4-0ubuntu1.17.10.4) ...
2026-05-03T00:40:14.2775962Z Removing libheif1:amd64 (1.17.6-1ubuntu4.2) ...
2026-05-03T00:40:14.2899942Z Removing libheif-plugin-libde265:amd64 (1.17.6-1ubuntu4.2) ...
2026-05-03T00:40:14.3016536Z Removing libde265-0:amd64 (1.0.15-1build3) ...
2026-05-03T00:40:14.3152603Z Removing libheif-plugin-aomdec:amd64 (1.17.6-1ubuntu4.2) ...
2026-05-03T00:40:14.3255098Z Removing libaom3:amd64 (3.8.2-2ubuntu0.1) ...
2026-05-03T00:40:14.3532090Z Processing triggers for man-db (2.12.0-4build2) ...
2026-05-03T00:40:14.3547166Z Not building database; man-db/auto-update is not 'true'.
2026-05-03T00:40:14.3558943Z Processing triggers for postgresql-common (290.pgdg24.04+1) ...
2026-05-03T00:40:14.4678299Z Building PostgreSQL dictionaries from installed myspell/hunspell packages...
2026-05-03T00:40:14.4678951Z Removing obsolete dictionary files:
2026-05-03T00:40:14.4680812Z   /var/cache/postgresql/dicts/en_us.affix
2026-05-03T00:40:14.4681231Z   /var/cache/postgresql/dicts/en_us.dict
2026-05-03T00:40:14.4688232Z   /usr/share/postgresql/16/tsearch_data/en_us.affix
2026-05-03T00:40:14.4688822Z   /usr/share/postgresql/16/tsearch_data/en_us.dict
2026-05-03T00:40:14.4898956Z Processing triggers for install-info (7.1-3build2) ...
2026-05-03T00:40:14.7583468Z Processing triggers for libc-bin (2.39-0ubuntu8.7) ...
2026-05-03T00:40:15.7447427Z === After cleanup ===
2026-05-03T00:40:15.7459632Z Filesystem      Size  Used Avail Use% Mounted on
2026-05-03T00:40:15.7460086Z /dev/root       145G   25G  120G  17% /
2026-05-03T00:40:15.7502071Z ##[group]Run sudo swapoff /mnt/swapfile 2>/dev/null || true
2026-05-03T00:40:15.7502501Z [36;1msudo swapoff /mnt/swapfile 2>/dev/null || true[0m
2026-05-03T00:40:15.7502819Z [36;1msudo rm -f /mnt/swapfile[0m
2026-05-03T00:40:15.7503244Z [36;1msudo fallocate -l 16G /mnt/swapfile || sudo dd if=/dev/zero of=/mnt/swapfile bs=1M count=16384[0m
2026-05-03T00:40:15.7503690Z [36;1msudo chmod 600 /mnt/swapfile[0m
2026-05-03T00:40:15.7503939Z [36;1msudo mkswap /mnt/swapfile[0m
2026-05-03T00:40:15.7504179Z [36;1msudo swapon /mnt/swapfile[0m
2026-05-03T00:40:15.7504402Z [36;1mfree -h[0m
2026-05-03T00:40:15.7527758Z shell: /usr/bin/bash -e {0}
2026-05-03T00:40:15.7528015Z env:
2026-05-03T00:40:15.7528197Z   KERNEL_NAME: Castorice
2026-05-03T00:40:15.7528641Z   DEVICE_CODE: fire
2026-05-03T00:40:15.7528859Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:40:15.7529120Z   CLANG_VERSION: 
2026-05-03T00:40:15.7529303Z   LLD_VERSION: 
2026-05-03T00:40:15.7529525Z   KERNEL_HEAD_HASH: 
2026-05-03T00:40:15.7529718Z   KSU_DIR: 
2026-05-03T00:40:15.7529887Z   KSU_VERSION: 
2026-05-03T00:40:15.7530064Z   KERNEL_VERSION: 
2026-05-03T00:40:15.7530251Z   ZIP_NAME: 
2026-05-03T00:40:15.7530427Z ##[endgroup]
2026-05-03T00:40:15.8121925Z Setting up swapspace version 1, size = 16 GiB (17179865088 bytes)
2026-05-03T00:40:15.8122510Z no label, UUID=2443ee17-349a-4afd-8169-10ed80742112
2026-05-03T00:40:15.8244691Z                total        used        free      shared  buff/cache   available
2026-05-03T00:40:15.8245382Z Mem:            15Gi       1.0Gi        11Gi        43Mi       3.3Gi        14Gi
2026-05-03T00:40:15.8245899Z Swap:           18Gi          0B        18Gi
2026-05-03T00:40:15.8277362Z ##[group]Run sudo apt-get update
2026-05-03T00:40:15.8277682Z [36;1msudo apt-get update[0m
2026-05-03T00:40:15.8278046Z [36;1msudo apt-get install -y aria2 git ccache automake flex lzop bison gperf \[0m
2026-05-03T00:40:15.8278822Z [36;1m  build-essential zip curl zlib1g-dev g++-multilib libxml2-utils bzip2 \[0m
2026-05-03T00:40:15.8279354Z [36;1m  libbz2-dev squashfs-tools pngcrush schedtool dpkg-dev liblz4-tool make \[0m
2026-05-03T00:40:15.8279878Z [36;1m  optipng maven libssl-dev pwgen libxml-sax-base-perl libxml-simple-perl \[0m
2026-05-03T00:40:15.8280370Z [36;1m  libc6-dev-i386 lib32ncurses-dev libncurses-dev libx11-dev lib32z-dev \[0m
2026-05-03T00:40:15.8280819Z [36;1m  libstdc++6 lib32stdc++6 libgl1-mesa-dev xsltproc unzip gzip \[0m
2026-05-03T00:40:15.8281279Z [36;1m  device-tree-compiler cpio findutils python3 bc p7zip-full libelf-dev \[0m
2026-05-03T00:40:15.8281660Z [36;1m  jq libyaml-dev -y[0m
2026-05-03T00:40:15.8304408Z shell: /usr/bin/bash -e {0}
2026-05-03T00:40:15.8304644Z env:
2026-05-03T00:40:15.8304830Z   KERNEL_NAME: Castorice
2026-05-03T00:40:15.8305044Z   DEVICE_CODE: fire
2026-05-03T00:40:15.8305269Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:40:15.8305523Z   CLANG_VERSION: 
2026-05-03T00:40:15.8305706Z   LLD_VERSION: 
2026-05-03T00:40:15.8305888Z   KERNEL_HEAD_HASH: 
2026-05-03T00:40:15.8306072Z   KSU_DIR: 
2026-05-03T00:40:15.8306250Z   KSU_VERSION: 
2026-05-03T00:40:15.8306420Z   KERNEL_VERSION: 
2026-05-03T00:40:15.8306612Z   ZIP_NAME: 
2026-05-03T00:40:15.8306782Z ##[endgroup]
2026-05-03T00:40:15.9025181Z Get:1 file:/etc/apt/apt-mirrors.txt Mirrorlist [144 B]
2026-05-03T00:40:15.9427783Z Hit:2 http://azure.archive.ubuntu.com/ubuntu noble InRelease
2026-05-03T00:40:15.9469478Z Get:3 http://azure.archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]
2026-05-03T00:40:15.9507918Z Get:4 http://azure.archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]
2026-05-03T00:40:15.9539245Z Get:5 http://azure.archive.ubuntu.com/ubuntu noble-security InRelease [126 kB]
2026-05-03T00:40:15.9600246Z Hit:6 https://packages.microsoft.com/repos/azure-cli noble InRelease
2026-05-03T00:40:15.9633773Z Get:7 https://packages.microsoft.com/ubuntu/24.04/prod noble InRelease [3600 B]
2026-05-03T00:40:16.0761012Z Get:8 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 Packages [1946 kB]
2026-05-03T00:40:16.0996354Z Get:9 http://azure.archive.ubuntu.com/ubuntu noble-updates/main Translation-en [348 kB]
2026-05-03T00:40:16.1019611Z Get:10 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 Components [177 kB]
2026-05-03T00:40:16.1032132Z Get:11 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 c-n-f Metadata [17.1 kB]
2026-05-03T00:40:16.1047449Z Get:12 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Packages [1685 kB]
2026-05-03T00:40:16.1164583Z Get:13 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe Translation-en [324 kB]
2026-05-03T00:40:16.1195105Z Get:14 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Components [386 kB]
2026-05-03T00:40:16.1236209Z Get:15 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 c-n-f Metadata [34.5 kB]
2026-05-03T00:40:16.1245502Z Get:16 http://azure.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Packages [3095 kB]
2026-05-03T00:40:16.1441961Z Get:17 http://azure.archive.ubuntu.com/ubuntu noble-updates/restricted Translation-en [715 kB]
2026-05-03T00:40:16.1449152Z Get:24 https://dl.google.com/linux/chrome-stable/deb stable InRelease [1825 B]
2026-05-03T00:40:16.1899062Z Get:18 http://azure.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Components [212 B]
2026-05-03T00:40:16.1905663Z Get:19 http://azure.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 c-n-f Metadata [480 B]
2026-05-03T00:40:16.1916514Z Get:20 http://azure.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Packages [44.4 kB]
2026-05-03T00:40:16.1930790Z Get:21 http://azure.archive.ubuntu.com/ubuntu noble-updates/multiverse Translation-en [10.2 kB]
2026-05-03T00:40:16.1943654Z Get:22 http://azure.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Components [940 B]
2026-05-03T00:40:16.1955547Z Get:23 http://azure.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 c-n-f Metadata [656 B]
2026-05-03T00:40:16.2002009Z Get:25 http://azure.archive.ubuntu.com/ubuntu noble-backports/main amd64 Packages [64.5 kB]
2026-05-03T00:40:16.2008337Z Get:26 http://azure.archive.ubuntu.com/ubuntu noble-backports/main Translation-en [9172 B]
2026-05-03T00:40:16.2009840Z Get:27 http://azure.archive.ubuntu.com/ubuntu noble-backports/main amd64 Components [7368 B]
2026-05-03T00:40:16.2011190Z Get:28 http://azure.archive.ubuntu.com/ubuntu noble-backports/main amd64 c-n-f Metadata [368 B]
2026-05-03T00:40:16.2013602Z Get:29 http://azure.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Packages [34.1 kB]
2026-05-03T00:40:16.2027598Z Get:30 http://azure.archive.ubuntu.com/ubuntu noble-backports/universe Translation-en [18.2 kB]
2026-05-03T00:40:16.2036983Z Get:31 http://azure.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Components [10.5 kB]
2026-05-03T00:40:16.2046172Z Get:32 http://azure.archive.ubuntu.com/ubuntu noble-backports/universe amd64 c-n-f Metadata [1484 B]
2026-05-03T00:40:16.2537916Z Get:33 http://azure.archive.ubuntu.com/ubuntu noble-backports/restricted amd64 Components [212 B]
2026-05-03T00:40:16.2551588Z Get:34 http://azure.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Packages [748 B]
2026-05-03T00:40:16.2564031Z Get:35 http://azure.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Components [212 B]
2026-05-03T00:40:16.2579463Z Get:36 http://azure.archive.ubuntu.com/ubuntu noble-security/main amd64 Packages [1625 kB]
2026-05-03T00:40:16.2662885Z Get:37 http://azure.archive.ubuntu.com/ubuntu noble-security/main Translation-en [259 kB]
2026-05-03T00:40:16.2690067Z Get:38 http://azure.archive.ubuntu.com/ubuntu noble-security/main amd64 Components [21.9 kB]
2026-05-03T00:40:16.2721606Z Get:39 http://azure.archive.ubuntu.com/ubuntu noble-security/main amd64 c-n-f Metadata [11.0 kB]
2026-05-03T00:40:16.2738895Z Get:40 http://azure.archive.ubuntu.com/ubuntu noble-security/universe amd64 Packages [1182 kB]
2026-05-03T00:40:16.2827651Z Get:41 http://azure.archive.ubuntu.com/ubuntu noble-security/universe Translation-en [227 kB]
2026-05-03T00:40:16.2850591Z Get:42 http://azure.archive.ubuntu.com/ubuntu noble-security/universe amd64 Components [74.2 kB]
2026-05-03T00:40:16.2879658Z Get:43 http://azure.archive.ubuntu.com/ubuntu noble-security/universe amd64 c-n-f Metadata [23.1 kB]
2026-05-03T00:40:16.2897626Z Get:44 http://azure.archive.ubuntu.com/ubuntu noble-security/restricted amd64 Packages [2844 kB]
2026-05-03T00:40:16.3056149Z Get:45 http://azure.archive.ubuntu.com/ubuntu noble-security/restricted Translation-en [666 kB]
2026-05-03T00:40:16.3102171Z Get:46 http://azure.archive.ubuntu.com/ubuntu noble-security/restricted amd64 Components [212 B]
2026-05-03T00:40:16.3115587Z Get:47 http://azure.archive.ubuntu.com/ubuntu noble-security/multiverse amd64 Packages [28.8 kB]
2026-05-03T00:40:16.3262838Z Get:50 https://packages.microsoft.com/ubuntu/24.04/prod noble/main amd64 Packages [132 kB]
2026-05-03T00:40:16.3317475Z Get:51 https://packages.microsoft.com/ubuntu/24.04/prod noble/main armhf Packages [11.6 kB]
2026-05-03T00:40:16.3444652Z Get:52 https://packages.microsoft.com/ubuntu/24.04/prod noble/main arm64 Packages [107 kB]
2026-05-03T00:40:16.3574032Z Get:48 http://azure.archive.ubuntu.com/ubuntu noble-security/multiverse Translation-en [7172 B]
2026-05-03T00:40:16.3591136Z Get:49 http://azure.archive.ubuntu.com/ubuntu noble-security/multiverse amd64 Components [208 B]
2026-05-03T00:40:16.4153418Z Get:53 https://dl.google.com/linux/chrome-stable/deb stable/main amd64 Packages [1216 B]
2026-05-03T00:40:23.2776577Z Fetched 16.5 MB in 2s (8476 kB/s)
2026-05-03T00:40:24.1309485Z Reading package lists...
2026-05-03T00:40:24.1677613Z Reading package lists...
2026-05-03T00:40:24.3448648Z Building dependency tree...
2026-05-03T00:40:24.3454410Z Reading state information...
2026-05-03T00:40:24.5101773Z aria2 is already the newest version (1.37.0+debian-1build3).
2026-05-03T00:40:24.5102489Z git is already the newest version (1:2.53.0-0ppa1~ubuntu24.04.1).
2026-05-03T00:40:24.5103007Z git set to manually installed.
2026-05-03T00:40:24.5103462Z automake is already the newest version (1:1.16.5-1.3ubuntu1).
2026-05-03T00:40:24.5104001Z flex is already the newest version (2.6.4-8.2build1).
2026-05-03T00:40:24.5104568Z bison is already the newest version (2:3.8.2+dfsg-1build2).
2026-05-03T00:40:24.5105159Z zip is already the newest version (3.0-13ubuntu0.2).
2026-05-03T00:40:24.5105727Z curl is already the newest version (8.5.0-2ubuntu10.8).
2026-05-03T00:40:24.5106319Z zlib1g-dev is already the newest version (1:1.3.dfsg-3.1ubuntu2.1).
2026-05-03T00:40:24.5106908Z bzip2 is already the newest version (1.0.8-5.1build0.1).
2026-05-03T00:40:24.5107562Z squashfs-tools is already the newest version (1:4.6.1-1build1).
2026-05-03T00:40:24.5108175Z squashfs-tools set to manually installed.
2026-05-03T00:40:24.5108894Z dpkg-dev is already the newest version (1.22.6ubuntu6.5).
2026-05-03T00:40:24.5109416Z make is already the newest version (4.3-4.1build2).
2026-05-03T00:40:24.5109953Z libssl-dev is already the newest version (3.0.13-0ubuntu3.9).
2026-05-03T00:40:24.5110562Z libxml-sax-base-perl is already the newest version (1.09-3).
2026-05-03T00:40:24.5111108Z libxml-sax-base-perl set to manually installed.
2026-05-03T00:40:24.5111694Z libstdc++6 is already the newest version (14.2.0-4ubuntu2~24.04.1).
2026-05-03T00:40:24.5112288Z unzip is already the newest version (6.0-28ubuntu4.1).
2026-05-03T00:40:24.5112830Z gzip is already the newest version (1.12-1ubuntu3.1).
2026-05-03T00:40:24.5113352Z cpio is already the newest version (2.15+dfsg-1ubuntu2).
2026-05-03T00:40:24.5113864Z cpio set to manually installed.
2026-05-03T00:40:24.5114390Z findutils is already the newest version (4.9.0-5build1).
2026-05-03T00:40:24.5115036Z python3 is already the newest version (3.12.3-0ubuntu2.1).
2026-05-03T00:40:24.5115567Z bc is already the newest version (1.07.1-3ubuntu4).
2026-05-03T00:40:24.5116084Z bc set to manually installed.
2026-05-03T00:40:24.5116604Z p7zip-full is already the newest version (16.02+transitional.1).
2026-05-03T00:40:24.5117224Z libyaml-dev is already the newest version (0.2.5-1build1).
2026-05-03T00:40:24.5117778Z The following additional packages will be installed:
2026-05-03T00:40:24.5118343Z   bzip2-doc g++-13-multilib gcc-13-multilib gcc-multilib lib32asan8
2026-05-03T00:40:24.5119109Z   lib32atomic1 lib32gcc-13-dev lib32gcc-s1 lib32gomp1 lib32itm1 lib32ncurses6
2026-05-03T00:40:24.5119811Z   lib32ncursesw6 lib32quadmath0 lib32stdc++-13-dev lib32tinfo6 lib32ubsan1
2026-05-03T00:40:24.5120592Z   lib32z1 libaopalliance-java libapache-pom-java libatinject-jsr330-api-java
2026-05-03T00:40:24.5121286Z   libc6-dev-x32 libc6-i386 libc6-x32 libcdi-api-java libcommons-cli-java
2026-05-03T00:40:24.5122021Z   libcommons-io-java libcommons-lang3-java libcommons-parent-java libegl-dev
2026-05-03T00:40:24.5122670Z   libegl-mesa0 libegl1 liberror-prone-java libfdt1
2026-05-03T00:40:24.5123322Z   libgeronimo-annotation-1.3-spec-java libgeronimo-interceptor-3.0-spec-java
2026-05-03T00:40:24.5124063Z   libgl-dev libgles-dev libgles1 libgles2 libglvnd-core-dev libglvnd-dev
2026-05-03T00:40:24.5124819Z   libglx-dev libguava-java libguice-java libhiredis1.1.0 libjansi-java libjq1
2026-05-03T00:40:24.5125526Z   libjsr305-java libmaven-parent-java libmaven-resolver-java
2026-05-03T00:40:24.5126225Z   libmaven-shared-utils-java libmaven3-core-java libopengl-dev libopengl0
2026-05-03T00:40:24.5126881Z   libplexus-cipher-java libplexus-classworlds-java
2026-05-03T00:40:24.5127492Z   libplexus-component-annotations-java libplexus-interpolation-java
2026-05-03T00:40:24.5128258Z   libplexus-sec-dispatcher-java libplexus-utils2-java libpthread-stubs0-dev
2026-05-03T00:40:24.5129588Z   libsisu-inject-java libsisu-plexus-java libslf4j-java libwagon-file-java
2026-05-03T00:40:24.5130496Z   libwagon-http-shaded-java libwagon-provider-api-java libx32asan8
2026-05-03T00:40:24.5131179Z   libx32atomic1 libx32gcc-13-dev libx32gcc-s1 libx32gomp1 libx32itm1
2026-05-03T00:40:24.5131874Z   libx32quadmath0 libx32stdc++-13-dev libx32stdc++6 libx32ubsan1 libxau-dev
2026-05-03T00:40:24.5132592Z   libxcb1-dev libxdmcp-dev x11proto-dev xorg-sgml-doctools xtrans-dev
2026-05-03T00:40:24.5133113Z Suggested packages:
2026-05-03T00:40:24.5133566Z   distcc | icecc lib32stdc++6-13-dbg libx32stdc++6-13-dbg ncurses-doc
2026-05-03T00:40:24.5134255Z   libatinject-jsr330-api-java-doc libel-api-java libcommons-io-java-doc
2026-05-03T00:40:24.5135010Z   libasm-java libcglib-java libjsr305-java-doc libmaven-shared-utils-java-doc
2026-05-03T00:40:24.5135693Z   liblogback-java libplexus-utils2-java-doc junit4 testng
2026-05-03T00:40:24.5136286Z   libcommons-logging-java liblog4j1.2-java libx11-doc libxcb-doc
2026-05-03T00:40:24.5778761Z The following NEW packages will be installed:
2026-05-03T00:40:24.5779501Z   build-essential bzip2-doc ccache device-tree-compiler g++-13-multilib
2026-05-03T00:40:24.5780320Z   g++-multilib gcc-13-multilib gcc-multilib gperf lib32asan8 lib32atomic1
2026-05-03T00:40:24.5782260Z   lib32gcc-13-dev lib32gcc-s1 lib32gomp1 lib32itm1 lib32ncurses-dev
2026-05-03T00:40:24.5782967Z   lib32ncurses6 lib32ncursesw6 lib32quadmath0 lib32stdc++-13-dev lib32stdc++6
2026-05-03T00:40:24.5783628Z   lib32tinfo6 lib32ubsan1 lib32z1 lib32z1-dev libaopalliance-java
2026-05-03T00:40:24.5784261Z   libapache-pom-java libatinject-jsr330-api-java libbz2-dev libc6-dev-i386
2026-05-03T00:40:24.5784913Z   libc6-dev-x32 libc6-i386 libc6-x32 libcdi-api-java libcommons-cli-java
2026-05-03T00:40:24.5785583Z   libcommons-io-java libcommons-lang3-java libcommons-parent-java libegl-dev
2026-05-03T00:40:24.5786224Z   libegl-mesa0 libegl1 libelf-dev liberror-prone-java libfdt1
2026-05-03T00:40:24.5786835Z   libgeronimo-annotation-1.3-spec-java libgeronimo-interceptor-3.0-spec-java
2026-05-03T00:40:24.5787591Z   libgl-dev libgl1-mesa-dev libgles-dev libgles1 libgles2 libglvnd-core-dev
2026-05-03T00:40:24.5788310Z   libglvnd-dev libglx-dev libguava-java libguice-java libhiredis1.1.0
2026-05-03T00:40:24.5789112Z   libjansi-java libjsr305-java liblz4-tool libmaven-parent-java
2026-05-03T00:40:24.5789697Z   libmaven-resolver-java libmaven-shared-utils-java libmaven3-core-java
2026-05-03T00:40:24.5790390Z   libncurses-dev libopengl-dev libopengl0 libplexus-cipher-java
2026-05-03T00:40:24.5790865Z   libplexus-classworlds-java libplexus-component-annotations-java
2026-05-03T00:40:24.5791285Z   libplexus-interpolation-java libplexus-sec-dispatcher-java
2026-05-03T00:40:24.5791699Z   libplexus-utils2-java libpthread-stubs0-dev libsisu-inject-java
2026-05-03T00:40:24.5792074Z   libsisu-plexus-java libslf4j-java libwagon-file-java
2026-05-03T00:40:24.5792541Z   libwagon-http-shaded-java libwagon-provider-api-java libx11-dev libx32asan8
2026-05-03T00:40:24.5793025Z   libx32atomic1 libx32gcc-13-dev libx32gcc-s1 libx32gomp1 libx32itm1
2026-05-03T00:40:24.5793476Z   libx32quadmath0 libx32stdc++-13-dev libx32stdc++6 libx32ubsan1 libxau-dev
2026-05-03T00:40:24.5793994Z   libxcb1-dev libxdmcp-dev libxml-simple-perl libxml2-utils lzop maven optipng
2026-05-03T00:40:24.5794487Z   pngcrush pwgen schedtool x11proto-dev xorg-sgml-doctools xsltproc xtrans-dev
2026-05-03T00:40:24.5795111Z The following packages will be upgraded:
2026-05-03T00:40:24.5801373Z   jq libjq1
2026-05-03T00:40:24.6014194Z 2 upgraded, 106 newly installed, 0 to remove and 48 not upgraded.
2026-05-03T00:40:24.6014766Z Need to get 41.7 MB of archives.
2026-05-03T00:40:24.6015226Z After this operation, 138 MB of additional disk space will be used.
2026-05-03T00:40:24.6015614Z Get:1 file:/etc/apt/apt-mirrors.txt Mirrorlist [144 B]
2026-05-03T00:40:24.7716093Z Get:2 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 build-essential amd64 12.10ubuntu1 [4928 B]
2026-05-03T00:40:24.8089152Z Get:3 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 bzip2-doc all 1.0.8-5.1build0.1 [499 kB]
2026-05-03T00:40:24.8532948Z Get:4 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libhiredis1.1.0 amd64 1.2.0-6ubuntu3 [41.4 kB]
2026-05-03T00:40:24.8900754Z Get:5 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 ccache amd64 4.9.1-1 [592 kB]
2026-05-03T00:40:24.9393764Z Get:6 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libc6-i386 amd64 2.39-0ubuntu8.7 [2788 kB]
2026-05-03T00:40:25.0142280Z Get:7 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libc6-dev-i386 amd64 2.39-0ubuntu8.7 [1447 kB]
2026-05-03T00:40:25.0871737Z Get:8 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libc6-x32 amd64 2.39-0ubuntu8.7 [2914 kB]
2026-05-03T00:40:25.1626125Z Get:9 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libc6-dev-x32 amd64 2.39-0ubuntu8.7 [1637 kB]
2026-05-03T00:40:25.2273305Z Get:10 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32gcc-s1 amd64 14.2.0-4ubuntu2~24.04.1 [92.3 kB]
2026-05-03T00:40:25.2645621Z Get:11 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32gcc-s1 amd64 14.2.0-4ubuntu2~24.04.1 [78.5 kB]
2026-05-03T00:40:25.3060666Z Get:12 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32gomp1 amd64 14.2.0-4ubuntu2~24.04.1 [141 kB]
2026-05-03T00:40:25.3427824Z Get:13 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32gomp1 amd64 14.2.0-4ubuntu2~24.04.1 [144 kB]
2026-05-03T00:40:25.3810971Z Get:14 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32itm1 amd64 14.2.0-4ubuntu2~24.04.1 [29.5 kB]
2026-05-03T00:40:25.4175943Z Get:15 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32itm1 amd64 14.2.0-4ubuntu2~24.04.1 [29.8 kB]
2026-05-03T00:40:25.4543282Z Get:16 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32atomic1 amd64 14.2.0-4ubuntu2~24.04.1 [8594 B]
2026-05-03T00:40:25.4910628Z Get:17 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32atomic1 amd64 14.2.0-4ubuntu2~24.04.1 [10.3 kB]
2026-05-03T00:40:25.5281225Z Get:18 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32asan8 amd64 14.2.0-4ubuntu2~24.04.1 [2880 kB]
2026-05-03T00:40:25.5941053Z Get:19 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32asan8 amd64 14.2.0-4ubuntu2~24.04.1 [2893 kB]
2026-05-03T00:40:25.6934918Z Get:20 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32stdc++6 amd64 14.2.0-4ubuntu2~24.04.1 [814 kB]
2026-05-03T00:40:25.7359811Z Get:21 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32ubsan1 amd64 14.2.0-4ubuntu2~24.04.1 [1150 kB]
2026-05-03T00:40:25.7794920Z Get:22 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32stdc++6 amd64 14.2.0-4ubuntu2~24.04.1 [778 kB]
2026-05-03T00:40:25.8205147Z Get:23 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32ubsan1 amd64 14.2.0-4ubuntu2~24.04.1 [1169 kB]
2026-05-03T00:40:25.8707393Z Get:24 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32quadmath0 amd64 14.2.0-4ubuntu2~24.04.1 [227 kB]
2026-05-03T00:40:25.9111100Z Get:25 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32quadmath0 amd64 14.2.0-4ubuntu2~24.04.1 [157 kB]
2026-05-03T00:40:25.9489433Z Get:26 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32gcc-13-dev amd64 13.3.0-6ubuntu2~24.04.1 [2380 kB]
2026-05-03T00:40:26.0009954Z Get:27 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32gcc-13-dev amd64 13.3.0-6ubuntu2~24.04.1 [2190 kB]
2026-05-03T00:40:26.0524624Z Get:28 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 gcc-13-multilib amd64 13.3.0-6ubuntu2~24.04.1 [880 B]
2026-05-03T00:40:26.0895723Z Get:29 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32stdc++-13-dev amd64 13.3.0-6ubuntu2~24.04.1 [1150 kB]
2026-05-03T00:40:26.1337799Z Get:30 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libx32stdc++-13-dev amd64 13.3.0-6ubuntu2~24.04.1 [1086 kB]
2026-05-03T00:40:26.1796711Z Get:31 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 g++-13-multilib amd64 13.3.0-6ubuntu2~24.04.1 [892 B]
2026-05-03T00:40:26.2159955Z Get:32 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 gcc-multilib amd64 4:13.2.0-7ubuntu1 [1474 B]
2026-05-03T00:40:26.2527634Z Get:33 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 g++-multilib amd64 4:13.2.0-7ubuntu1 [884 B]
2026-05-03T00:40:26.2894997Z Get:34 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 gperf amd64 3.1-1build1 [103 kB]
2026-05-03T00:40:26.3268316Z Get:35 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 jq amd64 1.7.1-3ubuntu0.24.04.2 [65.7 kB]
2026-05-03T00:40:26.3638271Z Get:36 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libjq1 amd64 1.7.1-3ubuntu0.24.04.2 [142 kB]
2026-05-03T00:40:26.4015010Z Get:37 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 lib32tinfo6 amd64 6.4+20240113-1ubuntu2 [105 kB]
2026-05-03T00:40:26.4395883Z Get:38 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 lib32ncurses6 amd64 6.4+20240113-1ubuntu2 [113 kB]
2026-05-03T00:40:26.5255834Z Get:39 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 lib32ncursesw6 amd64 6.4+20240113-1ubuntu2 [153 kB]
2026-05-03T00:40:26.5564678Z Get:40 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libncurses-dev amd64 6.4+20240113-1ubuntu2 [384 kB]
2026-05-03T00:40:26.5891186Z Get:41 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 lib32ncurses-dev amd64 6.4+20240113-1ubuntu2 [344 kB]
2026-05-03T00:40:26.6213811Z Get:42 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32z1 amd64 1:1.3.dfsg-3.1ubuntu2.1 [57.4 kB]
2026-05-03T00:40:26.6516697Z Get:43 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 lib32z1-dev amd64 1:1.3.dfsg-3.1ubuntu2.1 [56.4 kB]
2026-05-03T00:40:26.6814944Z Get:44 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libapache-pom-java all 29-2 [5284 B]
2026-05-03T00:40:26.7112219Z Get:45 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libatinject-jsr330-api-java all 1.0+ds1-5 [5348 B]
2026-05-03T00:40:26.7408009Z Get:46 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libbz2-dev amd64 1.0.8-5.1build0.1 [33.6 kB]
2026-05-03T00:40:26.7710267Z Get:47 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libgeronimo-interceptor-3.0-spec-java all 1.0.1-4fakesync [8616 B]
2026-05-03T00:40:26.8010831Z Get:48 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libcdi-api-java all 1.2-3 [54.3 kB]
2026-05-03T00:40:26.8315896Z Get:49 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libcommons-cli-java all 1.6.0-1 [59.9 kB]
2026-05-03T00:40:26.8618930Z Get:50 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libcommons-parent-java all 56-1 [10.7 kB]
2026-05-03T00:40:26.8920501Z Get:51 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libcommons-io-java all 2.11.0-2 [297 kB]
2026-05-03T00:40:26.9243011Z Get:52 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libcommons-lang3-java all 3.14.0-1 [586 kB]
2026-05-03T00:40:26.9633002Z Get:53 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libegl-mesa0 amd64 25.2.8-0ubuntu0.24.04.1 [117 kB]
2026-05-03T00:40:26.9946741Z Get:54 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libegl1 amd64 1.7.0-1build1 [28.7 kB]
2026-05-03T00:40:27.0251529Z Get:55 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 xorg-sgml-doctools all 1:1.11-1.1 [10.9 kB]
2026-05-03T00:40:27.0548759Z Get:56 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 x11proto-dev all 2023.2-1 [602 kB]
2026-05-03T00:40:27.1440752Z Get:57 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libxau-dev amd64 1:1.0.9-1build6 [9570 B]
2026-05-03T00:40:27.1741789Z Get:58 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libxdmcp-dev amd64 1:1.1.3-0ubuntu6 [26.5 kB]
2026-05-03T00:40:27.2039270Z Get:59 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 xtrans-dev all 1.4.0-1 [68.9 kB]
2026-05-03T00:40:27.2337438Z Get:60 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libpthread-stubs0-dev amd64 0.4-1build3 [4746 B]
2026-05-03T00:40:27.2633207Z Get:61 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libxcb1-dev amd64 1.15-1ubuntu2 [85.8 kB]
2026-05-03T00:40:27.2937985Z Get:62 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libx11-dev amd64 2:1.8.7-1build1 [732 kB]
2026-05-03T00:40:27.3309399Z Get:63 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libglx-dev amd64 1.7.0-1build1 [14.2 kB]
2026-05-03T00:40:27.3617497Z Get:64 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libgl-dev amd64 1.7.0-1build1 [102 kB]
2026-05-03T00:40:27.3986114Z Get:65 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libegl-dev amd64 1.7.0-1build1 [18.2 kB]
2026-05-03T00:40:27.4347125Z Get:66 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libelf-dev amd64 0.190-1.1ubuntu0.1 [68.5 kB]
2026-05-03T00:40:27.4665242Z Get:67 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libjsr305-java all 0.1~+svn49-11 [27.0 kB]
2026-05-03T00:40:27.4969356Z Get:68 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libguava-java all 32.0.1-1 [2692 kB]
2026-05-03T00:40:27.5630756Z Get:69 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 liberror-prone-java all 2.18.0-1 [22.5 kB]
2026-05-03T00:40:27.5929624Z Get:70 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libgeronimo-annotation-1.3-spec-java all 1.3-1 [11.2 kB]
2026-05-03T00:40:27.6226067Z Get:71 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libgles1 amd64 1.7.0-1build1 [11.6 kB]
2026-05-03T00:40:27.6526783Z Get:72 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libgles2 amd64 1.7.0-1build1 [17.1 kB]
2026-05-03T00:40:27.6823892Z Get:73 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libgles-dev amd64 1.7.0-1build1 [50.5 kB]
2026-05-03T00:40:27.7124676Z Get:74 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libaopalliance-java all 20070526-7 [8166 B]
2026-05-03T00:40:27.7465957Z Get:75 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libguice-java all 4.2.3-2 [1434 kB]
2026-05-03T00:40:27.8395228Z Get:76 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libjansi-java all 2.4.1-2 [83.0 kB]
2026-05-03T00:40:27.8700845Z Get:77 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libmaven-parent-java all 35-1 [5810 B]
2026-05-03T00:40:27.9000009Z Get:78 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libplexus-utils2-java all 3.4.2-1 [256 kB]
2026-05-03T00:40:27.9326682Z Get:79 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libwagon-provider-api-java all 3.5.3-1 [47.9 kB]
2026-05-03T00:40:27.9633220Z Get:80 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libmaven-resolver-java all 1.6.3-1 [544 kB]
2026-05-03T00:40:27.9982844Z Get:81 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libmaven-shared-utils-java all 3.3.4-1 [137 kB]
2026-05-03T00:40:28.0295842Z Get:82 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libplexus-cipher-java all 2.0-1 [14.7 kB]
2026-05-03T00:40:28.0593281Z Get:83 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libplexus-classworlds-java all 2.7.0-1 [50.0 kB]
2026-05-03T00:40:28.0896136Z Get:84 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libplexus-component-annotations-java all 2.1.1-1 [6550 B]
2026-05-03T00:40:28.1196910Z Get:85 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libplexus-interpolation-java all 1.26-1 [76.8 kB]
2026-05-03T00:40:28.1504943Z Get:86 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libplexus-sec-dispatcher-java all 2.0-3 [28.1 kB]
2026-05-03T00:40:28.1809353Z Get:87 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libslf4j-java all 1.7.32-1 [141 kB]
2026-05-03T00:40:28.2124840Z Get:88 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libsisu-inject-java all 0.3.4-2 [347 kB]
2026-05-03T00:40:28.2459721Z Get:89 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libsisu-plexus-java all 0.3.4-3 [181 kB]
2026-05-03T00:40:28.2777854Z Get:90 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libmaven3-core-java all 3.8.7-2 [1565 kB]
2026-05-03T00:40:28.3246009Z Get:91 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libopengl0 amd64 1.7.0-1build1 [32.8 kB]
2026-05-03T00:40:28.3548034Z Get:92 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libopengl-dev amd64 1.7.0-1build1 [3454 B]
2026-05-03T00:40:28.3849374Z Get:93 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libwagon-file-java all 3.5.3-1 [7918 B]
2026-05-03T00:40:28.4598605Z Get:94 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libwagon-http-shaded-java all 3.5.3-1 [1332 kB]
2026-05-03T00:40:28.5059207Z Get:95 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libxml-simple-perl all 2.25-2 [64.1 kB]
2026-05-03T00:40:28.5367933Z Get:96 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libxml2-utils amd64 2.9.14+dfsg-1.3ubuntu3.7 [39.4 kB]
2026-05-03T00:40:28.5670603Z Get:97 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 lzop amd64 1.04-2build3 [82.2 kB]
2026-05-03T00:40:28.5976845Z Get:98 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 maven all 3.8.7-2 [18.3 kB]
2026-05-03T00:40:28.6279710Z Get:99 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 optipng amd64 0.7.8+ds-1build2 [110 kB]
2026-05-03T00:40:28.6590872Z Get:100 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 pngcrush amd64 1.8.13-1build2 [49.5 kB]
2026-05-03T00:40:28.6891775Z Get:101 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 pwgen amd64 2.08-2build2 [17.2 kB]
2026-05-03T00:40:28.7189708Z Get:102 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 xsltproc amd64 1.1.39-0exp1ubuntu0.24.04.3 [15.0 kB]
2026-05-03T00:40:28.7796417Z Get:103 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libfdt1 amd64 1.7.0-2build1 [20.1 kB]
2026-05-03T00:40:28.8401402Z Get:104 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 device-tree-compiler amd64 1.7.0-2build1 [228 kB]
2026-05-03T00:40:28.9599671Z Get:105 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libglvnd-core-dev amd64 1.7.0-1build1 [13.6 kB]
2026-05-03T00:40:28.9892519Z Get:106 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libglvnd-dev amd64 1.7.0-1build1 [3198 B]
2026-05-03T00:40:29.0185480Z Get:107 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libgl1-mesa-dev amd64 25.2.8-0ubuntu0.24.04.1 [22.5 kB]
2026-05-03T00:40:29.0483315Z Get:108 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 liblz4-tool all 1.9.4-1build1.1 [2484 B]
2026-05-03T00:40:29.0775543Z Get:109 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 schedtool amd64 1.3.0-4 [22.0 kB]
2026-05-03T00:40:29.4092668Z Fetched 41.7 MB in 4s (9281 kB/s)
2026-05-03T00:40:29.4298837Z Selecting previously unselected package build-essential.
2026-05-03T00:40:29.4354039Z (Reading database ... 
2026-05-03T00:40:29.4354434Z (Reading database ... 5%
2026-05-03T00:40:29.4354786Z (Reading database ... 10%
2026-05-03T00:40:29.4355120Z (Reading database ... 15%
2026-05-03T00:40:29.4355440Z (Reading database ... 20%
2026-05-03T00:40:29.4355757Z (Reading database ... 25%
2026-05-03T00:40:29.4356076Z (Reading database ... 30%
2026-05-03T00:40:29.4356393Z (Reading database ... 35%
2026-05-03T00:40:29.4356746Z (Reading database ... 40%
2026-05-03T00:40:29.4357039Z (Reading database ... 45%
2026-05-03T00:40:29.4357292Z (Reading database ... 50%
2026-05-03T00:40:29.4357547Z (Reading database ... 55%
2026-05-03T00:40:29.4396289Z (Reading database ... 60%
2026-05-03T00:40:29.4499406Z (Reading database ... 65%
2026-05-03T00:40:29.4530346Z (Reading database ... 70%
2026-05-03T00:40:29.4550456Z (Reading database ... 75%
2026-05-03T00:40:29.4604188Z (Reading database ... 80%
2026-05-03T00:40:29.4634479Z (Reading database ... 85%
2026-05-03T00:40:29.4661894Z (Reading database ... 90%
2026-05-03T00:40:29.4778638Z (Reading database ... 95%
2026-05-03T00:40:29.4779412Z (Reading database ... 100%
2026-05-03T00:40:29.4779739Z (Reading database ... 119905 files and directories currently installed.)
2026-05-03T00:40:29.4806471Z Preparing to unpack .../000-build-essential_12.10ubuntu1_amd64.deb ...
2026-05-03T00:40:29.4815080Z Unpacking build-essential (12.10ubuntu1) ...
2026-05-03T00:40:29.4991113Z Selecting previously unselected package bzip2-doc.
2026-05-03T00:40:29.5068994Z Preparing to unpack .../001-bzip2-doc_1.0.8-5.1build0.1_all.deb ...
2026-05-03T00:40:29.5075714Z Unpacking bzip2-doc (1.0.8-5.1build0.1) ...
2026-05-03T00:40:29.5289286Z Selecting previously unselected package libhiredis1.1.0:amd64.
2026-05-03T00:40:29.5369048Z Preparing to unpack .../002-libhiredis1.1.0_1.2.0-6ubuntu3_amd64.deb ...
2026-05-03T00:40:29.5381678Z Unpacking libhiredis1.1.0:amd64 (1.2.0-6ubuntu3) ...
2026-05-03T00:40:29.5564009Z Selecting previously unselected package ccache.
2026-05-03T00:40:29.5641970Z Preparing to unpack .../003-ccache_4.9.1-1_amd64.deb ...
2026-05-03T00:40:29.5648984Z Unpacking ccache (4.9.1-1) ...
2026-05-03T00:40:29.5925092Z Selecting previously unselected package libc6-i386.
2026-05-03T00:40:29.6004600Z Preparing to unpack .../004-libc6-i386_2.39-0ubuntu8.7_amd64.deb ...
2026-05-03T00:40:29.6030086Z Unpacking libc6-i386 (2.39-0ubuntu8.7) ...
2026-05-03T00:40:29.6948367Z Selecting previously unselected package libc6-dev-i386.
2026-05-03T00:40:29.7030346Z Preparing to unpack .../005-libc6-dev-i386_2.39-0ubuntu8.7_amd64.deb ...
2026-05-03T00:40:29.7037143Z Unpacking libc6-dev-i386 (2.39-0ubuntu8.7) ...
2026-05-03T00:40:29.7547113Z Selecting previously unselected package libc6-x32.
2026-05-03T00:40:29.7628332Z Preparing to unpack .../006-libc6-x32_2.39-0ubuntu8.7_amd64.deb ...
2026-05-03T00:40:29.7662881Z Unpacking libc6-x32 (2.39-0ubuntu8.7) ...
2026-05-03T00:40:29.8562044Z Selecting previously unselected package libc6-dev-x32.
2026-05-03T00:40:29.8644129Z Preparing to unpack .../007-libc6-dev-x32_2.39-0ubuntu8.7_amd64.deb ...
2026-05-03T00:40:29.8650688Z Unpacking libc6-dev-x32 (2.39-0ubuntu8.7) ...
2026-05-03T00:40:29.9119469Z Selecting previously unselected package lib32gcc-s1.
2026-05-03T00:40:29.9200437Z Preparing to unpack .../008-lib32gcc-s1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:29.9207883Z Unpacking lib32gcc-s1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:29.9393610Z Selecting previously unselected package libx32gcc-s1.
2026-05-03T00:40:29.9471839Z Preparing to unpack .../009-libx32gcc-s1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:29.9480061Z Unpacking libx32gcc-s1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:29.9658036Z Selecting previously unselected package lib32gomp1.
2026-05-03T00:40:29.9735161Z Preparing to unpack .../010-lib32gomp1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:29.9742280Z Unpacking lib32gomp1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:29.9928080Z Selecting previously unselected package libx32gomp1.
2026-05-03T00:40:30.0004720Z Preparing to unpack .../011-libx32gomp1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.0012532Z Unpacking libx32gomp1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:30.0203020Z Selecting previously unselected package lib32itm1.
2026-05-03T00:40:30.0281897Z Preparing to unpack .../012-lib32itm1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.0288365Z Unpacking lib32itm1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:30.0462955Z Selecting previously unselected package libx32itm1.
2026-05-03T00:40:30.0540648Z Preparing to unpack .../013-libx32itm1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.0547703Z Unpacking libx32itm1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:30.0727940Z Selecting previously unselected package lib32atomic1.
2026-05-03T00:40:30.0803900Z Preparing to unpack .../014-lib32atomic1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.0812820Z Unpacking lib32atomic1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:30.0999132Z Selecting previously unselected package libx32atomic1.
2026-05-03T00:40:30.1074324Z Preparing to unpack .../015-libx32atomic1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.1081176Z Unpacking libx32atomic1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:30.1255047Z Selecting previously unselected package lib32asan8.
2026-05-03T00:40:30.1330117Z Preparing to unpack .../016-lib32asan8_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.1336438Z Unpacking lib32asan8 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:30.1899379Z Selecting previously unselected package libx32asan8.
2026-05-03T00:40:30.1981034Z Preparing to unpack .../017-libx32asan8_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.1988139Z Unpacking libx32asan8 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:30.2563265Z Selecting previously unselected package lib32stdc++6.
2026-05-03T00:40:30.2644566Z Preparing to unpack .../018-lib32stdc++6_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.2651665Z Unpacking lib32stdc++6 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:30.2918243Z Selecting previously unselected package lib32ubsan1.
2026-05-03T00:40:30.3000148Z Preparing to unpack .../019-lib32ubsan1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.3006938Z Unpacking lib32ubsan1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:30.3333403Z Selecting previously unselected package libx32stdc++6.
2026-05-03T00:40:30.3414945Z Preparing to unpack .../020-libx32stdc++6_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.3421956Z Unpacking libx32stdc++6 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:30.3685238Z Selecting previously unselected package libx32ubsan1.
2026-05-03T00:40:30.3765549Z Preparing to unpack .../021-libx32ubsan1_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.3772217Z Unpacking libx32ubsan1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:30.4081240Z Selecting previously unselected package lib32quadmath0.
2026-05-03T00:40:30.4159390Z Preparing to unpack .../022-lib32quadmath0_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.4165655Z Unpacking lib32quadmath0 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:30.4358081Z Selecting previously unselected package libx32quadmath0.
2026-05-03T00:40:30.4434054Z Preparing to unpack .../023-libx32quadmath0_14.2.0-4ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.4441116Z Unpacking libx32quadmath0 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:30.4616937Z Selecting previously unselected package lib32gcc-13-dev.
2026-05-03T00:40:30.4694265Z Preparing to unpack .../024-lib32gcc-13-dev_13.3.0-6ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.4700710Z Unpacking lib32gcc-13-dev (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T00:40:30.5157410Z Selecting previously unselected package libx32gcc-13-dev.
2026-05-03T00:40:30.5237162Z Preparing to unpack .../025-libx32gcc-13-dev_13.3.0-6ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.5245488Z Unpacking libx32gcc-13-dev (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T00:40:30.5670716Z Selecting previously unselected package gcc-13-multilib.
2026-05-03T00:40:30.5751341Z Preparing to unpack .../026-gcc-13-multilib_13.3.0-6ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.5757873Z Unpacking gcc-13-multilib (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T00:40:30.5918622Z Selecting previously unselected package lib32stdc++-13-dev.
2026-05-03T00:40:30.5998337Z Preparing to unpack .../027-lib32stdc++-13-dev_13.3.0-6ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.6003977Z Unpacking lib32stdc++-13-dev (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T00:40:30.6427673Z Selecting previously unselected package libx32stdc++-13-dev.
2026-05-03T00:40:30.6507815Z Preparing to unpack .../028-libx32stdc++-13-dev_13.3.0-6ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.6514955Z Unpacking libx32stdc++-13-dev (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T00:40:30.6925271Z Selecting previously unselected package g++-13-multilib.
2026-05-03T00:40:30.7004498Z Preparing to unpack .../029-g++-13-multilib_13.3.0-6ubuntu2~24.04.1_amd64.deb ...
2026-05-03T00:40:30.7011714Z Unpacking g++-13-multilib (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T00:40:30.7176109Z Selecting previously unselected package gcc-multilib.
2026-05-03T00:40:30.7258093Z Preparing to unpack .../030-gcc-multilib_4%3a13.2.0-7ubuntu1_amd64.deb ...
2026-05-03T00:40:30.7267053Z Unpacking gcc-multilib (4:13.2.0-7ubuntu1) ...
2026-05-03T00:40:30.7435933Z Selecting previously unselected package g++-multilib.
2026-05-03T00:40:30.7516998Z Preparing to unpack .../031-g++-multilib_4%3a13.2.0-7ubuntu1_amd64.deb ...
2026-05-03T00:40:30.7524229Z Unpacking g++-multilib (4:13.2.0-7ubuntu1) ...
2026-05-03T00:40:30.7689320Z Selecting previously unselected package gperf.
2026-05-03T00:40:30.7770287Z Preparing to unpack .../032-gperf_3.1-1build1_amd64.deb ...
2026-05-03T00:40:30.7777159Z Unpacking gperf (3.1-1build1) ...
2026-05-03T00:40:30.8101497Z Preparing to unpack .../033-jq_1.7.1-3ubuntu0.24.04.2_amd64.deb ...
2026-05-03T00:40:30.8119647Z Unpacking jq (1.7.1-3ubuntu0.24.04.2) over (1.7.1-3ubuntu0.24.04.1) ...
2026-05-03T00:40:30.8406807Z Preparing to unpack .../034-libjq1_1.7.1-3ubuntu0.24.04.2_amd64.deb ...
2026-05-03T00:40:30.8427615Z Unpacking libjq1:amd64 (1.7.1-3ubuntu0.24.04.2) over (1.7.1-3ubuntu0.24.04.1) ...
2026-05-03T00:40:30.8637197Z Selecting previously unselected package lib32tinfo6.
2026-05-03T00:40:30.8721775Z Preparing to unpack .../035-lib32tinfo6_6.4+20240113-1ubuntu2_amd64.deb ...
2026-05-03T00:40:30.8729545Z Unpacking lib32tinfo6 (6.4+20240113-1ubuntu2) ...
2026-05-03T00:40:30.8933385Z Selecting previously unselected package lib32ncurses6.
2026-05-03T00:40:30.9017223Z Preparing to unpack .../036-lib32ncurses6_6.4+20240113-1ubuntu2_amd64.deb ...
2026-05-03T00:40:30.9024493Z Unpacking lib32ncurses6 (6.4+20240113-1ubuntu2) ...
2026-05-03T00:40:30.9235108Z Selecting previously unselected package lib32ncursesw6.
2026-05-03T00:40:30.9317760Z Preparing to unpack .../037-lib32ncursesw6_6.4+20240113-1ubuntu2_amd64.deb ...
2026-05-03T00:40:30.9325390Z Unpacking lib32ncursesw6 (6.4+20240113-1ubuntu2) ...
2026-05-03T00:40:30.9535228Z Selecting previously unselected package libncurses-dev:amd64.
2026-05-03T00:40:30.9618075Z Preparing to unpack .../038-libncurses-dev_6.4+20240113-1ubuntu2_amd64.deb ...
2026-05-03T00:40:30.9626010Z Unpacking libncurses-dev:amd64 (6.4+20240113-1ubuntu2) ...
2026-05-03T00:40:30.9969478Z Selecting previously unselected package lib32ncurses-dev.
2026-05-03T00:40:31.0052276Z Preparing to unpack .../039-lib32ncurses-dev_6.4+20240113-1ubuntu2_amd64.deb ...
2026-05-03T00:40:31.0059690Z Unpacking lib32ncurses-dev (6.4+20240113-1ubuntu2) ...
2026-05-03T00:40:31.0329941Z Selecting previously unselected package lib32z1.
2026-05-03T00:40:31.0412680Z Preparing to unpack .../040-lib32z1_1%3a1.3.dfsg-3.1ubuntu2.1_amd64.deb ...
2026-05-03T00:40:31.0420042Z Unpacking lib32z1 (1:1.3.dfsg-3.1ubuntu2.1) ...
2026-05-03T00:40:31.0603315Z Selecting previously unselected package lib32z1-dev.
2026-05-03T00:40:31.0683635Z Preparing to unpack .../041-lib32z1-dev_1%3a1.3.dfsg-3.1ubuntu2.1_amd64.deb ...
2026-05-03T00:40:31.0691160Z Unpacking lib32z1-dev (1:1.3.dfsg-3.1ubuntu2.1) ...
2026-05-03T00:40:31.0864934Z Selecting previously unselected package libapache-pom-java.
2026-05-03T00:40:31.0942690Z Preparing to unpack .../042-libapache-pom-java_29-2_all.deb ...
2026-05-03T00:40:31.0949561Z Unpacking libapache-pom-java (29-2) ...
2026-05-03T00:40:31.1130489Z Selecting previously unselected package libatinject-jsr330-api-java.
2026-05-03T00:40:31.1207213Z Preparing to unpack .../043-libatinject-jsr330-api-java_1.0+ds1-5_all.deb ...
2026-05-03T00:40:31.1213508Z Unpacking libatinject-jsr330-api-java (1.0+ds1-5) ...
2026-05-03T00:40:31.1392609Z Selecting previously unselected package libbz2-dev:amd64.
2026-05-03T00:40:31.1468786Z Preparing to unpack .../044-libbz2-dev_1.0.8-5.1build0.1_amd64.deb ...
2026-05-03T00:40:31.1475462Z Unpacking libbz2-dev:amd64 (1.0.8-5.1build0.1) ...
2026-05-03T00:40:31.1644414Z Selecting previously unselected package libgeronimo-interceptor-3.0-spec-java.
2026-05-03T00:40:31.1721745Z Preparing to unpack .../045-libgeronimo-interceptor-3.0-spec-java_1.0.1-4fakesync_all.deb ...
2026-05-03T00:40:31.1729762Z Unpacking libgeronimo-interceptor-3.0-spec-java (1.0.1-4fakesync) ...
2026-05-03T00:40:31.1918569Z Selecting previously unselected package libcdi-api-java.
2026-05-03T00:40:31.1996766Z Preparing to unpack .../046-libcdi-api-java_1.2-3_all.deb ...
2026-05-03T00:40:31.2004372Z Unpacking libcdi-api-java (1.2-3) ...
2026-05-03T00:40:31.2218053Z Selecting previously unselected package libcommons-cli-java.
2026-05-03T00:40:31.2295297Z Preparing to unpack .../047-libcommons-cli-java_1.6.0-1_all.deb ...
2026-05-03T00:40:31.2303048Z Unpacking libcommons-cli-java (1.6.0-1) ...
2026-05-03T00:40:31.2490586Z Selecting previously unselected package libcommons-parent-java.
2026-05-03T00:40:31.2569736Z Preparing to unpack .../048-libcommons-parent-java_56-1_all.deb ...
2026-05-03T00:40:31.2575999Z Unpacking libcommons-parent-java (56-1) ...
2026-05-03T00:40:31.2760266Z Selecting previously unselected package libcommons-io-java.
2026-05-03T00:40:31.2841610Z Preparing to unpack .../049-libcommons-io-java_2.11.0-2_all.deb ...
2026-05-03T00:40:31.2848732Z Unpacking libcommons-io-java (2.11.0-2) ...
2026-05-03T00:40:31.3043565Z Selecting previously unselected package libcommons-lang3-java.
2026-05-03T00:40:31.3126063Z Preparing to unpack .../050-libcommons-lang3-java_3.14.0-1_all.deb ...
2026-05-03T00:40:31.3133244Z Unpacking libcommons-lang3-java (3.14.0-1) ...
2026-05-03T00:40:31.3345841Z Selecting previously unselected package libegl-mesa0:amd64.
2026-05-03T00:40:31.3427262Z Preparing to unpack .../051-libegl-mesa0_25.2.8-0ubuntu0.24.04.1_amd64.deb ...
2026-05-03T00:40:31.3434639Z Unpacking libegl-mesa0:amd64 (25.2.8-0ubuntu0.24.04.1) ...
2026-05-03T00:40:31.3634166Z Selecting previously unselected package libegl1:amd64.
2026-05-03T00:40:31.3714306Z Preparing to unpack .../052-libegl1_1.7.0-1build1_amd64.deb ...
2026-05-03T00:40:31.3720951Z Unpacking libegl1:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:31.3899022Z Selecting previously unselected package xorg-sgml-doctools.
2026-05-03T00:40:31.3979642Z Preparing to unpack .../053-xorg-sgml-doctools_1%3a1.11-1.1_all.deb ...
2026-05-03T00:40:31.3985924Z Unpacking xorg-sgml-doctools (1:1.11-1.1) ...
2026-05-03T00:40:31.4200285Z Selecting previously unselected package x11proto-dev.
2026-05-03T00:40:31.4281376Z Preparing to unpack .../054-x11proto-dev_2023.2-1_all.deb ...
2026-05-03T00:40:31.4288237Z Unpacking x11proto-dev (2023.2-1) ...
2026-05-03T00:40:31.4755216Z Selecting previously unselected package libxau-dev:amd64.
2026-05-03T00:40:31.4838995Z Preparing to unpack .../055-libxau-dev_1%3a1.0.9-1build6_amd64.deb ...
2026-05-03T00:40:31.4854417Z Unpacking libxau-dev:amd64 (1:1.0.9-1build6) ...
2026-05-03T00:40:31.5045293Z Selecting previously unselected package libxdmcp-dev:amd64.
2026-05-03T00:40:31.5126859Z Preparing to unpack .../056-libxdmcp-dev_1%3a1.1.3-0ubuntu6_amd64.deb ...
2026-05-03T00:40:31.5134138Z Unpacking libxdmcp-dev:amd64 (1:1.1.3-0ubuntu6) ...
2026-05-03T00:40:31.5317355Z Selecting previously unselected package xtrans-dev.
2026-05-03T00:40:31.5400173Z Preparing to unpack .../057-xtrans-dev_1.4.0-1_all.deb ...
2026-05-03T00:40:31.5406977Z Unpacking xtrans-dev (1.4.0-1) ...
2026-05-03T00:40:31.5627761Z Selecting previously unselected package libpthread-stubs0-dev:amd64.
2026-05-03T00:40:31.5709250Z Preparing to unpack .../058-libpthread-stubs0-dev_0.4-1build3_amd64.deb ...
2026-05-03T00:40:31.5716207Z Unpacking libpthread-stubs0-dev:amd64 (0.4-1build3) ...
2026-05-03T00:40:31.5893551Z Selecting previously unselected package libxcb1-dev:amd64.
2026-05-03T00:40:31.5975485Z Preparing to unpack .../059-libxcb1-dev_1.15-1ubuntu2_amd64.deb ...
2026-05-03T00:40:31.5982584Z Unpacking libxcb1-dev:amd64 (1.15-1ubuntu2) ...
2026-05-03T00:40:31.6188310Z Selecting previously unselected package libx11-dev:amd64.
2026-05-03T00:40:31.6271624Z Preparing to unpack .../060-libx11-dev_2%3a1.8.7-1build1_amd64.deb ...
2026-05-03T00:40:31.6280004Z Unpacking libx11-dev:amd64 (2:1.8.7-1build1) ...
2026-05-03T00:40:31.6575439Z Selecting previously unselected package libglx-dev:amd64.
2026-05-03T00:40:31.6657320Z Preparing to unpack .../061-libglx-dev_1.7.0-1build1_amd64.deb ...
2026-05-03T00:40:31.6663442Z Unpacking libglx-dev:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:31.6846289Z Selecting previously unselected package libgl-dev:amd64.
2026-05-03T00:40:31.6929853Z Preparing to unpack .../062-libgl-dev_1.7.0-1build1_amd64.deb ...
2026-05-03T00:40:31.6937151Z Unpacking libgl-dev:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:31.7163127Z Selecting previously unselected package libegl-dev:amd64.
2026-05-03T00:40:31.7245377Z Preparing to unpack .../063-libegl-dev_1.7.0-1build1_amd64.deb ...
2026-05-03T00:40:31.7251986Z Unpacking libegl-dev:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:31.7440144Z Selecting previously unselected package libelf-dev:amd64.
2026-05-03T00:40:31.7522476Z Preparing to unpack .../064-libelf-dev_0.190-1.1ubuntu0.1_amd64.deb ...
2026-05-03T00:40:31.7530385Z Unpacking libelf-dev:amd64 (0.190-1.1ubuntu0.1) ...
2026-05-03T00:40:31.7739124Z Selecting previously unselected package libjsr305-java.
2026-05-03T00:40:31.7821769Z Preparing to unpack .../065-libjsr305-java_0.1~+svn49-11_all.deb ...
2026-05-03T00:40:31.7844196Z Unpacking libjsr305-java (0.1~+svn49-11) ...
2026-05-03T00:40:31.8070089Z Selecting previously unselected package libguava-java.
2026-05-03T00:40:31.8152316Z Preparing to unpack .../066-libguava-java_32.0.1-1_all.deb ...
2026-05-03T00:40:31.8159139Z Unpacking libguava-java (32.0.1-1) ...
2026-05-03T00:40:31.8435833Z Selecting previously unselected package liberror-prone-java.
2026-05-03T00:40:31.8518617Z Preparing to unpack .../067-liberror-prone-java_2.18.0-1_all.deb ...
2026-05-03T00:40:31.8525277Z Unpacking liberror-prone-java (2.18.0-1) ...
2026-05-03T00:40:31.8749314Z Selecting previously unselected package libgeronimo-annotation-1.3-spec-java.
2026-05-03T00:40:31.8831377Z Preparing to unpack .../068-libgeronimo-annotation-1.3-spec-java_1.3-1_all.deb ...
2026-05-03T00:40:31.8838371Z Unpacking libgeronimo-annotation-1.3-spec-java (1.3-1) ...
2026-05-03T00:40:31.9058355Z Selecting previously unselected package libgles1:amd64.
2026-05-03T00:40:31.9140410Z Preparing to unpack .../069-libgles1_1.7.0-1build1_amd64.deb ...
2026-05-03T00:40:31.9147838Z Unpacking libgles1:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:31.9333026Z Selecting previously unselected package libgles2:amd64.
2026-05-03T00:40:31.9415843Z Preparing to unpack .../070-libgles2_1.7.0-1build1_amd64.deb ...
2026-05-03T00:40:31.9429286Z Unpacking libgles2:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:31.9613433Z Selecting previously unselected package libgles-dev:amd64.
2026-05-03T00:40:31.9694936Z Preparing to unpack .../071-libgles-dev_1.7.0-1build1_amd64.deb ...
2026-05-03T00:40:31.9702045Z Unpacking libgles-dev:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:31.9919333Z Selecting previously unselected package libaopalliance-java.
2026-05-03T00:40:32.0000147Z Preparing to unpack .../072-libaopalliance-java_20070526-7_all.deb ...
2026-05-03T00:40:32.0006607Z Unpacking libaopalliance-java (20070526-7) ...
2026-05-03T00:40:32.0180428Z Selecting previously unselected package libguice-java.
2026-05-03T00:40:32.0259144Z Preparing to unpack .../073-libguice-java_4.2.3-2_all.deb ...
2026-05-03T00:40:32.0265714Z Unpacking libguice-java (4.2.3-2) ...
2026-05-03T00:40:32.1484060Z Selecting previously unselected package libjansi-java.
2026-05-03T00:40:32.1567682Z Preparing to unpack .../074-libjansi-java_2.4.1-2_all.deb ...
2026-05-03T00:40:32.1574402Z Unpacking libjansi-java (2.4.1-2) ...
2026-05-03T00:40:32.1755205Z Selecting previously unselected package libmaven-parent-java.
2026-05-03T00:40:32.1835907Z Preparing to unpack .../075-libmaven-parent-java_35-1_all.deb ...
2026-05-03T00:40:32.1842846Z Unpacking libmaven-parent-java (35-1) ...
2026-05-03T00:40:32.2054470Z Selecting previously unselected package libplexus-utils2-java.
2026-05-03T00:40:32.2136485Z Preparing to unpack .../076-libplexus-utils2-java_3.4.2-1_all.deb ...
2026-05-03T00:40:32.2143529Z Unpacking libplexus-utils2-java (3.4.2-1) ...
2026-05-03T00:40:32.2346201Z Selecting previously unselected package libwagon-provider-api-java.
2026-05-03T00:40:32.2428172Z Preparing to unpack .../077-libwagon-provider-api-java_3.5.3-1_all.deb ...
2026-05-03T00:40:32.2435468Z Unpacking libwagon-provider-api-java (3.5.3-1) ...
2026-05-03T00:40:32.2634839Z Selecting previously unselected package libmaven-resolver-java.
2026-05-03T00:40:32.2723155Z Preparing to unpack .../078-libmaven-resolver-java_1.6.3-1_all.deb ...
2026-05-03T00:40:32.2734933Z Unpacking libmaven-resolver-java (1.6.3-1) ...
2026-05-03T00:40:32.3035423Z Selecting previously unselected package libmaven-shared-utils-java.
2026-05-03T00:40:32.3117344Z Preparing to unpack .../079-libmaven-shared-utils-java_3.3.4-1_all.deb ...
2026-05-03T00:40:32.3124065Z Unpacking libmaven-shared-utils-java (3.3.4-1) ...
2026-05-03T00:40:32.3448385Z Selecting previously unselected package libplexus-cipher-java.
2026-05-03T00:40:32.3530469Z Preparing to unpack .../080-libplexus-cipher-java_2.0-1_all.deb ...
2026-05-03T00:40:32.3537718Z Unpacking libplexus-cipher-java (2.0-1) ...
2026-05-03T00:40:32.3731838Z Selecting previously unselected package libplexus-classworlds-java.
2026-05-03T00:40:32.3814283Z Preparing to unpack .../081-libplexus-classworlds-java_2.7.0-1_all.deb ...
2026-05-03T00:40:32.3823325Z Unpacking libplexus-classworlds-java (2.7.0-1) ...
2026-05-03T00:40:32.4020285Z Selecting previously unselected package libplexus-component-annotations-java.
2026-05-03T00:40:32.4103308Z Preparing to unpack .../082-libplexus-component-annotations-java_2.1.1-1_all.deb ...
2026-05-03T00:40:32.4110608Z Unpacking libplexus-component-annotations-java (2.1.1-1) ...
2026-05-03T00:40:32.4302281Z Selecting previously unselected package libplexus-interpolation-java.
2026-05-03T00:40:32.4384795Z Preparing to unpack .../083-libplexus-interpolation-java_1.26-1_all.deb ...
2026-05-03T00:40:32.4391838Z Unpacking libplexus-interpolation-java (1.26-1) ...
2026-05-03T00:40:32.4628923Z Selecting previously unselected package libplexus-sec-dispatcher-java.
2026-05-03T00:40:32.4711543Z Preparing to unpack .../084-libplexus-sec-dispatcher-java_2.0-3_all.deb ...
2026-05-03T00:40:32.4721162Z Unpacking libplexus-sec-dispatcher-java (2.0-3) ...
2026-05-03T00:40:32.4913453Z Selecting previously unselected package libslf4j-java.
2026-05-03T00:40:32.4995410Z Preparing to unpack .../085-libslf4j-java_1.7.32-1_all.deb ...
2026-05-03T00:40:32.5002484Z Unpacking libslf4j-java (1.7.32-1) ...
2026-05-03T00:40:32.5288794Z Selecting previously unselected package libsisu-inject-java.
2026-05-03T00:40:32.5370855Z Preparing to unpack .../086-libsisu-inject-java_0.3.4-2_all.deb ...
2026-05-03T00:40:32.5377298Z Unpacking libsisu-inject-java (0.3.4-2) ...
2026-05-03T00:40:32.5794324Z Selecting previously unselected package libsisu-plexus-java.
2026-05-03T00:40:32.5876920Z Preparing to unpack .../087-libsisu-plexus-java_0.3.4-3_all.deb ...
2026-05-03T00:40:32.5885386Z Unpacking libsisu-plexus-java (0.3.4-3) ...
2026-05-03T00:40:32.6195941Z Selecting previously unselected package libmaven3-core-java.
2026-05-03T00:40:32.6280192Z Preparing to unpack .../088-libmaven3-core-java_3.8.7-2_all.deb ...
2026-05-03T00:40:32.6289279Z Unpacking libmaven3-core-java (3.8.7-2) ...
2026-05-03T00:40:32.6693133Z Selecting previously unselected package libopengl0:amd64.
2026-05-03T00:40:32.6777624Z Preparing to unpack .../089-libopengl0_1.7.0-1build1_amd64.deb ...
2026-05-03T00:40:32.6783781Z Unpacking libopengl0:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:32.6975380Z Selecting previously unselected package libopengl-dev:amd64.
2026-05-03T00:40:32.7058883Z Preparing to unpack .../090-libopengl-dev_1.7.0-1build1_amd64.deb ...
2026-05-03T00:40:32.7065874Z Unpacking libopengl-dev:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:32.7247186Z Selecting previously unselected package libwagon-file-java.
2026-05-03T00:40:32.7330528Z Preparing to unpack .../091-libwagon-file-java_3.5.3-1_all.deb ...
2026-05-03T00:40:32.7337053Z Unpacking libwagon-file-java (3.5.3-1) ...
2026-05-03T00:40:32.7519881Z Selecting previously unselected package libwagon-http-shaded-java.
2026-05-03T00:40:32.7603144Z Preparing to unpack .../092-libwagon-http-shaded-java_3.5.3-1_all.deb ...
2026-05-03T00:40:32.7609709Z Unpacking libwagon-http-shaded-java (3.5.3-1) ...
2026-05-03T00:40:32.7839439Z Selecting previously unselected package libxml-simple-perl.
2026-05-03T00:40:32.7922169Z Preparing to unpack .../093-libxml-simple-perl_2.25-2_all.deb ...
2026-05-03T00:40:32.7929234Z Unpacking libxml-simple-perl (2.25-2) ...
2026-05-03T00:40:32.8121835Z Selecting previously unselected package libxml2-utils.
2026-05-03T00:40:32.8205648Z Preparing to unpack .../094-libxml2-utils_2.9.14+dfsg-1.3ubuntu3.7_amd64.deb ...
2026-05-03T00:40:32.8212448Z Unpacking libxml2-utils (2.9.14+dfsg-1.3ubuntu3.7) ...
2026-05-03T00:40:32.8401467Z Selecting previously unselected package lzop.
2026-05-03T00:40:32.8486228Z Preparing to unpack .../095-lzop_1.04-2build3_amd64.deb ...
2026-05-03T00:40:32.8493455Z Unpacking lzop (1.04-2build3) ...
2026-05-03T00:40:32.8706574Z Selecting previously unselected package maven.
2026-05-03T00:40:32.8790136Z Preparing to unpack .../096-maven_3.8.7-2_all.deb ...
2026-05-03T00:40:32.8796704Z Unpacking maven (3.8.7-2) ...
2026-05-03T00:40:32.9046548Z Selecting previously unselected package optipng.
2026-05-03T00:40:32.9131185Z Preparing to unpack .../097-optipng_0.7.8+ds-1build2_amd64.deb ...
2026-05-03T00:40:32.9137878Z Unpacking optipng (0.7.8+ds-1build2) ...
2026-05-03T00:40:32.9344696Z Selecting previously unselected package pngcrush.
2026-05-03T00:40:32.9429939Z Preparing to unpack .../098-pngcrush_1.8.13-1build2_amd64.deb ...
2026-05-03T00:40:32.9437275Z Unpacking pngcrush (1.8.13-1build2) ...
2026-05-03T00:40:32.9625080Z Selecting previously unselected package pwgen.
2026-05-03T00:40:32.9708926Z Preparing to unpack .../099-pwgen_2.08-2build2_amd64.deb ...
2026-05-03T00:40:32.9715687Z Unpacking pwgen (2.08-2build2) ...
2026-05-03T00:40:32.9894550Z Selecting previously unselected package xsltproc.
2026-05-03T00:40:32.9977391Z Preparing to unpack .../100-xsltproc_1.1.39-0exp1ubuntu0.24.04.3_amd64.deb ...
2026-05-03T00:40:32.9984342Z Unpacking xsltproc (1.1.39-0exp1ubuntu0.24.04.3) ...
2026-05-03T00:40:33.0164069Z Selecting previously unselected package libfdt1:amd64.
2026-05-03T00:40:33.0245121Z Preparing to unpack .../101-libfdt1_1.7.0-2build1_amd64.deb ...
2026-05-03T00:40:33.0252082Z Unpacking libfdt1:amd64 (1.7.0-2build1) ...
2026-05-03T00:40:33.0429740Z Selecting previously unselected package device-tree-compiler.
2026-05-03T00:40:33.0511717Z Preparing to unpack .../102-device-tree-compiler_1.7.0-2build1_amd64.deb ...
2026-05-03T00:40:33.0518324Z Unpacking device-tree-compiler (1.7.0-2build1) ...
2026-05-03T00:40:33.0748273Z Selecting previously unselected package libglvnd-core-dev:amd64.
2026-05-03T00:40:33.0831436Z Preparing to unpack .../103-libglvnd-core-dev_1.7.0-1build1_amd64.deb ...
2026-05-03T00:40:33.0838786Z Unpacking libglvnd-core-dev:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:33.1027319Z Selecting previously unselected package libglvnd-dev:amd64.
2026-05-03T00:40:33.1110203Z Preparing to unpack .../104-libglvnd-dev_1.7.0-1build1_amd64.deb ...
2026-05-03T00:40:33.1117974Z Unpacking libglvnd-dev:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:33.1297150Z Selecting previously unselected package libgl1-mesa-dev:amd64.
2026-05-03T00:40:33.1380931Z Preparing to unpack .../105-libgl1-mesa-dev_25.2.8-0ubuntu0.24.04.1_amd64.deb ...
2026-05-03T00:40:33.1387727Z Unpacking libgl1-mesa-dev:amd64 (25.2.8-0ubuntu0.24.04.1) ...
2026-05-03T00:40:33.1572069Z Selecting previously unselected package liblz4-tool.
2026-05-03T00:40:33.1655112Z Preparing to unpack .../106-liblz4-tool_1.9.4-1build1.1_all.deb ...
2026-05-03T00:40:33.1663512Z Unpacking liblz4-tool (1.9.4-1build1.1) ...
2026-05-03T00:40:33.1836380Z Selecting previously unselected package schedtool.
2026-05-03T00:40:33.1918834Z Preparing to unpack .../107-schedtool_1.3.0-4_amd64.deb ...
2026-05-03T00:40:33.1926708Z Unpacking schedtool (1.3.0-4) ...
2026-05-03T00:40:33.2337288Z Setting up bzip2-doc (1.0.8-5.1build0.1) ...
2026-05-03T00:40:33.2360047Z Setting up libslf4j-java (1.7.32-1) ...
2026-05-03T00:40:33.2375543Z Setting up libplexus-utils2-java (3.4.2-1) ...
2026-05-03T00:40:33.2397093Z Setting up libncurses-dev:amd64 (6.4+20240113-1ubuntu2) ...
2026-05-03T00:40:33.2414269Z Setting up libplexus-classworlds-java (2.7.0-1) ...
2026-05-03T00:40:33.2430343Z Setting up libjsr305-java (0.1~+svn49-11) ...
2026-05-03T00:40:33.2452393Z Setting up libglvnd-core-dev:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:33.2470597Z Setting up libaopalliance-java (20070526-7) ...
2026-05-03T00:40:33.2488791Z Setting up libcommons-cli-java (1.6.0-1) ...
2026-05-03T00:40:33.2505617Z Setting up libjq1:amd64 (1.7.1-3ubuntu0.24.04.2) ...
2026-05-03T00:40:33.2529095Z Setting up pngcrush (1.8.13-1build2) ...
2026-05-03T00:40:33.2548591Z Setting up xsltproc (1.1.39-0exp1ubuntu0.24.04.3) ...
2026-05-03T00:40:33.2566206Z Setting up libplexus-component-annotations-java (2.1.1-1) ...
2026-05-03T00:40:33.2584768Z Setting up libfdt1:amd64 (1.7.0-2build1) ...
2026-05-03T00:40:33.2603766Z Setting up gperf (3.1-1build1) ...
2026-05-03T00:40:33.2626532Z Setting up libpthread-stubs0-dev:amd64 (0.4-1build3) ...
2026-05-03T00:40:33.2643718Z Setting up libopengl0:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:33.2661033Z Setting up libc6-x32 (2.39-0ubuntu8.7) ...
2026-05-03T00:40:33.2701134Z Setting up libgeronimo-annotation-1.3-spec-java (1.3-1) ...
2026-05-03T00:40:33.2722260Z Setting up libgeronimo-interceptor-3.0-spec-java (1.0.1-4fakesync) ...
2026-05-03T00:40:33.2740471Z Setting up xtrans-dev (1.4.0-1) ...
2026-05-03T00:40:33.2759066Z Setting up libegl-mesa0:amd64 (25.2.8-0ubuntu0.24.04.1) ...
2026-05-03T00:40:33.2779368Z Setting up libgles2:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:33.2799644Z Setting up optipng (0.7.8+ds-1build2) ...
2026-05-03T00:40:33.2815866Z Setting up libjansi-java (2.4.1-2) ...
2026-05-03T00:40:33.2833657Z Setting up libapache-pom-java (29-2) ...
2026-05-03T00:40:33.2855131Z Setting up libatinject-jsr330-api-java (1.0+ds1-5) ...
2026-05-03T00:40:33.2873162Z Setting up libgles1:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:33.2891738Z Setting up libplexus-interpolation-java (1.26-1) ...
2026-05-03T00:40:33.2910407Z Setting up libelf-dev:amd64 (0.190-1.1ubuntu0.1) ...
2026-05-03T00:40:33.2928245Z Setting up device-tree-compiler (1.7.0-2build1) ...
2026-05-03T00:40:33.2944854Z Setting up libxml-simple-perl (2.25-2) ...
2026-05-03T00:40:33.2963531Z Setting up libx32gomp1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:33.2980199Z Setting up liblz4-tool (1.9.4-1build1.1) ...
2026-05-03T00:40:33.3000415Z Setting up jq (1.7.1-3ubuntu0.24.04.2) ...
2026-05-03T00:40:33.3019153Z Setting up lzop (1.04-2build3) ...
2026-05-03T00:40:33.3035922Z Setting up libegl1:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:33.3053291Z Setting up libc6-i386 (2.39-0ubuntu8.7) ...
2026-05-03T00:40:33.3100829Z Setting up build-essential (12.10ubuntu1) ...
2026-05-03T00:40:33.3118057Z Setting up libx32quadmath0 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:33.3137406Z Setting up xorg-sgml-doctools (1:1.11-1.1) ...
2026-05-03T00:40:33.3154186Z Setting up libwagon-http-shaded-java (3.5.3-1) ...
2026-05-03T00:40:33.3172542Z Setting up libopengl-dev:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:33.3188334Z Setting up libxml2-utils (2.9.14+dfsg-1.3ubuntu3.7) ...
2026-05-03T00:40:33.3206696Z Setting up libcdi-api-java (1.2-3) ...
2026-05-03T00:40:33.3225862Z Setting up libhiredis1.1.0:amd64 (1.2.0-6ubuntu3) ...
2026-05-03T00:40:33.3242644Z Setting up pwgen (2.08-2build2) ...
2026-05-03T00:40:33.3262922Z Setting up lib32atomic1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:33.3281291Z Setting up schedtool (1.3.0-4) ...
2026-05-03T00:40:33.3298919Z Setting up libbz2-dev:amd64 (1.0.8-5.1build0.1) ...
2026-05-03T00:40:33.3317623Z Setting up libx32atomic1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:33.3336851Z Setting up libwagon-provider-api-java (3.5.3-1) ...
2026-05-03T00:40:33.3357203Z Setting up lib32z1 (1:1.3.dfsg-3.1ubuntu2.1) ...
2026-05-03T00:40:33.3375040Z Setting up libc6-dev-i386 (2.39-0ubuntu8.7) ...
2026-05-03T00:40:33.3394688Z Setting up lib32itm1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:33.3415424Z Setting up libx32gcc-s1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:33.3432694Z Setting up libmaven-parent-java (35-1) ...
2026-05-03T00:40:33.3453286Z Setting up ccache (4.9.1-1) ...
2026-05-03T00:40:33.3476783Z Updating symlinks in /usr/lib/ccache ...
2026-05-03T00:40:33.3554370Z Setting up libcommons-parent-java (56-1) ...
2026-05-03T00:40:33.3572825Z Setting up libsisu-inject-java (0.3.4-2) ...
2026-05-03T00:40:33.3592998Z Setting up libx32itm1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:33.3610480Z Setting up libplexus-cipher-java (2.0-1) ...
2026-05-03T00:40:33.3630190Z Setting up libx32asan8 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:33.3647562Z Setting up libc6-dev-x32 (2.39-0ubuntu8.7) ...
2026-05-03T00:40:33.3667043Z Setting up libsisu-plexus-java (0.3.4-3) ...
2026-05-03T00:40:33.3687307Z Setting up lib32gomp1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:33.3705202Z Setting up lib32gcc-s1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:33.3724915Z Setting up lib32stdc++6 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:33.3757150Z Setting up lib32asan8 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:33.3774005Z Setting up lib32z1-dev (1:1.3.dfsg-3.1ubuntu2.1) ...
2026-05-03T00:40:33.3794140Z Setting up libcommons-lang3-java (3.14.0-1) ...
2026-05-03T00:40:33.3814719Z Setting up lib32tinfo6 (6.4+20240113-1ubuntu2) ...
2026-05-03T00:40:33.3832036Z Setting up lib32quadmath0 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:33.3852197Z Setting up libplexus-sec-dispatcher-java (2.0-3) ...
2026-05-03T00:40:33.3871387Z Setting up libwagon-file-java (3.5.3-1) ...
2026-05-03T00:40:33.3889989Z Setting up libx32stdc++6 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:33.3909508Z Setting up libx32ubsan1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:33.3930556Z Setting up libcommons-io-java (2.11.0-2) ...
2026-05-03T00:40:33.3947264Z Setting up lib32ncurses6 (6.4+20240113-1ubuntu2) ...
2026-05-03T00:40:33.3967860Z Setting up lib32ncursesw6 (6.4+20240113-1ubuntu2) ...
2026-05-03T00:40:33.3985343Z Setting up lib32ubsan1 (14.2.0-4ubuntu2~24.04.1) ...
2026-05-03T00:40:33.4005631Z Setting up lib32gcc-13-dev (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T00:40:33.4026740Z Setting up libmaven-resolver-java (1.6.3-1) ...
2026-05-03T00:40:33.4152763Z Setting up libx32gcc-13-dev (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T00:40:33.4172092Z Setting up libmaven-shared-utils-java (3.3.4-1) ...
2026-05-03T00:40:33.4188815Z Setting up gcc-13-multilib (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T00:40:33.4205862Z Setting up lib32stdc++-13-dev (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T00:40:33.4225464Z Setting up gcc-multilib (4:13.2.0-7ubuntu1) ...
2026-05-03T00:40:33.4242314Z Setting up lib32ncurses-dev (6.4+20240113-1ubuntu2) ...
2026-05-03T00:40:33.4259714Z Setting up libx32stdc++-13-dev (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T00:40:33.4279270Z Setting up g++-13-multilib (13.3.0-6ubuntu2~24.04.1) ...
2026-05-03T00:40:33.4295983Z Setting up g++-multilib (4:13.2.0-7ubuntu1) ...
2026-05-03T00:40:33.4345642Z Setting up liberror-prone-java (2.18.0-1) ...
2026-05-03T00:40:33.4379281Z Setting up libguava-java (32.0.1-1) ...
2026-05-03T00:40:33.4425607Z Setting up libguice-java (4.2.3-2) ...
2026-05-03T00:40:33.4466884Z Setting up libmaven3-core-java (3.8.7-2) ...
2026-05-03T00:40:33.4490156Z Setting up maven (3.8.7-2) ...
2026-05-03T00:40:33.4578234Z update-alternatives: using /usr/share/maven/bin/mvn to provide /usr/bin/mvn (mvn) in auto mode
2026-05-03T00:40:33.4661002Z Processing triggers for man-db (2.12.0-4build2) ...
2026-05-03T00:40:33.4677977Z Not building database; man-db/auto-update is not 'true'.
2026-05-03T00:40:33.4698956Z Processing triggers for sgml-base (1.31) ...
2026-05-03T00:40:33.4809578Z Processing triggers for install-info (7.1-3build2) ...
2026-05-03T00:40:33.5723877Z Setting up x11proto-dev (2023.2-1) ...
2026-05-03T00:40:33.5749322Z Setting up libxau-dev:amd64 (1:1.0.9-1build6) ...
2026-05-03T00:40:33.5776493Z Processing triggers for libc-bin (2.39-0ubuntu8.7) ...
2026-05-03T00:40:33.5949171Z Setting up libxdmcp-dev:amd64 (1:1.1.3-0ubuntu6) ...
2026-05-03T00:40:33.5983229Z Setting up libxcb1-dev:amd64 (1.15-1ubuntu2) ...
2026-05-03T00:40:33.6007416Z Setting up libx11-dev:amd64 (2:1.8.7-1build1) ...
2026-05-03T00:40:33.6048295Z Setting up libglx-dev:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:33.6077915Z Setting up libgl-dev:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:33.6105366Z Setting up libegl-dev:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:33.6141216Z Setting up libgles-dev:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:33.6163375Z Setting up libglvnd-dev:amd64 (1.7.0-1build1) ...
2026-05-03T00:40:33.6189163Z Setting up libgl1-mesa-dev:amd64 (25.2.8-0ubuntu0.24.04.1) ...
2026-05-03T00:40:34.1963195Z 
2026-05-03T00:40:34.1963670Z Running kernel seems to be up-to-date.
2026-05-03T00:40:34.1964038Z 
2026-05-03T00:40:34.1964178Z No services need to be restarted.
2026-05-03T00:40:34.1964468Z 
2026-05-03T00:40:34.1964588Z No containers need to be restarted.
2026-05-03T00:40:34.1964767Z 
2026-05-03T00:40:34.1964884Z No user sessions are running outdated binaries.
2026-05-03T00:40:34.1965080Z 
2026-05-03T00:40:34.1965275Z No VM guests are running outdated hypervisor (qemu) binaries on this host.
2026-05-03T00:40:35.2973109Z ##[group]Run ZYCLANG=$(curl -sI https://github.com/ZyCromerZ/Clang/releases/latest | awk -F/ '/location:/ {print $NF}' | tr -d '\r')
2026-05-03T00:40:35.2974033Z [36;1mZYCLANG=$(curl -sI https://github.com/ZyCromerZ/Clang/releases/latest | awk -F/ '/location:/ {print $NF}' | tr -d '\r')[0m
2026-05-03T00:40:35.2974838Z [36;1mZYASSET=$(curl -sL https://github.com/ZyCromerZ/Clang/releases/expanded_assets/$ZYCLANG | grep -oP '[^/"]+\.tar.gz' | head -n1)[0m
2026-05-03T00:40:35.2975534Z [36;1mZYCLANG_DLINK="https://github.com/ZyCromerZ/Clang/releases/latest/download/$ZYASSET"[0m
2026-05-03T00:40:35.2975942Z [36;1m[0m
2026-05-03T00:40:35.2976146Z [36;1mecho "Downloading: $ZYCLANG_DLINK"[0m
2026-05-03T00:40:35.2976439Z [36;1mmkdir -p $GITHUB_WORKSPACE/ZyClang[0m
2026-05-03T00:40:35.2976776Z [36;1maria2c -s16 -x16 -k1M "$ZYCLANG_DLINK" -o ZyClang.tar.gz[0m
2026-05-03T00:40:35.2977159Z [36;1mtar -C $GITHUB_WORKSPACE/ZyClang/ -zxf ZyClang.tar.gz[0m
2026-05-03T00:40:35.2977502Z [36;1mrm -f ZyClang.tar.gz[0m
2026-05-03T00:40:35.2977718Z [36;1m[0m
2026-05-03T00:40:35.2978023Z [36;1mCLANG_VERSION=$($GITHUB_WORKSPACE/ZyClang/bin/clang --version | head -n 1)[0m
2026-05-03T00:40:35.2979110Z [36;1mLLD_VERSION=$($GITHUB_WORKSPACE/ZyClang/bin/ld.lld --version | head -n 1)[0m
2026-05-03T00:40:35.2979540Z [36;1mecho "CLANG_VERSION=$CLANG_VERSION" >> $GITHUB_ENV[0m
2026-05-03T00:40:35.2979883Z [36;1mecho "LLD_VERSION=$LLD_VERSION" >> $GITHUB_ENV[0m
2026-05-03T00:40:35.2980170Z [36;1mecho "Clang: $CLANG_VERSION"[0m
2026-05-03T00:40:35.2980422Z [36;1mecho "LLD: $LLD_VERSION"[0m
2026-05-03T00:40:35.3002497Z shell: /usr/bin/bash -e {0}
2026-05-03T00:40:35.3002736Z env:
2026-05-03T00:40:35.3002929Z   KERNEL_NAME: Castorice
2026-05-03T00:40:35.3003149Z   DEVICE_CODE: fire
2026-05-03T00:40:35.3003369Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:40:35.3003619Z   CLANG_VERSION: 
2026-05-03T00:40:35.3003813Z   LLD_VERSION: 
2026-05-03T00:40:35.3003992Z   KERNEL_HEAD_HASH: 
2026-05-03T00:40:35.3004186Z   KSU_DIR: 
2026-05-03T00:40:35.3004348Z   KSU_VERSION: 
2026-05-03T00:40:35.3004522Z   KERNEL_VERSION: 
2026-05-03T00:40:35.3004699Z   ZIP_NAME: 
2026-05-03T00:40:35.3004878Z ##[endgroup]
2026-05-03T00:40:35.7491543Z Downloading: https://github.com/ZyCromerZ/Clang/releases/latest/download/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:35.8374113Z 
2026-05-03T00:40:35.8375050Z 05/03 00:40:35 [[1;32mNOTICE[0m] Downloading 1 item(s)
2026-05-03T00:40:35.9548947Z 
2026-05-03T00:40:35.9550478Z 05/03 00:40:35 [[1;32mNOTICE[0m] CUID#7 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.0760389Z 
2026-05-03T00:40:36.0766960Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#7 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A35%3A47Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A35%3A10Z&ske=2026-05-03T01%3A35%3A47Z&sks=b&skv=2018-11-09&sig=%2FApodlWbLr2XR9PmNlFdO%2BzhdspRFw96VwSlm1PpgjA%3D&jwt=***
2026-05-03T00:40:36.1615037Z 
2026-05-03T00:40:36.1616517Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#9 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.2123350Z 
2026-05-03T00:40:36.2124813Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#14 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.2126048Z 
2026-05-03T00:40:36.2126985Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#11 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.2132902Z 
2026-05-03T00:40:36.2134343Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#13 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.2153373Z 
2026-05-03T00:40:36.2154369Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#15 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.2175209Z 
2026-05-03T00:40:36.2176174Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#16 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.2195698Z 
2026-05-03T00:40:36.2196656Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#19 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.2218092Z 
2026-05-03T00:40:36.2219269Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#20 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.2236624Z 
2026-05-03T00:40:36.2237555Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#23 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.2320983Z 
2026-05-03T00:40:36.2321912Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#21 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.2331915Z 
2026-05-03T00:40:36.2332618Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#10 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.2346518Z 
2026-05-03T00:40:36.2347291Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#12 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.2364553Z 
2026-05-03T00:40:36.2365363Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#18 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.2396650Z 
2026-05-03T00:40:36.2402738Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#13 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A24%3A31Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A23%3A59Z&ske=2026-05-03T01%3A24%3A31Z&sks=b&skv=2018-11-09&sig=ynMlwNf2UKF0v2i4EESeuYPBsFAOWPqcyh08tJVcMTk%3D&jwt=***
2026-05-03T00:40:36.2405879Z 
2026-05-03T00:40:36.2410660Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#14 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A24%3A31Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A23%3A59Z&ske=2026-05-03T01%3A24%3A31Z&sks=b&skv=2018-11-09&sig=ynMlwNf2UKF0v2i4EESeuYPBsFAOWPqcyh08tJVcMTk%3D&jwt=***
2026-05-03T00:40:36.2413267Z 
2026-05-03T00:40:36.2420782Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#9 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A24%3A31Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A23%3A59Z&ske=2026-05-03T01%3A24%3A31Z&sks=b&skv=2018-11-09&sig=ynMlwNf2UKF0v2i4EESeuYPBsFAOWPqcyh08tJVcMTk%3D&jwt=***
2026-05-03T00:40:36.2422523Z 
2026-05-03T00:40:36.2427072Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#11 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A24%3A31Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A23%3A59Z&ske=2026-05-03T01%3A24%3A31Z&sks=b&skv=2018-11-09&sig=ynMlwNf2UKF0v2i4EESeuYPBsFAOWPqcyh08tJVcMTk%3D&jwt=***
2026-05-03T00:40:36.2429036Z 
2026-05-03T00:40:36.2433425Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#15 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A24%3A31Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A23%3A59Z&ske=2026-05-03T01%3A24%3A31Z&sks=b&skv=2018-11-09&sig=ynMlwNf2UKF0v2i4EESeuYPBsFAOWPqcyh08tJVcMTk%3D&jwt=***
2026-05-03T00:40:36.2435157Z 
2026-05-03T00:40:36.2435709Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#22 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.2436225Z 
2026-05-03T00:40:36.2442699Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#16 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A24%3A31Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A23%3A59Z&ske=2026-05-03T01%3A24%3A31Z&sks=b&skv=2018-11-09&sig=ynMlwNf2UKF0v2i4EESeuYPBsFAOWPqcyh08tJVcMTk%3D&jwt=***
2026-05-03T00:40:36.2444441Z 
2026-05-03T00:40:36.2449165Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#19 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A24%3A31Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A23%3A59Z&ske=2026-05-03T01%3A24%3A31Z&sks=b&skv=2018-11-09&sig=ynMlwNf2UKF0v2i4EESeuYPBsFAOWPqcyh08tJVcMTk%3D&jwt=***
2026-05-03T00:40:36.2454588Z 
2026-05-03T00:40:36.2455642Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#17 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.2456784Z 
2026-05-03T00:40:36.2462784Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#20 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A24%3A31Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A23%3A59Z&ske=2026-05-03T01%3A24%3A31Z&sks=b&skv=2018-11-09&sig=ynMlwNf2UKF0v2i4EESeuYPBsFAOWPqcyh08tJVcMTk%3D&jwt=***
2026-05-03T00:40:36.2476253Z 
2026-05-03T00:40:36.2483115Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#23 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A24%3A31Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A23%3A59Z&ske=2026-05-03T01%3A24%3A31Z&sks=b&skv=2018-11-09&sig=ynMlwNf2UKF0v2i4EESeuYPBsFAOWPqcyh08tJVcMTk%3D&jwt=***
2026-05-03T00:40:36.2575469Z 
2026-05-03T00:40:36.2582380Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#21 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A24%3A31Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A23%3A59Z&ske=2026-05-03T01%3A24%3A31Z&sks=b&skv=2018-11-09&sig=ynMlwNf2UKF0v2i4EESeuYPBsFAOWPqcyh08tJVcMTk%3D&jwt=***
2026-05-03T00:40:36.2636530Z 
2026-05-03T00:40:36.2642744Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#10 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A24%3A31Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A23%3A59Z&ske=2026-05-03T01%3A24%3A31Z&sks=b&skv=2018-11-09&sig=ynMlwNf2UKF0v2i4EESeuYPBsFAOWPqcyh08tJVcMTk%3D&jwt=***
2026-05-03T00:40:36.2646031Z 
2026-05-03T00:40:36.2647242Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#9 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.2648177Z 
2026-05-03T00:40:36.2649305Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#14 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.2650117Z 
2026-05-03T00:40:36.2650901Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#15 - Redirecting to https://github.com/ZyCromerZ/Clang/releases/download/15.0.7-20260208-release/Clang-15.0.7-20260208.tar.gz
2026-05-03T00:40:36.2661068Z 
2026-05-03T00:40:36.2669521Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#22 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A24%3A31Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A23%3A59Z&ske=2026-05-03T01%3A24%3A31Z&sks=b&skv=2018-11-09&sig=ynMlwNf2UKF0v2i4EESeuYPBsFAOWPqcyh08tJVcMTk%3D&jwt=***
2026-05-03T00:40:36.2672713Z 
2026-05-03T00:40:36.2680839Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#12 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A24%3A31Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A23%3A59Z&ske=2026-05-03T01%3A24%3A31Z&sks=b&skv=2018-11-09&sig=ynMlwNf2UKF0v2i4EESeuYPBsFAOWPqcyh08tJVcMTk%3D&jwt=***
2026-05-03T00:40:36.2689389Z 
2026-05-03T00:40:36.2694772Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#18 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A24%3A31Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A23%3A59Z&ske=2026-05-03T01%3A24%3A31Z&sks=b&skv=2018-11-09&sig=ynMlwNf2UKF0v2i4EESeuYPBsFAOWPqcyh08tJVcMTk%3D&jwt=***
2026-05-03T00:40:36.2718347Z 
2026-05-03T00:40:36.2723977Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#17 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A24%3A31Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A23%3A59Z&ske=2026-05-03T01%3A24%3A31Z&sks=b&skv=2018-11-09&sig=ynMlwNf2UKF0v2i4EESeuYPBsFAOWPqcyh08tJVcMTk%3D&jwt=***
2026-05-03T00:40:36.2886950Z 
2026-05-03T00:40:36.2892530Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#14 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A24%3A31Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A23%3A59Z&ske=2026-05-03T01%3A24%3A31Z&sks=b&skv=2018-11-09&sig=ynMlwNf2UKF0v2i4EESeuYPBsFAOWPqcyh08tJVcMTk%3D&jwt=***
2026-05-03T00:40:36.2897590Z 
2026-05-03T00:40:36.2905522Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#15 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A24%3A31Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A23%3A59Z&ske=2026-05-03T01%3A24%3A31Z&sks=b&skv=2018-11-09&sig=ynMlwNf2UKF0v2i4EESeuYPBsFAOWPqcyh08tJVcMTk%3D&jwt=***
2026-05-03T00:40:36.2964291Z 
2026-05-03T00:40:36.2972447Z 05/03 00:40:36 [[1;32mNOTICE[0m] CUID#9 - Redirecting to https://release-assets.githubusercontent.com/github-production-release-asset/430970692/dbc32bf4-e958-4c56-bba3-2fbaefe83f39?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-05-03T01%3A24%3A31Z&rscd=attachment%3B+filename%3DClang-15.0.7-20260208.tar.gz&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-05-03T00%3A23%3A59Z&ske=2026-05-03T01%3A24%3A31Z&sks=b&skv=2018-11-09&sig=ynMlwNf2UKF0v2i4EESeuYPBsFAOWPqcyh08tJVcMTk%3D&jwt=***
2026-05-03T00:40:38.6960170Z [#e2343d 255MiB/580MiB(44%) CN:16 DL:365MiB]
2026-05-03T00:40:38.6960433Z 
2026-05-03T00:40:38.6961161Z 05/03 00:40:38 [[1;32mNOTICE[0m] Download complete: /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/ZyClang.tar.gz
2026-05-03T00:40:38.6961879Z 
2026-05-03T00:40:38.6961966Z Download Results:
2026-05-03T00:40:38.6962176Z gid   |stat|avg speed  |path/URI
2026-05-03T00:40:38.6962455Z ======+====+===========+=======================================================
2026-05-03T00:40:38.6962915Z e2343d|OK  |   423MiB/s|/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/ZyClang.tar.gz
2026-05-03T00:40:38.6963582Z 
2026-05-03T00:40:38.6963659Z Status Legend:
2026-05-03T00:40:38.6963858Z (OK):download completed.
2026-05-03T00:40:51.7511451Z Clang: ZyC clang version 15.0.7 (https://github.com/llvm/llvm-project 8dfdcc7b7bf66834a761bd8de445840ef68e4d1a)
2026-05-03T00:40:51.7512086Z LLD: LLD 15.0.7 (compatible with GNU linkers)
2026-05-03T00:40:51.8989548Z ##[group]Run git clone --depth=1 https://github.com/MiCode/Xiaomi_Kernel_OpenSource.git \
2026-05-03T00:40:51.8990630Z [36;1mgit clone --depth=1 https://github.com/MiCode/Xiaomi_Kernel_OpenSource.git \[0m
2026-05-03T00:40:51.8991338Z [36;1m  -b fire-t-oss $GITHUB_WORKSPACE/kernel[0m
2026-05-03T00:40:51.8991996Z [36;1mcd $GITHUB_WORKSPACE/kernel[0m
2026-05-03T00:40:51.8992511Z [36;1mKERNEL_HEAD_HASH=$(git log --pretty=format:'%H' -1)[0m
2026-05-03T00:40:51.8993108Z [36;1mecho "KERNEL_HEAD_HASH=$KERNEL_HEAD_HASH" >> $GITHUB_ENV[0m
2026-05-03T00:40:51.8993655Z [36;1mecho "Kernel HEAD: $KERNEL_HEAD_HASH"[0m
2026-05-03T00:40:51.9024891Z shell: /usr/bin/bash -e {0}
2026-05-03T00:40:51.9025268Z env:
2026-05-03T00:40:51.9025547Z   KERNEL_NAME: Castorice
2026-05-03T00:40:51.9025890Z   DEVICE_CODE: fire
2026-05-03T00:40:51.9026231Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:40:51.9027157Z   CLANG_VERSION: ZyC clang version 15.0.7 (https://github.com/llvm/llvm-project 8dfdcc7b7bf66834a761bd8de445840ef68e4d1a)
2026-05-03T00:40:51.9028042Z   LLD_VERSION: LLD 15.0.7 (compatible with GNU linkers)
2026-05-03T00:40:51.9028735Z   KERNEL_HEAD_HASH: 
2026-05-03T00:40:51.9029027Z   KSU_DIR: 
2026-05-03T00:40:51.9029290Z   KSU_VERSION: 
2026-05-03T00:40:51.9029570Z   KERNEL_VERSION: 
2026-05-03T00:40:51.9029852Z   ZIP_NAME: 
2026-05-03T00:40:51.9030118Z ##[endgroup]
2026-05-03T00:40:51.9098889Z Cloning into '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel'...
2026-05-03T00:41:11.0561069Z Updating files:  22% (17079/76589)
2026-05-03T00:41:11.1027073Z Updating files:  23% (17616/76589)
2026-05-03T00:41:11.1427350Z Updating files:  24% (18382/76589)
2026-05-03T00:41:11.1858350Z Updating files:  25% (19148/76589)
2026-05-03T00:41:11.2302732Z Updating files:  26% (19914/76589)
2026-05-03T00:41:11.2856766Z Updating files:  27% (20680/76589)
2026-05-03T00:41:11.3389557Z Updating files:  28% (21445/76589)
2026-05-03T00:41:11.4157957Z Updating files:  29% (22211/76589)
2026-05-03T00:41:11.4708269Z Updating files:  30% (22977/76589)
2026-05-03T00:41:11.5283850Z Updating files:  31% (23743/76589)
2026-05-03T00:41:11.5915244Z Updating files:  32% (24509/76589)
2026-05-03T00:41:11.7384703Z Updating files:  33% (25275/76589)
2026-05-03T00:41:11.8898263Z Updating files:  34% (26041/76589)
2026-05-03T00:41:11.9580446Z Updating files:  35% (26807/76589)
2026-05-03T00:41:11.9988051Z Updating files:  36% (27573/76589)
2026-05-03T00:41:12.0185629Z Updating files:  37% (28338/76589)
2026-05-03T00:41:12.0643154Z Updating files:  37% (28639/76589)
2026-05-03T00:41:12.1206139Z Updating files:  38% (29104/76589)
2026-05-03T00:41:12.1811797Z Updating files:  39% (29870/76589)
2026-05-03T00:41:12.2521491Z Updating files:  40% (30636/76589)
2026-05-03T00:41:12.3053021Z Updating files:  41% (31402/76589)
2026-05-03T00:41:12.3559524Z Updating files:  42% (32168/76589)
2026-05-03T00:41:12.4084153Z Updating files:  43% (32934/76589)
2026-05-03T00:41:12.4563625Z Updating files:  44% (33700/76589)
2026-05-03T00:41:12.5046391Z Updating files:  45% (34466/76589)
2026-05-03T00:41:12.5666718Z Updating files:  46% (35231/76589)
2026-05-03T00:41:12.6305747Z Updating files:  47% (35997/76589)
2026-05-03T00:41:12.7077574Z Updating files:  48% (36763/76589)
2026-05-03T00:41:12.7806628Z Updating files:  49% (37529/76589)
2026-05-03T00:41:12.8471545Z Updating files:  50% (38295/76589)
2026-05-03T00:41:12.9262068Z Updating files:  51% (39061/76589)
2026-05-03T00:41:12.9883810Z Updating files:  52% (39827/76589)
2026-05-03T00:41:13.0186087Z Updating files:  53% (40593/76589)
2026-05-03T00:41:13.0454574Z Updating files:  53% (41037/76589)
2026-05-03T00:41:13.1124575Z Updating files:  54% (41359/76589)
2026-05-03T00:41:13.1588163Z Updating files:  55% (42124/76589)
2026-05-03T00:41:13.2189349Z Updating files:  56% (42890/76589)
2026-05-03T00:41:13.2766352Z Updating files:  57% (43656/76589)
2026-05-03T00:41:13.3357880Z Updating files:  58% (44422/76589)
2026-05-03T00:41:13.3858634Z Updating files:  59% (45188/76589)
2026-05-03T00:41:13.4515888Z Updating files:  60% (45954/76589)
2026-05-03T00:41:13.5118995Z Updating files:  61% (46720/76589)
2026-05-03T00:41:13.5935610Z Updating files:  62% (47486/76589)
2026-05-03T00:41:13.6676304Z Updating files:  63% (48252/76589)
2026-05-03T00:41:13.7700338Z Updating files:  64% (49017/76589)
2026-05-03T00:41:13.8667143Z Updating files:  65% (49783/76589)
2026-05-03T00:41:13.9499325Z Updating files:  66% (50549/76589)
2026-05-03T00:41:14.0187343Z Updating files:  67% (51315/76589)
2026-05-03T00:41:14.0385332Z Updating files:  67% (51881/76589)
2026-05-03T00:41:14.1045638Z Updating files:  68% (52081/76589)
2026-05-03T00:41:14.1694798Z Updating files:  69% (52847/76589)
2026-05-03T00:41:14.2507730Z Updating files:  70% (53613/76589)
2026-05-03T00:41:14.3238262Z Updating files:  71% (54379/76589)
2026-05-03T00:41:14.4295162Z Updating files:  72% (55145/76589)
2026-05-03T00:41:14.4895071Z Updating files:  73% (55910/76589)
2026-05-03T00:41:14.5513087Z Updating files:  74% (56676/76589)
2026-05-03T00:41:14.6128144Z Updating files:  75% (57442/76589)
2026-05-03T00:41:14.6793064Z Updating files:  76% (58208/76589)
2026-05-03T00:41:14.7517689Z Updating files:  77% (58974/76589)
2026-05-03T00:41:14.8286583Z Updating files:  78% (59740/76589)
2026-05-03T00:41:14.9093415Z Updating files:  79% (60506/76589)
2026-05-03T00:41:14.9907171Z Updating files:  80% (61272/76589)
2026-05-03T00:41:15.0185578Z Updating files:  81% (62038/76589)
2026-05-03T00:41:15.0528655Z Updating files:  81% (62357/76589)
2026-05-03T00:41:15.0928929Z Updating files:  82% (62803/76589)
2026-05-03T00:41:15.1439842Z Updating files:  83% (63569/76589)
2026-05-03T00:41:15.2036974Z Updating files:  84% (64335/76589)
2026-05-03T00:41:15.2513101Z Updating files:  85% (65101/76589)
2026-05-03T00:41:15.3001369Z Updating files:  86% (65867/76589)
2026-05-03T00:41:15.3467459Z Updating files:  87% (66633/76589)
2026-05-03T00:41:15.4175539Z Updating files:  88% (67399/76589)
2026-05-03T00:41:15.4863777Z Updating files:  89% (68165/76589)
2026-05-03T00:41:15.5583824Z Updating files:  90% (68931/76589)
2026-05-03T00:41:15.6237441Z Updating files:  91% (69696/76589)
2026-05-03T00:41:15.7131576Z Updating files:  92% (70462/76589)
2026-05-03T00:41:15.7787786Z Updating files:  93% (71228/76589)
2026-05-03T00:41:15.8641422Z Updating files:  94% (71994/76589)
2026-05-03T00:41:15.9200965Z Updating files:  95% (72760/76589)
2026-05-03T00:41:15.9643336Z Updating files:  96% (73526/76589)
2026-05-03T00:41:16.0131519Z Updating files:  97% (74292/76589)
2026-05-03T00:41:16.0185631Z Updating files:  98% (75058/76589)
2026-05-03T00:41:16.0594619Z Updating files:  98% (75126/76589)
2026-05-03T00:41:16.0976243Z Updating files:  99% (75824/76589)
2026-05-03T00:41:16.0976637Z Updating files: 100% (76589/76589)
2026-05-03T00:41:16.0976978Z Updating files: 100% (76589/76589), done.
2026-05-03T00:41:16.1805693Z Kernel HEAD: 1d1aedfe40b2f5fd06c783b752af0197f38966eb
2026-05-03T00:41:16.1853457Z ##[group]Run cd $GITHUB_WORKSPACE/kernel
2026-05-03T00:41:16.1853780Z [36;1mcd $GITHUB_WORKSPACE/kernel[0m
2026-05-03T00:41:16.1854322Z [36;1mcurl -LSs "https://raw.githubusercontent.com/sidex15/KernelSU-Next/legacy/kernel/setup.sh" | bash -s legacy[0m
2026-05-03T00:41:16.1854820Z [36;1m[0m
2026-05-03T00:41:16.1854998Z [36;1mKSU_DIR=""[0m
2026-05-03T00:41:16.1855219Z [36;1mif [ -d "KernelSU-Next" ]; then[0m
2026-05-03T00:41:16.1855482Z [36;1m  KSU_DIR="KernelSU-Next"[0m
2026-05-03T00:41:16.1855727Z [36;1melif [ -d "KernelSU" ]; then[0m
2026-05-03T00:41:16.1855973Z [36;1m  KSU_DIR="KernelSU"[0m
2026-05-03T00:41:16.1856192Z [36;1melse[0m
2026-05-03T00:41:16.1856421Z [36;1m  echo "ERROR: KernelSU directory not found!"[0m
2026-05-03T00:41:16.1856884Z [36;1m  exit 1[0m
2026-05-03T00:41:16.1857063Z [36;1mfi[0m
2026-05-03T00:41:16.1857236Z [36;1m[0m
2026-05-03T00:41:16.1857493Z [36;1mKSU_GIT_VERSION=$(cd $KSU_DIR && git rev-list --count legacy)[0m
2026-05-03T00:41:16.1857922Z [36;1mKERNELSU_VERSION=$(($KSU_GIT_VERSION + 30000 + 60))[0m
2026-05-03T00:41:16.1858249Z [36;1mecho "KSU_DIR=$KSU_DIR" >> $GITHUB_ENV[0m
2026-05-03T00:41:16.1858841Z [36;1mecho "KSU_VERSION=$KERNELSU_VERSION" >> $GITHUB_ENV[0m
2026-05-03T00:41:16.1859245Z [36;1mecho "KernelSU-Next Legacy installed - version $KERNELSU_VERSION"[0m
2026-05-03T00:41:16.1881286Z shell: /usr/bin/bash -e {0}
2026-05-03T00:41:16.1881539Z env:
2026-05-03T00:41:16.1881717Z   KERNEL_NAME: Castorice
2026-05-03T00:41:16.1881931Z   DEVICE_CODE: fire
2026-05-03T00:41:16.1882147Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:41:16.1882674Z   CLANG_VERSION: ZyC clang version 15.0.7 (https://github.com/llvm/llvm-project 8dfdcc7b7bf66834a761bd8de445840ef68e4d1a)
2026-05-03T00:41:16.1883238Z   LLD_VERSION: LLD 15.0.7 (compatible with GNU linkers)
2026-05-03T00:41:16.1883587Z   KERNEL_HEAD_HASH: 1d1aedfe40b2f5fd06c783b752af0197f38966eb
2026-05-03T00:41:16.1883885Z   KSU_DIR: 
2026-05-03T00:41:16.1884057Z   KSU_VERSION: 
2026-05-03T00:41:16.1884243Z   KERNEL_VERSION: 
2026-05-03T00:41:16.1884427Z   ZIP_NAME: 
2026-05-03T00:41:16.1884607Z ##[endgroup]
2026-05-03T00:41:16.2916890Z [+] Setting up KernelSU-Next...
2026-05-03T00:41:16.2931727Z Cloning into 'KernelSU-Next'...
2026-05-03T00:41:18.0784814Z [+] Repository cloned.
2026-05-03T00:41:18.1080411Z No local changes to save
2026-05-03T00:41:18.1083227Z [-] Stashed current changes.
2026-05-03T00:41:18.3202217Z Already up to date.
2026-05-03T00:41:18.3206923Z [+] Repository updated.
2026-05-03T00:41:18.3656091Z Switched to a new branch 'legacy'
2026-05-03T00:41:18.3658913Z branch 'legacy' set up to track 'origin/legacy'.
2026-05-03T00:41:18.3663303Z [-] Checked out legacy.
2026-05-03T00:41:18.3689067Z [+] Symlink created.
2026-05-03T00:41:18.3703638Z [+] Modified Makefile.
2026-05-03T00:41:18.3733498Z [+] Modified Kconfig.
2026-05-03T00:41:18.3733820Z [+] Done.
2026-05-03T00:41:18.3966591Z KernelSU-Next Legacy installed - version 33042
2026-05-03T00:41:18.3997198Z ##[group]Run cd $GITHUB_WORKSPACE
2026-05-03T00:41:18.3997489Z [36;1mcd $GITHUB_WORKSPACE[0m
2026-05-03T00:41:18.3997903Z [36;1mgit clone --depth=1 https://gitlab.com/simonpunk/susfs4ksu.git -b kernel-4.19[0m
2026-05-03T00:41:18.3998311Z [36;1m[0m
2026-05-03T00:41:18.3998793Z [36;1mcd $GITHUB_WORKSPACE/kernel[0m
2026-05-03T00:41:18.3999046Z [36;1m# Copy SUSFS source files[0m
2026-05-03T00:41:18.3999299Z [36;1mecho "Copying SUSFS files..."[0m
2026-05-03T00:41:18.3999590Z [36;1mcp -rv ../susfs4ksu/kernel_patches/fs/* fs/[0m
2026-05-03T00:41:18.3999969Z [36;1mcp -rv ../susfs4ksu/kernel_patches/include/linux/* include/linux/[0m
2026-05-03T00:41:18.4000297Z [36;1m[0m
2026-05-03T00:41:18.4000490Z [36;1mecho "Verifying copied files:"[0m
2026-05-03T00:41:18.4000767Z [36;1mls -la include/linux/susfs*[0m
2026-05-03T00:41:18.4001009Z [36;1mls -la fs/susfs*[0m
2026-05-03T00:41:18.4001245Z [36;1mecho "SUSFS source files copied"[0m
2026-05-03T00:41:18.4022586Z shell: /usr/bin/bash -e {0}
2026-05-03T00:41:18.4022815Z env:
2026-05-03T00:41:18.4022998Z   KERNEL_NAME: Castorice
2026-05-03T00:41:18.4023207Z   DEVICE_CODE: fire
2026-05-03T00:41:18.4023423Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:41:18.4023949Z   CLANG_VERSION: ZyC clang version 15.0.7 (https://github.com/llvm/llvm-project 8dfdcc7b7bf66834a761bd8de445840ef68e4d1a)
2026-05-03T00:41:18.4024476Z   LLD_VERSION: LLD 15.0.7 (compatible with GNU linkers)
2026-05-03T00:41:18.4024826Z   KERNEL_HEAD_HASH: 1d1aedfe40b2f5fd06c783b752af0197f38966eb
2026-05-03T00:41:18.4025129Z   KSU_DIR: KernelSU-Next
2026-05-03T00:41:18.4025335Z   KSU_VERSION: 33042
2026-05-03T00:41:18.4025525Z   KERNEL_VERSION: 
2026-05-03T00:41:18.4025712Z   ZIP_NAME: 
2026-05-03T00:41:18.4026065Z ##[endgroup]
2026-05-03T00:41:18.4078068Z Cloning into 'susfs4ksu'...
2026-05-03T00:41:18.9926664Z Copying SUSFS files...
2026-05-03T00:41:18.9941374Z '../susfs4ksu/kernel_patches/fs/sus_su.c' -> 'fs/sus_su.c'
2026-05-03T00:41:18.9942026Z '../susfs4ksu/kernel_patches/fs/susfs.c' -> 'fs/susfs.c'
2026-05-03T00:41:18.9957514Z '../susfs4ksu/kernel_patches/include/linux/sus_su.h' -> 'include/linux/sus_su.h'
2026-05-03T00:41:18.9958347Z '../susfs4ksu/kernel_patches/include/linux/susfs.h' -> 'include/linux/susfs.h'
2026-05-03T00:41:18.9959230Z '../susfs4ksu/kernel_patches/include/linux/susfs_def.h' -> 'include/linux/susfs_def.h'
2026-05-03T00:41:18.9959829Z Verifying copied files:
2026-05-03T00:41:18.9979979Z -rw-r--r-- 1 runner runner 5921 May  3 00:41 include/linux/susfs.h
2026-05-03T00:41:18.9980700Z -rw-r--r-- 1 runner runner 2565 May  3 00:41 include/linux/susfs_def.h
2026-05-03T00:41:18.9994857Z -rw-r--r-- 1 runner runner 32318 May  3 00:41 fs/susfs.c
2026-05-03T00:41:18.9997017Z SUSFS source files copied
2026-05-03T00:41:19.0024732Z ##[group]Run cd $GITHUB_WORKSPACE
2026-05-03T00:41:19.0025036Z [36;1mcd $GITHUB_WORKSPACE[0m
2026-05-03T00:41:19.0025458Z [36;1mgit clone --depth=1 https://github.com/Alexjr2/KernelSU_Next_SUSFS_fire.git ref_patches[0m
2026-05-03T00:41:19.0025906Z [36;1mecho "=== Available patches ==="[0m
2026-05-03T00:41:19.0026193Z [36;1mls -la ref_patches/patchs/ || true[0m
2026-05-03T00:41:19.0048020Z shell: /usr/bin/bash -e {0}
2026-05-03T00:41:19.0048255Z env:
2026-05-03T00:41:19.0048630Z   KERNEL_NAME: Castorice
2026-05-03T00:41:19.0048844Z   DEVICE_CODE: fire
2026-05-03T00:41:19.0049063Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:41:19.0049590Z   CLANG_VERSION: ZyC clang version 15.0.7 (https://github.com/llvm/llvm-project 8dfdcc7b7bf66834a761bd8de445840ef68e4d1a)
2026-05-03T00:41:19.0050171Z   LLD_VERSION: LLD 15.0.7 (compatible with GNU linkers)
2026-05-03T00:41:19.0050521Z   KERNEL_HEAD_HASH: 1d1aedfe40b2f5fd06c783b752af0197f38966eb
2026-05-03T00:41:19.0050881Z   KSU_DIR: KernelSU-Next
2026-05-03T00:41:19.0051093Z   KSU_VERSION: 33042
2026-05-03T00:41:19.0051293Z   KERNEL_VERSION: 
2026-05-03T00:41:19.0051478Z   ZIP_NAME: 
2026-05-03T00:41:19.0051662Z ##[endgroup]
2026-05-03T00:41:19.0103451Z Cloning into 'ref_patches'...
2026-05-03T00:41:19.3039108Z === Available patches ===
2026-05-03T00:41:19.3052862Z total 148
2026-05-03T00:41:19.3053221Z drwxr-xr-x 2 runner runner  4096 May  3 00:41 .
2026-05-03T00:41:19.3053686Z drwxr-xr-x 5 runner runner  4096 May  3 00:41 ..
2026-05-03T00:41:19.3054095Z -rw-r--r-- 1 runner runner 43209 May  3 00:41 50_add_susfs_in_kernel-4.19.patch
2026-05-03T00:41:19.3054763Z -rw-r--r-- 1 runner runner  2588 May  3 00:41 69_hide_ksu.patch
2026-05-03T00:41:19.3055346Z -rw-r--r-- 1 runner runner  2801 May  3 00:41 69_hide_stuff.patch
2026-05-03T00:41:19.3055923Z -rw-r--r-- 1 runner runner  6296 May  3 00:41 ath9k_htc.patch
2026-05-03T00:41:19.3056538Z -rw-r--r-- 1 runner runner  3442 May  3 00:41 backslashxxksu.patch
2026-05-03T00:41:19.3057235Z -rw-r--r-- 1 runner runner   654 May  3 00:41 fix_kernel_genheaders.patch
2026-05-03T00:41:19.3058010Z -rw-r--r-- 1 runner runner 57742 May  3 00:41 fix_lcm.patch
2026-05-03T00:41:19.3058835Z -rw-r--r-- 1 runner runner  4772 May  3 00:41 ksu_hooks_4.19.patch
2026-05-03T00:41:19.3059250Z -rw-r--r-- 1 runner runner  4036 May  3 00:41 ksu_hooks_sukisu_4.19.patch
2026-05-03T00:41:19.3108165Z ##[group]Run cd $GITHUB_WORKSPACE/kernel
2026-05-03T00:41:19.3108989Z [36;1mcd $GITHUB_WORKSPACE/kernel[0m
2026-05-03T00:41:19.3109280Z [36;1m[0m
2026-05-03T00:41:19.3109540Z [36;1m# Apply KSU hooks for 4.19 (manual hook, NO kprobes)[0m
2026-05-03T00:41:19.3109870Z [36;1mif [ "true" = "true" ]; then[0m
2026-05-03T00:41:19.3110155Z [36;1m  echo "Applying KSU hooks patch..."[0m
2026-05-03T00:41:19.3110679Z [36;1m  patch -p1 --forward < ../ref_patches/patchs/ksu_hooks_4.19.patch || echo "WARN: ksu_hooks patch had issues"[0m
2026-05-03T00:41:19.3111157Z [36;1m[0m
2026-05-03T00:41:19.3111361Z [36;1m  echo "Applying hide KSU patch..."[0m
2026-05-03T00:41:19.3112015Z [36;1m  patch -p1 --forward < ../ref_patches/patchs/69_hide_ksu.patch || echo "WARN: hide_ksu patch had issues"[0m
2026-05-03T00:41:19.3112454Z [36;1mfi[0m
2026-05-03T00:41:19.3112628Z [36;1m[0m
2026-05-03T00:41:19.3112816Z [36;1m# Fix kernel genheaders (build fix)[0m
2026-05-03T00:41:19.3113133Z [36;1mecho "Applying genheaders fix..."[0m
2026-05-03T00:41:19.3113654Z [36;1mpatch -p1 --forward < ../ref_patches/patchs/fix_kernel_genheaders.patch || echo "WARN: genheaders patch had issues"[0m
2026-05-03T00:41:19.3114202Z [36;1m[0m
2026-05-03T00:41:19.3114396Z [36;1m# SUSFS kernel integration patch[0m
2026-05-03T00:41:19.3114666Z [36;1mif [ "true" = "true" ]; then[0m
2026-05-03T00:41:19.3114938Z [36;1m  echo "Applying SUSFS kernel patch..."[0m
2026-05-03T00:41:19.3115476Z [36;1m  patch -p1 --forward < ../ref_patches/patchs/50_add_susfs_in_kernel-4.19.patch || echo "WARN: susfs patch had issues"[0m
2026-05-03T00:41:19.3115954Z [36;1m[0m
2026-05-03T00:41:19.3116165Z [36;1m  # Fix SUSFS format strings for 4.19[0m
2026-05-03T00:41:19.3116584Z [36;1m  sed -i "s/poofed_size: '%u'/poofed_size: '%llu'/g" ./fs/susfs.c 2>/dev/null || true[0m
2026-05-03T00:41:19.3117116Z [36;1m  sed -i "s/length of string: %u/length of string: %lu/g" ./fs/susfs.c 2>/dev/null || true[0m
2026-05-03T00:41:19.3117502Z [36;1m[0m
2026-05-03T00:41:19.3117701Z [36;1m  # Fix task_work_add compatibility[0m
2026-05-03T00:41:19.3117987Z [36;1m  if [ -d "KernelSU-Next" ]; then[0m
2026-05-03T00:41:19.3118296Z [36;1m    sed -i "/task_work_add(tsk, cb, TWA_RESUME);/c\\[0m
2026-05-03T00:41:19.3118985Z [36;1m#if LINUX_VERSION_CODE >= KERNEL_VERSION(5, 10, 0)\\[0m
2026-05-03T00:41:19.3119319Z [36;1m\\ttask_work_add(tsk, cb, TWA_RESUME);\\[0m
2026-05-03T00:41:19.3119585Z [36;1m#else\\[0m
2026-05-03T00:41:19.3119797Z [36;1m\\ttask_work_add(tsk, cb, true);\\[0m
2026-05-03T00:41:19.3120140Z [36;1m#endif" ./KernelSU-Next/kernel/allowlist.c 2>/dev/null || true[0m
2026-05-03T00:41:19.3120476Z [36;1m  fi[0m
2026-05-03T00:41:19.3120649Z [36;1mfi[0m
2026-05-03T00:41:19.3120818Z [36;1m[0m
2026-05-03T00:41:19.3121048Z [36;1m# ===== LCD 0c/0d FIX (CRITICAL FOR TOUCHSCREEN) =====[0m
2026-05-03T00:41:19.3121404Z [36;1mecho "Applying LCM fix (LCD 0c/0d touchscreen fix)..."[0m
2026-05-03T00:41:19.3121920Z [36;1mpatch -p1 --forward < ../ref_patches/patchs/fix_lcm.patch || echo "WARN: fix_lcm patch had issues"[0m
2026-05-03T00:41:19.3122348Z [36;1m[0m
2026-05-03T00:41:19.3122554Z [36;1mecho "Applying primary display fix..."[0m
2026-05-03T00:41:19.3123072Z [36;1mpatch -p1 --forward < ../ref_patches/primary_display_fix.patch || echo "WARN: primary_display_fix patch had issues"[0m
2026-05-03T00:41:19.3123546Z [36;1m[0m
2026-05-03T00:41:19.3123732Z [36;1mecho "All patches applied"[0m
2026-05-03T00:41:19.3145409Z shell: /usr/bin/bash -e {0}
2026-05-03T00:41:19.3145645Z env:
2026-05-03T00:41:19.3145831Z   KERNEL_NAME: Castorice
2026-05-03T00:41:19.3146046Z   DEVICE_CODE: fire
2026-05-03T00:41:19.3146271Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:41:19.3146807Z   CLANG_VERSION: ZyC clang version 15.0.7 (https://github.com/llvm/llvm-project 8dfdcc7b7bf66834a761bd8de445840ef68e4d1a)
2026-05-03T00:41:19.3147340Z   LLD_VERSION: LLD 15.0.7 (compatible with GNU linkers)
2026-05-03T00:41:19.3147858Z   KERNEL_HEAD_HASH: 1d1aedfe40b2f5fd06c783b752af0197f38966eb
2026-05-03T00:41:19.3148172Z   KSU_DIR: KernelSU-Next
2026-05-03T00:41:19.3148381Z   KSU_VERSION: 33042
2026-05-03T00:41:19.3148850Z   KERNEL_VERSION: 
2026-05-03T00:41:19.3149039Z   ZIP_NAME: 
2026-05-03T00:41:19.3149217Z ##[endgroup]
2026-05-03T00:41:19.3189034Z Applying KSU hooks patch...
2026-05-03T00:41:19.3454809Z patching file fs/exec.c
2026-05-03T00:41:19.3455561Z Hunk #1 succeeded at 1888 (offset -24 lines).
2026-05-03T00:41:19.3458329Z patching file fs/open.c
2026-05-03T00:41:19.3461847Z patching file fs/read_write.c
2026-05-03T00:41:19.3464809Z patching file fs/stat.c
2026-05-03T00:41:19.3465152Z Hunk #1 succeeded at 354 (offset 1 line).
2026-05-03T00:41:19.3465798Z Hunk #2 succeeded at 367 (offset 1 line).
2026-05-03T00:41:19.3468816Z patching file drivers/input/input.c
2026-05-03T00:41:19.3469232Z Hunk #1 succeeded at 433 (offset -11 lines).
2026-05-03T00:41:19.3471895Z patching file kernel/reboot.c
2026-05-03T00:41:19.3474193Z patching file security/selinux/avc.c
2026-05-03T00:41:19.3474625Z Hunk #1 succeeded at 776 (offset -1 lines).
2026-05-03T00:41:19.3475023Z Hunk #2 succeeded at 788 (offset -1 lines).
2026-05-03T00:41:19.3478006Z Applying hide KSU patch...
2026-05-03T00:41:19.3488257Z patching file fs/proc/task_mmu.c
2026-05-03T00:41:19.3493024Z patching file fs/proc/base.c
2026-05-03T00:41:19.3498022Z Applying genheaders fix...
2026-05-03T00:41:19.3506752Z patching file kernel/gen_kheaders.sh
2026-05-03T00:41:19.3510084Z Applying SUSFS kernel patch...
2026-05-03T00:41:19.3518764Z patching file fs/Makefile
2026-05-03T00:41:19.3521098Z patching file fs/dcache.c
2026-05-03T00:41:19.3522560Z Hunk #2 succeeded at 2192 (offset -1 lines).
2026-05-03T00:41:19.3523030Z Hunk #3 succeeded at 2280 (offset -1 lines).
2026-05-03T00:41:19.3525760Z patching file fs/namei.c
2026-05-03T00:41:19.3527919Z Hunk #9 succeeded at 2957 (offset -20 lines).
2026-05-03T00:41:19.3528344Z Hunk #10 succeeded at 2991 (offset -20 lines).
2026-05-03T00:41:19.3528891Z Hunk #11 succeeded at 3134 (offset -20 lines).
2026-05-03T00:41:19.3529160Z Hunk #12 succeeded at 3211 (offset -20 lines).
2026-05-03T00:41:19.3539573Z Hunk #13 succeeded at 3363 (offset -20 lines).
2026-05-03T00:41:19.3541366Z Hunk #14 succeeded at 3412 (offset -20 lines).
2026-05-03T00:41:19.3541793Z Hunk #15 succeeded at 3437 (offset -20 lines).
2026-05-03T00:41:19.3542209Z Hunk #16 succeeded at 3780 (offset -22 lines).
2026-05-03T00:41:19.3542616Z Hunk #17 succeeded at 3800 (offset -22 lines).
2026-05-03T00:41:19.3543025Z patching file fs/namespace.c
2026-05-03T00:41:19.3543393Z Hunk #11 succeeded at 2397 (offset -23 lines).
2026-05-03T00:41:19.3543811Z Hunk #12 succeeded at 3014 (offset -26 lines).
2026-05-03T00:41:19.3544232Z Hunk #13 succeeded at 3100 (offset -26 lines).
2026-05-03T00:41:19.3544641Z Hunk #14 succeeded at 3123 (offset -26 lines).
2026-05-03T00:41:19.3545054Z Hunk #15 succeeded at 3168 (offset -26 lines).
2026-05-03T00:41:19.3545458Z Hunk #16 succeeded at 3737 (offset -26 lines).
2026-05-03T00:41:19.3545871Z patching file fs/notify/fdinfo.c
2026-05-03T00:41:19.3546243Z Hunk #4 succeeded at 135 (offset 7 lines).
2026-05-03T00:41:19.3546656Z patching file fs/overlayfs/inode.c
2026-05-03T00:41:19.3547029Z patching file fs/overlayfs/readdir.c
2026-05-03T00:41:19.3547413Z patching file fs/overlayfs/super.c
2026-05-03T00:41:19.3547780Z patching file fs/proc/cmdline.c
2026-05-03T00:41:19.3548127Z patching file fs/proc/fd.c
2026-05-03T00:41:19.3548616Z patching file fs/proc/task_mmu.c
2026-05-03T00:41:19.3549034Z Hunk #2 succeeded at 367 with fuzz 1 (offset 17 lines).
2026-05-03T00:41:19.3549532Z Hunk #3 succeeded at 386 with fuzz 2 (offset 18 lines).
2026-05-03T00:41:19.3549957Z patching file fs/proc_namespace.c
2026-05-03T00:41:19.3550322Z patching file fs/readdir.c
2026-05-03T00:41:19.3550639Z patching file fs/stat.c
2026-05-03T00:41:19.3551119Z patching file fs/statfs.c
2026-05-03T00:41:19.3552446Z patching file include/linux/mount.h
2026-05-03T00:41:19.3553810Z patching file include/linux/sched.h
2026-05-03T00:41:19.3554876Z Hunk #1 succeeded at 1319 (offset -6 lines).
2026-05-03T00:41:19.3555247Z Hunk #2 succeeded at 1349 (offset -6 lines).
2026-05-03T00:41:19.3556244Z patching file kernel/kallsyms.c
2026-05-03T00:41:19.3558006Z patching file kernel/sys.c
2026-05-03T00:41:19.3631986Z Applying LCM fix (LCD 0c/0d touchscreen fix)...
2026-05-03T00:41:19.3641558Z patching file drivers/input/touchscreen/mediatek/focaltech_FT8720/focaltech_core.c
2026-05-03T00:41:19.3643247Z Hunk #1 succeeded at 2716 (offset 320 lines).
2026-05-03T00:41:19.3644907Z patching file drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0c_dsc_vdo/Makefile
2026-05-03T00:41:19.3646203Z patching file drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0c_dsc_vdo/data_hw_roundedpattern.h
2026-05-03T00:41:19.3647714Z patching file drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0c_dsc_vdo/dsi_panel_m19a_42_03_0c_dsc_vdo.c
2026-05-03T00:41:19.3651346Z patching file drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0d_dsc_vdo/Makefile
2026-05-03T00:41:19.3652393Z patching file drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0d_dsc_vdo/data_hw_roundedpattern.h
2026-05-03T00:41:19.3654040Z patching file drivers/misc/mediatek/lcm/dsi_panel_m19a_42_03_0d_dsc_vdo/dsi_panel_m19a_42_03_0d_dsc_vdo.c
2026-05-03T00:41:19.3657282Z patching file drivers/misc/mediatek/lcm/mt65xx_lcm_list.c
2026-05-03T00:41:19.3659151Z patching file drivers/misc/mediatek/lcm/mt65xx_lcm_list.h
2026-05-03T00:41:19.3661275Z patching file drivers/misc/mediatek/leds/mt6768/ktd3136_bl.c
2026-05-03T00:41:19.3663717Z patching file drivers/misc/mediatek/leds/mt6768/ti-lmu-backlight-core.c
2026-05-03T00:41:19.3669842Z Applying primary display fix...
2026-05-03T00:41:19.3683623Z patching file drivers/misc/mediatek/video/mt6768/videox/primary_display.c
2026-05-03T00:41:19.3692494Z All patches applied
2026-05-03T00:41:19.3719313Z ##[group]Run cd $GITHUB_WORKSPACE/kernel
2026-05-03T00:41:19.3719704Z [36;1mcd $GITHUB_WORKSPACE/kernel[0m
2026-05-03T00:41:19.3720010Z [36;1mDEFCONFIG="arch/arm64/configs/fire_defconfig"[0m
2026-05-03T00:41:19.3720292Z [36;1m[0m
2026-05-03T00:41:19.3720537Z [36;1m# Use reference fire_defconfig as base (stock Xiaomi)[0m
2026-05-03T00:41:19.3720888Z [36;1mif [ -f "../ref_patches/fire_defconfig" ]; then[0m
2026-05-03T00:41:19.3721214Z [36;1m  echo "Using reference fire_defconfig..."[0m
2026-05-03T00:41:19.3721538Z [36;1m  cp ../ref_patches/fire_defconfig $DEFCONFIG[0m
2026-05-03T00:41:19.3721798Z [36;1mfi[0m
2026-05-03T00:41:19.3721971Z [36;1m[0m
2026-05-03T00:41:19.3722144Z [36;1m# KernelSU configs[0m
2026-05-03T00:41:19.3722374Z [36;1mif [ "true" = "true" ]; then[0m
2026-05-03T00:41:19.3722614Z [36;1m  echo "" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3733248Z [36;1m  echo "# KernelSU-Next (Legacy Manual Hook)" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3733655Z [36;1m  echo "CONFIG_KSU=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3733967Z [36;1m  echo "CONFIG_KSU_KPROBES_HOOK=n" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3734308Z [36;1m  echo "CONFIG_KSU_MANUAL_HOOK=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3734582Z [36;1mfi[0m
2026-05-03T00:41:19.3734760Z [36;1m[0m
2026-05-03T00:41:19.3734931Z [36;1m# SUSFS configs[0m
2026-05-03T00:41:19.3735176Z [36;1mif [ "true" = "true" ] && [ "true" = "true" ]; then[0m
2026-05-03T00:41:19.3735468Z [36;1m  echo "" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3735703Z [36;1m  echo "# SUSFS" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3735988Z [36;1m  echo "CONFIG_KSU_SUSFS=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3736309Z [36;1m  echo "CONFIG_KSU_SUSFS_SUS_PATH=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3736656Z [36;1m  echo "CONFIG_KSU_SUSFS_SUS_MOUNT=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3736999Z [36;1m  echo "CONFIG_KSU_SUSFS_SUS_MAP=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3737387Z [36;1m  echo "CONFIG_KSU_SUSFS_AUTO_ADD_SUS_KSU_DEFAULT_MOUNT=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3737826Z [36;1m  echo "CONFIG_KSU_SUSFS_AUTO_ADD_SUS_BIND_MOUNT=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3738206Z [36;1m  echo "CONFIG_KSU_SUSFS_SUS_KSTAT=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3738880Z [36;1m  echo "CONFIG_KSU_SUSFS_TRY_UMOUNT=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3739288Z [36;1m  echo "CONFIG_KSU_SUSFS_AUTO_ADD_TRY_UMOUNT_FOR_BIND_MOUNT=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3739712Z [36;1m  echo "CONFIG_KSU_SUSFS_SPOOF_UNAME=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3740064Z [36;1m  echo "CONFIG_KSU_SUSFS_ENABLE_LOG=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3740434Z [36;1m  echo "CONFIG_KSU_SUSFS_HIDE_KSU_SUSFS_SYMBOLS=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3740860Z [36;1m  echo "CONFIG_KSU_SUSFS_SPOOF_CMDLINE_OR_BOOTCONFIG=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3741262Z [36;1m  echo "CONFIG_KSU_SUSFS_OPEN_REDIRECT=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3741800Z [36;1m  echo "CONFIG_KSU_SUSFS_SUS_SU=n" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3742075Z [36;1mfi[0m
2026-05-03T00:41:19.3742246Z [36;1m[0m
2026-05-03T00:41:19.3742437Z [36;1m# Memory & CPU Optimization[0m
2026-05-03T00:41:19.3742681Z [36;1mecho "" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3742944Z [36;1mecho "# Memory Optimization" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3743230Z [36;1mecho "CONFIG_ZRAM=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3743514Z [36;1mecho "CONFIG_ZSMALLOC=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3743807Z [36;1mecho "CONFIG_COMPACTION=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3744087Z [36;1mecho "CONFIG_KSM=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3744353Z [36;1mecho "CONFIG_HZ_1000=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3744592Z [36;1m[0m
2026-05-03T00:41:19.3744781Z [36;1m# Networking (stable performance)[0m
2026-05-03T00:41:19.3745023Z [36;1mecho "" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3745290Z [36;1mecho "# Networking Performance" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3745764Z [36;1mecho "CONFIG_TCP_CONG_ADVANCED=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3746083Z [36;1mecho "CONFIG_TCP_CONG_BBR=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3746395Z [36;1mecho "CONFIG_IP_NF_TARGET_TTL=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3746704Z [36;1mecho "CONFIG_IP6_NF_TARGET_HL=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3746965Z [36;1m[0m
2026-05-03T00:41:19.3747136Z [36;1m# IPSet Support[0m
2026-05-03T00:41:19.3747344Z [36;1mecho "" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3747561Z [36;1mecho "# IPSet" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3747821Z [36;1mecho "CONFIG_IP_SET=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3748113Z [36;1mecho "CONFIG_IP_SET_MAX=65534" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3748606Z [36;1mecho "CONFIG_IP_SET_BITMAP_IP=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3749027Z [36;1mecho "CONFIG_IP_SET_BITMAP_IPMAC=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3749364Z [36;1mecho "CONFIG_IP_SET_BITMAP_PORT=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3749691Z [36;1mecho "CONFIG_IP_SET_HASH_IP=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3750001Z [36;1mecho "CONFIG_IP_SET_HASH_IPMARK=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3750322Z [36;1mecho "CONFIG_IP_SET_HASH_IPPORT=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3750664Z [36;1mecho "CONFIG_IP_SET_HASH_IPPORTIP=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3751010Z [36;1mecho "CONFIG_IP_SET_HASH_IPPORTNET=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3751345Z [36;1mecho "CONFIG_IP_SET_HASH_IPMAC=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3751656Z [36;1mecho "CONFIG_IP_SET_HASH_MAC=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3751987Z [36;1mecho "CONFIG_IP_SET_HASH_NETPORTNET=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3752317Z [36;1mecho "CONFIG_IP_SET_HASH_NET=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3752622Z [36;1mecho "CONFIG_IP_SET_HASH_NETNET=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3752951Z [36;1mecho "CONFIG_IP_SET_HASH_NETPORT=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3753285Z [36;1mecho "CONFIG_IP_SET_HASH_NETIFACE=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3753609Z [36;1mecho "CONFIG_IP_SET_LIST_SET=y" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3753863Z [36;1m[0m
2026-05-03T00:41:19.3754106Z [36;1m# Branding / Vermagic (MUST MATCH STOCK OR WIFI BREAKS)[0m
2026-05-03T00:41:19.3754413Z [36;1mecho "" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3754637Z [36;1mecho "# Branding" >> $DEFCONFIG[0m
2026-05-03T00:41:19.3755103Z [36;1msed -i 's/CONFIG_LOCALVERSION=".*"/CONFIG_LOCALVERSION="-Castorice-perf-g2da4f2613486"/' $DEFCONFIG[0m
2026-05-03T00:41:19.3755539Z [36;1m[0m
2026-05-03T00:41:19.3755719Z [36;1mecho "=== Defconfig tail ==="[0m
2026-05-03T00:41:19.3755965Z [36;1mtail -40 $DEFCONFIG[0m
2026-05-03T00:41:19.3776989Z shell: /usr/bin/bash -e {0}
2026-05-03T00:41:19.3777220Z env:
2026-05-03T00:41:19.3777401Z   KERNEL_NAME: Castorice
2026-05-03T00:41:19.3777613Z   DEVICE_CODE: fire
2026-05-03T00:41:19.3777824Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:41:19.3778850Z   CLANG_VERSION: ZyC clang version 15.0.7 (https://github.com/llvm/llvm-project 8dfdcc7b7bf66834a761bd8de445840ef68e4d1a)
2026-05-03T00:41:19.3779720Z   LLD_VERSION: LLD 15.0.7 (compatible with GNU linkers)
2026-05-03T00:41:19.3780092Z   KERNEL_HEAD_HASH: 1d1aedfe40b2f5fd06c783b752af0197f38966eb
2026-05-03T00:41:19.3780400Z   KSU_DIR: KernelSU-Next
2026-05-03T00:41:19.3780610Z   KSU_VERSION: 33042
2026-05-03T00:41:19.3780806Z   KERNEL_VERSION: 
2026-05-03T00:41:19.3780990Z   ZIP_NAME: 
2026-05-03T00:41:19.3781171Z ##[endgroup]
2026-05-03T00:41:19.3821042Z Using reference fire_defconfig...
2026-05-03T00:41:19.3872101Z === Defconfig tail ===
2026-05-03T00:41:19.3881728Z CONFIG_KSU_SUSFS_ENABLE_LOG=y
2026-05-03T00:41:19.3882127Z CONFIG_KSU_SUSFS_HIDE_KSU_SUSFS_SYMBOLS=y
2026-05-03T00:41:19.3882578Z CONFIG_KSU_SUSFS_SPOOF_CMDLINE_OR_BOOTCONFIG=y
2026-05-03T00:41:19.3883011Z CONFIG_KSU_SUSFS_OPEN_REDIRECT=y
2026-05-03T00:41:19.3883361Z CONFIG_KSU_SUSFS_SUS_SU=n
2026-05-03T00:41:19.3883583Z 
2026-05-03T00:41:19.3883709Z # Memory Optimization
2026-05-03T00:41:19.3884001Z CONFIG_ZRAM=y
2026-05-03T00:41:19.3884503Z CONFIG_ZSMALLOC=y
2026-05-03T00:41:19.3884786Z CONFIG_COMPACTION=y
2026-05-03T00:41:19.3885097Z CONFIG_KSM=y
2026-05-03T00:41:19.3885348Z CONFIG_HZ_1000=y
2026-05-03T00:41:19.3885524Z 
2026-05-03T00:41:19.3885646Z # Networking Performance
2026-05-03T00:41:19.3885993Z CONFIG_TCP_CONG_ADVANCED=y
2026-05-03T00:41:19.3886312Z CONFIG_TCP_CONG_BBR=y
2026-05-03T00:41:19.3886618Z CONFIG_IP_NF_TARGET_TTL=y
2026-05-03T00:41:19.3886827Z CONFIG_IP6_NF_TARGET_HL=y
2026-05-03T00:41:19.3886953Z 
2026-05-03T00:41:19.3887024Z # IPSet
2026-05-03T00:41:19.3887188Z CONFIG_IP_SET=y
2026-05-03T00:41:19.3887383Z CONFIG_IP_SET_MAX=65534
2026-05-03T00:41:19.3887592Z CONFIG_IP_SET_BITMAP_IP=y
2026-05-03T00:41:19.3887817Z CONFIG_IP_SET_BITMAP_IPMAC=y
2026-05-03T00:41:19.3888060Z CONFIG_IP_SET_BITMAP_PORT=y
2026-05-03T00:41:19.3888276Z CONFIG_IP_SET_HASH_IP=y
2026-05-03T00:41:19.3888998Z CONFIG_IP_SET_HASH_IPMARK=y
2026-05-03T00:41:19.3889212Z CONFIG_IP_SET_HASH_IPPORT=y
2026-05-03T00:41:19.3889428Z CONFIG_IP_SET_HASH_IPPORTIP=y
2026-05-03T00:41:19.3889656Z CONFIG_IP_SET_HASH_IPPORTNET=y
2026-05-03T00:41:19.3889882Z CONFIG_IP_SET_HASH_IPMAC=y
2026-05-03T00:41:19.3890085Z CONFIG_IP_SET_HASH_MAC=y
2026-05-03T00:41:19.3890300Z CONFIG_IP_SET_HASH_NETPORTNET=y
2026-05-03T00:41:19.3890520Z CONFIG_IP_SET_HASH_NET=y
2026-05-03T00:41:19.3890720Z CONFIG_IP_SET_HASH_NETNET=y
2026-05-03T00:41:19.3890933Z CONFIG_IP_SET_HASH_NETPORT=y
2026-05-03T00:41:19.3891147Z CONFIG_IP_SET_HASH_NETIFACE=y
2026-05-03T00:41:19.3891359Z CONFIG_IP_SET_LIST_SET=y
2026-05-03T00:41:19.3891480Z 
2026-05-03T00:41:19.3891552Z # Branding
2026-05-03T00:41:19.3912790Z ##[group]Run cd $GITHUB_WORKSPACE/kernel
2026-05-03T00:41:19.3913132Z [36;1mcd $GITHUB_WORKSPACE/kernel[0m
2026-05-03T00:41:19.3913375Z [36;1m[0m
2026-05-03T00:41:19.3913634Z [36;1mecho "=== Fixing modern Clang vs 4.19 incompatibilities ==="[0m
2026-05-03T00:41:19.3913965Z [36;1m[0m
2026-05-03T00:41:19.3914252Z [36;1m# Step 1: Remove ENTIRE compound -Werror=xxx flags from all Makefiles[0m
2026-05-03T00:41:19.3914754Z [36;1m# Must come BEFORE removing standalone -Werror to avoid leaving orphan '=xxx'[0m
2026-05-03T00:41:19.3915189Z [36;1mecho "Removing compound -Werror=xxx flags..."[0m
2026-05-03T00:41:19.3915560Z [36;1mfind . -type f \( -name "Makefile" -o -name "Kbuild" \) \[0m
2026-05-03T00:41:19.3915923Z [36;1m  -exec sed -i 's/-Werror=[a-zA-Z_-]*//g' {} +[0m
2026-05-03T00:41:19.3916190Z [36;1m[0m
2026-05-03T00:41:19.3916478Z [36;1m# Step 2: Remove standalone -Werror (safe now since compounds are gone)[0m
2026-05-03T00:41:19.3916893Z [36;1mecho "Removing standalone -Werror..."[0m
2026-05-03T00:41:19.3917219Z [36;1mfind . -type f \( -name "Makefile" -o -name "Kbuild" \) \[0m
2026-05-03T00:41:19.3917612Z [36;1m  -exec sed -i 's/ -Werror / /g; s/ -Werror$//g; s/^-Werror //g' {} +[0m
2026-05-03T00:41:19.3917944Z [36;1m[0m
2026-05-03T00:41:19.3918245Z [36;1m# Step 3: Remove GCC-specific warning flags that clang doesn't understand[0m
2026-05-03T00:41:19.3919073Z [36;1mecho "Removing clang-incompatible warning flags..."[0m
2026-05-03T00:41:19.3919452Z [36;1mfind . -type f \( -name "Makefile" -o -name "Kbuild" \) \[0m
2026-05-03T00:41:19.3919827Z [36;1m  -exec sed -i 's/-Wno-unused-but-set-variable//g' {} + \[0m
2026-05-03T00:41:19.3920197Z [36;1m  -exec sed -i 's/-Wno-unused-but-set-parameter//g' {} + \[0m
2026-05-03T00:41:19.3920562Z [36;1m  -exec sed -i 's/-Wunused-but-set-variable//g' {} + \[0m
2026-05-03T00:41:19.3920920Z [36;1m  -exec sed -i 's/-Wunused-but-set-parameter//g' {} +[0m
2026-05-03T00:41:19.3921203Z [36;1m[0m
2026-05-03T00:41:19.3921492Z [36;1m# Step 4: Fix strict-prototypes (clang 15+ enforces C2x no-K&R rule)[0m
2026-05-03T00:41:19.3921877Z [36;1mecho "Fixing strict-prototypes issues..."[0m
2026-05-03T00:41:19.3922240Z [36;1mif [ -f "drivers/block/zram/zram_drv.c" ]; then[0m
2026-05-03T00:41:19.3922686Z [36;1m  sed -i 's/zram_debugfs_init()/zram_debugfs_init(void)/g' drivers/block/zram/zram_drv.c[0m
2026-05-03T00:41:19.3923286Z [36;1m  sed -i 's/zram_debugfs_destroy()/zram_debugfs_destroy(void)/g' drivers/block/zram/zram_drv.c[0m
2026-05-03T00:41:19.3923707Z [36;1mfi[0m
2026-05-03T00:41:19.3923875Z [36;1m[0m
2026-05-03T00:41:19.3924082Z [36;1m# Step 5: Add clang compatibility CFLAGS[0m
2026-05-03T00:41:19.3924478Z [36;1m# CRITICAL: Append at END of Makefile, NOT inside the KBUILD_CFLAGS := block![0m
2026-05-03T00:41:19.3924937Z [36;1m# The old sed '/^KBUILD_CFLAGS.*:=/a ...' was inserting lines in the[0m
2026-05-03T00:41:19.3925424Z [36;1m# middle of a multi-line backslash-continuation block, breaking Makefile syntax.[0m
2026-05-03T00:41:19.3925923Z [36;1m# Error was: "Makefile:447: *** recipe commences before first target. Stop."[0m
2026-05-03T00:41:19.3926291Z [36;1mif [ -f "Makefile" ]; then[0m
2026-05-03T00:41:19.3926648Z [36;1m  echo "Adding clang compatibility CFLAGS (appending to end of Makefile)..."[0m
2026-05-03T00:41:19.3927043Z [36;1m  cat >> Makefile << 'CLANG_COMPAT_EOF'[0m
2026-05-03T00:41:19.3927304Z [36;1m[0m
2026-05-03T00:41:19.3927526Z [36;1m# Clang compatibility flags (appended by CI)[0m
2026-05-03T00:41:19.3927822Z [36;1mKBUILD_CFLAGS += -Wno-error[0m
2026-05-03T00:41:19.3928137Z [36;1mKBUILD_CFLAGS += -Wno-implicit-function-declaration[0m
2026-05-03T00:41:19.3928721Z [36;1mKBUILD_CFLAGS += -Wno-strict-prototypes[0m
2026-05-03T00:41:19.3929049Z [36;1mKBUILD_CFLAGS += -Wno-return-type[0m
2026-05-03T00:41:19.3929352Z [36;1mKBUILD_CFLAGS += -Wno-unknown-warning-option[0m
2026-05-03T00:41:19.3929655Z [36;1mKBUILD_CFLAGS += -Wno-int-conversion[0m
2026-05-03T00:41:19.3930124Z [36;1mKBUILD_CFLAGS += -Wno-unused-function[0m
2026-05-03T00:41:19.3930431Z [36;1mKBUILD_CFLAGS += -Wno-misleading-indentation[0m
2026-05-03T00:41:19.3930725Z [36;1mKBUILD_CFLAGS += -Wno-bool-operation[0m
2026-05-03T00:41:19.3931004Z [36;1mKBUILD_CFLAGS += -Wno-uninitialized[0m
2026-05-03T00:41:19.3931267Z [36;1mCLANG_COMPAT_EOF[0m
2026-05-03T00:41:19.3931560Z [36;1m  echo "Clang CFLAGS appended successfully"[0m
2026-05-03T00:41:19.3931823Z [36;1mfi[0m
2026-05-03T00:41:19.3931995Z [36;1m[0m
2026-05-03T00:41:19.3932198Z [36;1mecho "=== Compiler fixes applied ==="[0m
2026-05-03T00:41:19.3952010Z shell: /usr/bin/bash -e {0}
2026-05-03T00:41:19.3952240Z env:
2026-05-03T00:41:19.3952419Z   KERNEL_NAME: Castorice
2026-05-03T00:41:19.3952633Z   DEVICE_CODE: fire
2026-05-03T00:41:19.3952846Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:41:19.3953368Z   CLANG_VERSION: ZyC clang version 15.0.7 (https://github.com/llvm/llvm-project 8dfdcc7b7bf66834a761bd8de445840ef68e4d1a)
2026-05-03T00:41:19.3953906Z   LLD_VERSION: LLD 15.0.7 (compatible with GNU linkers)
2026-05-03T00:41:19.3954250Z   KERNEL_HEAD_HASH: 1d1aedfe40b2f5fd06c783b752af0197f38966eb
2026-05-03T00:41:19.3954556Z   KSU_DIR: KernelSU-Next
2026-05-03T00:41:19.3954758Z   KSU_VERSION: 33042
2026-05-03T00:41:19.3954954Z   KERNEL_VERSION: 
2026-05-03T00:41:19.3955274Z   ZIP_NAME: 
2026-05-03T00:41:19.3955455Z ##[endgroup]
2026-05-03T00:41:19.3994012Z === Fixing modern Clang vs 4.19 incompatibilities ===
2026-05-03T00:41:19.3994501Z Removing compound -Werror=xxx flags...
2026-05-03T00:41:20.0175327Z Removing standalone -Werror...
2026-05-03T00:41:20.9071213Z Removing clang-incompatible warning flags...
2026-05-03T00:41:23.7397342Z Fixing strict-prototypes issues...
2026-05-03T00:41:23.7439652Z Adding clang compatibility CFLAGS (appending to end of Makefile)...
2026-05-03T00:41:23.7452367Z Clang CFLAGS appended successfully
2026-05-03T00:41:23.7452778Z === Compiler fixes applied ===
2026-05-03T00:41:23.7479810Z ##[group]Run cd $GITHUB_WORKSPACE/kernel
2026-05-03T00:41:23.7480152Z [36;1mcd $GITHUB_WORKSPACE/kernel[0m
2026-05-03T00:41:23.7480391Z [36;1m[0m
2026-05-03T00:41:23.7480587Z [36;1mexport KBUILD_BUILD_USER=Castorice[0m
2026-05-03T00:41:23.7480877Z [36;1mexport KBUILD_BUILD_HOST=naidrahiqa[0m
2026-05-03T00:41:23.7481148Z [36;1mexport KBUILD_BUILD_VERSION=1[0m
2026-05-03T00:41:23.7481391Z [36;1m[0m
2026-05-03T00:41:23.7481626Z [36;1mARGS="PATH=$GITHUB_WORKSPACE/ZyClang/bin:$PATH \[0m
2026-05-03T00:41:23.7481944Z [36;1m  ARCH=arm64 \[0m
2026-05-03T00:41:23.7482166Z [36;1m  SUBARCH=arm64 \[0m
2026-05-03T00:41:23.7482420Z [36;1m  CROSS_COMPILE=aarch64-linux-gnu- \[0m
2026-05-03T00:41:23.7482747Z [36;1m  CROSS_COMPILE_ARM32=arm-linux-gnueabi- \[0m
2026-05-03T00:41:23.7483024Z [36;1m  CC=clang \[0m
2026-05-03T00:41:23.7483226Z [36;1m  NM=llvm-nm \[0m
2026-05-03T00:41:23.7483439Z [36;1m  CXX=clang++ \[0m
2026-05-03T00:41:23.7483639Z [36;1m  AR=llvm-ar \[0m
2026-05-03T00:41:23.7483867Z [36;1m  LD=ld.lld \[0m
2026-05-03T00:41:23.7484089Z [36;1m  STRIP=llvm-strip \[0m
2026-05-03T00:41:23.7484326Z [36;1m  OBJCOPY=llvm-objcopy \[0m
2026-05-03T00:41:23.7484585Z [36;1m  OBJDUMP=llvm-objdump \[0m
2026-05-03T00:41:23.7484818Z [36;1m  OBJSIZE=llvm-size \[0m
2026-05-03T00:41:23.7485050Z [36;1m  READELF=llvm-readelf \[0m
2026-05-03T00:41:23.7485292Z [36;1m  HOSTAR=llvm-ar \[0m
2026-05-03T00:41:23.7485511Z [36;1m  HOSTLD=ld.lld \[0m
2026-05-03T00:41:23.7485726Z [36;1m  HOSTCC=clang \[0m
2026-05-03T00:41:23.7485934Z [36;1m  HOSTCXX=clang++ \[0m
2026-05-03T00:41:23.7486151Z [36;1m  LLVM=1"[0m
2026-05-03T00:41:23.7486336Z [36;1m[0m
2026-05-03T00:41:23.7486512Z [36;1m# Generate .config[0m
2026-05-03T00:41:23.7486727Z [36;1mrm -rf out[0m
2026-05-03T00:41:23.7486943Z [36;1mmake O=out $ARGS fire_defconfig[0m
2026-05-03T00:41:23.7487191Z [36;1m[0m
2026-05-03T00:41:23.7487502Z [36;1mKERNEL_VERSION=$(make O=out $ARGS kernelversion 2>/dev/null | grep "4.19")[0m
2026-05-03T00:41:23.7487956Z [36;1mecho "KERNEL_VERSION=$KERNEL_VERSION" >> $GITHUB_ENV[0m
2026-05-03T00:41:23.7488301Z [36;1mecho "=== Building Linux $KERNEL_VERSION ==="[0m
2026-05-03T00:41:23.7488766Z [36;1m[0m
2026-05-03T00:41:23.7488936Z [36;1m# Build[0m
2026-05-03T00:41:23.7489198Z [36;1mmake O=out $ARGS -j"$(nproc --all)" 2>&1 | tee build.log[0m
2026-05-03T00:41:23.7489506Z [36;1m[0m
2026-05-03T00:41:23.7489668Z [36;1m# Verify[0m
2026-05-03T00:41:23.7489888Z [36;1mIMAGE="out/arch/arm64/boot/Image.gz-dtb"[0m
2026-05-03T00:41:23.7490164Z [36;1mif [ ! -f "$IMAGE" ]; then[0m
2026-05-03T00:41:23.7490444Z [36;1m  echo "BUILD FAILED! Image.gz-dtb not found"[0m
2026-05-03T00:41:23.7490721Z [36;1m  tail -100 build.log[0m
2026-05-03T00:41:23.7490936Z [36;1m  exit 1[0m
2026-05-03T00:41:23.7491112Z [36;1mfi[0m
2026-05-03T00:41:23.7491297Z [36;1mecho "BUILD SUCCESS: $IMAGE"[0m
2026-05-03T00:41:23.7491540Z [36;1mls -lah $IMAGE[0m
2026-05-03T00:41:23.7512876Z shell: /usr/bin/bash -e {0}
2026-05-03T00:41:23.7513106Z env:
2026-05-03T00:41:23.7513289Z   KERNEL_NAME: Castorice
2026-05-03T00:41:23.7513502Z   DEVICE_CODE: fire
2026-05-03T00:41:23.7513721Z   FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
2026-05-03T00:41:23.7514248Z   CLANG_VERSION: ZyC clang version 15.0.7 (https://github.com/llvm/llvm-project 8dfdcc7b7bf66834a761bd8de445840ef68e4d1a)
2026-05-03T00:41:23.7514967Z   LLD_VERSION: LLD 15.0.7 (compatible with GNU linkers)
2026-05-03T00:41:23.7515317Z   KERNEL_HEAD_HASH: 1d1aedfe40b2f5fd06c783b752af0197f38966eb
2026-05-03T00:41:23.7515623Z   KSU_DIR: KernelSU-Next
2026-05-03T00:41:23.7515828Z   KSU_VERSION: 33042
2026-05-03T00:41:23.7516022Z   KERNEL_VERSION: 
2026-05-03T00:41:23.7516210Z   ZIP_NAME: 
2026-05-03T00:41:23.7516386Z ##[endgroup]
2026-05-03T00:41:23.7622180Z make[1]: Entering directory '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/out'
2026-05-03T00:41:23.9925630Z   HOSTCC  scripts/basic/fixdep
2026-05-03T00:41:24.1398535Z   GEN     ./Makefile
2026-05-03T00:41:24.1569236Z   HOSTCC  scripts/kconfig/conf.o
2026-05-03T00:41:24.2741351Z   YACC    scripts/kconfig/zconf.tab.c
2026-05-03T00:41:24.4406937Z   LEX     scripts/kconfig/zconf.lex.c
2026-05-03T00:41:24.4701563Z   HOSTCC  scripts/kconfig/zconf.tab.o
2026-05-03T00:41:25.6512791Z   HOSTLD  scripts/kconfig/conf
2026-05-03T00:41:26.0202687Z drivers/misc/mediatek/base/power/Kconfig:90:warning: ignoring type redefinition of 'MTK_QOS_FRAMEWORK' from 'tristate' to 'bool'
2026-05-03T00:41:26.0365234Z drivers/input/touchscreen/mediatek/goodix_berlin_driver/Kconfig:4:warning: ignoring type redefinition of 'TOUCHSCREEN_GOODIX_BRL' from 'bool' to 'tristate'
2026-05-03T00:41:26.0435628Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T00:41:26.0437059Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T00:41:26.0438656Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T00:41:26.0440030Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T00:41:26.0441399Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T00:41:26.0442764Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T00:41:26.0444116Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T00:41:26.0445467Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T00:41:26.0447073Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T00:41:26.0448374Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T00:41:26.0449590Z drivers/power/supply/mediatek/charger/Kconfig:199:warning: ignoring type redefinition of 'CHARGER_BQ25890' from 'tristate' to 'bool'
2026-05-03T00:41:26.0765090Z drivers/soc/mediatek/Kconfig:7:warning: ignoring type redefinition of 'MTK_CMDQ' from 'bool' to 'tristate'
2026-05-03T00:41:26.1785842Z drivers/input/touchscreen/mediatek/hxchipset_hx83102p/Kconfig:19:warning: choice value used outside its choice group
2026-05-03T00:41:26.1787194Z drivers/input/touchscreen/mediatek/hxchipset_hx83102p/Kconfig:28:warning: choice value used outside its choice group
2026-05-03T00:41:26.1788802Z drivers/input/touchscreen/mediatek/hxchipset_hx83102p/Kconfig:16:warning: choice default symbol 'TOUCHSCREEN_HIMAX_INCELL' is not contained in the choice
2026-05-03T00:41:26.2083954Z arch/arm64/configs/fire_defconfig:447:warning: override: reassigning to symbol CMDLINE_FORCE
2026-05-03T00:41:26.2084926Z arch/arm64/configs/fire_defconfig:448:warning: override: reassigning to symbol EFI
2026-05-03T00:41:26.2121065Z arch/arm64/configs/fire_defconfig:5548:warning: override: reassigning to symbol CRYPTO_GHASH_ARM64_CE
2026-05-03T00:41:26.2122552Z arch/arm64/configs/fire_defconfig:5573:warning: override: reassigning to symbol ZRAM
2026-05-03T00:41:26.2123530Z arch/arm64/configs/fire_defconfig:5574:warning: override: reassigning to symbol ZSMALLOC
2026-05-03T00:41:26.2124515Z arch/arm64/configs/fire_defconfig:5575:warning: override: reassigning to symbol COMPACTION
2026-05-03T00:41:26.2125442Z arch/arm64/configs/fire_defconfig:5576:warning: override: reassigning to symbol KSM
2026-05-03T00:41:26.2126342Z arch/arm64/configs/fire_defconfig:5577:warning: override: reassigning to symbol HZ_1000
2026-05-03T00:41:26.2127511Z arch/arm64/configs/fire_defconfig:5577:warning: override: HZ_1000 changes choice state
2026-05-03T00:41:26.2128708Z arch/arm64/configs/fire_defconfig:5580:warning: override: reassigning to symbol TCP_CONG_ADVANCED
2026-05-03T00:41:26.2129735Z arch/arm64/configs/fire_defconfig:5581:warning: override: reassigning to symbol TCP_CONG_BBR
2026-05-03T00:41:26.2130724Z arch/arm64/configs/fire_defconfig:5582:warning: override: reassigning to symbol IP_NF_TARGET_TTL
2026-05-03T00:41:26.2131693Z arch/arm64/configs/fire_defconfig:5583:warning: override: reassigning to symbol IP6_NF_TARGET_HL
2026-05-03T00:41:26.2132577Z arch/arm64/configs/fire_defconfig:5586:warning: override: reassigning to symbol IP_SET
2026-05-03T00:41:26.2137198Z 
2026-05-03T00:41:26.2137537Z WARNING: unmet direct dependencies detected for BACKLIGHT_CLASS_DEVICE
2026-05-03T00:41:26.2138184Z   Depends on [n]: HAS_IOMEM [=y] && BACKLIGHT_LCD_SUPPORT [=n]
2026-05-03T00:41:26.2138830Z   Selected by [y]:
2026-05-03T00:41:26.2139122Z   - LM3697_SUPPORT [=y]
2026-05-03T00:41:26.2174031Z 
2026-05-03T00:41:26.2174419Z WARNING: unmet direct dependencies detected for MTK_PID_MAP
2026-05-03T00:41:26.2175206Z   Depends on [n]: (MTK_GMO_RAM_OPTIMIZE [=n] && MTK_ENG_BUILD [=n] || !MTK_GMO_RAM_OPTIMIZE [=n]) && DEBUG_FS [=n]
2026-05-03T00:41:26.2175868Z   Selected by [y]:
2026-05-03T00:41:26.2176139Z   - MACH_MT6768 [=y]
2026-05-03T00:41:26.2183175Z 
2026-05-03T00:41:26.2183511Z WARNING: unmet direct dependencies detected for MTK_CACHE_PARITY_CHECK
2026-05-03T00:41:26.2184059Z   Depends on [n]: MTK_SDA [=n]
2026-05-03T00:41:26.2184379Z   Selected by [y]:
2026-05-03T00:41:26.2184650Z   - MACH_MT6768 [=y]
2026-05-03T00:41:26.2219101Z 
2026-05-03T00:41:26.2219582Z WARNING: unmet direct dependencies detected for BACKLIGHT_CLASS_DEVICE
2026-05-03T00:41:26.2220241Z   Depends on [n]: HAS_IOMEM [=y] && BACKLIGHT_LCD_SUPPORT [=n]
2026-05-03T00:41:26.2220697Z   Selected by [y]:
2026-05-03T00:41:26.2220985Z   - LM3697_SUPPORT [=y]
2026-05-03T00:41:26.2241352Z 
2026-05-03T00:41:26.2241795Z WARNING: unmet direct dependencies detected for MTK_PID_MAP
2026-05-03T00:41:26.2242654Z   Depends on [n]: (MTK_GMO_RAM_OPTIMIZE [=n] && MTK_ENG_BUILD [=n] || !MTK_GMO_RAM_OPTIMIZE [=n]) && DEBUG_FS [=n]
2026-05-03T00:41:26.2243387Z   Selected by [y]:
2026-05-03T00:41:26.2243810Z   - MACH_MT6768 [=y]
2026-05-03T00:41:26.2244560Z 
2026-05-03T00:41:26.2244936Z WARNING: unmet direct dependencies detected for MTK_CACHE_PARITY_CHECK
2026-05-03T00:41:26.2245508Z   Depends on [n]: MTK_SDA [=n]
2026-05-03T00:41:26.2245847Z   Selected by [y]:
2026-05-03T00:41:26.2246131Z   - MACH_MT6768 [=y]
2026-05-03T00:41:26.2970385Z #
2026-05-03T00:41:26.2970752Z # configuration written to .config
2026-05-03T00:41:26.2971147Z #
2026-05-03T00:41:26.2993873Z make[1]: Leaving directory '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/out'
2026-05-03T00:41:27.6400927Z === Building Linux 4.19.191 ===
2026-05-03T00:41:27.6464274Z make[1]: Entering directory '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/out'
2026-05-03T00:41:28.9861238Z   UPD     include/config/kernel.release
2026-05-03T00:41:28.9969372Z   GEN     ./Makefile
2026-05-03T00:41:29.0032122Z   WRAP    arch/arm64/include/generated/uapi/asm/errno.h
2026-05-03T00:41:29.0033617Z   WRAP    arch/arm64/include/generated/uapi/asm/ioctl.h
2026-05-03T00:41:29.0041360Z   WRAP    arch/arm64/include/generated/uapi/asm/ioctls.h
2026-05-03T00:41:29.0044433Z   WRAP    arch/arm64/include/generated/uapi/asm/ipcbuf.h
2026-05-03T00:41:29.0055362Z   WRAP    arch/arm64/include/generated/uapi/asm/kvm_para.h
2026-05-03T00:41:29.0058684Z   WRAP    arch/arm64/include/generated/uapi/asm/mman.h
2026-05-03T00:41:29.0067646Z   WRAP    arch/arm64/include/generated/uapi/asm/msgbuf.h
2026-05-03T00:41:29.0077087Z   WRAP    arch/arm64/include/generated/uapi/asm/poll.h
2026-05-03T00:41:29.0079658Z   WRAP    arch/arm64/include/generated/uapi/asm/resource.h
2026-05-03T00:41:29.0080451Z   WRAP    arch/arm64/include/generated/uapi/asm/sembuf.h
2026-05-03T00:41:29.0081201Z   WRAP    arch/arm64/include/generated/uapi/asm/shmbuf.h
2026-05-03T00:41:29.0082285Z   WRAP    arch/arm64/include/generated/uapi/asm/socket.h
2026-05-03T00:41:29.0083172Z   WRAP    arch/arm64/include/generated/uapi/asm/sockios.h
2026-05-03T00:41:29.0088938Z   WRAP    arch/arm64/include/generated/uapi/asm/swab.h
2026-05-03T00:41:29.0095257Z   WRAP    arch/arm64/include/generated/uapi/asm/termbits.h
2026-05-03T00:41:29.0099026Z   WRAP    arch/arm64/include/generated/uapi/asm/termios.h
2026-05-03T00:41:29.0105800Z   WRAP    arch/arm64/include/generated/uapi/asm/types.h
2026-05-03T00:41:29.0180457Z   UPD     include/generated/uapi/linux/version.h
2026-05-03T00:41:29.0387017Z   UPD     include/generated/utsrelease.h
2026-05-03T00:41:29.7266812Z $GED: CONFIG_MTK_PLATFORM is ["mt6768"]
2026-05-03T00:41:29.7351984Z *MTK_GPU_VERSION 2 = valhall
2026-05-03T00:41:29.7400250Z *MTK_GPU_VERSION 3 = r32p1
2026-05-03T00:41:29.7469359Z mali MTK evironment, building r32p1 DDK
2026-05-03T00:41:29.7490583Z mtk-Kbuild CONFIG_MALI_PLATFORM_THIRDPARTY := y
2026-05-03T00:41:29.7491557Z mtk-Kbuild CONFIG_MALI_PLATFORM_THIRDPARTY_NAME := "mt6768"
2026-05-03T00:41:29.7492321Z mali MTK evironment, building r32p1 DDK
2026-05-03T00:41:29.7492996Z mtk-Kbuild CONFIG_MALI_PLATFORM_THIRDPARTY := y
2026-05-03T00:41:29.7493754Z mtk-Kbuild CONFIG_MALI_PLATFORM_THIRDPARTY_NAME := "mt6768"
2026-05-03T00:41:29.7494491Z mali MTK evironment, building r32p1 DDK
2026-05-03T00:41:29.7495161Z mtk-Kbuild CONFIG_MALI_PLATFORM_THIRDPARTY := y
2026-05-03T00:41:29.7495915Z mtk-Kbuild CONFIG_MALI_PLATFORM_THIRDPARTY_NAME := "mt6768"
2026-05-03T00:41:29.7826675Z   Using .. as source for kernel
2026-05-03T00:41:29.8174027Z   WRAP    arch/arm64/include/generated/asm/bugs.h
2026-05-03T00:41:29.8207170Z   WRAP    arch/arm64/include/generated/asm/delay.h
2026-05-03T00:41:29.8238172Z   WRAP    arch/arm64/include/generated/asm/div64.h
2026-05-03T00:41:29.8259349Z   WRAP    arch/arm64/include/generated/asm/dma.h
2026-05-03T00:41:29.8284834Z   WRAP    arch/arm64/include/generated/asm/dma-contiguous.h
2026-05-03T00:41:29.8285857Z   WRAP    arch/arm64/include/generated/asm/early_ioremap.h
2026-05-03T00:41:29.8286768Z   WRAP    arch/arm64/include/generated/asm/emergency-restart.h
2026-05-03T00:41:29.8287525Z   WRAP    arch/arm64/include/generated/asm/hw_irq.h
2026-05-03T00:41:29.8288232Z   WRAP    arch/arm64/include/generated/asm/irq_regs.h
2026-05-03T00:41:29.8289611Z   WRAP    arch/arm64/include/generated/asm/kdebug.h
2026-05-03T00:41:29.8290320Z   WRAP    arch/arm64/include/generated/asm/kmap_types.h
2026-05-03T00:41:29.8296205Z   WRAP    arch/arm64/include/generated/asm/local.h
2026-05-03T00:41:29.8306197Z   WRAP    arch/arm64/include/generated/asm/local64.h
2026-05-03T00:41:29.8321183Z   WRAP    arch/arm64/include/generated/asm/mcs_spinlock.h
2026-05-03T00:41:29.8338334Z   WRAP    arch/arm64/include/generated/asm/mm-arch-hooks.h
2026-05-03T00:41:29.8349815Z   WRAP    arch/arm64/include/generated/asm/msi.h
2026-05-03T00:41:29.8365304Z   WRAP    arch/arm64/include/generated/asm/preempt.h
2026-05-03T00:41:29.8377763Z   WRAP    arch/arm64/include/generated/asm/qrwlock.h
2026-05-03T00:41:29.8387560Z   WRAP    arch/arm64/include/generated/asm/qspinlock.h
2026-05-03T00:41:29.8406724Z   WRAP    arch/arm64/include/generated/asm/rwsem.h
2026-05-03T00:41:29.8409191Z   WRAP    arch/arm64/include/generated/asm/segment.h
2026-05-03T00:41:29.8424410Z   WRAP    arch/arm64/include/generated/asm/serial.h
2026-05-03T00:41:29.8439452Z   WRAP    arch/arm64/include/generated/asm/set_memory.h
2026-05-03T00:41:29.8453741Z   WRAP    arch/arm64/include/generated/asm/sizes.h
2026-05-03T00:41:29.8465102Z   WRAP    arch/arm64/include/generated/asm/switch_to.h
2026-05-03T00:41:29.8482365Z   WRAP    arch/arm64/include/generated/asm/trace_clock.h
2026-05-03T00:41:29.8497829Z   WRAP    arch/arm64/include/generated/asm/unaligned.h
2026-05-03T00:41:29.8505065Z   WRAP    arch/arm64/include/generated/asm/user.h
2026-05-03T00:41:29.8525761Z   WRAP    arch/arm64/include/generated/asm/vga.h
2026-05-03T00:41:29.8526741Z   WRAP    arch/arm64/include/generated/asm/xor.h
2026-05-03T00:41:29.9823888Z   HOSTCC  scripts/dtc/dtc.o
2026-05-03T00:41:30.0324803Z   HOSTCC  scripts/genksyms/genksyms.o
2026-05-03T00:41:30.0831346Z   HOSTCC  scripts/dtc/flattree.o
2026-05-03T00:41:30.1848264Z -- KernelSU-Next Git repo detected at: /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/KernelSU-Next
2026-05-03T00:41:30.1854875Z -- KernelSU-Next version: 33132
2026-05-03T00:41:30.1864144Z -- KernelSU-Next tag: v3.2.0-legacy
2026-05-03T00:41:30.1864821Z -- KernelSU-Next Manager signature size: 0x3e6
2026-05-03T00:41:30.1865821Z -- KernelSU-Next Manager signature hash: 79e590113c4c4c0c222978e413a5faa801666957b1212a328e46c00c69821bf7
2026-05-03T00:41:30.1887780Z -- KernelSU-Next: Hook mode: Manual
2026-05-03T00:41:30.1903727Z   CC      scripts/mod/empty.o
2026-05-03T00:41:30.1928333Z -- KSU_NEXT: adding function 'static int can_umount(const struct path *path, int flags);' to ../fs/namespace.c
2026-05-03T00:41:30.2019631Z -- KSU_NEXT: adding function 'int path_umount(struct path *path, int flags);' to ../fs/namespace.c
2026-05-03T00:41:30.2128313Z -- KSU_NEXT: adding 'int path_umount(struct path *path, int flags);' to ../fs/internal.h
2026-05-03T00:41:30.2171328Z -- KSU_NEXT: patching struct seccomp for filter_count
2026-05-03T00:41:30.2229041Z -- KSU_NEXT: patching selinux/hooks.c for selinux_inode
2026-05-03T00:41:30.2426528Z -- KSU_NEXT: patching selinux/selinuxfs.c for selinux_inode
2026-05-03T00:41:30.2429263Z   YACC    scripts/genksyms/parse.tab.c
2026-05-03T00:41:30.2468020Z   HOSTCC  scripts/mod/mk_elfconfig
2026-05-03T00:41:30.2479383Z -- KSU_NEXT: patching selinux/xfrm.c for selinux_cred
2026-05-03T00:41:30.2507462Z -- KSU_NEXT: patching selinux/include/objsec.h for selinux_inode
2026-05-03T00:41:30.2563601Z -- KSU_NEXT: patching selinux/include/objsec.h for selinux_cred
2026-05-03T00:41:30.3153020Z   HOSTCC  scripts/dtc/fstree.o
2026-05-03T00:41:30.3280189Z   CC      scripts/mod/devicetable-offsets.s
2026-05-03T00:41:30.3671973Z   MKELF   scripts/mod/elfconfig.h
2026-05-03T00:41:30.3709353Z   HOSTCC  scripts/mod/modpost.o
2026-05-03T00:41:30.3767270Z   LEX     scripts/genksyms/lex.lex.c
2026-05-03T00:41:30.3803153Z   HOSTCC  scripts/dtc/data.o
2026-05-03T00:41:30.3864680Z   YACC    scripts/genksyms/parse.tab.h
2026-05-03T00:41:30.5255352Z   HOSTCC  scripts/dtc/livetree.o
2026-05-03T00:41:30.5319926Z   HOSTCC  scripts/genksyms/parse.tab.o
2026-05-03T00:41:30.7039411Z   HOSTCC  scripts/genksyms/lex.lex.o
2026-05-03T00:41:30.8546091Z   HOSTCC  scripts/dtc/treesource.o
2026-05-03T00:41:30.9576568Z   UPD     scripts/mod/devicetable-offsets.h
2026-05-03T00:41:30.9614695Z   HOSTCC  scripts/mod/sumversion.o
2026-05-03T00:41:31.0134433Z   HOSTCC  scripts/dtc/srcpos.o
2026-05-03T00:41:31.0339879Z ../drivers/misc/mediatek/base/power/cpufreq_v1/src/Makefile:89: "use CONFIG_MTK_TINYSYS_SSPM_V1"
2026-05-03T00:41:31.1119473Z   HOSTLD  scripts/genksyms/genksyms
2026-05-03T00:41:31.1529647Z   HOSTCC  scripts/dtc/checks.o
2026-05-03T00:41:31.1627728Z   HOSTCC  scripts/mod/file2alias.o
2026-05-03T00:41:31.2079761Z ../drivers/misc/mediatek/base/power/ppm_v3/src/Makefile:110: USE_PPM_CPI
2026-05-03T00:41:31.2319393Z   CC      kernel/bounds.s
2026-05-03T00:41:31.3505667Z   UPD     include/generated/timeconst.h
2026-05-03T00:41:31.3574922Z   UPD     include/generated/bounds.h
2026-05-03T00:41:31.3639202Z   CC      arch/arm64/kernel/asm-offsets.s
2026-05-03T00:41:31.3969216Z ..
2026-05-03T00:41:31.4059133Z FDVT: Drv use 4.0 folder
2026-05-03T00:41:31.4128987Z ..
2026-05-03T00:41:31.4248956Z ..
2026-05-03T00:41:31.4849509Z ../drivers/misc/mediatek/ccu/src/Makefile:33: CCU_MAKE_FILE_CALLED
2026-05-03T00:41:31.4919403Z ../drivers/misc/mediatek/ccu/src/1.2/Makefile:28: CCU_INC=../drivers/misc/mediatek/ccu/src/mt6768/ccu_ext_interface
2026-05-03T00:41:31.5679791Z   HOSTCC  scripts/dtc/util.o
2026-05-03T00:41:31.5840455Z   HOSTLD  scripts/mod/modpost
2026-05-03T00:41:31.6992318Z CONFIG_MTK_PLATFORM_CCCI := mt6768
2026-05-03T00:41:31.7019066Z CONFIG_MTK_PLATFORM_CCCI := "mt6768"
2026-05-03T00:41:31.7049141Z MTK_PLATFORM_CCCI := mt6768
2026-05-03T00:41:31.7065964Z   LEX     scripts/dtc/dtc-lexer.lex.c
2026-05-03T00:41:31.7141978Z   YACC    scripts/dtc/dtc-parser.tab.h
2026-05-03T00:41:31.8169702Z ************  drivers/trusty/mtee-kree mk ************
2026-05-03T00:41:31.8489429Z   YACC    scripts/dtc/dtc-parser.tab.c
2026-05-03T00:41:31.8607302Z imgsensor drv by common ../common/v1/s5kjns_sunny_mipi_raw/ ../common/v1/ov50d40_truly_mipi_raw/ ../common/v1/ov8856_sunny_mipi_raw/ ../common/v1/ov8856_ofilm_mipi_raw/ ../common/v1/imx355_sunny_mipi_raw/ ../common/v1/sc820cs_truly_mipi_raw/ ../common/v1/sc202cs_sunny_mipi_raw/ ../common/v1/ov02b10_truly_mipi_raw/
2026-05-03T00:41:31.8744588Z   HOSTCC  scripts/dtc/yamltree.o
2026-05-03T00:41:31.8959956Z   UPD     include/generated/asm-offsets.h
2026-05-03T00:41:31.8988569Z   CALL    ../scripts/checksyscalls.sh
2026-05-03T00:41:31.9819289Z   HOSTCC  scripts/selinux/genheaders/genheaders
2026-05-03T00:41:31.9879201Z   HOSTCC  scripts/dtc/dtc-lexer.lex.o
2026-05-03T00:41:32.0129386Z   LDS     scripts/module-lto.lds
2026-05-03T00:41:32.0379407Z   HOSTCC  scripts/dtc/dtc-parser.tab.o
2026-05-03T00:41:32.1137681Z   HOSTCC  scripts/selinux/mdp/mdp
2026-05-03T00:41:32.1460537Z M4U platform folder:"mt6768"
2026-05-03T00:41:32.1481442Z M4U version:2.0
2026-05-03T00:41:32.2526286Z   LDS     arch/arm64/kernel/vdso/vdso.lds
2026-05-03T00:41:32.2649389Z   CC      arch/arm64/kernel/vdso/vgettimeofday.o
2026-05-03T00:41:32.2879615Z   HOSTLD  scripts/dtc/dtc
2026-05-03T00:41:32.2949978Z   AS      arch/arm64/kernel/vdso/note.o
2026-05-03T00:41:32.3246074Z   HOSTCC  scripts/bin2c
2026-05-03T00:41:32.4000581Z   HOSTCC  scripts/kallsyms
2026-05-03T00:41:32.4029676Z   AS      arch/arm64/kernel/vdso/sigreturn.o
2026-05-03T00:41:32.4106359Z   HOSTCC  scripts/pnmtologo
2026-05-03T00:41:32.4379709Z   LD      arch/arm64/kernel/vdso/vdso.so.dbg
2026-05-03T00:41:32.4579568Z   VDSOSYM include/generated/vdso-offsets.h
2026-05-03T00:41:32.4699305Z   HOSTCC  scripts/sortextable
2026-05-03T00:41:32.6529617Z   HOSTCC  scripts/asn1_compiler
2026-05-03T00:41:32.7209700Z TCORE_UT_TESTS_SUPPORT = n
2026-05-03T00:41:32.7239197Z TCORE_PROFILING_SUPPORT = n
2026-05-03T00:41:32.7259036Z TCORE_PROFILING_AUTO_DUMP = n
2026-05-03T00:41:32.7299157Z TCORE_MEMORY_LEAK_DETECTION_SUPPORT = n
2026-05-03T00:41:32.7328936Z   HOSTCC  scripts/extract-cert
2026-05-03T00:41:32.9886733Z ION:enable mtk ion
2026-05-03T00:41:32.9953590Z "CONFIG_MICROTRUST_TEE_VERSION="400""
2026-05-03T00:41:33.0017200Z "CONFIG_MICROTRUST_TEE_SUPPORT=y"
2026-05-03T00:41:33.0018068Z "CONFIG_MICROTRUST_TZ_DRIVER=Y"
2026-05-03T00:41:33.0019179Z "CONFIG_MICROTRUST_VFS_DRIVER=Y"
2026-05-03T00:41:33.0019690Z "CONFIG_MICROTRUST_FP_DRIVER=Y"
2026-05-03T00:41:33.0020278Z "CONFIG_MICROTRUST_DEBUG="
2026-05-03T00:41:33.0021816Z "CONFIG_MICROTRUST_TEST_DRIVERS="
2026-05-03T00:41:33.0642563Z ../scripts/extract-cert.c:46:14: warning: 'ERR_get_error_line' is deprecated [-Wdeprecated-declarations]
2026-05-03T00:41:33.0669776Z         while ((e = ERR_get_error_line(&file, &line))) {
2026-05-03T00:41:33.0684636Z                     ^
2026-05-03T00:41:33.0685507Z /usr/include/openssl/err.h:422:1: note: 'ERR_get_error_line' has been explicitly marked deprecated here
2026-05-03T00:41:33.0686422Z OSSL_DEPRECATEDIN_3_0
2026-05-03T00:41:33.0686884Z ^
2026-05-03T00:41:33.0687485Z /usr/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
2026-05-03T00:41:33.0688604Z #   define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
2026-05-03T00:41:33.0689269Z                                                 ^
2026-05-03T00:41:33.0689879Z /usr/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
2026-05-03T00:41:33.0690592Z #     define OSSL_DEPRECATED(since) __attribute__((deprecated))
2026-05-03T00:41:33.0691092Z                                                    ^
2026-05-03T00:41:33.0691792Z ../scripts/extract-cert.c:59:9: warning: 'ERR_get_error_line' is deprecated [-Wdeprecated-declarations]
2026-05-03T00:41:33.0692736Z         while (ERR_get_error_line(&file, &line)) {}
2026-05-03T00:41:33.0693136Z                ^
2026-05-03T00:41:33.0693711Z /usr/include/openssl/err.h:422:1: note: 'ERR_get_error_line' has been explicitly marked deprecated here
2026-05-03T00:41:33.0694371Z OSSL_DEPRECATEDIN_3_0
2026-05-03T00:41:33.0694665Z ^
2026-05-03T00:41:33.0695148Z /usr/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
2026-05-03T00:41:33.0695908Z #   define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
2026-05-03T00:41:33.0696449Z                                                 ^
2026-05-03T00:41:33.0697016Z /usr/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
2026-05-03T00:41:33.0697750Z #     define OSSL_DEPRECATED(since) __attribute__((deprecated))
2026-05-03T00:41:33.0698251Z                                                    ^
2026-05-03T00:41:33.0699303Z ../scripts/extract-cert.c:124:3: warning: 'ENGINE_load_builtin_engines' is deprecated [-Wdeprecated-declarations]
2026-05-03T00:41:33.0700263Z                 ENGINE_load_builtin_engines();
2026-05-03T00:41:33.0700643Z                 ^
2026-05-03T00:41:33.0701295Z /usr/include/openssl/engine.h:358:1: note: 'ENGINE_load_builtin_engines' has been explicitly marked deprecated here
2026-05-03T00:41:33.0702185Z OSSL_DEPRECATEDIN_3_0 void ENGINE_load_builtin_engines(void);
2026-05-03T00:41:33.0702657Z ^
2026-05-03T00:41:33.0703169Z /usr/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
2026-05-03T00:41:33.0703913Z #   define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
2026-05-03T00:41:33.0704426Z                                                 ^
2026-05-03T00:41:33.0704994Z /usr/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
2026-05-03T00:41:33.0705672Z #     define OSSL_DEPRECATED(since) __attribute__((deprecated))
2026-05-03T00:41:33.0706166Z                                                    ^
2026-05-03T00:41:33.0706866Z ../scripts/extract-cert.c:126:7: warning: 'ENGINE_by_id' is deprecated [-Wdeprecated-declarations]
2026-05-03T00:41:33.0707569Z                 e = ENGINE_by_id("pkcs11");
2026-05-03T00:41:33.0707936Z                     ^
2026-05-03T00:41:33.0709136Z /usr/include/openssl/engine.h:336:1: note: 'ENGINE_by_id' has been explicitly marked deprecated here
2026-05-03T00:41:33.0709944Z OSSL_DEPRECATEDIN_3_0 ENGINE *ENGINE_by_id(const char *id);
2026-05-03T00:41:33.0710429Z ^
2026-05-03T00:41:33.0710914Z /usr/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
2026-05-03T00:41:33.0711692Z #   define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
2026-05-03T00:41:33.0712224Z                                                 ^
2026-05-03T00:41:33.0712828Z /usr/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
2026-05-03T00:41:33.0713542Z #     define OSSL_DEPRECATED(since) __attribute__((deprecated))
2026-05-03T00:41:33.0714057Z                                                    ^
2026-05-03T00:41:33.0714772Z ../scripts/extract-cert.c:128:7: warning: 'ENGINE_init' is deprecated [-Wdeprecated-declarations]
2026-05-03T00:41:33.0715476Z                 if (ENGINE_init(e))
2026-05-03T00:41:33.0715838Z                     ^
2026-05-03T00:41:33.0716473Z /usr/include/openssl/engine.h:620:1: note: 'ENGINE_init' has been explicitly marked deprecated here
2026-05-03T00:41:33.0717454Z OSSL_DEPRECATEDIN_3_0 int ENGINE_init(ENGINE *e);
2026-05-03T00:41:33.0717879Z ^
2026-05-03T00:41:33.0718363Z /usr/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
2026-05-03T00:41:33.0719448Z #   define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
2026-05-03T00:41:33.0719983Z                                                 ^
2026-05-03T00:41:33.0720589Z /usr/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
2026-05-03T00:41:33.0721301Z #     define OSSL_DEPRECATED(since) __attribute__((deprecated))
2026-05-03T00:41:33.0721964Z                                                    ^
2026-05-03T00:41:33.0722719Z ../scripts/extract-cert.c:133:9: warning: 'ENGINE_ctrl_cmd_string' is deprecated [-Wdeprecated-declarations]
2026-05-03T00:41:33.0723693Z                         ERR(!ENGINE_ctrl_cmd_string(e, "PIN", key_pass, 0), "Set PKCS#11 PIN");
2026-05-03T00:41:33.0724272Z                              ^
2026-05-03T00:41:33.0724982Z /usr/include/openssl/engine.h:478:1: note: 'ENGINE_ctrl_cmd_string' has been explicitly marked deprecated here
2026-05-03T00:41:33.0725771Z OSSL_DEPRECATEDIN_3_0
2026-05-03T00:41:33.0726076Z ^
2026-05-03T00:41:33.0726567Z /usr/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
2026-05-03T00:41:33.0727341Z #   define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
2026-05-03T00:41:33.0727863Z                                                 ^
2026-05-03T00:41:33.0741466Z /usr/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
2026-05-03T00:41:33.0742289Z #     define OSSL_DEPRECATED(since) __attribute__((deprecated))
2026-05-03T00:41:33.0742821Z                                                    ^
2026-05-03T00:41:33.0743566Z ../scripts/extract-cert.c:134:3: warning: 'ENGINE_ctrl_cmd' is deprecated [-Wdeprecated-declarations]
2026-05-03T00:41:33.0744374Z                 ENGINE_ctrl_cmd(e, "LOAD_CERT_CTRL", 0, &parms, NULL, 1);
2026-05-03T00:41:33.0744864Z                 ^
2026-05-03T00:41:33.0745453Z /usr/include/openssl/engine.h:450:1: note: 'ENGINE_ctrl_cmd' has been explicitly marked deprecated here
2026-05-03T00:41:33.0746335Z OSSL_DEPRECATEDIN_3_0 int ENGINE_ctrl_cmd(ENGINE *e, const char *cmd_name,
2026-05-03T00:41:33.0746868Z ^
2026-05-03T00:41:33.0747350Z /usr/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
2026-05-03T00:41:33.0748104Z #   define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
2026-05-03T00:41:33.0748839Z                                                 ^
2026-05-03T00:41:33.0749453Z /usr/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
2026-05-03T00:41:33.0750145Z #     define OSSL_DEPRECATED(since) __attribute__((deprecated))
2026-05-03T00:41:33.0750662Z                                                    ^
2026-05-03T00:41:33.0978568Z 7 warnings generated.
2026-05-03T00:41:33.1921979Z   CHK     include/generated/compile.h
2026-05-03T00:41:33.1959255Z   CC      init/main.o
2026-05-03T00:41:33.2010345Z   CC      init/do_mounts.o
2026-05-03T00:41:33.2107378Z   HOSTCC  usr/gen_init_cpio
2026-05-03T00:41:33.2294444Z   UPD     include/generated/compile.h
2026-05-03T00:41:33.2359327Z   CC      init/do_mounts_rd.o
2026-05-03T00:41:33.4047102Z   GEN     usr/initramfs_data.cpio
2026-05-03T00:41:33.4419355Z   AS      usr/initramfs_data.o
2026-05-03T00:41:33.4819437Z   AR      usr/built-in.a
2026-05-03T00:41:33.4939090Z   CC      init/do_mounts_initrd.o
2026-05-03T00:41:33.9442742Z   CC      arch/arm64/kernel/probes/kprobes.o
2026-05-03T00:41:34.1609457Z   CC      arch/arm64/mm/dma-mapping.o
2026-05-03T00:41:34.4633664Z   CC      arch/arm64/net/bpf_jit_comp.o
2026-05-03T00:41:34.4697080Z   CC      arch/arm64/kernel/probes/decode-insn.o
2026-05-03T00:41:34.6849418Z   CC      init/initramfs.o
2026-05-03T00:41:34.9033899Z   AS      arch/arm64/kernel/probes/kprobes_trampoline.o
2026-05-03T00:41:34.9499684Z   CC      arch/arm64/kernel/probes/simulate-insn.o
2026-05-03T00:41:35.0859437Z   CC      arch/arm64/mm/extable.o
2026-05-03T00:41:35.2985131Z   CC      init/calibrate.o
2026-05-03T00:41:35.3559044Z   CC      arch/arm64/mm/fault.o
2026-05-03T00:41:35.3855226Z   AR      arch/arm64/net/built-in.a
2026-05-03T00:41:35.4031825Z   OBJCOPY arch/arm64/kernel/vdso/vdso.so
2026-05-03T00:41:35.4077455Z   AS      arch/arm64/kernel/vdso/vdso.o
2026-05-03T00:41:35.4274351Z   CC      arch/arm64/kernel/probes/uprobes.o
2026-05-03T00:41:35.4539535Z   AR      arch/arm64/kernel/vdso/built-in.a
2026-05-03T00:41:35.4632421Z   CC      init/init_task.o
2026-05-03T00:41:35.4869856Z   CC      arch/arm64/mm/init.o
2026-05-03T00:41:35.9040765Z   AR      arch/arm64/kernel/probes/built-in.a
2026-05-03T00:41:35.9139198Z   CC      arch/arm64/kernel/debug-monitors.o
2026-05-03T00:41:36.3146187Z   AS      arch/arm64/mm/cache.o
2026-05-03T00:41:36.3247632Z   CC      init/version.o
2026-05-03T00:41:36.3799319Z   CC      arch/arm64/mm/copypage.o
2026-05-03T00:41:36.4089504Z   CC      arch/arm64/crypto/sha2-ce-glue.o
2026-05-03T00:41:36.4449521Z   AS      arch/arm64/kernel/entry.o
2026-05-03T00:41:36.5199548Z   CC      arch/arm64/kernel/irq.o
2026-05-03T00:41:36.7209352Z   AR      init/built-in.a
2026-05-03T00:41:36.7359294Z   AS      arch/arm64/crypto/sha2-ce-core.o
2026-05-03T00:41:36.7839384Z   CC      arch/arm64/mm/flush.o
2026-05-03T00:41:36.9589708Z   CC      arch/arm64/crypto/ghash-ce-glue.o
2026-05-03T00:41:37.0129479Z   CC      arch/arm64/kernel/fpsimd.o
2026-05-03T00:41:37.3859392Z   CC      kernel/bpf/core.o
2026-05-03T00:41:37.4459606Z   CC      arch/arm64/mm/ioremap.o
2026-05-03T00:41:37.6380396Z   AS      arch/arm64/crypto/ghash-ce-core.o
2026-05-03T00:41:37.6895281Z   AS      arch/arm64/crypto/aes-ce-core.o
2026-05-03T00:41:37.7369445Z   CC      arch/arm64/crypto/aes-ce-glue.o
2026-05-03T00:41:37.8739855Z   AS      arch/arm64/kernel/entry-fpsimd.o
2026-05-03T00:41:37.9359416Z   CC      arch/arm64/kernel/process.o
2026-05-03T00:41:38.0499574Z   CC      arch/arm64/mm/mmap.o
2026-05-03T00:41:38.2899435Z   CC      arch/arm64/crypto/aes-glue-ce.o
2026-05-03T00:41:38.4779644Z   CC      arch/arm64/mm/pgd.o
2026-05-03T00:41:38.8849679Z   AS      arch/arm64/crypto/aes-ce.o
2026-05-03T00:41:38.9059632Z   CC      arch/arm64/mm/mmu.o
2026-05-03T00:41:38.9119154Z   CC      kernel/bpf/syscall.o
2026-05-03T00:41:38.9589629Z   CC      arch/arm64/crypto/sha256-glue.o
2026-05-03T00:41:38.9783136Z   CC      arch/arm64/kernel/ptrace.o
2026-05-03T00:41:39.8469653Z   SHIPPED arch/arm64/crypto/sha256-core.S
2026-05-03T00:41:39.8499009Z   AS      arch/arm64/crypto/aes-cipher-core.o
2026-05-03T00:41:39.8979537Z   CC      arch/arm64/crypto/aes-cipher-glue.o
2026-05-03T00:41:39.9837332Z   CC      arch/arm64/kernel/setup.o
2026-05-03T00:41:39.9877598Z   CC      arch/arm64/mm/context.o
2026-05-03T00:41:40.4099427Z   AS      arch/arm64/crypto/sha256-core.o
2026-05-03T00:41:40.4569439Z   AR      arch/arm64/crypto/built-in.a
2026-05-03T00:41:40.4689099Z   AS      arch/arm64/mm/proc.o
2026-05-03T00:41:40.5281020Z   CC      arch/arm64/mm/pageattr.o
2026-05-03T00:41:40.5449549Z   CC      certs/system_keyring.o
2026-05-03T00:41:40.5954693Z   CC      kernel/bpf/verifier.o
2026-05-03T00:41:40.7949550Z   CC      arch/arm64/kernel/signal.o
2026-05-03T00:41:40.9382556Z   EXTRACT_CERTS   
2026-05-03T00:41:40.9439209Z   AS      certs/system_certificates.o
2026-05-03T00:41:40.9829643Z   AR      certs/built-in.a
2026-05-03T00:41:41.0029378Z   CC      kernel/cgroup/cgroup.o
2026-05-03T00:41:41.1762724Z   AR      arch/arm64/mm/built-in.a
2026-05-03T00:41:41.2069308Z   CC      kernel/dma/mapping.o
2026-05-03T00:41:42.0295003Z   CC      arch/arm64/kernel/sys.o
2026-05-03T00:41:42.0339283Z   CC      kernel/dma/contiguous.o
2026-05-03T00:41:42.6002120Z   CC      arch/arm64/kernel/stacktrace.o
2026-05-03T00:41:42.6589404Z   CC      kernel/bpf/inode.o
2026-05-03T00:41:42.7129287Z   CC      kernel/dma/coherent.o
2026-05-03T00:41:43.3089500Z   CC      arch/arm64/kernel/time.o
2026-05-03T00:41:43.3834127Z   CC      kernel/cgroup/rstat.o
2026-05-03T00:41:43.4849401Z   CC      kernel/dma/removed.o
2026-05-03T00:41:43.7559418Z   CC      kernel/bpf/helpers.o
2026-05-03T00:41:43.8839414Z   CC      arch/arm64/kernel/traps.o
2026-05-03T00:41:44.0000237Z   CC      kernel/cgroup/namespace.o
2026-05-03T00:41:44.2889392Z   CC      kernel/dma/direct.o
2026-05-03T00:41:44.4799641Z   CC      kernel/bpf/tnum.o
2026-05-03T00:41:44.5565561Z   CC      arch/arm64/kernel/io.o
2026-05-03T00:41:44.6350048Z   CC      kernel/cgroup/cgroup-v1.o
2026-05-03T00:41:44.6659357Z   CC      kernel/bpf/hashtab.o
2026-05-03T00:41:44.9795567Z   CC      arch/arm64/kernel/vdso.o
2026-05-03T00:41:44.9969292Z   CC      kernel/dma/swiotlb.o
2026-05-03T00:41:45.1290060Z ../kernel/cgroup/cgroup-v1.c:908:6: warning: variable 'nr_opts' set but not used [-Wunused-but-set-variable]
2026-05-03T00:41:45.1349067Z         int nr_opts = 0;
2026-05-03T00:41:45.1358926Z             ^
2026-05-03T00:41:45.3659402Z 1 warning generated.
2026-05-03T00:41:45.5490283Z   AS      arch/arm64/kernel/hyp-stub.o
2026-05-03T00:41:45.5959631Z   CC      arch/arm64/kernel/psci.o
2026-05-03T00:41:45.6449594Z   CC      kernel/cgroup/freezer.o
2026-05-03T00:41:45.6610511Z   CC      kernel/bpf/arraymap.o
2026-05-03T00:41:45.9881183Z   CC      arch/arm64/kernel/cpu_ops.o
2026-05-03T00:41:46.0785779Z   AR      kernel/dma/built-in.a
2026-05-03T00:41:46.1054300Z   CC      kernel/cgroup/legacy_freezer.o
2026-05-03T00:41:46.1279134Z   CC      mm/filemap.o
2026-05-03T00:41:46.4979445Z   CC      arch/arm64/kernel/insn.o
2026-05-03T00:41:46.5532324Z   CC      kernel/bpf/percpu_freelist.o
2026-05-03T00:41:46.5959632Z   CC      kernel/cgroup/cpuset.o
2026-05-03T00:41:46.7479731Z   CC      kernel/bpf/bpf_lru_list.o
2026-05-03T00:41:47.0809486Z   CC      kernel/bpf/lpm_trie.o
2026-05-03T00:41:47.1569455Z   CC      arch/arm64/kernel/return_address.o
2026-05-03T00:41:47.1689909Z ../kernel/cgroup/cpuset.c:1529:17: warning: variable 'cs' set but not used [-Wunused-but-set-variable]
2026-05-03T00:41:47.1709198Z         struct cpuset *cs;
2026-05-03T00:41:47.1738957Z                        ^
2026-05-03T00:41:47.6079604Z 1 warning generated.
2026-05-03T00:41:47.8289567Z   CC      mm/mempool.o
2026-05-03T00:41:47.9339476Z   CC      arch/arm64/kernel/cpuinfo.o
2026-05-03T00:41:48.0299817Z   AR      kernel/cgroup/built-in.a
2026-05-03T00:41:48.0639612Z   CC      arch/arm64/kernel/cpu_errata.o
2026-05-03T00:41:48.3729679Z   CC      kernel/bpf/map_in_map.o
2026-05-03T00:41:48.7414446Z   CC      kernel/bpf/local_storage.o
2026-05-03T00:41:48.8979486Z   CC      arch/arm64/kernel/cpufeature.o
2026-05-03T00:41:48.9029490Z   CC      fs/configfs/inode.o
2026-05-03T00:41:49.0159415Z   CC      mm/oom_kill.o
2026-05-03T00:41:49.5439636Z   CC      fs/configfs/file.o
2026-05-03T00:41:49.7459529Z   CC      kernel/bpf/disasm.o
2026-05-03T00:41:49.8339237Z   CC      arch/arm64/kernel/alternative.o
2026-05-03T00:41:50.1879449Z   CC      fs/configfs/dir.o
2026-05-03T00:41:50.1909438Z   CC      kernel/bpf/btf.o
2026-05-03T00:41:50.2659521Z   CC      arch/arm64/kernel/cacheinfo.o
2026-05-03T00:41:50.5839587Z   CC      arch/arm64/kernel/smp.o
2026-05-03T00:41:50.7009604Z   CC      mm/fadvise.o
2026-05-03T00:41:51.2299772Z   CC      fs/configfs/symlink.o
2026-05-03T00:41:51.2769579Z   CC      kernel/bpf/devmap.o
2026-05-03T00:41:51.6339520Z   CC      fs/configfs/mount.o
2026-05-03T00:41:51.6560282Z   CC      mm/maccess.o
2026-05-03T00:41:52.1589621Z   CC      arch/arm64/kernel/smp_spin_table.o
2026-05-03T00:41:52.2284333Z   CC      fs/configfs/item.o
2026-05-03T00:41:52.2369746Z   CC      kernel/bpf/cpumap.o
2026-05-03T00:41:52.3619344Z   CC      mm/page_alloc.o
2026-05-03T00:41:52.6378686Z   CC      arch/arm64/kernel/topology.o
2026-05-03T00:41:52.6839395Z   AR      fs/configfs/built-in.a
2026-05-03T00:41:52.7079548Z   CC      fs/crypto/crypto.o
2026-05-03T00:41:53.1209476Z   CC      kernel/bpf/offload.o
2026-05-03T00:41:53.1909419Z   AS      arch/arm64/kernel/smccc-call.o
2026-05-03T00:41:53.2339640Z   CC      arch/arm64/kernel/syscall.o
2026-05-03T00:41:53.5169830Z   CC      fs/crypto/fname.o
2026-05-03T00:41:53.8239922Z   CC      arch/arm64/kernel/sys32.o
2026-05-03T00:41:54.2909366Z   CC      fs/crypto/hkdf.o
2026-05-03T00:41:54.3629718Z   CC      arch/arm64/kernel/signal32.o
2026-05-03T00:41:54.5719641Z   CC      mm/page-writeback.o
2026-05-03T00:41:54.5900915Z   CC      kernel/bpf/stackmap.o
2026-05-03T00:41:54.6934098Z   CC      fs/crypto/hooks.o
2026-05-03T00:41:55.1689681Z   CC      arch/arm64/kernel/sys_compat.o
2026-05-03T00:41:55.3969428Z   CC      fs/crypto/keyring.o
2026-05-03T00:41:55.4999629Z   CC      kernel/bpf/cgroup.o
2026-05-03T00:41:55.7039206Z   AS      arch/arm64/kernel/sigreturn32.o
2026-05-03T00:41:55.7475295Z   AS      arch/arm64/kernel/kuser32.o
2026-05-03T00:41:55.7889636Z   CC      arch/arm64/kernel/arm64ksyms.o
2026-05-03T00:41:56.1769378Z   CC      mm/readahead.o
2026-05-03T00:41:56.2159371Z   CC      fs/crypto/keysetup.o
2026-05-03T00:41:56.5879439Z   CC      arch/arm64/kernel/module.o
2026-05-03T00:41:56.8279371Z   CC      kernel/bpf/reuseport_array.o
2026-05-03T00:41:56.9219428Z   CC      fs/crypto/keysetup_v1.o
2026-05-03T00:41:57.0239716Z   CC      arch/arm64/kernel/module-plts.o
2026-05-03T00:41:57.1769359Z   CC      mm/swap.o
2026-05-03T00:41:57.3731110Z   CC      arch/arm64/kernel/perf_regs.o
2026-05-03T00:41:57.6259592Z   CC      fs/crypto/policy.o
2026-05-03T00:41:57.6276674Z   AR      kernel/bpf/built-in.a
2026-05-03T00:41:57.6570023Z   CC      kernel/events/core.o
2026-05-03T00:41:57.9169658Z   CC      arch/arm64/kernel/perf_callchain.o
2026-05-03T00:41:58.4200502Z   CC      fs/crypto/bio.o
2026-05-03T00:41:58.4450956Z   CC      arch/arm64/kernel/perf_event.o
2026-05-03T00:41:58.4532790Z   CC      mm/truncate.o
2026-05-03T00:41:59.1519627Z   CC      arch/arm64/kernel/hw_breakpoint.o
2026-05-03T00:41:59.2263835Z   CC      fs/crypto/inline_crypt.o
2026-05-03T00:41:59.4559565Z   CC      mm/vmscan.o
2026-05-03T00:41:59.8189381Z   AS      arch/arm64/kernel/sleep.o
2026-05-03T00:41:59.8669586Z   CC      arch/arm64/kernel/suspend.o
2026-05-03T00:42:00.2060063Z ../mm/vmscan.c:2855:17: warning: variable 'node_lru_pages' set but not used [-Wunused-but-set-variable]
2026-05-03T00:42:00.2099162Z                 unsigned long node_lru_pages = 0;
2026-05-03T00:42:00.2149084Z                               ^
2026-05-03T00:42:00.2179439Z ../mm/vmscan.c:3464:6: warning: variable 'nid' set but not used [-Wunused-but-set-variable]
2026-05-03T00:42:00.2209012Z         int nid;
2026-05-03T00:42:00.2209338Z             ^
2026-05-03T00:42:00.2209652Z   AR      fs/crypto/built-in.a
2026-05-03T00:42:00.2419023Z   CC      fs/devpts/inode.o
2026-05-03T00:42:00.3339163Z   CC      arch/arm64/kernel/cpuidle.o
2026-05-03T00:42:00.5699929Z   CC      kernel/events/ring_buffer.o
2026-05-03T00:42:00.7989141Z   AR      fs/devpts/built-in.a
2026-05-03T00:42:00.8171676Z   CC      fs/exfat/exfat_core.o
2026-05-03T00:42:00.8459248Z   CC      arch/arm64/kernel/armv8_deprecated.o
2026-05-03T00:42:00.9349419Z 2 warnings generated.
2026-05-03T00:42:01.3849964Z   CC      mm/shmem.o
2026-05-03T00:42:01.5349514Z   CC      kernel/events/callchain.o
2026-05-03T00:42:01.5735885Z   CC      arch/arm64/kernel/kaslr.o
2026-05-03T00:42:02.0254154Z   CC      arch/arm64/kernel/ssbd.o
2026-05-03T00:42:02.0490794Z   CC      fs/exfat/exfat_super.o
2026-05-03T00:42:02.1689420Z   CC      kernel/events/hw_breakpoint.o
2026-05-03T00:42:02.4045177Z   AS      arch/arm64/kernel/head.o
2026-05-03T00:42:02.4581796Z   LDS     arch/arm64/kernel/vmlinux.lds
2026-05-03T00:42:02.4939615Z   AR      arch/arm64/kernel/built-in.a
2026-05-03T00:42:02.5326877Z   CC      kernel/irq/irqdesc.o
2026-05-03T00:42:02.9219362Z   CC      mm/util.o
2026-05-03T00:42:02.9594819Z   CC      fs/exfat/exfat_api.o
2026-05-03T00:42:03.0669438Z   CC      kernel/events/uprobes.o
2026-05-03T00:42:03.1479410Z   CC      kernel/irq/handle.o
2026-05-03T00:42:03.7820595Z   CC      kernel/irq/manage.o
2026-05-03T00:42:03.8229704Z   CC      fs/exfat/exfat_blkdev.o
2026-05-03T00:42:03.8349314Z   CC      mm/mmzone.o
2026-05-03T00:42:04.2899402Z   AR      kernel/events/built-in.a
2026-05-03T00:42:04.3109330Z   AR      fs/exofs/built-in.a
2026-05-03T00:42:04.3449135Z   AR      ipc/built-in.a
2026-05-03T00:42:04.3529032Z   CC      kernel/irq/spurious.o
2026-05-03T00:42:04.3779405Z   CC      fs/exfat/exfat_cache.o
2026-05-03T00:42:04.4538366Z   CC      mm/vmstat.o
2026-05-03T00:42:04.6086361Z   AR      kernel/livepatch/built-in.a
2026-05-03T00:42:04.6290155Z   CC      kernel/locking/mutex.o
2026-05-03T00:42:04.7299615Z   CC      kernel/irq/resend.o
2026-05-03T00:42:05.0189778Z   CC      fs/exfat/exfat_data.o
2026-05-03T00:42:05.1289644Z   CC      kernel/irq/chip.o
2026-05-03T00:42:05.2569962Z   CC      kernel/locking/semaphore.o
2026-05-03T00:42:05.5259733Z   CC      fs/exfat/exfat_bitmap.o
2026-05-03T00:42:05.5709687Z   CC      fs/exfat/exfat_nls.o
2026-05-03T00:42:05.5916691Z   CC      mm/backing-dev.o
2026-05-03T00:42:05.9109448Z   CC      kernel/irq/dummychip.o
2026-05-03T00:42:05.9969551Z   CC      kernel/locking/rwsem.o
2026-05-03T00:42:06.1259444Z   CC      fs/exfat/exfat_oal.o
2026-05-03T00:42:06.3996682Z   CC      kernel/locking/percpu-rwsem.o
2026-05-03T00:42:06.4439591Z   CC      fs/exfat/exfat_upcase.o
2026-05-03T00:42:06.4599260Z   CC      kernel/irq/devres.o
2026-05-03T00:42:06.6149832Z   CC      mm/mm_init.o
2026-05-03T00:42:06.7799543Z   AR      fs/exfat/built-in.a
2026-05-03T00:42:06.7899249Z   CC      kernel/locking/spinlock.o
2026-05-03T00:42:06.8009423Z   CC      fs/exportfs/expfs.o
2026-05-03T00:42:07.0399192Z   CC      kernel/irq/autoprobe.o
2026-05-03T00:42:07.2566809Z   CC      kernel/locking/osq_lock.o
2026-05-03T00:42:07.3009549Z   CC      mm/mmu_context.o
2026-05-03T00:42:07.3749444Z   AR      fs/exportfs/built-in.a
2026-05-03T00:42:07.4002299Z   CC      fs/ext4/balloc.o
2026-05-03T00:42:07.5289554Z   CC      kernel/locking/qspinlock.o
2026-05-03T00:42:07.5949399Z   CC      kernel/irq/irqdomain.o
2026-05-03T00:42:07.8086380Z   CC      kernel/locking/rtmutex.o
2026-05-03T00:42:07.9689423Z   CC      mm/percpu.o
2026-05-03T00:42:08.3527105Z   CC      kernel/locking/rwsem-xadd.o
2026-05-03T00:42:08.4934273Z   CC      kernel/irq/proc.o
2026-05-03T00:42:08.4947156Z   CC      fs/ext4/bitmap.o
2026-05-03T00:42:08.8429422Z   CC      kernel/locking/qrwlock.o
2026-05-03T00:42:08.9619508Z   CC      kernel/irq/cpuhotplug.o
2026-05-03T00:42:09.1259604Z   AR      kernel/locking/built-in.a
2026-05-03T00:42:09.1357782Z   CC      fs/ext4/block_validity.o
2026-05-03T00:42:09.1808999Z   CC      security/integrity/iint.o
2026-05-03T00:42:09.3319506Z   CC      kernel/irq/pm.o
2026-05-03T00:42:09.4539921Z   CC      mm/slab_common.o
2026-05-03T00:42:09.6919633Z   CC      security/integrity/integrity_audit.o
2026-05-03T00:42:09.8069740Z   CC      fs/ext4/dir.o
2026-05-03T00:42:10.1259582Z   AR      security/integrity/built-in.a
2026-05-03T00:42:10.1449227Z   CC      security/keys/gc.o
2026-05-03T00:42:10.1889446Z   CC      kernel/irq/msi.o
2026-05-03T00:42:10.5747410Z   CC      fs/ext4/ext4_jbd2.o
2026-05-03T00:42:10.6513690Z   CC      security/keys/key.o
2026-05-03T00:42:10.7470753Z   CC      mm/compaction.o
2026-05-03T00:42:10.8369626Z   CC      kernel/irq/affinity.o
2026-05-03T00:42:11.2654930Z   AR      kernel/irq/built-in.a
2026-05-03T00:42:11.2979389Z   CC      kernel/power/qos.o
2026-05-03T00:42:11.4349642Z   CC      security/keys/keyring.o
2026-05-03T00:42:11.5323628Z   CC      fs/ext4/extents.o
2026-05-03T00:42:12.2658224Z   CC      security/keys/keyctl.o
2026-05-03T00:42:12.3079393Z   CC      kernel/power/main.o
2026-05-03T00:42:12.3203095Z   CC      mm/vmacache.o
2026-05-03T00:42:12.7564159Z   CC      mm/interval_tree.o
2026-05-03T00:42:12.9660377Z   CC      security/keys/permission.o
2026-05-03T00:42:13.1299461Z   CC      kernel/power/process.o
2026-05-03T00:42:13.3789294Z   CC      mm/list_lru.o
2026-05-03T00:42:13.4389397Z   CC      fs/ext4/extents_status.o
2026-05-03T00:42:13.6279454Z   CC      security/keys/process_keys.o
2026-05-03T00:42:13.8072019Z   CC      kernel/power/suspend.o
2026-05-03T00:42:14.2499539Z   CC      mm/workingset.o
2026-05-03T00:42:14.3852254Z   CC      security/keys/request_key.o
2026-05-03T00:42:14.4919589Z   CC      fs/ext4/file.o
2026-05-03T00:42:14.7156887Z ../mm/workingset.c:200:15: warning: variable 'nid' set but not used [-Wunused-but-set-variable]
2026-05-03T00:42:14.7179039Z         int memcgid, nid;
2026-05-03T00:42:14.7208940Z                      ^
2026-05-03T00:42:14.7979428Z 1 warning generated.
2026-05-03T00:42:14.8489483Z   CC      mm/debug.o
2026-05-03T00:42:14.8979365Z   CC      kernel/power/wakelock.o
2026-05-03T00:42:15.1379722Z   CC      security/keys/request_key_auth.o
2026-05-03T00:42:15.1899407Z   CC      fs/ext4/fsmap.o
2026-05-03T00:42:15.4290026Z   CC      kernel/power/poweroff.o
2026-05-03T00:42:15.6229503Z   CC      security/keys/user_defined.o
2026-05-03T00:42:15.6349490Z   CC      kernel/power/energy_model.o
2026-05-03T00:42:15.7620753Z   CC      mm/gup.o
2026-05-03T00:42:16.2323727Z   CC      fs/ext4/fsync.o
2026-05-03T00:42:16.2639401Z   CC      kernel/power/wakeup_reason.o
2026-05-03T00:42:16.3239383Z   CC      security/keys/compat.o
2026-05-03T00:42:16.8789456Z   CC      security/keys/proc.o
2026-05-03T00:42:16.9509395Z   CC      mm/highmem.o
2026-05-03T00:42:17.0915704Z   AR      kernel/power/built-in.a
2026-05-03T00:42:17.1119514Z   CC      fs/ext4/hash.o
2026-05-03T00:42:17.1159152Z   CC      kernel/printk/printk.o
2026-05-03T00:42:17.3539627Z   CC      security/keys/sysctl.o
2026-05-03T00:42:17.5120927Z mm/.tmp_highmem.o: no symbols
2026-05-03T00:42:17.5199944Z   CC      mm/memory.o
2026-05-03T00:42:17.7839627Z   AR      security/keys/built-in.a
2026-05-03T00:42:17.7959391Z   CC      fs/ext4/ialloc.o
2026-05-03T00:42:17.8099452Z   GEN     security/selinux/flask.h security/selinux/av_permissions.h
2026-05-03T00:42:17.8149006Z   CC      security/selinux/avc.o
2026-05-03T00:42:18.1809989Z ../mm/memory.c:4535:8: warning: variable 'p4dval' set but not used [-Wunused-but-set-variable]
2026-05-03T00:42:18.1811159Z         p4d_t p4dval;
2026-05-03T00:42:18.1839053Z               ^
2026-05-03T00:42:18.4509460Z   CC      kernel/printk/printk_safe.o
2026-05-03T00:42:18.6999445Z   AR      kernel/printk/built-in.a
2026-05-03T00:42:18.7239367Z   CC      kernel/rcu/update.o
2026-05-03T00:42:18.8269476Z   CC      security/selinux/hooks.o
2026-05-03T00:42:18.9799658Z   CC      fs/ext4/indirect.o
2026-05-03T00:42:19.0379360Z 1 warning generated.
2026-05-03T00:42:19.3782019Z   CC      mm/mincore.o
2026-05-03T00:42:19.6371745Z   CC      kernel/rcu/sync.o
2026-05-03T00:42:19.9049493Z   CC      kernel/rcu/srcutree.o
2026-05-03T00:42:19.9939570Z   CC      mm/mlock.o
2026-05-03T00:42:20.1279356Z   CC      fs/ext4/inline.o
2026-05-03T00:42:20.6074690Z   CC      kernel/rcu/tree.o
2026-05-03T00:42:20.7261549Z   CC      security/selinux/selinuxfs.o
2026-05-03T00:42:21.0506495Z   CC      mm/mmap.o
2026-05-03T00:42:21.1308036Z   CC      fs/ext4/inode.o
2026-05-03T00:42:21.2389503Z In file included from ../kernel/rcu/tree.c:4188:
2026-05-03T00:42:21.2419399Z ../kernel/rcu/tree_exp.h:653:19: warning: variable 'rdp' set but not used [-Wunused-but-set-variable]
2026-05-03T00:42:21.2449160Z         struct rcu_data *rdp;
2026-05-03T00:42:21.2478998Z                          ^
2026-05-03T00:42:21.2829272Z In file included from ../kernel/rcu/tree.c:4189:
2026-05-03T00:42:21.2839496Z ../kernel/rcu/tree_plugin.h:712:22: warning: variable 't' set but not used [-Wunused-but-set-variable]
2026-05-03T00:42:21.2869180Z         struct task_struct *t;
2026-05-03T00:42:21.2891963Z                             ^
2026-05-03T00:42:21.7499726Z ../mm/mmap.c:2370:16: warning: variable 'new_start' set but not used [-Wunused-but-set-variable]
2026-05-03T00:42:21.7528940Z         unsigned long new_start;
2026-05-03T00:42:21.7559069Z                       ^
2026-05-03T00:42:21.9529433Z   CC      security/selinux/netlink.o
2026-05-03T00:42:22.0109480Z 2 warnings generated.
2026-05-03T00:42:22.1749416Z 1 warning generated.
2026-05-03T00:42:22.4189386Z   CC      kernel/rcu/rcu_segcblist.o
2026-05-03T00:42:22.5069549Z   CC      security/selinux/nlmsgtab.o
2026-05-03T00:42:22.5369894Z   CC      mm/mprotect.o
2026-05-03T00:42:22.7587556Z   AR      kernel/rcu/built-in.a
2026-05-03T00:42:22.7909797Z   CC      kernel/sched/extension/eas_plus.o
2026-05-03T00:42:23.1839631Z   CC      fs/ext4/ioctl.o
2026-05-03T00:42:23.3239661Z   CC      security/selinux/netif.o
2026-05-03T00:42:23.3339663Z   CC      mm/mremap.o
2026-05-03T00:42:23.7154104Z ../kernel/sched/extension/eas_plus.c:364:6: warning: variable 'task_prefer' set but not used [-Wunused-but-set-variable]
2026-05-03T00:42:23.7169178Z         int task_prefer;
2026-05-03T00:42:23.7198946Z             ^
2026-05-03T00:42:23.9329413Z 1 warning generated.
2026-05-03T00:42:24.0718074Z   CC      mm/msync.o
2026-05-03T00:42:24.2818658Z   CC      security/selinux/netnode.o
2026-05-03T00:42:24.3599654Z   CC      fs/ext4/mballoc.o
2026-05-03T00:42:24.4079406Z   CC      kernel/sched/extension/debug.o
2026-05-03T00:42:24.6384019Z   CC      mm/page_vma_mapped.o
2026-05-03T00:42:25.2119417Z   CC      security/selinux/netport.o
2026-05-03T00:42:25.2589487Z   CC      mm/pagewalk.o
2026-05-03T00:42:25.2830138Z   CC      kernel/sched/extension/tuning.o
2026-05-03T00:42:25.8036927Z   CC      mm/pgtable-generic.o
2026-05-03T00:42:26.1189782Z   CC      security/selinux/ibpkey.o
2026-05-03T00:42:26.3294157Z   CC      fs/ext4/migrate.o
2026-05-03T00:42:26.3779303Z   CC      mm/rmap.o
2026-05-03T00:42:26.7381261Z   CC      kernel/sched/extension/debug_aee.o
2026-05-03T00:42:26.9449647Z   CC      fs/ext4/mmp.o
2026-05-03T00:42:26.9939698Z ../mm/rmap.c:960:17: warning: variable 'cstart' set but not used [-Wunused-but-set-variable]
2026-05-03T00:42:26.9969107Z                 unsigned long cstart;
2026-05-03T00:42:26.9969584Z                               ^
2026-05-03T00:42:27.0389666Z   CC      security/selinux/exports.o
2026-05-03T00:42:27.2048272Z 1 warning generated.
2026-05-03T00:42:27.4696459Z   CC      security/selinux/ss/ebitmap.o
2026-05-03T00:42:27.5254191Z   CC      mm/vmalloc.o
2026-05-03T00:42:27.6409603Z   CC      fs/ext4/move_extent.o
2026-05-03T00:42:27.6589416Z   AR      kernel/sched/extension/built-in.a
2026-05-03T00:42:27.6739203Z   CC      kernel/sched/core.o
2026-05-03T00:42:28.3219637Z   CC      security/selinux/ss/hashtab.o
2026-05-03T00:42:28.3639431Z   CC      fs/ext4/namei.o
2026-05-03T00:42:28.6437898Z   CC      security/selinux/ss/symtab.o
2026-05-03T00:42:28.7576156Z   CC      security/selinux/ss/sidtab.o
2026-05-03T00:42:28.9089993Z   CC      mm/process_vm_access.o
2026-05-03T00:42:29.5529473Z   CC      mm/init-mm.o
2026-05-03T00:42:29.7889912Z   CC      security/selinux/ss/avtab.o
2026-05-03T00:42:29.8309397Z   CC      mm/nobootmem.o
2026-05-03T00:42:29.8670119Z   CC      fs/ext4/page-io.o
2026-05-03T00:42:30.6244964Z   CC      security/selinux/ss/policydb.o
2026-05-03T00:42:30.6319372Z   CC      mm/madvise.o
2026-05-03T00:42:30.6409233Z   CC      fs/ext4/readpage.o
2026-05-03T00:42:30.9599625Z   CC      kernel/sched/loadavg.o
2026-05-03T00:42:31.4299481Z   CC      mm/memblock.o
2026-05-03T00:42:31.4349216Z   CC      fs/ext4/resize.o
2026-05-03T00:42:31.9311719Z   CC      security/selinux/ss/services.o
2026-05-03T00:42:32.2116300Z   CC      kernel/sched/clock.o
2026-05-03T00:42:32.3349530Z   CC      mm/page_io.o
2026-05-03T00:42:32.4531700Z   CC      fs/ext4/super.o
2026-05-03T00:42:32.8302246Z ../security/selinux/ss/services.c:2314:17: warning: variable 'sidtab' set but not used [-Wunused-but-set-variable]
2026-05-03T00:42:32.8349096Z         struct sidtab *sidtab;
2026-05-03T00:42:32.8379079Z                        ^
2026-05-03T00:42:32.8389286Z ../security/selinux/ss/services.c:2403:17: warning: variable 'sidtab' set but not used [-Wunused-but-set-variable]
2026-05-03T00:42:32.8418965Z         struct sidtab *sidtab;
2026-05-03T00:42:32.8438958Z                        ^
2026-05-03T00:42:32.8439726Z ../security/selinux/ss/services.c:2448:17: warning: variable 'sidtab' set but not used [-Wunused-but-set-variable]
2026-05-03T00:42:32.8440544Z         struct sidtab *sidtab;
2026-05-03T00:42:32.8440884Z                        ^
2026-05-03T00:42:32.8441643Z ../security/selinux/ss/services.c:2799:17: warning: variable 'sidtab' set but not used [-Wunused-but-set-variable]
2026-05-03T00:42:32.8468969Z         struct sidtab *sidtab;
2026-05-03T00:42:32.8469346Z                        ^
2026-05-03T00:42:33.0237148Z   CC      mm/swap_state.o
2026-05-03T00:42:33.2469992Z 4 warnings generated.
2026-05-03T00:42:33.2899619Z   CC      security/selinux/ss/conditional.o
2026-05-03T00:42:33.4278954Z   CC      kernel/sched/cputime.o
2026-05-03T00:42:33.7313256Z   CC      mm/swapfile.o
2026-05-03T00:42:34.2099437Z   CC      security/selinux/ss/mls.o
2026-05-03T00:42:34.7369573Z   CC      kernel/sched/idle.o
2026-05-03T00:42:35.0513172Z   CC      security/selinux/ss/status.o
2026-05-03T00:42:35.3239473Z   CC      mm/swap_slots.o
2026-05-03T00:42:35.4739686Z   CC      fs/ext4/symlink.o
2026-05-03T00:42:35.8460996Z   CC      mm/dmapool.o
2026-05-03T00:42:35.9619646Z   AR      security/selinux/built-in.a
2026-05-03T00:42:35.9739454Z   CC      security/commoncap.o
2026-05-03T00:42:36.0579406Z   CC      kernel/sched/fair.o
2026-05-03T00:42:36.0939615Z   CC      fs/ext4/sysfs.o
2026-05-03T00:42:36.5936666Z   CC      mm/sparse.o
2026-05-03T00:42:36.7658371Z   CC      security/min_addr.o
2026-05-03T00:42:36.7685442Z   CC      fs/ext4/xattr.o
2026-05-03T00:42:37.0210014Z ../kernel/sched/fair.c:6932:16: warning: variable 'target_util' set but not used [-Wunused-but-set-variable]
2026-05-03T00:42:37.0239238Z         unsigned long target_util = ULONG_MAX;
2026-05-03T00:42:37.0294809Z                       ^
2026-05-03T00:42:37.0300181Z ../kernel/sched/fair.c:7666:37: warning: comparison of distinct pointer types ('typeof (1) *' (aka 'int *') and 'typeof ((best_energy >> 4)) *' (aka 'unsigned long *')) [-Wcompare-distinct-pointer-types]
2026-05-03T00:42:37.0319107Z                                 if((best_energy - cur_energy) > max(1, (best_energy >> 4))) {
2026-05-03T00:42:37.0339031Z                                                                 ^~~~~~~~~~~~~~~~~~~~~~~~~~
2026-05-03T00:42:37.0359330Z ../include/linux/kernel.h:859:19: note: expanded from macro 'max'
2026-05-03T00:42:37.0389069Z #define max(x, y)       __careful_cmp(x, y, >)
2026-05-03T00:42:37.0399083Z                         ^~~~~~~~~~~~~~~~~~~~~~
2026-05-03T00:42:37.0419214Z ../include/linux/kernel.h:843:24: note: expanded from macro '__careful_cmp'
2026-05-03T00:42:37.0449102Z         __builtin_choose_expr(__safe_cmp(x, y), \
2026-05-03T00:42:37.0478996Z                               ^~~~~~~~~~~~~~~~
2026-05-03T00:42:37.0479609Z ../include/linux/kernel.h:833:4: note: expanded from macro '__safe_cmp'
2026-05-03T00:42:37.0480256Z                 (__typecheck(x, y) && __no_side_effects(x, y))
2026-05-03T00:42:37.0480705Z                  ^~~~~~~~~~~~~~~~~
2026-05-03T00:42:37.0481245Z ../include/linux/kernel.h:819:29: note: expanded from macro '__typecheck'
2026-05-03T00:42:37.0481887Z                 (!!(sizeof((typeof(x) *)1 == (typeof(y) *)1)))
2026-05-03T00:42:37.0482373Z                            ~~~~~~~~~~~~~~ ^  ~~~~~~~~~~~~~~
2026-05-03T00:42:37.3516428Z   CC      mm/sparse-vmemmap.o
2026-05-03T00:42:37.4039420Z   CC      security/security.o
2026-05-03T00:42:37.8761652Z   CC      mm/ksm.o
2026-05-03T00:42:37.9579629Z   CC      fs/ext4/xattr_trusted.o
2026-05-03T00:42:38.5758229Z   CC      fs/ext4/xattr_user.o
2026-05-03T00:42:38.6669409Z 2 warnings generated.
2026-05-03T00:42:38.7089589Z   CC      kernel/sched/rt.o
2026-05-03T00:42:38.9367323Z   CC      security/lsm_audit.o
2026-05-03T00:42:38.9417899Z   CC      mm/slub.o
2026-05-03T00:42:39.1189354Z   CC      fs/ext4/acl.o
2026-05-03T00:42:39.5070000Z ../kernel/sched/rt.c:1445:22: warning: variable 'curr' set but not used [-Wunused-but-set-variable]
2026-05-03T00:42:39.5129248Z         struct task_struct *curr;
2026-05-03T00:42:39.5158968Z                             ^
2026-05-03T00:42:39.8222846Z 1 warning generated.
2026-05-03T00:42:39.8300173Z   CC      fs/ext4/xattr_security.o
2026-05-03T00:42:39.8639644Z   CC      kernel/sched/deadline.o
2026-05-03T00:42:39.9069323Z   AR      security/built-in.a
2026-05-03T00:42:39.9309113Z   CC      fs/f2fs/dir.o
2026-05-03T00:42:40.4549521Z   CC      fs/ext4/verity.o
2026-05-03T00:42:40.6739526Z   CC      mm/migrate.o
2026-05-03T00:42:40.9826531Z   CC      kernel/sched/wait.o
2026-05-03T00:42:41.0019456Z   CC      fs/f2fs/file.o
2026-05-03T00:42:41.1649662Z   AR      fs/ext4/built-in.a
2026-05-03T00:42:41.1889327Z   CC      fs/fat/cache.o
2026-05-03T00:42:41.7367066Z   CC      fs/fat/dir.o
2026-05-03T00:42:42.0123152Z   CC      mm/page_counter.o
2026-05-03T00:42:42.2757000Z   CC      kernel/sched/wait_bit.o
2026-05-03T00:42:42.3019436Z   CC      mm/memcontrol.o
2026-05-03T00:42:42.7414931Z   CC      fs/fat/fatent.o
2026-05-03T00:42:42.8562428Z   CC      fs/f2fs/inode.o
2026-05-03T00:42:43.4659456Z   CC      kernel/sched/swait.o
2026-05-03T00:42:43.6538652Z   CC      fs/fat/file.o
2026-05-03T00:42:43.9617333Z   CC      fs/f2fs/namei.o
2026-05-03T00:42:44.6609529Z   CC      fs/fat/inode.o
2026-05-03T00:42:44.7049523Z   CC      kernel/sched/completion.o
2026-05-03T00:42:44.7539665Z   CC      mm/vmpressure.o
2026-05-03T00:42:45.0199419Z   CC      fs/f2fs/hash.o
2026-05-03T00:42:45.2989470Z   CC      mm/swap_cgroup.o
2026-05-03T00:42:45.6529518Z   CC      fs/f2fs/super.o
2026-05-03T00:42:45.7899747Z   CC      fs/fat/misc.o
2026-05-03T00:42:45.8474420Z   CC      mm/page_isolation.o
2026-05-03T00:42:45.9649662Z   CC      kernel/sched/stubs.o
2026-05-03T00:42:46.4949477Z   CC      fs/fat/nfs.o
2026-05-03T00:42:46.5259366Z   CC      mm/zsmalloc.o
2026-05-03T00:42:47.0089377Z   CC      fs/fat/namei_vfat.o
2026-05-03T00:42:47.1119395Z   CC      kernel/sched/cpupri.o
2026-05-03T00:42:47.6783414Z   CC      mm/early_ioremap.o
2026-05-03T00:42:47.6889492Z   CC      fs/fat/namei_msdos.o
2026-05-03T00:42:47.7159776Z   CC      fs/f2fs/inline.o
2026-05-03T00:42:48.0029439Z   CC      kernel/sched/cpudeadline.o
2026-05-03T00:42:48.1400829Z   CC      mm/cma.o
2026-05-03T00:42:48.2659432Z   AR      fs/fat/built-in.a
2026-05-03T00:42:48.3769485Z   CC      crypto/asymmetric_keys/asymmetric_type.o
2026-05-03T00:42:48.6529058Z   CC      fs/f2fs/checkpoint.o
2026-05-03T00:42:48.8978690Z   CC      kernel/sched/topology.o
2026-05-03T00:42:49.0279415Z   CC      crypto/asymmetric_keys/restrict.o
2026-05-03T00:42:49.1449412Z   CC      mm/frame_vector.o
2026-05-03T00:42:49.3528820Z   CC      crypto/asymmetric_keys/signature.o
2026-05-03T00:42:49.8781633Z   CC      mm/usercopy.o
2026-05-03T00:42:49.8819033Z   CC      crypto/asymmetric_keys/public_key.o
2026-05-03T00:42:49.9069413Z   CC      fs/f2fs/gc.o
2026-05-03T00:42:50.0299602Z   CC      kernel/sched/stop_task.o
2026-05-03T00:42:50.5689600Z   CC      mm/memfd.o
2026-05-03T00:42:50.6259754Z   ASN.1   crypto/asymmetric_keys/x509.asn1.c
2026-05-03T00:42:50.6297690Z   ASN.1   crypto/asymmetric_keys/x509_akid.asn1.c
2026-05-03T00:42:50.6319294Z   CC      crypto/asymmetric_keys/x509_public_key.o
2026-05-03T00:42:50.8431875Z   CC      kernel/sched/pelt.o
2026-05-03T00:42:51.0889686Z   ASN.1   crypto/asymmetric_keys/pkcs7.asn1.c
2026-05-03T00:42:51.0919252Z   CC      crypto/asymmetric_keys/pkcs7_trust.o
2026-05-03T00:42:51.2529583Z   AR      mm/built-in.a
2026-05-03T00:42:51.3120817Z   CC      crypto/asymmetric_keys/pkcs7_verify.o
2026-05-03T00:42:51.3529520Z   CC      fs/f2fs/data.o
2026-05-03T00:42:51.4939568Z   CC      kernel/time/time.o
2026-05-03T00:42:51.8859378Z   CC      kernel/sched/stats.o
2026-05-03T00:42:51.8889303Z   CC      crypto/asymmetric_keys/x509.asn1.o
2026-05-03T00:42:51.9309529Z   CC      crypto/asymmetric_keys/x509_akid.asn1.o
2026-05-03T00:42:51.9729481Z   CC      crypto/asymmetric_keys/x509_cert_parser.o
2026-05-03T00:42:52.3889529Z   CC      crypto/asymmetric_keys/pkcs7.asn1.o
2026-05-03T00:42:52.4309421Z   CC      crypto/asymmetric_keys/pkcs7_parser.o
2026-05-03T00:42:52.4779384Z   CC      kernel/time/timer.o
2026-05-03T00:42:52.7351107Z   CC      kernel/sched/debug.o
2026-05-03T00:42:52.9090138Z   AR      crypto/asymmetric_keys/built-in.a
2026-05-03T00:42:52.9268869Z   CC      crypto/api.o
2026-05-03T00:42:53.2675165Z   CC      fs/f2fs/node.o
2026-05-03T00:42:53.8589651Z   CC      kernel/sched/tune.o
2026-05-03T00:42:53.8809380Z   CC      crypto/cipher.o
2026-05-03T00:42:53.9039408Z   CC      kernel/time/hrtimer.o
2026-05-03T00:42:54.5139672Z   CC      crypto/compress.o
2026-05-03T00:42:54.9372926Z   CC      fs/f2fs/segment.o
2026-05-03T00:42:55.0272301Z   CC      kernel/time/timekeeping.o
2026-05-03T00:42:55.0836785Z   CC      crypto/memneq.o
2026-05-03T00:42:55.4379437Z   CC      kernel/sched/cpuacct.o
2026-05-03T00:42:55.8819439Z   CC      crypto/crypto_wq.o
2026-05-03T00:42:56.0044705Z   CC      kernel/time/ntp.o
2026-05-03T00:42:56.2470069Z   CC      kernel/sched/cpufreq.o
2026-05-03T00:42:56.5484679Z   CC      kernel/time/clocksource.o
2026-05-03T00:42:56.6649697Z   CC      crypto/algapi.o
2026-05-03T00:42:56.9339874Z   CC      fs/f2fs/recovery.o
2026-05-03T00:42:57.1469642Z   CC      kernel/time/jiffies.o
2026-05-03T00:42:57.4893785Z   CC      kernel/sched/cpufreq_schedutil.o
2026-05-03T00:42:57.6399476Z   CC      kernel/time/timer_list.o
2026-05-03T00:42:57.8389649Z   CC      crypto/scatterwalk.o
2026-05-03T00:42:57.8769593Z   CC      fs/f2fs/shrinker.o
2026-05-03T00:42:58.1119459Z   CC      kernel/time/timeconv.o
2026-05-03T00:42:58.4999467Z   CC      fs/f2fs/extent_cache.o
2026-05-03T00:42:58.5719580Z   CC      kernel/time/timecounter.o
2026-05-03T00:42:58.6469621Z   CC      kernel/time/alarmtimer.o
2026-05-03T00:42:58.6954268Z   CC      crypto/proc.o
2026-05-03T00:42:59.1669438Z   CC      kernel/sched/membarrier.o
2026-05-03T00:42:59.2149563Z   CC      crypto/aead.o
2026-05-03T00:42:59.4759698Z   CC      fs/f2fs/sysfs.o
2026-05-03T00:42:59.6706128Z   CC      kernel/time/posix-timers.o
2026-05-03T00:43:00.0439555Z   CC      kernel/sched/isolation.o
2026-05-03T00:43:00.3049511Z   CC      crypto/ablkcipher.o
2026-05-03T00:43:00.3779450Z   CC      kernel/time/posix-cpu-timers.o
2026-05-03T00:43:00.4516361Z   CC      fs/f2fs/debug.o
2026-05-03T00:43:01.0509573Z   CC      kernel/time/posix-clock.o
2026-05-03T00:43:01.2079544Z   CC      fs/f2fs/xattr.o
2026-05-03T00:43:01.3078017Z   CC      crypto/blkcipher.o
2026-05-03T00:43:01.3109492Z   CC      kernel/sched/psi.o
2026-05-03T00:43:01.8589111Z   CC      kernel/time/itimer.o
2026-05-03T00:43:02.1048770Z   CC      fs/f2fs/acl.o
2026-05-03T00:43:02.3029603Z   CC      crypto/skcipher.o
2026-05-03T00:43:02.3499422Z   AR      kernel/sched/built-in.a
2026-05-03T00:43:02.3899345Z   CC      fs/fuse/dev.o
2026-05-03T00:43:02.4642038Z   CC      kernel/time/clockevents.o
2026-05-03T00:43:02.8084420Z   CC      fs/f2fs/verity.o
2026-05-03T00:43:03.0519589Z   CC      kernel/time/tick-common.o
2026-05-03T00:43:03.4966445Z   AR      fs/f2fs/built-in.a
2026-05-03T00:43:03.5099260Z   CC      kernel/time/tick-broadcast.o
2026-05-03T00:43:03.5659534Z   CC      crypto/seqiv.o
2026-05-03T00:43:03.7476392Z   CC      fs/fuse/dir.o
2026-05-03T00:43:04.1250513Z   CC      kernel/time/tick-broadcast-hrtimer.o
2026-05-03T00:43:04.1419411Z   CC      block/partitions/check.o
2026-05-03T00:43:04.1499242Z   CC      crypto/echainiv.o
2026-05-03T00:43:04.5009318Z   CC      kernel/time/sched_clock.o
2026-05-03T00:43:04.5869653Z   CC      fs/fuse/file.o
2026-05-03T00:43:04.7361805Z   CC      block/partitions/msdos.o
2026-05-03T00:43:04.7655582Z   CC      crypto/ahash.o
2026-05-03T00:43:04.8449624Z   CC      kernel/time/tick-oneshot.o
2026-05-03T00:43:05.2169654Z   CC      kernel/time/tick-sched.o
2026-05-03T00:43:05.3789451Z   CC      block/partitions/efi.o
2026-05-03T00:43:05.8129401Z   CC      crypto/shash.o
2026-05-03T00:43:06.0123461Z   AR      block/partitions/built-in.a
2026-05-03T00:43:06.0228855Z   CC      block/bio.o
2026-05-03T00:43:06.0549549Z   CC      fs/fuse/inode.o
2026-05-03T00:43:06.1639462Z   CC      kernel/time/vsyscall.o
2026-05-03T00:43:06.5139291Z   CC      kernel/time/timer_list_aee.o
2026-05-03T00:43:06.8389511Z   CC      crypto/akcipher.o
2026-05-03T00:43:07.0296135Z   AR      kernel/time/built-in.a
2026-05-03T00:43:07.0515347Z   CC      fs/fuse/control.o
2026-05-03T00:43:07.0722034Z   CC      kernel/trace/trace_clock.o
2026-05-03T00:43:07.4029608Z   CC      block/elevator.o
2026-05-03T00:43:07.5477963Z   CC      kernel/trace/ring_buffer.o
2026-05-03T00:43:07.6634545Z   CC      fs/fuse/xattr.o
2026-05-03T00:43:07.6769594Z   CC      crypto/kpp.o
2026-05-03T00:43:08.2860101Z   CC      fs/fuse/acl.o
2026-05-03T00:43:08.5499594Z   ASN.1   crypto/rsapubkey.asn1.c
2026-05-03T00:43:08.5529437Z   ASN.1   crypto/rsaprivkey.asn1.c
2026-05-03T00:43:08.5589239Z   CC      crypto/rsa.o
2026-05-03T00:43:08.5879478Z   CC      block/blk-core.o
2026-05-03T00:43:08.8489668Z   CC      fs/fuse/passthrough.o
2026-05-03T00:43:08.9164127Z   CC      kernel/trace/trace.o
2026-05-03T00:43:09.1419654Z   CC      crypto/rsa_helper.o
2026-05-03T00:43:09.3369421Z   CC      crypto/rsa-pkcs1pad.o
2026-05-03T00:43:09.4939651Z   AR      fs/fuse/built-in.a
2026-05-03T00:43:09.5199735Z   CC      fs/incfs/data_mgmt.o
2026-05-03T00:43:10.0092813Z ../fs/incfs/data_mgmt.c:1065:21: warning: variable 'mi' set but not used [-Wunused-but-set-variable]
2026-05-03T00:43:10.0109039Z         struct mount_info *mi = NULL;
2026-05-03T00:43:10.0109468Z                            ^
2026-05-03T00:43:10.0266895Z   CC      crypto/acompress.o
2026-05-03T00:43:10.2269610Z 1 warning generated.
2026-05-03T00:43:10.2589462Z   CC      fs/incfs/format.o
2026-05-03T00:43:10.6189583Z   CC      block/blk-tag.o
2026-05-03T00:43:10.7389595Z   CC      fs/incfs/integrity.o
2026-05-03T00:43:10.8649678Z   CC      kernel/trace/trace_output.o
2026-05-03T00:43:10.9169752Z   CC      crypto/scompress.o
2026-05-03T00:43:11.0630004Z   CC      fs/incfs/main.o
2026-05-03T00:43:11.4131298Z   CC      fs/incfs/vfs.o
2026-05-03T00:43:11.4749433Z   CC      block/blk-sysfs.o
2026-05-03T00:43:11.8444575Z   CC      crypto/algboss.o
2026-05-03T00:43:11.9209422Z   CC      kernel/trace/trace_seq.o
2026-05-03T00:43:12.3890020Z   AR      fs/incfs/built-in.a
2026-05-03T00:43:12.4069308Z   CC      fs/isofs/namei.o
2026-05-03T00:43:12.4761901Z   CC      kernel/trace/trace_stat.o
2026-05-03T00:43:12.4808259Z   CC      block/blk-flush.o
2026-05-03T00:43:12.5479580Z   CC      crypto/testmgr.o
2026-05-03T00:43:12.9049605Z   CC      fs/isofs/inode.o
2026-05-03T00:43:13.1123406Z   CC      kernel/trace/trace_printk.o
2026-05-03T00:43:13.3794178Z   CC      block/blk-settings.o
2026-05-03T00:43:13.4389371Z   CC      crypto/crypto_user.o
2026-05-03T00:43:13.5979612Z   CC      fs/isofs/dir.o
2026-05-03T00:43:13.9799681Z   CC      kernel/trace/trace_sched_switch.o
2026-05-03T00:43:14.0719492Z   CC      crypto/cmac.o
2026-05-03T00:43:14.1109575Z   CC      fs/isofs/util.o
2026-05-03T00:43:14.3109727Z   CC      block/blk-ioc.o
2026-05-03T00:43:14.5286778Z   CC      fs/isofs/rock.o
2026-05-03T00:43:14.6979631Z   CC      crypto/hmac.o
2026-05-03T00:43:14.7069463Z   CC      kernel/trace/trace_nop.o
2026-05-03T00:43:15.1079696Z   CC      fs/isofs/export.o
2026-05-03T00:43:15.2067026Z   CC      block/blk-map.o
2026-05-03T00:43:15.3169439Z   CC      kernel/trace/blktrace.o
2026-05-03T00:43:15.3289327Z   CC      crypto/xcbc.o
2026-05-03T00:43:15.5857923Z   CC      fs/isofs/joliet.o
2026-05-03T00:43:15.9263761Z   CC      crypto/crypto_null.o
2026-05-03T00:43:16.0479543Z   CC      block/blk-exec.o
2026-05-03T00:43:16.0749521Z   CC      fs/isofs/compress.o
2026-05-03T00:43:16.3519358Z   CC      kernel/trace/trace_events.o
2026-05-03T00:43:16.7249664Z   AR      fs/isofs/built-in.a
2026-05-03T00:43:16.7494062Z   CC      crypto/md5.o
2026-05-03T00:43:16.7519364Z   CC      fs/jbd2/transaction.o
2026-05-03T00:43:16.8329626Z   CC      block/blk-merge.o
2026-05-03T00:43:17.6179427Z   CC      crypto/sha1_generic.o
2026-05-03T00:43:17.7256494Z   CC      kernel/trace/trace_export.o
2026-05-03T00:43:17.9849594Z   CC      block/blk-softirq.o
2026-05-03T00:43:18.0212976Z   CC      fs/jbd2/commit.o
2026-05-03T00:43:18.2984076Z   CC      kernel/trace/trace_event_perf.o
2026-05-03T00:43:18.3809383Z   CC      crypto/sha256_generic.o
2026-05-03T00:43:18.7617419Z   CC      block/blk-timeout.o
2026-05-03T00:43:18.9079626Z   CC      fs/jbd2/recovery.o
2026-05-03T00:43:19.2369395Z   CC      kernel/trace/trace_events_filter.o
2026-05-03T00:43:19.3939490Z   CC      crypto/sha512_generic.o
2026-05-03T00:43:19.5332411Z   CC      fs/jbd2/checkpoint.o
2026-05-03T00:43:19.5633900Z   CC      block/blk-lib.o
2026-05-03T00:43:20.2309653Z   CC      fs/jbd2/revoke.o
2026-05-03T00:43:20.2759512Z   CC      crypto/gf128mul.o
2026-05-03T00:43:20.3952948Z   CC      kernel/trace/trace_events_trigger.o
2026-05-03T00:43:20.4429572Z   CC      block/blk-mq.o
2026-05-03T00:43:20.6765462Z ../fs/jbd2/revoke.c:532:17: warning: variable 'count' set but not used [-Wunused-but-set-variable]
2026-05-03T00:43:20.6819411Z         int i, offset, count;
2026-05-03T00:43:20.6848944Z                        ^
2026-05-03T00:43:20.8049519Z 1 warning generated.
2026-05-03T00:43:20.8339490Z   CC      fs/jbd2/journal.o
2026-05-03T00:43:20.9079514Z   CC      crypto/ecb.o
2026-05-03T00:43:21.3719759Z   CC      kernel/trace/bpf_trace.o
2026-05-03T00:43:21.4219462Z   CC      crypto/cbc.o
2026-05-03T00:43:22.0645607Z   CC      crypto/cts.o
2026-05-03T00:43:22.1369556Z   CC      block/blk-mq-tag.o
2026-05-03T00:43:22.5109390Z   AR      fs/jbd2/built-in.a
2026-05-03T00:43:22.5319280Z   CC      fs/kernfs/mount.o
2026-05-03T00:43:22.6609661Z   CC      crypto/xts.o
2026-05-03T00:43:22.7799715Z   CC      kernel/trace/trace_kprobe.o
2026-05-03T00:43:22.9919382Z   CC      block/blk-stat.o
2026-05-03T00:43:23.0199606Z   CC      fs/kernfs/inode.o
2026-05-03T00:43:23.3639449Z   CC      crypto/ctr.o
2026-05-03T00:43:23.6482294Z   CC      kernel/trace/power-traces.o
2026-05-03T00:43:23.6499658Z   CC      fs/kernfs/dir.o
2026-05-03T00:43:23.8699667Z   CC      block/blk-mq-sysfs.o
2026-05-03T00:43:23.9489453Z   CC      crypto/gcm.o
2026-05-03T00:43:24.4709519Z   CC      fs/kernfs/file.o
2026-05-03T00:43:24.7210034Z   CC      crypto/ccm.o
2026-05-03T00:43:24.7929400Z   CC      block/blk-mq-cpumap.o
2026-05-03T00:43:24.8469408Z   CC      kernel/trace/rpm-traces.o
2026-05-03T00:43:25.2619019Z   CC      fs/kernfs/symlink.o
2026-05-03T00:43:25.4459723Z   CC      crypto/chacha20poly1305.o
2026-05-03T00:43:25.6289492Z   CC      block/blk-mq-sched.o
2026-05-03T00:43:25.6730028Z   CC      kernel/trace/trace_probe.o
2026-05-03T00:43:25.8059425Z   AR      fs/kernfs/built-in.a
2026-05-03T00:43:25.8299463Z   CC      fs/nls/nls_base.o
2026-05-03T00:43:26.1629455Z   CC      crypto/cryptd.o
2026-05-03T00:43:26.3129546Z   CC      fs/nls/nls_cp437.o
2026-05-03T00:43:26.4119667Z   CC      kernel/trace/trace_uprobe.o
2026-05-03T00:43:26.5780690Z   CC      fs/nls/nls_cp950.o
2026-05-03T00:43:26.5979401Z   CC      block/ioctl.o
2026-05-03T00:43:27.0329639Z   CC      fs/nls/nls_ascii.o
2026-05-03T00:43:27.1859444Z   CC      crypto/des_generic.o
2026-05-03T00:43:27.2918926Z   CC      fs/nls/nls_iso8859-1.o
2026-05-03T00:43:27.2993198Z   CC      kernel/trace/mtk_trace.o
2026-05-03T00:43:27.5915483Z   CC      fs/nls/nls_utf8.o
2026-05-03T00:43:27.6099531Z   CC      block/genhd.o
2026-05-03T00:43:27.8389571Z   CC [M]  kernel/trace/trace_mmstat.o
2026-05-03T00:43:27.8682728Z   AR      fs/nls/built-in.a
2026-05-03T00:43:27.8869892Z   CC      crypto/blowfish_generic.o
2026-05-03T00:43:27.8949739Z   CC      fs/notify/dnotify/dnotify.o
2026-05-03T00:43:28.3300355Z   AR      fs/notify/dnotify/built-in.a
2026-05-03T00:43:28.3479385Z   AR      fs/notify/fanotify/built-in.a
2026-05-03T00:43:28.3661847Z   CC      fs/notify/inotify/inotify_fsnotify.o
2026-05-03T00:43:28.3919901Z   CC      crypto/blowfish_common.o
2026-05-03T00:43:28.5689191Z   AR      kernel/trace/built-in.a
2026-05-03T00:43:28.5949308Z   CHK     kernel/kheaders_data.tar.xz
2026-05-03T00:43:28.7339641Z   CC      block/partition-generic.o
2026-05-03T00:43:28.7549579Z   CC      fs/notify/inotify/inotify_user.o
2026-05-03T00:43:28.7550674Z   GEN     kernel/kheaders_data.tar.xz
2026-05-03T00:43:29.0339415Z   CC      crypto/twofish_generic.o
2026-05-03T00:43:29.3899485Z   AR      fs/notify/inotify/built-in.a
2026-05-03T00:43:29.3987403Z   CC      fs/notify/fsnotify.o
2026-05-03T00:43:29.4559471Z   CC      crypto/twofish_common.o
2026-05-03T00:43:29.5990039Z   CC      block/ioprio.o
2026-05-03T00:43:30.3439544Z   CC      crypto/aes_generic.o
2026-05-03T00:43:30.4179984Z   CC      fs/notify/notification.o
2026-05-03T00:43:30.7430726Z   CC      block/badblocks.o
2026-05-03T00:43:31.1650112Z   CC      crypto/arc4.o
2026-05-03T00:43:31.3469602Z   CC      fs/notify/group.o
2026-05-03T00:43:31.5351114Z   CC      block/blk-rq-qos.o
2026-05-03T00:43:31.9683228Z   CC      crypto/chacha_generic.o
2026-05-03T00:43:32.0327651Z   CC      fs/notify/mark.o
2026-05-03T00:43:32.3039662Z   CC      block/scsi_ioctl.o
2026-05-03T00:43:32.7790367Z   CC      fs/notify/fdinfo.o
2026-05-03T00:43:32.8079625Z   CC      crypto/poly1305_generic.o
2026-05-03T00:43:33.4483988Z   CC      crypto/deflate.o
2026-05-03T00:43:33.4839619Z   AR      fs/notify/built-in.a
2026-05-03T00:43:33.5285249Z   CC      fs/ntfs/aops.o
2026-05-03T00:43:33.6163746Z   CC      block/noop-iosched.o
2026-05-03T00:43:34.1119568Z   CC      crypto/crc32c_generic.o
2026-05-03T00:43:34.2458280Z   CC      block/deadline-iosched.o
2026-05-03T00:43:34.5589497Z   CC      fs/ntfs/attrib.o
2026-05-03T00:43:34.8846110Z   CC      crypto/crc32_generic.o
2026-05-03T00:43:35.0214217Z   CC      block/cfq-iosched.o
2026-05-03T00:43:35.6480012Z   CC      crypto/authenc.o
2026-05-03T00:43:35.6669853Z   CC      fs/ntfs/collate.o
2026-05-03T00:43:36.3269465Z   CC      fs/ntfs/compress.o
2026-05-03T00:43:36.3869349Z   CC      block/mq-deadline.o
2026-05-03T00:43:36.9899389Z   CC      crypto/authencesn.o
2026-05-03T00:43:37.2129557Z   CC      fs/ntfs/debug.o
2026-05-03T00:43:37.4679580Z   CC      block/kyber-iosched.o
2026-05-03T00:43:37.7129477Z   CC      fs/ntfs/dir.o
2026-05-03T00:43:37.9149587Z   CC      crypto/lzo.o
2026-05-03T00:43:38.4289458Z   CC      block/bfq-iosched.o
2026-05-03T00:43:38.4379296Z   CC      fs/ntfs/file.o
2026-05-03T00:43:38.6269747Z   CC      crypto/lz4.o
2026-05-03T00:43:39.0969349Z   CC      crypto/rng.o
2026-05-03T00:43:39.1849721Z ../fs/ntfs/file.c:340:14: warning: variable 'base_ni' set but not used [-Wunused-but-set-variable]
2026-05-03T00:43:39.1879253Z         ntfs_inode *base_ni, *ni = NTFS_I(vi);
2026-05-03T00:43:39.1908962Z                     ^
2026-05-03T00:43:39.8019376Z 1 warning generated.
2026-05-03T00:43:39.8444756Z   CC      fs/ntfs/index.o
2026-05-03T00:43:39.8695581Z   CC      block/bfq-wf2q.o
2026-05-03T00:43:40.2769926Z   CC      crypto/drbg.o
2026-05-03T00:43:40.6459421Z   CC      fs/ntfs/inode.o
2026-05-03T00:43:40.8390780Z   CC      block/bfq-cgroup.o
2026-05-03T00:43:41.1669596Z   CC      crypto/jitterentropy.o
2026-05-03T00:43:41.2173526Z ../crypto/jitterentropy.c:668:6: warning: variable 'count_var' set but not used [-Wunused-but-set-variable]
2026-05-03T00:43:41.2219517Z         int count_var = 0;
2026-05-03T00:43:41.2259330Z             ^
2026-05-03T00:43:41.2259995Z 1 warning generated.
2026-05-03T00:43:41.2759430Z   CC      crypto/jitterentropy-kcapi.o
2026-05-03T00:43:41.3589757Z ../fs/ntfs/inode.c:2378:6: warning: variable 'attr_len' set but not used [-Wunused-but-set-variable]
2026-05-03T00:43:41.3649142Z         u32 attr_len;
2026-05-03T00:43:41.3708948Z             ^
2026-05-03T00:43:41.6259466Z 1 warning generated.
2026-05-03T00:43:41.6789637Z   CC      fs/ntfs/mft.o
2026-05-03T00:43:41.8054404Z   CC      block/compat_ioctl.o
2026-05-03T00:43:42.0669581Z   CC      crypto/ghash-generic.o
2026-05-03T00:43:42.5599656Z   CC      fs/ntfs/mst.o
2026-05-03T00:43:42.6489596Z   CC      crypto/hash_info.o
2026-05-03T00:43:42.6729915Z   CC      block/blk-mq-virtio.o
2026-05-03T00:43:42.7089416Z   CC      crypto/simd.o
2026-05-03T00:43:42.9423969Z   CC      fs/ntfs/namei.o
2026-05-03T00:43:43.3528091Z   CC      fs/ntfs/runlist.o
2026-05-03T00:43:43.5089529Z   CC      block/keyslot-manager.o
2026-05-03T00:43:43.5749444Z   CC      crypto/rsapubkey.asn1.o
2026-05-03T00:43:43.6149417Z   CC      crypto/rsaprivkey.asn1.o
2026-05-03T00:43:43.6569439Z   AR      crypto/built-in.a
2026-05-03T00:43:43.7309421Z   CC      fs/ntfs/super.o
2026-05-03T00:43:43.9525203Z   CC      fs/overlayfs/super.o
2026-05-03T00:43:44.4294901Z   CC      block/bio-crypt-ctx.o
2026-05-03T00:43:44.5172730Z   CC      fs/overlayfs/namei.o
2026-05-03T00:43:44.6249277Z   CC      fs/ntfs/sysctl.o
2026-05-03T00:43:44.9069377Z   CC      fs/ntfs/unistr.o
2026-05-03T00:43:45.0729664Z   CC      fs/overlayfs/util.o
2026-05-03T00:43:45.2479399Z   CC      block/blk-crypto.o
2026-05-03T00:43:45.3429957Z   CC      fs/ntfs/upcase.o
2026-05-03T00:43:45.5699415Z   CC      fs/overlayfs/inode.o
2026-05-03T00:43:45.7349470Z   CC      fs/ntfs/bitmap.o
2026-05-03T00:43:46.0299355Z   CC      fs/overlayfs/file.o
2026-05-03T00:43:46.0519946Z   CC      block/blk-crypto-fallback.o
2026-05-03T00:43:46.2599564Z   CC      fs/ntfs/lcnalloc.o
2026-05-03T00:43:46.5110066Z   CC      fs/overlayfs/dir.o
2026-05-03T00:43:46.6899456Z   AR      block/built-in.a
2026-05-03T00:43:46.7569577Z   CC      wt_sys/trigger_panic.o
2026-05-03T00:43:46.8609630Z   CC      fs/ntfs/logfile.o
2026-05-03T00:43:47.0789679Z   AR      wt_sys/built-in.a
2026-05-03T00:43:47.1379584Z   CC      fs/overlayfs/readdir.o
2026-05-03T00:43:47.1969373Z   CC      fs/proc/task_mmu.o
2026-05-03T00:43:47.2859165Z ../fs/ntfs/logfile.c:495:21: warning: variable 'log_page_mask' set but not used [-Wunused-but-set-variable]
2026-05-03T00:43:47.2919422Z         int log_page_size, log_page_mask, err;
2026-05-03T00:43:47.2948972Z                            ^
2026-05-03T00:43:47.4079387Z 1 warning generated.
2026-05-03T00:43:47.4379505Z   CC      fs/ntfs/quota.o
2026-05-03T00:43:47.7817567Z   CC      fs/overlayfs/copy_up.o
2026-05-03T00:43:47.8339670Z   CC      fs/ntfs/usnjrnl.o
2026-05-03T00:43:48.0619593Z   CC      fs/proc/inode.o
2026-05-03T00:43:48.2186756Z   AR      fs/ntfs/built-in.a
2026-05-03T00:43:48.2409496Z   CC      fs/pstore/inode.o
2026-05-03T00:43:48.4420338Z   CC      fs/overlayfs/export.o
2026-05-03T00:43:48.5875314Z   CC      fs/proc/root.o
2026-05-03T00:43:48.6819624Z   CC      fs/pstore/platform.o
2026-05-03T00:43:48.9089609Z   AR      fs/overlayfs/built-in.a
2026-05-03T00:43:48.9200046Z   CC      kernel/fork.o
2026-05-03T00:43:49.0459418Z   CC      fs/proc/base.o
2026-05-03T00:43:49.2049375Z   CC      fs/pstore/pmsg.o
2026-05-03T00:43:49.6081267Z   CC      fs/pstore/ram.o
2026-05-03T00:43:50.0569477Z   CC      fs/proc/generic.o
2026-05-03T00:43:50.0747757Z   CC      fs/pstore/ram_core.o
2026-05-03T00:43:50.5809622Z   AR      fs/pstore/built-in.a
2026-05-03T00:43:50.5965708Z   CC      fs/proc/array.o
2026-05-03T00:43:50.6268996Z   CC      drivers/amba/bus.o
2026-05-03T00:43:50.8149433Z   AR      sound/arm/built-in.a
2026-05-03T00:43:50.8299472Z   AR      sound/atmel/built-in.a
2026-05-03T00:43:50.8549725Z   CC      sound/core/seq/seq.o
2026-05-03T00:43:51.1929661Z   CC      sound/core/seq/seq_lock.o
2026-05-03T00:43:51.2919445Z   AR      drivers/amba/built-in.a
2026-05-03T00:43:51.3109654Z   CC      drivers/android/binderfs.o
2026-05-03T00:43:51.3229525Z   CC      fs/proc/fd.o
2026-05-03T00:43:51.5649395Z   CC      sound/core/seq/seq_clientmgr.o
2026-05-03T00:43:51.8432120Z   CC      fs/proc/proc_tty.o
2026-05-03T00:43:51.8979632Z   CC      drivers/android/binder.o
2026-05-03T00:43:52.2749436Z   CC      fs/proc/cmdline.o
2026-05-03T00:43:52.3332178Z   CC      sound/core/seq/seq_memory.o
2026-05-03T00:43:52.6442821Z   CC      fs/proc/consoles.o
2026-05-03T00:43:52.9503421Z   CC      sound/core/seq/seq_queue.o
2026-05-03T00:43:52.9949560Z   CC      fs/proc/cpuinfo.o
2026-05-03T00:43:53.2899584Z   CC      fs/proc/devices.o
2026-05-03T00:43:53.4849593Z   CC      sound/core/seq/seq_fifo.o
2026-05-03T00:43:53.5709412Z   CC      fs/proc/interrupts.o
2026-05-03T00:43:53.8289840Z   CC      drivers/android/binder_alloc.o
2026-05-03T00:43:53.8709172Z   CC      fs/proc/loadavg.o
2026-05-03T00:43:53.9030036Z   CC      sound/core/seq/seq_prioq.o
2026-05-03T00:43:54.2149679Z   CC      fs/proc/meminfo.o
2026-05-03T00:43:54.3688878Z   CC      sound/core/seq/seq_timer.o
2026-05-03T00:43:54.6379225Z   CC      fs/proc/stat.o
2026-05-03T00:43:54.6817951Z   AR      drivers/android/built-in.a
2026-05-03T00:43:54.6975660Z   AR      drivers/auxdisplay/built-in.a
2026-05-03T00:43:54.7260600Z   CC      drivers/base/firmware_loader/fallback_table.o
2026-05-03T00:43:54.8429591Z   CC      sound/core/seq/seq_system.o
2026-05-03T00:43:54.9354056Z   CC      kernel/exec_domain.o
2026-05-03T00:43:55.0609576Z   CC      fs/proc/uptime.o
2026-05-03T00:43:55.2789791Z   CC      sound/core/seq/seq_ports.o
2026-05-03T00:43:55.3989640Z   CC      drivers/base/firmware_loader/main.o
2026-05-03T00:43:55.4533606Z   CC      fs/proc/util.o
2026-05-03T00:43:55.4849396Z   CC      kernel/panic.o
2026-05-03T00:43:55.6479602Z   CC      fs/proc/version.o
2026-05-03T00:43:55.9565906Z   CC      sound/core/seq/seq_info.o
2026-05-03T00:43:56.0069628Z   CC      fs/proc/softirqs.o
2026-05-03T00:43:56.2829808Z   CC      drivers/base/firmware_loader/fallback.o
2026-05-03T00:43:56.3226384Z   CC      kernel/cpu.o
2026-05-03T00:43:56.3233097Z   CC      sound/core/seq/seq_dummy.o
2026-05-03T00:43:56.3429314Z   CC      fs/proc/namespaces.o
2026-05-03T00:43:56.7607473Z   CC      sound/core/seq/seq_midi.o
2026-05-03T00:43:56.8583362Z   AR      drivers/base/firmware_loader/built-in.a
2026-05-03T00:43:56.8797650Z   CC      drivers/base/power/sysfs.o
2026-05-03T00:43:56.9629446Z   CC      fs/proc/self.o
2026-05-03T00:43:57.1989538Z   CC      sound/core/seq/seq_midi_event.o
2026-05-03T00:43:57.3917522Z   CC      fs/proc/thread_self.o
2026-05-03T00:43:57.4237365Z   CC      drivers/base/power/generic_ops.o
2026-05-03T00:43:57.6879769Z   CC      kernel/exit.o
2026-05-03T00:43:57.7059323Z   AR      sound/core/seq/built-in.a
2026-05-03T00:43:57.7219211Z   CC      sound/core/sound.o
2026-05-03T00:43:57.8459740Z   CC      fs/proc/secboot_fuse.o
2026-05-03T00:43:57.9220984Z   CC      drivers/base/power/common.o
2026-05-03T00:43:58.2039480Z   CC      fs/proc/serial_num.o
2026-05-03T00:43:58.3930263Z   CC      sound/core/init.o
2026-05-03T00:43:58.5179583Z   CC      fs/proc/proc_sysctl.o
2026-05-03T00:43:58.5572656Z   CC      drivers/base/power/qos.o
2026-05-03T00:43:59.1679683Z   CC      sound/core/memory.o
2026-05-03T00:43:59.3849544Z   CC      kernel/softirq.o
2026-05-03T00:43:59.5199556Z   CC      drivers/base/power/runtime.o
2026-05-03T00:43:59.5719397Z   CC      fs/proc/proc_net.o
2026-05-03T00:43:59.6199516Z   CC      sound/core/control.o
2026-05-03T00:44:00.3229610Z   CC      drivers/base/power/wakeirq.o
2026-05-03T00:44:00.4279471Z   CC      fs/proc/kmsg.o
2026-05-03T00:44:00.4309281Z   CC      kernel/resource.o
2026-05-03T00:44:00.7909676Z   CC      fs/proc/page.o
2026-05-03T00:44:00.8377823Z   CC      sound/core/misc.o
2026-05-03T00:44:00.8809444Z   CC      drivers/base/power/main.o
2026-05-03T00:44:01.2089519Z   CC      kernel/sysctl.o
2026-05-03T00:44:01.3139467Z   CC      sound/core/device.o
2026-05-03T00:44:01.3909491Z   AR      fs/proc/built-in.a
2026-05-03T00:44:01.4169308Z   CC      fs/quota/dquot.o
2026-05-03T00:44:01.8199387Z   CC      sound/core/info.o
2026-05-03T00:44:01.8640007Z ../fs/quota/dquot.c:1054:6: warning: variable 'reserved' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:01.8669208Z         int reserved = 0;
2026-05-03T00:44:01.8698921Z             ^
2026-05-03T00:44:02.2419491Z   CC      drivers/base/power/wakeup.o
2026-05-03T00:44:02.2909700Z 1 warning generated.
2026-05-03T00:44:02.5729342Z   CC      fs/quota/quota_v2.o
2026-05-03T00:44:02.6139505Z   CC      sound/core/ctljack.o
2026-05-03T00:44:02.8449566Z   CC      kernel/sysctl_binary.o
2026-05-03T00:44:02.9349668Z   CC      sound/core/jack.o
2026-05-03T00:44:02.9772942Z   CC      fs/quota/quota_tree.o
2026-05-03T00:44:03.3439537Z   CC      drivers/base/power/wakeup_stats.o
2026-05-03T00:44:03.5779607Z   CC      sound/core/hwdep.o
2026-05-03T00:44:03.6759539Z   CC      fs/quota/quota.o
2026-05-03T00:44:03.6849405Z   CC      drivers/base/power/domain.o
2026-05-03T00:44:03.6969298Z   CC      kernel/capability.o
2026-05-03T00:44:04.3491786Z   CC      sound/core/timer.o
2026-05-03T00:44:04.3761254Z   CC      fs/quota/kqid.o
2026-05-03T00:44:04.6209762Z   CC      kernel/ptrace.o
2026-05-03T00:44:04.7789717Z   CC      drivers/base/power/domain_governor.o
2026-05-03T00:44:04.8489734Z   CC      fs/quota/netlink.o
2026-05-03T00:44:05.1619520Z   CC      drivers/base/power/clock_ops.o
2026-05-03T00:44:05.4789603Z   CC      sound/core/hrtimer.o
2026-05-03T00:44:05.6649353Z   CC      kernel/user.o
2026-05-03T00:44:05.6829817Z   AR      fs/quota/built-in.a
2026-05-03T00:44:05.7099622Z   CC      fs/ramfs/inode.o
2026-05-03T00:44:05.7711766Z   AR      drivers/base/power/built-in.a
2026-05-03T00:44:05.8009370Z   CC      drivers/base/regmap/regmap.o
2026-05-03T00:44:05.8099301Z   CC      sound/core/pcm.o
2026-05-03T00:44:06.2859986Z   CC      kernel/signal.o
2026-05-03T00:44:06.2889383Z   CC      fs/ramfs/file-mmu.o
2026-05-03T00:44:06.7119526Z   AR      fs/ramfs/built-in.a
2026-05-03T00:44:06.7244240Z   CC      sound/core/pcm_native.o
2026-05-03T00:44:06.7319417Z   CC      fs/sdcardfs/dentry.o
2026-05-03T00:44:07.2139358Z   CC      fs/sdcardfs/file.o
2026-05-03T00:44:07.2989464Z   CC      drivers/base/regmap/regcache.o
2026-05-03T00:44:07.7269390Z   CC      fs/sdcardfs/inode.o
2026-05-03T00:44:08.0709724Z   CC      drivers/base/regmap/regcache-rbtree.o
2026-05-03T00:44:08.2303683Z   CC      fs/sdcardfs/main.o
2026-05-03T00:44:08.2891223Z   CC      kernel/sys.o
2026-05-03T00:44:08.4819718Z   CC      sound/core/pcm_lib.o
2026-05-03T00:44:08.5260041Z   CC      drivers/base/regmap/regcache-flat.o
2026-05-03T00:44:08.9668328Z   CC      drivers/base/regmap/regmap-i2c.o
2026-05-03T00:44:08.9829694Z   CC      fs/sdcardfs/super.o
2026-05-03T00:44:09.4699897Z   CC      fs/sdcardfs/lookup.o
2026-05-03T00:44:09.5692964Z   CC      drivers/base/regmap/regmap-spi.o
2026-05-03T00:44:09.8334273Z ../fs/sdcardfs/lookup.c:89:30: warning: variable 'info' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:09.8379146Z         struct sdcardfs_inode_info *info;
2026-05-03T00:44:09.8379629Z                                     ^
2026-05-03T00:44:09.8419392Z ../fs/sdcardfs/lookup.c:261:27: warning: variable 'sbi' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:09.8420218Z         struct sdcardfs_sb_info *sbi;
2026-05-03T00:44:09.8449178Z                                  ^
2026-05-03T00:44:09.8809684Z 2 warnings generated.
2026-05-03T00:44:09.8999528Z   CC      sound/core/pcm_misc.o
2026-05-03T00:44:09.9029125Z   CC      kernel/umh.o
2026-05-03T00:44:09.9106195Z   CC      fs/sdcardfs/mmap.o
2026-05-03T00:44:10.2329477Z   CC      drivers/base/regmap/regmap-mmio.o
2026-05-03T00:44:10.3049461Z   CC      fs/sdcardfs/packagelist.o
2026-05-03T00:44:10.6499590Z   CC      sound/core/pcm_memory.o
2026-05-03T00:44:10.8549586Z   AR      drivers/base/regmap/built-in.a
2026-05-03T00:44:10.8783060Z   AR      drivers/base/test/built-in.a
2026-05-03T00:44:10.8919529Z   CC      drivers/base/component.o
2026-05-03T00:44:10.9009478Z   CC      kernel/workqueue.o
2026-05-03T00:44:11.4029491Z   CC      sound/core/memalloc.o
2026-05-03T00:44:11.5899774Z   CC      drivers/base/core.o
2026-05-03T00:44:11.9270224Z   CC      fs/sdcardfs/derived_perm.o
2026-05-03T00:44:12.1779322Z   CC      sound/core/pcm_timer.o
2026-05-03T00:44:12.4549626Z   AR      fs/sdcardfs/built-in.a
2026-05-03T00:44:12.4779250Z   CC      fs/sysfs/file.o
2026-05-03T00:44:12.6179558Z   CC      sound/core/seq_device.o
2026-05-03T00:44:12.6239453Z   CC      kernel/pid.o
2026-05-03T00:44:13.0804667Z   CC      drivers/base/bus.o
2026-05-03T00:44:13.1419617Z   CC      fs/sysfs/dir.o
2026-05-03T00:44:13.2949137Z   CC      sound/core/rawmidi.o
2026-05-03T00:44:13.5540393Z   CC      kernel/task_work.o
2026-05-03T00:44:13.6699221Z   CC      fs/sysfs/symlink.o
2026-05-03T00:44:13.7246268Z   CC      drivers/base/dd.o
2026-05-03T00:44:14.1350223Z   CC      kernel/extable.o
2026-05-03T00:44:14.3279607Z   CC      fs/sysfs/mount.o
2026-05-03T00:44:14.3479673Z   AR      sound/core/built-in.a
2026-05-03T00:44:14.3909635Z   AR      sound/drivers/mpu401/built-in.a
2026-05-03T00:44:14.4051108Z   AR      sound/drivers/opl3/built-in.a
2026-05-03T00:44:14.4246093Z   AR      sound/drivers/opl4/built-in.a
2026-05-03T00:44:14.4439599Z   AR      sound/drivers/pcsp/built-in.a
2026-05-03T00:44:14.4619326Z   AR      sound/drivers/vx/built-in.a
2026-05-03T00:44:14.4769386Z   AR      sound/drivers/built-in.a
2026-05-03T00:44:14.4939131Z   AR      sound/firewire/built-in.a
2026-05-03T00:44:14.5129242Z   AR      sound/hda/built-in.a
2026-05-03T00:44:14.5339223Z   AR      sound/i2c/other/built-in.a
2026-05-03T00:44:14.5457556Z   AR      sound/i2c/built-in.a
2026-05-03T00:44:14.5699444Z   AR      sound/isa/ad1816a/built-in.a
2026-05-03T00:44:14.5803534Z   CC      drivers/base/syscore.o
2026-05-03T00:44:14.5859424Z   AR      sound/isa/ad1848/built-in.a
2026-05-03T00:44:14.6009184Z   AR      sound/isa/cs423x/built-in.a
2026-05-03T00:44:14.6189156Z   AR      sound/isa/es1688/built-in.a
2026-05-03T00:44:14.6339187Z   AR      sound/isa/galaxy/built-in.a
2026-05-03T00:44:14.6479308Z   AR      sound/isa/gus/built-in.a
2026-05-03T00:44:14.6629335Z   AR      sound/isa/msnd/built-in.a
2026-05-03T00:44:14.6650193Z   CC      fs/sysfs/group.o
2026-05-03T00:44:14.6769060Z   AR      sound/isa/opti9xx/built-in.a
2026-05-03T00:44:14.6929083Z   AR      sound/isa/sb/built-in.a
2026-05-03T00:44:14.7097872Z   AR      sound/isa/wavefront/built-in.a
2026-05-03T00:44:14.7259268Z   AR      sound/isa/wss/built-in.a
2026-05-03T00:44:14.7499126Z   AR      sound/isa/built-in.a
2026-05-03T00:44:14.7679149Z   AR      sound/mips/built-in.a
2026-05-03T00:44:14.7828254Z   AR      sound/parisc/built-in.a
2026-05-03T00:44:14.8035530Z   AR      sound/pci/ac97/built-in.a
2026-05-03T00:44:14.8209229Z   AR      sound/pci/ali5451/built-in.a
2026-05-03T00:44:14.8239158Z   CC      kernel/params.o
2026-05-03T00:44:14.8359127Z   AR      sound/pci/asihpi/built-in.a
2026-05-03T00:44:14.8509131Z   AR      sound/pci/au88x0/built-in.a
2026-05-03T00:44:14.8669162Z   AR      sound/pci/aw2/built-in.a
2026-05-03T00:44:14.8839141Z   AR      sound/pci/ca0106/built-in.a
2026-05-03T00:44:14.8989135Z   AR      sound/pci/cs46xx/built-in.a
2026-05-03T00:44:14.9149115Z   AR      sound/pci/cs5535audio/built-in.a
2026-05-03T00:44:14.9319252Z   AR      sound/pci/ctxfi/built-in.a
2026-05-03T00:44:14.9489333Z   AR      sound/pci/echoaudio/built-in.a
2026-05-03T00:44:14.9679261Z   AR      sound/pci/emu10k1/built-in.a
2026-05-03T00:44:14.9829319Z   AR      sound/pci/hda/built-in.a
2026-05-03T00:44:14.9994418Z   AR      sound/pci/ice1712/built-in.a
2026-05-03T00:44:15.0194591Z   AR      sound/pci/korg1212/built-in.a
2026-05-03T00:44:15.0367811Z   AR      sound/pci/lola/built-in.a
2026-05-03T00:44:15.0544672Z   AR      sound/pci/lx6464es/built-in.a
2026-05-03T00:44:15.0708021Z   AR      sound/pci/mixart/built-in.a
2026-05-03T00:44:15.0891665Z   AR      sound/pci/nm256/built-in.a
2026-05-03T00:44:15.1039070Z   AR      sound/pci/oxygen/built-in.a
2026-05-03T00:44:15.1209332Z   AR      sound/pci/pcxhr/built-in.a
2026-05-03T00:44:15.1356719Z   AR      sound/pci/riptide/built-in.a
2026-05-03T00:44:15.1509032Z   AR      sound/pci/rme9652/built-in.a
2026-05-03T00:44:15.1669568Z   AR      sound/pci/trident/built-in.a
2026-05-03T00:44:15.1766996Z   AR      fs/sysfs/built-in.a
2026-05-03T00:44:15.1834678Z   AR      sound/pci/vx222/built-in.a
2026-05-03T00:44:15.2001328Z   CC      fs/tracefs/inode.o
2026-05-03T00:44:15.2029920Z   AR      sound/pci/ymfpci/built-in.a
2026-05-03T00:44:15.2427674Z   AR      sound/pci/built-in.a
2026-05-03T00:44:15.2670164Z   AR      sound/pcmcia/pdaudiocf/built-in.a
2026-05-03T00:44:15.2849420Z   AR      sound/pcmcia/vx/built-in.a
2026-05-03T00:44:15.2980837Z   AR      sound/pcmcia/built-in.a
2026-05-03T00:44:15.3139053Z   AR      sound/ppc/built-in.a
2026-05-03T00:44:15.3329408Z   AR      sound/sh/built-in.a
2026-05-03T00:44:15.3551567Z   AR      sound/soc/adi/built-in.a
2026-05-03T00:44:15.3711861Z   AR      sound/soc/amd/built-in.a
2026-05-03T00:44:15.4009134Z   CC      kernel/kthread.o
2026-05-03T00:44:15.4062220Z   AR      sound/soc/atmel/built-in.a
2026-05-03T00:44:15.4239257Z   AR      sound/soc/au1x/built-in.a
2026-05-03T00:44:15.4419443Z   AR      sound/soc/bcm/built-in.a
2026-05-03T00:44:15.4594877Z   AR      sound/soc/cirrus/built-in.a
2026-05-03T00:44:15.4889746Z   CC      sound/soc/codecs/aw87xxx/aw87xxx.o
2026-05-03T00:44:15.5529008Z   CC      drivers/base/driver.o
2026-05-03T00:44:15.7482679Z   AR      fs/tracefs/built-in.a
2026-05-03T00:44:15.7679890Z   SHIPPED fs/unicode/utf8data.h
2026-05-03T00:44:15.7709147Z   CC      fs/unicode/utf8-core.o
2026-05-03T00:44:16.0709667Z   CC      drivers/base/class.o
2026-05-03T00:44:16.0829824Z ../sound/soc/codecs/aw87xxx/aw87xxx.c:513:8: warning: variable 'profile' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:16.0831459Z         char *profile;
2026-05-03T00:44:16.0870175Z               ^
2026-05-03T00:44:16.2610318Z   CC      fs/unicode/utf8-norm.o
2026-05-03T00:44:16.2639438Z 1 warning generated.
2026-05-03T00:44:16.3999364Z   CC      kernel/sys_ni.o
2026-05-03T00:44:16.5870982Z   CC      sound/soc/codecs/aw87xxx/aw87xxx_device.o
2026-05-03T00:44:16.5989407Z   CC      kernel/nsproxy.o
2026-05-03T00:44:16.7169567Z   CC      drivers/base/platform.o
2026-05-03T00:44:16.9149234Z   AR      fs/unicode/built-in.a
2026-05-03T00:44:16.9409464Z   CC      fs/verity/enable.o
2026-05-03T00:44:17.2739720Z   CC      sound/soc/codecs/aw87xxx/aw87xxx_monitor.o
2026-05-03T00:44:17.2759447Z   CC      kernel/notifier.o
2026-05-03T00:44:17.7129363Z   CC      drivers/base/cpu.o
2026-05-03T00:44:17.9507456Z   CC      fs/verity/hash_algs.o
2026-05-03T00:44:17.9846504Z   CC      kernel/ksysfs.o
2026-05-03T00:44:17.9979543Z   CC      sound/soc/codecs/aw87xxx/aw87xxx_bin_parse.o
2026-05-03T00:44:18.3307273Z   CC      drivers/base/firmware.o
2026-05-03T00:44:18.4548770Z   CC      sound/soc/codecs/aw87xxx/aw87xxx_dsp.o
2026-05-03T00:44:18.4899648Z   CC      fs/verity/init.o
2026-05-03T00:44:18.6888363Z   CC      kernel/cred.o
2026-05-03T00:44:18.7809606Z   CC      drivers/base/init.o
2026-05-03T00:44:18.7999340Z   CC      fs/verity/measure.o
2026-05-03T00:44:19.0889404Z   CC      drivers/base/map.o
2026-05-03T00:44:19.2159462Z   CC      sound/soc/codecs/aw87xxx/aw87xxx_acf_bin.o
2026-05-03T00:44:19.3629672Z   CC      fs/verity/open.o
2026-05-03T00:44:19.4049588Z   CC      drivers/base/devres.o
2026-05-03T00:44:19.5979395Z   CC      kernel/reboot.o
2026-05-03T00:44:19.6220129Z ../sound/soc/codecs/aw87xxx/aw87xxx_acf_bin.c:152:21: warning: variable 'acf_dde' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:19.6249069Z         struct aw_acf_dde *acf_dde = NULL;
2026-05-03T00:44:19.6249520Z                            ^
2026-05-03T00:44:19.6250378Z ../sound/soc/codecs/aw87xxx/aw87xxx_acf_bin.c:284:31: warning: variable 'acf_dde' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:19.6251280Z         struct aw_acf_dde_v_1_0_0_0 *acf_dde = NULL;
2026-05-03T00:44:19.6251726Z                                      ^
2026-05-03T00:44:19.9252402Z   CC      fs/verity/verify.o
2026-05-03T00:44:19.9879478Z   CC      drivers/base/attribute_container.o
2026-05-03T00:44:20.0329376Z 2 warnings generated.
2026-05-03T00:44:20.0649345Z   AR      sound/soc/codecs/aw87xxx/built-in.a
2026-05-03T00:44:20.1129612Z   CC      sound/soc/codecs/sipa/sipa.o
2026-05-03T00:44:20.5108076Z   CC      drivers/base/transport_class.o
2026-05-03T00:44:20.5169321Z   CC      kernel/async.o
2026-05-03T00:44:20.6619561Z   CC      fs/verity/signature.o
2026-05-03T00:44:20.9577616Z   CC      kernel/range.o
2026-05-03T00:44:20.9736739Z   CC      drivers/base/topology.o
2026-05-03T00:44:21.0899695Z   CC      kernel/smpboot.o
2026-05-03T00:44:21.2065205Z   AR      fs/verity/built-in.a
2026-05-03T00:44:21.2209619Z   CC      fs/open.o
2026-05-03T00:44:21.2479540Z   CC      sound/soc/codecs/sipa/sipa_regmap.o
2026-05-03T00:44:21.3929412Z   CC      drivers/base/container.o
2026-05-03T00:44:21.6120086Z   CC      kernel/ucount.o
2026-05-03T00:44:21.7052248Z   CC      drivers/base/property.o
2026-05-03T00:44:21.8629676Z   CC      sound/soc/codecs/sipa/sipa_aux_dev_if.o
2026-05-03T00:44:21.9439466Z   CC      kernel/kmod.o
2026-05-03T00:44:22.4099413Z   CC      fs/read_write.o
2026-05-03T00:44:22.7299492Z   CC      sound/soc/codecs/sipa/sipa_91xx.o
2026-05-03T00:44:22.8819568Z   CC      kernel/groups.o
2026-05-03T00:44:23.0019660Z   CC      drivers/base/cacheinfo.o
2026-05-03T00:44:23.2839760Z ../sound/soc/codecs/sipa/sipa_91xx.c:82:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:23.2869205Z         int ret;
2026-05-03T00:44:23.2898980Z             ^
2026-05-03T00:44:23.3599892Z 1 warning generated.
2026-05-03T00:44:23.3910957Z   CC      sound/soc/codecs/sipa/sipa_parameter.o
2026-05-03T00:44:23.5069552Z   CC      drivers/base/devcon.o
2026-05-03T00:44:23.7213274Z   CC      fs/file_table.o
2026-05-03T00:44:23.8039405Z   CC      kernel/freezer.o
2026-05-03T00:44:23.9559646Z   CC      sound/soc/codecs/sipa/sipa_tuning_misc.o
2026-05-03T00:44:23.9809446Z   CC      drivers/base/module.o
2026-05-03T00:44:24.2649817Z ../drivers/base/module.c:36:6: warning: variable 'no_warn' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:24.2689231Z         int no_warn;
2026-05-03T00:44:24.2698951Z             ^
2026-05-03T00:44:24.2819074Z 1 warning generated.
2026-05-03T00:44:24.3119312Z   CC      drivers/base/soc.o
2026-05-03T00:44:24.3499616Z   CC      sound/soc/codecs/sipa/sipa_tuning_if.o
2026-05-03T00:44:24.6279569Z   CC      fs/super.o
2026-05-03T00:44:24.6799869Z   CC      kernel/profile.o
2026-05-03T00:44:24.7571885Z   CC      drivers/base/pinctrl.o
2026-05-03T00:44:24.7628826Z   AR      sound/soc/codecs/sipa/built-in.a
2026-05-03T00:44:24.7769238Z   CC      sound/soc/codecs/mt6358.o
2026-05-03T00:44:25.1599667Z   CC      drivers/base/platform-msi.o
2026-05-03T00:44:25.5259878Z   CC      kernel/stacktrace.o
2026-05-03T00:44:25.7020448Z   CC      drivers/base/arch_topology.o
2026-05-03T00:44:25.7101163Z   CC      fs/char_dev.o
2026-05-03T00:44:25.8341609Z   CC [M]  sound/soc/codecs/mt6357-accdet.o
2026-05-03T00:44:26.1469440Z   CC      kernel/futex.o
2026-05-03T00:44:26.2889641Z   AR      drivers/base/built-in.a
2026-05-03T00:44:26.3449823Z   CC      drivers/block/zram/zcomp.o
2026-05-03T00:44:26.3699838Z ../sound/soc/codecs/mt6357-accdet.c:619:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:26.3729187Z         int ret = 0;
2026-05-03T00:44:26.3758940Z             ^
2026-05-03T00:44:26.3777041Z ../sound/soc/codecs/mt6357-accdet.c:702:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:26.3788882Z         int ret = 0;
2026-05-03T00:44:26.3816120Z             ^
2026-05-03T00:44:26.3843512Z ../sound/soc/codecs/mt6357-accdet.c:1496:22: warning: variable 'acc_sts' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:26.3863380Z         u32 irq_status = 0, acc_sts = 0, eint_sts = 0;
2026-05-03T00:44:26.3888928Z                             ^
2026-05-03T00:44:26.3889749Z ../sound/soc/codecs/mt6357-accdet.c:1496:35: warning: variable 'eint_sts' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:26.3890624Z         u32 irq_status = 0, acc_sts = 0, eint_sts = 0;
2026-05-03T00:44:26.3891089Z                                          ^
2026-05-03T00:44:26.3891832Z ../sound/soc/codecs/mt6357-accdet.c:1566:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:26.3892600Z         int ret = 0;
2026-05-03T00:44:26.3892894Z             ^
2026-05-03T00:44:26.3909333Z ../sound/soc/codecs/mt6357-accdet.c:1975:19: warning: variable 'res' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:26.3959036Z         struct resource *res;
2026-05-03T00:44:26.3988997Z                          ^
2026-05-03T00:44:26.6069485Z 6 warnings generated.
2026-05-03T00:44:26.6391202Z   CC      fs/stat.o
2026-05-03T00:44:26.6990798Z   CC      drivers/block/zram/zram_drv.o
2026-05-03T00:44:26.9459616Z   CC [M]  sound/soc/codecs/mt6359-accdet.o
2026-05-03T00:44:27.2079556Z   CC      kernel/smp.o
2026-05-03T00:44:27.2979990Z ../drivers/block/zram/zram_drv.c:2710:23: error: expected expression
2026-05-03T00:44:27.3009339Z         zram_debugfs_destroy(void);
2026-05-03T00:44:27.3010184Z                              ^
2026-05-03T00:44:27.3010538Z 1 error generated.
2026-05-03T00:44:27.3047261Z make[4]: *** [../scripts/Makefile.build:334: drivers/block/zram/zram_drv.o] Error 1
2026-05-03T00:44:27.3069138Z make[3]: *** [../scripts/Makefile.build:637: drivers/block/zram] Error 2
2026-05-03T00:44:27.3099131Z make[2]: *** [../scripts/Makefile.build:637: drivers/block] Error 2
2026-05-03T00:44:27.3103649Z make[1]: *** [/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/Makefile:1180: drivers] Error 2
2026-05-03T00:44:27.3104673Z make[1]: *** Waiting for unfinished jobs....
2026-05-03T00:44:27.3189590Z   AR      sound/soc/davinci/built-in.a
2026-05-03T00:44:27.3269309Z   CC      fs/exec.o
2026-05-03T00:44:27.4900015Z ../sound/soc/codecs/mt6359-accdet.c:742:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:27.4929081Z         int ret = 0;
2026-05-03T00:44:27.4929431Z             ^
2026-05-03T00:44:27.4930151Z ../sound/soc/codecs/mt6359-accdet.c:825:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:27.4930931Z         int ret = 0;
2026-05-03T00:44:27.4931223Z             ^
2026-05-03T00:44:27.4979478Z ../sound/soc/codecs/mt6359-accdet.c:2091:33: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:27.4999160Z         u32 efuseval = 0, eintvth = 0, ret = 0;
2026-05-03T00:44:27.5039035Z                                        ^
2026-05-03T00:44:27.5039924Z ../sound/soc/codecs/mt6359-accdet.c:2142:35: warning: variable 'eint_sts' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:27.5040858Z         u32 irq_status = 0, acc_sts = 0, eint_sts = 0;
2026-05-03T00:44:27.5041324Z                                          ^
2026-05-03T00:44:27.5042138Z ../sound/soc/codecs/mt6359-accdet.c:2142:22: warning: variable 'acc_sts' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:27.5043006Z         u32 irq_status = 0, acc_sts = 0, eint_sts = 0;
2026-05-03T00:44:27.5043446Z                             ^
2026-05-03T00:44:27.5044139Z ../sound/soc/codecs/mt6359-accdet.c:2185:6: warning: variable 'ret' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:27.5044890Z         int ret = 0;
2026-05-03T00:44:27.5045177Z             ^
2026-05-03T00:44:27.5139378Z ../sound/soc/codecs/mt6359-accdet.c:2981:19: warning: variable 'res' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:27.5168956Z         struct resource *res;
2026-05-03T00:44:27.5188931Z                          ^
2026-05-03T00:44:27.6687500Z   AR      sound/sparc/built-in.a
2026-05-03T00:44:27.6856115Z   AR      sound/spi/built-in.a
2026-05-03T00:44:27.6938975Z   CC      kernel/uid16.o
2026-05-03T00:44:27.7853026Z   AR      sound/soc/dwc/built-in.a
2026-05-03T00:44:27.7921846Z 7 warnings generated.
2026-05-03T00:44:27.8059766Z   AR      sound/soc/fsl/built-in.a
2026-05-03T00:44:27.8136795Z   CC      fs/pipe.o
2026-05-03T00:44:28.1509594Z   AR      sound/soc/codecs/built-in.a
2026-05-03T00:44:28.1689269Z   AR      sound/soc/generic/built-in.a
2026-05-03T00:44:28.1869293Z   AR      sound/soc/hisilicon/built-in.a
2026-05-03T00:44:28.2059326Z   AR      sound/soc/img/built-in.a
2026-05-03T00:44:28.2309370Z   AR      sound/soc/intel/boards/built-in.a
2026-05-03T00:44:28.2459118Z   AR      sound/soc/intel/common/built-in.a
2026-05-03T00:44:28.2579075Z   AR      sound/soc/intel/built-in.a
2026-05-03T00:44:28.2759095Z   AR      sound/soc/jz4740/built-in.a
2026-05-03T00:44:28.2909200Z   AR      sound/soc/kirkwood/built-in.a
2026-05-03T00:44:28.3173691Z   CC      kernel/module.o
2026-05-03T00:44:28.3449713Z   CC      sound/soc/mediatek/common/mtk-mmap-ion.o
2026-05-03T00:44:28.7676511Z   CC      sound/soc/mediatek/common/mtk-afe-platform-driver.o
2026-05-03T00:44:28.8019436Z   AR      sound/synth/emux/built-in.a
2026-05-03T00:44:28.8287028Z   AR      sound/synth/built-in.a
2026-05-03T00:44:28.8519252Z   AR      sound/soc/meson/built-in.a
2026-05-03T00:44:28.8639204Z   CC      kernel/kallsyms.o
2026-05-03T00:44:28.8699154Z   CC      fs/namei.o
2026-05-03T00:44:29.6429657Z   CC      sound/soc/mediatek/common/mtk-afe-fe-dai.o
2026-05-03T00:44:30.0377520Z   CC      kernel/compat.o
2026-05-03T00:44:30.0423137Z   CC      sound/soc/mediatek/mt6768/mt6768-afe-pcm.o
2026-05-03T00:44:30.4659718Z   CC      sound/soc/mediatek/common/mtk-sram-manager.o
2026-05-03T00:44:30.6679668Z   CC      sound/soc/mediatek/mt6768/mt6768-afe-clk.o
2026-05-03T00:44:30.7129700Z   CC      fs/fcntl.o
2026-05-03T00:44:31.0157322Z   CC      kernel/utsname.o
2026-05-03T00:44:31.2309723Z   CC      sound/soc/mediatek/mt6768/mt6768-afe-gpio.o
2026-05-03T00:44:31.3081571Z   CC      sound/soc/mediatek/common/mtk-sp-pcm-ops.o
2026-05-03T00:44:31.3219480Z   CC      kernel/pid_namespace.o
2026-05-03T00:44:31.6019478Z   CC      fs/ioctl.o
2026-05-03T00:44:31.7990429Z   CC      sound/soc/mediatek/mt6768/mt6768-dai-adda.o
2026-05-03T00:44:32.0529715Z   CC      sound/soc/mediatek/common/mtk-afe-debug.o
2026-05-03T00:44:32.1961264Z   GZIP    kernel/config_data.gz
2026-05-03T00:44:32.2169480Z   CC      kernel/stop_machine.o
2026-05-03T00:44:32.2925570Z   CC      sound/soc/mediatek/mt6768/mt6768-afe-control.o
2026-05-03T00:44:32.5289394Z   CC      fs/readdir.o
2026-05-03T00:44:32.8115083Z   CC      sound/soc/mediatek/common/mtk-sp-spk-amp.o
2026-05-03T00:44:32.9969797Z   CC      kernel/audit.o
2026-05-03T00:44:33.0554918Z   CC      sound/soc/mediatek/mt6768/mt6768-dai-i2s.o
2026-05-03T00:44:33.4729784Z   CC      fs/select.o
2026-05-03T00:44:33.5999535Z   CC      sound/soc/mediatek/mt6768/mt6768-dai-hw-gain.o
2026-05-03T00:44:33.6969617Z   CC      sound/soc/mediatek/common/mtk-usip.o
2026-05-03T00:44:34.1469495Z   CC      sound/soc/mediatek/mt6768/mt6768-dai-pcm.o
2026-05-03T00:44:34.2519602Z   CC      sound/soc/mediatek/common/mtk-btcvsd.o
2026-05-03T00:44:34.4929454Z   CC      kernel/auditfilter.o
2026-05-03T00:44:34.7059565Z   CC      sound/soc/mediatek/mt6768/mt6768-dai-hostless.o
2026-05-03T00:44:34.9286417Z   AR      sound/soc/mediatek/common/built-in.a
2026-05-03T00:44:34.9589470Z   AR      sound/soc/mxs/built-in.a
2026-05-03T00:44:34.9819373Z   AR      sound/usb/6fire/built-in.a
2026-05-03T00:44:34.9987133Z   AR      sound/usb/bcd2000/built-in.a
2026-05-03T00:44:35.0139217Z   AR      sound/usb/caiaq/built-in.a
2026-05-03T00:44:35.0301192Z   AR      sound/usb/hiface/built-in.a
2026-05-03T00:44:35.0459207Z   AR      sound/usb/misc/built-in.a
2026-05-03T00:44:35.0639226Z   AR      sound/usb/usx2y/built-in.a
2026-05-03T00:44:35.0759221Z   CC      sound/usb/card.o
2026-05-03T00:44:35.1089346Z   CC      fs/dcache.o
2026-05-03T00:44:35.2259554Z   CC      sound/soc/mediatek/mt6768/mt6768-misc-control.o
2026-05-03T00:44:35.5470940Z   CC      kernel/auditsc.o
2026-05-03T00:44:35.9194105Z   CC      sound/soc/mediatek/mt6768/mt6768-mt6358.o
2026-05-03T00:44:36.0179679Z   CC      sound/usb/clock.o
2026-05-03T00:44:36.2529245Z   CC      fs/inode.o
2026-05-03T00:44:36.4649668Z   AR      sound/soc/mediatek/mt6768/built-in.a
2026-05-03T00:44:36.4829691Z   AR      sound/soc/mediatek/built-in.a
2026-05-03T00:44:36.5019475Z   AR      sound/soc/nuc900/built-in.a
2026-05-03T00:44:36.5209983Z   AR      sound/soc/omap/built-in.a
2026-05-03T00:44:36.5410009Z   AR      sound/soc/pxa/built-in.a
2026-05-03T00:44:36.5585145Z   AR      sound/soc/qcom/built-in.a
2026-05-03T00:44:36.5739023Z   AR      sound/soc/rockchip/built-in.a
2026-05-03T00:44:36.5849533Z   CC      sound/usb/endpoint.o
2026-05-03T00:44:36.5919358Z   AR      sound/soc/samsung/built-in.a
2026-05-03T00:44:36.6064336Z   AR      sound/soc/sh/built-in.a
2026-05-03T00:44:36.6237740Z   AR      sound/soc/sirf/built-in.a
2026-05-03T00:44:36.6407985Z   AR      sound/soc/spear/built-in.a
2026-05-03T00:44:36.6599449Z   AR      sound/soc/sti/built-in.a
2026-05-03T00:44:36.6748932Z   AR      sound/soc/stm/built-in.a
2026-05-03T00:44:36.6916621Z   AR      sound/soc/sunxi/built-in.a
2026-05-03T00:44:36.7109151Z   AR      sound/soc/tegra/built-in.a
2026-05-03T00:44:36.7249053Z   AR      sound/soc/txx9/built-in.a
2026-05-03T00:44:36.7411884Z   AR      sound/soc/uniphier/built-in.a
2026-05-03T00:44:36.7589180Z   AR      sound/soc/ux500/built-in.a
2026-05-03T00:44:36.7769180Z   AR      sound/soc/xtensa/built-in.a
2026-05-03T00:44:36.7919140Z   AR      sound/soc/zte/built-in.a
2026-05-03T00:44:36.8009061Z   CC      sound/soc/soc-core.o
2026-05-03T00:44:36.8574732Z   CC      kernel/audit_watch.o
2026-05-03T00:44:37.2469868Z   CC      sound/usb/format.o
2026-05-03T00:44:37.4969041Z   CC      kernel/audit_fsnotify.o
2026-05-03T00:44:37.5749528Z   CC      fs/attr.o
2026-05-03T00:44:37.8539659Z   CC      sound/usb/helper.o
2026-05-03T00:44:38.1063868Z   CC      kernel/audit_tree.o
2026-05-03T00:44:38.3239652Z   CC      fs/bad_inode.o
2026-05-03T00:44:38.4790157Z   CC      sound/usb/mixer.o
2026-05-03T00:44:38.5209394Z   CC      sound/soc/soc-dapm.o
2026-05-03T00:44:38.8479587Z   CC      fs/file.o
2026-05-03T00:44:38.8619260Z   CC      kernel/kprobes.o
2026-05-03T00:44:38.8979804Z ../sound/usb/mixer.c:1902:28: warning: variable 'first_ch_bits' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:38.9009201Z         unsigned int master_bits, first_ch_bits;
2026-05-03T00:44:38.9018945Z                                   ^
2026-05-03T00:44:39.3948701Z 1 warning generated.
2026-05-03T00:44:39.4309575Z   CC      sound/usb/mixer_quirks.o
2026-05-03T00:44:39.8408140Z   CC      fs/filesystems.o
2026-05-03T00:44:39.8959427Z   CC      kernel/seccomp.o
2026-05-03T00:44:40.0179601Z   CC      sound/soc/soc-jack.o
2026-05-03T00:44:40.0499518Z   CC      sound/usb/mixer_scarlett.o
2026-05-03T00:44:40.5793678Z   CC      sound/usb/mixer_us16x08.o
2026-05-03T00:44:40.6859650Z   CC      fs/namespace.o
2026-05-03T00:44:40.9037510Z   CC      kernel/utsname_sysctl.o
2026-05-03T00:44:41.0229454Z   CC      sound/soc/soc-utils.o
2026-05-03T00:44:41.1189680Z   CC      sound/usb/pcm.o
2026-05-03T00:44:41.1669703Z   CC      kernel/taskstats.o
2026-05-03T00:44:41.8329720Z   CC      sound/soc/soc-pcm.o
2026-05-03T00:44:41.9069549Z   CC      kernel/tsacct.o
2026-05-03T00:44:41.9919809Z   CC      fs/seq_file.o
2026-05-03T00:44:42.2029560Z   CC      sound/usb/power.o
2026-05-03T00:44:42.3119612Z   CC      kernel/tracepoint.o
2026-05-03T00:44:42.6351444Z   CC      sound/usb/proc.o
2026-05-03T00:44:42.8090089Z   CC      fs/xattr.o
2026-05-03T00:44:42.9709479Z   CC      kernel/irq_work.o
2026-05-03T00:44:43.1219374Z   CC      sound/usb/quirks.o
2026-05-03T00:44:43.1699397Z   CC      sound/soc/soc-io.o
2026-05-03T00:44:43.5401025Z   CC      kernel/cpu_pm.o
2026-05-03T00:44:43.7689466Z   CC      fs/libfs.o
2026-05-03T00:44:43.7749188Z   CC      sound/usb/stream.o
2026-05-03T00:44:43.9469799Z   CC      kernel/iomem.o
2026-05-03T00:44:44.0079680Z   CC      sound/soc/soc-devres.o
2026-05-03T00:44:44.4769695Z   CC      sound/usb/validate.o
2026-05-03T00:44:44.6059688Z   CC      kernel/rseq.o
2026-05-03T00:44:44.7979426Z   CC      fs/fs-writeback.o
2026-05-03T00:44:44.8062238Z   CC      sound/soc/soc-ops.o
2026-05-03T00:44:44.8309529Z   CC      sound/usb/midi.o
2026-05-03T00:44:45.2879316Z   CC [M]  kernel/kheaders.o
2026-05-03T00:44:45.5806309Z   UPD     kernel/config_data.h
2026-05-03T00:44:45.5869262Z   CC      kernel/configs.o
2026-05-03T00:44:45.6979483Z   AR      sound/soc/built-in.a
2026-05-03T00:44:45.7249285Z   CC      fs/pnode.o
2026-05-03T00:44:45.8359615Z   AR      sound/usb/built-in.a
2026-05-03T00:44:45.8609276Z   AR      sound/x86/built-in.a
2026-05-03T00:44:45.8769238Z   AR      sound/xen/built-in.a
2026-05-03T00:44:45.8879165Z   CC      sound/sound_core.o
2026-05-03T00:44:45.9580000Z   AR      kernel/built-in.a
2026-05-03T00:44:46.0371602Z   CC      sound/last.o
2026-05-03T00:44:46.1979650Z   CC      fs/splice.o
2026-05-03T00:44:46.3267121Z   CC      fs/sync.o
2026-05-03T00:44:46.3589284Z   AR      sound/built-in.a
2026-05-03T00:44:46.3794071Z   CC      fs/utimes.o
2026-05-03T00:44:46.4554669Z   CC      fs/d_path.o
2026-05-03T00:44:47.0257010Z   CC      fs/stack.o
2026-05-03T00:44:47.3149512Z   CC      fs/fs_struct.o
2026-05-03T00:44:47.3494750Z   CC      fs/statfs.o
2026-05-03T00:44:47.4069600Z   CC      fs/fs_pin.o
2026-05-03T00:44:47.4789517Z   CC      fs/nsfs.o
2026-05-03T00:44:47.8179569Z   CC      fs/buffer.o
2026-05-03T00:44:47.8539542Z   CC      fs/block_dev.o
2026-05-03T00:44:48.0479077Z   CC      fs/direct-io.o
2026-05-03T00:44:48.2749260Z   CC      fs/mpage.o
2026-05-03T00:44:49.0380578Z   CC      fs/proc_namespace.o
2026-05-03T00:44:49.3809477Z   CC      fs/eventpoll.o
2026-05-03T00:44:49.4299389Z   CC      fs/anon_inodes.o
2026-05-03T00:44:49.4689431Z   CC      fs/signalfd.o
2026-05-03T00:44:49.4839431Z   CC      fs/timerfd.o
2026-05-03T00:44:50.0285288Z   CC      fs/eventfd.o
2026-05-03T00:44:50.0989943Z   CC      fs/aio.o
2026-05-03T00:44:50.1619517Z   CC      fs/locks.o
2026-05-03T00:44:50.5279777Z   CC      fs/compat.o
2026-05-03T00:44:50.9427715Z   CC      fs/compat_ioctl.o
2026-05-03T00:44:51.0754021Z   CC      fs/binfmt_script.o
2026-05-03T00:44:51.4289541Z   CC      fs/binfmt_elf.o
2026-05-03T00:44:51.6483042Z   CC      fs/compat_binfmt_elf.o
2026-05-03T00:44:51.6799030Z   CC      fs/mbcache.o
2026-05-03T00:44:52.2369876Z   CC      fs/posix_acl.o
2026-05-03T00:44:52.3449429Z   CC      fs/coredump.o
2026-05-03T00:44:52.4429583Z   CC      fs/drop_caches.o
2026-05-03T00:44:52.4759567Z   CC      fs/iomap.o
2026-05-03T00:44:52.8789571Z   CC      fs/dcookies.o
2026-05-03T00:44:53.5900080Z   AR      fs/built-in.a
2026-05-03T00:44:53.6555094Z make[1]: Leaving directory '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/out'
2026-05-03T00:44:53.6557545Z make: *** [Makefile:146: sub-make] Error 2
2026-05-03T00:44:53.6563262Z BUILD FAILED! Image.gz-dtb not found
2026-05-03T00:44:53.6573132Z   AR      sound/soc/tegra/built-in.a
2026-05-03T00:44:53.6573535Z   AR      sound/soc/txx9/built-in.a
2026-05-03T00:44:53.6573915Z   AR      sound/soc/uniphier/built-in.a
2026-05-03T00:44:53.6574323Z   AR      sound/soc/ux500/built-in.a
2026-05-03T00:44:53.6574692Z   AR      sound/soc/xtensa/built-in.a
2026-05-03T00:44:53.6575056Z   AR      sound/soc/zte/built-in.a
2026-05-03T00:44:53.6575427Z   CC      sound/soc/soc-core.o
2026-05-03T00:44:53.6575770Z   CC      kernel/audit_watch.o
2026-05-03T00:44:53.6576109Z   CC      sound/usb/format.o
2026-05-03T00:44:53.6576448Z   CC      kernel/audit_fsnotify.o
2026-05-03T00:44:53.6576798Z   CC      fs/attr.o
2026-05-03T00:44:53.6577087Z   CC      sound/usb/helper.o
2026-05-03T00:44:53.6577421Z   CC      kernel/audit_tree.o
2026-05-03T00:44:53.6577781Z   CC      fs/bad_inode.o
2026-05-03T00:44:53.6578139Z   CC      sound/usb/mixer.o
2026-05-03T00:44:53.6580260Z   CC      sound/soc/soc-dapm.o
2026-05-03T00:44:53.6580635Z   CC      fs/file.o
2026-05-03T00:44:53.6580936Z   CC      kernel/kprobes.o
2026-05-03T00:44:53.6581561Z ../sound/usb/mixer.c:1902:28: warning: variable 'first_ch_bits' set but not used [-Wunused-but-set-variable]
2026-05-03T00:44:53.6582326Z         unsigned int master_bits, first_ch_bits;
2026-05-03T00:44:53.6582733Z                                   ^
2026-05-03T00:44:53.6583082Z 1 warning generated.
2026-05-03T00:44:53.6583393Z   CC      sound/usb/mixer_quirks.o
2026-05-03T00:44:53.6583755Z   CC      fs/filesystems.o
2026-05-03T00:44:53.6584070Z   CC      kernel/seccomp.o
2026-05-03T00:44:53.6584462Z   CC      sound/soc/soc-jack.o
2026-05-03T00:44:53.6584807Z   CC      sound/usb/mixer_scarlett.o
2026-05-03T00:44:53.6585150Z   CC      sound/usb/mixer_us16x08.o
2026-05-03T00:44:53.6585388Z   CC      fs/namespace.o
2026-05-03T00:44:53.6585614Z   CC      kernel/utsname_sysctl.o
2026-05-03T00:44:53.6585846Z   CC      sound/soc/soc-utils.o
2026-05-03T00:44:53.6586078Z   CC      sound/usb/pcm.o
2026-05-03T00:44:53.6586301Z   CC      kernel/taskstats.o
2026-05-03T00:44:53.6586532Z   CC      sound/soc/soc-pcm.o
2026-05-03T00:44:53.6586757Z   CC      kernel/tsacct.o
2026-05-03T00:44:53.6586961Z   CC      fs/seq_file.o
2026-05-03T00:44:53.6587173Z   CC      sound/usb/power.o
2026-05-03T00:44:53.6587393Z   CC      kernel/tracepoint.o
2026-05-03T00:44:53.6587616Z   CC      sound/usb/proc.o
2026-05-03T00:44:53.6588046Z   CC      fs/xattr.o
2026-05-03T00:44:53.6588246Z   CC      kernel/irq_work.o
2026-05-03T00:44:53.6588677Z   CC      sound/usb/quirks.o
2026-05-03T00:44:53.6589002Z   CC      sound/soc/soc-io.o
2026-05-03T00:44:53.6589320Z   CC      kernel/cpu_pm.o
2026-05-03T00:44:53.6589609Z   CC      fs/libfs.o
2026-05-03T00:44:53.6589871Z   CC      sound/usb/stream.o
2026-05-03T00:44:53.6590169Z   CC      kernel/iomem.o
2026-05-03T00:44:53.6590453Z   CC      sound/soc/soc-devres.o
2026-05-03T00:44:53.6590775Z   CC      sound/usb/validate.o
2026-05-03T00:44:53.6591085Z   CC      kernel/rseq.o
2026-05-03T00:44:53.6591365Z   CC      fs/fs-writeback.o
2026-05-03T00:44:53.6591937Z   CC      sound/soc/soc-ops.o
2026-05-03T00:44:53.6592269Z   CC      sound/usb/midi.o
2026-05-03T00:44:53.6592576Z   CC [M]  kernel/kheaders.o
2026-05-03T00:44:53.6592881Z   UPD     kernel/config_data.h
2026-05-03T00:44:53.6593202Z   CC      kernel/configs.o
2026-05-03T00:44:53.6593495Z   AR      sound/soc/built-in.a
2026-05-03T00:44:53.6593799Z   CC      fs/pnode.o
2026-05-03T00:44:53.6594093Z   AR      sound/usb/built-in.a
2026-05-03T00:44:53.6594410Z   AR      sound/x86/built-in.a
2026-05-03T00:44:53.6594719Z   AR      sound/xen/built-in.a
2026-05-03T00:44:53.6595034Z   CC      sound/sound_core.o
2026-05-03T00:44:53.6595333Z   AR      kernel/built-in.a
2026-05-03T00:44:53.6595617Z   CC      sound/last.o
2026-05-03T00:44:53.6595884Z   CC      fs/splice.o
2026-05-03T00:44:53.6596157Z   CC      fs/sync.o
2026-05-03T00:44:53.6596438Z   AR      sound/built-in.a
2026-05-03T00:44:53.6596745Z   CC      fs/utimes.o
2026-05-03T00:44:53.6597038Z   CC      fs/d_path.o
2026-05-03T00:44:53.6597337Z   CC      fs/stack.o
2026-05-03T00:44:53.6597632Z   CC      fs/fs_struct.o
2026-05-03T00:44:53.6597945Z   CC      fs/statfs.o
2026-05-03T00:44:53.6598216Z   CC      fs/fs_pin.o
2026-05-03T00:44:53.6598726Z   CC      fs/nsfs.o
2026-05-03T00:44:53.6598999Z   CC      fs/buffer.o
2026-05-03T00:44:53.6599304Z   CC      fs/block_dev.o
2026-05-03T00:44:53.6599617Z   CC      fs/direct-io.o
2026-05-03T00:44:53.6599936Z   CC      fs/mpage.o
2026-05-03T00:44:53.6600249Z   CC      fs/proc_namespace.o
2026-05-03T00:44:53.6600597Z   CC      fs/eventpoll.o
2026-05-03T00:44:53.6600904Z   CC      fs/anon_inodes.o
2026-05-03T00:44:53.6601231Z   CC      fs/signalfd.o
2026-05-03T00:44:53.6601516Z   CC      fs/timerfd.o
2026-05-03T00:44:53.6601819Z   CC      fs/eventfd.o
2026-05-03T00:44:53.6602105Z   CC      fs/aio.o
2026-05-03T00:44:53.6602381Z   CC      fs/locks.o
2026-05-03T00:44:53.6602665Z   CC      fs/compat.o
2026-05-03T00:44:53.6602964Z   CC      fs/compat_ioctl.o
2026-05-03T00:44:53.6603303Z   CC      fs/binfmt_script.o
2026-05-03T00:44:53.6603626Z   CC      fs/binfmt_elf.o
2026-05-03T00:44:53.6603952Z   CC      fs/compat_binfmt_elf.o
2026-05-03T00:44:53.6604305Z   CC      fs/mbcache.o
2026-05-03T00:44:53.6604618Z   CC      fs/posix_acl.o
2026-05-03T00:44:53.6604932Z   CC      fs/coredump.o
2026-05-03T00:44:53.6605254Z   CC      fs/drop_caches.o
2026-05-03T00:44:53.6605574Z   CC      fs/iomap.o
2026-05-03T00:44:53.6605879Z   CC      fs/dcookies.o
2026-05-03T00:44:53.6606190Z   AR      fs/built-in.a
2026-05-03T00:44:53.6606814Z make[1]: Leaving directory '/home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN/kernel/out'
2026-05-03T00:44:53.6607563Z make: *** [Makefile:146: sub-make] Error 2
2026-05-03T00:44:53.6618195Z ##[error]Process completed with exit code 1.
2026-05-03T00:44:53.6723880Z Post job cleanup.
2026-05-03T00:44:53.7547119Z [command]/usr/bin/git version
2026-05-03T00:44:53.7583550Z git version 2.53.0
2026-05-03T00:44:53.7618174Z Temporarily overriding HOME='/home/runner/work/_temp/9f5d9602-8a1a-44a7-a476-9012bac3e500' before making global git config changes
2026-05-03T00:44:53.7619222Z Adding repository directory to the temporary git global config as a safe directory
2026-05-03T00:44:53.7624195Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/CastoriceKernelSUN/CastoriceKernelSUN
2026-05-03T00:44:53.7660889Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-05-03T00:44:53.7696167Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-05-03T00:44:53.7915590Z fatal: No url found for submodule path 'temp_susfs' in .gitmodules
2026-05-03T00:44:53.7953056Z ##[warning]The process '/usr/bin/git' failed with exit code 128
2026-05-03T00:44:53.8070638Z Cleaning up orphan processes
2026-05-03T00:44:53.8369711Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
