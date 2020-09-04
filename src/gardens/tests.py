import pytest
import json
from gardens.models import Garden
from users.models import CustomUser
from datetime import datetime
from graphene_django.utils.testing import GraphQLTestCase

class TestGardenInstance:
    """
    Test that various properties are created by default on a new Garden object
    """
    GARDEN_NAME = 'Secret Garden'
    EMAIL = 'test@test.com'
    PASSWORD = 'testing1234'
    user = CustomUser(email=EMAIL, password=PASSWORD)
    garden = Garden(garden_name=GARDEN_NAME, owner=user) 
    
    """ garden_name is assigned to __str__ method """
    def test_str_matches_garden_name(self):
        assert str(self.garden) == self.GARDEN_NAME

    """ garden_name matches what we entered """
    def test_garden_name_matches(self):
        assert self.garden.garden_name == self.GARDEN_NAME
    
    """ start_date exists as a date """
    def test_start_date_property_exists_as_a_date(self):
        assert isinstance(self.garden.start_date, datetime)
    
    """ is_active property defaults to true """
    def test_is_active_property_exists(self):
        assert self.garden.is_active == True

    """ owner refers to the user passed as argument """
    def test_owner_is_passed_user(self):
        assert (
            self.garden.owner.email == self.EMAIL
            and self.garden.owner.password == self.PASSWORD
        )

class TestGraphQLQueries(GraphQLTestCase):

    """ gardens query returns a response and no errors """
    @pytest.mark.filterwarnings("ignore")
    def test_gardens_query(self):
        response = self.query(
            '''
            query {
                gardens {
                    id
                    gardenName
                    owner {
                        id
                        email
                    }
                }
            }
            '''
        )

        # content returned in json format
        content = json.loads(response.content)

        # response 200 with no errors
        self.assertResponseNoErrors(response)