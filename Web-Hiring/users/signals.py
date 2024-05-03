from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    Signal handler for User model.
    Creates or updates the associated Profile when a User is saved.
    Sends a welcome email for new users.
    """
    if created:
        profile = Profile.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email,
            name=instance.first_name,
        )

        subject = 'Welcome to DevSearch'
        message = 'We are glad you are here!'

        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [profile.email],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Error sending welcome email: {e}")

@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    """
    Signal handler for Profile model.
    Deletes the associated User when a Profile is deleted.
    """
    try:
        instance.user.delete()
    except User.DoesNotExist:
        pass
    except Exception as e:
        print(f"An error occurred while deleting user: {e}")

# Connect signals
post_save.connect(create_or_update_profile, sender=User)
post_delete.connect(delete_user, sender=Profile)
