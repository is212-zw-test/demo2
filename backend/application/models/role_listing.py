from application import db
from datetime import datetime, timedelta
from sqlalchemy import Column, TIMESTAMP
import uuid
from sqlalchemy.dialects.postgresql import TEXT,UUID, VARCHAR


time_format = "%Y-%m-%dT%H:%M:%SZ"
class RoleListing(db.Model):
    __tablename__ = 'role_listing'
    
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    name = Column(VARCHAR(40), nullable=False)
    description = Column(TEXT, nullable=False)
    start_time = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    end_time = Column(TIMESTAMP, nullable=False, default=datetime.utcnow() + timedelta(days=30))

    def json(self) -> dict:
        return {
            "id": str(self.id), 
            "name": self.name,
            "description": self.description,
            "start_time": self.start_time.strftime(time_format),
            "end_time": self.end_time.strftime(time_format),
        }
    
    def __repr__(self):
        return f'{self.json()}'
    
