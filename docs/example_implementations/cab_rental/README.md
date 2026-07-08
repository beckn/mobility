# Cab Rental — End-to-End Implementation Guide

## Overview

This guide provides complete Beckn protocol v2.0 JSON payloads for a cab rental transaction (8 hours / 80 km package).

**Scenario:** Meera books a Sedan rental in Goa for 9 AM the next morning — ₹1,800 base package, ₹10/km overage. She selects non-toll route, pays online, driver is assigned, and 22 extra km are billed at end of day.

**Key differentiator from ride hailing:** `SystemPricingPlan` carries the rental package rates (base fee + per-km + per-hour overage). No destination at search time. `on_update` is triggered twice — once for driver assignment and once for end-of-rental overage settlement.

---

## Context Values

| Field | Value |
|-------|-------|
| `domain` | `mobility` |
| `bap_id` | `rental-app.bap.io` |
| `bpp_id` | `goa-rentals.bpp.io` |
| `transaction_id` | `txn-cr-7b4e2d` |

---

## 1. search / on_search — Discovery

### `search` (BAP → BPP)

```json
{
  "context": {
    "domain": "mobility", "action": "search", "version": "2.0",
    "transaction_id": "txn-cr-7b4e2d", "message_id": "msg-001",
    "timestamp": "2026-02-03T19:00:00+05:30", "ttl": "PT30S",
    "bap_id": "rental-app.bap.io", "bap_uri": "https://api.rental-app.io/beckn",
    "location": { "city": { "name": "Panaji, Goa" }, "country": { "code": "IND" } }
  },
  "message": {
    "intent": {
      "@type": "mobility:RideRequest",
      "fulfillment": {
        "stops": [
          {
            "type": "START",
            "time": { "timestamp": "2026-02-04T09:00:00+05:30", "label": "START_TIME" },
            "location": {
              "@type": "mobility:Place",
              "gps": "15.5057,73.8264",
              "descriptor": { "name": "Grand Hyatt Goa, Bambolim" }
            }
          }
        ]
      },
      "item": {
        "category": {
          "@type": "mobility:VehicleCategory",
          "descriptor": { "code": "SEDAN" }
        }
      },
      "tags": [
        { "descriptor": { "code": "RENTAL_PACKAGE" }, "value": "8HR_80KM" },
        { "descriptor": { "code": "RIDER_CATEGORY" }, "value": "ADULT" }
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
    "transaction_id": "txn-cr-7b4e2d", "message_id": "msg-002",
    "timestamp": "2026-02-03T19:00:01+05:30", "ttl": "PT30S",
    "bap_id": "rental-app.bap.io", "bap_uri": "https://api.rental-app.io/beckn",
    "bpp_id": "goa-rentals.bpp.io", "bpp_uri": "https://api.goa-rentals.io/beckn"
  },
  "message": {
    "catalog": {
      "providers": [
        {
          "@type": "mobility:Operator",
          "id": "goa-rentals",
          "descriptor": { "name": "Goa Car Rentals", "short_desc": "Chauffeur-driven cab rentals in Goa" },
          "items": [
            {
              "@type": "mobility:RideOption",
              "id": "pkg-sedan-8hr",
              "descriptor": { "name": "Sedan 8Hr/80Km", "short_desc": "AC Sedan with driver for 8 hours" },
              "category_ids": ["SEDAN"],
              "price": {
                "@type": "mobility:FareEstimate",
                "value": "1800",
                "currency": "INR"
              },
              "tags": [
                { "descriptor": { "code": "VEHICLE_AC" }, "value": "yes" },
                { "descriptor": { "code": "VEHICLE_BOOT_SPACE_LITRES" }, "value": "350" },
                { "descriptor": { "code": "PACKAGE_HOURS" }, "value": "8" },
                { "descriptor": { "code": "PACKAGE_KM" }, "value": "80" }
              ]
            },
            {
              "@type": "mobility:AncillaryService",
              "id": "anc-insurance-rental",
              "descriptor": { "name": "Rental Insurance", "short_desc": "Comprehensive coverage for the rental period" },
              "price": { "value": "50", "currency": "INR" }
            }
          ],
          "fulfillments": [
            {
              "id": "ff-sedan-8hr",
              "type": "RENTAL",
              "tags": [
                {
                  "descriptor": { "code": "SYSTEM_PRICING_PLAN" },
                  "@type": "mobility:SystemPricingPlan",
                  "list": [
                    { "descriptor": { "code": "PER_TRIP_STARTING_FEE_INR" }, "value": "1800" },
                    { "descriptor": { "code": "PER_KM_CHARGING_RATE_INR" }, "value": "10" },
                    { "descriptor": { "code": "PER_MINUTE_CHARGING_RATE_INR" }, "value": "2" },
                    { "descriptor": { "code": "CURRENCY" }, "value": "INR" }
                  ]
                },
                {
                  "descriptor": { "code": "WAITING_POLICY" },
                  "@type": "mobility:WaitingPolicy",
                  "list": [
                    { "descriptor": { "code": "FREE_WAITING_MINUTES" }, "value": "5" },
                    { "descriptor": { "code": "CHARGE_PER_EXTRA_MINUTE_INR" }, "value": "2" }
                  ]
                },
                {
                  "descriptor": { "code": "CANCELLATION_POLICY" },
                  "@type": "mobility:CancellationPolicy",
                  "list": [
                    { "descriptor": { "code": "CANCELLATION_TERMS" }, "value": "Full refund if cancelled 4+ hours before start" },
                    { "descriptor": { "code": "REFUND_PERCENTAGE_WITHIN_4HR" }, "value": "50" }
                  ]
                },
                {
                  "descriptor": { "code": "BOOKING_RULE" },
                  "@type": "mobility:BookingRule",
                  "list": [
                    { "descriptor": { "code": "PRIOR_NOTICE_DURATION_MIN" }, "value": "60" },
                    { "descriptor": { "code": "LATEST_BOOKING_TIME" }, "value": "08:00" }
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
    "transaction_id": "txn-cr-7b4e2d", "message_id": "msg-003",
    "timestamp": "2026-02-03T19:01:00+05:30", "ttl": "PT30S",
    "bap_id": "rental-app.bap.io", "bap_uri": "https://api.rental-app.io/beckn",
    "bpp_id": "goa-rentals.bpp.io", "bpp_uri": "https://api.goa-rentals.io/beckn" },
  "message": {
    "order": {
      "provider": { "id": "goa-rentals" },
      "items": [
        { "id": "pkg-sedan-8hr", "quantity": { "count": 1 } },
        { "id": "anc-insurance-rental", "quantity": { "count": 1 } }
      ],
      "fulfillments": [
        {
          "id": "ff-sedan-8hr",
          "type": "RENTAL",
          "stops": [
            {
              "type": "START",
              "time": { "timestamp": "2026-02-04T09:00:00+05:30" },
              "location": {
                "@type": "mobility:Place",
                "gps": "15.5057,73.8264",
                "descriptor": { "name": "Grand Hyatt Goa — Hotel Lobby" }
              }
            }
          ],
          "tags": [
            { "descriptor": { "code": "SERVICE_CLASS" }, "value": "STANDARD" }
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
  "context": { "domain": "mobility", "action": "on_select", "version": "2.0",
    "transaction_id": "txn-cr-7b4e2d", "message_id": "msg-004",
    "timestamp": "2026-02-03T19:01:01+05:30", "ttl": "PT30S",
    "bap_id": "rental-app.bap.io", "bap_uri": "https://api.rental-app.io/beckn",
    "bpp_id": "goa-rentals.bpp.io", "bpp_uri": "https://api.goa-rentals.io/beckn" },
  "message": {
    "order": {
      "items": [
        { "id": "pkg-sedan-8hr", "price": { "value": "1800", "currency": "INR" } },
        { "id": "anc-insurance-rental", "price": { "value": "50", "currency": "INR" } }
      ],
      "fulfillments": [
        {
          "id": "ff-sedan-8hr",
          "tags": [
            {
              "descriptor": { "code": "SYSTEM_PRICING_PLAN" },
              "@type": "mobility:SystemPricingPlan",
              "list": [
                { "descriptor": { "code": "PER_TRIP_STARTING_FEE_INR" }, "value": "1800" },
                { "descriptor": { "code": "PER_KM_CHARGING_RATE_INR" }, "value": "10" },
                { "descriptor": { "code": "PER_MINUTE_CHARGING_RATE_INR" }, "value": "2" }
              ]
            }
          ]
        }
      ],
      "quote": {
        "price": { "value": "1918", "currency": "INR" },
        "breakup": [
          { "item": { "descriptor": { "code": "BASE_PACKAGE_8HR_80KM" } }, "price": { "value": "1800", "currency": "INR" } },
          { "item": { "descriptor": { "code": "INSURANCE" } }, "price": { "value": "50", "currency": "INR" } },
          { "item": { "descriptor": { "code": "PLATFORM_FEE" } }, "price": { "value": "18", "currency": "INR" } },
          { "item": { "descriptor": { "code": "EXTRA_KM_RATE_NOTE" } }, "price": { "value": "0", "currency": "INR" },
            "tags": [{ "descriptor": { "code": "NOTE" }, "value": "₹10/km charged for kms beyond 80" }] }
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
    "transaction_id": "txn-cr-7b4e2d", "message_id": "msg-005",
    "timestamp": "2026-02-03T19:01:30+05:30", "ttl": "PT30S",
    "bap_id": "rental-app.bap.io", "bap_uri": "https://api.rental-app.io/beckn",
    "bpp_id": "goa-rentals.bpp.io", "bpp_uri": "https://api.goa-rentals.io/beckn" },
  "message": {
    "order": {
      "provider": { "id": "goa-rentals" },
      "items": [
        { "id": "pkg-sedan-8hr", "quantity": { "count": 1 } },
        { "id": "anc-insurance-rental", "quantity": { "count": 1 } }
      ],
      "fulfillments": [
        {
          "id": "ff-sedan-8hr",
          "customer": {
            "@type": "mobility:Rider",
            "person": { "name": "Meera Iyer" },
            "contact": { "phone": "+919812345678", "email": "meera@example.com" }
          }
        }
      ],
      "billing": { "name": "Meera Iyer", "phone": "+919812345678", "email": "meera@example.com" }
    }
  }
}
```

