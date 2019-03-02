from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Board, Note
from users.models import CustomUser
from .serializers import BoardSerializer, NoteSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_board(name, isPrivate, ownerId):
        if name != "" and isPrivate is not None:
            owner = CustomUser.objects.get(id=ownerId)
            Board.objects.create(name=name, isPrivate=isPrivate, owner=owner)

    def setUp(self):
        # add test data
        owner1 = CustomUser.objects.create(username='admin', email='admin@admin.com', password='admin')
        owner2 = CustomUser.objects.create(username='user', email='user@user.com', password='user')
        self.create_board("Board 1", True,  1)
        self.create_board("Board 2", False, 1)
        self.create_board("Board 3", True,  2)
        self.create_board("Board 4", False, 2)


class GetAllBoardsTest(BaseViewTest):

    def test_get_all_boards_unauthenticated(self):
        """
        This test ensures that the API forbids access to the boards/
        endpoint if the reques is not authenticated
        """
        # hit the API endpoint
        response = self.client.get('/api/v1/boards/')
        # Expect a 403 status
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_all_boards_authenticated(self):
        """
        This test ensures that all boards added in the setUp method
        exist when we make a GET request to the boards/ endpoint
        """
        #Authenticate
        user = CustomUser.objects.get(username='admin')
        self.client.force_authenticate(user=user)
        # hit the API endpoint
        response = self.client.get('/api/v1/boards/')
        # fetch the data from db
        expected = Board.objects.all()
        serialized = BoardSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PostBoardTest(BaseViewTest):

    def test_post_board_unauthenticated(self):
        """
        This test ensures that the API forbids access to the boards/
        endpoint if the reques is not authenticated
        """
        # hit the API endpoint
        response = self.client.post('/api/v1/boards/')
        # Expect a 403 status
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_board_authenticated(self):
        """
        This test ensures that an authenticated user is able to create
        a board with the right fields
        """
        #Authenticate
        user = CustomUser.objects.get(username='admin')
        self.client.force_authenticate(user=user)
        board = {"name": "adminBoard","isPrivate": False}
        # hit the API endpoint
        response = self.client.post('/api/v1/boards/', board, format='json')
        # fetch the data from db
        expected = Board.objects.get(name='adminBoard')
        self.assertEqual(response.data, board)
        self.assertEqual(expected.owner, user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class PutBoardTest(BaseViewTest):

    def test_put_board_unauthenticated(self):
        """
        This test ensures that the API forbids access to the boards/
        endpoint if the reques is not authenticated
        """
        # hit the API endpoint
        response = self.client.put('/api/v1/boards/1/')
        # Expect a 403 status
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_board_authenticated_owner(self):
        """
        This test ensures that an authenticated user is able to create
        a board with the right fields
        """
        #Authenticate
        owner = CustomUser.objects.get(username='admin')
        self.client.force_authenticate(user=owner)
        board = {"name": "adminBoard","isPrivate": True}
        # hit the API endpoint
        response = self.client.put('/api/v1/boards/1/',board,format='json')
        # fetch the data from db
        self.assertEqual(response.data, board)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_board_authenticated_other(self):
        """
        This test ensures that an authenticated user is able to create
        a board with the right fields
        """
        #Authenticate
        user = CustomUser.objects.get(username='user')
        self.client.force_authenticate(user=user)
        board = {"name": "adminBoard","isPrivate": True}
        # hit the API endpoint
        response = self.client.put('/api/v1/boards/1/', board, format='json')
        # fetch the data from db        self.assertEqual(response.data, bard)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
