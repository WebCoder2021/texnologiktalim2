from import_export import resources
from  .models import TestAnswer,TestQuestion

class TestAnswerAdminResource(resources.ModelResource):
    
    class Meta:
        model = TestAnswer
        exclude = ('imported', )

class TestQuestionDetailAdmin(resources.ModelResource):
    
    class Meta:
        model = TestQuestion
        exclude = ('imported', )