### `on_init` (BPP → BAP)

```json
{
  "context": { "domain": "mobility", "action": "on_init", "version": "2.0",
    "transaction_id": "txn-cr-7b4e2d", "message_id": "msg-006",
    "timestamp": "2026-02-03T19:01:31+05:30", "ttl": "PT30S",
    "bap_id": "rental-app.bap.io", "bap_uri": "https://api.rental-app.io/beckn",
    "bpp_id": "goa-rentals.bpp.io", "bpp_uri": "https://api.goa-rentals.io/beckn" },
  "message": {
    "order": {
      "items": [
        { "id": "pkg-sedan-8hr", "price": { "value": "1800", "currency": "INR" } },
        { "id": "anc-insurance-rental", "price": { "value": "50", "currency": "INR" } }
      ],
      "fulfillments": [
        {
          "id": "ff-sedan-8hr",
          "tags": [
            {
              "descriptor": { "code": "ROUTE_PREFERENCE_FORM" },
              "list": [
                { "descriptor": { "code": "FORM_TYPE" }, "value": "ROUTE_PREFERENCE" },
                { "descriptor": { "code": "OPTION_TOLL" }, "value": "Include Toll Roads" },
                { "descriptor": { "code": "OPTION_NO_TOLL" }, "value": "Avoid Toll Roads" }
              ]
            },
            {
              "descriptor": { "code": "SYSTEM_PRICING_PLAN" },
              "@type": "mobility:SystemPricingPlan",
              "list": [
                { "descriptor": { "code": "PER_TRIP_STARTING_FEE_INR" }, "value": "1800" },
                { "descriptor": { "code": "PER_KM_CHARGING_RATE_INR" }, "value": "10" },
                { "descriptor": { "code": "PER_MINUTE_CHARGING_RATE_INR" }, "value": "2" },
                { "descriptor": { "code": "TAXABLE" }, "value": "true" }
              ]
            }
          ]
        }
      ],
      "quote": {
        "price": { "value": "1918", "currency": "INR" },
        "breakup": [
          { "item": { "descriptor": { "code": "BASE_PACKAGE" } }, "price": { "value": "1800", "currency": "INR" } },
          { "item": { "descriptor": { "code": "INSURANCE" } }, "price": { "value": "50", "currency": "INR" } },
          { "item": { "descriptor": { "code": "PLATFORM_FEE" } }, "price": { "value": "18", "currency": "INR" } }
        ]
      },
      "cancellation_terms": [
        { "fulfillment_state": { "descriptor": { "code": "BEFORE_4_HOURS" } }, "cancellation_fee": { "percentage": "0" } },
        { "fulfillment_state": { "descriptor": { "code": "WITHIN_4_HOURS" } }, "cancellation_fee": { "percentage": "50" } }
      ],
      "payments": [
        { "type": "ON_ORDER", "collected_by": "BPP", "status": "NOT-PAID",
          "tags": [{ "descriptor": { "code": "PAYMENT_CHANNEL_OPTIONS" }, "value": "ONLINE_UPI,ONLINE_CARD" }] }
      ]
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
    "transaction_id": "txn-cr-7b4e2d", "message_id": "msg-007",
    "timestamp": "2026-02-03T19:02:00+05:30", "ttl": "PT30S",
    "bap_id": "rental-app.bap.io", "bap_uri": "https://api.rental-app.io/beckn",
    "bpp_id": "goa-rentals.bpp.io", "bpp_uri": "https://api.goa-rentals.io/beckn" },
  "message": {
    "order": {
      "provider": { "id": "goa-rentals" },
      "items": [
        { "id": "pkg-sedan-8hr", "quantity": { "count": 1 } },
        { "id": "anc-insurance-rental", "quantity": { "count": 1 } }
      ],
      "fulfillments": [
        {
          "id": "ff-sedan-8hr",
          "customer": { "person": { "name": "Meera Iyer" }, "contact": { "phone": "+919812345678" } },
          "tags": [{ "descriptor": { "code": "ROUTE_PREFERENCE" }, "value": "NO_TOLL" }]
        }
      ],
      "billing": { "name": "Meera Iyer", "phone": "+919812345678", "email": "meera@example.com" },
      "payments": [
        { "type": "ON_ORDER", "collected_by": "BPP", "status": "PAID",
          "transaction_id": "upi-txn-goa-cr-001",
          "tags": [{ "descriptor": { "code": "PAYMENT_CHANNEL" }, "value": "ONLINE_UPI" }] }
      ]
    }
  }
}
```

