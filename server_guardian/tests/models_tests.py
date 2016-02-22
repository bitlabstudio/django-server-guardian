"""Tests for the models of the server_guardian app."""
from django.test import TestCase
from mixer.backend.django import mixer
from server_guardian import constants

from ..models import get_parsed_response


class ServerTestCase(TestCase):
    """Tests for the ``Server`` model class."""
    longMessage = True

    def test_instantiation(self):
        server = mixer.blend('server_guardian.Server')
        self.assertTrue(server.pk)


class ServerLogTestCase(TestCase):
    """Tests for the ``ServerLog`` model class."""
    longMessage = True

    def test_instantiation(self):
        server_log = mixer.blend('server_guardian.ServerLog')
        self.assertTrue(server_log.pk)


class GetParsedResponseTestCase(TestCase):
    """Tests for the ``get_parsed_response`` function."""
    longMessage = True

    def test_get_parsed_response(self):
        json_response = (
            '[{"label": "foobar", "status": "OK", "info": "it is OK"}]'
        )
        self.assertEqual(
            get_parsed_response(json_response)[0]['status'],
            constants.SERVER_STATUS['OK'],
            msg=(
                'Should return a status of OK. Info: {0}'.format(
                    get_parsed_response(json_response)
                )
            )
        )
        self.assertEqual(
            get_parsed_response(json_response)[0]['info'],
            'it is OK',
            msg=(
                'It should be possible to read the info from the'
                ' response dict.'
            )
        )
        html_response = '<html><head></head><body>HTML RESPONSE</body></html>'
        self.assertEqual(
            get_parsed_response(html_response)[0]['status'],
            constants.SERVER_STATUS['DANGER'],
            msg=(
                'For an HTML response, the dict should return a'
                ' warning status.'
            )
        )
