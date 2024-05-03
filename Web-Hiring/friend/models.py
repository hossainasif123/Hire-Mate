from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class FriendList(models.Model):
    user =models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="user")
    friends =models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name="friends")
    def __str__(self):
       
       return self.user.username
    def add_friend(self,account):
        if not account in self.friend.all():
            self.friends.add(account)
            self.save()

    def remove_friend(self,account):
        if account in self.friends.all():
            self.friend.remove(account)
    def unfriend(self,removee):  

        remover_friends_list =self 
    
        remover_friends_list.remove_friend(removee)
        friend_list = FriendList.objects.get(user=removee)
        friend_list.remove_friend(self.user)
    def is_mutual_friend(self,friend):
        if friend in self.friends.all():
            return True
        return False




class FriendRequest(models.Model):
    """
       1)SENDER:
       sender will sending the friend request
       2)RECEiVER:
       person receiving the friend request
    """
    sender =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="sender")
    receiver=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="receiver")
    is_active = models.BooleanField(blank=True,null=False,default=True)
    
    timestamp =models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.sender.username
    
    def accept(self):
       receiver_friend_list =FriendList.objects.get(user=self.receiver)
       if receiver_friend_list:
            receiver_friend_list.add_friend(self.sender)
            sender_friend_list=FriendList.objects.get(user=self.sender)
            if sender_friend_list:
                sender_friend_list.add_friend(self.receiver)
                self.is_active= False
                self.save()
    

    def decline(self):
        """
        Decline a friend request.
        It is "declined " by setting the 'is_active' field to False
        """
        self.is_active = False
        self.save()

    def cancel(self):
       
       """
       cancel a friend request it is cancelled by setting the 'is_active' field to False.This is only different with respect to "declinig" through the notification that is generated.
       """
       self.is_active=False

from django.db import models
from users.models import Profile

class Notification(models.Model):
    recipient = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='notifications_received')
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.recipient.user.username} - {self.message}'
      
    