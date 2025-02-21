import os
from backend_python import create_app
import pytest
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@pytest.fixture
def client():
    # Use the same database URL from .env
    os.environ['DATABASE_URL'] = os.getenv('DATABASE_URL')
    
    app = create_app('testing')
    with app.test_client() as client:
        yield client

def test_get_words(client):
    """Test GET /api/words endpoint"""
    response = client.get('/api/words')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    if len(data) > 0:
        word = data[0]
        assert 'characters' in word
        assert 'pinyin' in word
        assert 'english' in word

def test_get_groups(client):
    """Test GET /api/groups endpoint"""
    response = client.get('/api/groups')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    if len(data) > 0:
        group = data[0]
        assert 'name' in group
        assert 'words_count' in group

def test_get_study_activities(client):
    """Test GET /api/study-activities endpoint"""
    response = client.get('/api/study-activities')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    if len(data) > 0:
        activity = data[0]
        assert 'name' in activity
        assert 'url' in activity 