### `on_confirm` (BPP → BAP)

```json
{
  "context": { "domain": "mobility", "action": "on_confirm", "version": "2.0",
    "transaction_id": "txn-cr-7b4e2d", "message_id": "msg-008",
    "timestamp": "2026-02-03T19:02:02+05:30", "ttl": "PT30S",
    "bap_id": "rental-app.bap.io", "bap_uri": "https://api.rental-app.io/beckn",
    "bpp_id": "goa-rentals.bpp.io", "bpp_uri": "https://api.goa-rentals.io/beckn" },
  "message": {
    "order": {
      "@type": "mobility:Trip",
      "id": "rental-goa-20260204-001",
      "status": "SEARCHING_DRIVER",
      "provider": { "@type": "mobility:Operator", "id": "goa-rentals", "descriptor": { "name": "Goa Car Rentals" } },
      "items": [
        { "id": "pkg-sedan-8hr", "descriptor": { "name": "Sedan 8Hr/80Km" }, "price": { "value": "1800", "currency": "INR" } },
        { "id": "anc-insurance-rental", "descriptor": { "name": "Rental Insurance" }, "price": { "value": "50", "currency": "INR" } }
      ],
      "fulfillments": [
        {
          "id": "ff-sedan-8hr",
          "state": {
            "@type": "mobility:Event",
            "descriptor": { "code": "DRIVER_ALLOCATION_SEARCHING", "name": "Allocating driver for 9 AM pickup..." }
          },
          "stops": [
            {
              "type": "START",
              "time": { "timestamp": "2026-02-04T09:00:00+05:30" },
              "location": { "gps": "15.5057,73.8264", "descriptor": { "name": "Grand Hyatt Goa — Hotel Lobby" } },
              "instructions": {
                "@type": "mobility:PickupDropoffPoint",
                "descriptor": { "name": "Driver will meet you at the hotel main entrance" }
              }
            }
          ],
          "tags": [
            {
              "descriptor": { "code": "SYSTEM_PRICING_PLAN" },
              "@type": "mobility:SystemPricingPlan",
              "list": [
                { "descriptor": { "code": "PER_TRIP_STARTING_FEE_INR" }, "value": "1800" },
                { "descriptor": { "code": "PER_KM_CHARGING_RATE_INR" }, "value": "10" },
                { "descriptor": { "code": "PER_MINUTE_CHARGING_RATE_INR" }, "value": "2" }
              ]
            },
            { "descriptor": { "code": "ROUTE_PREFERENCE" }, "value": "NO_TOLL" }
          ]
        }
      ],
      "billing": { "name": "Meera Iyer", "phone": "+919812345678", "email": "meera@example.com" },
      "quote": {
        "price": { "value": "1918", "currency": "INR" },
        "breakup": [
          { "item": { "descriptor": { "code": "BASE_PACKAGE" } }, "price": { "value": "1800", "currency": "INR" } },
          { "item": { "descriptor": { "code": "INSURANCE" } }, "price": { "value": "50", "currency": "INR" } },
          { "item": { "descriptor": { "code": "PLATFORM_FEE" } }, "price": { "value": "18", "currency": "INR" } }
        ]
      },
      "payments": [{ "type": "ON_ORDER", "status": "PAID", "transaction_id": "upi-txn-goa-cr-001" }],
      "created_at": "2026-02-03T19:02:02+05:30"
    }
  }
}
```

