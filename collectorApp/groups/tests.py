from django.test import TestCase
from .models import Group, GroupMember
from django.contrib.auth import get_user_model

User = get_user_model()

class GroupModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpass'
        )
        self.group = Group.objects.create(
            name='Test Group',
            description='This is a test group',
        )
        self.group_member = GroupMember.objects.create(
            group=self.group,
            user=self.user
        )

    def test_group_creation(self):
        self.assertEqual(self.group.name, 'Test Group')
        self.assertEqual(self.group.description, 'This is a test group')

    def test_group_member_creation(self):
        self.assertEqual(self.group_member.group, self.group)
        self.assertEqual(self.group_member.user, self.user)

class GroupTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user1 = User.objects.create_user(username='user1', password='pass')
        self.user2 = User.objects.create_user(username='user2', password='pass')
        self.group = Group.objects.create(name='Test Group', description='A test group')

    def test_join_group(self):
        # Test user1 joining the group
        self.group.members.add(self.user1)
        self.assertEqual(self.group.members.count(), 1)
        self.assertEqual(self.group.members.first(), self.user1)
        # Test user2 joining the group
        self.group.members.add(self.user2)
        self.assertEqual(self.group.members.count(), 2)
        self.assertEqual(self.group.members.last(), self.user2)

    def test_leave_group(self):
        # Add both users to the group first
        self.group.members.add(self.user1, self.user2)
        self.assertEqual(self.group.members.count(), 2)
        # Test user1 leaving the group
        self.group.members.remove(self.user1)
        self.assertEqual(self.group.members.count(), 1)
        self.assertEqual(self.group.members.first(), self.user2)
        # Test user2 leaving the group
        self.group.members.remove(self.user2)
        self.assertEqual(self.group.members.count(), 0)

