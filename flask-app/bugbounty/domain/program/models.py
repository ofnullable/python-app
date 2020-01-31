from bugbounty.env.database import db, BaseTimeModel, BaseModel, Column, Model, \
    reference_col, relationship


class Program(Model, BaseModel):
    __tablename__ = 'program'

    title = Column(db.String(64), unique=True, nullable=False)
    is_public = Column(db.Boolean, nullable=False, default=False)
    is_proceeding = Column(db.Boolean, nullable=False, default=False)

    vendor_id = reference_col('user', nullable=False)
    vendor = relationship('User', lazy=True)

    policies = relationship('ProgramPolicy', backref='program', lazy='joined', order_by='ProgramPolicy.id.desc()')

    def __init__(self, vendor, **kwargs):
        title = kwargs.get('title')
        if not title:
            title = vendor.profile.vendor_name
        super(Program, self).__init__(vendor=vendor, title=title, **kwargs)


class ProgramPolicy(Model, BaseTimeModel):
    __tablename__ = 'program_policy'

    contents = Column(db.LargeBinary, nullable=False)

    writer_id = reference_col('user', nullable=False)
    writer = relationship('User', lazy=True)

    program_id = reference_col('program', nullable=False)

    def __init__(self, **kwargs):
        contents = kwargs.pop('contents')

        super(ProgramPolicy, self).__init__(contents=bytes(contents, 'utf-8'), **kwargs)
