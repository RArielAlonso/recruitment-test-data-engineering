USE codetest;

CREATE TABLE IF NOT EXISTS places (
    place_id INT AUTO_INCREMENT PRIMARY KEY,
    city TEXT,
    county TEXT,
    country TEXT
);

CREATE TABLE IF NOT EXISTS people (
    given_name TEXT,
    family_name TEXT,
    date_of_birth DATE,
    place_id INT,
    FOREIGN KEY (place_id) REFERENCES places(place_id)
);
