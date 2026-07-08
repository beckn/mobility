# Metro Ticket Booking — End-to-End Implementation Guide

## Overview

This guide provides complete Beckn protocol v2.0 JSON payloads for a metro ticket transaction.

**Scenario:** Kavya purchases a ₹45 Adult QR ticket on Kochi Metro's Purple Line from MG Road to Whitefield. She receives the QR code + metro live updates link at `on_confirm`. A signal fault delay is pushed via `on_update` (alerts only — no contract change).

**Key differentiators from bus transit:**
- Search uses `StopPlace` (complex station) not `Stop`
- `on_confirm` includes `Quay`, `Level`, `Pathway` (station wayfinding) + **metro live updates link**
- `on_update` sends delay alerts only — NO contract modifications
- Fare is zone-based: `TariffZone` + `FareLegRule`

---

## Context Values

| Field | Value |
|-------|-------|
| `domain` | `mobility` |
| `bap_id` | `metro-app.bap.io` |
| `bpp_id` | `kmrl.bpp.io` |
| `transaction_id` | `txn-metro-8e1f4b` |

---

## 1. search / on_search — Discovery

### `search` (BAP → BPP) — station-to-station, NOT GPS

```json
{
  "context": {
    "domain": "mobility", "action": "search", "version": "2.0",
    "transaction_id": "txn-metro-8e1f4b", "message_id": "msg-001",
    "timestamp": "2026-02-03T09:00:00+05:30", "ttl": "PT30S",
    "bap_id": "metro-app.bap.io", "bap_uri": "https://api.metro-app.io/beckn",
    "location": { "city": { "name": "Kochi" }, "country": { "code": "IND" } }
  },
  "message": {
    "intent": {
      "@type": "mobility:TripRequest",
      "fulfillment": {
        "stops": [
          {
            "type": "START",
            "location": {
              "@type": "mobility:StopPlace",
              "id": "KMRL-SP-MGROAD",
              "descriptor": { "name": "MG Road Metro Station" },
              "stop_place_type": "METRO_STATION"
            }
          },
          {
            "type": "END",
            "location": {
              "@type": "mobility:StopPlace",
              "id": "KMRL-SP-WHITEFIELD",
              "descriptor": { "name": "Whitefield Metro Station" },
              "stop_place_type": "METRO_STATION"
            }
          }
        ],
        "time": { "timestamp": "2026-02-03T09:00:00+05:30", "label": "DEPARTURE" }
      },
      "tags": [
        { "descriptor": { "code": "RIDER_CATEGORY" }, "value": "ADULT" },
        { "descriptor": { "code": "MODES" }, "value": "METRO" }
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
    "transaction_id": "txn-metro-8e1f4b", "message_id": "msg-002",
    "timestamp": "2026-02-03T09:00:01+05:30", "ttl": "PT30S",
    "bap_id": "metro-app.bap.io", "bap_uri": "https://api.metro-app.io/beckn",
    "bpp_id": "kmrl.bpp.io", "bpp_uri": "https://api.kmrl.in/beckn"
  },
  "message": {
    "catalog": {
      "providers": [
        {
          "@type": "mobility:Operator",
          "id": "kmrl",
          "descriptor": { "name": "Kochi Metro Rail Limited" },
          "items": [
            {
              "@type": "mobility:FareProduct",
              "id": "fare-kmrl-adult-single",
              "descriptor": { "name": "Adult Single Trip — Purple Line" },
              "price": { "value": "45", "currency": "INR" },
              "tags": [
                { "descriptor": { "code": "RIDER_CATEGORY_ID" }, "value": "ADULT" },
                { "descriptor": { "code": "DURATION_TYPE" }, "value": "SINGLE_TRIP" },
                { "descriptor": { "code": "FARE_COMPUTATION" }, "value": "ZONE_BASED" },
                {
                  "descriptor": { "code": "TARIFF_ZONES" },
                  "@type": "mobility:TariffZone",
                  "list": [
                    { "descriptor": { "code": "ORIGIN_ZONE" }, "value": "ZONE_2" },
                    { "descriptor": { "code": "DESTINATION_ZONE" }, "value": "ZONE_4" }
                  ]
                }
              ]
            }
          ],
          "fulfillments": [
            {
              "@type": "mobility:Itinerary",
              "id": "itin-kmrl-purple-direct",
              "descriptor": { "name": "Purple Line Direct — MG Road to Whitefield", "short_desc": "32 min, 0 transfers" },
              "legs": [
                {
                  "@type": "mobility:Leg",
                  "id": "leg-purple-01",
                  "mode": "METRO",
                  "route": {
                    "@type": "mobility:Route",
                    "id": "KMRL-RT-PURPLE",
                    "descriptor": { "name": "Purple Line", "short_name": "PL" },
                    "line": {
                      "@type": "mobility:Line",
                      "id": "KMRL-LINE-PURPLE",
                      "descriptor": { "name": "Kochi Metro Purple Line" }
                    }
                  },
                  "vehicle_journey": {
                    "@type": "mobility:VehicleJourney",
                    "id": "vj-purple-0915",
                    "departure": "2026-02-03T09:15:00+05:30",
                    "arrival": "2026-02-03T09:47:00+05:30"
                  },
                  "origin": {
                    "@type": "mobility:StopPlace",
                    "id": "KMRL-SP-MGROAD",
                    "descriptor": { "name": "MG Road" }
                  },
                  "destination": {
                    "@type": "mobility:StopPlace",
                    "id": "KMRL-SP-WHITEFIELD",
                    "descriptor": { "name": "Whitefield" }
                  }
                }
              ],
              "fare": {
                "@type": "mobility:Fare",
                "id": "fare-45-kmrl",
                "amount": "45",
                "currency": "INR",
                "fare_rules": [
                  {
                    "@type": "mobility:FareLegRule",
                    "fare_product_id": "fare-kmrl-adult-single",
                    "from_area_id": "ZONE_2",
                    "to_area_id": "ZONE_4"
                  }
                ]
              },
              "transfer_rule": null
            }
          ],
          "tags": [
            {
              "descriptor": { "code": "FARE_TRANSFER_RULE" },
              "@type": "mobility:FareTransferRule",
              "list": [
                { "descriptor": { "code": "DESCRIPTION" }, "value": "Free transfer between Purple and Blue line within 30 min" },
                { "descriptor": { "code": "DURATION_LIMIT_MINUTES" }, "value": "30" }
              ]
            },
            {
              "descriptor": { "code": "CANCELLATION_POLICY" },
              "@type": "mobility:CancellationPolicy",
              "list": [{ "descriptor": { "code": "CANCELLATION_TERMS" }, "value": "Non-refundable once QR scanned at fare gate" }]
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
    "transaction_id": "txn-metro-8e1f4b", "message_id": "msg-003",
    "timestamp": "2026-02-03T09:01:00+05:30", "ttl": "PT30S",
    "bap_id": "metro-app.bap.io", "bap_uri": "https://api.metro-app.io/beckn",
    "bpp_id": "kmrl.bpp.io", "bpp_uri": "https://api.kmrl.in/beckn" },
  "message": {
    "order": {
      "provider": { "id": "kmrl" },
      "items": [{ "id": "fare-kmrl-adult-single", "quantity": { "count": 1 } }],
      "fulfillments": [
        {
          "id": "itin-kmrl-purple-direct",
          "stops": [
            { "type": "START", "location": { "@type": "mobility:StopPlace", "id": "KMRL-SP-MGROAD" } },
            { "type": "END", "location": { "@type": "mobility:StopPlace", "id": "KMRL-SP-WHITEFIELD" } }
          ],
          "tags": [
            { "descriptor": { "code": "VEHICLE_JOURNEY_ID" }, "value": "vj-purple-0915" },
            { "descriptor": { "code": "FARE_MEDIUM" }, "value": "QR_CODE" }
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
    "transaction_id": "txn-metro-8e1f4b", "message_id": "msg-004",
    "timestamp": "2026-02-03T09:01:01+05:30", "ttl": "PT30S",
    "bap_id": "metro-app.bap.io", "bap_uri": "https://api.metro-app.io/beckn",
    "bpp_id": "kmrl.bpp.io", "bpp_uri": "https://api.kmrl.in/beckn" },
  "message": {
    "order": {
      "items": [{ "id": "fare-kmrl-adult-single", "price": { "value": "45", "currency": "INR" } }],
      "fulfillments": [
        {
          "id": "itin-kmrl-purple-direct",
          "tags": [
            {
              "descriptor": { "code": "BOARDING_PLATFORM" },
              "@type": "mobility:Quay",
              "list": [
                { "descriptor": { "code": "QUAY_ID" }, "value": "KMRL-QUAY-MGROAD-P2" },
                { "descriptor": { "code": "PUBLIC_CODE" }, "value": "Platform 2" },
                { "descriptor": { "code": "QUAY_TYPE" }, "value": "METRO_PLATFORM" }
              ]
            },
            {
              "descriptor": { "code": "FARE_GATE_ZONE" },
              "@type": "mobility:StopArea",
              "list": [
                { "descriptor": { "code": "AREA_ID" }, "value": "KMRL-FAREGATE-MGROAD" },
                { "descriptor": { "code": "AREA_NAME" }, "value": "MG Road Fare Gate" }
              ]
            }
          ]
        }
      ],
      "quote": {
        "price": { "value": "45", "currency": "INR" },
        "breakup": [{ "item": { "descriptor": { "code": "ADULT_SINGLE_TRIP_ZONE2_TO_ZONE4" } }, "price": { "value": "45", "currency": "INR" } }]
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
    "transaction_id": "txn-metro-8e1f4b", "message_id": "msg-005",
    "timestamp": "2026-02-03T09:01:20+05:30", "ttl": "PT30S",
    "bap_id": "metro-app.bap.io", "bap_uri": "https://api.metro-app.io/beckn",
    "bpp_id": "kmrl.bpp.io", "bpp_uri": "https://api.kmrl.in/beckn" },
  "message": {
    "order": {
      "provider": { "id": "kmrl" },
      "items": [{ "id": "fare-kmrl-adult-single", "quantity": { "count": 1 } }],
      "fulfillments": [
        {
          "id": "itin-kmrl-purple-direct",
          "customer": {
            "@type": "mobility:Passenger",
            "person": { "name": "Kavya Nair" },
            "contact": { "phone": "+919745123456", "email": "kavya@example.com" }
          },
          "tags": [
            { "descriptor": { "code": "FARE_MEDIUM" }, "value": "QR_CODE" }
          ]
        }
      ],
      "billing": { "name": "Kavya Nair", "phone": "+919745123456", "email": "kavya@example.com" }
    }
  }
}
```

