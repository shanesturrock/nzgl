install
text
#cdrom
reboot

url --url=http://nzglrepo.biomatters.com/rhel-x86_64-server-6
repo --name=nzgl-stable --baseurl=http://nzglrepo.biomatters.com/nzgl-stable
repo --name=rhel-optional --baseurl=http://nzglrepo.biomatters.com/rhel-x86_64-server-optional-6

lang en_US.UTF-8
keyboard us
network --onboot yes --device eth0 --bootproto dhcp
rootpw --iscrypted $6$/c8wetYVjfiZENyf$g32b9vhjDwZKYe7ZVjAjFcQfBWbHqN4F4rbf3gb7sclPQscguZIm6rBhP.YkP2HeixQuJ5NA0IsQnoT4h6rr4/
#firewall --enabled --ssh --port=161:udp
skipx
#authconfig --enableshadow --passalgo=sha512 --enableldap --enableldapauth --ldapserver=ldap://rhel6-build.biomatters.com --ldapbasedn="dc=testing,dc=com" --disableldaptls --enablesssd --enablesssdauth --update
authconfig --enableshadow --passalgo=sha512 --enableldap --enableldapauth --ldapserver=ldaps://ldap.biomatters.com --ldapbasedn="dc=biomatters,dc=com" --enablesssd --enablesssdauth --update
selinux --disabled
timezone NZ
zerombr
bootloader --location=mbr --append="console=tty0 console=ttyS0,115200 rd_NO_PLYMOUTH"
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
yum-cron
net-snmp
nzgl-release
nzgl-rhn-release
@Development tools
@NZGL
@Internet Browser
@Desktop
%end

%post --logfile /root/post.log

master_ipv4="192.168.30.104"
master_ipv6="2001:dead:beef:fdb8::1"

# Disable services
cat << EOF > /usr/local/sbin/disableservices
#!/bin/bash
services_enable="crond|netfs|network|postfix|rsyslog|sshd|udev-post|rpcbind|sssd|iptables|freenx-server|ntpd|snmpd|yum-cron"
services_disable=\$(/sbin/chkconfig --list | grep 3:on | awk '{print \$1}' | egrep -v "\${services_enable}" | egrep -v "network")
for service in \${services_disable}; do
	/sbin/chkconfig --del \${service}
done
EOF

chmod +x /usr/local/sbin/disableservices

echo '*:install:/usr/local/sbin/disableservices
*:update:/usr/local/sbin/disableservices' > /etc/yum/post-actions/services.action

# Disable yum RHN subscription plugin
#sed 's/enabled=1/enabled=0/g' --in-place /etc/yum/pluginconf.d/subscription-manager.conf
rpm -e subscription-manager subscription-manager-gnome

# Enforce default JDK is 1.6.0
echo '#!/bin/bash
alternatives --remove java /usr/lib/jvm/jre-1.7.0-openjdk.x86_64/bin/java
alternatives --remove jre_openjdk /usr/lib/jvm/jre-1.7.0-openjdk.x86_64
alternatives --remove jre_1.7.0 /usr/lib/jvm/jre-1.7.0-openjdk.x86_64' > /usr/local/sbin/disablejava7
chmod +x /usr/local/sbin/disablejava7

echo 'java-1.7*:install:/usr/local/sbin/disablejava7 
java-1.7*:update:/usr/local/sbin/disablejava7' > /etc/yum/post-actions/java.action

# Enable yum-cron
chkconfig yum-cron on


# Remove unnecessary firmware packages
rpm -e $(rpm -qa | grep -i \\-firmware | grep -v kernel-firmware)

# Upgrade packages
yum -y upgrade

# NFS 
#echo "rhel6-build:/home /home nfs rw,hard,intr,rsize=8192,wsize=8192 0 0" >> /etc/fstab

# SSH
sed 's/GSSAPIAuthentication yes/GSSAPIAuthentication no/g' --in-place /etc/ssh/sshd_config
sed 's/#PermitRootLogin yes/PermitRootLogin no/g' --in-place /etc/ssh/sshd_config
sed 's/PasswordAuthentication yes/PasswordAuthentication no/g' --in-place /etc/ssh/sshd_config
sed 's/#MaxAuthTries 6/MaxAuthTries 2/g' --in-place /etc/ssh/sshd_config
echo 'AllowGroups biomatters nx' >> /etc/ssh/sshd_config

# PAM/LDAP host restriction
# sed 's/#pam_check_host_attr yes/pam_check_host_attr yes/g' --in-place /etc/pam_ldap.conf
# SSSD allow self-signed certs for testing only
sed 's/\[sssd\]/ldap_tls_reqcert = never \n\[sssd\]/g' --in-place /etc/sssd/sssd.conf
sed 's/#tls_checkpeer yes/tls_checkpeer no/g' --in-place /etc/pam_ldap.conf

# Sudoers
echo '%biomatters ALL=(ALL) ALL' >> /etc/sudoers

#NX
sed 's/#ENABLE_SSH_AUTHENTICATION="1"/ENABLE_SSH_AUTHENTICATION="1"/g' --in-place /etc/nxserver/node.conf
nxsetup --install --clean --purge --setup-nomachine-key --ignore-errors
# Allow password authentication from localhost (else NX can't authenticate)
echo 'Match Address 127.0.0.1
  PasswordAuthentication yes' >> /etc/ssh/sshd_config

# Munin
#chkconfig munin-node on
#mkdir -m 0700 /var/lib/munin/.ssh
#echo 'ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAvMI275mOlgGSj1xusO4HzS7uktCfvfqVNILxAFV/I0DtDAhtS27/KSlWeRA0NMHK8xM/sn8XWe0xePO89q+6u31QWg6KQSH8Fg7ovlOSVk3T6Tur8lL/nwEc3ommTMzzTTs5dO5jBVUtOB41DPMLkXv8+QiVE3ZU1H+FIbpIqcXUp66lyDeQPibugwmU17zAhI+gdLEo0q2f9TkUDTgqicC97xnfMqc7VyqH3kJMT39TM/d7MgdomUYtLeLb1Y640wmW0oGrC3o6HOT1ACYEi9xc8lvFBXTO/6+MIhjflznHXki60iUbYpPk3VWay+1ovNBbAKLU3bQ+N668Y2IsnQ== munin master' > /var/lib/munin/.ssh/authorized_keys
#chown -R munin:munin /var/lib/munin/.ssh/
#chmod 600 /var/lib/munin/.ssh/authorized_keys

# Munin plugins
#/bin/rm /etc/munin/plugins/*

#plugins='cpu df df_inode diskstats load memory netstat processes proc_pri swap threads uptime users vmstat'
#for plugin in ${plugins}; do
#	ln -sf /usr/share/munin/plugins/${plugin} /etc/munin/plugins/${plugin} 
#	ln -sf /usr/share/munin/plugins/if_ /etc/munin/plugins/if_eth0
#done

# SNMP
echo "sysservices 72
sysContact nzgl@biomatters.com
sysLocation NZGL
rocommunity nzgl_pub ${master_ipv4} ${master_ipv6}
disk  /" > /etc/snmp/snmpd.conf
chkconfig snmpd on

%end
