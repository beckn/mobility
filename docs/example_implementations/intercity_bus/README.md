# Intercity Bus Transport — End-to-End Implementation Guide

## Overview

This guide provides complete Beckn protocol v2.0 JSON payloads for an intercity bus booking transaction.

**Scenario:** Sanjay searches for KSRTC Volvo buses from Bengaluru city to Mysuru city for 2 adults. He selects the 6 AM Volvo Sleeper, picks seats 12A and 12B at Bay 7 (Kempegowda Bus Terminal), pays ₹700, and receives QR tickets with pickup instructions. On travel day, the bus is 15 minutes late — BPP pushes a delay notification. After departure, BPP activates live tracking via `on_update`.

**Key differentiators from city bus:**
- Search is **city-to-city** using `Place` (not stop-to-stop)
- Catalog shows **operators** with bus features, pickup/drop locations, and shuttle availability
- `select` commits to **specific pickup and drop stations** within the city + seat selection
- `init` collects **both passengers** (billing + travel participant)
- `on_confirm` issues **two QR tickets** + pickup point instructions + invoice link
- `on_update` after departure carries **tracking active flag** + optional GPS URL

---

## Context Values

| Field | Value |
|-------|-------|
| `domain` | `mobility` |
| `bap_id` | `redbus.bap.io` |
| `bpp_id` | `ksrtc.bpp.io` |
| `transaction_id` | `txn-icb-3a7e9d` |

---

## 1. search / on_search — City-to-City Discovery

### `search` (BAP → BPP) — CITY-LEVEL Place, NOT stop-to-stop

```json
{
  "context": {
    "domain": "mobility", "action": "search", "version": "2.0",
    "transaction_id": "txn-icb-3a7e9d", "message_id": "msg-001",
    "timestamp": "2026-02-03T20:00:00+05:30", "ttl": "PT30S",
    "bap_id": "redbus.bap.io", "bap_uri": "https://api.redbus.in/beckn",
    "location": { "country": { "code": "IND" } }
  },
  "message": {
    "intent": {
      "@type": "mobility:TripSpecification",
      "fulfillment": {
        "stops": [
          {
            "type": "START",
            "location": {
              "@type": "mobility:Place",
              "descriptor": { "name": "Bengaluru" },
              "tags": [{ "descriptor": { "code": "PLACE_TYPE" }, "value": "CITY" }]
            }
          },
          {
            "type": "END",
            "location": {
              "@type": "mobility:Place",
              "descriptor": { "name": "Mysuru" },
              "tags": [{ "descriptor": { "code": "PLACE_TYPE" }, "value": "CITY" }]
            }
          }
        ],
        "time": { "timestamp": "2026-02-04T05:00:00+05:30", "label": "TRAVEL_DATE" }
      },
      "tags": [
        { "descriptor": { "code": "NUM_TRAVELERS" }, "value": "2" },
        { "descriptor": { "code": "RIDER_CATEGORY" }, "value": "ADULT" },
        { "descriptor": { "code": "SERVICE_CLASS_PREFERENCE" }, "value": "VOLVO_SLEEPER" },
        { "descriptor": { "code": "MODES" }, "value": "BUS" }
      ]
    }
  }
}
```

### `on_search` (BPP → BAP) — Operators + Bus Features + Pickup/Drop Locations + Shuttle

