from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

Soccer = Category(title="Soccer")
Basketball = Category(title="Basketball")
Snowboarding = Category(title="Snowboarding")
Football = Category(title="Football")
Hockey = Category(title="Hockey")


SoccerItem = Item(title="Soccer Item", description="This is a soccer item description", 
                user_id="1", category_id="1")
BasketballItem = Item(title="Basketball Item", description="This is a Basketball item description", 
                user_id="1", category_id="2")
SnowboardingItem = Item(title="Snowboarding Item", description="This is a Snowboarding item description", 
                user_id="1", category_id="3")
FootballItem = Item(title="Football Item", description="This is a Football item description", 
                user_id="1", category_id="4")
HockeyItem = Item(title="Hockey Item", description="This is a Hockey item description", 
                user_id="1", category_id="5")

user = User(name="Mohamad Bahamdain", email="mohamad.bahamdain@gmail.com")

session.add_all([Soccer, Basketball, Snowboarding, Football, Hockey])
session.add_all([SoccerItem, BasketballItem, SnowboardingItem, HockeyItem, FootballItem])
session.commit()

