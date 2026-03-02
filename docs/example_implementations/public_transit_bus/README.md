# Public Transit (Bus) — End-to-End Implementation Guide

## Overview

This guide provides complete Beckn protocol v2.0 JSON payloads for a public bus transit transaction, from stop-to-stop search through support.

**Scenario:** Ravi searches for BMTC buses from Silk Board stop to Majestic Bus Stand. He selects the direct Route 500C, pays ₹32 for an Adult single-trip QR ticket, boards the bus, and rates the service.

**Key differentiators from ride hailing:**
- Search is **stop-to-stop** (not GPS)
- No `on_update` for bus — only informational alerts
- `on_confirm` issues ticket as a **Verifiable Credential** (QR code) + invoice link

---

## Context Values

| Field | Value |
|-------|-------|
| `domain` | `mobility` |
| `bap_id` | `transit-app.bap.io` |
| `bpp_id` | `bmtc.bpp.io` |
| `transaction_id` | `txn-bus-4d9c2f` |

---

## 1. search / on_search — Discovery

### `search` (BAP → BPP)

```json
{
  "context": {
    "domain": "mobility", "action": "search", "version": "2.0",
    "transaction_id": "txn-bus-4d9c2f", "message_id": "msg-001",
    "timestamp": "2026-02-03T08:00:00+05:30", "ttl": "PT30S",
    "bap_id": "transit-app.bap.io", "bap_uri": "https://api.transit-app.io/beckn",
    "location": { "city": { "name": "Bengaluru" }, "country": { "code": "IND" } }
  },
  "message": {
    "intent": {
      "@type": "mobility:TripRequest",
      "fulfillment": {
        "stops": [
          {
            "type": "START",
            "location": {
              "@type": "mobility:Stop",
              "id": "BLR-STOP-SILKBOARD-01",
              "descriptor": { "name": "Silk Board Bus Stop" }
            }
          },
          {
            "type": "END",
            "location": {
              "@type": "mobility:Stop",
              "id": "BLR-STOP-MAJESTIC-01",
              "descriptor": { "name": "Kempegowda Bus Terminal (Majestic)" }
            }
          }
        ],
        "time": { "timestamp": "2026-02-03T08:00:00+05:30", "label": "DEPARTURE" }
      },
      "item": {
        "category": { "@type": "mobility:VehicleCategory", "descriptor": { "code": "BUS" } }
      },
      "tags": [
        { "descriptor": { "code": "RIDER_CATEGORY" }, "value": "ADULT" },
        { "descriptor": { "code": "PASSENGER_COUNT" }, "value": "1" },
        { "descriptor": { "code": "MODES" }, "value": "BUS" }
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
    "transaction_id": "txn-bus-4d9c2f", "message_id": "msg-002",
    "timestamp": "2026-02-03T08:00:01+05:30", "ttl": "PT30S",
    "bap_id": "transit-app.bap.io", "bap_uri": "https://api.transit-app.io/beckn",
    "bpp_id": "bmtc.bpp.io", "bpp_uri": "https://api.bmtc.in/beckn"
  },
  "message": {
    "catalog": {
      "@type": "mobility:TripResult",
      "providers": [
        {
          "@type": "mobility:Operator",
          "id": "bmtc",
          "descriptor": { "name": "Bruhat Bengaluru Mahanagara Palike Transport" },
          "items": [
            {
              "@type": "mobility:FareProduct",
              "id": "fare-adult-single",
              "descriptor": { "name": "Adult Single Trip", "short_desc": "Valid for one journey on selected route" },
              "price": { "value": "32", "currency": "INR" },
              "tags": [
                { "descriptor": { "code": "RIDER_CATEGORY_ID" }, "value": "ADULT" },
                { "descriptor": { "code": "DURATION_TYPE" }, "value": "SINGLE_TRIP" }
              ]
            }
          ],
          "fulfillments": [
            {
              "@type": "mobility:Itinerary",
              "id": "itin-500c-direct",
              "descriptor": { "name": "Direct — Route 500C", "short_desc": "38 min, 0 transfers" },
              "tags": [
                { "descriptor": { "code": "TOTAL_DURATION_MINUTES" }, "value": "38" },
                { "descriptor": { "code": "TRANSFER_COUNT" }, "value": "0" }
              ],
              "legs": [
                {
                  "@type": "mobility:Leg",
                  "id": "leg-500c-01",
                  "mode": "BUS",
                  "route": {
                    "@type": "mobility:Route",
                    "id": "BLR-RT-500C",
                    "descriptor": { "short_name": "500C", "name": "Silk Board — Majestic via Koramangala" },
                    "route_type": "BUS"
                  },
                  "vehicle_journey": {
                    "@type": "mobility:VehicleJourney",
                    "id": "vj-500c-0815",
                    "departure": "2026-02-03T08:12:00+05:30",
                    "arrival": "2026-02-03T08:50:00+05:30"
                  },
                  "origin": {
                    "@type": "mobility:Stop",
                    "id": "BLR-STOP-SILKBOARD-01",
                    "descriptor": { "name": "Silk Board" },
                    "stop_time": { "departure_time": "08:12:00" }
                  },
                  "destination": {
                    "@type": "mobility:Stop",
                    "id": "BLR-STOP-MAJESTIC-01",
                    "descriptor": { "name": "Majestic" },
                    "stop_time": { "arrival_time": "08:50:00" }
                  }
                }
              ],
              "fare": {
                "@type": "mobility:Fare",
                "id": "fare-500c-adult",
                "amount": "32",
                "currency": "INR",
                "fare_rules": [{ "@type": "mobility:FareLegRule", "fare_product_id": "fare-adult-single" }]
              }
            },
            {
              "@type": "mobility:Itinerary",
              "id": "itin-via-krmarket",
              "descriptor": { "name": "Via KR Market — 2 buses", "short_desc": "52 min, 1 transfer at KR Market" },
              "tags": [
                { "descriptor": { "code": "TOTAL_DURATION_MINUTES" }, "value": "52" },
                { "descriptor": { "code": "TRANSFER_COUNT" }, "value": "1" }
              ]
            }
          ],
          "tags": [
            {
              "descriptor": { "code": "NETWORK" },
              "@type": "mobility:Network",
              "list": [
                { "descriptor": { "code": "NETWORK_ID" }, "value": "BMTC" },
                { "descriptor": { "code": "NETWORK_NAME" }, "value": "BMTC Bengaluru City Bus" }
              ]
            },
            {
              "descriptor": { "code": "CANCELLATION_POLICY" },
              "@type": "mobility:CancellationPolicy",
              "list": [{ "descriptor": { "code": "CANCELLATION_TERMS" }, "value": "Non-refundable once ticket issued" }]
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
  "context": { "domain": "mobility", "action": "select", "version": "2.0",
    "transaction_id": "txn-bus-4d9c2f", "message_id": "msg-003",
    "timestamp": "2026-02-03T08:01:00+05:30", "ttl": "PT30S",
    "bap_id": "transit-app.bap.io", "bap_uri": "https://api.transit-app.io/beckn",
    "bpp_id": "bmtc.bpp.io", "bpp_uri": "https://api.bmtc.in/beckn" },
  "message": {
    "order": {
      "provider": { "id": "bmtc" },
      "items": [{ "id": "fare-adult-single", "quantity": { "count": 1 } }],
      "fulfillments": [
        {
          "id": "itin-500c-direct",
          "stops": [
            { "type": "START", "location": { "@type": "mobility:Stop", "id": "BLR-STOP-SILKBOARD-01" } },
            { "type": "END", "location": { "@type": "mobility:Stop", "id": "BLR-STOP-MAJESTIC-01" } }
          ],
          "tags": [
            { "descriptor": { "code": "VEHICLE_JOURNEY_ID" }, "value": "vj-500c-0815" },
            { "descriptor": { "code": "ROUTE_ID" }, "value": "BLR-RT-500C" },
            { "descriptor": { "code": "QUANTITY" }, "value": "1" }
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
    "transaction_id": "txn-bus-4d9c2f", "message_id": "msg-004",
    "timestamp": "2026-02-03T08:01:01+05:30", "ttl": "PT30S",
    "bap_id": "transit-app.bap.io", "bap_uri": "https://api.transit-app.io/beckn",
    "bpp_id": "bmtc.bpp.io", "bpp_uri": "https://api.bmtc.in/beckn" },
  "message": {
    "order": {
      "items": [{ "id": "fare-adult-single", "price": { "value": "32", "currency": "INR" } }],
      "fulfillments": [
        {
          "id": "itin-500c-direct",
          "tags": [
            {
              "descriptor": { "code": "BOARDING_STOP" },
              "@type": "mobility:Stop",
              "list": [
                { "descriptor": { "code": "STOP_ID" }, "value": "BLR-STOP-SILKBOARD-01" },
                { "descriptor": { "code": "STOP_NAME" }, "value": "Silk Board Bus Stop" },
                { "descriptor": { "code": "DEPARTURE_TIME" }, "value": "08:12" }
              ]
            },
            {
              "descriptor": { "code": "FARE_MEDIUM" },
              "@type": "mobility:FareMedium",
              "list": [{ "descriptor": { "code": "MEDIUM_TYPE" }, "value": "QR_CODE" }]
            }
          ]
        }
      ],
      "quote": {
        "price": { "value": "32", "currency": "INR" },
        "breakup": [{ "item": { "descriptor": { "code": "ADULT_SINGLE_TRIP_500C" } }, "price": { "value": "32", "currency": "INR" } }]
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
    "transaction_id": "txn-bus-4d9c2f", "message_id": "msg-005",
    "timestamp": "2026-02-03T08:01:15+05:30", "ttl": "PT30S",
    "bap_id": "transit-app.bap.io", "bap_uri": "https://api.transit-app.io/beckn",
    "bpp_id": "bmtc.bpp.io", "bpp_uri": "https://api.bmtc.in/beckn" },
  "message": {
    "order": {
      "provider": { "id": "bmtc" },
      "items": [{ "id": "fare-adult-single", "quantity": { "count": 1 } }],
      "fulfillments": [
        {
          "id": "itin-500c-direct",
          "customer": {
            "@type": "mobility:Passenger",
            "person": { "name": "Ravi Sharma" },
            "contact": { "phone": "+919988776655" }
          },
          "tags": [
            { "descriptor": { "code": "RIDER_CATEGORY" }, "value": "ADULT" },
            { "descriptor": { "code": "FARE_MEDIUM" }, "value": "QR_CODE" }
          ]
        }
      ],
      "billing": { "name": "Ravi Sharma", "phone": "+919988776655" }
    }
  }
}
```

