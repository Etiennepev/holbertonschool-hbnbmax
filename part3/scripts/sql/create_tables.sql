-- User Table
CREATE TABLE IF NOT EXISTS User (
    id CHAR(36) PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE
);

-- Place Table
CREATE TABLE IF NOT EXISTS Place (
    id CHAR(36) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    latitude FLOAT CHECK (latitude BETWEEN -90 AND 90),
    longitude FLOAT CHECK (longitude BETWEEN -180 AND 180),
    owner_id CHAR(36) NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES User(id) ON DELETE CASCADE
);

-- Review Table
CREATE TABLE IF NOT EXISTS Review (
    id CHAR(36) PRIMARY KEY,
    text TEXT NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    user_id CHAR(36) NOT NULL,
    place_id CHAR(36) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
    FOREIGN KEY (place_id) REFERENCES Place(id) ON DELETE CASCADE,
    CONSTRAINT unique_review UNIQUE (user_id, place_id)
);

-- Amenity Table
CREATE TABLE IF NOT EXISTS Amenity (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

-- Place_Amenity Table (Many-to-Many relationship)
CREATE TABLE Place_Amenity (
    place_id CHAR(36) NOT NULL,
    amenity_id CHAR(36) NOT NULL,
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES Place(id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES Amenity(id) ON DELETE CASCADE
);

-- Insert Initial Data

-- Administrator User
INSERT INTO User (id, first_name, last_name, email, password, is_admin) VALUES (
	'36c9050e-ddd3-4c3b-9731-9f487208bbc1',
	'Admin',
	'HBnB',
	'admin@hbnb.io',
	'hash the pass word 'admin1234' here', 
	TRUE
);

INSERT INTO Amenity (id, name) VALUES (
	'2c3f91da-1258-45f3-9ed2-445ad8da14c6', 'WiFi',
	'ac1bb5af-70dd-41a4-85d5-55df15f28b8b', 'Swimming Pool',
	'06383743-20e8-4280-91a5-e29c932a27bc', 'Air Conditioning',
)
