### install strip command line 
* Add Bintray’s GPG key to the apt sources keyring.   
`sudo apt-key adv --keyserver hkp://pool.sks-keyservers.net:80 --recv-keys 379CE192D401AB61`   
* Add stripe-cli’s apt repository to the apt sources list.   
`echo "deb https://dl.bintray.com/stripe/stripe-cli-deb stable main" | sudo tee -a /etc/apt/sources.list`   
* Update the package list   
`sudo apt-get update`   
* Install the CLI  
`sudo apt-get install stripe`

### Login with your Stripe account  
* installing the Stripe CLI, you must pair it with your Stripe account. run    
`stripe login`   
* You’ll be prompted to launch your browser and login to the Stripe Dashboard to grant the Stripe CLI access to your account.
```` 
(python_virtual3.8) maaz@maaz-Lenovo-G50-70:~/github/python/payment_strip$ stripe login
Your pairing code is: solid-glory-bravo-fame
This pairing code verifies your authentication with Stripe.
Press Enter to open the browser (^C to quit)
> Done! The Stripe CLI is configured for your account with account id acct_1IBtOyFLebDPRWT7

Please note: this key will expire after 90 days, at which point you'll need to re-authenticate.
````
### error at install strip 
1. Sub-process /usr/bin/dpkg returned an error code (1)
```` 
(python_virtual3.8) maaz@maaz-Lenovo-G50-70:~/github/python/payment_strip$ sudo apt-get install stripe
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  autotools-dev command-not-found-data dh-python diffstat fonts-lato g++-7 gdal-data gfortran gfortran-9 gir1.2-gtksource-3.0 gir1.2-harfbuzz-0.0
  gir1.2-mutter-2 gnome-software-common gnome-user-guide gsfonts guile-2.0-libs hplip-data ibverbs-providers iputils-arping javascript-common libaacs0
  libaec0 libappstream-glib8 libapt-pkg-perl libarchive-zip-perl libargon2-0 libart-2.0-2 libasync-mergepoint-perl libavutil55 libb-hooks-op-check-perl
  libbdplus0 libblkid-dev libbluray2 libboost-date-time1.65.1 libboost-iostreams1.65.1 libboost-system1.65.1 libcamel-1.2-61 libcapture-tiny-perl
  libcdio-cdda2 libcdio-paranoia2 libcdio18 libcgi-pm-perl libcharls1 libcharls2 libclass-accessor-perl libclass-method-modifiers-perl
  libclass-xsaccessor-perl libclone-perl libcoarrays-dev libcommon-sense-perl libcrystalhd3 libdc1394-22 libdevel-size-perl libdns-export1100
  libecal-1.2-19 libedataserver-1.2-23 libenchant1c2a libepsilon1 libevent-2.1-6 libevent-core-2.1-7 libevent-dev libevent-extra-2.1-7
  libevent-openssl-2.1-7 libevent-pthreads-2.1-7 libexempi3 libexiv2-14 libexporter-tiny-perl libfftw3-double3 libfile-copy-recursive-perl
  libfont-ttf-perl libfreexl1 libfuture-perl libgail-3-0 libgdcm2.8 libgdcm3.0 libgeos-3.6.2 libgeos-3.8.0 libgeotiff2 libgeotiff5 libgfortran-9-dev
  libgfortran5 libgl2ps1.4 libgme0 libgmime-3.0-0 libgnome-desktop-3-17 libgspell-1-1 libgtksourceview-3.0-1 libgtksourceview-3.0-common
  libgutenprint-common libgutenprint2 libgutenprint9 libharfbuzz-gobject0 libhdf4-0-alt libhogweed4 libhpmud0 libhunspell-1.6-0 libhwloc15 libhwloc5
  libibverbs-dev libibverbs1 libilmbase12 libilmbase24 libimagequant0 libio-async-loop-epoll-perl libio-async-perl libio-pty-perl libio-string-perl
  libip4tc0 libipc-run-perl libiptc0 libisc-export169 libisc169 libisccc160 libisl19 libjs-jquery libjs-underscore libjson-c3 libjson-xs-perl
  liblinux-epoll-perl liblist-compare-perl liblist-moreutils-perl libllvm10:i386 liblouis14 liblqr-1-0 liblwres160 libminiupnpc10 libminizip1
  libmozjs-52-0 libmutter-2-0 libmysqlclient20 libncurses5 libnetpbm10 libnettle6 libnfs13 libnl-3-dev libnl-route-3-dev liboauth0 libogdi3.2 libopenexr22
  libopenexr24 libpackage-stash-xs-perl libparse-debianchangelog-perl libpath-tiny-perl libpcre2-dev libpcre2-posix2 libpcre32-3 libpcrecpp0v5
  libperlio-gzip-perl libplymouth4 libproj12 libproj15 libpsm-infinipath1 libpsm2-2 libpython-all-dev libpython3-dev libpython3.6-dev libqhull7 libqpdf21
  libqscintilla2-qt5-13 libraw16 libreadonly-perl libref-util-perl libref-util-xs-perl libreoffice-avmedia-backend-gstreamer libreoffice-style-galaxy
  librole-tiny-perl libruby2.7 libsane-hpaio libsane1 libselinux1-dev libsepol1-dev libsereal-decoder-perl libsereal-encoder-perl libsereal-perl
  libsocket++1 libstdc++-7-dev libstrictures-perl libstruct-dumb-perl libsub-identify-perl libsub-quote-perl libswresample2 libswscale4 libtest-fatal-perl
  libtest-refcount-perl libtext-levenshtein-perl libtype-tiny-xs-perl libtypes-serialiser-perl libunicode-utf8-perl libusbmuxd4 libvpx5 libx264-152
  libx265-146 libxml-simple-perl libxml-writer-perl libxnvctrl0 libyaml-libyaml-perl libzeitgeist-2.0-0 multiarch-support netpbm openmpi-common patchutils
  php-cli-prompt php-symfony-debug printer-driver-gutenprint printer-driver-hpcups printer-driver-postscript-hp proj-bin proj-data python-all
  python-all-dev python-asn1crypto python-cffi-backend python-crypto python-dbus python-enum34 python-gi python-idna python-pkg-resources
  python-setuptools python-six python-wheel python-xdg python3-oauth python3-renderpm python3-reportlab-accel qpdf rake ruby ruby-did-you-mean
  ruby-minitest ruby-net-telnet ruby-power-assert ruby-test-unit ruby-xmlrpc ruby2.7 rubygems-integration t1utils ubuntu-system-service uuid-dev
  xserver-xorg-core-hwe-18.04 xserver-xorg-hwe-18.04 xserver-xorg-input-all-hwe-18.04 xserver-xorg-input-libinput-hwe-18.04
  xserver-xorg-input-wacom-hwe-18.04 xserver-xorg-legacy-hwe-18.04 xserver-xorg-video-all-hwe-18.04 xserver-xorg-video-amdgpu-hwe-18.04
  xserver-xorg-video-fbdev-hwe-18.04 xserver-xorg-video-intel-hwe-18.04 xserver-xorg-video-nouveau-hwe-18.04 xserver-xorg-video-qxl-hwe-18.04
  xserver-xorg-video-vmware-hwe-18.04
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed:
  stripe
