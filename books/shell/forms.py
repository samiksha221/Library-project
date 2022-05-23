from django .forms import ModelForm
from .models import studentRecords,bookDataset,issueRecords
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class StudentForm(ModelForm):
    class Meta:
        model=studentRecords
        fields='__all__'

class BookForm(ModelForm):
    class Meta:
        model=bookDataset
        fields='__all__'

class BookIssueForm(ModelForm):
    class Meta:
        model=issueRecords
        fields='__all__'

class AdminForms(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password']
