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

# Generate SECRET_KEY on first launch and persist it
KEY_FILE=/app/data/.secret_key
if [ ! -f "$KEY_FILE" ]; then
    echo "Generating new SECRET_KEY..."
    python3 -c "import secrets; print(secrets.token_hex(32))" > "$KEY_FILE"
    chmod 600 "$KEY_FILE"
    chown willman:willman "$KEY_FILE"
fi
export SECRET_KEY=$(cat "$KEY_FILE")

# Run database migrations as the willman user
gosu willman flask db upgrade 2>/dev/null || true

# Drop to 'willman' user and run the application
exec gosu willman "$@"
