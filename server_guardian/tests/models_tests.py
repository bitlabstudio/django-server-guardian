"""Tests for the models of the server_guardian app."""
from django.test import TestCase

from mixer.backend.django import mixer

from server_guardian import constants


class ServerTestCase(TestCase):
    """Tests for the ``Server`` model class."""
    longMessage = True

    def test_instantiation(self):
        server = mixer.blend('server_guardian.Server')
        self.assertTrue(server.pk)

    def test_get_response_dict(self):
        json_response = '{"status": "OK", "info": "it is OK"}'
        server = mixer.blend('server_guardian.Server',
                             response_body=json_response)
        self.assertEqual(server.get_response_dict()['status'],
                         constants.SERVER_STATUS['OK'],
                         msg=(
                             'It should be possible to read the status from the'
                             ' response dict.'
                         ))
        self.assertEqual(server.get_response_dict()['info'],
                         'it is OK',
                         msg=(
                             'It should be possible to read the info from the'
                             ' response dict.'
                         ))
        html_response = '<html><head></head><body>HTML RESPONSE</body></html>'
        server2 = mixer.blend('server_guardian.Server',
                              response_body=html_response)
        self.assertEqual(server2.get_response_dict()['status'],
                         constants.SERVER_STATUS['DANGER'],
                         msg=(
                             'For an HTML response, the dict should return a'
                             ' warning status.'
                         ))
