from django.test import TestCase, Client, RequestFactory
from note.models import *
from note.views import *

class userTests(TestCase):

    def test_add_user(self):
        """Users can be added to the database"""
        user = User(username="JohnDoe", password="testPass")
        user.save()
        profile = UserProfile(user=user)
        profile.save()
        self.assertEquals(profile, UserProfile.objects.get(user=user))

    def test_add_note(self):
        """Notes are created correctly"""
        note = Note(title="test")
        self.assertEquals(note.title, "test")

    def test_add_note_document(self):
        """Documents are added to notes"""
        note = Note(title="test", file=self.client.get("/static/images/default.jpg"))
        self.assertNotEquals(note.file, None)

    def test_note_in_module(self):
        """Notes can be found in subjects"""
        note = Note(title="test", subject="mathematics", module="1R: Calculus")
        self.assertEquals(note.subject, "mathematics")

    def test_note_date(self):
        """Notes are added with correct date"""
        note = Note(title="test", date=datetime.now())
        self.assertEquals(datetime.now().day, note.date.day)