CREATE DATABASE ordergenerator;
CREATE USER ordergenerator WITH ENCRYPTED PASSWORD 'ordergenerator';
GRANT ALL PRIVILEGES ON DATABASE ordergenerator TO ordergenerator;
ALTER USER ordergenerator WITH SUPERUSER;
