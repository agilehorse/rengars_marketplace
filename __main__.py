#!/usr/bin/env python3

from App import application
from env_vars import MARKETPLACE_PORT

if __name__ == '__main__':
    application.run(host="0.0.0.0", port=MARKETPLACE_PORT)