### `on_init` (BPP → BAP)

```json
{
  "context": { "domain": "mobility", "action": "on_init", "version": "2.0",
    "transaction_id": "txn-bus-4d9c2f", "message_id": "msg-006",
    "timestamp": "2026-02-03T08:01:16+05:30", "ttl": "PT30S",
    "bap_id": "transit-app.bap.io", "bap_uri": "https://api.transit-app.io/beckn",
    "bpp_id": "bmtc.bpp.io", "bpp_uri": "https://api.bmtc.in/beckn" },
  "message": {
    "order": {
      "items": [{ "id": "fare-adult-single", "price": { "value": "32", "currency": "INR" } }],
      "fulfillments": [{ "id": "itin-500c-direct" }],
      "quote": { "price": { "value": "32", "currency": "INR" }, "breakup": [
        { "item": { "descriptor": { "code": "ADULT_SINGLE_TRIP" } }, "price": { "value": "32", "currency": "INR" } }
      ]},
      "cancellation_terms": [{ "cancellation_fee": { "percentage": "100" }, "reason_required": false,
        "tags": [{ "descriptor": { "code": "NOTE" }, "value": "Non-refundable once QR code is issued" }] }],
      "payments": [{ "type": "ON_ORDER", "collected_by": "BPP", "status": "NOT-PAID",
        "tags": [{ "descriptor": { "code": "PAYMENT_TERMS" }, "value": "PRE_PAYMENT_REQUIRED" }] }]
    }
  }
}
```

