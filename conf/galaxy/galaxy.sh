#!/bin/bash

set -e

user='galaxy'
home_dir='/home/galaxy'
yum_packages='postgresql postgresql-server mercurial wget nginx'

virtualenvpy_mirror="http://bitbucket.org/ianb/virtualenv/raw/tip/virtualenv.py"
virtualenvpy='virtualenv.py'
galaxyinit="galaxy.init"
universewsgiini="universe_wsgi.ini"
nginxconf="nginx.conf"

db='galaxy'
db_user='galaxy'
db_password=$(cat /dev/urandom | tr -cd 'a-f0-9' | head -c 16)

if [ ! -e ${virtualenvpy} ]; then
	wget -q ${virtualenvpy_mirror}
fi

for file in ${galaxyinit} ${universewsgiini} ${nginxconf} ${virtualenvpy}; do
	if [ ! -e ${file} ]; then
		echo "${file} does not exist."
		exit 1
	fi
done

if [ -d "${home_dir}" ]; then
	echo "Home directory (${home_dir}) exists."
	exit 1
fi

if [ $(getent passwd | grep ^"${user}:") ]; then
	echo "Galaxy user (${user}) exists."
	exit 1
fi

# Add galaxy user
/usr/sbin/useradd --home-dir ${home_dir} --create-home ${user}
if [ $? -ne 0 ]; then
	echo "Failed to create user (${user})."
fi

# Install required packages
yum --quiet -y install ${yum_packages}
if [ $? -ne 0 ]; then
	echo "Failed to install required packages: ${yum_packages}"
	exit 1
fi

# Clone galaxy-dist
if [ -d ~/galaxy-dist ]; then
	cp -r ~/galaxy-dist /home/galaxy/
else
	su ${user} -c "cd ~; hg clone https://bitbucket.org/galaxy/galaxy-dist"
	if [ $? -ne 0 ]; then
		echo "Failed to run hg clone."
		exit 1
	fi
fi

# Setup Python virtualenv
{
/bin/cp -f ${virtualenvpy} ${home_dir}/virtualenv.py
su ${user} -c "cd ~; python ./virtualenv.py galaxy_env"
su ${user} -c "cd ~; . ./galaxy_env/bin/activate; which python"
echo 'source ~/galaxy_env/bin/activate
TEMP=$HOME/galaxy-dist/database/tmp 
export TEMP' > "${home_dir}/.bashrc"
} || { echo "virtualenv setup failed."; exit 1; }

# Setup postgresql
/sbin/service postgresql initdb

sed 's/^host/#host/g' --in-place /var/lib/pgsql/data/pg_hba.conf
sed 's/^local/#local/g' --in-place /var/lib/pgsql/data/pg_hba.conf
echo 'local   all         all                               trust
host    all         all         127.0.0.1/32          trust
host    all         all         ::1/128               trust
host    all         all         0.0.0.0/0             md5' >> /var/lib/pgsql/data/pg_hba.conf

/sbin/service postgresql restart
if [ $? -ne 0 ]; then
	echo "PostgreSQL failed to start."
	exit 1
fi

/sbin/chkconfig postgresql on

{
sudo -u postgres createdb ${db}
sudo -u postgres psql -c "CREATE USER ${db_user} WITH PASSWORD '${db_password}';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE ${db} to ${db_user};"
} || { echo "Failed to create database/database user."; exit 1; }

# Copy config into place, setup with DB settings
#/bin/cp -f ${universewsgiini} ${home_dir}/galaxy-dist/universe_wsgi.ini
#sed "s={db_connection}=postgres://${db_user}:${db_password}@localhost:5432/${db}=g" --in-place ${home_dir}/galaxy-dist/universe_wsgi.ini

# Add db details to universe_wsgi.ini
cp universe_wsgi.ini universe_wsgi.ini.db
sed "s={db_connection}=postgres://${db_user}:${db_password}@localhost:5432/${db}=g" --in-place universe_wsgi.ini.db

# Copy galaxy init into place
/bin/cp -f ${galaxyinit} /etc/init.d/galaxy
chmod +x /etc/init.d/galaxy
/sbin/chkconfig galaxy on

# nginx
mkdir -p /home/galaxy/galaxy-dist/database/tmp/upload_store
/bin/cp -f ${nginxconf} /etc/nginx/nginx.conf
service nginx start

chown -R galaxy:galaxy /home/galaxy

echo "Galaxy prep complete."
