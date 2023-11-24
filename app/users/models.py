from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    hashed_password: Mapped[str]
    task: Mapped['Tasks'] = relationship(back_populates='user')

    def __str__(self):
        return f'User {self.email}'