---

## 4. confirm / on_confirm — QR Ticket Issued

### `confirm` (BAP → BPP)

```json
{
  "context": { "domain": "mobility", "action": "confirm", "version": "2.0",
    "transaction_id": "txn-bus-4d9c2f", "message_id": "msg-007",
    "timestamp": "2026-02-03T08:01:30+05:30", "ttl": "PT30S",
    "bap_id": "transit-app.bap.io", "bap_uri": "https://api.transit-app.io/beckn",
    "bpp_id": "bmtc.bpp.io", "bpp_uri": "https://api.bmtc.in/beckn" },
  "message": {
    "order": {
      "provider": { "id": "bmtc" },
      "items": [{ "id": "fare-adult-single", "quantity": { "count": 1 } }],
      "fulfillments": [
        {
          "id": "itin-500c-direct",
          "customer": { "person": { "name": "Ravi Sharma" }, "contact": { "phone": "+919988776655" } }
        }
      ],
      "billing": { "name": "Ravi Sharma", "phone": "+919988776655" },
      "payments": [{ "type": "ON_ORDER", "collected_by": "BPP", "status": "PAID",
        "transaction_id": "upi-bmtc-bus-001",
        "tags": [{ "descriptor": { "code": "PAYMENT_REF" }, "value": "upi-bmtc-bus-001" }] }]
    }
  }
}
```

