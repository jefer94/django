from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from projects.models import Project
from .projects_tests import create_project

data = {
    'title': 'asdsad1',
    'code': 'asdsad2',
    'project': 1 }

def create_code(self):
    create_project(self)
    url = '/codes'    
    response = self.client.post(url, data, format='json')

    print('================', response.data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(response.data['id'], 1)
    self.assertEqual(response.data['title'], data['title'])
    self.assertEqual(response.data['code'], data['code'])
    self.assertEqual(response.data['project'], data['project'])

def delete_code(self):
    create_code(self)
    url = '/codes/1'
    response = self.client.delete(url, format='json')
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class RoutesTests(APITestCase):
    def test_empty_codes(self):
        url = '/codes'
        response = self.client.get(url, format='json')

        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_code(self):
        create_code(self)

    # def test_code_with_id_1(self):
    #     create_code(self)
    #     url = '/codes/1'
    #     response = self.client.get(url, format='json')

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['id'], 1)
    #     self.assertEqual(response.data['user'], data['user'])
    #     self.assertEqual(response.data['name'], data['name'])
    #     self.assertEqual(response.data['description'], data['description'])

    # def test_codes_with_length_1(self):
    #     create_code(self)
    #     url = '/codes'
    #     response = self.client.get(url, format='json')

    #     self.assertEqual(len(response.data), 1)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data[0]['id'], 1)
    #     self.assertEqual(response.data[0]['user'], data['user'])
    #     self.assertEqual(response.data[0]['name'], data['name'])
    #     self.assertEqual(response.data[0]['description'], data['description'])

    # def test_delete_code_with_id_1_but_not_exist(self):
    #     url = '/codes/1'
    #     response = self.client.delete(url, format='json')

    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    #     self.assertEqual(len(response.data), 1)
    #     self.assertEqual(response.data['detail'], 'Not found.')

    # def test_empty_codes_again(self):
    #     delete_code(self)
    #     url = '/codes'
    #     response = self.client.get(url, format='json')

    #     self.assertEqual(len(response.data), 0)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
