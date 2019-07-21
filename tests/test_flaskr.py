import os
import tempfile

import pytest

from flaskr import create_app


@pytest.fixture
def client():
        
    flaskr.app.config['TESTING'] = True
    client = flaskr.app.test_client()

    flaskr.init_db()
           

    yield client

    os.close(db_fd)
    os.unlink(flaskr.app.config['DATABASE'])