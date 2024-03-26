# Beckn Mobility Interface

## What is Beckn?
[Beckn](https://becknprotocol.io/) protocol is a collection of open specifications consisting of protocol APIs, message formats, network design and reference architectures to allow any two entities to execute commercial transactions without being on the same platform. The core protocol specifications are industry-sector-agnostic by design and allow sector-specific policies to be layered as machine readable code.

This server-to-server communication protocol allows any consumer facing online platform to discover and transact with any business with minimal implementation overhead. The server-to-server nature of the protocol allows rich user experiences to be built by bundling services from multiple independent platforms.


## What is the project mission?
Beckn protocol mobility specification is an adaptation of the core protocol specification for the mobility sector and applies mobility specific rules and policies on its API and architecture to allow the creation of Open Mobility Networks.

The "beckn mobility interface" likely refers to the interface or set of standards provided by the beckn protocol that allows various mobility services, such as ride-sharing, public transportation, bike-sharing, etc., to connect and interact with each other in a standardized way. This can help create a more integrated and user-friendly experience for travelers by enabling different services to work together cohesively.

## Key Functionality

#### Interoperability
The beckn protocol aims to establish a common framework and standards for different mobility services to interact and exchange information seamlessly. This enables interoperability between various service providers and platforms.

#### Service Discovery 
The beckn protocol facilitates the discovery of available mobility services. Users can find and access different transportation options, such as ride-sharing, public transit, bike rentals, etc., through a unified interface.

#### Real-time Availability
Users can access real-time information about the availability of different mobility services, allowing them to make informed decisions on their travel plans.

#### Booking and Reservations
 The protocol enables users to make bookings and reservations for various mobility services through a standardized interface. This simplifies the process for users and service providers alike.

#### Data Privacy
 Beckn emphasizes data privacy and control for users. Personal data is shared securely and only with explicit user consent, ensuring that privacy is maintained.

#### Ecosystem Integration
 The protocol is designed to accommodate a wide range of mobility services, from public transit to private ride-sharing and beyond. This helps create an integrated and cohesive ecosystem that benefits both users and service providers.


### Local Installation
1. Clone https://github.com/beckn/mobility.git
2. In the root directory go to the api folder and check the mobility.yaml file.
3. In VScode download the Swagger Viewer extension.
4. Click ctrl+alt+P to view the yaml in swagger representation.
5. Refer to the mobility use cases in the examples folder.


## Pre Installation Steps

Prerequisities

	1. Node > 14x
	2. VScode
    
---

### Project Setup

1. Clone project

    ```console
    git clone https://github.com/beckn/mobility.git
    ```

    > ***Note***: Stable versions of the mobility are available via tags for each release, and the master branch contains latest stable release.

2. Navigate

   In the root directory go to the api folder and check the     mobility.yaml file.

3. In VScode download the Swagger Viewer extension.

4. Click ctrl+alt+P to view the yaml in swagger representation.

5. Refer to the mobility use cases in the examples folder.

### Project Structure

    .
    ├── Mobility                                            
    |   ├── /api                           
    │   |   └── mobility.yml                        
    │   |   └── core-0.9.x-lts @ 25b73d8                        
    │   |── /docs                        
    │   |     └── images                        
    │   |     └── API-flow.md                        
    │   |     └── ReadMe.md                         
    │   |── /tags                        
    │   |     └── tag-groups-draft-01.md                        
    │   |     └── tags-draft-01.md                       
    │   |── /.gitmodules                                            

## Demo

[Video](https://drive.google.com/file/d/1t_2hekrjdP6F80yUcFgS93WoSMWQRVnl/view?usp=drive_link)

