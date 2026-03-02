# Advance Cab Reservation — End-to-End Implementation Guide

## Overview

This guide provides complete Beckn protocol v2.0 JSON payloads for an advance cab reservation from GPS pickup to destination, with a future pickup time.

**Scenario:** Arjun books a Sedan for 3:30 AM airport pickup the night before. Fixed fare, no surge. Driver assigned at 2:45 AM via `on_update`.

**Key differentiator from instant ride hailing:** `RideRequest.fulfillment.stops[0].time.timestamp` is set to a future time. The `on_confirm` returns `DRIVER_ALLOCATION_DEFERRED` (not searching immediately). `BookingRule` and `NoShowPolicy` appear in `on_search`. Driver details arrive in `on_update` at 2:45 AM.

---

## Context Values

| Field | Value |
|-------|-------|
| `domain` | `mobility` |
| `bap_id` | `cab-app.bap.io` |
| `bpp_id` | `airport-cabs.bpp.io` |
| `transaction_id` | `txn-adv-5c8b1e` |

---

## 1. search / on_search — Discovery (Night Before)

### `search` (BAP → BPP)

```json
{
  "context": {
    "domain": "mobility", "action": "search", "version": "2.0",
    "transaction_id": "txn-adv-5c8b1e", "message_id": "msg-001",
    "timestamp": "2026-02-03T22:00:00+05:30", "ttl": "PT30S",
    "bap_id": "cab-app.bap.io", "bap_uri": "https://api.cab-app.io/beckn",
    "location": { "city": { "name": "Mumbai" }, "country": { "code": "IND" } }
  },
  "message": {
    "intent": {
      "@type": "mobility:RideRequest",
      "fulfillment": {
        "stops": [
          {
            "type": "START",
            "time": { "timestamp": "2026-02-04T03:30:00+05:30", "label": "ADVANCE_PICKUP" },
            "location": {
              "@type": "mobility:Place",
              "gps": "19.0548,72.8397",
              "descriptor": { "name": "Arjun's Home, Bandra West" }
            }
          },
          {
            "type": "END",
            "location": {
              "@type": "mobility:Place",
              "gps": "19.0896,72.8656",
              "descriptor": { "name": "Chhatrapati Shivaji Maharaj International Airport, T2" },
              "tags": [{ "descriptor": { "code": "PLACE_TYPE" }, "value": "AIRPORT" }]
            }
          }
        ]
      },
      "item": {
        "category": { "@type": "mobility:VehicleCategory", "descriptor": { "code": "SEDAN" } }
      },
      "tags": [
        { "descriptor": { "code": "RIDER_CATEGORY" }, "value": "ADULT" },
        { "descriptor": { "code": "BOOKING_TYPE" }, "value": "ADVANCE" }
      ]
    }
  }
}
```

### `on_search` (BPP → BAP)

