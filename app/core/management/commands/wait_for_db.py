"""
Django command to wait for the database to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError 
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    """Django command to wait for the database to be available"""
    def handle(self, *args, **kwargs):
        "Entrypoint for command to wait for the database to be available"
        self.stdout.write("Waiting for database...")
        db_up=False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up=True
            except (OperationalError, Psycopg2OpError) :
                self.stdout.write("Database not available, waiting 1 second")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))