#!/usr/bin/env python3

from models import Dev, Company, Freebie
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///freebies.db")
Session = sessionmaker(bind=engine)
session = Session()

session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()

dev1 = Dev(name="Jenny")
dev2 = Dev(name="Jacob")
company1 = Company(name="Deloitte", founding_year=2015)
company2 = Company(name="Huwaei", founding_year=1998)

freebie1 = Freebie(item_name="T-shirt", value=20, dev=dev1, company=company1)
freebie2 = Freebie(item_name="Mug", value=19, dev=dev2, company=company1)

session.add_all([dev1, dev2, company1, company2, freebie1, freebie2])
session.commit()
