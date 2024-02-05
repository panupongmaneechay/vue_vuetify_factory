CREATE DATABASE factory;

\c factory;

CREATE TABLE auth_user (
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);

INSERT INTO auth_user (username, password) VALUES ('admin123', 'admin123');

CREATE TABLE main_data (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    editTime TIMESTAMP
);

CREATE TABLE parts (
    id SERIAL PRIMARY KEY,
    main_data_id INT REFERENCES main_data(id),
    part_name VARCHAR(255),
    part_value VARCHAR(255)
);


CREATE TABLE parts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    editTime TIMESTAMP,
    part_name VARCHAR(255),
    part_value VARCHAR(255)
);

-- Insert data into the 'components' table
INSERT INTO parts (name, editTime, part_name, part_value) VALUES
    ('Part A', '', 'Part A', ''),
    ('Part A', '', 'Part B', '3'),
    ('Part A', '', 'Part C', '4'),
    ('Part B', '', 'Part A', '4'),
    ('Part B', '', 'Part B', ''),
    ('Part B', '', 'Part C', '2'),
    ('Part C', '', 'Part A', '5'),
    ('Part C', '', 'Part B', '6'),
    ('Part C', '', 'Part C', '');

-- Optionally, update the 'editTime' in the 'components' table if needed
UPDATE components SET editTime = CURRENT_TIMESTAMP;
