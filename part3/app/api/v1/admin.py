from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash
from app.services import facade
from flask import request

api = Namespace('admin', description='Admin operations')
    
    
@api.route('/users/')
class AdminUserCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        user_data = request.json
        email = user_data.get('email')
        password = user_data.get('password')

        if not email or not password:
            return {'error': 'Email and password are required'}, 400

        # Check if email is already in use
        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400

        # Logic to create a new user
        new_user = facade.create_user(email=email, password=password, is_admin=user_data.get('is_admin', False))
        return {'message': 'User created successfully', 'user_id': new_user.id}, 201


@api.route('/users/<user_id>')
class AdminUserModify(Resource):
    from app.models.basemodel import save
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt_identity()
        
        # If 'is_admin' is part of the identity payload
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        data = request.json
        email = data.get('email')
        password = data.get('password')
        
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        if email:
            # Check if email is already in use
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email is already in use'}, 400
            user.email = email

        # Logic to update user details, including email and password
        hash_password = generate_password_hash(user['password'])

        if password:
            user.password = hash_password(password)
		# Save the modification
        facade.save(user)
        return {'message': 'User updated successfully'}, 200
    
    
@api.route('/amenities/')
class AdminAmenityCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        data = request.json
        name = data.get('name')
        if not name:
            return {'error': 'Amenity name is required'}, 400

        # Logic to create a new amenity
        new_amenity = facade.create_amenity(name=name)
        return {'message': 'Amenity created successfully', 'amenity_id': new_amenity.id}, 201
    
    
@api.route('/amenities/<amenity_id>')
class AdminAmenityModify(Resource):
    from app.models.basemodel import save
    @jwt_required()
    def put(self, amenity_id):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        data = request.json
        name = data.get('name')
        # Logic to update an amenity
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404

        if name:
            amenity.name = name
        facade.save(amenity)
        return {'message': 'Amenity updated successfully'}, 200


@api.route('/places/<place_id>')
class AdminPlaceModify(Resource):
    from app.models.basemodel import save
    @jwt_required()
    def put(self, place_id):
        current_user = get_jwt_identity()

        # Set is_admin default to False if not exists
        is_admin = current_user.get('is_admin', False)
        user_id = current_user.get('id')

        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404

        if not is_admin and place.owner_id != user_id:
            return {'error': 'Unauthorized action'}, 403

        data = request.json
        title = data.get('title')
        description = data.get('description')
        # Logic to update the place
        if title:
            place.title = title
        if description:
            place.description = description
        
        facade.save(place)
        return {'message': 'Place updated successfully'}, 200
