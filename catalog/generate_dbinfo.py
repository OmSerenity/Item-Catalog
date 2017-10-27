from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from database_setup import Base, Category, Item, User


engine = create_engine('postgresql://catalog:catalog:postgres@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create sample users
User0 = User(name="Oprah Winfrey", email="oprah@oprah.com",
             picture='https://upload.wikimedia.org/wikipedia/commons/6/65/Oprah_closeup.jpg')
session.add(User0)
session.commit()
User1 = User(name="Germaine Greer", email="Germaine@Greer.com",
             picture='https://upload.wikimedia.org/wikipedia/commons/a/a6/Germaine_Greer.jpg')
session.add(User1)
session.commit()
User2 = User(name="Heema Chopra", email="heemachopra@gmail.com",
             picture='https://upload.wikimedia.org/wikipedia/commons/a/ad/Indian_lady.jpg')
session.add(User2)
session.commit()
User3 = User(name="Ima Peruviana", email="Peruviana@yahoo.com",
             picture='https://upload.wikimedia.org/wikipedia/commons/9/9e/Old_zacatecas_lady.jpg')
session.add(User3)
session.commit()
User4 = User(name="Reema Sattarvand", email="Reema@outlook.com",
             picture='https://upload.wikimedia.org/wikipedia/commons/c/ca/Portrait_of_a_Persian_lady_in_Iran%2C_10-08-2006.jpg')
session.add(User4)
session.commit()


# Create sample categories
category0 = Category(user_id=1, name="Bushes")
session.add(category0)
session.commit()
category1 = Category(user_id=2, name="Wildflowers")
session.add(category1)
session.commit()
category2 = Category(user_id=3, name="Edible Plants")
session.add(category2)
session.commit()
category3 = Category(user_id=3, name="Striking Plants")
session.add(category3)
session.commit()
category4 = Category(user_id=3, name="Useful Plants")
session.add(category4)
session.commit()

# Create sample items
newitem0 = Item(user_id=0, name="Desert Peach",
                description="Beautiful pink flowers, part of the rose family",
                category=category0)
session.add(newitem0)
session.commit()
newitem1 = Item(user_id=0, name="Wyoming Big Sagebrush",
                description="Fire hazard because of flammable, volatile oils",
                category=category0)
session.add(newitem1)
session.commit()
newitem2 = Item(user_id=0, name="Snowbrush",
                description="Burns with high intensity, fragrant flowers attract bees",
                category=category0)
session.add(newitem2)
session.commit()
newitem3 = Item(user_id=1, name="California Poppy",
                description="Has sedative and pain-reducing properties",
                category=category1)
session.add(newitem3)
session.commit()
newitem4 = Item(user_id=1, name="Desert Paintbrush",
                description="Striking red flowers",
                category=category1)
session.add(newitem4)
session.commit()
newitem5 = Item(user_id=1, name="Desert Sunflower",
                description="Beautiful and tough",
                category=category1)
session.add(newitem5)
session.commit()
newitem6 = Item(user_id=2, name="Prickly Pear Cactus",
                description="Juicy red fruits",
                category=category2)
session.add(newitem6)
session.commit()
newitem7 = Item(user_id=2, name="Desert Gooseberry",
                description="Thorny, Fruit can be used for pies",
                category=category2)
session.add(newitem7)
session.commit()
newitem8 = Item(user_id=2, name="Western Serviceberry",
                description="Edible fruit",
                category=category2)
session.add(newitem8)
session.commit()
newitem9 = Item(user_id=3, name="Joshua Tree",
                description="30 ft tall: Iconic, but not really a tree!",
                category=category3)
session.add(newitem9)
session.commit()
newitem10 = Item(user_id=3, name="Rubber Rabbitbrush",
                 description="Bright yellow flowers, beware the pollen!",
                 category=category3)
session.add(newitem10)
session.commit()
newitem11 = Item(user_id=3, name="Spiny hopsage",
                 description="Interesting rose colored flowers",
                 category=category3)
session.add(newitem11)
session.commit()
newitem12 = Item(user_id=4, name="Yucca",
                 description="Edible flowers and useful fibers from leaves",
                 category=category4)
session.add(newitem12)
session.commit()
newitem13 = Item(user_id=4, name="Sumac",
                 description="Acidic red flowers can be made into a drink",
                 category=category4)
session.add(newitem13)
session.commit()
newitem14 = Item(user_id=4, name="Pinyon",
                 description="Where yummy pine nuts come from",
                 category=category4)
session.add(newitem14)
session.commit()

print("Added Sample Plant Content!")
