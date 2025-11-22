# seed.py
from app import app
from models import db, User

def seed():
    with app.app_context():
        db.create_all()
        if User.query.filter_by(username="admin").first():
            print("Admin already exists. Seeding skipped.")
            return

        admin = User(
            username="admin",
            password="admin123"  # plain text for simplicity
        )
        db.session.add(admin)
        db.session.commit()

        print("Admin seeded successfully!")
        print("Login with username='admin', password='admin123'")

if __name__ == "__main__":
    seed()
