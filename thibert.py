import json
import requests
from typing import Any

from swagger_client.rest import ApiException, RESTClientObject
from swagger_client.configuration import Configuration
import cred


HOST: str = cred.HOST
KEY: str = cred.KEY



# class CarLightingDistrictApi:
#     """ This is the class for the CarLightingDistrict API.
#     """
    
#     def __init__(self, config):
#         """Initialize the CarLightingDistrict API client."""
#         self.rest_client = RESTClientObject(config)

#     def get_vehicle_years(self) -> Any:
#         """Return a list of vehicle years.

#         Returns:
#             Any: response data
#         """
#         url = "/api/CarLightingDistrict/Vehicle/Years"
#         response = self.rest_client.GET(url)
#         return json.loads(response.data)

#     def get_vehicle_makes(self, vehicle_year: int) -> Any:
#         """ Get a list of vehicle makes for a given year.

#         Args:
#             vehicle_year (int): vehicle year

#         Returns:
#             Any: returns a list of vehicle makes if found, otherwise returns empty.
#         """
#         url = f"/api/CarLightingDistrict/Vehicle/Makes/{vehicle_year}"
#         response = self.rest_client.GET(url)
#         return json.loads(response.data)

#     def get_vehicle_models(self, vehicle_year, vehicle_make):
#         """ Gets a list of vehicle models for a given year and make.

#         Args:
#             vehicle_year (int): _description_
#             vehicle_make (_type_): _description_

#         Returns:
#             _type_: _description_
#         """
#         url = f"/api/CarLightingDistrict/Vehicle/Models/{vehicle_year}/{vehicle_make}"
#         response = self.rest_client.GET(url)
#         return json.loads(response.data)



# # Instantiate the configuration
# configuration = Configuration()
# configuration.host = HOST
# configuration.api_key = KEY


# # Instantiate the API client
# api_client = CarLightingDistrictApi(configuration)

# # Example usage:
# vehicle_years = api_client.get_vehicle_years()
# print("Vehicle Years:", vehicle_years)

# vehicle_year = 2022
# vehicle_makes = api_client.get_vehicle_makes(vehicle_year)
# print(f"Vehicle Makes for {vehicle_year}:", vehicle_makes)

# vehicle_make = 'Honda'
# vehicle_models = api_client.get_vehicle_models(vehicle_year, vehicle_make)
# print(f"Vehicle Models for {vehicle_year} {vehicle_make}:", vehicle_models)




class APIConnector:
    """A base class for connecting to an API."""

    def __init__(self, base_url: str=HOST, api_key: str=KEY, authorization: str=KEY):
        """Initialize the API connector.

        Args:
            base_url (str): Base URL for the API.
            api_key (str): The API key.
            authorization (str): Authorization header.
        """
        self.base_url = base_url
        self.api_key = api_key
        self.authorization = authorization
        self.base_url = base_url

    def get_data(self, endpoint: str, params=None) -> Any:
        """Get data from the API.

        Args:
            endpoint (str): The url endpoint.
            params (Any, optional): Parameters to the endpoint. Defaults to None.

        Returns:
            Any: The response data.
        """
        url = self.base_url + endpoint
        headers = {
            "x-api-key": self.api_key,
            "Authorization": self.authorization
        }
        response = requests.get(url, params=params, headers=headers)
        return response.json()


class CarLightingDistrictAPI(APIConnector):
    """The CarLightingDistrict API connector."""

    def __init__(self):
        """Create the CarLightingDistrict API connector."""
        super().__init__()

    def get_vehicle_years(self) -> Any:
        """Get a list of vehicle years.

        Returns:
            Any: Returns a list of vehicle years.
        """
        endpoint = "/api/CarLightingDistrict/Vehicle/Years"
        return self.get_data(endpoint)

    def get_vehicle_makes(self, vehicle_year: int) -> Any:
        """Get a list of vehicle makes for a given year."""
        endpoint = f"/api/CarLightingDistrict/Vehicle/Makes/{vehicle_year}"
        return self.get_data(endpoint)

    def get_vehicle_models(self, vehicle_year: int, vehicle_make: str) -> Any:
        """Get a list of vehicle models for a given year and make."""
        endpoint = f"/api/CarLightingDistrict/Vehicle/Models/{vehicle_year}/{vehicle_make}"
        return self.get_data(endpoint)



def main():
    """ Main entry point of the app
    """
    api = CarLightingDistrictAPI()

    # Example usage
    years = api.get_vehicle_years()
    print("Years:", years)

    # if years:
    #     makes = api.get_vehicle_makes(years[0])
    #     print("Makes for the first year:", makes)

    #     if makes:
    #         models = api.get_vehicle_models(years[0], makes[0])
    #         print(f"Models for {years[0]} and {makes[0]}:", models)

if __name__ == "__main__":
    main()
