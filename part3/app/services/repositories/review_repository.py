from app import db
from models.review import Review
from app.persistence.repository import SQLAlchemyRepository

class ReviewRepository(SQLAlchemyRepository):

    def __init__(self):
        super().__init__(Review)

    def get_reviews_by_place(self, place_id):
        """Retrieve all reviews for a specific place."""
        return self.model.query.filter_by(place_id=place_id).all()

    def get_reviews_by_user(self, user_id):
        """Retrieve all reviews written by a specific user."""
        return self.model.query.filter_by(user_id=user_id).all()
