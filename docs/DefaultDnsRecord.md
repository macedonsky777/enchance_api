# DefaultDnsRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**kind** | [**DnsRecordKind**](DnsRecordKind.md) |  | 
**name** | **str** |  | 
**value** | **str** |  | 
**ttl** | **int** |  | [optional] 
**override_conflicting** | **bool** |  | [optional] [default to False]

## Example

```python
from openapi_client.models.default_dns_record import DefaultDnsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultDnsRecord from a JSON string
default_dns_record_instance = DefaultDnsRecord.from_json(json)
# print the JSON string representation of the object
print(DefaultDnsRecord.to_json())

# convert the object into a dict
default_dns_record_dict = default_dns_record_instance.to_dict()
# create an instance of DefaultDnsRecord from a dict
default_dns_record_from_dict = DefaultDnsRecord.from_dict(default_dns_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


