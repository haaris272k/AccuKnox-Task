'''By default, Django signals are executed synchronously. 
This means that the signal handler will run in the same thread
and context as the signal sender, which can block execution until 
the signal is fully processed.

Proof:
We can create a Django signal and demonstrate that it runs synchronously
by adding a delay in the signal handler. If the signal were asynchronous,
the delay would not block the main thread'''


import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal handler
@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    print("Signal received!")
    time.sleep(5)  # Simulate a time-consuming task
    print("Handler finished processing!")

# Simulate saving a user
def create_user():
    print("Creating user...")
    user = User(username="test_user")
    user.save()
    print("User creation done!")

# Call the function
create_user()