---

## 5. on_update — Driver Assigned (BPP-Initiated at 8:45 AM)

```json
{
  "context": { "domain": "mobility", "action": "on_update", "version": "2.0",
    "transaction_id": "txn-cr-7b4e2d", "message_id": "msg-009",
    "timestamp": "2026-02-04T08:45:00+05:30", "ttl": "PT30S",
    "bap_id": "rental-app.bap.io", "bap_uri": "https://api.rental-app.io/beckn",
    "bpp_id": "goa-rentals.bpp.io", "bpp_uri": "https://api.goa-rentals.io/beckn" },
  "message": {
    "order": {
      "@type": "mobility:Trip",
      "id": "rental-goa-20260204-001",
      "status": "DRIVER_ASSIGNED",
      "fulfillments": [
        {
          "id": "ff-sedan-8hr",
          "state": { "@type": "mobility:Event", "descriptor": { "code": "DRIVER_ASSIGNED", "name": "Driver en route to hotel" } },
          "agent": {
            "@type": "mobility:Driver",
            "person": { "name": "Vishwas Naik", "image": "https://cdn.goa-rentals.io/drivers/d-goa-221.jpg" },
            "rating": "4.9",
            "tags": [
              { "descriptor": { "code": "LICENSE_NUMBER" }, "value": "GA01 20180034567" },
              { "descriptor": { "code": "YEARS_OF_EXPERIENCE" }, "value": "8" }
            ]
          },
          "vehicle": {
            "@type": "mobility:Vehicle",
            "registration": "GA-01-AA-4421",
            "model": "Honda City",
            "color": "Silver",
            "year": "2023"
          },
          "tracking": true,
          "contact": { "@type": "mobility:ContactHandle", "phone": "+91-MASKED-2233", "descriptor": { "name": "Call Driver" } },
          "start": {
            "authorization": { "type": "OTP", "token": "7732", "valid_from": "2026-02-04T08:45:00+05:30", "valid_to": "2026-02-04T10:00:00+05:30" }
          },
          "tags": [
            {
              "descriptor": { "code": "CURRENT_LOCATION" },
              "@type": "mobility:VehiclePosition",
              "list": [
                { "descriptor": { "code": "LATITUDE" }, "value": "15.5103" },
                { "descriptor": { "code": "LONGITUDE" }, "value": "73.8210" },
                { "descriptor": { "code": "ETA_MINUTES" }, "value": "12" }
              ]
            },
            {
              "descriptor": { "code": "SYSTEM_PRICING_PLAN" },
              "@type": "mobility:SystemPricingPlan",
              "list": [
                { "descriptor": { "code": "PER_TRIP_STARTING_FEE_INR" }, "value": "1800" },
                { "descriptor": { "code": "PER_KM_CHARGING_RATE_INR" }, "value": "10" },
                { "descriptor": { "code": "PER_MINUTE_CHARGING_RATE_INR" }, "value": "2" }
              ]
            }
          ]
        }
      ],
      "updated_at": "2026-02-04T08:45:00+05:30"
    }
  }
}
```

