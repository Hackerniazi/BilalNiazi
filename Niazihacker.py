
$ pkg update
Ign:2 https://dl.bintray.com/grimler/game-packages-24 games InRelease
Ign:3 https://dl.bintray.com/grimler/science-packages-24 science InRelease
Ign:1 https://dl.bintray.com/termux/termux-packages-24 stable InRelease
Get:5 https://dl.bintray.com/grimler/game-packages-24 games Release [5344 B]
Get:6 https://dl.bintray.com/grimler/science-packages-24 science Release [6191 B]
Get:4 https://dl.bintray.com/termux/termux-packages-24 stable Release [8255 B]
Get:7 https://dl.bintray.com/grimler/game-packages-24 games Release.gpg [475 B]
Get:8 https://dl.bintray.com/grimler/science-packages-24 science Release.gpg [475 B]
Get:9 https://dl.bintray.com/termux/termux-packages-24 stable Release.gpg [821 B]
Get:10 https://dl.bintray.com/grimler/game-packages-24 games/stable aarch64 Packages [3980 B]
Get:11 https://dl.bintray.com/grimler/science-packages-24 science/stable aarch64 Packages [8803 B]
Get:12 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 Packages [115 kB]
Fetched 149 kB in 7s (18.8 kB/s)
Reading package lists... Done
Building dependency tree... Done
8 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree... Done
Calculating upgrade... Done
The following packages will be upgraded:
  ca-certificates command-not-found curl
  libandroid-glob libcurl openssl termux-tools
  unzip
8 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Need to get 2518 kB of archives.
After this operation, 69.6 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 ca-certificates all 20200626 [122 kB]
Get:2 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 openssl aarch64 1.1.1g-3 [1134 kB]
Get:3 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 libcurl aarch64 7.71.0 [831 kB]
Get:4 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 curl aarch64 7.71.0 [147 kB]
Get:5 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 termux-tools all 0.83-1 [6734 B]
Get:6 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 libandroid-glob aarch64 0.6-1 [6742 B]
Get:7 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 command-not-found aarch64 1.53-1 [159 kB]
Get:8 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 unzip aarch64 6.0-6 [113 kB]
Fetched 2518 kB in 17s (140 kB/s)
(Reading database ... 3434 files and directories currently installed.)
Preparing to unpack .../ca-certificates_20200626_all.deb ...
Unpacking ca-certificates (20200626) over (20200101) ...
Setting up ca-certificates (20200626) ...
(Reading database ... 3434 files and directories currently installed.)
Preparing to unpack .../openssl_1.1.1g-3_aarch64.deb ...
Unpacking openssl (1.1.1g-3) over (1.1.1g-2) ...
Setting up openssl (1.1.1g-3) ...
(Reading database ... 3436 files and directories currently installed.)
Preparing to unpack .../libcurl_7.71.0_aarch64.deb ...
Unpacking libcurl (7.71.0) over (7.70.0-1) ...
Setting up libcurl (7.71.0) ...
(Reading database ... 3443 files and directories currently installed.)
Preparing to unpack .../curl_7.71.0_aarch64.deb ...
Unpacking curl (7.71.0) over (7.70.0-1) ...
Setting up curl (7.71.0) ...
(Reading database ... 3443 files and directories currently installed.)
Preparing to unpack .../termux-tools_0.83-1_all.deb ...
Unpacking termux-tools (0.83-1) over (0.81-3) ...
Setting up termux-tools (0.83-1) ...
(Reading database ... 3444 files and directories currently installed.)
Preparing to unpack .../libandroid-glob_0.6-1_aarch64.deb ...
Unpacking libandroid-glob (0.6-1) over (0.6) ...
Setting up libandroid-glob (0.6-1) ...
(Reading database ... 3444 files and directories currently installed.)
Preparing to unpack .../command-not-found_1.53-1_aarch64.deb ...
Unpacking command-not-found (1.53-1) over (1.52) ...
Preparing to unpack .../unzip_6.0-6_aarch64.deb ...
Unpacking unzip (6.0-6) over (6.0-5) ...
Setting up unzip (6.0-6) ...
Setting up command-not-found (1.53-1) ...
$ pkg upgrade
Ign:2 https://dl.bintray.com/grimler/game-packages-24 games InRelease
Ign:3 https://dl.bintray.com/grimler/science-packages-24 science InRelease
Ign:1 https://dl.bintray.com/termux/termux-packages-24 stable InRelease
Get:5 https://dl.bintray.com/grimler/game-packages-24 games Release [5344 B]
Hit:5 https://dl.bintray.com/grimler/game-packages-24 games Release
Get:7 https://dl.bintray.com/grimler/science-packages-24 science Release [6191 B]
Hit:7 https://dl.bintray.com/grimler/science-packages-24 science Release
Get:4 https://dl.bintray.com/termux/termux-packages-24 stable Release [8255 B]
Hit:4 https://dl.bintray.com/termux/termux-packages-24 stable Release
Reading package lists... Done
Building dependency tree
Reading state information... Done
All packages are up to date.
Reading package lists... Done
Building dependency tree
Reading state information... Done
Calculating upgrade... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
$ pkg install python
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  binutils clang gdbm glib libffi libllvm
  libsqlite make ncurses-ui-libs ndk-sysroot
  pkg-config
