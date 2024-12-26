import time
import os
import uuid

from sqlalchemy.orm import sessionmaker
from open_webui.internal.db import Base, get_db 
from open_webui.models.users import UserModel, Users
from open_webui.models.models import Model, ModelForm, Models
from passlib.context import CryptContext
from open_webui.models.auths import AuthModel, Auth
from sqlalchemy import update
from sqlalchemy.sql import null

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

email = os.getenv('ADMIN_EMAIL')
password = pwd_context.hash(os.getenv('ADMIN_PASSWORD'))
role = os.getenv('ROLE')
oauth_sub=None
ADMIN_NAME = os.getenv('ADMIN_NAME')
profile_image_url = os.getenv('DEFAULT_IMG')
model_name = os.getenv('MODEL_NAME')
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
            modelInstance = ModelForm(
                id=model_name,
                base_model_id=None,
                name=model_name,
                meta={"profile_image_url": "/static/favicon.png",
                       "description": "", "capabilities": {"vision": True, "citations": True},
                       "suggestion_prompts":None, "tags": []},
                params={},
                access_control=None,
                is_active=1   
            )
            Gptmodel = Models.insert_new_model(modelInstance, id)
            db.commit()
            db.refresh(result)
except Exception as e:
    print(f'Error while inserting data to db: {e}')