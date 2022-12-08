from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import News, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'



class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('id', 'title', 'category', 'content',  'is_published','photo', 'get_photo','created_at', 'updated_at','views' )
    readonly_fields = ('id','get_photo','created_at', 'updated_at','views' )
    save_on_top = True


    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src = "{ obj.photo.url }" width = "75" >')

    get_photo.short_description = 'image'



admin.site.register(News, NewsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )

admin.site.register(Category, CategoryAdmin)
admin.site.site_header = 'Meiirzhan Top'
admin.site.site_title = 'Meiirzhan Top'