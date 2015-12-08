"""The command, that fetches the information from the configured servers."""
import sys
import json

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import now

import requests
from django_libs.utils_email import send_email

from ... import default_settings
from ...models import Server
from ...constants import SERVER_STATUS


class Command(BaseCommand):

    def send_error_email(self, server):
        context = {
            'server': server,
        }
        send_email(
            request={},
            extra_context=context,
            subject_template='server_guardian/email/email_subject.html',
            body_template='server_guardian/email/warning_email_body.html',
            from_email=settings.FROM_EMAIL,
            recipients=[admin[0] for admin in settings.ADMINS],
        )

    def get_email_required(self, server):
        """
        Send a warning email, if the server response contains errors.

        This includes when the server reports a status of "DANGER" or if the
        json response failed to decode or if the response code was within the
        EMAIL_ON_STATUS settings.

        """
        if server.status_code in default_settings.EMAIL_ON_STATUS:
            return True

        try:
            if server.get_response_dict()['status'] == SERVER_STATUS[
                    'DANGER']:
                return True
        except KeyError as ex:
            server.response_body = (
                'Server got an error "{0}" and returned the following content:'
                '{1}'.format(ex, server.response_body)
            )
            server.save()
            return True

        return False

    def handle(self, *args, **options):

        count = 0
        mails_sent = 0

        for server in Server.objects.all():
            # TODO add security token
            response = requests.get(url=server.url)
            server.response_body = response.content
            server.status_code = response.status_code
            server.last_updated = now()
            server.save()
            if self.get_email_required(server):
                self.send_error_email(server)
                mails_sent += 1
            count += 1

        sys.stdout.write(
            '[{0}] Updated {1} servers. Sent {2} warning emails.\n'.format(
                now(), count, mails_sent)
        )
