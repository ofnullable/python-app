from bugbounty.env.database import db, BaseTimeModel, BaseModel, Column, Model, \
    reference_col, relationship


class Program(Model, BaseModel):
    __tablename__ = 'program'

    title = Column(db.String(64), unique=True, nullable=False)
    is_public = Column(db.Boolean, nullable=False, default=False)
    is_proceeding = Column(db.Boolean, nullable=False, default=False)

    vendor_id = reference_col('user', nullable=False)
    vendor = relationship('User', backref='program', lazy=True)

    policy = relationship('ProgramPolicy', back_populates='program', lazy=True)

    def __init__(self, vendor, **kwargs):
        if not kwargs.get('title'):
            super(Program, self).__init__(vendor=vendor, title=vendor.profile.vendor_name, **kwargs)
        else:
            super(Program, self).__init__(vendor=vendor, **kwargs)


class ProgramPolicy(Model, BaseTimeModel):
    __tablename__ = 'program_policy'

    policy = Column(db.LargeBinary, nullable=False)

    registrant_id = reference_col('user', nullable=False)
    registrant = relationship('User', lazy=True)

    program_id = reference_col('program', nullable=False)
    program = relationship('Program', back_populates='policy', lazy=True)

    def __init__(self, **kwargs):
        super(ProgramPolicy, self).__init__(**kwargs)
