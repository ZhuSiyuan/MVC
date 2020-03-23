
import pytest
from myRESTfulTodoList import app


class TestClass(object):

    def setup_class(self):
        # 测试开始时首先执行，准备工作
        app.config['TESTING'] = True
        self.app = app.test_client()

    def teardown_class(self):
        # 测试结束时执行，收尾工作，关闭资源
        pass

    def test_query_all(self):
        response = self.app.get('/api/tasks/')
        print(str(response.data, encoding='utf-8'))
        assert 200 == response.status_code

    def test_insert(self):
        response = self.app.post('/api/tasks/')
        assert 403 == response.status_code

        response = self.app.post('/api/tasks/1')
        assert 405 == response.status_code

        data = '{"id":1, "content": "test_insert"}'
        response = self.app.post('/api/tasks/', data=data)
        assert 403 == response.status_code

        data = '{"id":2, "content": "test_insert"}'
        response = self.app.post('/api/tasks/', data=data)
        assert 200 == response.status_code

    def test_query_by_id(self):
        response = self.app.get('/api/tasks/1')
        assert 200 == response.status_code

        response = self.app.get('/api/tasks/1x')
        assert 403 == response.status_code

    def test_delete_by_id(self):
        response = self.app.delete('/api/tasks/2')
        assert 200 == response.status_code

        response = self.app.delete('/api/tasks/2')
        assert 404 == response.status_code


if __name__ =="__main__":
    pytest.main(['test.py','-s'])
