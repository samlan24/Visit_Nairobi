from app import db, create_app
from seed_data import COUNTY_DATA
from app.categories.models import Category
from app.auth.models import Role, User
from app.businesses.models import Business
from app.chats.models import Chat
from app.reviews.models import Review
from app.events.models import Event
from app.location.models import Location


app = create_app()

def seed_locations():
    """Seed location data into the database."""
    with app.app_context():
        for county, areas in COUNTY_DATA.items():
            if isinstance(areas, dict):
                for constituency, towns in areas.items():
                    for town in towns:
                        location = Location(name=town, county=county, area=constituency)
                        db.session.add(location)
            else:
                for town in areas:
                    location = Location(name=town, county=county, area=town)
                    db.session.add(location)

        db.session.commit()
        print("Database seeding complete!")

if __name__ == "__main__":
    seed_locations()