### `on_init` (BPP → BAP)

```json
{
  "context": { "domain": "mobility", "action": "on_init", "version": "2.0",
    "transaction_id": "txn-metro-8e1f4b", "message_id": "msg-006",
    "timestamp": "2026-02-03T09:01:21+05:30", "ttl": "PT30S",
    "bap_id": "metro-app.bap.io", "bap_uri": "https://api.metro-app.io/beckn",
    "bpp_id": "kmrl.bpp.io", "bpp_uri": "https://api.kmrl.in/beckn" },
  "message": {
    "order": {
      "items": [{ "id": "fare-kmrl-adult-single", "price": { "value": "45", "currency": "INR" } }],
      "quote": { "price": { "value": "45", "currency": "INR" } },
      "cancellation_terms": [
        { "cancellation_fee": { "percentage": "100" },
          "tags": [{ "descriptor": { "code": "NOTE" }, "value": "Non-refundable once QR is scanned at fare gate" }] }
      ],
      "payments": [{ "type": "ON_ORDER", "collected_by": "BPP", "status": "NOT-PAID",
        "tags": [{ "descriptor": { "code": "PAYMENT_TERMS" }, "value": "PRE_PAYMENT_REQUIRED" }] }]
    }
  }
}
```

---

## 4. confirm / on_confirm — QR Ticket + Station Wayfinding + Live Updates Link

