from sqlalchemy.orm import sessionmaker
import sys,os
from User.userRepository import User


class UserService:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)

    def create_user(self, Name, Nationality):
        session = self.Session()
        user = User(
            Name=Name,
            Nationality=Nationality,

        )
        session.add(user)
        session.commit()
        session.close()
    def get_all_users(self):
        session = self.Session()
        try:
            users = session.query(User).all()
            # Convert User objects to dictionaries
            users_dicts = [
                {"Name": user.Name, "Id": user.Id, "Nationality": user.Nationality}
                for user in users
            ]
            return users_dicts
        finally:
            session.close()
    def get_user_by_ID(self, ID):
        session = self.Session()
        selected_user = session.query(User).filter_by(Id=ID).first()
        session.close()
        return (
            {
                "Id": selected_user.Id,
                "Name": selected_user.Name,
                "Nationality": selected_user.Nationality,
            }
            if selected_user
            else {}
        )
