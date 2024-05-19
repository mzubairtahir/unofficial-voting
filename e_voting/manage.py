#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv

load_dotenv()

def main():
    """Run administrative tasks."""
    debug = os.environ.get("DEBUG")
    if(debug):
        if debug=="True":
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_voting.settings.development')
        elif debug=="False":
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_voting.settings.production')
    else:
        raise Exception("Could not get mode from env.")
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
