from django.contrib.messages import get_messages
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase, Client
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from task_manager.apps.statuses.models import Status
from task_manager.apps.users.models import User
from task_manager.load_data import from_json


class StatusTestCase(TestCase):
    fixtures = ['users.json', 'statuses.json']
    test_statuses = from_json('test_statuses.json')

    def setUp(self):
        self.client = Client()
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)
        self.status_1 = Status.objects.get(pk=1)
        self.status_2 = Status.objects.get(pk=2)
        self.status_3 = Status.objects.get(pk=3)
        self.count = Status.objects.count()


class TestStatusesListView(StatusTestCase):
    def test_status_view_if_unauthorized(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('statuses_list'))
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message,
                         _('You are not logged in! Please log in.'))
        self.assertEqual(messages[0].level, 40)

    def test_status_view(self):
        response = self.client.get(reverse_lazy('statuses_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/list.html')

    def test_status_columns(self):
        valid_status = self.test_statuses['list']
        response = self.client.get(reverse_lazy('statuses_list'))
        page = str(response.content)
        tag_class = 'class="align-middle"'

        self.assertInHTML(f'<td {tag_class}>{valid_status["id"]}</td>',
                          page)
        self.assertInHTML(f'<td {tag_class}>{valid_status["name"]}</td>',
                          page)
        self.assertInHTML(
            f'<td  {tag_class}>{valid_status["created_at"]}</td>',
            page
        )

    def test_status_rows(self):
        response = self.client.get(reverse_lazy('statuses_list'))
        page = str(response.content)

        self.assertInHTML(self.status_1.name, page)
        self.assertInHTML(self.status_2.name, page)
        self.assertInHTML(self.status_3.name, page)


class TestStatusCreateView(StatusTestCase):
    def test_create_status_if_unauthorized(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('status_create'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_create_status_view(self):
        response = self.client.get(reverse_lazy('status_create'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='statuses/create.html')

    def test_create_status(self):
        valid_status = self.test_statuses['create']
        response = self.client.post(reverse_lazy('status_create'),
                                    data=valid_status)
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses_list'))
        self.assertEqual(Status.objects.count(), self.count + 1)

        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message,
                         _('Status created successfully'))
        self.assertEqual(messages[0].level, 25)


class TestStatusUpdateView(StatusTestCase):
    def test_update_status_if_unauthorized(self):
        self.client.logout()
        response = self.client.get(
            reverse_lazy('status_update', kwargs={'pk': 1})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_update_status_view(self):
        response = self.client.get(
            reverse_lazy('status_update', kwargs={'pk': 2})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='statuses/update.html')

    def test_update_status(self):
        valid_status = self.test_statuses['update']
        response = self.client.post(
            reverse_lazy('status_update', kwargs={'pk': 3}),
            data=valid_status
        )
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses_list'))
        self.assertEqual(Status.objects.get(pk=self.status_3.pk).name,
                         valid_status['name'])
        self.assertEqual(Status.objects.count(), self.count)

        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message,
                         _('Status updated successfully'))
        self.assertEqual(messages[0].level, 25)


class TestStatusDeleteView(StatusTestCase):
    def test_delete_status_if_unauthorized(self):
        self.client.logout()
        response = self.client.get(
            reverse_lazy('status_delete', kwargs={'pk': 3})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_delete_status_view(self):
        response = self.client.get(
            reverse_lazy('status_delete', kwargs={'pk': 3})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='statuses/delete.html')

    def test_delete_status(self):
        response = self.client.post(
            reverse_lazy('status_delete', kwargs={'pk': 3})
        )
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses_list'))

        self.assertEqual(Status.objects.count(), self.count - 1)
        with self.assertRaises(ObjectDoesNotExist):
            Status.objects.get(pk=self.status_3.pk)

        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message,
                         _('Status deleted successfully'))
        self.assertEqual(messages[0].level, 25)
