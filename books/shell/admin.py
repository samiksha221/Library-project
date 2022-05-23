from django.contrib import admin
from .models import studentRecords,bookDataset,issueRecords

# Register your models here.
admin.site.register(studentRecords)
admin.site.register(bookDataset)
admin.site.register(issueRecords)


