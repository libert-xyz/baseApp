from crud import db

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(60))
    date_message = db.Column(db.DateTime)
    message = db.Column(db.String(140))

    def __init__(self,nickname):
        self.nickname = nickname


    @property
    def serialize(self):
        return {
        'id': self.id,
        'nickname': self.nickname,
        'date': self.date_message,
        'message': self.message
        }
