install
text
reboot

url --url=http://packages.genomics.local/mirrors/CentOS/6/os/x86_64/
repo --name=nzgl-stable --baseurl=http://packages.genomics.local/nzgl-stable

lang en_US.UTF-8
keyboard us
network --onboot yes --device eth0 --bootproto dhcp
rootpw --iscrypted $1$thfc41$XIkOu/l/lKZvvRO6WMDgy.
skipx
authconfig --enableldap --disableldapauth --ldapserver=ldap://genomics.local --ldapbasedn="dc=genomics,dc=local" --enablesssd --enablesssdauth --enablekrb5 --krb5kdc=genomics.local --krb5realm=GENOMICS.LOCAL --krb5adminserver=genomics.local --updateall
selinux --disabled
timezone --utc Pacific/Auckland
zerombr
bootloader --location=mbr --append="rd_NO_PLYMOUTH"
clearpart --all

part / --fstype=ext4 --grow --asprimary --size=200

%packages --nobase
authconfig
system-config-firewall-base
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
blas-devel
lapack-devel
gd-devel
nfs-utils
pam_ldap
pam_krb5
krb5-workstation
sssd
nx
freenx
gedit
nano
mc
libreoffice
yum-plugin-post-transaction-actions
yum-utils
munin-node
valgrind
cpan
cmake
glibc-static
glib2-devel
python-devel
python-argparse
python-backports
libcurl
ius-release
boost-devel
libxml2-devel
ncurses-devel
nautilus-open-terminal
perl-Bio-SamTools
perl-DBD-MySQL
perl-Module-Build
nzgl-release
nzgl-sysscripts
postgresql-libs
postgresql-devel
python-matplotlib
libXp-devel
mysql-devel
sqlite-devel
environment-modules
tmpwatch
xorg-x11-fonts-100dpi
xorg-x11-fonts-75dpi
vim-enhanced
tk
@Development tools
@NZGL
@Internet Browser
@Desktop
%end

%post --logfile /root/post.log

nfs_host="stn.genomics.local"
nfs_host2="stn03.genomics.local"
ntp_servers="10.0.1.1 10.10.0.3"

# NTP
/sbin/service ntpd stop
[ -e /etc/ntp.conf ] && mv /etc/ntp.conf /etc/ntp.conf.orig
echo "driftfile /var/lib/ntp/drift" > /etc/ntp.conf
for ntp_server in ${ntp_servers}; do
	echo "server ${ntp_server}" >> /etc/ntp.conf
done
/sbin/service ntpd start

# NFS 
mkdir /active 
mkdir /archive 
mkdir /scratch
mkdir /databases
mkdir /home/shane
mkdir /home/simon
mkdir /home/sidney
mkdir /home/qiime
mkdir /home/R-network
mkdir /home/rtg
mkdir -p /home/galaxy/upload

echo "${nfs_host}:/fs1/home/shane /home/shane nfs rw,hard,intr,rsize=32768,wsize=32768 0 0" >> /etc/fstab
echo "${nfs_host}:/fs1/home/simon /home/simon nfs rw,hard,intr,rsize=32768,wsize=32768 0 0" >> /etc/fstab
echo "${nfs_host}:/fs1/home/sidney /home/sidney nfs rw,hard,intr,rsize=32768,wsize=32768 0 0" >> /etc/fstab
echo "${nfs_host}:/fs1/home/qiime /home/qiime nfs rw,hard,intr,rsize=32768,wsize=32768 0 0" >> /etc/fstab
echo "${nfs_host}:/fs1/home/R-network /home/R-network nfs rw,hard,intr,rsize=32768,wsize=32768 0 0" >> /etc/fstab
echo "${nfs_host}:/fs1/home/rtg /home/rtg nfs rw,hard,intr,rsize=32768,wsize=32768 0 0" >> /etc/fstab
echo "${nfs_host}:/fs1/home/galaxy/upload /home/galaxy/upload nfs rw,hard,intr,rsize=32768,wsize=32768 0 0" >> /etc/fstab
echo "${nfs_host2}:/fs1/databases /databases nfs rw,hard,intr,rsize=32768,wsize=32768 0 0" >> /etc/fstab
# echo "${nfs_host}:/fs1/archive /archive nfs rw,hard,intr,rsize=32768,wsize=32768 0 0" >> /etc/fstab
# echo "${nfs_host}:/fs1/active /active nfs rw,hard,intr,rsize=32768,wsize=32768 0 0" >> /etc/fstab
# echo "${nfs_host}:/fs1/scratch /scratch nfs rw,hard,intr,rsize=32768,wsize=32768 0 0" >> /etc/fstab

