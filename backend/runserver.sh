#!/bin/bash
cd $(dirname $0)
uwsgi --ini ./uwsgi.ini