### `on_confirm` (BPP → BAP) — QR ticket issued as VC

```json
{
  "context": { "domain": "mobility", "action": "on_confirm", "version": "2.0",
    "transaction_id": "txn-bus-4d9c2f", "message_id": "msg-008",
    "timestamp": "2026-02-03T08:01:32+05:30", "ttl": "PT30S",
    "bap_id": "transit-app.bap.io", "bap_uri": "https://api.transit-app.io/beckn",
    "bpp_id": "bmtc.bpp.io", "bpp_uri": "https://api.bmtc.in/beckn" },
  "message": {
    "order": {
      "@type": "mobility:Itinerary",
      "id": "booking-bmtc-20260203-001",
      "status": "CONFIRMED",
      "provider": { "@type": "mobility:Operator", "id": "bmtc", "descriptor": { "name": "BMTC" } },
      "items": [
        {
          "@type": "mobility:FareProduct",
          "id": "fare-adult-single",
          "descriptor": { "name": "Adult Single Trip — Route 500C" },
          "price": { "value": "32", "currency": "INR" },
          "tags": [
            { "descriptor": { "code": "VALID_FROM" }, "value": "2026-02-03T08:01:32+05:30" },
            { "descriptor": { "code": "VALID_UNTIL" }, "value": "2026-02-03T23:59:59+05:30" }
          ]
        }
      ],
      "fulfillments": [
        {
          "id": "itin-500c-direct",
          "state": { "descriptor": { "code": "TICKET_ISSUED", "name": "QR code ready to scan" } },
          "stops": [
            {
              "type": "START",
              "location": { "@type": "mobility:Stop", "id": "BLR-STOP-SILKBOARD-01", "descriptor": { "name": "Silk Board" } },
              "time": { "timestamp": "2026-02-03T08:12:00+05:30", "label": "DEPARTURE" }
            },
            {
              "type": "END",
              "location": { "@type": "mobility:Stop", "id": "BLR-STOP-MAJESTIC-01", "descriptor": { "name": "Majestic" } }
            }
          ],
          "documents": [
            {
              "@type": "mobility:TravelDocument",
              "id": "doc-qr-bmtc-001",
              "type": "QR_CODE",
              "url": "https://tickets.bmtc.in/qr/tkts-bus-blr-20260203-001",
              "descriptor": { "name": "BMTC QR Ticket — Show to conductor" },
              "valid_from": "2026-02-03T08:01:32+05:30",
              "valid_until": "2026-02-03T23:59:59+05:30"
            },
            {
              "descriptor": { "code": "KIOSK_PRINT_INSTRUCTIONS" },
              "descriptor": { "name": "No smartphone? Print at BMTC kiosk using booking ID: BMTC-20260203-001" }
            }
          ],
          "tags": [
            {
              "descriptor": { "code": "TICKET" },
              "@type": "mobility:Ticket",
              "list": [
                { "descriptor": { "code": "TICKET_ID" }, "value": "tkts-bus-blr-20260203-001" },
                { "descriptor": { "code": "TICKET_TYPE" }, "value": "SINGLE" },
                { "descriptor": { "code": "ROUTE" }, "value": "500C Silk Board → Majestic" }
              ]
            },
            { "descriptor": { "code": "INVOICE_URL" }, "value": "https://invoices.bmtc.in/inv/booking-bmtc-20260203-001.pdf" }
          ]
        }
      ],
      "quote": { "price": { "value": "32", "currency": "INR" } },
      "payments": [{ "type": "ON_ORDER", "status": "PAID", "transaction_id": "upi-bmtc-bus-001" }]
    }
  }
}
```

