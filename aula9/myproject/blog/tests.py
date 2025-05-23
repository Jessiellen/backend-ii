from django.test import TestCase
import pytest
from blog.models import BlogPost

@pytest.mark.django_db
def test_blogpost_creation():
    post = BlogPost.objects.create(
        title="Meu primeiro post",
        content="Conteúdo do post"
    )
    assert post.title == "Meu primeiro post"
    assert post.content == "Conteúdo do post"
    assert post.published_at is not None

@pytest.mark.django_db
def test_blogpost_str():
    post = BlogPost(title="Teste __str__")
    assert str(post) == "Teste __str__"

