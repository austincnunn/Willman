#!/bin/bash
set -e

# Fix ownership of data directory for bind mounts
# This runs as root before dropping to the 'willman' user
if [ -d "/app/data" ]; then
    chown -R willman:willman /app/data
fi

# Create uploads directory if it doesn't exist
mkdir -p /app/data/uploads
chown -R willman:willman /app/data

# Run database migrations as the willman user
gosu willman flask db upgrade 2>/dev/null || true

# Drop to 'willman' user and run the application
exec gosu willman "$@"
