from django.test import TestCase

class WorkerTestCase(TestCase):
    def test_open_workers_list(self):
        response = self.client.get("/workers/")
        assert response.status_code == 200
