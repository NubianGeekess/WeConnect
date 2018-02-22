#This script tests the functionality of the business class

from tests.test_weconnectusers import WeConnectTestCase


class TestBusiness(WeConnectTestCase):
    #Test Business class functionality.

    def test_business_creation(self):
        """Test if business is created"""

        self.weconnect.register(self.user)
        self.weconnect.create_category(
            'Ivan Safari', 'AIM Assurance', 'Cat001')
        self.weconnect.create_location('Ivan', 'Kampala', 'Loc001')
        businesses = self.weconnect.create_business(
            'Ivan Safari', 'New in insurance', 'For all your solutions on the life assurance scheme',
            'Insurance', 'Kampala', 'path to logo')

        self.assertTrue(businesses['New in insurance'],
                        msg='Business was not created')

    def test_business_edit(self):
        #Test if business is edited

        self.weconnect.register(self.user)
        self.weconnect.create_category(
            'Ivan Safari', 'Insurance', 'For all your solutions on the life assurance scheme')
        self.weconnect.create_location('Ivan Safari', 'Kampala', 'Loc001')
        self.weconnect.create_business(
            'Ivan Safari', 'New in insurance', 'For all your solutions on the life assurance scheme',
            'Insurance', 'Kampala', 'path to logo')
        businesses = self.weconnect.edit_business(
            'Ivan Safari', 'New in Insurance', 'For all your solutions on the life assurance scheme, consultancy on insurance legalities',
            'Telecommunications', 'Kampala', 'path to logo')

        self.assertEqual('For all your solutions on the life assurance scheme, consultancy on insurance legalities',
                         businesses['New in insurance'].businessProfile, msg='Business was not edited')


    def test_business_view(self):
        #Test if business is viewed

        self.weconnect.register(self.user)
        self.weconnect.create_category(
            'Ivan Safari', 'Insurance', 'For all your latest mobile gadgets')
        self.weconnect.create_location('Ivan Safari', 'Kampala', 'Loc001')
        self.weconnect.create_business(
            'Ivan Safari', 'New in insurance', 'For all your solutions on the life assurance scheme',
            'Insurance', 'Kampala', 'path to logo')
        business = self.weconnect.view_business('Ivan Safari', 'New in insurance')

        self.assertEqual('New in insurance', business.businessName,
                         msg='Business does not exist')


    def test_business_deletion(self):
        #Test if business is deleted

        self.weconnect.register(self.user)
        self.weconnect.create_category(
            'Ivan Safari', 'New in insurance', 'For all your solutions on the life assurance scheme')
        self.weconnect.create_location('Ivan Safari', 'Kampala', 'Loc001')
        self.weconnect.create_business(
            'Ivan Safari', 'New in insurance', 'For all your solutions on the life assurance scheme',
            'Insurance', 'Kampala', 'path to logo')
        businesses = self.weconnect.delete_business('Ivan Safari', 'New in insurance')

        self.assertNotIn('New in insurance', businesses.keys(),
                         msg='Business was not deleted')
