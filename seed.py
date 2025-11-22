# seed.py
from app import app
from models import db, User

USERNAME="admin"
PASSWORD="admin123"

def seed():
    with app.app_context():
        db.create_all()
        if User.query.filter_by(username="admin").first():
            print("Admin already exists. Seeding skipped.")
            return

        admin = User(
            username=USERNAME,
            password=PASSWORD  # plain password text for simplicity
        )
        db.session.add(admin)
        db.session.commit()

        print("Admin seeded successfully!")
        print(f"Login with username='{USERNAME}', password='{PASSWORD}'")

if __name__ == "__main__":
    seed()