### `confirm` (BAP → BPP)

```json
{
  "context": { "domain": "mobility", "action": "confirm", "version": "2.0",
    "transaction_id": "txn-metro-8e1f4b", "message_id": "msg-007",
    "timestamp": "2026-02-03T09:01:45+05:30", "ttl": "PT30S",
    "bap_id": "metro-app.bap.io", "bap_uri": "https://api.metro-app.io/beckn",
    "bpp_id": "kmrl.bpp.io", "bpp_uri": "https://api.kmrl.in/beckn" },
  "message": {
    "order": {
      "provider": { "id": "kmrl" },
      "items": [{ "id": "fare-kmrl-adult-single", "quantity": { "count": 1 } }],
      "fulfillments": [
        {
          "id": "itin-kmrl-purple-direct",
          "customer": { "person": { "name": "Kavya Nair" }, "contact": { "phone": "+919745123456" } }
        }
      ],
      "billing": { "name": "Kavya Nair", "phone": "+919745123456" },
      "payments": [{ "type": "ON_ORDER", "status": "PAID", "transaction_id": "upi-kmrl-001",
        "tags": [{ "descriptor": { "code": "PAYMENT_REF" }, "value": "upi-kmrl-001" }] }]
    }
  }
}
```

### `on_confirm` (BPP → BAP) — QR ticket + Quay + Level + Pathway + LIVE UPDATES LINK

