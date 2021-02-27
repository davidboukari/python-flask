from app.bin.app_srv import app


'''Test test_app_srv'''


class TestAppSrv:
    @staticmethod
    def test_app_root():
        response = app.test_client().get('/')
        assert response.status_code == 200
