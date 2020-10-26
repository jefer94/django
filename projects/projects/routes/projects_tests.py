# from rest_framework.test import APIClient

# client = APIClient()
# client.post('/notes/', {'title': 'new idea'}, format='json')


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from projects.models import Project

data = {
    'user': 'asdsad1',
    'name': 'asdsad2',
    'description': 'asdsad3' }

def create_project(self):
    url = '/projects'    
    response = self.client.post(url, data, format='json')

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(response.data['id'], 1)
    self.assertEqual(response.data['user'], data['user'])
    self.assertEqual(response.data['name'], data['name'])
    self.assertEqual(response.data['description'], data['description'])

def delete_project(self):
    create_project(self)
    url = '/projects/1'
    response = self.client.delete(url, format='json')
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class RoutesTests(APITestCase):
    def test_empty_projects(self):
        url = '/projects'
        response = self.client.get(url, format='json')

        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_project(self):
        create_project(self)

    def test_project_with_id_1(self):
        create_project(self)
        url = '/projects/1'
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['user'], data['user'])
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['description'], data['description'])

    def test_projects_with_length_1(self):
        create_project(self)
        url = '/projects'
        response = self.client.get(url, format='json')

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'], 1)
        self.assertEqual(response.data[0]['user'], data['user'])
        self.assertEqual(response.data[0]['name'], data['name'])
        self.assertEqual(response.data[0]['description'], data['description'])

    def test_delete_project_with_id_1_but_not_exist(self):
        url = '/projects/1'
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data['detail'], 'Not found.')

    def test_empty_projects_again(self):
        delete_project(self)
        url = '/projects'
        response = self.client.get(url, format='json')

        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
