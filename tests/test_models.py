import faker
from django.db.utils import IntegrityError
from django.test import TransactionTestCase

from user_email.factory import User, UserFactory


class UserManagerTestCase(TransactionTestCase):
    fields = ("is_active", "is_staff", "is_superuser")

    def test_create_user(self):
        for case in (None, False, True):
            with self.subTest(case=case):
                extra_fields = {"is_active": case, "is_staff": case, "is_superuser": case} if type(case) is bool else {}
                instance = UserFactory.build(**extra_fields)
                user = User.objects.create_user(instance.name, instance.email, "password", **extra_fields)

                self.assertEqual(user.name, instance.name)
                self.assertEqual(user.email, instance.email)
                for field in self.fields:
                    self.assertEqual(getattr(user, field), bool(case))

    def test_create_superuser(self):
        for case in (None, True):
            with self.subTest(case=case):
                extra_fields = {"is_active": True, "is_staff": True, "is_superuser": True}
                instance = UserFactory.build(**extra_fields)
                user = User.objects.create_superuser(
                    instance.name, instance.email, "password", **extra_fields if case else {}
                )

                self.assertEqual(user.name, instance.name)
                self.assertEqual(user.email, instance.email)
                for field in self.fields:
                    self.assertEqual(getattr(user, field), True)

    def test_create_superuser_with_false_fields(self):
        f = faker.Faker()

        for field in self.fields:
            with self.subTest(field=field):
                self.assertRaises(
                    ValueError,
                    lambda _: User.objects.create_superuser(
                        f.name(),
                        f.email(),
                        "password",
                        **{_field: False if field == _field else True for _field in self.fields},
                    ),
                    f"Superuser must have {field}=True.",
                )

    def test_user_unique_constraint(self):
        user = UserFactory()

        with self.assertRaises(IntegrityError):
            User.objects.create_user(user.name, user.email, "password", **{field: True for field in self.fields})
