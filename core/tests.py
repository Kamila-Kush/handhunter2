from django.test import TestCase

class HomepageTestCase(TestCase):
    def test_open_homepage_should_success(self):
        response = self.client.get("/")
        assert response.status_code == 200

        # response_1 = self.client.get("/workers")
        # assert response_1.status_code == 301

        title = "Поиск работы и работников"
        self.assertContains(response, title)

    def test_post_request_homepage_should_405(self):
        response = self.client.post('/')
        assert response.status_code == 405

