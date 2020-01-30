from bugbounty.env.database import db, BaseModel, Column, Model, BaseTimeModel, \
    relationship, reference_col
from bugbounty.env.extensions import bcrypt


class User(Model, BaseTimeModel):
    __tablename__ = 'user'

    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(100), unique=True, nullable=False)
    password = Column(db.Binary(128), nullable=True)
    is_vendor = Column(db.Boolean, nullable=False)

    profile = relationship('Profile', uselist=False, back_populates='user',
                           lazy=False)

    def __init__(self, password=None, vendor_name=None, vendor_info=None,
                 **kwargs):
        super(User, self).__init__(**kwargs)
        self.set_profile(vendor_name=vendor_name,
                         vendor_info=vendor_info, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_profile(self, is_vendor, **kwargs):
        if is_vendor:
            vendor_name = kwargs['vendor_name']
            vendor_info = kwargs['vendor_info']
            self.profile = VendorProfile(vendor_name=vendor_name,
                                         vendor_info=vendor_info)
        else:
            self.profile = HackerProfile(score=0)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        return bcrypt.check_password_hash(self.password, value)


class Profile(Model, BaseModel):
    __tablename__ = 'user_profile'

    image = Column(db.String(120))
    type = Column(db.String(50))

    user_id = reference_col('user', nullable=False)
    user = relationship('User', back_populates='profile')

    __mapper_args__ = {
        'polymorphic_identity': 'profile',
        'polymorphic_on': type
    }

    def __init__(self, **kwargs):
        super(Profile, self).__init__(**kwargs)


class HackerProfile(Profile):
    __tablename__ = None

    score = Column(db.Integer, default=0)

    __mapper_args__ = {
        'polymorphic_identity': 'hacker_profile',
    }


class VendorProfile(Profile):
    __tablename__ = None

    vendor_name = Column(db.String(120))
    vendor_info = Column(db.String(240))

    __mapper_args__ = {
        'polymorphic_identity': 'vendor_profile',
    }
