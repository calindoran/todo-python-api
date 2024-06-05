#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Apply any outstanding database migrations
sleep 10
python3 manage.py makemigrations
python3 manage.py migrate

# Convert static asset files
python manage.py collectstatic --no-input