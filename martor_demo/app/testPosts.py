from django.test import TestCase
from app.models import Post


class PostTestCase(TestCase):
    def testPost(self):
        post = Post(
            title="Título",
            description="Esto es una prueba(test)",
            wiki="Cuerpo del post\n Creo que estamos\
            creando una instancia de la clase Post puede ser ?")
        self.assertEqual(post.title, "Título")
