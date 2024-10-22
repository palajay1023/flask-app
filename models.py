# backend/models.py
from app import db

class PaperRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    comments = db.Column(db.Text, nullable=True)
    whatsapp_number = db.Column(db.String(15), nullable=False)
    country_code = db.Column(db.String(5), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
 
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'link': self.link,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'comments': self.comments,
            'whatsapp_number': self.whatsapp_number,
            'country_code': self.country_code,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
