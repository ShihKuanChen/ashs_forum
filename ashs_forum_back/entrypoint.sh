#!/bin/bash
set -e

SQLALCHEMY_DATABASE_URI=$SUPER_DATABASE_URI \
flask db upgrade

exec "$@"