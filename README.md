# thibert-client

- API version: V1 DEVELOPMENT
- Package version: 1.0.0

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

Install requirements.

```sh
pip3 install -r requirements.txt
```

## Getting Started
After installing the prerequisites, create a cred.py file with the required API key and base URL for the endpoints.

Run the following to start the order.
```
python thibert.py
```
Input the information into the CLI and wait for the submission.

The tracking number and order creation date will be saved in a CSV file in the directory.
## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------

## Documentation For Models

 - [Address](docs/Address.md)
 - [Attribute](docs/Attribute.md)
 - [Category](docs/Category.md)
 - [Contact](docs/Contact.md)
 - [DiameterFilter](docs/DiameterFilter.md)
 - [FilterLine](docs/FilterLine.md)
 - [FilterTags](docs/FilterTags.md)
 - [FitmentDetails](docs/FitmentDetails.md)
 - [Image](docs/Image.md)
 - [Inventory](docs/Inventory.md)
 - [Invoice](docs/Invoice.md)
 - [LocalizedString](docs/LocalizedString.md)
 - [Order](docs/Order.md)
 - [OrderConfirmation](docs/OrderConfirmation.md)
 - [OrderLine](docs/OrderLine.md)
 - [OrderStatus](docs/OrderStatus.md)
 - [OrderTracking](docs/OrderTracking.md)
 - [Part](docs/Part.md)
 - [PartInventory](docs/PartInventory.md)
 - [PartIsVehicleSpecific](docs/PartIsVehicleSpecific.md)
 - [PartsFilters](docs/PartsFilters.md)
 - [PricesByCurrencies](docs/PricesByCurrencies.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [RelatedPart](docs/RelatedPart.md)
 - [Salesline](docs/Salesline.md)
 - [TaskCreationRequest](docs/TaskCreationRequest.md)
 - [TaskItem](docs/TaskItem.md)
 - [Taxline](docs/Taxline.md)
 - [WheelInstallation](docs/WheelInstallation.md)
 - [WheelInstallationKit](docs/WheelInstallationKit.md)
 - [WheelInstallationPart](docs/WheelInstallationPart.md)
 - [WheelPartType](docs/WheelPartType.md)

## Documentation For Authorization


## TAPI Key

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header


## Author
Momin Naseem

