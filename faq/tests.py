from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python web framework."
        )

    def test_get_translated_question_default(self):
        self.assertEqual(self.faq.get_translated_question('en'), "What is Django?")

    def test_get_translated_question_hindi(self):
        translated_question = self.faq.get_translated_question('hi')
        self.assertTrue(translated_question, "Expected a translated response for Hindi.")

    def test_get_translated_question_bengali(self):
        translated_question = self.faq.get_translated_question('bn')
        self.assertTrue(translated_question, "Expected a translated response for Bengali.")


class FAQAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python web framework."
        )

    def test_api_default_language(self):
        url = reverse('faq-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['question'], "What is Django?")

    def test_api_with_language_hindi(self):
        url = reverse('faq-list') + '?lang=hi'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data[0]['question'], "Expected translated text in Hindi.")

    def test_api_with_language_bengali(self):
        url = reverse('faq-list') + '?lang=bn'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data[0]['question'], "Expected translated text in Bengali.")

    
