from django.contrib import admin
from api.models import Answer, Category, Comment, Tag, Question, UserProfile


admin.site.register(Answer)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(UserProfile)