```json
{
  "context": {
    "domain": "mobility", "action": "on_search", "version": "2.0",
    "transaction_id": "txn-icb-3a7e9d", "message_id": "msg-002",
    "timestamp": "2026-02-03T20:00:01+05:30", "ttl": "PT30S",
    "bap_id": "redbus.bap.io", "bap_uri": "https://api.redbus.in/beckn",
    "bpp_id": "ksrtc.bpp.io", "bpp_uri": "https://api.ksrtc.in/beckn"
  },
  "message": {
    "catalog": {
      "@type": "mobility:TripResult",
      "providers": [
        {
          "@type": "mobility:Operator",
          "id": "ksrtc-karnataka",
          "descriptor": {
            "name": "KSRTC Karnataka",
            "short_desc": "Karnataka State Road Transport Corporation",
            "images": ["https://cdn.ksrtc.in/logo.png"]
          },
          "items": [
            {
              "@type": "mobility:FareProduct",
              "id": "fare-ksrtc-volvo-adult",
              "descriptor": { "name": "Volvo A/C Sleeper — Adult", "short_desc": "Single trip, Bengaluru to Mysuru" },
              "price": { "value": "350", "currency": "INR" },
              "tags": [
                { "descriptor": { "code": "RIDER_CATEGORY_ID" }, "value": "ADULT" },
                { "descriptor": { "code": "DURATION_TYPE" }, "value": "SINGLE_TRIP" }
              ]
            },
            {
              "@type": "mobility:SalesOfferPackage",
              "id": "pkg-ksrtc-volvo-with-insurance",
              "descriptor": { "name": "Volvo Seat + Travel Insurance Bundle" },
              "price": { "value": "365", "currency": "INR" },
              "tags": [
                { "descriptor": { "code": "FARE_PRODUCTS" }, "value": "fare-ksrtc-volvo-adult + insurance" }
              ]
            }
          ],
          "fulfillments": [
            {
              "@type": "mobility:Journey",
              "id": "journey-ksrtc-0600",
              "descriptor": { "name": "KSRTC Volvo 06:00 AM — Bengaluru to Mysuru", "short_desc": "3h 30min, Volvo A/C Sleeper" },
              "legs": [
                {
                  "@type": "mobility:Leg",
                  "mode": "BUS",
                  "route": {
                    "@type": "mobility:Route",
                    "id": "KSRTC-RT-BLR-MYS-001",
                    "descriptor": { "name": "Bengaluru — Mysuru Express", "short_name": "BLR-MYS" }
                  },
                  "vehicle_journey": {
                    "@type": "mobility:VehicleJourney",
                    "id": "vj-ksrtc-0600",
                    "departure": "2026-02-04T06:00:00+05:30",
                    "arrival": "2026-02-04T09:30:00+05:30"
                  },
                  "segments": [
                    {
                      "@type": "mobility:Segment",
                      "segment_number": 1,
                      "train_number": "KSRTC-KA-4421",
                      "origin": { "descriptor": { "name": "Bengaluru" } },
                      "destination": { "descriptor": { "name": "Ramanagara" } }
                    },
                    {
                      "@type": "mobility:Segment",
                      "segment_number": 2,
                      "origin": { "descriptor": { "name": "Ramanagara" } },
                      "destination": { "descriptor": { "name": "Mysuru" } }
                    }
                  ]
                }
              ],
              "tags": [
                {
                  "descriptor": { "code": "VEHICLE_TYPE" },
                  "@type": "mobility:VehicleType",
                  "list": [
                    { "descriptor": { "code": "VEHICLE_TYPE_CODE" }, "value": "BUS" },
                    { "descriptor": { "code": "MAX_CAPACITY" }, "value": "40" },
                    { "descriptor": { "code": "AC" }, "value": "yes" },
                    { "descriptor": { "code": "WIFI" }, "value": "yes" },
                    { "descriptor": { "code": "CHARGING_POINTS" }, "value": "yes" },
                    { "descriptor": { "code": "RECLINING_SEATS" }, "value": "yes" }
                  ]
                },
                {
                  "descriptor": { "code": "SERVICE_CLASS" },
                  "@type": "mobility:ServiceClass",
                  "list": [{ "descriptor": { "code": "SERVICE_CLASS_CODE" }, "value": "VOLVO_AC_SLEEPER" }]
                },
                {
                  "descriptor": { "code": "PICKUP_STOPS_BENGALURU" },
                  "list": [
                    { "@type": "mobility:Stop", "descriptor": { "code": "STOP_ID" }, "value": "BLR-KBS-BAY7",
                      "tags": [{ "descriptor": { "code": "STOP_NAME" }, "value": "Kempegowda Bus Terminal — Bay 7" },
                               { "descriptor": { "code": "DEPARTURE_TIME" }, "value": "06:00" }] },
                    { "@type": "mobility:Stop", "descriptor": { "code": "STOP_ID" }, "value": "BLR-SATELLITE-01",
                      "tags": [{ "descriptor": { "code": "STOP_NAME" }, "value": "Satellite Bus Station, Mysore Road" },
                               { "descriptor": { "code": "DEPARTURE_TIME" }, "value": "06:25" }] }
                  ]
                },
                {
                  "descriptor": { "code": "DROP_STOPS_MYSURU" },
                  "list": [
                    { "@type": "mobility:Stop", "descriptor": { "code": "STOP_ID" }, "value": "MYS-CBS-MAIN",
                      "tags": [{ "descriptor": { "code": "STOP_NAME" }, "value": "Mysuru Central Bus Stand" },
                               { "descriptor": { "code": "ARRIVAL_TIME" }, "value": "09:30" }] },
                    { "@type": "mobility:Stop", "descriptor": { "code": "STOP_ID" }, "value": "MYS-AGARA-01",
                      "tags": [{ "descriptor": { "code": "STOP_NAME" }, "value": "Agara Bus Stand" },
                               { "descriptor": { "code": "ARRIVAL_TIME" }, "value": "09:45" }] }
                  ]
                },
                {
                  "descriptor": { "code": "SHUTTLE_AVAILABILITY" },
                  "@type": "mobility:AncillaryService",
                  "list": [
                    { "descriptor": { "code": "SERVICE_CODE" }, "value": "CITY_SHUTTLE_MYS" },
                    { "descriptor": { "code": "SERVICE_CATEGORY" }, "value": "SHUTTLE" },
                    { "descriptor": { "code": "DESCRIPTION" }, "value": "City shuttle from Mysuru CBS to hotel zones — ₹50 per person" }
                  ]
                },
                {
                  "descriptor": { "code": "SEAT_MAP_AVAILABLE" },
                  "list": [
                    { "descriptor": { "code": "AVAILABLE_SEATS" }, "value": "12A,12B,14A,14B,16A,18B" },
                    { "descriptor": { "code": "SEAT_TYPES" }, "value": "WINDOW(A), AISLE(B), LOWER_BERTH" }
                  ]
                },
                {
                  "descriptor": { "code": "BAGGAGE_ALLOWANCE" },
                  "@type": "mobility:BaggageAllowance",
                  "list": [
                    { "descriptor": { "code": "CHECKED_BAGGAGE_COUNT" }, "value": "1" },
                    { "descriptor": { "code": "CHECKED_BAGGAGE_WEIGHT_KG" }, "value": "15" }
                  ]
                },
                {
                  "descriptor": { "code": "BOOKING_RULE" },
                  "@type": "mobility:BookingRule",
                  "list": [{ "descriptor": { "code": "LATEST_BOOKING_TIME" }, "value": "05:00 on travel date" }]
                },
                {
                  "descriptor": { "code": "CANCELLATION_POLICY" },
                  "@type": "mobility:CancellationPolicy",
                  "list": [
                    { "descriptor": { "code": "REFUND_PERCENTAGE_BEFORE_24HR" }, "value": "100" },
                    { "descriptor": { "code": "REFUND_PERCENTAGE_4_TO_24HR" }, "value": "50" },
                    { "descriptor": { "code": "REFUND_PERCENTAGE_WITHIN_4HR" }, "value": "0" }
                  ]
                },
                {
                  "descriptor": { "code": "FARE_LEG_RULE" },
                  "@type": "mobility:FareLegRule",
                  "list": [
                    { "descriptor": { "code": "FARE_PRODUCT_ID" }, "value": "fare-ksrtc-volvo-adult" },
                    { "descriptor": { "code": "CONTAINS_SERVICE_ID" }, "value": "KSRTC-RT-BLR-MYS-001" }
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

## 2. select / on_select — Operator + Seats + Actual Pickup/Drop Stations

### `select` (BAP → BPP) — Commits to specific pickup/drop stops and seats

```json
{
  "context": { "domain": "mobility", "action": "select", "version": "2.0",
    "transaction_id": "txn-icb-3a7e9d", "message_id": "msg-003",
    "timestamp": "2026-02-03T20:01:00+05:30", "ttl": "PT30S",
    "bap_id": "redbus.bap.io", "bap_uri": "https://api.redbus.in/beckn",
    "bpp_id": "ksrtc.bpp.io", "bpp_uri": "https://api.ksrtc.in/beckn" },
  "message": {
    "order": {
      "provider": { "id": "ksrtc-karnataka" },
      "items": [{ "id": "fare-ksrtc-volvo-adult", "quantity": { "count": 2 } }],
      "fulfillments": [
        {
          "id": "journey-ksrtc-0600",
          "stops": [
            {
              "type": "START",
              "location": {
                "@type": "mobility:Stop",
                "id": "BLR-KBS-BAY7",
                "descriptor": { "name": "Kempegowda Bus Terminal — Bay 7" }
              }
            },
            {
              "type": "END",
              "location": {
                "@type": "mobility:Stop",
                "id": "MYS-CBS-MAIN",
                "descriptor": { "name": "Mysuru Central Bus Stand" }
              }
            }
          ],
          "tags": [
            { "descriptor": { "code": "VEHICLE_JOURNEY_ID" }, "value": "vj-ksrtc-0600" },
            { "descriptor": { "code": "OPERATOR_ID" }, "value": "ksrtc-karnataka" },
            { "descriptor": { "code": "PASSENGER_COUNT" }, "value": "2" },
            { "descriptor": { "code": "SERVICE_CLASS" }, "value": "VOLVO_AC_SLEEPER" },
            {
              "descriptor": { "code": "SEAT_REQUESTS" },
              "list": [
                { "@type": "mobility:PlaceRequest", "descriptor": { "code": "PASSENGER_1_SEAT" }, "value": "12A",
                  "tags": [{ "descriptor": { "code": "ACCOMMODATION_TYPE" }, "value": "SEAT" },
                           { "descriptor": { "code": "PREFERENCES" }, "value": "WINDOW" }] },
                { "@type": "mobility:PlaceRequest", "descriptor": { "code": "PASSENGER_2_SEAT" }, "value": "12B",
                  "tags": [{ "descriptor": { "code": "ACCOMMODATION_TYPE" }, "value": "SEAT" },
                           { "descriptor": { "code": "PREFERENCES" }, "value": "AISLE" }] }
              ]
            }
          ]
        }
      ]
    }
  }
}
```

### `on_select` (BPP → BAP) — Seats locked for 10 min

```json
{
  "context": { "domain": "mobility", "action": "on_select", "version": "2.0",
    "transaction_id": "txn-icb-3a7e9d", "message_id": "msg-004",
    "timestamp": "2026-02-03T20:01:01+05:30", "ttl": "PT30S",
    "bap_id": "redbus.bap.io", "bap_uri": "https://api.redbus.in/beckn",
    "bpp_id": "ksrtc.bpp.io", "bpp_uri": "https://api.ksrtc.in/beckn" },
  "message": {
    "order": {
      "items": [{ "id": "fare-ksrtc-volvo-adult", "quantity": { "count": 2 }, "price": { "value": "700", "currency": "INR" } }],
      "fulfillments": [
        {
          "id": "journey-ksrtc-0600",
          "tags": [
            {
              "descriptor": { "code": "CONFIRMED_SEATS" },
              "list": [
                { "@type": "mobility:Seat", "descriptor": { "code": "SEAT_12A" }, "value": "12A",
                  "tags": [{ "descriptor": { "code": "SEAT_TYPE" }, "value": "WINDOW" },
                           { "descriptor": { "code": "LOCKED_UNTIL" }, "value": "2026-02-03T20:11:00+05:30" }] },
                { "@type": "mobility:Seat", "descriptor": { "code": "SEAT_12B" }, "value": "12B",
                  "tags": [{ "descriptor": { "code": "SEAT_TYPE" }, "value": "AISLE" },
                           { "descriptor": { "code": "LOCKED_UNTIL" }, "value": "2026-02-03T20:11:00+05:30" }] }
              ]
            },
            { "descriptor": { "code": "DEPARTURE_TIME" }, "value": "2026-02-04T06:00:00+05:30" },
            { "descriptor": { "code": "BOARDING_OPENS" }, "value": "2026-02-04T05:45:00+05:30" }
          ]
        }
      ],
      "quote": {
        "price": { "value": "700", "currency": "INR" },
        "breakup": [
          { "item": { "descriptor": { "code": "SEAT_12A_ADULT" } }, "price": { "value": "350", "currency": "INR" } },
          { "item": { "descriptor": { "code": "SEAT_12B_ADULT" } }, "price": { "value": "350", "currency": "INR" } }
        ]
      }
    }
  }
}
```

---

## 3. init / on_init — Both Passenger Details

### `init` (BAP → BPP) — Billing + travel participants

```json
{
  "context": { "domain": "mobility", "action": "init", "version": "2.0",
    "transaction_id": "txn-icb-3a7e9d", "message_id": "msg-005",
    "timestamp": "2026-02-03T20:02:00+05:30", "ttl": "PT30S",
    "bap_id": "redbus.bap.io", "bap_uri": "https://api.redbus.in/beckn",
    "bpp_id": "ksrtc.bpp.io", "bpp_uri": "https://api.ksrtc.in/beckn" },
  "message": {
    "order": {
      "provider": { "id": "ksrtc-karnataka" },
      "items": [{ "id": "fare-ksrtc-volvo-adult", "quantity": { "count": 2 } }],
      "fulfillments": [
        {
          "id": "journey-ksrtc-0600",
          "passengers": [
            {
              "@type": "mobility:Passenger",
              "id": "pax-1",
              "person": { "name": "Sanjay Rao" },
              "contact": { "phone": "+919911223344", "email": "sanjay@example.com" },
              "tags": [
                { "descriptor": { "code": "PASSENGER_TYPE" }, "value": "ADULT" },
                { "descriptor": { "code": "BILLING_CONTACT" }, "value": "true" },
                { "descriptor": { "code": "SEAT_ID" }, "value": "12A" }
              ]
            },
            {
              "@type": "mobility:Passenger",
              "id": "pax-2",
              "person": { "name": "Anjali Rao" },
              "contact": { "phone": "+919911223345" },
              "tags": [
                { "descriptor": { "code": "PASSENGER_TYPE" }, "value": "ADULT" },
                { "descriptor": { "code": "SEAT_ID" }, "value": "12B" }
              ]
            }
          ]
        }
      ],
      "billing": { "name": "Sanjay Rao", "phone": "+919911223344", "email": "sanjay@example.com" }
    }
  }
}
```

### `on_init` (BPP → BAP)

```json
{
  "context": { "domain": "mobility", "action": "on_init", "version": "2.0",
    "transaction_id": "txn-icb-3a7e9d", "message_id": "msg-006",
    "timestamp": "2026-02-03T20:02:01+05:30", "ttl": "PT30S",
    "bap_id": "redbus.bap.io", "bap_uri": "https://api.redbus.in/beckn",
    "bpp_id": "ksrtc.bpp.io", "bpp_uri": "https://api.ksrtc.in/beckn" },
  "message": {
    "order": {
      "fulfillments": [{ "id": "journey-ksrtc-0600" }],
      "quote": { "price": { "value": "700", "currency": "INR" }, "breakup": [
        { "item": { "descriptor": { "code": "SEAT_12A_ADULT" } }, "price": { "value": "350", "currency": "INR" } },
        { "item": { "descriptor": { "code": "SEAT_12B_ADULT" } }, "price": { "value": "350", "currency": "INR" } }
      ]},
      "cancellation_terms": [
        { "fulfillment_state": { "descriptor": { "code": "MORE_THAN_24HR_BEFORE" } }, "cancellation_fee": { "percentage": "0" } },
        { "fulfillment_state": { "descriptor": { "code": "4_TO_24HR_BEFORE" } }, "cancellation_fee": { "percentage": "50" } },
        { "fulfillment_state": { "descriptor": { "code": "WITHIN_4HR" } }, "cancellation_fee": { "percentage": "100" } }
      ],
      "payments": [{ "type": "ON_ORDER", "collected_by": "BPP", "status": "NOT-PAID",
        "tags": [{ "descriptor": { "code": "PAYMENT_TERMS" }, "value": "PRE_PAYMENT_REQUIRED" }] }]
    }
  }
}
```

---

## 4. confirm / on_confirm — 2 QR Tickets + Pickup Instructions + Invoice Link

### `confirm` (BAP → BPP)

```json
{
  "context": { "domain": "mobility", "action": "confirm", "version": "2.0",
    "transaction_id": "txn-icb-3a7e9d", "message_id": "msg-007",
    "timestamp": "2026-02-03T20:02:30+05:30", "ttl": "PT30S",
    "bap_id": "redbus.bap.io", "bap_uri": "https://api.redbus.in/beckn",
    "bpp_id": "ksrtc.bpp.io", "bpp_uri": "https://api.ksrtc.in/beckn" },
  "message": {
    "order": {
      "provider": { "id": "ksrtc-karnataka" },
      "items": [{ "id": "fare-ksrtc-volvo-adult", "quantity": { "count": 2 } }],
      "fulfillments": [
        {
          "id": "journey-ksrtc-0600",
          "passengers": [
            { "id": "pax-1", "person": { "name": "Sanjay Rao" }, "contact": { "phone": "+919911223344" } },
            { "id": "pax-2", "person": { "name": "Anjali Rao" }, "contact": { "phone": "+919911223345" } }
          ]
        }
      ],
      "billing": { "name": "Sanjay Rao", "phone": "+919911223344", "email": "sanjay@example.com" },
      "payments": [{ "type": "ON_ORDER", "collected_by": "BPP", "status": "PAID",
        "transaction_id": "upi-ksrtc-icb-001",
        "tags": [{ "descriptor": { "code": "PAYMENT_REF" }, "value": "upi-ksrtc-icb-001" }] }]
    }
  }
}
```

### `on_confirm` (BPP → BAP) — 2 tickets + pickup instructions + invoice link

```json
{
  "context": { "domain": "mobility", "action": "on_confirm", "version": "2.0",
    "transaction_id": "txn-icb-3a7e9d", "message_id": "msg-008",
    "timestamp": "2026-02-03T20:02:32+05:30", "ttl": "PT30S",
    "bap_id": "redbus.bap.io", "bap_uri": "https://api.redbus.in/beckn",
    "bpp_id": "ksrtc.bpp.io", "bpp_uri": "https://api.ksrtc.in/beckn" },
  "message": {
    "order": {
      "@type": "mobility:Journey",
      "id": "booking-ksrtc-20260204-001",
      "status": "CONFIRMED",
      "provider": { "@type": "mobility:Operator", "id": "ksrtc-karnataka", "descriptor": { "name": "KSRTC Karnataka" } },
      "items": [
        { "id": "fare-ksrtc-volvo-adult", "quantity": { "count": 2 }, "price": { "value": "700", "currency": "INR" } }
      ],
      "fulfillments": [
        {
          "id": "journey-ksrtc-0600",
          "state": { "descriptor": { "code": "BOOKING_CONFIRMED", "name": "Booking confirmed. Board at Bay 7 by 5:45 AM." } },
          "stops": [
            {
              "type": "START",
              "location": { "@type": "mobility:Stop", "id": "BLR-KBS-BAY7", "descriptor": { "name": "Kempegowda Bus Terminal — Bay 7" } },
              "time": { "timestamp": "2026-02-04T06:00:00+05:30", "label": "DEPARTURE" },
              "instructions": {
                "@type": "mobility:FulfillmentStop",
                "descriptor": { "name": "Report to Bay 7 by 5:45 AM. Show QR code to conductor. Bus No: KSRTC KA-4421" }
              }
            },
            {
              "type": "END",
              "location": { "@type": "mobility:Stop", "id": "MYS-CBS-MAIN", "descriptor": { "name": "Mysuru Central Bus Stand" } },
              "time": { "timestamp": "2026-02-04T09:30:00+05:30", "label": "ARRIVAL" }
            }
          ],
          "passengers": [
            { "id": "pax-1", "person": { "name": "Sanjay Rao" },
              "tags": [{ "descriptor": { "code": "SEAT_ID" }, "value": "12A" }] },
            { "id": "pax-2", "person": { "name": "Anjali Rao" },
              "tags": [{ "descriptor": { "code": "SEAT_ID" }, "value": "12B" }] }
          ],
          "documents": [
            {
              "@type": "mobility:TravelDocument",
              "id": "doc-qr-ksrtc-pax1",
              "type": "QR_CODE",
              "url": "https://tickets.ksrtc.in/qr/tkts-ksrtc-icb-001-pax1",
              "descriptor": { "name": "Sanjay Rao — Seat 12A — KSRTC Volvo" },
              "valid_from": "2026-02-04T05:30:00+05:30",
              "valid_until": "2026-02-04T10:00:00+05:30"
            },
            {
              "@type": "mobility:TravelDocument",
              "id": "doc-qr-ksrtc-pax2",
              "type": "QR_CODE",
              "url": "https://tickets.ksrtc.in/qr/tkts-ksrtc-icb-001-pax2",
              "descriptor": { "name": "Anjali Rao — Seat 12B — KSRTC Volvo" },
              "valid_from": "2026-02-04T05:30:00+05:30",
              "valid_until": "2026-02-04T10:00:00+05:30"
            }
          ],
          "tags": [
            {
              "descriptor": { "code": "TICKET_PAX1" },
              "@type": "mobility:Ticket",
              "list": [
                { "descriptor": { "code": "TICKET_ID" }, "value": "tkts-ksrtc-icb-001-pax1" },
                { "descriptor": { "code": "PASSENGER_REF" }, "value": "pax-1" },
                { "descriptor": { "code": "SEAT_ID" }, "value": "12A" }
              ]
            },
            {
              "descriptor": { "code": "TICKET_PAX2" },
              "@type": "mobility:Ticket",
              "list": [
                { "descriptor": { "code": "TICKET_ID" }, "value": "tkts-ksrtc-icb-001-pax2" },
                { "descriptor": { "code": "PASSENGER_REF" }, "value": "pax-2" },
                { "descriptor": { "code": "SEAT_ID" }, "value": "12B" }
              ]
            },
            {
              "descriptor": { "code": "BAGGAGE_ALLOWANCE" },
              "@type": "mobility:BaggageAllowance",
              "list": [
                { "descriptor": { "code": "CHECKED_BAGGAGE_COUNT" }, "value": "1" },
                { "descriptor": { "code": "CHECKED_BAGGAGE_WEIGHT_KG" }, "value": "15" },
                { "descriptor": { "code": "APPLIES_PER" }, "value": "PASSENGER" }
              ]
            },
            { "descriptor": { "code": "INVOICE_URL" }, "value": "https://invoices.ksrtc.in/inv/booking-ksrtc-20260204-001.pdf" },
            { "descriptor": { "code": "CONTACT_PHONE" }, "value": "080-22975500",
              "tags": [{ "descriptor": { "code": "LABEL" }, "value": "KSRTC Helpline (24/7)" }] }
          ]
        }
      ],
      "quote": {
        "price": { "value": "700", "currency": "INR" },
        "breakup": [
          { "item": { "descriptor": { "code": "SEAT_12A_ADULT_KSRTC_VOLVO" } }, "price": { "value": "350", "currency": "INR" } },
          { "item": { "descriptor": { "code": "SEAT_12B_ADULT_KSRTC_VOLVO" } }, "price": { "value": "350", "currency": "INR" } }
        ]
      },
      "payments": [{ "type": "ON_ORDER", "status": "PAID", "transaction_id": "upi-ksrtc-icb-001" }]
    }
  }
}
```

---

## 5. status / on_status — Day of Travel (15-Minute Delay)

```json
{
  "context": { "domain": "mobility", "action": "status", "version": "2.0",
    "transaction_id": "txn-icb-3a7e9d", "message_id": "msg-009",
    "timestamp": "2026-02-04T05:45:00+05:30", "ttl": "PT30S",
    "bap_id": "redbus.bap.io", "bap_uri": "https://api.redbus.in/beckn",
    "bpp_id": "ksrtc.bpp.io", "bpp_uri": "https://api.ksrtc.in/beckn" },
  "message": { "order_id": "booking-ksrtc-20260204-001" }
}
```

```json
{
  "context": { "domain": "mobility", "action": "on_status", "version": "2.0",
    "transaction_id": "txn-icb-3a7e9d", "message_id": "msg-010",
    "timestamp": "2026-02-04T05:45:01+05:30", "ttl": "PT30S",
    "bap_id": "redbus.bap.io", "bap_uri": "https://api.redbus.in/beckn",
    "bpp_id": "ksrtc.bpp.io", "bpp_uri": "https://api.ksrtc.in/beckn" },
  "message": {
    "order": {
      "id": "booking-ksrtc-20260204-001",
      "fulfillments": [
        {
          "id": "journey-ksrtc-0600",
          "state": { "@type": "mobility:Event", "descriptor": { "code": "SERVICE_DELAYED", "name": "Bus delayed 15 minutes. New departure: 6:15 AM" } },
          "tags": [
            {
              "descriptor": { "code": "VEHICLE_POSITION" },
              "@type": "mobility:VehiclePosition",
              "list": [
                { "descriptor": { "code": "LATITUDE" }, "value": "12.9720" },
                { "descriptor": { "code": "LONGITUDE" }, "value": "77.5380" },
                { "descriptor": { "code": "STATUS" }, "value": "IN_DEPOT" }
              ]
            },
            {
              "descriptor": { "code": "STOP_TIME_UPDATE" },
              "@type": "mobility:StopTimeUpdate",
              "list": [
                { "descriptor": { "code": "STOP_ID" }, "value": "BLR-KBS-BAY7" },
                { "descriptor": { "code": "DEPARTURE_DELAY_SECONDS" }, "value": "900" },
                { "descriptor": { "code": "NEW_DEPARTURE_TIME" }, "value": "2026-02-04T06:15:00+05:30" }
              ]
            },
            {
              "descriptor": { "code": "DELAY_ALERT" },
              "@type": "mobility:Alert",
              "list": [
                { "descriptor": { "code": "CAUSE" }, "value": "TECHNICAL_PROBLEM" },
                { "descriptor": { "code": "EFFECT" }, "value": "MODIFIED_SERVICE" },
                { "descriptor": { "code": "DESCRIPTION_TEXT" }, "value": "Bus KSRTC KA-4421 delayed 15 minutes due to maintenance check. New departure from Bay 7: 6:15 AM." }
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

## 6. track / on_track — En Route GPS Tracking

```json
{
  "context": { "domain": "mobility", "action": "track", "version": "2.0",
    "transaction_id": "txn-icb-3a7e9d", "message_id": "msg-011",
    "timestamp": "2026-02-04T07:00:00+05:30", "ttl": "PT30S",
    "bap_id": "redbus.bap.io", "bap_uri": "https://api.redbus.in/beckn",
    "bpp_id": "ksrtc.bpp.io", "bpp_uri": "https://api.ksrtc.in/beckn" },
  "message": { "order_id": "booking-ksrtc-20260204-001" }
}
```

```json
{
  "context": { "domain": "mobility", "action": "on_track", "version": "2.0",
    "transaction_id": "txn-icb-3a7e9d", "message_id": "msg-012",
    "timestamp": "2026-02-04T07:00:01+05:30", "ttl": "PT30S",
    "bap_id": "redbus.bap.io", "bap_uri": "https://api.redbus.in/beckn",
    "bpp_id": "ksrtc.bpp.io", "bpp_uri": "https://api.ksrtc.in/beckn" },
  "message": {
    "tracking": {
      "id": "track-ksrtc-vj-0615",
      "status": "active",
      "url": "https://track.ksrtc.in/live/vj-ksrtc-0615",
      "location": {
        "@type": "mobility:VehiclePosition",
        "updated_at": "2026-02-04T06:58:30+05:30",
        "gps": "12.7200,77.2100",
        "tags": [
          { "descriptor": { "code": "SPEED_KPH" }, "value": "84" },
          { "descriptor": { "code": "BEARING_DEGREES" }, "value": "205" },
          { "descriptor": { "code": "ODOMETER_KM" }, "value": "38" }
        ]
      }
    }
  }
}
```

---

## 7. on_update — Journey Started + Tracking Activated (BPP-Initiated)

```json
{
  "context": { "domain": "mobility", "action": "on_update", "version": "2.0",
    "transaction_id": "txn-icb-3a7e9d", "message_id": "msg-013",
    "timestamp": "2026-02-04T06:17:00+05:30", "ttl": "PT30S",
    "bap_id": "redbus.bap.io", "bap_uri": "https://api.redbus.in/beckn",
    "bpp_id": "ksrtc.bpp.io", "bpp_uri": "https://api.ksrtc.in/beckn" },
  "message": {
    "order": {
      "@type": "mobility:Journey",
      "id": "booking-ksrtc-20260204-001",
      "status": "JOURNEY_IN_PROGRESS",
      "fulfillments": [
        {
          "id": "journey-ksrtc-0600",
          "state": { "@type": "mobility:Event", "descriptor": { "code": "JOURNEY_STARTED", "name": "Bus departed Bay 7 at 6:15 AM" } },
          "tracking": true,
          "tags": [
            { "descriptor": { "code": "TRACKING_ACTIVE" }, "value": "true" },
            { "descriptor": { "code": "TRACKING_URL" }, "value": "https://track.ksrtc.in/live/vj-ksrtc-0615",
              "tags": [{ "descriptor": { "code": "NOTE" }, "value": "Live GPS tracking of your KSRTC Volvo" }] },
            {
              "descriptor": { "code": "CURRENT_LOCATION" },
              "@type": "mobility:VehiclePosition",
              "list": [
                { "descriptor": { "code": "LATITUDE" }, "value": "12.9218" },
                { "descriptor": { "code": "LONGITUDE" }, "value": "77.4821" },
                { "descriptor": { "code": "SPEED_KPH" }, "value": "72" }
              ]
            },
            {
              "descriptor": { "code": "REVISED_ETA" },
              "@type": "mobility:StopTimeUpdate",
              "list": [
                { "descriptor": { "code": "STOP_ID" }, "value": "MYS-CBS-MAIN" },
                { "descriptor": { "code": "ESTIMATED_ARRIVAL" }, "value": "2026-02-04T09:45:00+05:30" },
                { "descriptor": { "code": "DELAY_MINUTES" }, "value": "15" }
              ]
            }
          ]
        }
      ],
      "updated_at": "2026-02-04T06:17:00+05:30"
    }
  }
}
```

> **Note:** Intercity bus `on_update` (after departure) carries tracking active flag + GPS URL. This is different from city bus and metro which carry nothing in `on_update`.

---

## 8. cancel / on_cancel

```json
{
  "context": { "domain": "mobility", "action": "cancel", "version": "2.0",
    "transaction_id": "txn-icb-3a7e9d", "message_id": "msg-014",
    "timestamp": "2026-02-04T04:00:00+05:30", "ttl": "PT30S",
    "bap_id": "redbus.bap.io", "bap_uri": "https://api.redbus.in/beckn",
    "bpp_id": "ksrtc.bpp.io", "bpp_uri": "https://api.ksrtc.in/beckn" },
  "message": { "order_id": "booking-ksrtc-20260204-001", "cancellation_reason_id": "002",
    "descriptor": { "short_desc": "Plans changed" } }
}
```

```json
{
  "context": { "domain": "mobility", "action": "on_cancel", "version": "2.0",
    "transaction_id": "txn-icb-3a7e9d", "message_id": "msg-015",
    "timestamp": "2026-02-04T04:00:02+05:30", "ttl": "PT30S",
    "bap_id": "redbus.bap.io", "bap_uri": "https://api.redbus.in/beckn",
    "bpp_id": "ksrtc.bpp.io", "bpp_uri": "https://api.ksrtc.in/beckn" },
  "message": {
    "order": {
      "@type": "mobility:Journey",
      "id": "booking-ksrtc-20260204-001",
      "status": "CANCELLED",
      "quote": {
        "price": { "value": "350", "currency": "INR" },
        "breakup": [
          { "item": { "descriptor": { "code": "CANCELLATION_FEE_50_PERCENT" } }, "price": { "value": "350", "currency": "INR" } },
          { "item": { "descriptor": { "code": "REFUND" } }, "price": { "value": "350", "currency": "INR" },
            "tags": [{ "descriptor": { "code": "NOTE" }, "value": "Cancelled 2 hours before departure — 50% refund" }] }
        ]
      },
      "fulfillments": [
        {
          "id": "journey-ksrtc-0600",
          "documents": [
            { "@type": "mobility:Ticket", "id": "tkts-ksrtc-icb-001-pax1", "tags": [{ "descriptor": { "code": "STATUS" }, "value": "INVALIDATED" }] },
            { "@type": "mobility:Ticket", "id": "tkts-ksrtc-icb-001-pax2", "tags": [{ "descriptor": { "code": "STATUS" }, "value": "INVALIDATED" }] }
          ]
        }
      ]
    }
  }
}
```

---

## 9. rating / on_rating — Seat Dispute

```json
{
  "context": { "domain": "mobility", "action": "rating", "version": "2.0",
    "transaction_id": "txn-icb-3a7e9d", "message_id": "msg-016",
    "timestamp": "2026-02-04T10:30:00+05:30", "ttl": "PT30S",
    "bap_id": "redbus.bap.io", "bap_uri": "https://api.redbus.in/beckn",
    "bpp_id": "ksrtc.bpp.io", "bpp_uri": "https://api.ksrtc.in/beckn" },
  "message": {
    "ratings": [
      { "@type": "mobility:Rating", "id": "rat-icb-01", "rating_category": "Service", "value": "3" },
      { "@type": "mobility:Rating", "id": "rat-icb-02", "rating_category": "Vehicle", "value": "4" }
    ],
    "feedback_form": {
      "@type": "mobility:Review",
      "responses": [{ "question": { "code": "REVIEW_TEXT" }, "answer": "Seat 12A was occupied by another passenger. Had to sit elsewhere for 3.5 hours." }]
    },
    "tags": [{ "descriptor": { "code": "FEEDBACK_TAGS" }, "value": "SEAT_ISSUE,DELAY,CLEAN_BUS" }]
  }
}
```

---

## 10. support / on_support — Seat Dispute + Travel Voucher Resolution

```json
{
  "context": { "domain": "mobility", "action": "support", "version": "2.0",
    "transaction_id": "txn-icb-3a7e9d", "message_id": "msg-017",
    "timestamp": "2026-02-04T10:45:00+05:30", "ttl": "PT30S",
    "bap_id": "redbus.bap.io", "bap_uri": "https://api.redbus.in/beckn",
    "bpp_id": "ksrtc.bpp.io", "bpp_uri": "https://api.ksrtc.in/beckn" },
  "message": {
    "support": {
      "@type": "mobility:SupportCase",
      "order_id": "booking-ksrtc-20260204-001",
      "type": "COMPLAINT",
      "descriptor": { "short_desc": "Reserved seat 12A was occupied by another passenger for the entire journey" },
      "tags": [{ "descriptor": { "code": "PRIORITY" }, "value": "HIGH" }]
    }
  }
}
```

```json
{
  "context": { "domain": "mobility", "action": "on_support", "version": "2.0",
    "transaction_id": "txn-icb-3a7e9d", "message_id": "msg-018",
    "timestamp": "2026-02-04T10:45:02+05:30", "ttl": "PT30S",
    "bap_id": "redbus.bap.io", "bap_uri": "https://api.redbus.in/beckn",
    "bpp_id": "ksrtc.bpp.io", "bpp_uri": "https://api.ksrtc.in/beckn" },
  "message": {
    "support": {
      "@type": "mobility:SupportCase",
      "order_id": "booking-ksrtc-20260204-001",
      "ref_id": "case-ksrtc-seat-2291",
      "descriptor": { "short_desc": "Seat complaint acknowledged. KSRTC reviewing complaint. Travel voucher issued as goodwill." },
      "phone": "080-22975500",
      "email": "grievance@ksrtc.in",
      "url": "https://support.ksrtc.in/case/case-ksrtc-seat-2291",
      "tags": [
        { "descriptor": { "code": "RECEIPT_URL" }, "value": "https://invoices.ksrtc.in/inv/booking-ksrtc-20260204-001.pdf" },
        {
          "descriptor": { "code": "TRAVEL_VOUCHER" },
          "@type": "mobility:Entitlement",
          "list": [
            { "descriptor": { "code": "ENTITLEMENT_TYPE" }, "value": "TRAVEL_VOUCHER" },
            { "descriptor": { "code": "VOUCHER_VALUE_INR" }, "value": "175" },
            { "descriptor": { "code": "VALID_UNTIL" }, "value": "2026-08-03T23:59:59+05:30" },
            { "descriptor": { "code": "APPLICABLE_FOR" }, "value": "Any future KSRTC intercity booking" }
          ]
        }
      ]
    }
  }
}
```
