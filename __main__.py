#!/usr/bin/env python3

from App import application, APP_PORT

if __name__ == '__main__':
    application.run(host="0.0.0.0", port=APP_PORT)
