"""Collection of constants fo the ``server_guardian`` app."""


SERVER_STATUS = {
    'OK': 'OK',
    'WARNING': 'WARNING',
    'DANGER': 'DANGER',
}


HTML_STATUS_FALLBACK = {
    'status': SERVER_STATUS['DANGER'],
    'info': 'JSON response could not be decoded.'
}
