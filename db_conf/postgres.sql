
# shell:
sudo su - postgres

# In postgres:
createdb mydb

# Needs superuser for hstore
createuser user1 -s -P
# use pass: user1

# in the same root shell start psql:
psql

# Grant permissions
GRANT ALL PRIVILEGES ON DATABASE mydb TO user1;
CREATE EXTENSION IF NOT EXISTS hstore;

## TO play with the db:
pgcli mydb user1
user1

# list tables
\dt