0 upgraded, 1 newly installed, 0 to remove and 32 not upgraded.
Need to get 6,531 kB of archives.
After this operation, 18.5 MB of additional disk space will be used.
Get:1 https://dl.bintray.com/stripe/stripe-cli-deb stable/main amd64 stripe amd64 1.5.7 [6,531 kB]
Fetched 6,531 kB in 1min 14s (88.4 kB/s)                                                                                                                   
Selecting previously unselected package stripe.
(Reading database ... 241555 files and directories currently installed.)
Preparing to unpack .../stripe_1.5.7_amd64.deb ...
Unpacking stripe (1.5.7) ...
Setting up stripe (1.5.7) ...
/var/lib/dpkg/info/stripe.postinst: 3: stripe: not found
dpkg: error processing package stripe (--configure):
 installed stripe package post-installation script subprocess returned error exit status 127
Errors were encountered while processing:
 stripe
E: Sub-process /usr/bin/dpkg returned an error code (1)
````   
#### solve installation problem 
1. If the package installation process is stopped or interrupted in mid-way, the dpkg database might be corrupted.      
Reconfiguring dpkg database may solve this issue.
```
(python_virtual3.8) maaz@maaz-Lenovo-G50-70:~/github/python$ sudo dpkg --configure -a
[sudo] password for maaz: 
Setting up stripe (1.5.7) ...
❤ Thanks for installing the Stripe CLI! To get started, run `stripe login`
```