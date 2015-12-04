"""Tests for the models of the server_guardian app."""
from django.test import TestCase

from mixer.backend.django import mixer


class ServerTestCase(TestCase):
    """Tests for the ``Server`` model class."""
    longMessage = True

    def test_instantiation(self):
        server = mixer.blend('server_guardian.Server')
        self.assertTrue(server.pk)

