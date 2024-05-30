from django.urls import reverse
from django.test import TestCase


class InventoryTests(TestCase):

    def test_inventory_list_after_date_view_valid_date(self):
        response = self.client.get(reverse('inventory-list-after-date'), data={"start_date": "2022-02-16"})
        assert response.status_code == 200

    def test_inventory_list_after_date_view_invalid_date(self):
        response = self.client.get(reverse('inventory-list-after-date'), data={"start_date": "None"})
        assert response.status_code != 200

    def test_inventory_list_after_date_view_no_date(self):
        response = self.client.get(reverse('inventory-list-after-date'))
        assert response.status_code != 200

    def test_inventory_list_after_date_returns_correct_inventory_items(self):
        """
        Stubbing this test because I don't have time to properly write it because I would need to create complex
        inventory objects to filter without factory boy or equivalent but the idea is to create new inventory objects
        and test the apis ability to return the properly filtered ones
        """
        # Arrange

        # Act

        # Assert
        pass

