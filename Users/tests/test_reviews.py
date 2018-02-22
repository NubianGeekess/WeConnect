# app/tests/test_review.py
#This script tests the functionality of Review class

from tests.test_weconnectusers import WeConnectTestCase


class TestReview(WeConnectTestCase):
    Test Review class functionality.

    def test_review_creation(self):
        #Test if review is created

        self.weconnect.register(self.user)
        self.weconnect.create_category(
            'ivansafari', 'Insurance', 'For all your solutions on the life assurance scheme')
        self.weconnect.create_location('ivansafari', 'Kampala', 'Loc001')
        self.weconnect.create_business(
            'ivansafari', 'AIM Assurance', 'For all your solutions on the life assurance scheme',
            'Insurance', 'Kampala', 'path to logo')
        reviews = self.weconnect.create_review(
            'ivansafari', 'Good service', 'I even got free consultancy for a month', 'AIM Assurance')

        self.assertTrue(reviews['Good service'], msg='Review was not created')

    def test_review_view(self):
        #Test if review is viewed

        self.weconnect.register(self.user)
        self.weconnect.create_category(
            'ivansafari', 'Insurance', 'For all your solutions on the life assurance scheme')
        self.weconnect.create_location('ivansafari', 'Kampala', 'Loc001')
        self.weconnect.create_business(
            'ivansafari', 'AIM Assurance', 'For all your solutions on the life assurance scheme',
            'Insurance', 'Kampala', 'path to logo')
        self.weconnect.create_review(
            'ivansafari', 'Good service', 'I even got free consultancy for a month', 'AIM Assurance)
        review = self.weconnect.view_review('ivansafari', 'Good service')

        self.assertEqual('Good service', review.name, msg='Review does not exist')

    def test_review_edit(self):
        #Test if review is edited

        self.weconnect.register(self.user)
        self.weconnect.create_category(
            'ivansafari', 'Insurance', 'For all your solutions on the life assurance scheme')
        self.weconnect.create_location('ivansafari', 'Kampala', 'Loc001')
        self.weconnect.create_business(
            'ivansafari', 'AIM Assurance', 'For all your solutions on the life assurance scheme',
            'Insurance', 'Kampala', 'path to logo')
        self.weconnect.create_review(
            'ivansafari', 'Good service', 'I even got free consultancy for a month', 'AIM Assurance)
        reviews = self.weconnect.edit_review(
            'ivansafari', 'Good service', 'I even got free consultancy for a month', 'AIM Assurance)

        self.assertEqual('I even got free consultancy for a month',
                         reviews['Good service'].description, msg='Review was not edited')

    def test_review_deletion(self):
        #Test if review is deleted

        self.weconnect.register(self.user)
        self.weconnect.create_category(
            'ivansafari', 'Insurance', 'For all your solutions on the life assurance scheme')
        self.weconnect.create_location('ivansafari', 'Kampala', 'Loc001')
        self.weconnect.create_business(
            'ivansafari', 'AIM Assurance', 'For all your solutions on the life assurance scheme',
            'Insurance', 'Kampala', 'path to logo')
        self.weconnect.create_review(
            'ivansafari', 'Good service', 'I even got free consultancy for a year', 'AIM Assurance')
        reviews = self.weconnect.delete_review('ivansafari', 'Good service')

        self.assertNotIn('Good service', reviews.keys(),
                         msg='Review was not deleted')
