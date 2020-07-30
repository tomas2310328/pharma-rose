

# pharmarose
### Documentation:

1. [Django](https://docs.djangoproject.com/en/2.0/releases/2.0/)

### Installation:

1. Install git on Linux:  
`sudo apt-get install -y git`
2. Clone or download this repo.
3. Install pip and vitualenv on Linux:  
`sudo apt-get install -y virtualenv`  
`sudo apt-get install -y python3-pip`
4. Create a virtual environment on Linux or Mac:  
`virtualenv -p python3 ~/.virtualenvs/pharmarose`
5. Activate the virtual environment on Linux or Mac:  
`source ~/.virtualenvs/pharmarose/bin/activate`
6. Install requirements in the virtualenv:  
`pip3 install -r requirements.txt`

##### Relational database dependencies (PostgreSQL):
1. Install components for Ubuntu:  
`sudo apt-get update`  
`sudo apt-get install python-dev libpq-dev postgresql postgresql-contrib`
2. Switch to **postgres** (PostgreSQL administrative user):  
`sudo su postgres`
3. Log into a Postgres session:  
`psql`
4. Create database with name **pharmarosedb**:  
`CREATE DATABASE pharmarosedb;`
5. Create a database user which we will use to connect to the database:  
`CREATE USER eslam WITH PASSWORD 'eslam123';`
6. Modify a few of the connection parameters for the user we just created:  
`ALTER ROLE eslam SET client_encoding TO 'utf8';`  
`ALTER ROLE eslam SET default_transaction_isolation TO 'read committed';`  
`ALTER ROLE eslam SET timezone TO 'UTC';` 
7. Give our database user access rights to the database we created:  
`GRANT ALL PRIVILEGES ON DATABASE pharmarosedb TO eslam;`
8. Exit the SQL prompt and the postgres user's shell session:  
`\q` then `exit`

9. Activate the virtual environment:  
`source ~/.virtualenvs/pharmarosedb/bin/activate`
10. Make Django database migrations:
`python manage.py makemigrations`  
then: `python manage.py migrate`


### Admin Credentials
### Username: `admin`  
### Password: `admin` 

## For Dump and Load data

##### you should creating a folder to do this operations

##### for dump data from database:

###### python manage.py dumpdata products --format json --indent 4 > products/fixures/products.json

##### For loading data into database:
###### python manage.py loaddata products/fixures/products.json