Suggested packages:
  python-tkinter
The following NEW packages will be installed:
  binutils clang gdbm glib libffi libllvm
  libsqlite make ncurses-ui-libs ndk-sysroot
  pkg-config python
0 upgraded, 12 newly installed, 0 to remove and 0 not upgraded.
Need to get 43.0 MB of archives.
After this operation, 253 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 binutils aarch64 2.34 [2275 kB]
Get:2 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 ndk-sysroot aarch64 20-8 [1451 kB]
Get:3 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 libffi aarch64 3.3 [28.4 kB]
Get:4 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 libllvm aarch64 9.0.1-7 [28.2 MB]
Get:5 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 clang aarch64 9.0.1-7 [736 kB]
Get:6 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 gdbm aarch64 1.18.1-3 [103 kB]
Get:7 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 glib aarch64 2.64.3-1 [1060 kB]
Get:8 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 libsqlite aarch64 3.32.3 [541 kB]
Get:9 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 make aarch64 4.3-1 [219 kB]
Get:10 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 ncurses-ui-libs aarch64 6.2.20200222 [28.9 kB]
Get:11 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 pkg-config aarch64 0.29.2 [25.9 kB]
Get:12 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 python aarch64 3.8.3-1 [8282 kB]
Fetched 43.0 MB in 1min 27s (492 kB/s)
Selecting previously unselected package binutils.
(Reading database ... 3444 files and directories currently installed.)
Preparing to unpack .../00-binutils_2.34_aarch64.deb ...
Unpacking binutils (2.34) ...
Selecting previously unselected package ndk-sysroot.
Preparing to unpack .../01-ndk-sysroot_20-8_aarch64.deb ...
Unpacking ndk-sysroot (20-8) ...
Selecting previously unselected package libffi.
Preparing to unpack .../02-libffi_3.3_aarch64.deb ...
Unpacking libffi (3.3) ...
Selecting previously unselected package libllvm.
Preparing to unpack .../03-libllvm_9.0.1-7_aarch64.deb ...
Unpacking libllvm (9.0.1-7) ...
Selecting previously unselected package clang.
Preparing to unpack .../04-clang_9.0.1-7_aarch64.deb ...
Unpacking clang (9.0.1-7) ...
Selecting previously unselected package gdbm.
Preparing to unpack .../05-gdbm_1.18.1-3_aarch64.deb ...
Unpacking gdbm (1.18.1-3) ...
Selecting previously unselected package glib.
Preparing to unpack .../06-glib_2.64.3-1_aarch64.deb ...
Unpacking glib (2.64.3-1) ...
Selecting previously unselected package libsqlite.
Preparing to unpack .../07-libsqlite_3.32.3_aarch64.deb ...
Unpacking libsqlite (3.32.3) ...
Selecting previously unselected package make.
Preparing to unpack .../08-make_4.3-1_aarch64.deb ...
Unpacking make (4.3-1) ...
Selecting previously unselected package ncurses-ui-libs.
Preparing to unpack .../09-ncurses-ui-libs_6.2.20200222_aarch64.deb ...
Unpacking ncurses-ui-libs (6.2.20200222) ...
Selecting previously unselected package pkg-config.
Preparing to unpack .../10-pkg-config_0.29.2_aarch64.deb ...
Unpacking pkg-config (0.29.2) ...
Selecting previously unselected package python.
Preparing to unpack .../11-python_3.8.3-1_aarch64.deb ...
Unpacking python (3.8.3-1) ...
Setting up gdbm (1.18.1-3) ...
Setting up ndk-sysroot (20-8) ...
Setting up binutils (2.34) ...
Setting up libsqlite (3.32.3) ...
Setting up libffi (3.3) ...
Setting up ncurses-ui-libs (6.2.20200222) ...
Setting up make (4.3-1) ...
Setting up libllvm (9.0.1-7) ...
Setting up glib (2.64.3-1) ...
Setting up python (3.8.3-1) ...
Setting up pip...
Looking in links: /data/data/com.termux/files/usr/tmp/tmp4d6cgqut
Collecting setuptools
Collecting pip
Installing collected packages: setuptools, pip
Successfully installed pip-19.2.3 setuptools-41.2.0
Setting up clang (9.0.1-7) ...
Setting up pkg-config (0.29.2) ...
$ pkg install  python2
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following NEW packages will be installed:
  python2
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 4866 kB of archives.
After this operation, 19.2 MB of additional disk space will be used.
Get:1 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 python2 aarch64 2.7.18-1 [4866 kB]
Fetched 4866 kB in 14s (329 kB/s)
Selecting previously unselected package python2.
(Reading database ... 10917 files and directories currently installed.)
Preparing to unpack .../python2_2.7.18-1_aarch64.deb ...
Unpacking python2 (2.7.18-1) ...
Setting up python2 (2.7.18-1) ...
Setting up pip2...
DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
Looking in links: /data/data/com.termux/files/usr/tmp/tmpR3NYkU
Collecting setuptools
Collecting pip
Installing collected packages: setuptools, pip
vSuccessfully installed pip-19.2.3 setuptools-41.2.0
$ pkg install git
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  pcre2
The following NEW packages will be installed:
  git pcre2
