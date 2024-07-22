from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db
import os.path
import json
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# read the experiment configuration (hardcoded config filename is a big issue!)
config = json.load(open("experiments/current_config.json"))

if not os.path.exists(f"experiments/{config['simulation']['name']}.db"):
    # copy the clean database to the experiments folder
    shutil.copyfile(f"{BASE_DIR}/../../data_schema/database_clean_client.db", f"{BASE_DIR}/../../experiments/{config['simulation']['name']}.db")

base = declarative_base()
engine = db.create_engine(f"sqlite:///experiments/{config['simulation']['name']}.db")
base.metadata.bind = engine
session = orm.scoped_session(orm.sessionmaker())(bind=engine)


class Articles(base):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    summary = db.Column(db.String(800))
    website_id = db.Column(db.Integer, nullable=False)
    fetched_on = db.Column(db.Integer, nullable=False)
    link = db.Column(db.String(200), nullable=False)


class Websites(base):
    __tablename__ = "websites"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rss = db.Column(db.String(200), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    language = db.Column(db.String(50), nullable=False)
    leaning = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    last_fetched = db.Column(db.Integer, nullable=False)
