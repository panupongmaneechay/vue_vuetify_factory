# Use an official PostgreSQL image as the base image
FROM postgres:latest

# Set environment variables for PostgreSQL
ENV POSTGRES_DB factory
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres

# Copy the SQL script to create the database and table
COPY init.sql /docker-entrypoint-initdb.d/
