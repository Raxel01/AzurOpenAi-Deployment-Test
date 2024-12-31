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

email = os.getenv('OPEN_WEB_UI_ADMIN_EMAIL')
password = pwd_context.hash(os.getenv('OPEN_WEB_UI_ADMIN_PASSWORD'))

role = os.getenv('ROLE')
oauth_sub=None


OPEN_WEB_UI_ADMIN_NAME = os.getenv('OPEN_WEB_UI_ADMIN_NAME')
profile_image_url = os.getenv('DEFAULT_IMG')

model_name = os.getenv('MODEL_NAME')
gptmini_model_name = os.getenv('GPT_MINI_NAME')

try :
    with get_db() as db:
            Is_admin_exist = db.query(Auth).filter(Auth.email==email).first()
            Is_gpt_exist = db.query(Model).filter(Model.name == model_name).first()
            Is_gpt_mini_exist = db.query(Model).filter(Model.name == gptmini_model_name).first()
            
            if Is_admin_exist is None:
                print('Admin User added Succesfully')
                id = str(uuid.uuid4())
                auth = AuthModel(
                    **{"id": id, "email": email, "password": password, "active": True}
                )
                result = Auth(**auth.model_dump())
                db.add(result)
                user = Users.insert_new_user(
                    id, OPEN_WEB_UI_ADMIN_NAME, email, profile_image_url, role, oauth_sub
                )
            
            if Is_gpt_exist is None:
                print('GPT Model added Succesfully')
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
            
            if Is_gpt_mini_exist is None:
                print('GPT Mini Model added Succesfully')
                mini_modelInstance = ModelForm(
                    id=gptmini_model_name,
                    base_model_id=None,
                    name=gptmini_model_name,
                    meta={"profile_image_url": "/static/favicon.png",
                          "description": "", "capabilities": {"vision": True, "citations": True},
                          "suggestion_prompts": None, "tags": []},
                    params={},
                    access_control=None,
                    is_active=1
                )
                Gptminimodel = Models.insert_new_model(mini_modelInstance, id)
            db.commit()
            db.refresh(result)
except Exception as e:
    print(f'Error while inserting data to db: {e}')