```json
{
  "context": { "domain": "mobility", "action": "on_confirm", "version": "2.0",
    "transaction_id": "txn-metro-8e1f4b", "message_id": "msg-008",
    "timestamp": "2026-02-03T09:01:47+05:30", "ttl": "PT30S",
    "bap_id": "metro-app.bap.io", "bap_uri": "https://api.metro-app.io/beckn",
    "bpp_id": "kmrl.bpp.io", "bpp_uri": "https://api.kmrl.in/beckn" },
  "message": {
    "order": {
      "@type": "mobility:Itinerary",
      "id": "booking-kmrl-20260203-001",
      "status": "CONFIRMED",
      "provider": { "@type": "mobility:Operator", "id": "kmrl", "descriptor": { "name": "Kochi Metro" } },
      "items": [
        {
          "@type": "mobility:FareProduct",
          "id": "fare-kmrl-adult-single",
          "descriptor": { "name": "Adult Single — MG Road → Whitefield" },
          "price": { "value": "45", "currency": "INR" },
          "tags": [
            { "descriptor": { "code": "VALID_FROM" }, "value": "2026-02-03T09:01:47+05:30" },
            { "descriptor": { "code": "VALID_UNTIL" }, "value": "2026-02-03T11:01:47+05:30" }
          ]
        }
      ],
      "fulfillments": [
        {
          "id": "itin-kmrl-purple-direct",
          "state": { "descriptor": { "code": "TICKET_ISSUED", "name": "Tap QR at fare gate to enter" } },
          "stops": [
            {
              "type": "START",
              "location": { "@type": "mobility:StopPlace", "id": "KMRL-SP-MGROAD", "descriptor": { "name": "MG Road Metro" } },
              "time": { "timestamp": "2026-02-03T09:15:00+05:30", "label": "DEPARTURE" }
            },
            {
              "type": "END",
              "location": { "@type": "mobility:StopPlace", "id": "KMRL-SP-WHITEFIELD", "descriptor": { "name": "Whitefield" } }
            }
          ],
          "documents": [
            {
              "@type": "mobility:TravelDocument",
              "id": "doc-qr-kmrl-001",
              "type": "QR_CODE",
              "url": "https://tickets.kmrl.in/qr/tkts-kmrl-20260203-001",
              "descriptor": { "name": "Kochi Metro QR Ticket" },
              "valid_from": "2026-02-03T09:01:47+05:30",
              "valid_until": "2026-02-03T11:01:47+05:30"
            },
            {
              "descriptor": { "code": "KIOSK_PRINT_INSTRUCTIONS", "name": "No smartphone? Use kiosk at MG Road station entrance. Booking ID: KMRL-20260203-001" }
            }
          ],
          "tags": [
            {
              "descriptor": { "code": "TICKET" },
              "@type": "mobility:Ticket",
              "list": [
                { "descriptor": { "code": "TICKET_ID" }, "value": "tkts-kmrl-20260203-001" },
                { "descriptor": { "code": "TICKET_TYPE" }, "value": "SINGLE" }
              ]
            },
            {
              "descriptor": { "code": "BOARDING_PLATFORM" },
              "@type": "mobility:Quay",
              "list": [
                { "descriptor": { "code": "QUAY_ID" }, "value": "KMRL-QUAY-MGROAD-P2" },
                { "descriptor": { "code": "PUBLIC_CODE" }, "value": "Platform 2" },
                { "descriptor": { "code": "DIRECTION" }, "value": "Towards Whitefield" }
              ]
            },
            {
              "descriptor": { "code": "PLATFORM_LEVEL" },
              "@type": "mobility:Level",
              "list": [
                { "descriptor": { "code": "LEVEL_NAME" }, "value": "Platform Level (Level 2)" },
                { "descriptor": { "code": "ELEVATION_METRES" }, "value": "8" }
              ]
            },
            {
              "descriptor": { "code": "ROUTE_TO_PLATFORM" },
              "@type": "mobility:Pathway",
              "list": [
                { "descriptor": { "code": "PATHWAY_MODE" }, "value": "4 (ESCALATOR)" },
                { "descriptor": { "code": "FROM" }, "value": "Main entrance fare gate" },
                { "descriptor": { "code": "TO" }, "value": "Platform 2" },
                { "descriptor": { "code": "TRAVERSAL_TIME_SECONDS" }, "value": "90" }
              ]
            },
            { "descriptor": { "code": "INVOICE_URL" }, "value": "https://invoices.kmrl.in/inv/booking-kmrl-20260203-001.pdf" },
            {
              "descriptor": { "code": "METRO_LIVE_UPDATES_URL" },
              "value": "https://live.kmrl.in/departures?station=MG_ROAD&line=PURPLE",
              "tags": [{ "descriptor": { "code": "NOTE" }, "value": "Tap to see real-time Purple Line departures at MG Road" }]
            }
          ]
        }
      ],
      "quote": { "price": { "value": "45", "currency": "INR" } },
      "payments": [{ "type": "ON_ORDER", "status": "PAID", "transaction_id": "upi-kmrl-001" }]
    }
  }
}
```

