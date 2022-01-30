from sqlalchemy.orm import Session
from fastapi import Depends
from infrastructure.session import get_db
from infrastructure.models.user import User
from utils.oauth2 import get_current_user

# This function is use for services dependent on more than one repository.
def DependentRepos(dependencies:dict={}):
    def service_decorator(service):
        def wrapped_service(db:Session=Depends(get_db),user:User=Depends(get_current_user)):
            modf_service = service()
            for key,repo in dependencies.items():
                # very magic (looking for optimal solution)
                if key == "courier_repo":
                    setattr(modf_service,key,repo(db))
                else:
                    setattr(modf_service,key,repo(db,user))
            return modf_service
        return wrapped_service
    return service_decorator
    