from rest_framework.routers import DefaultRouter
from boards.api import BoardViewSet, NoteViewSet
 
 
router = DefaultRouter()
 
router.register('boards', BoardViewSet)
router.register('notes', NoteViewSet)
