from import_export import resources
from  .models import FinalControlTest

class ControlAdminResource(resources.ModelResource):
    
    class Meta:
        model = FinalControlTest
        exclude = ('imported', )