---

## 5. status / on_status — Train ETA at Platform 2

```json
{
  "context": { "domain": "mobility", "action": "status", "version": "2.0",
    "transaction_id": "txn-metro-8e1f4b", "message_id": "msg-009",
    "timestamp": "2026-02-03T09:10:00+05:30", "ttl": "PT30S",
    "bap_id": "metro-app.bap.io", "bap_uri": "https://api.metro-app.io/beckn",
    "bpp_id": "kmrl.bpp.io", "bpp_uri": "https://api.kmrl.in/beckn" },
  "message": { "order_id": "booking-kmrl-20260203-001" }
}
```

```json
{
  "context": { "domain": "mobility", "action": "on_status", "version": "2.0",
    "transaction_id": "txn-metro-8e1f4b", "message_id": "msg-010",
    "timestamp": "2026-02-03T09:10:01+05:30", "ttl": "PT30S",
    "bap_id": "metro-app.bap.io", "bap_uri": "https://api.metro-app.io/beckn",
    "bpp_id": "kmrl.bpp.io", "bpp_uri": "https://api.kmrl.in/beckn" },
  "message": {
    "order": {
      "id": "booking-kmrl-20260203-001",
      "fulfillments": [
        {
          "id": "itin-kmrl-purple-direct",
          "tags": [
            {
              "descriptor": { "code": "NEXT_DEPARTURE" },
              "@type": "mobility:EstimatedTimetableDelivery",
              "list": [
                { "descriptor": { "code": "VEHICLE_JOURNEY_ID" }, "value": "vj-purple-0915" },
                { "descriptor": { "code": "DEPARTURE_TIME" }, "value": "2026-02-03T09:15:00+05:30" },
                { "descriptor": { "code": "PLATFORM" }, "value": "Platform 2" }
              ]
            },
            {
              "descriptor": { "code": "STOP_TIME_UPDATE" },
              "@type": "mobility:StopTimeUpdate",
              "list": [
                { "descriptor": { "code": "STOP_ID" }, "value": "KMRL-SP-MGROAD" },
                { "descriptor": { "code": "ARRIVAL_DELAY_SECONDS" }, "value": "0" },
                { "descriptor": { "code": "STATUS" }, "value": "ON_TIME" }
              ]
            },
            {
              "descriptor": { "code": "OCCUPANCY" },
              "@type": "mobility:OccupancyStatus",
              "list": [{ "descriptor": { "code": "OCCUPANCY_LEVEL" }, "value": "FEW_SEATS_AVAILABLE" }]
            }
          ]
        }
      ]
    }
  }
}
```

