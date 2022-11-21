from import_export import resources
from users.models import CustomUser

class UserAdminResource(resources.ModelResource):
    
    class Meta:
        model = CustomUser
        exclude = ('imported', )
       