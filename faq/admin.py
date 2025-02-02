from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import FAQ

class FAQAdminForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        widgets = {
            'answer': CKEditorWidget(),
            'answer_hi': CKEditorWidget(),
            'answer_bn': CKEditorWidget(),
        }

class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm
    list_display = ('id', 'question', 'created_at')
    search_fields = ('question',)

admin.site.register(FAQ, FAQAdmin)