---

## 6. track / on_track — Purple Line Live Map

```json
{
  "context": { "domain": "mobility", "action": "track", "version": "2.0",
    "transaction_id": "txn-metro-8e1f4b", "message_id": "msg-011",
    "timestamp": "2026-02-03T09:13:00+05:30", "ttl": "PT30S",
    "bap_id": "metro-app.bap.io", "bap_uri": "https://api.metro-app.io/beckn",
    "bpp_id": "kmrl.bpp.io", "bpp_uri": "https://api.kmrl.in/beckn" },
  "message": { "order_id": "booking-kmrl-20260203-001" }
}
```

```json
{
  "context": { "domain": "mobility", "action": "on_track", "version": "2.0",
    "transaction_id": "txn-metro-8e1f4b", "message_id": "msg-012",
    "timestamp": "2026-02-03T09:13:01+05:30", "ttl": "PT30S",
    "bap_id": "metro-app.bap.io", "bap_uri": "https://api.metro-app.io/beckn",
    "bpp_id": "kmrl.bpp.io", "bpp_uri": "https://api.kmrl.in/beckn" },
  "message": {
    "tracking": {
      "id": "track-purple-vj-0915",
      "status": "active",
      "url": "https://live.kmrl.in/track/vj-purple-0915",
      "location": {
        "@type": "mobility:VehiclePosition",
        "updated_at": "2026-02-03T09:12:58+05:30",
        "gps": "9.9882,76.3028",
        "tags": [
          { "descriptor": { "code": "CURRENT_STOP_SEQUENCE" }, "value": "3" },
          { "descriptor": { "code": "CURRENT_STATUS" }, "value": "IN_TRANSIT_TO" },
          { "descriptor": { "code": "NEXT_STOP" }, "value": "MG Road" }
        ]
      }
    }
  }
}
```

---

## 7. update / on_update — Signal Fault Delay (ALERTS ONLY — no contract changes)

