from giovanniflix import db

class ContentEntry(db.Model):
    """Model for content video entries."""

    __tablename__ = 'content'
    id = db.Column(db.String(64),
                   primary_key=True)
    link = db.Column(db.String(256),
                         nullable=False)
    title = db.Column(db.String(80),
                      nullable=False)
    def __repr__(self):
        return '<Content {}>'.format(self.title)