```json
{
  "context": {
    "domain": "mobility", "action": "on_search", "version": "2.0",
    "transaction_id": "txn-adv-5c8b1e", "message_id": "msg-002",
    "timestamp": "2026-02-03T22:00:01+05:30", "ttl": "PT30S",
    "bap_id": "cab-app.bap.io", "bap_uri": "https://api.cab-app.io/beckn",
    "bpp_id": "airport-cabs.bpp.io", "bpp_uri": "https://api.airport-cabs.io/beckn"
  },
  "message": {
    "catalog": {
      "providers": [
        {
          "@type": "mobility:Operator",
          "id": "airport-cabs-mum",
          "descriptor": { "name": "Mumbai Airport Cabs", "short_desc": "24/7 advance airport transfers" },
          "items": [
            {
              "@type": "mobility:RideOption",
              "id": "opt-sedan-airport",
              "descriptor": { "name": "Sedan Airport Transfer", "short_desc": "Fixed fare, no surge for advance bookings" },
              "category_ids": ["SEDAN"],
              "price": {
                "@type": "mobility:FareEstimate",
                "value": "780",
                "currency": "INR"
              },
              "tags": [
                { "descriptor": { "code": "ETA_AT_PICKUP_TIME" }, "value": "3:30 AM guaranteed" },
                { "descriptor": { "code": "FIXED_FARE" }, "value": "true" },
                { "descriptor": { "code": "SURGE_APPLICABLE" }, "value": "false" },
                { "descriptor": { "code": "VEHICLE_AC" }, "value": "yes" },
                { "descriptor": { "code": "VEHICLE_BOOT_SPACE_LITRES" }, "value": "350" }
              ]
            },
            {
              "@type": "mobility:AncillaryService",
              "id": "anc-insurance-adv",
              "descriptor": { "name": "Trip Insurance" },
              "price": { "value": "9", "currency": "INR" }
            }
          ],
          "fulfillments": [
            {
              "id": "ff-sedan-airport",
              "type": "ADVANCE_RIDE",
              "tags": [
                {
                  "descriptor": { "code": "BOOKING_RULE" },
                  "@type": "mobility:BookingRule",
                  "list": [
                    { "descriptor": { "code": "PRIOR_NOTICE_DURATION_MIN" }, "value": "60" },
                    { "descriptor": { "code": "EARLIEST_BOOKING_TIME_HRS_IN_ADVANCE" }, "value": "1" },
                    { "descriptor": { "code": "LATEST_BOOKING_TIME_HRS_IN_ADVANCE" }, "value": "168" },
                    { "descriptor": { "code": "PHONE_NUMBER" }, "value": "+91-022-46780000" }
                  ]
                },
                {
                  "descriptor": { "code": "PRICING_MODEL" },
                  "@type": "mobility:PricingModel",
                  "list": [{ "descriptor": { "code": "MODEL_TYPE" }, "value": "FIXED" }]
                },
                {
                  "descriptor": { "code": "NO_SHOW_POLICY" },
                  "@type": "mobility:NoShowPolicy",
                  "list": [
                    { "descriptor": { "code": "NO_SHOW_FEE_INR" }, "value": "780" },
                    { "descriptor": { "code": "GRACE_PERIOD_MINUTES" }, "value": "5" },
                    { "descriptor": { "code": "NOTE" }, "value": "Full fare charged if not at pickup at 3:30 AM" }
                  ]
                },
                {
                  "descriptor": { "code": "WAITING_POLICY" },
                  "@type": "mobility:WaitingPolicy",
                  "list": [
                    { "descriptor": { "code": "FREE_WAITING_MINUTES" }, "value": "5" },
                    { "descriptor": { "code": "MAX_WAITING_MINUTES" }, "value": "10" }
                  ]
                },
                {
                  "descriptor": { "code": "CANCELLATION_POLICY" },
                  "@type": "mobility:CancellationPolicy",
                  "list": [
                    { "descriptor": { "code": "REFUND_PERCENTAGE_BEFORE_4HR" }, "value": "100" },
                    { "descriptor": { "code": "REFUND_PERCENTAGE_2_TO_4HR" }, "value": "50" },
                    { "descriptor": { "code": "REFUND_PERCENTAGE_WITHIN_2HR" }, "value": "0" }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  }
}
```

---

## 2. select / on_select

### `select` (BAP → BPP)

```json
{
  "context": { "domain": "mobility", "action": "select", "version": "2.0",
    "transaction_id": "txn-adv-5c8b1e", "message_id": "msg-003",
    "timestamp": "2026-02-03T22:01:00+05:30", "ttl": "PT30S",
    "bap_id": "cab-app.bap.io", "bap_uri": "https://api.cab-app.io/beckn",
    "bpp_id": "airport-cabs.bpp.io", "bpp_uri": "https://api.airport-cabs.io/beckn" },
  "message": {
    "order": {
      "provider": { "id": "airport-cabs-mum" },
      "items": [
        { "id": "opt-sedan-airport", "quantity": { "count": 1 } },
        { "id": "anc-insurance-adv", "quantity": { "count": 1 } }
      ],
      "fulfillments": [
        {
          "id": "ff-sedan-airport",
          "type": "ADVANCE_RIDE",
          "stops": [
            {
              "type": "START",
              "time": { "timestamp": "2026-02-04T03:30:00+05:30" },
              "location": { "@type": "mobility:Place", "gps": "19.0548,72.8397", "descriptor": { "name": "Bandra West — Gate 3" } }
            },
            {
              "type": "END",
              "location": { "@type": "mobility:Place", "gps": "19.0896,72.8656", "descriptor": { "name": "T2 Departures" } }
            }
          ],
          "tags": [{ "descriptor": { "code": "SERVICE_CLASS" }, "value": "PREMIUM" }]
        }
      ]
    }
  }
}
```

### `on_select` (BPP → BAP)