```json
{
  "context": { "domain": "mobility", "action": "on_update", "version": "2.0",
    "transaction_id": "txn-metro-8e1f4b", "message_id": "msg-013",
    "timestamp": "2026-02-03T09:20:00+05:30", "ttl": "PT30S",
    "bap_id": "metro-app.bap.io", "bap_uri": "https://api.metro-app.io/beckn",
    "bpp_id": "kmrl.bpp.io", "bpp_uri": "https://api.kmrl.in/beckn" },
  "message": {
    "order": {
      "id": "booking-kmrl-20260203-001",
      "fulfillments": [
        {
          "id": "itin-kmrl-purple-direct",
          "tags": [
            {
              "descriptor": { "code": "SERVICE_ALERT" },
              "@type": "mobility:Alert",
              "list": [
                { "descriptor": { "code": "CAUSE" }, "value": "TECHNICAL_PROBLEM" },
                { "descriptor": { "code": "EFFECT" }, "value": "SIGNIFICANT_DELAYS" },
                { "descriptor": { "code": "HEADER_TEXT" }, "value": "Signal fault — all Purple Line trains delayed 8 minutes" }
              ]
            },
            {
              "descriptor": { "code": "ENTITY_SELECTOR" },
              "@type": "mobility:EntitySelector",
              "list": [
                { "descriptor": { "code": "ROUTE_ID" }, "value": "KMRL-RT-PURPLE" },
                { "descriptor": { "code": "STOP_ID" }, "value": "KMRL-SP-MGROAD" }
              ]
            },
            {
              "descriptor": { "code": "GENERAL_MESSAGE" },
              "@type": "mobility:GeneralMessageDelivery",
              "list": [
                { "descriptor": { "code": "MESSAGE_TEXT" }, "value": "All Purple Line services delayed by approximately 8 minutes. We apologise for the inconvenience." },
                { "descriptor": { "code": "CHANNEL" }, "value": "APP" }
              ]
            },
            {
              "descriptor": { "code": "REVISED_STOP_TIME" },
              "@type": "mobility:StopTimeUpdate",
              "list": [
                { "descriptor": { "code": "STOP_ID" }, "value": "KMRL-SP-MGROAD" },
                { "descriptor": { "code": "ARRIVAL_DELAY_SECONDS" }, "value": "480" },
                { "descriptor": { "code": "NEW_DEPARTURE" }, "value": "2026-02-03T09:23:00+05:30" }
              ]
            }
          ]
        }
      ]
    }
  }
}
```

> **Note:** Metro `on_update` carries ONLY alerts and revised times — no changes to `quote`, `items`, or `fulfillments`. The ₹45 ticket remains valid.

---

## 8. cancel / on_cancel — Delay-Caused Cancellation (Full Refund)

```json
{
  "context": { "domain": "mobility", "action": "cancel", "version": "2.0",
    "transaction_id": "txn-metro-8e1f4b", "message_id": "msg-014",
    "timestamp": "2026-02-03T09:16:00+05:30", "ttl": "PT30S",
    "bap_id": "metro-app.bap.io", "bap_uri": "https://api.metro-app.io/beckn",
    "bpp_id": "kmrl.bpp.io", "bpp_uri": "https://api.kmrl.in/beckn" },
  "message": { "order_id": "booking-kmrl-20260203-001", "cancellation_reason_id": "DELAY",
    "descriptor": { "short_desc": "Cancelling due to 8-minute signal fault delay" } }
}
```

```json
{
  "context": { "domain": "mobility", "action": "on_cancel", "version": "2.0",
    "transaction_id": "txn-metro-8e1f4b", "message_id": "msg-015",
    "timestamp": "2026-02-03T09:16:02+05:30", "ttl": "PT30S",
    "bap_id": "metro-app.bap.io", "bap_uri": "https://api.metro-app.io/beckn",
    "bpp_id": "kmrl.bpp.io", "bpp_uri": "https://api.kmrl.in/beckn" },
  "message": {
    "order": {
      "id": "booking-kmrl-20260203-001", "status": "CANCELLED",
      "fulfillments": [
        {
          "id": "itin-kmrl-purple-direct",
          "state": { "descriptor": { "code": "CANCELLED" } },
          "documents": [
            { "@type": "mobility:Ticket", "id": "tkts-kmrl-20260203-001",
              "tags": [{ "descriptor": { "code": "STATUS" }, "value": "INVALIDATED" }] }
          ]
        }
      ],
      "quote": { "price": { "value": "45", "currency": "INR" }, "breakup": [
        { "item": { "descriptor": { "code": "FULL_REFUND_DELAY_CAUSED" } }, "price": { "value": "45", "currency": "INR" } }
      ]},
      "payments": [{ "type": "ON_CANCEL", "status": "REFUNDED", "amount": { "value": "45", "currency": "INR" } }]
    }
  }
}
```