---

## 5. status / on_status — Live Bus Location

### `status` (BAP → BPP)

```json
{
  "context": { "domain": "mobility", "action": "status", "version": "2.0",
    "transaction_id": "txn-bus-4d9c2f", "message_id": "msg-009",
    "timestamp": "2026-02-03T08:08:00+05:30", "ttl": "PT30S",
    "bap_id": "transit-app.bap.io", "bap_uri": "https://api.transit-app.io/beckn",
    "bpp_id": "bmtc.bpp.io", "bpp_uri": "https://api.bmtc.in/beckn" },
  "message": { "order_id": "booking-bmtc-20260203-001" }
}
```

### `on_status` (BPP → BAP)

```json
{
  "context": { "domain": "mobility", "action": "on_status", "version": "2.0",
    "transaction_id": "txn-bus-4d9c2f", "message_id": "msg-010",
    "timestamp": "2026-02-03T08:08:01+05:30", "ttl": "PT30S",
    "bap_id": "transit-app.bap.io", "bap_uri": "https://api.transit-app.io/beckn",
    "bpp_id": "bmtc.bpp.io", "bpp_uri": "https://api.bmtc.in/beckn" },
  "message": {
    "order": {
      "id": "booking-bmtc-20260203-001",
      "fulfillments": [
        {
          "id": "itin-500c-direct",
          "state": { "descriptor": { "code": "BUS_EN_ROUTE", "name": "Bus 2 stops away, arriving in ~4 min" } },
          "tags": [
            {
              "descriptor": { "code": "VEHICLE_POSITION" },
              "@type": "mobility:VehiclePosition",
              "list": [
                { "descriptor": { "code": "LATITUDE" }, "value": "12.9631" },
                { "descriptor": { "code": "LONGITUDE" }, "value": "77.6300" },
                { "descriptor": { "code": "CURRENT_STOP_SEQUENCE" }, "value": "14" },
                { "descriptor": { "code": "CURRENT_STATUS" }, "value": "IN_TRANSIT_TO" }
              ]
            },
            {
              "descriptor": { "code": "STOP_TIME_UPDATE" },
              "@type": "mobility:StopTimeUpdate",
              "list": [
                { "descriptor": { "code": "STOP_ID" }, "value": "BLR-STOP-SILKBOARD-01" },
                { "descriptor": { "code": "ARRIVAL_DELAY_SECONDS" }, "value": "120" },
                { "descriptor": { "code": "EXPECTED_ARRIVAL" }, "value": "2026-02-03T08:14:00+05:30" }
              ]
            },
            {
              "descriptor": { "code": "OCCUPANCY_STATUS" },
              "@type": "mobility:OccupancyStatus",
              "list": [{ "descriptor": { "code": "OCCUPANCY_LEVEL" }, "value": "MANY_SEATS_AVAILABLE" }]
            }
          ]
        }
      ]
    }
  }
}
```

---

## 6. track / on_track — Real-Time Bus Map

### `track` / `on_track`

