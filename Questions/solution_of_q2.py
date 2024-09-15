'''Yes, by default, Django signals run in the same thread as the caller. 
   This means that when a signal is sent, the signal handler runs in the same
   thread as the function that triggered the signal.
   
Proof:
We can create a signal and log the thread IDs of both the signal sender and
the signal handler. If the thread IDs match, it proves that they are running
in the same thread.'''

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal handler
@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")

# Simulate saving a user
def create_user():
    print(f"Caller thread ID: {threading.get_ident()}")
    user = User(username="test_user")
    user.save()

# Call the function
create_user()