```json
{
  "context": { "domain": "mobility", "action": "on_select", "version": "2.0",
    "transaction_id": "txn-adv-5c8b1e", "message_id": "msg-004",
    "timestamp": "2026-02-03T22:01:01+05:30", "ttl": "PT30S",
    "bap_id": "cab-app.bap.io", "bap_uri": "https://api.cab-app.io/beckn",
    "bpp_id": "airport-cabs.bpp.io", "bpp_uri": "https://api.airport-cabs.io/beckn" },
  "message": {
    "order": {
      "items": [
        { "id": "opt-sedan-airport", "price": { "value": "780", "currency": "INR" } },
        { "id": "anc-insurance-adv", "price": { "value": "9", "currency": "INR" } }
      ],
      "fulfillments": [
        {
          "id": "ff-sedan-airport",
          "tags": [
            { "descriptor": { "code": "ADVANCE_SLOT_GUARANTEED" }, "value": "2026-02-04T03:30:00+05:30" },
            { "descriptor": { "code": "DRIVER_ASSIGNMENT_EXPECTED_BY" }, "value": "2026-02-04T02:45:00+05:30" }
          ]
        }
      ],
      "quote": {
        "price": { "value": "789", "currency": "INR" },
        "breakup": [
          { "item": { "descriptor": { "code": "FIXED_FARE_AIRPORT_TRANSFER" } }, "price": { "value": "780", "currency": "INR" } },
          { "item": { "descriptor": { "code": "INSURANCE" } }, "price": { "value": "9", "currency": "INR" } }
        ]
      }
    }
  }
}
```

---

## 3. init / on_init

### `init` (BAP → BPP)

```json
{
  "context": { "domain": "mobility", "action": "init", "version": "2.0",
    "transaction_id": "txn-adv-5c8b1e", "message_id": "msg-005",
    "timestamp": "2026-02-03T22:01:30+05:30", "ttl": "PT30S",
    "bap_id": "cab-app.bap.io", "bap_uri": "https://api.cab-app.io/beckn",
    "bpp_id": "airport-cabs.bpp.io", "bpp_uri": "https://api.airport-cabs.io/beckn" },
  "message": {
    "order": {
      "provider": { "id": "airport-cabs-mum" },
      "items": [{ "id": "opt-sedan-airport" }, { "id": "anc-insurance-adv" }],
      "fulfillments": [
        {
          "id": "ff-sedan-airport",
          "customer": {
            "@type": "mobility:Rider",
            "person": { "name": "Arjun Mehta" },
            "contact": { "phone": "+919900112233", "email": "arjun@example.com" }
          }
        }
      ],
      "billing": { "name": "Arjun Mehta", "phone": "+919900112233", "email": "arjun@example.com" }
    }
  }
}
```

### `on_init` (BPP → BAP)

```json
{
  "context": { "domain": "mobility", "action": "on_init", "version": "2.0",
    "transaction_id": "txn-adv-5c8b1e", "message_id": "msg-006",
    "timestamp": "2026-02-03T22:01:31+05:30", "ttl": "PT30S",
    "bap_id": "cab-app.bap.io", "bap_uri": "https://api.cab-app.io/beckn",
    "bpp_id": "airport-cabs.bpp.io", "bpp_uri": "https://api.airport-cabs.io/beckn" },
  "message": {
    "order": {
      "fulfillments": [
        {
          "id": "ff-sedan-airport",
          "tags": [
            {
              "descriptor": { "code": "ROUTE_PREFERENCE_FORM" },
              "list": [
                { "descriptor": { "code": "OPTION_TOLL" }, "value": "Western Express Highway (Toll: ₹130 extra)" },
                { "descriptor": { "code": "OPTION_NO_TOLL" }, "value": "Jogeshwari-Vikhroli Link Road (No toll, +12 min)" }
              ]
            },
            {
              "descriptor": { "code": "NO_SHOW_POLICY" },
              "@type": "mobility:NoShowPolicy",
              "list": [
                { "descriptor": { "code": "NO_SHOW_FEE_INR" }, "value": "780" },
                { "descriptor": { "code": "GRACE_PERIOD_MINUTES" }, "value": "5" }
              ]
            }
          ]
        }
      ],
      "quote": { "price": { "value": "789", "currency": "INR" }, "breakup": [
        { "item": { "descriptor": { "code": "FIXED_FARE" } }, "price": { "value": "780", "currency": "INR" } },
        { "item": { "descriptor": { "code": "INSURANCE" } }, "price": { "value": "9", "currency": "INR" } }
      ]},
      "cancellation_terms": [
        { "fulfillment_state": { "descriptor": { "code": "MORE_THAN_4HR_BEFORE" } }, "cancellation_fee": { "percentage": "0" } },
        { "fulfillment_state": { "descriptor": { "code": "2_TO_4HR_BEFORE" } }, "cancellation_fee": { "percentage": "50" } },
        { "fulfillment_state": { "descriptor": { "code": "WITHIN_2HR" } }, "cancellation_fee": { "percentage": "100" } }
      ],
      "payments": [{ "type": "ON_ORDER", "status": "NOT-PAID", "collected_by": "BPP",
        "tags": [{ "descriptor": { "code": "PAYMENT_CHANNEL_OPTIONS" }, "value": "ONLINE_UPI,ONLINE_CARD" }] }]
    }
  }
}
```

