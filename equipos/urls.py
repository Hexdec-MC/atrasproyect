from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserRegisterView,
    UserRoleUpdateView,
    EquipoViewSet,
    MantenimientoViewSet,
    InformeMecanicoViewSet,
    ChecklistViewSet,
    UsoEquipoViewSet,
    ReservaViewSet,
)

router = DefaultRouter()
router.register(r"equipos", EquipoViewSet)
router.register(r"mantenimientos", MantenimientoViewSet)
router.register(r"informes", InformeMecanicoViewSet)
router.register(r"checklists", ChecklistViewSet)
router.register(r"usos", UsoEquipoViewSet)
router.register(r"reservas", ReservaViewSet)

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path("users/<int:id>/role/", UserRoleUpdateView.as_view(), name="user-role-update"),
    path("", include(router.urls)),  # CRUDs
]
