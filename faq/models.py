from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField(_("Question"))
    answer = RichTextField(_("Answer"))
    question_hi = models.TextField(_("Question (Hindi)"), blank=True, null=True)
    answer_hi = RichTextField(_("Answer (Hindi)"), blank=True, null=True)
    question_bn = models.TextField(_("Question (Bengali)"), blank=True, null=True)
    answer_bn = RichTextField(_("Answer (Bengali)"), blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_translated_question(self, lang):
        if lang == 'en' or not getattr(self, f"question_{lang}", None):
            return self.question
        return getattr(self, f"question_{lang}")

    def get_translated_answer(self, lang):
        if lang == 'en' or not getattr(self, f"answer_{lang}", None):
            return self.answer
        return getattr(self, f"answer_{lang}")

    def save(self, *args, **kwargs):
        translator = Translator()
        if not self.question_hi:
            try:
                translated = translator.translate(self.question, dest='hi')
                self.question_hi = translated.text
            except Exception:
                self.question_hi = self.question
        if not self.answer_hi:
            try:
                translated = translator.translate(self.answer, dest='hi')
                self.answer_hi = translated.text
            except Exception:
                self.answer_hi = self.answer
        if not self.question_bn:
            try:
                translated = translator.translate(self.question, dest='bn')
                self.question_bn = translated.text
            except Exception:
                self.question_bn = self.question
        if not self.answer_bn:
            try:
                translated = translator.translate(self.answer, dest='bn')
                self.answer_bn = translated.text
            except Exception:
                self.answer_bn = self.answer

        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