0 upgraded, 2 newly installed, 0 to remove and 0 not upgraded.
Need to get 4258 kB of archives.
After this operation, 24.8 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 pcre2 aarch64 10.35 [814 kB]
Get:2 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 git aarch64 2.27.0-3 [3444 kB]
Fetched 4258 kB in 16s (252 kB/s)
Selecting previously unselected package pcre2.
(Reading database ... 11731 files and directories currently installed.)
Preparing to unpack .../pcre2_10.35_aarch64.deb ...
Unpacking pcre2 (10.35) ...
Selecting previously unselected package git.
Preparing to unpack .../git_2.27.0-3_aarch64.deb ...
Unpacking git (2.27.0-3) ...
Setting up pcre2 (10.35) ...
Setting up git (2.27.0-3) ...
$ pip2 install requests
DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
Collecting requests
  Downloading https://files.pythonhosted.org/packages/45/1e/0c169c6a5381e241ba7404532c16a21d86ab872c9bed8bdcd4c423954103/requests-2.24.0-py2.py3-none-any.whl (61kB)
     |█████▎                          | 10kB 1.6MB     |██████████▋                     | 20kB 79kB/     |████████████████                | 30kB 74kB/     |█████████████████████▏          | 40kB 86kB/     |██████████████████████████▌     | 51kB 97kB/     |███████████████████████████████▉| 61kB 100kB     |████████████████████████████████| 71kB 112kB/s
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 (from requests)
  Downloading https://files.pythonhosted.org/packages/e1/e5/df302e8017440f111c11cc41a6b432838672f5a70aa29227bf58149dc72f/urllib3-1.25.9-py2.py3-none-any.whl (126kB)
     |██▋                             | 10kB 1.7MB     |█████▏                          | 20kB 530kB     |███████▊                        | 30kB 687kB     |██████████▍                     | 40kB 661kB     |█████████████                   | 51kB 630kB     |███████████████▌                | 61kB 457kB     |██████████████████              | 71kB 368kB     |████████████████████▊           | 81kB 356kB     |███████████████████████▎        | 92kB 344kB     |█████████████████████████▉      | 102kB 356k     |████████████████████████████▍   | 112kB 356k     |███████████████████████████████ | 122kB 356k     |████████████████████████████████| 133kB 356kB/s
Collecting chardet<4,>=3.0.2 (from requests)
  Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
     |██▌                             | 10kB 2.3MB     |█████                           | 20kB 2.2MB     |███████▍                        | 30kB 2.7MB     |█████████▉                      | 40kB 3.2MB     |████████████▎                   | 51kB 3.6MB     |██████████████▊                 | 61kB 1.5MB     |█████████████████▏              | 71kB 1.5MB     |███████████████████▋            | 81kB 1.6MB     |██████████████████████▏         | 92kB 1.6MB     |████████████████████████▋       | 102kB 1.6M     |███████████████████████████     | 112kB 1.6M     |█████████████████████████████▌  | 122kB 1.6M     |████████████████████████████████| 133kB 1.6M     |████████████████████████████████| 143kB 1.6MB/s
