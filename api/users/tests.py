from django.contrib.auth import get_user_model
from django.test import TestCase


class UserTests(TestCase):
    User = get_user_model()

    def test_create_user(self):
        user = self.User.objects.create_user(
            name="Test User",
            email="test@email.com",
            phone="+34 555 55 55 55",
            origin="Spain",
        )

        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@email.com")
        self.assertEqual(user.phone, "+34 555 55 55 55")
        self.assertEqual(user.origin, "Spain")

        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_without_origin(self):
        user = self.User.objects.create_user(
            name="Test User",
            email="test@email.com",
            phone="+34 555 55 55 55",
        )

        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@email.com")
        self.assertEqual(user.phone, "+34 555 55 55 55")

        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_update_user(self):
        self.User.objects.create_user(
            name="Test User",
            email="test@email.com",
            phone="+34 555 55 55 55",
            origin="Italy",
        )

        user = self.User.objects.get(email="test@email.com")

        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@email.com")
        self.assertEqual(user.phone, "+34 555 55 55 55")
        self.assertEqual(user.origin, "Italy")

        user.name = "Test User (updated)"
        user.phone = "+34 666 66 66 66"
        user.origin = "Portugal"
        user.save()

        self.assertEqual(user.name, "Test User (updated)")
        self.assertEqual(user.phone, "+34 666 66 66 66")
        self.assertEqual(user.origin, "Portugal")

    def test_update_user_without_previous_origin(self):
        self.User.objects.create_user(
            name="Test User",
            email="test@email.com",
            phone="+34 555 55 55 55",
        )

        user = self.User.objects.get(email="test@email.com")

        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@email.com")
        self.assertEqual(user.phone, "+34 555 55 55 55")

        user.name = "Test User (updated)"
        user.phone = "+34 666 66 66 66"
        user.origin = "Portugal"
        user.save()

        self.assertEqual(user.name, "Test User (updated)")
        self.assertEqual(user.phone, "+34 666 66 66 66")
        self.assertEqual(user.origin, "Portugal")

    def test_update_user_with_previous_origin__no_change(self):
        self.User.objects.create_user(
            name="Test User",
            email="test@email.com",
            phone="+34 555 55 55 55",
            origin="Italy",
        )

        user = self.User.objects.get(email="test@email.com")

        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@email.com")
        self.assertEqual(user.phone, "+34 555 55 55 55")
        self.assertEqual(user.origin, "Italy")

        user.name = "Test User (updated)"
        user.phone = "+34 666 66 66 66"
        user.save()

        self.assertEqual(user.name, "Test User (updated)")
        self.assertEqual(user.phone, "+34 666 66 66 66")
        self.assertEqual(user.origin, "Italy")

    def test_create_superuser(self):
        admin_user = self.User.objects.create_superuser(
            name="Test Super User",
            email="test_super@email.com",
            phone="ext 0123",
            origin="France",
            password="testpassword123_",
        )

        self.assertEqual(admin_user.name, "Test Super User")
        self.assertEqual(admin_user.email, "test_super@email.com")
        self.assertEqual(admin_user.phone, "ext 0123")
        self.assertEqual(admin_user.origin, "France")

        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_create_superuser_without_origin(self):
        admin_user = self.User.objects.create_superuser(
            name="Test Super User",
            email="test_super@email.com",
            phone="ext 0123",
            password="testpassword123_",
        )

        self.assertEqual(admin_user.name, "Test Super User")
        self.assertEqual(admin_user.email, "test_super@email.com")
        self.assertEqual(admin_user.phone, "ext 0123")

        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
