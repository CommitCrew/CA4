FROM mysql:latest

#ENV MYSQL_DATABASE=studentInfo
ENV MYSQL_ROOT_PASSWORD=root

COPY ./database.sql /docker-entrypoint-initdb.d/

EXPOSE 3306