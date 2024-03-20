# Tags

Tags are used to transmit product-specific attributes. Mobility service providers can send these values to describe attributes related to fare policies, product features, commercials etc. Tags can be used by BAPs to create filters, to allow sorting, comparison etc. Tags can also be used by BPPs for catalog indexing.  
## Examples

### Item Tags with simple name-value pairs

```
[
    {
        "id": "5777a0bf-9a08-49aa-a97d-1e5561a9622e",
        "descriptor": {
            "name": "Economy Plus",
        },
        "price": {
            "value": "175",
            "currency": "INR"
        },
        "tags": {
            "groups/1/descriptor/name": "Daytime Charges",
            "groups/1/display": true,
            "groups/1/list/1/descriptor/name": "Min Fare upto 2 km",
            "groups/1/list/1/value": "₹ 30 upto 2 km",
            "groups/1/list/2/descriptor/name": "Rate above Min. Fare",
            "groups/1/list/2/value": "₹15 / km",
            "groups/1/list/3/descriptor/name": "Driver Pickup Charges",
            "groups/1/list/3/value": "₹ 10",
            "groups/1/list/4/descriptor/name": "Nominal Fare",
            "groups/1/list/4/descriptor/short_desc": "Driver may quote extra to cover for traffic, chance of return trip, etc.",
            "groups/1/list/4/value": "₹ 10",
            "groups/1/list/5/descriptor/name": "Waiting Charges",
            "groups/1/list/5/descriptor/short_desc": "Driver may quote extra to cover for traffic, chance of return trip, etc.",
            "groups/1/list/5/value": "₹ 0 / min"
        }
    }
]
```

### Item Tags with standardized (codified) name-value pairs

```
[
    {
        "id": "5777a0bf-9a08-49aa-a97d-1e5561a9622e",
        "descriptor": {
            "name": "Economy",
            "code": "RIDE"
        },
        "price": {
            "value": "175",
            "currency": "INR"
        },
        "tags": {
            "groups/1/descriptor/name": "Daytime Charges",
            "groups/1/descriptor/code": "fare_policy",
            "groups/1/display": true,
            "groups/1/list/1/descriptor/name": "Min Fare upto 2 km",
            "groups/1/list/1/value": "₹ 30 upto 2 km",
            "groups/1/list/2/descriptor/name": "Rate above Min. Fare",
            "groups/1/list/2/descriptor/code": "extra_fare",
            "groups/1/list/2/value": "₹15 / km",
            "groups/1/list/3/descriptor/name": "Driver Pickup Charges",
            "groups/1/list/3/descriptor/code": "pickup_charges",
            "groups/1/list/3/value": "₹ 10",
            "groups/1/list/4/descriptor/name": "Nominal Fare",
            "groups/1/list/4/descriptor/short_desc": "Driver may quote extra to cover for traffic, chance of return trip, etc.",
            "groups/1/list/4/descriptor/code": "nominal_fare",
            "groups/1/list/4/value": "₹ 10",
            "groups/1/list/5/descriptor/name": "Waiting Charges",
            "groups/1/list/5/descriptor/short_desc": "Driver may quote extra to cover for traffic, chance of return trip, etc.",
            "groups/1/list/5/descriptor/code": "waiting_charges",
            "groups/1/list/5/value": "₹ 0 / min"
        }
    }
]
```

**Note:** The above tag list is NOT a recommended or required standard. This list will be standardized on the basis of adoption by implementers across multiple networks. 


## Contributing to Tags
Tags are standardized by the Mobility Working Group on the basis of community adoption. At the current moment, there are no standard tags recommended by the working group. Eventually a tag list will be created that looks like the table below. Implementers are free to submit tags for consideration via a PR with a row added to the table below along with an attached report on adoption of that tag across the implementer community. It is recommended for contributors to do extensive research on adoption before submitting the PR. 


## Tag List

| Name                  | Code                   | Description                                                                    | Type   | Format                                                                                                      | Examples                                                                                                                                              |
|-----------------------|------------------------|--------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| (name)              | (code)                   | (description)                                          | (type) | (format)                                                                                    | (examples)                                                                                                                                              |


### An example Tag List with standardizations (NOT A RECOMMENDATION)

| Name                  | Code                   | Description                                                                    | Type   | Format                                                                                                      | Examples                                                                                                                                              |
|-----------------------|------------------------|--------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Language              | lang                   | Language spoken by a person or entity                                          | string | ISO 639-2 language code                                                                                     | eng, hin                                                                                                                                              |
| Base Fare             | min_fare               | Minimum fare that has to be paid for a mobility service                        | string | <value> <currency>                                                                                          | 30 iNR                                                                                                                                                |
| Minimum Fare Distance | min_fare_dist          | Distance upto which minimum fare is to be paid                                 | string | <value> <distance unit>                                                                                     | 1 km                                                                                                                                                  |
| Fare per distance     | fare_per_dist          | Fare applicable for every unit of distance travelled                           | string | <value> <currency> / <distance unit>                                                                        | 12 INR / km                                                                                                                                           |
| Fare per time         | fare_per_time          | Fare applicable for every unit of time travelled                               | string | <value> <currency> / <time unit>                                                                            | 10 INR / hr                                                                                                                                           |
| Pickup Charges        | pickup_charges         | Compensation to driver for travelling pickup distance                          | string | <value> <currency>                                                                                          | 20 INR                                                                                                                                                |
| Nominal Fare          | nominal_fare           | Fair compensation for driver to cover for traffic, chance of return trip, etc. | string | <value> <currency>                                                                                          | 20 INR                                                                                                                                                |
| Waiting Charges       | waiting_charges        | Fair compensation for driver for making a stop along the route                 | string | <value> <currency> / <time unit>                                                                            | 5 INR / min                                                                                                                                           |
| Night Shift Start     | night_shift_start_time | Time from which night shift begins                                             | string | time as per RFC3339                                                                                         | 22:00:00                                                                                                                                              |
| Night Shift End       | night_shift_end_time   | Time at which night shift ends                                                 | string | time as per RFC3339                                                                                         | 05:00:00                                                                                                                                              |
| Path                  | encoded_polyline       | Compressed polyline path generated from a set of gps coordinates               | string | Refer to [polyline algorithm](https://developers.google.com/maps/documentation/utilities/polylinealgorithm) | _p~iF~ps\|U_ulLnnqC_mqNvxq`@                                                                                                                          |
| Waypoints             | waypoints              | Set of specific GPS points along a route                                       | string | stringify(minifiy(JSON array of Location objects with gps property set))                                    | [{\"gps\":\"12.9099828, 77.6118226\"},{\"gps\":\"12.9099828, 77.6118226\"},{\"gps\":\"12.9099828, 77.6118226\"},{\"gps\":\"12.9099828, 77.6118226\"}] |