Collecting certifi>=2017.4.17 (from requests)
  Downloading https://files.pythonhosted.org/packages/5e/c4/6c4fe722df5343c33226f0b4e0bb042e4dc13483228b4718baf286f86d87/certifi-2020.6.20-py2.py3-none-any.whl (156kB)
     |██                              | 10kB 2.1MB     |████▏                           | 20kB 2.5MB     |██████▎                         | 30kB 2.8MB     |████████▍                       | 40kB 2.7MB     |██████████▌                     | 51kB 2.8MB     |████████████▋                   | 61kB 2.9MB     |██████████████▋                 | 71kB 3.2MB     |████████████████▊               | 81kB 3.4MB     |██████████████████▉             | 92kB 3.7MB     |█████████████████████           | 102kB 3.9M     |███████████████████████         | 112kB 3.9M     |█████████████████████████▏      | 122kB 3.9M     |███████████████████████████▏    | 133kB 3.9M     |█████████████████████████████▎  | 143kB 3.9M     |███████████████████████████████▍| 153kB 3.9M     |████████████████████████████████| 163kB 3.9MB/s
Collecting idna<3,>=2.5 (from requests)
  Downloading https://files.pythonhosted.org/packages/a2/38/928ddce2273eaa564f6f50de919327bf3a00f091b5baba8dfa9460f3a8a8/idna-2.10-py2.py3-none-any.whl (58kB)
     |█████▋                          | 10kB 3.0MB     |███████████▏                    | 20kB 2.7MB     |████████████████▊               | 30kB 3.5MB     |██████████████████████▎         | 40kB 4.1MB     |███████████████████████████▉    | 51kB 4.7MB     |████████████████████████████████| 61kB 3.4MB/s
Installing collected packages: urllib3, chardet, certifi, idna, requests
Successfully installed certifi-2020.6.20 chardet-3.0.4 idna-2.10 requests-2.24.0 urllib3-1.25.9
WARNING: You are using pip version 19.2.3, however version 20.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
$ pip2 install mechanize
DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
Collecting mechanize
  Downloading https://files.pythonhosted.org/packages/13/08/77368b47ba2f9e0c03f33902ed2c8e0fa83d15d81dcf7fe102b40778d810/mechanize-0.4.5-py2.py3-none-any.whl (109kB)
     |███                             | 10kB 1.0MB     |██████                          | 20kB 104kB     |█████████                       | 30kB 132kB     |████████████                    | 40kB 104kB     |███████████████                 | 51kB 120kB     |██████████████████              | 61kB 136kB     |█████████████████████           | 71kB 150kB     |████████████████████████        | 81kB 162kB     |███████████████████████████     | 92kB 155kB     |██████████████████████████████  | 102kB 168k     |████████████████████████████████| 112kB 168kB/s
Collecting html5lib>=0.999999999 (from mechanize)
  Downloading https://files.pythonhosted.org/packages/6c/dd/a834df6482147d48e225a49515aabc28974ad5a4ca3215c18a882565b028/html5lib-1.1-py2.py3-none-any.whl (112kB)
     |███                             | 10kB 1.7MB     |█████▉                          | 20kB 1.9MB     |████████▊                       | 30kB 2.0MB     |███████████▊                    | 40kB 1.9MB     |██████████████▋                 | 51kB 1.7MB     |█████████████████▌              | 61kB 1.4MB     |████████████████████▌           | 71kB 1.6MB     |███████████████████████▍        | 81kB 1.2MB     |██████████████████████████▎     | 92kB 1.1MB     |█████████████████████████████▏  | 102kB 1.1M     |████████████████████████████████| 112kB 1.1MB/s
Collecting six>=1.9 (from html5lib>=0.999999999->mechanize)
  Downloading https://files.pythonhosted.org/packages/ee/ff/48bde5c0f013094d729fe4b0316ba2a24774b3ff1c52d924a8a4cb04078a/six-1.15.0-py2.py3-none-any.whl
Collecting webencodings (from html5lib>=0.999999999->mechanize)
  Downloading https://files.pythonhosted.org/packages/f4/24/2a3e3df732393fed8b3ebf2ec078f05546de641fe1b667ee316ec1dcf3b7/webencodings-0.5.1-py2.py3-none-any.whl