---

## 4. confirm / on_confirm

### `confirm` (BAP → BPP)

```json
{
  "context": { "domain": "mobility", "action": "confirm", "version": "2.0",
    "transaction_id": "txn-adv-5c8b1e", "message_id": "msg-007",
    "timestamp": "2026-02-03T22:02:00+05:30", "ttl": "PT30S",
    "bap_id": "cab-app.bap.io", "bap_uri": "https://api.cab-app.io/beckn",
    "bpp_id": "airport-cabs.bpp.io", "bpp_uri": "https://api.airport-cabs.io/beckn" },
  "message": {
    "order": {
      "provider": { "id": "airport-cabs-mum" },
      "items": [{ "id": "opt-sedan-airport" }, { "id": "anc-insurance-adv" }],
      "fulfillments": [
        {
          "id": "ff-sedan-airport",
          "customer": { "person": { "name": "Arjun Mehta" }, "contact": { "phone": "+919900112233" } },
          "tags": [{ "descriptor": { "code": "ROUTE_PREFERENCE" }, "value": "NO_TOLL" }]
        }
      ],
      "billing": { "name": "Arjun Mehta", "phone": "+919900112233" },
      "payments": [{ "type": "ON_ORDER", "status": "PAID", "transaction_id": "upi-adv-mum-001",
        "tags": [{ "descriptor": { "code": "PAYMENT_CHANNEL" }, "value": "ONLINE_UPI" }] }]
    }
  }
}
```

### `on_confirm` (BPP → BAP)

```json
{
  "context": { "domain": "mobility", "action": "on_confirm", "version": "2.0",
    "transaction_id": "txn-adv-5c8b1e", "message_id": "msg-008",
    "timestamp": "2026-02-03T22:02:02+05:30", "ttl": "PT30S",
    "bap_id": "cab-app.bap.io", "bap_uri": "https://api.cab-app.io/beckn",
    "bpp_id": "airport-cabs.bpp.io", "bpp_uri": "https://api.airport-cabs.io/beckn" },
  "message": {
    "order": {
      "@type": "mobility:Trip",
      "id": "adv-mum-20260204-001",
      "status": "BOOKING_CONFIRMED",
      "provider": { "@type": "mobility:Operator", "id": "airport-cabs-mum" },
      "items": [
        { "id": "opt-sedan-airport", "descriptor": { "name": "Sedan Airport Transfer" }, "price": { "value": "780", "currency": "INR" } },
        { "id": "anc-insurance-adv", "descriptor": { "name": "Trip Insurance" }, "price": { "value": "9", "currency": "INR" } }
      ],
      "fulfillments": [
        {
          "id": "ff-sedan-airport",
          "state": {
            "@type": "mobility:Event",
            "descriptor": { "code": "DRIVER_ALLOCATION_DEFERRED", "name": "Driver will be assigned by 2:45 AM" },
            "updated_at": "2026-02-03T22:02:02+05:30"
          },
          "stops": [
            {
              "type": "START",
              "time": { "timestamp": "2026-02-04T03:30:00+05:30", "label": "PICKUP_TIME" },
              "location": { "gps": "19.0548,72.8397", "descriptor": { "name": "Bandra West — Gate 3" } },
              "instructions": {
                "@type": "mobility:PickupDropoffPoint",
                "descriptor": { "name": "Be at Gate 3 by 3:25 AM. Driver will call 10 minutes before arrival." }
              }
            },
            { "type": "END", "location": { "gps": "19.0896,72.8656", "descriptor": { "name": "T2 Departures" } } }
          ],
          "contact": { "@type": "mobility:ContactHandle", "phone": "+91-022-46780000", "descriptor": { "name": "24/7 Booking Support" } },
          "tags": [
            { "descriptor": { "code": "DRIVER_ASSIGNMENT_EXPECTED_BY" }, "value": "2026-02-04T02:45:00+05:30" },
            { "descriptor": { "code": "ROUTE_PREFERENCE" }, "value": "NO_TOLL" }
          ]
        }
      ],
      "quote": { "price": { "value": "789", "currency": "INR" }, "breakup": [
        { "item": { "descriptor": { "code": "FIXED_FARE" } }, "price": { "value": "780", "currency": "INR" } },
        { "item": { "descriptor": { "code": "INSURANCE" } }, "price": { "value": "9", "currency": "INR" } }
      ]},
      "payments": [{ "type": "ON_ORDER", "status": "PAID", "transaction_id": "upi-adv-mum-001" }],
      "created_at": "2026-02-03T22:02:02+05:30"
    }
  }
}
```

