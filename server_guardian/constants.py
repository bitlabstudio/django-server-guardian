"""Collection of constants fo the ``server_guardian`` app."""


SERVER_STATUS = {  # pragma: no cover
    'OK': 'OK',
    'WARNING': 'WARNING',
    'DANGER': 'DANGER',
}


HTML_STATUS_FALLBACK = {  # pragma: no cover
    'status': SERVER_STATUS['DANGER'],
    'info': 'JSON response could not be decoded.'
}
