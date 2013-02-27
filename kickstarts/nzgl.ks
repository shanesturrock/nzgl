install
text
reboot

url --url=http://mirrors.biomatters.com/mirrors/CentOS/6/os/x86_64/
repo --name=nzgl-stable --baseurl=http://nzglrepo.biomatters.com/nzgl-stable

lang en_US.UTF-8
keyboard us
network --onboot yes --device eth0 --bootproto dhcp
rootpw --iscrypted $1$g7II31$SBWELk3Sch95R2adstVjE0
skipx
authconfig --enableshadow --passalgo=sha512 --enableldap --enableldapauth --ldapserver=ldaps://ldap.biomatters.com --ldapbasedn="dc=biomatters,dc=com" --enablesssd --enablesssdauth --update
selinux --disabled
timezone NZ
zerombr
bootloader --location=mbr --append="rd_NO_PLYMOUTH"
clearpart --all

part / --fstype=ext4 --grow --asprimary --size=200

%packages --nobase
coreutils
yum
rpm
e2fsprogs
grub
openssh-server
openssh-clients
dhclient
ntp
yum-presto
xauth
bind-utils
wget
man
screen
nfs-utils
pam_ldap
sssd
nx
freenx
yum-plugin-post-transaction-actions
munin-node
rstudio
cpan
perl-Bio-SamTools
perl-Module-Build
nzgl-release
#nzgl-rhn-release
nzgl-sysscripts
@Development tools
@NZGL
@Internet Browser
@Desktop
%end

%post --logfile /root/post.log

nfs_host="192.168.30.55"
ntp_servers="0.rhel.pool.ntp.org 1.rhel.pool.ntp.org 2.rhel.pool.ntp.org"

# NFS 
echo "${nfs_host}:/home /home nfs rw,hard,intr,rsize=8192,wsize=8192 0 0" >> /etc/fstab

# SSH
sed 's/GSSAPIAuthentication yes/GSSAPIAuthentication no/g' --in-place /etc/ssh/sshd_config
sed 's/#PermitRootLogin yes/PermitRootLogin no/g' --in-place /etc/ssh/sshd_config
sed 's/PasswordAuthentication yes/PasswordAuthentication no/g' --in-place /etc/ssh/sshd_config
sed 's/#MaxAuthTries 6/MaxAuthTries 3/g' --in-place /etc/ssh/sshd_config
echo "AllowGroups biomatters munin nx $(hostname)" >> /etc/ssh/sshd_config

# PAM/LDAP host restriction
# sed 's/#pam_check_host_attr yes/pam_check_host_attr yes/g' --in-place /etc/pam_ldap.conf
# SSSD allow self-signed certs for testing only
sed 's/\[sssd\]/ldap_tls_reqcert = never \n\[sssd\]/g' --in-place /etc/sssd/sssd.conf
sed 's/#tls_checkpeer yes/tls_checkpeer no/g' --in-place /etc/pam_ldap.conf

# Sudoers
echo '%biomatters ALL=(ALL) ALL' >> /etc/sudoers

#NX
sed 's/#ENABLE_SSH_AUTHENTICATION="1"/ENABLE_SSH_AUTHENTICATION="1"/g' --in-place /etc/nxserver/node.conf
#nxsetup --install --clean --purge --setup-nomachine-key --ignore-errors
# Allow password authentication from localhost (else NX can't authenticate)
echo 'Match Address 127.0.0.1,::1
  PasswordAuthentication yes' >> /etc/ssh/sshd_config

# SNMP
#master_ipv4="192.168.30.106"
# Our test IPv6 range is fd46:af09:3ae3::/48
#master_ipv6="fd46:af09:3ae3::10"
#echo "sysservices 72
#sysContact nzgl@biomatters.com
#sysLocation NZGL
#agentaddress udp:161,udp6:161,tcp:161,tcp6:161
#rocommunity nzgl_pub ${master_ipv4}
#rocommunity6 nzgl_pub ${master_ipv6}
#disk  /" > /etc/snmp/snmpd.conf
#chkconfig snmpd on

# NTP
[ -e /etc/ntp.conf ] && mv /etc/ntp.conf /etc/ntp.conf.orig
echo "driftfile /var/lib/ntp/drift" > /etc/ntp.conf
for ntp_server in ${ntp_servers}; do
	echo "server ${ntp_server}" >> /etc/ntp.conf
done

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

# Upgrade packages
/usr/sbin/nzgl-yum-upgrade

# Configure services
/usr/sbin/nzgl-configure-services

# Configure java
/usr/sbin/nzgl-configure-java

# Firewall setup
yum -y install nzgl-iptables

%end
