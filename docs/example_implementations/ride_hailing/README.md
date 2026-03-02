# Ride Hailing — End-to-End Implementation Guide

## Overview

This guide provides complete Beckn protocol v2.0 JSON request and response payloads for a ride hailing transaction, from `search` through `support`.

**Scenario:** Priya searches for a Mini cab from Indiranagar to Koramangala in Bengaluru, selects the ride with insurance, pays online, receives driver assignment, completes the trip, and rates the driver.

**Key mobility schema classes used:** `RideRequest`, `Place`, `VehicleCategory`, `RideOption`, `AncillaryService`, `FareEstimate`, `FareBreakup`, `SurgeMultiplier`, `PricingModel`, `WaitingPolicy`, `CancellationPolicy`, `Trip`, `Driver`, `Vehicle`, `VehiclePosition`, `TripUpdate`, `Event`, `Receipt`, `Rating`, `Review`, `Feedback`, `SupportCase`

---

## Context Values

| Field | Value |
|-------|-------|
| `domain` | `mobility` |
| `version` | `2.0` |
| `transaction_id` | Unique per transaction (all actions share same txn id) |
| `bap_id` | `namma-yatri.bap.io` |
| `bap_uri` | `https://api.namma-yatri.io/beckn` |
| `bpp_id` | `ride-platform.bpp.io` |
| `bpp_uri` | `https://api.ride-platform.io/beckn` |

---

## 1. search / on_search — Discovery

### `search` (BAP → BPP)

```json
{
  "context": {
    "domain": "mobility",
    "action": "search",
    "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c",
    "message_id": "msg-001-a1b2",
    "timestamp": "2026-02-03T10:00:00+05:30",
    "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io",
    "bap_uri": "https://api.namma-yatri.io/beckn",
    "location": { "city": { "name": "Bengaluru" }, "country": { "code": "IND" } }
  },
  "message": {
    "intent": {
      "@type": "mobility:RideRequest",
      "fulfillment": {
        "stops": [
          {
            "type": "START",
            "location": {
              "@type": "mobility:Place",
              "gps": "12.9716,77.6412",
              "descriptor": { "name": "Indiranagar 100ft Road" }
            }
          },
          {
            "type": "END",
            "location": {
              "@type": "mobility:Place",
              "gps": "12.9352,77.6245",
              "descriptor": { "name": "Koramangala 4th Block" }
            }
          }
        ]
      },
      "item": {
        "category": {
          "@type": "mobility:VehicleCategory",
          "descriptor": { "code": "MINI" }
        }
      },
      "tags": [
        { "descriptor": { "code": "RIDER_CATEGORY" }, "value": "ADULT" },
        { "descriptor": { "code": "PASSENGER_COUNT" }, "value": "1" }
      ]
    }
  }
}
```

### `on_search` (BPP → BAP)

