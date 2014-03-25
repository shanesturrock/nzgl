install
text
reboot

url --url=http://ftp.wicks.co.nz/pub/linux/dist/centos/6/os/x86_64/
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
xauth
bind-utils
wget
man
screen
evince
emacs
nfs-utils
gedit
libreoffice
valgrind
rstudio
cpan
cmake
python-argparse
libcurl-devel
libxml2-devel
perl-Bio-SamTools
perl-Module-Build
nzgl-release
nzgl-sysscripts-appliance
@Development tools
@NZGL
@Internet Browser
@Desktop
%end

%post --logfile /root/post.log

# Standard directories
mkdir /active 
mkdir /archive 
mkdir /scratch
mkdir /databases
mkdir /home/qiime
mkdir /home/R-network

# Install R packages
ln -s /home/R-network/R-2/bin/R /usr/bin/R2
ln -s /home/R-network/R-2/bin/Rscript /usr/bin/Rscript2
ln -s /home/R-network/R-3/bin/R /usr/bin/R3
ln -s /home/R-network/R-3/bin/Rscript /usr/bin/Rscript3
wget http://10.10.2.50/R-2.15.3.tgz
tar -xvf /home/R-network R-2.15.3.tgz
wget http://10.10.2.50/R-3.0.3.tgz
tar -xvf /home/R-network R-3.0.3.tgz
ln -s /home/R-network/R-2 /home/R-network/R-2.15.3
ln -s /home/R-network/R-3 /home/R-network/R-3.0.3

# Install qiime isn't practical here since it is 1.1GB

# Upgrade packages
/usr/sbin/nzgl-yum-upgrade

# 32 bit binary support
yum -y install glibc.i686 libstdc++.i686 libgomp.i686

# Java 7 development support
yum -y install java-1.7.0-openjdk-devel ant

# Process Accounting
yum -y install psacct
chkconfig psacct on

# Set runlevel 5
sed 's/id:3:initdefault:/id:5:initdefault:/g' --in-place /etc/inittab

# Add packages to /etc/hosts
echo '10.10.2.50 packages packages.genomics.local' >> /etc/hosts

# Set hostname to nzglapp
sed 's/localhost.localdomain/nzglapp/g' --in-place /etc/sysconfig/network

%end