```json
{
  "context": { "domain": "mobility", "action": "track", "version": "2.0",
    "transaction_id": "txn-bus-4d9c2f", "message_id": "msg-011",
    "timestamp": "2026-02-03T08:09:00+05:30", "ttl": "PT30S",
    "bap_id": "transit-app.bap.io", "bap_uri": "https://api.transit-app.io/beckn",
    "bpp_id": "bmtc.bpp.io", "bpp_uri": "https://api.bmtc.in/beckn" },
  "message": { "order_id": "booking-bmtc-20260203-001" }
}
```

```json
{
  "context": { "domain": "mobility", "action": "on_track", "version": "2.0",
    "transaction_id": "txn-bus-4d9c2f", "message_id": "msg-012",
    "timestamp": "2026-02-03T08:09:01+05:30", "ttl": "PT30S",
    "bap_id": "transit-app.bap.io", "bap_uri": "https://api.transit-app.io/beckn",
    "bpp_id": "bmtc.bpp.io", "bpp_uri": "https://api.bmtc.in/beckn" },
  "message": {
    "tracking": {
      "id": "track-500c-vj-0815",
      "status": "active",
      "url": "https://live.bmtc.in/track/vj-500c-0815",
      "location": {
        "@type": "mobility:VehiclePosition",
        "updated_at": "2026-02-03T08:08:55+05:30",
        "gps": "12.9631,77.6300",
        "tags": [
          { "descriptor": { "code": "SPEED_KPH" }, "value": "28" },
          { "descriptor": { "code": "BEARING_DEGREES" }, "value": "320" }
        ]
      }
    }
  }
}
```

---

## 7. update / on_update — Route Diversion Alert (Bus carries NOTHING in contract changes)

```json
{
  "context": { "domain": "mobility", "action": "on_update", "version": "2.0",
    "transaction_id": "txn-bus-4d9c2f", "message_id": "msg-013",
    "timestamp": "2026-02-03T08:20:00+05:30", "ttl": "PT30S",
    "bap_id": "transit-app.bap.io", "bap_uri": "https://api.transit-app.io/beckn",
    "bpp_id": "bmtc.bpp.io", "bpp_uri": "https://api.bmtc.in/beckn" },
  "message": {
    "order": {
      "id": "booking-bmtc-20260203-001",
      "fulfillments": [
        {
          "id": "itin-500c-direct",
          "tags": [
            {
              "descriptor": { "code": "SERVICE_ALERT" },
              "@type": "mobility:Alert",
              "list": [
                { "descriptor": { "code": "CAUSE" }, "value": "CONSTRUCTION" },
                { "descriptor": { "code": "EFFECT" }, "value": "DETOUR" },
                { "descriptor": { "code": "HEADER_TEXT" }, "value": "Route 500C Detour via Hosur Road" },
                { "descriptor": { "code": "DESCRIPTION_TEXT" }, "value": "Buses diverted via Hosur Road due to road work near Bommanahalli. No stop change for passengers." }
              ]
            },
            {
              "descriptor": { "code": "AFFECTED_LINE" },
              "@type": "mobility:AffectedLine",
              "list": [
                { "descriptor": { "code": "LINE_ID" }, "value": "BLR-RT-500C" },
                { "descriptor": { "code": "CAUSE" }, "value": "CONSTRUCTION" }
              ]
            }
          ]
        }
      ]
    }
  }
}
```

> **Note:** Bus `on_update` carries ONLY informational alerts. No `quote` changes, no `item` modifications. The ticket remains valid.

---

## 8. cancel / on_cancel

```json
{
  "context": { "domain": "mobility", "action": "cancel", "version": "2.0",
    "transaction_id": "txn-bus-4d9c2f", "message_id": "msg-014",
    "timestamp": "2026-02-03T08:10:00+05:30", "ttl": "PT30S",
    "bap_id": "transit-app.bap.io", "bap_uri": "https://api.transit-app.io/beckn",
    "bpp_id": "bmtc.bpp.io", "bpp_uri": "https://api.bmtc.in/beckn" },
  "message": { "order_id": "booking-bmtc-20260203-001", "cancellation_reason_id": "007",
    "descriptor": { "short_desc": "Route diverted — journey no longer viable" } }
}
```