# Set 500GB max file size limit
echo "*	hard	fsize	512000000" >> /etc/security/limits.conf

# SSH
sed 's/GSSAPIAuthentication yes/GSSAPIAuthentication no/g' --in-place /etc/ssh/sshd_config
sed 's/#PermitRootLogin yes/PermitRootLogin no/g' --in-place /etc/ssh/sshd_config
sed 's/PasswordAuthentication yes/PasswordAuthentication no/g' --in-place /etc/ssh/sshd_config
sed 's/#MaxAuthTries 6/MaxAuthTries 3/g' --in-place /etc/ssh/sshd_config
echo "AllowGroups Biomatters munin nx $(hostname)" >> /etc/ssh/sshd_config

# motd
# suppress ssh display of motd because it will be displayed by all bash shells
sed 's/#PrintMotd yes/PrintMotd no/g' --in-place /etc/ssh/sshd_config
# bash shells will display motd as served by central.genomics.local web server
echo "curl -m 3 -f -s http://central.genomics.local/motd" > /etc/profile.d/motd.sh

# AD authentication
authconfig --enableshadow --passalgo=sha512 --enableldap --enableldapauth --ldapserver=ldap://genomics.local --ldapbasedn="dc=genomics,dc=local" --enablesssd --enablesssdauth --enablekrb5 --krb5kdc=genomics.local --krb5realm=GENOMICS.LOCAL --krb5adminserver=genomics.local --update
touch /etc/sssd/sssd.conf
sed 's/\[sssd\]/ldap_default_bind_dn = cn=svc_linux,ou=Service Accounts,ou=Special Accounts,ou=IAAS,dc=genomics,dc=local\nldap_default_authtok = Laptip23\nldap_schema = ad\nldap_user_principal = nosuchattribute\nentry_cache_timeout = 300\n\[sssd\]/g' --in-place /etc/sssd/sssd.conf
echo 'binddn CN=svc_linux,OU=Service Accounts,OU=Special Accounts,OU=IAAS,DC=genomics,DC=local
bindpw Laptip23' >> /etc/pam_ldap.conf
sed 's/dns_lookup_realm = false/dns_lookup_realm = true/g' --in-place /etc/krb5.conf 
sed 's/dns_lookup_kdc = false/dns_lookup_kdc = true/g' --in-place /etc/krb5.conf 


# Sudoers
echo '%Biomatters ALL=(ALL) ALL' >> /etc/sudoers

#NX
sed 's/#ENABLE_SSH_AUTHENTICATION="1"/ENABLE_SSH_AUTHENTICATION="1"/g' --in-place /etc/nxserver/node.conf
sed 's/#DISPLAY_BASE=1000/DISPLAY_BASE=1001/g' --in-place /etc/nxserver/node.conf
#nxsetup --install --clean --purge --setup-nomachine-key --ignore-errors
# Allow password authentication from localhost (else NX can't authenticate)
echo 'Match Address 127.0.0.1,::1
  PasswordAuthentication yes' >> /etc/ssh/sshd_config


