CREATE USER fast_user WITH PASSWORD 'fast_user';
create database fast_db;

grant all privileges on database fast_db to fast_user;