```json
{
  "context": { "domain": "mobility", "action": "on_cancel", "version": "2.0",
    "transaction_id": "txn-bus-4d9c2f", "message_id": "msg-015",
    "timestamp": "2026-02-03T08:10:02+05:30", "ttl": "PT30S",
    "bap_id": "transit-app.bap.io", "bap_uri": "https://api.transit-app.io/beckn",
    "bpp_id": "bmtc.bpp.io", "bpp_uri": "https://api.bmtc.in/beckn" },
  "message": {
    "order": {
      "id": "booking-bmtc-20260203-001", "status": "CANCELLED",
      "quote": { "price": { "value": "0", "currency": "INR" }, "breakup": [
        { "item": { "descriptor": { "code": "NO_REFUND" } }, "price": { "value": "32", "currency": "INR" },
          "tags": [{ "descriptor": { "code": "NOTE" }, "value": "Non-refundable bus ticket — platform credit of ₹32 issued" }] }
      ]},
      "fulfillments": [
        { "id": "itin-500c-direct", "state": { "descriptor": { "code": "CANCELLED" } },
          "tags": [{ "descriptor": { "code": "PLATFORM_CREDIT_INR" }, "value": "32" }] }
      ]
    }
  }
}
```

---

## 9. rating / on_rating

```json
{
  "context": { "domain": "mobility", "action": "rating", "version": "2.0",
    "transaction_id": "txn-bus-4d9c2f", "message_id": "msg-016",
    "timestamp": "2026-02-03T09:15:00+05:30", "ttl": "PT30S",
    "bap_id": "transit-app.bap.io", "bap_uri": "https://api.transit-app.io/beckn",
    "bpp_id": "bmtc.bpp.io", "bpp_uri": "https://api.bmtc.in/beckn" },
  "message": {
    "ratings": [
      { "@type": "mobility:Rating", "id": "rat-bus-01", "rating_category": "Service", "value": "3",
        "tags": [{ "descriptor": { "code": "ORDER_ID" }, "value": "booking-bmtc-20260203-001" }] }
    ],
    "tags": [{ "descriptor": { "code": "FEEDBACK_TAGS" }, "value": "OVERCROWDED,ON_TIME" }]
  }
}
```

---

## 10. support / on_support — Billing Complaint (₹42 charged vs ₹32)

```json
{
  "context": { "domain": "mobility", "action": "support", "version": "2.0",
    "transaction_id": "txn-bus-4d9c2f", "message_id": "msg-017",
    "timestamp": "2026-02-03T09:30:00+05:30", "ttl": "PT30S",
    "bap_id": "transit-app.bap.io", "bap_uri": "https://api.transit-app.io/beckn",
    "bpp_id": "bmtc.bpp.io", "bpp_uri": "https://api.bmtc.in/beckn" },
  "message": {
    "support": {
      "@type": "mobility:SupportCase",
      "order_id": "booking-bmtc-20260203-001",
      "type": "COMPLAINT",
      "descriptor": { "short_desc": "Ticket shows ₹32 but app deducted ₹42 from wallet" }
    }
  }
}
```

```json
{
  "context": { "domain": "mobility", "action": "on_support", "version": "2.0",
    "transaction_id": "txn-bus-4d9c2f", "message_id": "msg-018",
    "timestamp": "2026-02-03T09:30:02+05:30", "ttl": "PT30S",
    "bap_id": "transit-app.bap.io", "bap_uri": "https://api.transit-app.io/beckn",
    "bpp_id": "bmtc.bpp.io", "bpp_uri": "https://api.bmtc.in/beckn" },
  "message": {
    "support": {
      "@type": "mobility:SupportCase",
      "order_id": "booking-bmtc-20260203-001",
      "ref_id": "case-bmtc-billing-441",
      "descriptor": { "short_desc": "Billing dispute raised. Reviewing payment gateway logs." },
      "phone": "080-22975500",
      "email": "helpdesk@bmtc.in",
      "url": "https://support.bmtc.in/case/case-bmtc-billing-441",
      "tags": [
        { "descriptor": { "code": "RECEIPT_URL" }, "value": "https://invoices.bmtc.in/inv/booking-bmtc-20260203-001.pdf" }
      ]
    }
  }
}
```
