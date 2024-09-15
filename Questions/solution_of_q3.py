'''By default, Django signals do run in the same database transaction as the caller.
   This means that if the database transaction fails or is rolled back, any changes
   or actions triggered by signals within the transaction will also be rolled back.

Proof:
We can demonstrate this by combining a signal and an explicit database transaction.
If the transaction is rolled back, the changes triggered by the signal should also be
rolled back, proving that signals run in the same database transaction.'''

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import models

# A simple log model to track if the signal was executed
class SignalLog(models.Model):
    message = models.CharField(max_length=100)

# Signal handler
@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    print("Signal handler executing...")
    SignalLog.objects.create(message="Signal executed for user creation")

# Simulate saving a user within a transaction
def create_user_with_transaction():
    try:
        with transaction.atomic():  # Start a transaction
            print("Transaction started")
            user = User(username="test_user")
            user.save()  # This will trigger the signal
            raise Exception("Something went wrong!")  # Force a transaction rollback
    except Exception as e:
        print(f"Exception: {e}")

    # Check if the signal log was saved
    log_count = SignalLog.objects.count()
    print(f"SignalLog count: {log_count}")

# Call the function
create_user_with_transaction()
