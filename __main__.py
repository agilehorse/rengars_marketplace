#!/usr/bin/env python3
import os

from App import application

if __name__ == '__main__':
    application.run(port=os.environ.get("APP_PORT", 5000))