Installing collected packages: six, webencodings, html5lib, mechanize
Successfully installed html5lib-1.1 mechanize-0.4.5 six-1.15.0 webencodings-0.5.1
WARNING: You are using pip version 19.2.3, however version 20.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
$ git clone https://github.com/niazibilal/HackerCloning into 'World'...
remote: Enumerating objects: 88, done.
remote: Counting objects: 100% (88/88), done.
remote: Compressing objects: 100% (88/88), done.
Receiving objects:  12% (124/1031), 68.01 KiB | 12Receiving objects:  13% (135/1031), 68.01 KiB | 12Receiving objects:  14% (145/1031), 68.01 KiB | 12Receiving objects:  15% (155/1031), 68.01 KiB | 12Receiving objects:  16% (165/1031), 68.01 KiB | 12Receiving objects:  17% (176/1031), 68.01 KiB | 12Receiving objects:  18% (186/1031), 68.01 KiB | 12Receiving objects:  19% (196/1031), 68.01 KiB | 12Receiving objects:  20% (207/1031), 68.01 KiB | 12Receiving objects:  21% (217/1031), 68.01 KiB | 12Receiving objects:  22% (227/1031), 68.01 KiB | 12Receiving objects:  23% (238/1031), 68.01 KiB | 12Receiving objects:  24% (248/1031), 68.01 KiB | 12Receiving objects:  25% (258/1031), 68.01 KiB | 12Receiving objects:  25% (265/1031), 148.01 KiB | 1Receiving objects:  26% (269/1031), 148.01 KiB | 1Receiving objects:  27% (279/1031), 148.01 KiB | 1Receiving objects:  28% (289/1031), 148.01 KiB | 1Receiving objects:  29% (299/1031), 148.01 KiB | 1Receiving objects:  30% (310/1031), 148.01 KiB | 1Receiving objects:  31% (320/1031), 148.01 KiB | 1Receiving objects:  32% (330/1031), 148.01 KiB | 1Receiving objects:  32% (340/1031), 340.01 KiB | 1Receiving objects:  33% (341/1031), 452.01 KiB | 1Receiving objects:  34% (351/1031), 452.01 KiB | 1Receiving objects:  35% (361/1031), 452.01 KiB | 1Receiving objects:  36% (372/1031), 452.01 KiB | 1Receiving objects:  37% (382/1031), 452.01 KiB | 1Receiving objects:  38% (392/1031), 452.01 KiB | 1Receiving objects:  39% (403/1031), 452.01 KiB | 1Receiving objects:  39% (410/1031), 580.01 KiB | 1Receiving objects:  39% (410/1031), 868.01 KiB | 1Receiving objects:  39% (410/1031), 1.02 MiB | 208Receiving objects:  39% (410/1031), 1.46 MiB | 264Receiving objects:  39% (410/1031), 2.06 MiB | 351Receiving objects:  39% (410/1031), 2.46 MiB | 391Receiving objects:  39% (410/1031), 3.05 MiB | 451Receiving objects:  39% (410/1031), 3.10 MiB | 349Receiving objects:  39% (410/1031), 3.91 MiB | 377Receiving objects:  39% (410/1031), 4.27 MiB | 381Receiving objects:  39% (410/1031), 4.99 MiB | 415Receiving objects:  39% (410/1031), 5.32 MiB | 385Receiving objects:  39% (410/1031), 5.33 MiB | 355Receiving objects:  39% (410/1031), 5.96 MiB | 398Receiving objects:  39% (410/1031), 6.43 MiB | 467Receiving objects:  39% (410/1031), 6.82 MiB | 393Receiving objects:  39% (410/1031), 7.14 MiB | 391Receiving objects:  39% (410/1031), 7.59 MiB | 401Receiving objects:  39% (410/1031), 7.82 MiB | 341Receiving objects:  39% (410/1031), 7.97 MiB | 323Receiving objects:  39% (410/1031), 8.13 MiB | 251Receiving objects:  39% (410/1031), 8.40 MiB | 278Receiving objects:  39% (410/1031), 8.62 MiB | 241Receiving objects:  39% (410/1031), 8.90 MiB | 232Receiving objects:  39% (411/1031), 9.01 MiB | 231Receiving objects:  40% (413/1031), 9.01 MiB | 231Receiving objects:  41% (423/1031), 9.01 MiB | 231Receiving objects:  42% (434/1031), 9.01 MiB | 231Receiving objects:  43% (444/1031), 9.01 MiB | 231Receiving objects:  44% (454/1031), 9.01 MiB | 231Receiving objects:  44% (459/1031), 9.13 MiB | 197Receiving objects:  45% (464/1031), 9.13 MiB | 197Receiving objects:  46% (475/1031), 9.13 MiB | 197Receiving objects:  47% (485/1031), 9.13 MiB | 197Receiving objects:  48% (495/1031), 9.13 MiB | 197Receiving objects:  49% (506/1031), 9.13 MiB | 197Receiving objects:  50% (516/1031), 9.13 MiB | 197Receiving objects:  51% (526/1031), 9.13 MiB | 197Receiving objects:  52% (537/1031), 9.13 MiB | 197Receiving objects:  53% (547/1031), 9.13 MiB | 197Receiving objects:  54% (557/1031), 9.13 MiB | 197Receiving objects:  55% (568/1031), 9.13 MiB | 197Receiving objects:  56% (578/1031), 9.13 MiB | 197Receiving objects:  57% (588/1031), 9.13 MiB | 197Receiving objects:  58% (598/1031), 9.13 MiB | 197Receiving objects:  59% (609/1031), 9.13 MiB | 197Receiving objects:  60% (619/1031), 9.13 MiB | 197Receiving objects:  61% (629/1031), 9.13 MiB | 197Receiving objects:  62% (640/1031), 9.13 MiB | 197Receiving objects:  63% (650/1031), 9.13 MiB | 197Receiving objects:  64% (660/1031), 9.13 MiB | 197Receiving objects:  65% (671/1031), 9.13 MiB | 197Receiving objects:  66% (681/1031), 9.13 MiB | 197Receiving objects:  67% (691/1031), 9.13 MiB | 197Receiving objects:  68% (702/1031), 9.13 MiB | 197Receiving objects:  69% (712/1031), 9.13 MiB | 197Receiving objects:  70% (722/1031), 9.13 MiB | 197Receiving objects:  71% (733/1031), 9.13 MiB | 197Receiving objects:  72% (743/1031), 9.13 MiB | 197Receiving objects:  73% (753/1031), 9.13 MiB | 197Receiving objects:  74% (763/1031), 9.13 MiB | 197Receiving objects:  75% (774/1031), 9.13 MiB | 197Receiving objects:  76% (784/1031), 9.13 MiB | 197Receiving objects:  77% (794/1031), 9.13 MiB | 197Receiving objects:  78% (805/1031), 9.13 MiB | 197Receiving objects:  79% (815/1031), 9.13 MiB | 197Receiving objects:  80% (825/1031), 9.13 MiB | 197Receiving objects:  81% (836/1031), 9.13 MiB | 197Receiving objects:  82% (846/1031), 9.13 MiB | 197Receiving objects:  83% (856/1031), 9.13 MiB | 197Receiving objects:  84% (867/1031), 9.13 MiB | 197Receiving objects:  85% (877/1031), 9.13 MiB | 197Receiving objects:  86% (887/1031), 9.13 MiB | 197remote: Total 1031 (delta 53), reused 0 (delta 0), pack-reused 943
Receiving objects:  87% (897/1031), 9.13 MiB | 197Receiving objects:  88% (908/1031), 9.13 MiB | 197Receiving objects:  89% (918/1031), 9.13 MiB | 197Receiving objects:  90% (928/1031), 9.13 MiB | 197Receiving objects:  91% (939/1031), 9.13 MiB | 197Receiving objects:  92% (949/1031), 9.13 MiB | 197Receiving objects:  93% (959/1031), 9.13 MiB | 197Receiving objects:  94% (970/1031), 9.13 MiB | 197Receiving objects:  95% (980/1031), 9.13 MiB | 197Receiving objects:  96% (990/1031), 9.13 MiB | 197Receiving objects:  97% (1001/1031), 9.13 MiB | 19Receiving objects:  98% (1011/1031), 9.13 MiB | 19Receiving objects:  99% (1021/1031), 9.13 MiB | 19Receiving objects: 100% (1031/1031), 9.13 MiB | 19Receiving objects: 100% (1031/1031), 9.34 MiB | 325.00 KiB/s, done.
Resolving deltas: 100% (412/412), done.
$ cd Hacker
$ python2 Niazihacker.py
