from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
from .models import Research
from .models import Geodesy
from .models import Modeling
from .models import Rock
from .models import Newswall




class PostAdmin(SummernoteModelAdmin):
    summernote_fields = 'content'


class ResearchAdmin(SummernoteModelAdmin):
    summernote_fields = 'content'


class GeodesyAdmin(SummernoteModelAdmin):
    summernote_fields = 'content'


class ModelingAdmin(SummernoteModelAdmin):
    summernote_fields = 'content'


class RockAdmin(SummernoteModelAdmin):
    summernote_fields = 'content'


admin.site.register(Post, PostAdmin)
admin.site.register(Research, ResearchAdmin)
admin.site.register(Geodesy, GeodesyAdmin)
admin.site.register(Modeling, ModelingAdmin)
admin.site.register(Rock, RockAdmin)
admin.site.register(Newswall)

# Register your models here.
