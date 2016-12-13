install
text
reboot

# Need to set the IP address for the image to ftp.wicks.co.nz manually
# because Cisco AnyConnect seems to disable DNS
url --url=http://103.247.152.85/pub/linux/dist/centos/6/os/x86_64/
repo --name=nzgl-stable --baseurl=http://10.10.2.50/nzgl-stable

lang en_US.UTF-8
keyboard us
network --onboot yes --device eth0 --bootproto dhcp
# root password will be ChangeMeNow
rootpw --iscrypted $1$thfc41$dgkI90H8xqOz61ha8zuyF.
selinux --disabled
timezone --utc Pacific/Auckland
zerombr
bootloader --location=mbr --append="rd_NO_PLYMOUTH"
clearpart --all

part / --fstype=ext4 --grow --asprimary --size=200

%packages --nobase
coreutils
yum
rpm
e2fsprogs
ftp
grub
openssh-server
openssh-clients
dhclient
ntp
yum-presto
yum-changelog
yum-utils
xauth
bind-utils
wget
man
screen
evince
blas
emacs
nfs-utils
gedit
mc
libreoffice
valgrind
cpan
cmake
glibc-static
glib2-devel
bzip2-devel
python-devel
python-argparse
python-backports
ius-release
libcurl
boost-devel
libxml2-devel
libXp-devel
ncurses-devel
nautilus-open-terminal
environment-modules
perl-Bio-SamTools
perl-Filesys-Df
perl-DBD-MySQL
perl-Module-Build
python-matplotlib
nzgl-release
nzgl-sysscripts-appliance
postgresql-libs
postgresql-devel
mysql-devel
xorg-x11-fonts-100dpi
xorg-x11-fonts-75dpi
tmpwatch
vim-enhanced
tk
@Development tools
@NZGL
@Internet Browser
@Desktop
@Desktop Platform
@X Window System
%end

%post --logfile /root/post.log

# Standard directories
mkdir /active 
mkdir /archive 
mkdir /scratch
mkdir /databases
mkdir /home/qiime
mkdir /home/R-network

# Create standard R links
# ln -s /home/R-network/R-2/bin/R /usr/bin/R2
# ln -s /home/R-network/R-2/bin/Rscript /usr/bin/Rscript2
# ln -s /home/R-network/R-3/bin/R /usr/bin/R3
# ln -s /home/R-network/R-3/bin/Rscript /usr/bin/Rscript3

# Upgrade packages
/usr/sbin/nzgl-yum-upgrade

# 32 bit binary support
yum -y install glibc.i686 libstdc++.i686 libgomp.i686

# Java 7 development support
yum -y install java-1.7.0-openjdk-devel ant

# Java 8 development support
yum -y install java-1.8.0-openjdk-devel ant

# Set Java 8 as default
alternatives --set java /usr/lib/jvm/jre-1.8.0-openjdk.x86_64/bin/java

# Set runlevel 5
sed 's/id:3:initdefault:/id:5:initdefault:/g' --in-place /etc/inittab

# Add packages to /etc/hosts
echo '10.10.2.50 packages packages.genomics.local' >> /etc/hosts

# Set hostname to nzglapp
sed 's/localhost.localdomain/nzglapp/g' --in-place /etc/sysconfig/network

# Install R-core dummy package and rstudio
yum -y install R-core rstudio

# Install extra fonts
yum -y install msttcorefonts
# Install htop
yum -y install htop

%end