> **Note:** `on_confirm` returns `DRIVER_ALLOCATION_DEFERRED` — not `SEARCHING_DRIVER`. Driver assignment begins at ~2:45 AM. The `DRIVER_ASSIGNMENT_EXPECTED_BY` tag communicates when Arjun can expect the driver notification.

---

## 5. on_update — Driver Assigned at 2:45 AM (BPP-Initiated)

```json
{
  "context": { "domain": "mobility", "action": "on_update", "version": "2.0",
    "transaction_id": "txn-adv-5c8b1e", "message_id": "msg-009",
    "timestamp": "2026-02-04T02:47:00+05:30", "ttl": "PT30S",
    "bap_id": "cab-app.bap.io", "bap_uri": "https://api.cab-app.io/beckn",
    "bpp_id": "airport-cabs.bpp.io", "bpp_uri": "https://api.airport-cabs.io/beckn" },
  "message": {
    "order": {
      "@type": "mobility:Trip",
      "id": "adv-mum-20260204-001",
      "status": "DRIVER_ASSIGNED",
      "fulfillments": [
        {
          "id": "ff-sedan-airport",
          "state": { "@type": "mobility:Event", "descriptor": { "code": "DRIVER_ASSIGNED", "name": "Driver Ramesh is heading to Bandra" } },
          "agent": {
            "@type": "mobility:Driver",
            "person": { "name": "Ramesh Patil" },
            "rating": "4.9",
            "tags": [
              { "descriptor": { "code": "LICENSE_NUMBER" }, "value": "MH02 20150012345" },
              { "descriptor": { "code": "TOTAL_AIRPORT_TRIPS" }, "value": "847" }
            ]
          },
          "vehicle": {
            "@type": "mobility:Vehicle",
            "registration": "MH-02-CK-9934",
            "model": "Honda Amaze",
            "color": "White",
            "year": "2024"
          },
          "tracking": true,
          "contact": { "@type": "mobility:ContactHandle", "phone": "+91-MASKED-8800", "descriptor": { "name": "Call Ramesh" } },
          "start": {
            "authorization": { "type": "OTP", "token": "3319", "valid_from": "2026-02-04T02:47:00+05:30", "valid_to": "2026-02-04T04:30:00+05:30" }
          },
          "tags": [
            {
              "descriptor": { "code": "CURRENT_LOCATION" },
              "@type": "mobility:VehiclePosition",
              "list": [
                { "descriptor": { "code": "LATITUDE" }, "value": "19.0701" },
                { "descriptor": { "code": "LONGITUDE" }, "value": "72.8336" },
                { "descriptor": { "code": "ETA_MINUTES" }, "value": "32" }
              ]
            }
          ]
        }
      ],
      "updated_at": "2026-02-04T02:47:00+05:30"
    }
  }
}
```

---

## 6–10. status / track / cancel / rating / support

*These follow the exact same structure as the ride hailing guide. Key differences:*
- `status` / `on_status`: Same pattern — `DRIVER_EN_ROUTE`, `DRIVER_ARRIVED`, `TRIP_STARTED`, `TRIP_ENDED` events
- `track` / `on_track`: Same live GPS tracking structure
- `cancel` / `on_cancel`: Uses the advance cancellation policy (100% / 50% / 0% tiered by time)
- `rating` / `on_rating`: Same structure, rating the airport transfer experience
- `support` / `on_support`: Arjun requests an itemised receipt for employer reimbursement

*See [Ride Hailing guide](../ride_hailing/README.md) for these action JSON examples.*

---

## Transaction Summary

| Action | Key Differentiator from Instant Ride Hailing |
|--------|----------------------------------------------|
| `search` | `stops[0].time.timestamp` = future 3:30 AM |
| `on_search` | `BookingRule` + `NoShowPolicy` + no `SurgeMultiplier` |
| `on_confirm` | `DRIVER_ALLOCATION_DEFERRED` (not SEARCHING) + `DRIVER_ASSIGNMENT_EXPECTED_BY` |
| `on_update` (2:45 AM) | Same driver assignment pattern as instant ride hailing |
