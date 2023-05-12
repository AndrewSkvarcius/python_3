from app import db
from models import Pet

db.drop_all()
db.create_all()

j = Pet(name="Jane", species="dog",photo_url="https://www.what-dog.net/Images/faces2/scroll001.jpg",age=2,notes="Incredibly adorable.")
db.session.add(j)
db.session.commit()
p = Pet(name="Porchetta", species="porcupine",photo_url="http://kids.sandiegozoo.org/sites/default/files/2017-12/porcupine-incisors.jpg",age=4,notes="Somewhat spiky!")
db.session.add(p)
db.session.commit()
s = Pet(name="Snargle", species="cat",photo_url="https://www.catster.com/wp-content/uploads/2017/08/A-fluffy-cat-looking-funny-surprised-or-concerned.jpg",age=5  ,notes="Mean as hell")
db.session.add(s)
db.session.commit()
m = Pet(name="M.Claw", species="cat",photo_url="",age=5  ,notes="Mean as hell")
db.session.add(m)
db.session.commit()


