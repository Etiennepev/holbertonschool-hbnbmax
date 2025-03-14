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
