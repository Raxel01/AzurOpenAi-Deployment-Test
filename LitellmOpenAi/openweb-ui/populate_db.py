import time
import os
import uuid

from sqlalchemy.orm import sessionmaker
from open_webui.apps.webui.internal.db import Base, get_db
from open_webui.apps.webui.models.users import UserModel, Users
from open_webui.apps.webui.models.models import Model
from passlib.context import CryptContext
from open_webui.apps.webui.models.auths import AuthModel, Auth
from sqlalchemy import update
from sqlalchemy.sql import null

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

email = os.getenv('ADMIN_EMAIL')
password = pwd_context.hash(os.getenv('ADMIN_PASSWORD'))
role = os.getenv('ROLE')
oauth_sub=None
ADMIN_NAME = os.getenv('ADMIN_NAME')
profile_image_url = os.getenv('DEFAULT_IMG')

try :
    with get_db() as db:
            id = str(uuid.uuid4())

            auth = AuthModel(
                **{"id": id, "email": email, "password": password, "active": True}
            )
            result = Auth(**auth.model_dump())
            db.add(result)

            user = Users.insert_new_user(
                id, ADMIN_NAME, email, profile_image_url, role, oauth_sub
            )
            
            updateGPT = update(Model).where(Model.name == "gpt-4o").values(access_control=None)
            db.execute(updateGPT)
            db.commit()
            db.refresh(result)
except Exception as e:
    print(f'Error while inserting data to db: {e}')