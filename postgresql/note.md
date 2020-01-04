
















# ~ ~ ~ ~ ~  Install PostgreSQL ~ ~ ~ ~ ~

## step 0 - Start Debian VM
VBoxManage startvm Debian10 --type headless
ssh losacii@192.168.1.9

## Step 1 – Setup PostgreSQL PPA
wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'

## Step 2 – Install PostgreSQL on Debian 10
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

## Step 3 – Connect to PostgreSQL
sudo -u postgres psql
\conninfo
( You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432". )
\q



# ~ ~ ~ ~ ~  Install pgcli for PostgreSQL ~ ~ ~ ~ ~

## =====> pgcli step 1:
sudo apt-get install postgresql python-psycopg2 libpq-dev

pip3 install -U pgcli

## pgcli step 2: Create Superuser, Create Database: myDB
sudo -i
su - postgres

createuser --interactive --pwprompt
createdb myDB

pgcli myDB ...

## to be continued...
