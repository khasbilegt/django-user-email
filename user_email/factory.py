import factory

from .models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Faker("name")
    email = factory.Sequence(lambda n: f"person_{n}@email.com")
    is_active = True
