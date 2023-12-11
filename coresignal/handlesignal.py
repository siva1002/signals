# blog/signals.py
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
User=get_user_model()
# Define the signal

@receiver(pre_save,sender=User)
def send_notification(sender, **kwargs):
    """
    This function will be called whenever the new_blog_post_signal is sent.
    """
    # Get the newly created blog post
    # blog_post = kwargs['instance']

    # # Simulate sending a notification to site administrators
    # admins = User.objects.filter(is_staff=True)
    # for admin in admins:
    #     # Replace this print statement with actual notification sending logic
    obj=kwargs.get('instance')
    obj.username='No a given user'
    print(f"function call useing signals",kwargs)