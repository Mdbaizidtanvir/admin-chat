from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="media/images/" ,default="media/avatar.png")

    def __str__(self):
        return self.user.username
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.profile.save()


@receiver(pre_delete, sender=User)
def delete_user_profile(sender, instance, **kwargs):
    instance.profile.delete()

class Message(models.Model):

    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to="message_attachments/", blank=True, null=True)


    class Meta:
        ordering = ("date_created",)