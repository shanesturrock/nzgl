install
text
cdrom
reboot

#url --url=http://nzglrepo.biomatters.com/rhel-x86_64-server-6
repo --name=nzgl-stable --baseurl=http://nzglrepo.biomatters.com/nzgl-stable
#repo --name=rhel-optional --baseurl=http://nzglrepo.biomatters.com/rhel-x86_64-server-optional-6

lang en_US.UTF-8
keyboard us
network --onboot yes --device eth0 --bootproto dhcp
rootpw --iscrypted $6$/c8wetYVjfiZENyf$g32b9vhjDwZKYe7ZVjAjFcQfBWbHqN4F4rbf3gb7sclPQscguZIm6rBhP.YkP2HeixQuJ5NA0IsQnoT4h6rr4/
firewall --enabled --ssh
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
nzgl-release
@Development tools
@NZGL
@Internet Browser
@Desktop
%end

%post --logfile /root/post.log
# Remove unnecessary firmware packages
rpm -e $(rpm -qa | grep -i \\-firmware | grep -v kernel-firmware)

# Disable services
services_enable="crond|netfs|network|postfix|rsyslog|sshd|udev-post|rpcbind|sssd|iptables|freenx-server|ntpd"
services_disable=$(/sbin/chkconfig --list | grep 3:on | awk '{print $1}' | egrep -v "${services_enable}" | egrep -v "network")
for service in ${services_disable}; do
	/sbin/chkconfig --del ${service}
done

# Disable yum RHN subscription plugin
#sed 's/enabled=1/enabled=0/g' --in-place /etc/yum/pluginconf.d/subscription-manager.conf
rpm -e subscription-manager subscription-manager-gnome

# Revert default JDK to 1.6.0
#alternatives --remove java /usr/lib/jvm/jre-1.7.0-openjdk.x86_64/bin/java
#alternatives --remove jre_openjdk /usr/lib/jvm/jre-1.7.0-openjdk.x86_64
#alternatives --remove jre_1.7.0 /usr/lib/jvm/jre-1.7.0-openjdk.x86_64

echo 'java-1.7*:install:alternatives --remove java /usr/lib/jvm/jre-1.7.0-openjdk.x86_64/bin/java; alternatives --remove jre_openjdk /usr/lib/jvm/jre-1.7.0-openjdk.x86_64; alternatives --remove jre_1.7.0 /usr/lib/jvm/jre-1.7.0-openjdk.x86_64
java-1.7*:update:alternatives --remove java /usr/lib/jvm/jre-1.7.0-openjdk.x86_64/bin/java; alternatives --remove jre_openjdk /usr/lib/jvm/jre-1.7.0-openjdk.x86_64; alternatives --remove jre_1.7.0 /usr/lib/jvm/jre-1.7.0-openjdk.x86_64' > /etc/yum/post-actions/java.action

# NFS 
#echo "rhel6-build:/home /home nfs rw,hard,intr,rsize=8192,wsize=8192 0 0" >> /etc/fstab

# SSH
#mkdir /root/.ssh
#chmod 700 /root/.ssh
#echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCmlq64iOtDSgNkJEektc6usef+bjI1XCCO5gsZSzQQzSdHWCfNNrhc3RuKakYIaW8NvQaX6jaDD9QiIQKRNAWKrD9VgOFTLDcrUtNW5Qs+DO/B8vikkhF6OCknIZAIG8MNXLYwJLKiiL58sChHFNyfoD5jXh+P+4rz4UCO9RH1x18lNwXC01rYRYct5rQJsvHNUFpz5whZO3WhkSoJMvRspHuE0ZQn98qGxld8DfIlBEh4Ox6wmbpBU5MvN55Y8NZD8DBng0d+YOMmMLcOYj/IWYV99pRJPKJ0wFVlJmFd7ShslEuhJcUirzGcNcxHfC7zwL0tDCirxBpPlDgXtlBl carl' >> /root/.ssh/authorized_keys
#echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCtptTkYtbxgHQZKvOhv9U+v7uP/7TWqKOHPE4KU6VXVDrUb1W2CL3tBW1q0NVbmk9rd1j9/nm5982hMQL/5VygBbAyt/JAUi8CZ9fAtH4En965jn1tso1Ov8ynbcvwkV8nOCj0ZQJw81+43Ro+WtfM/ENV2c1UCjYEqpaurGiLhFWNfsdkp+gdSAVCFZ0r5PuRdal8iedZ8K0ezGd2Nlg9zXhpj1p0C1h/cqDCxEFcyBQcBD5m8vt+JC6EW1/cbzNfZhfJp7W8dTfPgSnF88IL2QoeNgU0odt0LQmkuPJga0+Y/LiK4jCjNvkUcomOfaut9FGLLEoa7u26ZTVPNGev shane@biomatters.com' >> /root/.ssh/authorized_keys
#chmod 600 /root/.ssh/authorized_keys

#sed 's/#PermitRootLogin yes/PermitRootLogin without-password/g' --in-place /etc/ssh/sshd_config

sed 's/GSSAPIAuthentication yes/GSSAPIAuthentication no/g' --in-place /etc/ssh/sshd_config
sed 's/#PermitRootLogin yes/PermitRootLogin no/g' --in-place /etc/ssh/sshd_config
sed 's/PasswordAuthentication yes/PasswordAuthentication no/g' --in-place /etc/ssh/sshd_config
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

%end
