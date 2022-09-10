from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from api.tickets.views import TicketViewSet
from api.users.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet, basename="users")
router.register("tickets", TicketViewSet, basename="tickets")


app_name = "api"
urlpatterns = router.urls
