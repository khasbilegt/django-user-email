import factory

from .models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Faker("name")
    email = factory.Faker("email")
    is_active = True
