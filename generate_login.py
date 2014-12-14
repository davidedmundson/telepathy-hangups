#!/bin/python
import hangups
from os.path import expanduser

hangups.auth.get_auth_stdin(expanduser("~/.hangups_auth_tmp"))