# Munin
chkconfig --add munin-node
chkconfig munin-node on
chsh -s /bin/bash munin
mkdir -m 0700 /var/lib/munin/.ssh
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAvMI275mOlgGSj1xusO4HzS7uktCfvfqVNILxAFV/I0DtDAhtS27/KSlWeRA0NMHK8xM/sn8XWe0xePO89q+6u31QWg6KQSH8Fg7ovlOSVk3T6Tur8lL/nwEc3ommTMzzTTs5dO5jBVUtOB41DPMLkXv8+QiVE3ZU1H+FIbpIqcXUp66lyDeQPibugwmU17zAhI+gdLEo0q2f9TkUDTgqicC97xnfMqc7VyqH3kJMT39TM/d7MgdomUYtLeLb1Y640wmW0oGrC3o6HOT1ACYEi9xc8lvFBXTO/6+MIhjflznHXki60iUbYpPk3VWay+1ovNBbAKLU3bQ+N668Y2IsnQ== munin master' > /var/lib/munin/.ssh/authorized_keys
chown -R munin:munin /var/lib/munin/.ssh/
chmod 600 /var/lib/munin/.ssh/authorized_keys
sed s='fuse.gvfs-fuse-daemon'='fuse.gvfs-fuse-daemon tmpfs'=g --in-place /etc/munin/plugin-conf.d/df

# Munin plugins
/bin/rm /etc/munin/plugins/*
plugins='cpu df df_inode diskstats load memory netstat processes proc_pri swap threads uptime users vmstat'
for plugin in ${plugins}; do
	ln -sf /usr/share/munin/plugins/${plugin} /etc/munin/plugins/${plugin} 
done
ln -sf /usr/share/munin/plugins/if_ /etc/munin/plugins/if_eth0

# Remove unnecessary firmware packages
rpm -e $(rpm -qa | grep -i \\-firmware | grep -v kernel-firmware)

# Set CentOS repos
echo '[base]
name=CentOS-$releasever - Base
baseurl=http://packages.genomics.local/mirrors/CentOS/$releasever/os/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6

#released updates 
[updates]
name=CentOS-$releasever - Updates
baseurl=http://packages.genomics.local/mirrors/CentOS/$releasever/updates/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6

#additional packages that may be useful
[extras]
name=CentOS-$releasever - Extras
baseurl=http://packages.genomics.local/mirrors/CentOS/$releasever/extras/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6' > /etc/yum.repos.d/CentOS-Base.repo

# Upgrade packages
/usr/sbin/nzgl-yum-upgrade

# Configure services
/usr/sbin/nzgl-configure-services

# Configure java
# /usr/sbin/nzgl-configure-java

# Firewall setup
yum -y install nzgl-iptables

# Set the nzgl.cron job to run at a random time after 4am
sed -e 's/0/'$((RANDOM%60))'/g' --in-place /etc/cron.d/nzgl.cron

# Fix NX keyboard map problem and set it up
touch /usr/share/X11/xkb/keymap.dir
nxsetup --install --clean --purge --setup-nomachine-key --ignore-errors

# 32 bit binary support
yum -y install glibc.i686 libstdc++.i686 libgomp.i686

# Java 7 development support
yum -y install java-1.7.0-openjdk-devel ant

# Java 8 development support
yum -y install java-1.8.0-openjdk-devel

# Process Accounting
yum -y install psacct
chkconfig --add psacct
chkconfig psacct on

# Install R-core dummy package and rstudio
yum -y install R-core rstudio

# Fix yum
sed '/gpgkey/{/gpgkey/s/$/\'$'\n''#exclude = kernel*,libXfixes*/;}' --in-place /etc/yum.repos.d/CentOS-Base.repo

#Fix NX libXfixes issue
# yum --releasever=6.5 downgrade libXfixes

# Install extra fonts
yum -y install msttcorefonts
# Install htop
yum -y install htop

# Symlink to rtg tools
ln -s /home/rtg/rtg-core-current/rtg /usr/bin/rtg