```json
{
  "context": {
    "domain": "mobility",
    "action": "on_search",
    "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c",
    "message_id": "msg-002-b3c4",
    "timestamp": "2026-02-03T10:00:01+05:30",
    "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io",
    "bap_uri": "https://api.namma-yatri.io/beckn",
    "bpp_id": "ride-platform.bpp.io",
    "bpp_uri": "https://api.ride-platform.io/beckn"
  },
  "message": {
    "catalog": {
      "providers": [
        {
          "@type": "mobility:Operator",
          "id": "ride-platform-blr",
          "descriptor": {
            "name": "Namma Rides",
            "short_desc": "Open mobility platform for Bengaluru"
          },
          "categories": [
            { "@type": "mobility:VehicleCategory", "id": "MINI", "descriptor": { "code": "MINI", "name": "Mini" } },
            { "@type": "mobility:VehicleCategory", "id": "SEDAN", "descriptor": { "code": "SEDAN", "name": "Sedan" } },
            { "@type": "mobility:VehicleCategory", "id": "AUTO", "descriptor": { "code": "AUTO", "name": "Auto Rickshaw" } }
          ],
          "items": [
            {
              "@type": "mobility:RideOption",
              "id": "opt-mini-001",
              "descriptor": {
                "name": "Mini",
                "short_desc": "Compact 4-seater AC cab"
              },
              "category_ids": ["MINI"],
              "price": {
                "@type": "mobility:FareEstimate",
                "value": "135",
                "minimum_value": "120",
                "maximum_value": "155",
                "currency": "INR"
              },
              "tags": [
                { "descriptor": { "code": "ETA_MINUTES" }, "value": "4" },
                { "descriptor": { "code": "ESTIMATED_DISTANCE_KM" }, "value": "5.2" },
                { "descriptor": { "code": "ESTIMATED_DURATION_MINUTES" }, "value": "18" },
                { "descriptor": { "code": "VEHICLE_MAX_CAPACITY" }, "value": "4" },
                { "descriptor": { "code": "VEHICLE_AC" }, "value": "yes" },
                { "descriptor": { "code": "VEHICLE_BOOT_SPACE_LITRES" }, "value": "280" },
                { "descriptor": { "code": "SURGE_ACTIVE" }, "value": "true" }
              ]
            },
            {
              "@type": "mobility:AncillaryService",
              "id": "anc-insurance-001",
              "descriptor": { "name": "Trip Insurance", "short_desc": "Coverage up to ₹5 lakh for accidents" },
              "price": { "value": "9", "currency": "INR" },
              "tags": [
                { "descriptor": { "code": "SERVICE_CODE" }, "value": "INSURANCE" },
                { "descriptor": { "code": "SERVICE_CATEGORY" }, "value": "SAFETY" }
              ]
            }
          ],
          "fulfillments": [
            {
              "id": "ff-mini-001",
              "type": "RIDE",
              "tags": [
                {
                  "descriptor": { "code": "PRICING_MODEL" },
                  "@type": "mobility:PricingModel",
                  "list": [
                    { "descriptor": { "code": "MODEL_TYPE" }, "value": "UPFRONT_QUOTE" },
                    { "descriptor": { "code": "BASE_RATE_INR" }, "value": "45" },
                    { "descriptor": { "code": "PER_KM_RATE_INR" }, "value": "14" },
                    { "descriptor": { "code": "PER_MIN_RATE_INR" }, "value": "1.5" }
                  ]
                },
                {
                  "descriptor": { "code": "SURGE_MULTIPLIER" },
                  "@type": "mobility:SurgeMultiplier",
                  "list": [
                    { "descriptor": { "code": "MULTIPLIER_VALUE" }, "value": "1.2" },
                    { "descriptor": { "code": "REASON" }, "value": "HIGH_DEMAND" }
                  ]
                },
                {
                  "descriptor": { "code": "WAITING_POLICY" },
                  "@type": "mobility:WaitingPolicy",
                  "list": [
                    { "descriptor": { "code": "FREE_WAITING_MINUTES" }, "value": "3" },
                    { "descriptor": { "code": "CHARGE_PER_EXTRA_MINUTE_INR" }, "value": "2" }
                  ]
                },
                {
                  "descriptor": { "code": "CANCELLATION_POLICY" },
                  "@type": "mobility:CancellationPolicy",
                  "list": [
                    { "descriptor": { "code": "CANCELLATION_TERMS" }, "value": "Free before driver assignment" },
                    { "descriptor": { "code": "REFUND_PERCENTAGE_POST_ASSIGNMENT" }, "value": "0" }
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

## 2. select / on_select — Contract Start

### `select` (BAP → BPP)

```json
{
  "context": {
    "domain": "mobility", "action": "select", "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c", "message_id": "msg-003-c5d6",
    "timestamp": "2026-02-03T10:00:30+05:30", "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io", "bap_uri": "https://api.namma-yatri.io/beckn",
    "bpp_id": "ride-platform.bpp.io", "bpp_uri": "https://api.ride-platform.io/beckn"
  },
  "message": {
    "order": {
      "provider": { "id": "ride-platform-blr" },
      "items": [
        { "id": "opt-mini-001", "quantity": { "count": 1 } },
        { "id": "anc-insurance-001", "quantity": { "count": 1 } }
      ],
      "fulfillments": [
        {
          "id": "ff-mini-001",
          "type": "RIDE",
          "stops": [
            {
              "type": "START",
              "location": {
                "@type": "mobility:Place",
                "gps": "12.9718,77.6415",
                "descriptor": { "name": "Indiranagar 100ft Road, near HDFC ATM" }
              }
            },
            {
              "type": "END",
              "location": {
                "@type": "mobility:Place",
                "gps": "12.9350,77.6248",
                "descriptor": { "name": "Koramangala 4th Block, Sony World Signal" }
              }
            }
          ],
          "tags": [
            { "descriptor": { "code": "SERVICE_CLASS" }, "value": "ECONOMY" }
          ]
        }
      ]
    }
  }
}
```

### `on_select` (BPP → BAP)

```json
{
  "context": {
    "domain": "mobility", "action": "on_select", "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c", "message_id": "msg-004-d7e8",
    "timestamp": "2026-02-03T10:00:31+05:30", "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io", "bap_uri": "https://api.namma-yatri.io/beckn",
    "bpp_id": "ride-platform.bpp.io", "bpp_uri": "https://api.ride-platform.io/beckn"
  },
  "message": {
    "order": {
      "provider": {
        "@type": "mobility:Operator",
        "id": "ride-platform-blr",
        "descriptor": { "name": "Namma Rides" }
      },
      "items": [
        {
          "@type": "mobility:RideOption",
          "id": "opt-mini-001",
          "descriptor": { "name": "Mini" },
          "price": { "value": "135", "currency": "INR" }
        },
        {
          "@type": "mobility:AncillaryService",
          "id": "anc-insurance-001",
          "descriptor": { "name": "Trip Insurance" },
          "price": { "value": "9", "currency": "INR" }
        }
      ],
      "fulfillments": [
        {
          "id": "ff-mini-001",
          "type": "RIDE",
          "stops": [
            {
              "type": "START",
              "location": { "gps": "12.9718,77.6415", "descriptor": { "name": "Indiranagar 100ft Road" } }
            },
            {
              "type": "END",
              "location": { "gps": "12.9350,77.6248", "descriptor": { "name": "Koramangala 4th Block" } }
            }
          ],
          "tags": [
            { "descriptor": { "code": "VEHICLE_MAX_CAPACITY" }, "value": "4" },
            { "descriptor": { "code": "VEHICLE_AC" }, "value": "yes" },
            {
              "descriptor": { "code": "DROP_POLICY" },
              "@type": "mobility:DropPolicy",
              "list": [{ "descriptor": { "code": "DROP_CONDITIONS" }, "value": "Anywhere within city limits" }]
            }
          ]
        }
      ],
      "quote": {
        "@type": "mobility:FareBreakup",
        "price": { "value": "144", "currency": "INR" },
        "breakup": [
          { "item": { "descriptor": { "code": "BASE_FARE" } }, "price": { "value": "45", "currency": "INR" } },
          { "item": { "descriptor": { "code": "DISTANCE_CHARGE_5.2KM" } }, "price": { "value": "72.8", "currency": "INR" } },
          { "item": { "descriptor": { "code": "SURGE_1.2X" } }, "price": { "value": "23.4", "currency": "INR" } },
          { "item": { "descriptor": { "code": "INSURANCE" } }, "price": { "value": "9", "currency": "INR" } },
          { "item": { "descriptor": { "code": "PLATFORM_FEE" } }, "price": { "value": "3", "currency": "INR" } }
        ]
      }
    }
  }
}
```

---

## 3. init / on_init — Billing Details + Payment Terms

### `init` (BAP → BPP)

```json
{
  "context": {
    "domain": "mobility", "action": "init", "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c", "message_id": "msg-005-e9f0",
    "timestamp": "2026-02-03T10:00:45+05:30", "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io", "bap_uri": "https://api.namma-yatri.io/beckn",
    "bpp_id": "ride-platform.bpp.io", "bpp_uri": "https://api.ride-platform.io/beckn"
  },
  "message": {
    "order": {
      "provider": { "id": "ride-platform-blr" },
      "items": [
        { "id": "opt-mini-001", "quantity": { "count": 1 } },
        { "id": "anc-insurance-001", "quantity": { "count": 1 } }
      ],
      "fulfillments": [
        {
          "id": "ff-mini-001",
          "type": "RIDE",
          "stops": [
            { "type": "START", "location": { "gps": "12.9718,77.6415", "descriptor": { "name": "Indiranagar 100ft Road" } } },
            { "type": "END", "location": { "gps": "12.9350,77.6248", "descriptor": { "name": "Koramangala 4th Block" } } }
          ],
          "customer": {
            "@type": "mobility:Rider",
            "person": { "name": "Priya Sharma" },
            "contact": { "phone": "+919876543210", "email": "priya@example.com" }
          }
        }
      ],
      "billing": {
        "@type": "mobility:Rider",
        "name": "Priya Sharma",
        "phone": "+919876543210",
        "email": "priya@example.com"
      },
      "tags": [
        { "descriptor": { "code": "RIDER_CATEGORY" }, "value": "ADULT" }
      ]
    }
  }
}
```

### `on_init` (BPP → BAP)

```json
{
  "context": {
    "domain": "mobility", "action": "on_init", "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c", "message_id": "msg-006-g1h2",
    "timestamp": "2026-02-03T10:00:46+05:30", "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io", "bap_uri": "https://api.namma-yatri.io/beckn",
    "bpp_id": "ride-platform.bpp.io", "bpp_uri": "https://api.ride-platform.io/beckn"
  },
  "message": {
    "order": {
      "provider": { "id": "ride-platform-blr", "descriptor": { "name": "Namma Rides" } },
      "items": [
        { "id": "opt-mini-001", "descriptor": { "name": "Mini" }, "price": { "value": "135", "currency": "INR" } },
        { "id": "anc-insurance-001", "descriptor": { "name": "Trip Insurance" }, "price": { "value": "9", "currency": "INR" } }
      ],
      "fulfillments": [
        {
          "id": "ff-mini-001",
          "type": "RIDE",
          "stops": [
            { "type": "START", "location": { "gps": "12.9718,77.6415", "descriptor": { "name": "Indiranagar 100ft Road" } } },
            { "type": "END", "location": { "gps": "12.9350,77.6248", "descriptor": { "name": "Koramangala 4th Block" } } }
          ],
          "customer": {
            "person": { "name": "Priya Sharma" },
            "contact": { "phone": "+919876543210" }
          },
          "tags": [
            {
              "descriptor": { "code": "ROUTE_PREFERENCE_FORM" },
              "list": [
                { "descriptor": { "code": "FORM_TYPE" }, "value": "ROUTE_PREFERENCE" },
                { "descriptor": { "code": "OPTION_TOLL" }, "value": "Toll Road (faster, ₹35 toll extra)" },
                { "descriptor": { "code": "OPTION_NO_TOLL" }, "value": "Non-Toll Route (slower by ~8 min)" }
              ]
            },
            {
              "descriptor": { "code": "NO_SHOW_POLICY" },
              "@type": "mobility:NoShowPolicy",
              "list": [
                { "descriptor": { "code": "NO_SHOW_FEE_INR" }, "value": "50" },
                { "descriptor": { "code": "GRACE_PERIOD_MINUTES" }, "value": "3" }
              ]
            }
          ]
        }
      ],
      "billing": { "name": "Priya Sharma", "phone": "+919876543210", "email": "priya@example.com" },
      "quote": {
        "@type": "mobility:FareBreakup",
        "price": { "value": "144", "currency": "INR" },
        "breakup": [
          { "item": { "descriptor": { "code": "BASE_FARE" } }, "price": { "value": "45", "currency": "INR" } },
          { "item": { "descriptor": { "code": "DISTANCE_CHARGE" } }, "price": { "value": "72.8", "currency": "INR" } },
          { "item": { "descriptor": { "code": "SURGE_1.2X" } }, "price": { "value": "23.4", "currency": "INR" } },
          { "item": { "descriptor": { "code": "INSURANCE" } }, "price": { "value": "9", "currency": "INR" } },
          { "item": { "descriptor": { "code": "PLATFORM_FEE" } }, "price": { "value": "3", "currency": "INR" } }
        ]
      },
      "cancellation_terms": [
        {
          "@type": "mobility:CancellationPolicy",
          "fulfillment_state": { "descriptor": { "code": "BEFORE_DRIVER_ASSIGNMENT" } },
          "cancellation_fee": { "percentage": "0" },
          "reason_required": false
        },
        {
          "@type": "mobility:CancellationPolicy",
          "fulfillment_state": { "descriptor": { "code": "AFTER_DRIVER_ASSIGNMENT" } },
          "cancellation_fee": { "amount": { "value": "50", "currency": "INR" } },
          "reason_required": true
        }
      ],
      "payments": [
        { "type": "ON_ORDER", "collected_by": "BPP", "status": "NOT-PAID",
          "tags": [
            { "descriptor": { "code": "PAYMENT_CHANNEL_OPTIONS" }, "value": "ONLINE_UPI,ONLINE_CARD,CASH_TO_DRIVER" }
          ]
        }
      ]
    }
  }
}
```

---

## 4. confirm / on_confirm — Booking Created

### `confirm` (BAP → BPP)

```json
{
  "context": {
    "domain": "mobility", "action": "confirm", "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c", "message_id": "msg-007-i3j4",
    "timestamp": "2026-02-03T10:01:00+05:30", "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io", "bap_uri": "https://api.namma-yatri.io/beckn",
    "bpp_id": "ride-platform.bpp.io", "bpp_uri": "https://api.ride-platform.io/beckn"
  },
  "message": {
    "order": {
      "provider": { "id": "ride-platform-blr" },
      "items": [
        { "id": "opt-mini-001", "quantity": { "count": 1 } },
        { "id": "anc-insurance-001", "quantity": { "count": 1 } }
      ],
      "fulfillments": [
        {
          "id": "ff-mini-001",
          "stops": [
            { "type": "START", "location": { "gps": "12.9718,77.6415", "descriptor": { "name": "Indiranagar 100ft Road" } } },
            { "type": "END", "location": { "gps": "12.9350,77.6248", "descriptor": { "name": "Koramangala 4th Block" } } }
          ],
          "customer": { "person": { "name": "Priya Sharma" }, "contact": { "phone": "+919876543210" } },
          "tags": [
            { "descriptor": { "code": "ROUTE_PREFERENCE" }, "value": "NO_TOLL" }
          ]
        }
      ],
      "billing": { "name": "Priya Sharma", "phone": "+919876543210", "email": "priya@example.com" },
      "payments": [
        {
          "type": "ON_ORDER",
          "collected_by": "BPP",
          "status": "PAID",
          "transaction_id": "upi-txn-777xyz",
          "tags": [
            { "descriptor": { "code": "PAYMENT_CHANNEL" }, "value": "ONLINE_UPI" }
          ]
        }
      ]
    }
  }
}
```

### `on_confirm` (BPP → BAP)

```json
{
  "context": {
    "domain": "mobility", "action": "on_confirm", "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c", "message_id": "msg-008-k5l6",
    "timestamp": "2026-02-03T10:01:02+05:30", "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io", "bap_uri": "https://api.namma-yatri.io/beckn",
    "bpp_id": "ride-platform.bpp.io", "bpp_uri": "https://api.ride-platform.io/beckn"
  },
  "message": {
    "order": {
      "@type": "mobility:Trip",
      "id": "trip-blr-20260203-001",
      "status": "SEARCHING_DRIVER",
      "provider": { "@type": "mobility:Operator", "id": "ride-platform-blr", "descriptor": { "name": "Namma Rides" } },
      "items": [
        { "@type": "mobility:RideOption", "id": "opt-mini-001", "descriptor": { "name": "Mini" }, "price": { "value": "135", "currency": "INR" } },
        { "@type": "mobility:AncillaryService", "id": "anc-insurance-001", "descriptor": { "name": "Trip Insurance" }, "price": { "value": "9", "currency": "INR" } }
      ],
      "fulfillments": [
        {
          "id": "ff-mini-001",
          "type": "RIDE",
          "state": {
            "@type": "mobility:Event",
            "descriptor": { "code": "DRIVER_ALLOCATION_SEARCHING", "name": "Searching for nearby driver..." }
          },
          "stops": [
            {
              "type": "START",
              "location": { "gps": "12.9718,77.6415", "descriptor": { "name": "Indiranagar 100ft Road" } },
              "instructions": {
                "@type": "mobility:PickupDropoffPoint",
                "descriptor": { "name": "Meet driver near HDFC ATM, not inside the lane" }
              }
            },
            {
              "type": "END",
              "location": { "gps": "12.9350,77.6248", "descriptor": { "name": "Koramangala 4th Block" } }
            }
          ],
          "customer": { "person": { "name": "Priya Sharma" }, "contact": { "phone": "+919876543210" } },
          "contact": {
            "@type": "mobility:ContactHandle",
            "phone": "080-46680000",
            "descriptor": { "name": "Namma Rides Support" }
          },
          "tags": [
            { "descriptor": { "code": "ROUTE_PREFERENCE" }, "value": "NO_TOLL" }
          ]
        }
      ],
      "billing": { "name": "Priya Sharma", "phone": "+919876543210", "email": "priya@example.com" },
      "quote": {
        "price": { "value": "144", "currency": "INR" },
        "breakup": [
          { "item": { "descriptor": { "code": "BASE_FARE" } }, "price": { "value": "45", "currency": "INR" } },
          { "item": { "descriptor": { "code": "DISTANCE_CHARGE" } }, "price": { "value": "72.8", "currency": "INR" } },
          { "item": { "descriptor": { "code": "SURGE_1.2X" } }, "price": { "value": "23.4", "currency": "INR" } },
          { "item": { "descriptor": { "code": "INSURANCE" } }, "price": { "value": "9", "currency": "INR" } },
          { "item": { "descriptor": { "code": "PLATFORM_FEE" } }, "price": { "value": "3", "currency": "INR" } }
        ]
      },
      "payments": [{ "type": "ON_ORDER", "status": "PAID", "transaction_id": "upi-txn-777xyz" }],
      "cancellation_terms": [
        { "fulfillment_state": { "descriptor": { "code": "BEFORE_DRIVER_ASSIGNMENT" } }, "cancellation_fee": { "percentage": "0" } },
        { "fulfillment_state": { "descriptor": { "code": "AFTER_DRIVER_ASSIGNMENT" } }, "cancellation_fee": { "amount": { "value": "50", "currency": "INR" } } }
      ],
      "created_at": "2026-02-03T10:01:02+05:30",
      "updated_at": "2026-02-03T10:01:02+05:30"
    }
  }
}
```

> **⚠️ Note:** `on_confirm` does NOT contain driver or vehicle details. Only `DRIVER_ALLOCATION_SEARCHING` status is returned. Driver details arrive in `on_update`.

---

## 5. on_update (BPP-Initiated) — Driver Assigned

> BPP pushes this unsolicited to BAP when a driver accepts the job. This is the most information-dense message.

```json
{
  "context": {
    "domain": "mobility", "action": "on_update", "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c", "message_id": "msg-009-m7n8",
    "timestamp": "2026-02-03T10:01:45+05:30", "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io", "bap_uri": "https://api.namma-yatri.io/beckn",
    "bpp_id": "ride-platform.bpp.io", "bpp_uri": "https://api.ride-platform.io/beckn"
  },
  "message": {
    "order": {
      "@type": "mobility:Trip",
      "id": "trip-blr-20260203-001",
      "status": "DRIVER_ASSIGNED",
      "provider": { "@type": "mobility:Operator", "id": "ride-platform-blr" },
      "items": [
        { "id": "opt-mini-001", "descriptor": { "name": "Mini" }, "price": { "value": "135", "currency": "INR" } },
        { "id": "anc-insurance-001", "descriptor": { "name": "Trip Insurance" }, "price": { "value": "9", "currency": "INR" } }
      ],
      "fulfillments": [
        {
          "id": "ff-mini-001",
          "type": "RIDE",
          "state": {
            "@type": "mobility:Event",
            "descriptor": { "code": "DRIVER_ASSIGNED", "name": "Driver is on the way" }
          },
          "agent": {
            "@type": "mobility:Driver",
            "person": { "name": "Raju Kumar", "image": "https://cdn.ride-platform.io/drivers/d-4821.jpg" },
            "rating": "4.8",
            "tags": [
              { "descriptor": { "code": "LICENSE_NUMBER" }, "value": "KA04 20190023881" },
              { "descriptor": { "code": "YEARS_OF_EXPERIENCE" }, "value": "6" },
              { "descriptor": { "code": "TOTAL_TRIPS" }, "value": "3421" }
            ]
          },
          "vehicle": {
            "@type": "mobility:Vehicle",
            "registration": "KA-05-MN-7823",
            "model": "Maruti Swift",
            "color": "White",
            "year": "2022",
            "category": { "@type": "mobility:VehicleCategory", "descriptor": { "code": "MINI" } }
          },
          "tracking": true,
          "stops": [
            {
              "type": "START",
              "location": { "gps": "12.9718,77.6415", "descriptor": { "name": "Indiranagar 100ft Road" } },
              "time": { "timestamp": "2026-02-03T10:05:30+05:30", "label": "ETA" }
            },
            { "type": "END", "location": { "gps": "12.9350,77.6248", "descriptor": { "name": "Koramangala 4th Block" } } }
          ],
          "contact": {
            "@type": "mobility:ContactHandle",
            "phone": "+91-MASKED-5678",
            "descriptor": { "name": "Call Driver" }
          },
          "start": {
            "authorization": {
              "type": "OTP",
              "token": "4821",
              "valid_from": "2026-02-03T10:01:45+05:30",
              "valid_to": "2026-02-03T11:01:45+05:30"
            }
          },
          "tags": [
            {
              "descriptor": { "code": "CURRENT_LOCATION" },
              "@type": "mobility:VehiclePosition",
              "list": [
                { "descriptor": { "code": "LATITUDE" }, "value": "12.9783" },
                { "descriptor": { "code": "LONGITUDE" }, "value": "77.6380" },
                { "descriptor": { "code": "BEARING_DEGREES" }, "value": "215" },
                { "descriptor": { "code": "SPEED_KPH" }, "value": "24" },
                { "descriptor": { "code": "ETA_MINUTES" }, "value": "4" }
              ]
            }
          ]
        }
      ],
      "billing": { "name": "Priya Sharma", "phone": "+919876543210", "email": "priya@example.com" },
      "quote": {
        "price": { "value": "144", "currency": "INR" },
        "breakup": [
          { "item": { "descriptor": { "code": "BASE_FARE" } }, "price": { "value": "45", "currency": "INR" } },
          { "item": { "descriptor": { "code": "DISTANCE_CHARGE" } }, "price": { "value": "72.8", "currency": "INR" } },
          { "item": { "descriptor": { "code": "SURGE_1.2X" } }, "price": { "value": "23.4", "currency": "INR" } },
          { "item": { "descriptor": { "code": "INSURANCE" } }, "price": { "value": "9", "currency": "INR" } },
          { "item": { "descriptor": { "code": "PLATFORM_FEE" } }, "price": { "value": "3", "currency": "INR" } }
        ]
      },
      "payments": [{ "type": "ON_ORDER", "status": "PAID", "transaction_id": "upi-txn-777xyz" }],
      "updated_at": "2026-02-03T10:01:45+05:30"
    }
  }
}
```

---

## 6. status / on_status — Trip State Poll

### `status` (BAP → BPP)

```json
{
  "context": {
    "domain": "mobility", "action": "status", "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c", "message_id": "msg-010-o9p0",
    "timestamp": "2026-02-03T10:06:00+05:30", "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io", "bap_uri": "https://api.namma-yatri.io/beckn",
    "bpp_id": "ride-platform.bpp.io", "bpp_uri": "https://api.ride-platform.io/beckn"
  },
  "message": { "order_id": "trip-blr-20260203-001" }
}
```

### `on_status` (BPP → BAP) — driver arrived

```json
{
  "context": {
    "domain": "mobility", "action": "on_status", "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c", "message_id": "msg-011-q1r2",
    "timestamp": "2026-02-03T10:06:01+05:30", "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io", "bap_uri": "https://api.namma-yatri.io/beckn",
    "bpp_id": "ride-platform.bpp.io", "bpp_uri": "https://api.ride-platform.io/beckn"
  },
  "message": {
    "order": {
      "@type": "mobility:Trip",
      "id": "trip-blr-20260203-001",
      "status": "DRIVER_ARRIVED",
      "fulfillments": [
        {
          "id": "ff-mini-001",
          "state": {
            "@type": "mobility:Event",
            "descriptor": { "code": "DRIVER_ARRIVED", "name": "Driver has arrived at pickup point" },
            "updated_at": "2026-02-03T10:05:48+05:30"
          },
          "agent": {
            "@type": "mobility:Driver",
            "person": { "name": "Raju Kumar" },
            "rating": "4.8"
          },
          "vehicle": { "@type": "mobility:Vehicle", "registration": "KA-05-MN-7823", "model": "Maruti Swift", "color": "White" },
          "tracking": true,
          "tags": [
            {
              "descriptor": { "code": "CURRENT_LOCATION" },
              "@type": "mobility:VehiclePosition",
              "list": [
                { "descriptor": { "code": "LATITUDE" }, "value": "12.9719" },
                { "descriptor": { "code": "LONGITUDE" }, "value": "77.6414" },
                { "descriptor": { "code": "CURRENT_STATUS" }, "value": "STOPPED_AT" }
              ]
            }
          ]
        }
      ],
      "updated_at": "2026-02-03T10:05:48+05:30"
    }
  }
}
```

---

## 7. track / on_track — Live Location

### `track` (BAP → BPP)

```json
{
  "context": {
    "domain": "mobility", "action": "track", "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c", "message_id": "msg-012-s3t4",
    "timestamp": "2026-02-03T10:08:00+05:30", "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io", "bap_uri": "https://api.namma-yatri.io/beckn",
    "bpp_id": "ride-platform.bpp.io", "bpp_uri": "https://api.ride-platform.io/beckn"
  },
  "message": { "order_id": "trip-blr-20260203-001" }
}
```

### `on_track` (BPP → BAP)

```json
{
  "context": {
    "domain": "mobility", "action": "on_track", "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c", "message_id": "msg-013-u5v6",
    "timestamp": "2026-02-03T10:08:01+05:30", "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io", "bap_uri": "https://api.namma-yatri.io/beckn",
    "bpp_id": "ride-platform.bpp.io", "bpp_uri": "https://api.ride-platform.io/beckn"
  },
  "message": {
    "tracking": {
      "id": "track-trip-blr-20260203-001",
      "status": "active",
      "url": "https://track.ride-platform.io/live/trip-blr-20260203-001",
      "location": {
        "@type": "mobility:VehiclePosition",
        "updated_at": "2026-02-03T10:07:58+05:30",
        "gps": "12.9600,77.6320",
        "tags": [
          { "descriptor": { "code": "BEARING_DEGREES" }, "value": "195" },
          { "descriptor": { "code": "SPEED_KPH" }, "value": "32" },
          { "descriptor": { "code": "ODOMETER_KM" }, "value": "1.8" }
        ]
      }
    }
  }
}
```

---

## 8. cancel / on_cancel

### `cancel` (BAP → BPP)

```json
{
  "context": {
    "domain": "mobility", "action": "cancel", "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c", "message_id": "msg-014-w7x8",
    "timestamp": "2026-02-03T10:02:30+05:30", "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io", "bap_uri": "https://api.namma-yatri.io/beckn",
    "bpp_id": "ride-platform.bpp.io", "bpp_uri": "https://api.ride-platform.io/beckn"
  },
  "message": {
    "order_id": "trip-blr-20260203-001",
    "cancellation_reason_id": "004",
    "descriptor": { "short_desc": "Driver taking too long" }
  }
}
```

### `on_cancel` (BPP → BAP) — after driver assignment, ₹50 cancellation fee applied

```json
{
  "context": {
    "domain": "mobility", "action": "on_cancel", "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c", "message_id": "msg-015-y9z0",
    "timestamp": "2026-02-03T10:02:32+05:30", "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io", "bap_uri": "https://api.namma-yatri.io/beckn",
    "bpp_id": "ride-platform.bpp.io", "bpp_uri": "https://api.ride-platform.io/beckn"
  },
  "message": {
    "order": {
      "@type": "mobility:Trip",
      "id": "trip-blr-20260203-001",
      "status": "CANCELLED",
      "cancellation": {
        "cancelled_by": "CONSUMER",
        "reason": { "id": "004", "descriptor": { "short_desc": "Driver taking too long" } },
        "time": "2026-02-03T10:02:32+05:30"
      },
      "quote": {
        "@type": "mobility:FareBreakup",
        "price": { "value": "50", "currency": "INR" },
        "breakup": [
          { "item": { "descriptor": { "code": "CANCELLATION_FEE" } }, "price": { "value": "50", "currency": "INR" } },
          { "item": { "descriptor": { "code": "REFUND_INSURANCE" } }, "price": { "value": "9", "currency": "INR" } }
        ]
      },
      "payments": [
        { "type": "ON_CANCEL", "status": "PAID", "collected_by": "BPP",
          "tags": [{ "descriptor": { "code": "REFUND_AMOUNT_INR" }, "value": "94" }] }
      ],
      "fulfillments": [
        {
          "id": "ff-mini-001",
          "state": { "descriptor": { "code": "CANCELLED" } },
          "tags": [
            { "descriptor": { "code": "RECEIPT_ID" }, "value": "rcpt-cancel-blr-001" },
            { "descriptor": { "code": "RECEIPT_URL" }, "value": "https://receipts.ride-platform.io/rcpt-cancel-blr-001.pdf" }
          ]
        }
      ]
    }
  }
}
```

---

## 9. rating / on_rating — Post-Trip Rating

### `rating` (BAP → BPP)

```json
{
  "context": {
    "domain": "mobility", "action": "rating", "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c", "message_id": "msg-016-aa1b",
    "timestamp": "2026-02-03T10:35:00+05:30", "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io", "bap_uri": "https://api.namma-yatri.io/beckn",
    "bpp_id": "ride-platform.bpp.io", "bpp_uri": "https://api.ride-platform.io/beckn"
  },
  "message": {
    "ratings": [
      {
        "@type": "mobility:Rating",
        "id": "rat-001",
        "rating_category": "Driver",
        "value": "4",
        "tags": [
          { "descriptor": { "code": "RATED_ENTITY_ID" }, "value": "d-4821-raju" },
          { "descriptor": { "code": "RATED_ENTITY_TYPE" }, "value": "DRIVER" },
          { "descriptor": { "code": "ORDER_ID" }, "value": "trip-blr-20260203-001" }
        ]
      }
    ],
    "feedback_form": {
      "@type": "mobility:Review",
      "responses": [
        { "question": { "code": "REVIEW_TEXT" }, "answer": "Raju was polite and punctual. Clean car." }
      ]
    },
    "tags": [
      { "descriptor": { "code": "FEEDBACK_TYPE" }, "value": "COMPLIMENT" },
      { "descriptor": { "code": "FEEDBACK_TAGS" }, "value": "CLEAN_VEHICLE,ON_TIME,POLITE" }
    ]
  }
}
```

### `on_rating` (BPP → BAP)

```json
{
  "context": {
    "domain": "mobility", "action": "on_rating", "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c", "message_id": "msg-017-bb2c",
    "timestamp": "2026-02-03T10:35:01+05:30", "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io", "bap_uri": "https://api.namma-yatri.io/beckn",
    "bpp_id": "ride-platform.bpp.io", "bpp_uri": "https://api.ride-platform.io/beckn"
  },
  "message": {
    "feedback_form": {
      "@type": "mobility:Feedback",
      "id": "fb-001",
      "descriptor": { "name": "Thank you for your rating!", "short_desc": "Your feedback helps us improve" }
    }
  }
}
```

---

## 10. support / on_support — Lost Item

### `support` (BAP → BPP)

```json
{
  "context": {
    "domain": "mobility", "action": "support", "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c", "message_id": "msg-018-cc3d",
    "timestamp": "2026-02-03T10:50:00+05:30", "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io", "bap_uri": "https://api.namma-yatri.io/beckn",
    "bpp_id": "ride-platform.bpp.io", "bpp_uri": "https://api.ride-platform.io/beckn"
  },
  "message": {
    "support": {
      "@type": "mobility:SupportCase",
      "order_id": "trip-blr-20260203-001",
      "type": "LOST_ITEM",
      "descriptor": { "short_desc": "Left my red umbrella in the cab" },
      "tags": [
        { "descriptor": { "code": "CASE_TYPE" }, "value": "LOST_ITEM" },
        { "descriptor": { "code": "PRIORITY" }, "value": "MEDIUM" },
        {
          "descriptor": { "code": "LOST_ITEM_DETAILS" },
          "@type": "mobility:LostAndFoundItem",
          "list": [
            { "descriptor": { "code": "ITEM_TYPE" }, "value": "UMBRELLA" },
            { "descriptor": { "code": "ITEM_DESCRIPTION" }, "value": "Red compact umbrella with black handle" },
            { "descriptor": { "code": "LOST_AT" }, "value": "2026-02-03T10:28:00+05:30" }
          ]
        }
      ]
    }
  }
}
```

### `on_support` (BPP → BAP)

```json
{
  "context": {
    "domain": "mobility", "action": "on_support", "version": "2.0",
    "transaction_id": "txn-rh-9f3a8c", "message_id": "msg-019-dd4e",
    "timestamp": "2026-02-03T10:50:02+05:30", "ttl": "PT30S",
    "bap_id": "namma-yatri.bap.io", "bap_uri": "https://api.namma-yatri.io/beckn",
    "bpp_id": "ride-platform.bpp.io", "bpp_uri": "https://api.ride-platform.io/beckn"
  },
  "message": {
    "support": {
      "@type": "mobility:SupportCase",
      "order_id": "trip-blr-20260203-001",
      "ref_id": "case-laf-20260203-447",
      "type": "LOST_ITEM",
      "descriptor": { "short_desc": "Lost item case opened. Driver notified." },
      "phone": "+91-080-46680000",
      "email": "support@ride-platform.io",
      "url": "https://support.ride-platform.io/case/case-laf-20260203-447",
      "tags": [
        { "descriptor": { "code": "CASE_STATUS" }, "value": "OPEN" },
        { "descriptor": { "code": "TICKET_ID" }, "value": "case-laf-20260203-447" },
        {
          "descriptor": { "code": "DRIVER_CONTACT" },
          "@type": "mobility:ContactHandle",
          "list": [
            { "descriptor": { "code": "HANDLE_TYPE" }, "value": "PHONE" },
            { "descriptor": { "code": "HANDLE" }, "value": "+91-MASKED-5678" },
            { "descriptor": { "code": "LABEL" }, "value": "Call driver via masked number" }
          ]
        }
      ]
    }
  }
}
```

---

## Transaction Summary

| Action | BAP → BPP | BPP → BAP | Key Mobility Class |
|--------|-----------|-----------|-------------------|
| search / on_search | `RideRequest` intent with GPS `Place` | Catalog with `RideOption`, `FareEstimate`, `SurgeMultiplier` | `RideOption` |
| select / on_select | Exact GPS pickup/drop, item selection | Confirmed quote with `FareBreakup` | `FareBreakup` |
| init / on_init | `Rider` billing details | `RoutePreference` form, payment channels, `CancellationPolicy` | `CancellationPolicy` |
| confirm / on_confirm | Route preference + payment channel | `Trip` contract, `SEARCHING_DRIVER` state | `Trip`, `Event` |
| on_update (BPP push) | — | `Driver`, `Vehicle`, `VehiclePosition`, OTP | `Driver`, `VehiclePosition` |
| status / on_status | `order_id` | `Event` state update, live position | `Event` |
| track / on_track | `order_id` | Tracking URL + `VehiclePosition` | `VehiclePosition` |
| cancel / on_cancel | Reason code | Cancellation fee applied, `Receipt` | `CancellationPolicy` |
| rating / on_rating | `Rating` + `Review` + `Feedback` | Feedback form acknowledgement | `Rating` |
| support / on_support | `SupportCase` + `LostAndFoundItem` | Case ref + `ContactHandle` | `SupportCase` |
