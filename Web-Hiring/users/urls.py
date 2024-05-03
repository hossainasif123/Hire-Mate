from django.urls import path
from . import views
from friend.views import(
	send_friend_request,
	friend_requests,
	accept_friend_request,
	remove_friend,
	decline_friend_request,
	cancel_friend_request,
	friends_list_view,
)
urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('account/', views.userAccount, name="account"),

    path('edit-account/', views.editAccount, name="edit-account"),

    path('create-skill/', views.createSkill, name="create-skill"),
    path('update-skill/<str:pk>/', views.updateSkill, name="update-skill"),
    path('delete-skill/<str:pk>/', views.deleteSkill, name="delete-skill"),

    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>/', views.viewMessage, name="message"),
    path('create-message/<str:pk>/', views.createMessage, name="create-message"),
    path('list/<user_id>', friends_list_view, name='list'),
	path('friend_remove/', remove_friend, name='remove-friend'),
    path('friend_request/', send_friend_request, name='friend-request'),
    path('friend_request_cancel/', cancel_friend_request, name='friend-request-cancel'),
    path('friend_requests/<user_id>/', friend_requests, name='friend-requests'),
    path('friend_request_accept/<friend_request_id>/', accept_friend_request, name='friend-request-accept'),
    path('friend_request_decline/<friend_request_id>/', decline_friend_request, name='friend-request-decline'),
    
   
]
          
  