---

## 6. status / on_status — Mid-Day Check (Odometer + Overage Warning)

### `status` (BAP → BPP)

```json
{
  "context": { "domain": "mobility", "action": "status", "version": "2.0",
    "transaction_id": "txn-cr-7b4e2d", "message_id": "msg-010",
    "timestamp": "2026-02-04T14:30:00+05:30", "ttl": "PT30S",
    "bap_id": "rental-app.bap.io", "bap_uri": "https://api.rental-app.io/beckn",
    "bpp_id": "goa-rentals.bpp.io", "bpp_uri": "https://api.goa-rentals.io/beckn" },
  "message": { "order_id": "rental-goa-20260204-001" }
}
```

### `on_status` (BPP → BAP) — 72 km used, 8 km remaining in package

```json
{
  "context": { "domain": "mobility", "action": "on_status", "version": "2.0",
    "transaction_id": "txn-cr-7b4e2d", "message_id": "msg-011",
    "timestamp": "2026-02-04T14:30:01+05:30", "ttl": "PT30S",
    "bap_id": "rental-app.bap.io", "bap_uri": "https://api.rental-app.io/beckn",
    "bpp_id": "goa-rentals.bpp.io", "bpp_uri": "https://api.goa-rentals.io/beckn" },
  "message": {
    "order": {
      "@type": "mobility:Trip",
      "id": "rental-goa-20260204-001",
      "status": "RENTAL_IN_PROGRESS",
      "fulfillments": [
        {
          "id": "ff-sedan-8hr",
          "state": {
            "@type": "mobility:Event",
            "descriptor": { "code": "OVERAGE_WARNING", "name": "72 km used. 8 km remaining in package." }
          },
          "tags": [
            {
              "descriptor": { "code": "ODOMETER" },
              "@type": "mobility:Telemetry",
              "list": [
                { "descriptor": { "code": "ODOMETER_KM" }, "value": "72" },
                { "descriptor": { "code": "HOURS_ELAPSED" }, "value": "5.5" },
                { "descriptor": { "code": "KM_REMAINING_IN_PACKAGE" }, "value": "8" }
              ]
            },
            {
              "descriptor": { "code": "RUNNING_QUOTE" },
              "list": [
                { "descriptor": { "code": "BASE_PACKAGE_INR" }, "value": "1800" },
                { "descriptor": { "code": "INSURANCE_INR" }, "value": "50" },
                { "descriptor": { "code": "PLATFORM_FEE_INR" }, "value": "18" },
                { "descriptor": { "code": "PROJECTED_OVERAGE_NOTE" }, "value": "₹10/km beyond 80 km" }
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

## 7. update / on_update — End of Rental, Overage Settlement

### `update` (BPP-Initiated, end of rental — 22 extra km)

```json
{
  "context": { "domain": "mobility", "action": "on_update", "version": "2.0",
    "transaction_id": "txn-cr-7b4e2d", "message_id": "msg-012",
    "timestamp": "2026-02-04T17:05:00+05:30", "ttl": "PT30S",
    "bap_id": "rental-app.bap.io", "bap_uri": "https://api.rental-app.io/beckn",
    "bpp_id": "goa-rentals.bpp.io", "bpp_uri": "https://api.goa-rentals.io/beckn" },
  "message": {
    "order": {
      "@type": "mobility:Trip",
      "id": "rental-goa-20260204-001",
      "status": "RENTAL_COMPLETED",
      "fulfillments": [
        {
          "id": "ff-sedan-8hr",
          "state": { "@type": "mobility:Event", "descriptor": { "code": "RENTAL_COMPLETED", "name": "Rental completed. 102 km total." } },
          "tags": [
            {
              "descriptor": { "code": "FINAL_ODOMETER" },
              "list": [
                { "descriptor": { "code": "TOTAL_KM" }, "value": "102" },
                { "descriptor": { "code": "OVERAGE_KM" }, "value": "22" },
                { "descriptor": { "code": "TOTAL_HOURS" }, "value": "8.08" }
              ]
            }
          ]
        }
      ],
      "quote": {
        "@type": "mobility:FareBreakup",
        "price": { "value": "2158", "currency": "INR" },
        "breakup": [
          { "item": { "descriptor": { "code": "BASE_PACKAGE_8HR_80KM" } }, "price": { "value": "1800", "currency": "INR" } },
          { "item": { "descriptor": { "code": "OVERAGE_22KM_AT_10_PER_KM" } }, "price": { "value": "220", "currency": "INR" } },
          { "item": { "descriptor": { "code": "INSURANCE" } }, "price": { "value": "50", "currency": "INR" } },
          { "item": { "descriptor": { "code": "PLATFORM_FEE" } }, "price": { "value": "18", "currency": "INR" } },
          { "item": { "descriptor": { "code": "GST_5_PERCENT" } }, "price": { "value": "70", "currency": "INR" } }
        ]
      },
      "payments": [
        { "type": "ON_ORDER", "status": "PAID", "transaction_id": "upi-txn-goa-cr-001" },
        { "type": "ON_FULFILLMENT", "collected_by": "BPP", "status": "NOT-PAID",
          "amount": { "value": "240", "currency": "INR" },
          "tags": [{ "descriptor": { "code": "OVERAGE_CHARGE" }, "value": "220 + 20 GST on overage" }] }
      ],
      "updated_at": "2026-02-04T17:05:00+05:30"
    }
  }
}
```

---

## 8. cancel / on_cancel — Pre-Rental Cancellation

### `cancel` / `on_cancel` *(same structure as ride hailing — see ride hailing guide)*

```json
{
  "context": { "domain": "mobility", "action": "on_cancel", "version": "2.0",
    "transaction_id": "txn-cr-7b4e2d", "message_id": "msg-013",
    "timestamp": "2026-02-03T20:00:00+05:30", "ttl": "PT30S",
    "bap_id": "rental-app.bap.io", "bap_uri": "https://api.rental-app.io/beckn",
    "bpp_id": "goa-rentals.bpp.io", "bpp_uri": "https://api.goa-rentals.io/beckn" },
  "message": {
    "order": {
      "@type": "mobility:Trip",
      "id": "rental-goa-20260204-001",
      "status": "CANCELLED",
      "quote": {
        "price": { "value": "0", "currency": "INR" },
        "breakup": [
          { "item": { "descriptor": { "code": "FULL_REFUND" } }, "price": { "value": "1918", "currency": "INR" },
            "tags": [{ "descriptor": { "code": "NOTE" }, "value": "Cancelled 13 hours before pickup — full refund" }] }
        ]
      }
    }
  }
}
```

---

## 9. rating / on_rating

```json
{
  "context": { "domain": "mobility", "action": "rating", "version": "2.0",
    "transaction_id": "txn-cr-7b4e2d", "message_id": "msg-014",
    "timestamp": "2026-02-04T17:30:00+05:30", "ttl": "PT30S",
    "bap_id": "rental-app.bap.io", "bap_uri": "https://api.rental-app.io/beckn",
    "bpp_id": "goa-rentals.bpp.io", "bpp_uri": "https://api.goa-rentals.io/beckn" },
  "message": {
    "ratings": [
      { "@type": "mobility:Rating", "id": "rat-cr-01", "rating_category": "Driver", "value": "5",
        "tags": [{ "descriptor": { "code": "RATED_ENTITY_TYPE" }, "value": "DRIVER" }] },
      { "@type": "mobility:Rating", "id": "rat-cr-02", "rating_category": "Vehicle", "value": "5",
        "tags": [{ "descriptor": { "code": "RATED_ENTITY_TYPE" }, "value": "VEHICLE" }] },
      { "@type": "mobility:Rating", "id": "rat-cr-03", "rating_category": "Service", "value": "4",
        "tags": [{ "descriptor": { "code": "RATED_ENTITY_TYPE" }, "value": "SERVICE" }] }
    ],
    "feedback_form": {
      "@type": "mobility:Review",
      "responses": [{ "question": { "code": "REVIEW_TEXT" }, "answer": "Vishwas was excellent! Overage billing was a bit surprising." }]
    },
    "tags": [{ "descriptor": { "code": "FEEDBACK_TAGS" }, "value": "CLEAN_VEHICLE,HELPFUL_DRIVER" }]
  }
}
```

---

## 10. support / on_support — Billing Dispute

```json
{
  "context": { "domain": "mobility", "action": "support", "version": "2.0",
    "transaction_id": "txn-cr-7b4e2d", "message_id": "msg-015",
    "timestamp": "2026-02-04T18:00:00+05:30", "ttl": "PT30S",
    "bap_id": "rental-app.bap.io", "bap_uri": "https://api.rental-app.io/beckn",
    "bpp_id": "goa-rentals.bpp.io", "bpp_uri": "https://api.goa-rentals.io/beckn" },
  "message": {
    "support": {
      "@type": "mobility:SupportCase",
      "order_id": "rental-goa-20260204-001",
      "type": "BILLING_DISPUTE",
      "descriptor": { "short_desc": "Overage of 22 km seems incorrect — I think I drove 95 km total" }
    }
  }
}
```

```json
{
  "context": { "domain": "mobility", "action": "on_support", "version": "2.0",
    "transaction_id": "txn-cr-7b4e2d", "message_id": "msg-016",
    "timestamp": "2026-02-04T18:00:02+05:30", "ttl": "PT30S",
    "bap_id": "rental-app.bap.io", "bap_uri": "https://api.rental-app.io/beckn",
    "bpp_id": "goa-rentals.bpp.io", "bpp_uri": "https://api.goa-rentals.io/beckn" },
  "message": {
    "support": {
      "@type": "mobility:SupportCase",
      "order_id": "rental-goa-20260204-001",
      "ref_id": "case-billing-goa-882",
      "descriptor": { "short_desc": "Odometer dispute case opened. GPS log attached." },
      "phone": "+91-832-2441100",
      "email": "support@goa-rentals.io",
      "url": "https://support.goa-rentals.io/case/case-billing-goa-882",
      "tags": [
        { "descriptor": { "code": "RECEIPT_URL" }, "value": "https://receipts.goa-rentals.io/rental-goa-20260204-001.pdf" },
        { "descriptor": { "code": "GPS_LOG_URL" }, "value": "https://track.goa-rentals.io/log/rental-goa-20260204-001" }
      ]
    }
  }
}
```