---

## 9. rating / on_rating

```json
{
  "context": { "domain": "mobility", "action": "rating", "version": "2.0",
    "transaction_id": "txn-metro-8e1f4b", "message_id": "msg-016",
    "timestamp": "2026-02-03T10:15:00+05:30", "ttl": "PT30S",
    "bap_id": "metro-app.bap.io", "bap_uri": "https://api.metro-app.io/beckn",
    "bpp_id": "kmrl.bpp.io", "bpp_uri": "https://api.kmrl.in/beckn" },
  "message": {
    "ratings": [
      { "@type": "mobility:Rating", "id": "rat-metro-01", "rating_category": "Service", "value": "4",
        "tags": [{ "descriptor": { "code": "ORDER_ID" }, "value": "booking-kmrl-20260203-001" }] }
    ],
    "feedback_form": {
      "@type": "mobility:Review",
      "responses": [{ "question": { "code": "REVIEW_TEXT" }, "answer": "Clean stations but the signal delay was frustrating." }]
    },
    "tags": [{ "descriptor": { "code": "FEEDBACK_TAGS" }, "value": "CLEAN_STATION,PUNCTUALITY_ISSUE" }]
  }
}
```

---

## 10. support / on_support — Fare Gate Double Charge

```json
{
  "context": { "domain": "mobility", "action": "support", "version": "2.0",
    "transaction_id": "txn-metro-8e1f4b", "message_id": "msg-017",
    "timestamp": "2026-02-03T10:30:00+05:30", "ttl": "PT30S",
    "bap_id": "metro-app.bap.io", "bap_uri": "https://api.metro-app.io/beckn",
    "bpp_id": "kmrl.bpp.io", "bpp_uri": "https://api.kmrl.in/beckn" },
  "message": {
    "support": {
      "@type": "mobility:SupportCase",
      "order_id": "booking-kmrl-20260203-001",
      "type": "COMPLAINT",
      "descriptor": { "short_desc": "Exit gate at Whitefield didn't scan QR — was charged ₹45 again at manual counter" }
    }
  }
}
```

```json
{
  "context": { "domain": "mobility", "action": "on_support", "version": "2.0",
    "transaction_id": "txn-metro-8e1f4b", "message_id": "msg-018",
    "timestamp": "2026-02-03T10:30:02+05:30", "ttl": "PT30S",
    "bap_id": "metro-app.bap.io", "bap_uri": "https://api.metro-app.io/beckn",
    "bpp_id": "kmrl.bpp.io", "bpp_uri": "https://api.kmrl.in/beckn" },
  "message": {
    "support": {
      "@type": "mobility:SupportCase",
      "order_id": "booking-kmrl-20260203-001",
      "ref_id": "case-kmrl-faregate-774",
      "descriptor": { "short_desc": "Fare gate complaint raised. Station CCTV review initiated." },
      "phone": "0484-2974901",
      "email": "customercare@kmrl.in",
      "url": "https://support.kmrl.in/case/case-kmrl-faregate-774",
      "tags": [
        { "descriptor": { "code": "RECEIPT_URL" }, "value": "https://invoices.kmrl.in/inv/booking-kmrl-20260203-001.pdf" },
        { "descriptor": { "code": "CONTACT_HANDLE" },
          "@type": "mobility:ContactHandle",
          "list": [
            { "descriptor": { "code": "HANDLE_TYPE" }, "value": "PHONE" },
            { "descriptor": { "code": "HANDLE" }, "value": "0484-2974901" },
            { "descriptor": { "code": "LABEL" }, "value": "Kochi Metro Helpdesk (24/7)" }
          ]
        }
      ]
    }
  }
}
```
