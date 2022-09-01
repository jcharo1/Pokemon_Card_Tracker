Pokebinder

# Pokemon Card Binder API

This is a mainly a back-end oriented project. A temporary front-end page is displayed for aesthetic purposes only and is non interactive.

## Capstone Project for Udacity's Full Stack Developer Nanodegree

Heroku Link: https://online-poke-binder.herokuapp.com/

While running locally: http://localhost:5000

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).

#### Virtual Enviornment

Recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

## Database Setup Locally

With Postgres running, initialize the the database

```bash
createdb poketrack

psql poketrack < poketrack.psql
```

## Enviorment variables

In order to set enviorment varibles for test cases create a .test.env and update with your information
a .test.env file has been included with valid tokens for testing purposes
ie

```
DATABASE_URL=postgresql://@localhost:5432/poketrack
API_AUDIENCE=pokemon
ADMIN_TOKEN=
USER_TOKEN=
```

all postman endpoints have been exported to git hub with auth tokens included

## Running the server

To run the server, execute:

```bash
export DATABASE_URL=<database-connection-url>
export FLASK_APP=app.py
flask run --reload
```

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file to find the application.

Using the `--reload` flag will detect file changes and restart the server automatically.

## API Reference

## Getting Started

Base URL: This application can be run locally. The hosted version is at `https://online-poke-binder.herokuapp.com/`.

Authentication: This application requires authentication to perform various actions. All the endpoints require
various permissions, except the root (or health) endpoint, that are passed via the `Bearer` token.

The application has three different types of roles:

- Public
- can get all users
- has 'get:users' permissions

- User

- has `delete:actor, delete:movie` permissions
- can get user by id , add cards and delete cards
- has `get:user-id, post:add-card, delete:card` permissions

- Admin
  - can perform all the actions
  - can post new users, edit users, get users by id, add cards, delete cards and get all users
  - has `post:user, patch:user, get:user-id, post:add-card, delete:card, get:users` permissions

## Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "error": 404,
    "message": "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.",
    "success": false
}
```

The API will return the following errors based on how the request fails:

- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 405: Method Not Allowed
- 422: Unprocessable Entity
- 500: Internal Server Error

## Endpoints

#### GET /

- General

  - root endpoint
  - can also work to check if the api is up and running
  - is a public endpoint, requires no authentication

- Sample Request
  - `https://online-poke-binder.herokuapp.com/`

<details>
<summary>Sample Response</summary>

```
{
    "health": "Running!!"
}
```

</details>

#### GET /user

- General

  - gets the list of all users
  - requires no permission

- Sample Request
  - `https://online-poke-binder.herokuapp.com/user`

<details>
<summary>Sample Response</summary>

```
{
    "success": true,
    "total users": 32,
    "users": [
        {
            "id": 3,
            "name": "charomandergod",
            "pokemongo_id": "212212313",
            "verified": false
        },
        {
            "id": 4,
            "name": "charomandergod",
            "pokemongo_id": "212212313",
            "verified": false
        },
        {
            "id": 5,
            "name": "charomandergod",
            "pokemongo_id": "212212313",
            "verified": false
        },
        {
            "id": 6,
            "name": "charomandergod",
            "pokemongo_id": "212212313",
            "verified": false
        },
        {
            "id": 7,
            "name": "charomandergod",
            "pokemongo_id": "212212313",
            "verified": false
        },
        {
            "id": 8,
            "name": "charomandergod",
            "pokemongo_id": "212212313",
            "verified": false
        },
        {
            "id": 9,
            "name": "charomandergod",
            "pokemongo_id": "212212313",
            "verified": false
        },
        {
            "id": 10,
            "name": "charomandergod",
            "pokemongo_id": "212212313",
            "verified": false
        },
        {
            "id": 11,
            "name": "charomandergod",
            "pokemongo_id": "212212313",
            "verified": false
        },
        {
            "id": 12,
            "name": "charomandergod",
            "pokemongo_id": "212212313",
            "verified": false
        },
        {
            "id": 13,
            "name": "charomandergod",
            "pokemongo_id": "212212313",
            "verified": false
        },
        {
            "id": 14,
            "name": "charomandergod",
            "pokemongo_id": "212212313",
            "verified": false
        },
        {
            "id": 15,
            "name": "charomandergod",
            "pokemongo_id": "212212313",
            "verified": false
        },
        {
            "id": 16,
            "name": "",
            "pokemongo_id": "",
            "verified": false
        },
        {
            "id": 17,
            "name": "",
            "pokemongo_id": "",
            "verified": false
        },
        {
            "id": 18,
            "name": "",
            "pokemongo_id": "",
            "verified": false
        },
        {
            "id": 19,
            "name": "",
            "pokemongo_id": "",
            "verified": false
        },
        {
            "id": 21,
            "name": "",
            "pokemongo_id": "",
            "verified": false
        },
        {
            "id": 22,
            "name": "",
            "pokemongo_id": "",
            "verified": false
        },
        {
            "id": 23,
            "name": "",
            "pokemongo_id": "",
            "verified": false
        },
        {
            "id": 24,
            "name": "fgfgfgff",
            "pokemongo_id": "",
            "verified": false
        },
        {
            "id": 25,
            "name": "fgfgfgff",
            "pokemongo_id": "",
            "verified": false
        },
        {
            "id": 26,
            "name": "",
            "pokemongo_id": "",
            "verified": false
        },
        {
            "id": 27,
            "name": "",
            "pokemongo_id": "",
            "verified": false
        },
        {
            "id": 28,
            "name": "ffff",
            "pokemongo_id": "ffff",
            "verified": false
        },
        {
            "id": 29,
            "name": "ffff",
            "pokemongo_id": "ffff",
            "verified": false
        },
        {
            "id": 30,
            "name": "ffff",
            "pokemongo_id": "ffff",
            "verified": false
        },
        {
            "id": 31,
            "name": "ffff",
            "pokemongo_id": "ffff",
            "verified": false
        },
        {
            "id": 20,
            "name": "likey mc likey likeyy like",
            "pokemongo_id": "likeys pokemon id ",
            "verified": false
        },
        {
            "id": 1,
            "name": "Likey likes to programmm",
            "pokemongo_id": "100000",
            "verified": false
        },
        {
            "id": 32,
            "name": "ffff",
            "pokemongo_id": "ffff",
            "verified": false
        },
        {
            "id": 2,
            "name": "new",
            "pokemongo_id": "39393993",
            "verified": false
        }
    ]
}
```

</details>

#### GET /user/<int:id>

- General

  - gets user by id and pokemon binder asscoiated with user
  - requires `get:user-id` permission

- Sample Request
  - `https://online-poke-binder.herokuapp.com/user/2`

<details>
<summary>Sample Response</summary>

```
{
    "id": 2,
    "name": "new njjjjj4444444444ew helloo",
    "pokemon_cards": [
        {
            "artist": "Mitsuhiro Arita",
            "attacks": [
                {
                    "convertedEnergyCost": 3,
                    "cost": [
                        "Water",
                        "Water",
                        "Water"
                    ],
                    "damage": "50",
                    "name": "Dragon Rage",
                    "text": ""
                },
                {
                    "convertedEnergyCost": 4,
                    "cost": [
                        "Water",
                        "Water",
                        "Water",
                        "Water"
                    ],
                    "damage": "40",
                    "name": "Bubblebeam",
                    "text": "Flip a coin. If heads, the Defending Pokémon is now Paralyzed."
                }
            ],
            "cardmarket": {
                "prices": {
                    "averageSellPrice": 21.61,
                    "avg1": 37.0,
                    "avg30": 19.98,
                    "avg7": 21.34,
                    "germanProLow": null,
                    "lowPrice": 1.0,
                    "lowPriceExPlus": 7.5,
                    "reverseHoloAvg1": 12.94,
                    "reverseHoloAvg30": 12.87,
                    "reverseHoloAvg7": 13.88,
                    "reverseHoloLow": null,
                    "reverseHoloSell": null,
                    "reverseHoloTrend": 14.3,
                    "suggestedPrice": null,
                    "trendPrice": 33.23
                },
                "updatedAt": "2021/08/22",
                "url": "https://prices.pokemontcg.io/cardmarket/base1-6"
            },
            "convertedRetreatCost": 3,
            "evolvesFrom": "Magikarp",
            "flavorText": "Rarely seen in the wild. Huge and vicious, it is capable of destroying entire cities in a rage.",
            "hp": "100",
            "id": "base1-6",
            "images": {
                "large": "https://images.pokemontcg.io/base1/6_hires.png",
                "small": "https://images.pokemontcg.io/base1/6.png"
            },
            "legalities": {
                "unlimited": "Legal"
            },
            "level": "41",
            "name": "Gyarados",
            "nationalPokedexNumbers": [
                130
            ],
            "number": "6",
            "rarity": "Rare Holo",
            "resistances": [
                {
                    "type": "Fighting",
                    "value": "-30"
                }
            ],
            "retreatCost": [
                "Colorless",
                "Colorless",
                "Colorless"
            ],
            "set": {
                "id": "base1",
                "images": {
                    "logo": "https://images.pokemontcg.io/base1/logo.png",
                    "symbol": "https://images.pokemontcg.io/base1/symbol.png"
                },
                "legalities": {
                    "unlimited": "Legal"
                },
                "name": "Base",
                "printedTotal": 102,
                "ptcgoCode": "BS",
                "releaseDate": "1999/01/09",
                "series": "Base",
                "total": 102,
                "updatedAt": "2020/08/14 09:35:00"
            },
            "subtypes": [
                "Stage 1"
            ],
            "supertype": "Pokémon",
            "tcgplayer": {
                "prices": {
                    "holofoil": {
                        "directLow": 5.0,
                        "high": 107.99,
                        "low": 7.0,
                        "market": 18.71,
                        "mid": 20.0
                    }
                },
                "updatedAt": "2021/08/22",
                "url": "https://prices.pokemontcg.io/tcgplayer/base1-6"
            },
            "types": [
                "Water"
            ],
            "weaknesses": [
                {
                    "type": "Grass",
                    "value": "×2"
                }
            ]
        },
        {
            "artist": "Keiji Kinebuchi",
            "attacks": [
                {
                    "convertedEnergyCost": 3,
                    "cost": [
                        "Lightning",
                        "Lightning",
                        "Colorless"
                    ],
                    "damage": "30",
                    "name": "Thunder Wave",
                    "text": "Flip a coin. If heads, the Defending Pokémon is now Paralyzed."
                },
                {
                    "convertedEnergyCost": 4,
                    "cost": [
                        "Lightning",
                        "Lightning",
                        "Colorless",
                        "Colorless"
                    ],
                    "damage": "80",
                    "name": "Selfdestruct",
                    "text": "Does 20 damage to each Pokémon on each player's Bench. (Don't apply Weakness and Resistance for Benched Pokémon.) Magneton does 80 damage to itself."
                }
            ],
            "cardmarket": {
                "prices": {
                    "averageSellPrice": 17.14,
                    "avg1": 9.09,
                    "avg30": 15.58,
                    "avg7": 16.75,
                    "germanProLow": null,
                    "lowPrice": 1.0,
                    "lowPriceExPlus": 9.0,
                    "reverseHoloAvg1": 8.8,
                    "reverseHoloAvg30": 12.92,
                    "reverseHoloAvg7": 13.69,
                    "reverseHoloLow": null,
                    "reverseHoloSell": null,
                    "reverseHoloTrend": 12.94,
                    "suggestedPrice": null,
                    "trendPrice": 27.51
                },
                "updatedAt": "2021/08/22",
                "url": "https://prices.pokemontcg.io/cardmarket/base1-9"
            },
            "convertedRetreatCost": 1,
            "evolvesFrom": "Magnemite",
            "evolvesTo": [
                "Magnezone"
            ],
            "flavorText": "Formed by several Magnemites linked together. It frequently appears when sunspots flare up.",
            "hp": "60",
            "id": "base1-9",
            "images": {
                "large": "https://images.pokemontcg.io/base1/9_hires.png",
                "small": "https://images.pokemontcg.io/base1/9.png"
            },
            "legalities": {
                "unlimited": "Legal"
            },
            "level": "28",
            "name": "Magneton",
            "nationalPokedexNumbers": [
                82
            ],
            "number": "9",
            "rarity": "Rare Holo",
            "retreatCost": [
                "Colorless"
            ],
            "set": {
                "id": "base1",
                "images": {
                    "logo": "https://images.pokemontcg.io/base1/logo.png",
                    "symbol": "https://images.pokemontcg.io/base1/symbol.png"
                },
                "legalities": {
                    "unlimited": "Legal"
                },
                "name": "Base",
                "printedTotal": 102,
                "ptcgoCode": "BS",
                "releaseDate": "1999/01/09",
                "series": "Base",
                "total": 102,
                "updatedAt": "2020/08/14 09:35:00"
            },
            "subtypes": [
                "Stage 1"
            ],
            "supertype": "Pokémon",
            "tcgplayer": {
                "prices": {
                    "holofoil": {
                        "directLow": 9.44,
                        "high": 39.99,
                        "low": 5.89,
                        "market": 19.11,
                        "mid": 12.9
                    }
                },
                "updatedAt": "2021/08/22",
                "url": "https://prices.pokemontcg.io/tcgplayer/base1-9"
            },
            "types": [
                "Lightning"
            ],
            "weaknesses": [
                {
                    "type": "Fighting",
                    "value": "×2"
                }
            ]
        },
        {
            "artist": "Keiji Kinebuchi",
            "attacks": [
                {
                    "convertedEnergyCost": 3,
                    "cost": [
                        "Lightning",
                        "Lightning",
                        "Colorless"
                    ],
                    "damage": "30",
                    "name": "Thunder Wave",
                    "text": "Flip a coin. If heads, the Defending Pokémon is now Paralyzed."
                },
                {
                    "convertedEnergyCost": 4,
                    "cost": [
                        "Lightning",
                        "Lightning",
                        "Colorless",
                        "Colorless"
                    ],
                    "damage": "80",
                    "name": "Selfdestruct",
                    "text": "Does 20 damage to each Pokémon on each player's Bench. (Don't apply Weakness and Resistance for Benched Pokémon.) Magneton does 80 damage to itself."
                }
            ],
            "cardmarket": {
                "prices": {
                    "averageSellPrice": 17.14,
                    "avg1": 9.09,
                    "avg30": 15.58,
                    "avg7": 16.75,
                    "germanProLow": null,
                    "lowPrice": 1.0,
                    "lowPriceExPlus": 9.0,
                    "reverseHoloAvg1": 8.8,
                    "reverseHoloAvg30": 12.92,
                    "reverseHoloAvg7": 13.69,
                    "reverseHoloLow": null,
                    "reverseHoloSell": null,
                    "reverseHoloTrend": 12.94,
                    "suggestedPrice": null,
                    "trendPrice": 27.51
                },
                "updatedAt": "2021/08/22",
                "url": "https://prices.pokemontcg.io/cardmarket/base1-9"
            },
            "convertedRetreatCost": 1,
            "evolvesFrom": "Magnemite",
            "evolvesTo": [
                "Magnezone"
            ],
            "flavorText": "Formed by several Magnemites linked together. It frequently appears when sunspots flare up.",
            "hp": "60",
            "id": "base1-9",
            "images": {
                "large": "https://images.pokemontcg.io/base1/9_hires.png",
                "small": "https://images.pokemontcg.io/base1/9.png"
            },
            "legalities": {
                "unlimited": "Legal"
            },
            "level": "28",
            "name": "Magneton",
            "nationalPokedexNumbers": [
                82
            ],
            "number": "9",
            "rarity": "Rare Holo",
            "retreatCost": [
                "Colorless"
            ],
            "set": {
                "id": "base1",
                "images": {
                    "logo": "https://images.pokemontcg.io/base1/logo.png",
                    "symbol": "https://images.pokemontcg.io/base1/symbol.png"
                },
                "legalities": {
                    "unlimited": "Legal"
                },
                "name": "Base",
                "printedTotal": 102,
                "ptcgoCode": "BS",
                "releaseDate": "1999/01/09",
                "series": "Base",
                "total": 102,
                "updatedAt": "2020/08/14 09:35:00"
            },
            "subtypes": [
                "Stage 1"
            ],
            "supertype": "Pokémon",
            "tcgplayer": {
                "prices": {
                    "holofoil": {
                        "directLow": 9.44,
                        "high": 39.99,
                        "low": 5.89,
                        "market": 19.11,
                        "mid": 12.9
                    }
                },
                "updatedAt": "2021/08/22",
                "url": "https://prices.pokemontcg.io/tcgplayer/base1-9"
            },
            "types": [
                "Lightning"
            ],
            "weaknesses": [
                {
                    "type": "Fighting",
                    "value": "×2"
                }
            ]
        },
        {
            "artist": "Keiji Kinebuchi",
            "attacks": [
                {
                    "convertedEnergyCost": 3,
                    "cost": [
                        "Lightning",
                        "Lightning",
                        "Colorless"
                    ],
                    "damage": "30",
                    "name": "Thunder Wave",
                    "text": "Flip a coin. If heads, the Defending Pokémon is now Paralyzed."
                },
                {
                    "convertedEnergyCost": 4,
                    "cost": [
                        "Lightning",
                        "Lightning",
                        "Colorless",
                        "Colorless"
                    ],
                    "damage": "80",
                    "name": "Selfdestruct",
                    "text": "Does 20 damage to each Pokémon on each player's Bench. (Don't apply Weakness and Resistance for Benched Pokémon.) Magneton does 80 damage to itself."
                }
            ],
            "cardmarket": {
                "prices": {
                    "averageSellPrice": 17.14,
                    "avg1": 9.09,
                    "avg30": 15.58,
                    "avg7": 16.75,
                    "germanProLow": null,
                    "lowPrice": 1.0,
                    "lowPriceExPlus": 9.0,
                    "reverseHoloAvg1": 8.8,
                    "reverseHoloAvg30": 12.92,
                    "reverseHoloAvg7": 13.69,
                    "reverseHoloLow": null,
                    "reverseHoloSell": null,
                    "reverseHoloTrend": 12.94,
                    "suggestedPrice": null,
                    "trendPrice": 27.51
                },
                "updatedAt": "2021/08/22",
                "url": "https://prices.pokemontcg.io/cardmarket/base1-9"
            },
            "convertedRetreatCost": 1,
            "evolvesFrom": "Magnemite",
            "evolvesTo": [
                "Magnezone"
            ],
            "flavorText": "Formed by several Magnemites linked together. It frequently appears when sunspots flare up.",
            "hp": "60",
            "id": "base1-9",
            "images": {
                "large": "https://images.pokemontcg.io/base1/9_hires.png",
                "small": "https://images.pokemontcg.io/base1/9.png"
            },
            "legalities": {
                "unlimited": "Legal"
            },
            "level": "28",
            "name": "Magneton",
            "nationalPokedexNumbers": [
                82
            ],
            "number": "9",
            "rarity": "Rare Holo",
            "retreatCost": [
                "Colorless"
            ],
            "set": {
                "id": "base1",
                "images": {
                    "logo": "https://images.pokemontcg.io/base1/logo.png",
                    "symbol": "https://images.pokemontcg.io/base1/symbol.png"
                },
                "legalities": {
                    "unlimited": "Legal"
                },
                "name": "Base",
                "printedTotal": 102,
                "ptcgoCode": "BS",
                "releaseDate": "1999/01/09",
                "series": "Base",
                "total": 102,
                "updatedAt": "2020/08/14 09:35:00"
            },
            "subtypes": [
                "Stage 1"
            ],
            "supertype": "Pokémon",
            "tcgplayer": {
                "prices": {
                    "holofoil": {
                        "directLow": 9.44,
                        "high": 39.99,
                        "low": 5.89,
                        "market": 19.11,
                        "mid": 12.9
                    }
                },
                "updatedAt": "2021/08/22",
                "url": "https://prices.pokemontcg.io/tcgplayer/base1-9"
            },
            "types": [
                "Lightning"
            ],
            "weaknesses": [
                {
                    "type": "Fighting",
                    "value": "×2"
                }
            ]
        },
        {
            "artist": "Keiji Kinebuchi",
            "attacks": [
                {
                    "convertedEnergyCost": 3,
                    "cost": [
                        "Lightning",
                        "Lightning",
                        "Colorless"
                    ],
                    "damage": "30",
                    "name": "Thunder Wave",
                    "text": "Flip a coin. If heads, the Defending Pokémon is now Paralyzed."
                },
                {
                    "convertedEnergyCost": 4,
                    "cost": [
                        "Lightning",
                        "Lightning",
                        "Colorless",
                        "Colorless"
                    ],
                    "damage": "80",
                    "name": "Selfdestruct",
                    "text": "Does 20 damage to each Pokémon on each player's Bench. (Don't apply Weakness and Resistance for Benched Pokémon.) Magneton does 80 damage to itself."
                }
            ],
            "cardmarket": {
                "prices": {
                    "averageSellPrice": 17.14,
                    "avg1": 9.09,
                    "avg30": 15.58,
                    "avg7": 16.75,
                    "germanProLow": null,
                    "lowPrice": 1.0,
                    "lowPriceExPlus": 9.0,
                    "reverseHoloAvg1": 8.8,
                    "reverseHoloAvg30": 12.92,
                    "reverseHoloAvg7": 13.69,
                    "reverseHoloLow": null,
                    "reverseHoloSell": null,
                    "reverseHoloTrend": 12.94,
                    "suggestedPrice": null,
                    "trendPrice": 27.51
                },
                "updatedAt": "2021/08/22",
                "url": "https://prices.pokemontcg.io/cardmarket/base1-9"
            },
            "convertedRetreatCost": 1,
            "evolvesFrom": "Magnemite",
            "evolvesTo": [
                "Magnezone"
            ],
            "flavorText": "Formed by several Magnemites linked together. It frequently appears when sunspots flare up.",
            "hp": "60",
            "id": "base1-9",
            "images": {
                "large": "https://images.pokemontcg.io/base1/9_hires.png",
                "small": "https://images.pokemontcg.io/base1/9.png"
            },
            "legalities": {
                "unlimited": "Legal"
            },
            "level": "28",
            "name": "Magneton",
            "nationalPokedexNumbers": [
                82
            ],
            "number": "9",
            "rarity": "Rare Holo",
            "retreatCost": [
                "Colorless"
            ],
            "set": {
                "id": "base1",
                "images": {
                    "logo": "https://images.pokemontcg.io/base1/logo.png",
                    "symbol": "https://images.pokemontcg.io/base1/symbol.png"
                },
                "legalities": {
                    "unlimited": "Legal"
                },
                "name": "Base",
                "printedTotal": 102,
                "ptcgoCode": "BS",
                "releaseDate": "1999/01/09",
                "series": "Base",
                "total": 102,
                "updatedAt": "2020/08/14 09:35:00"
            },
            "subtypes": [
                "Stage 1"
            ],
            "supertype": "Pokémon",
            "tcgplayer": {
                "prices": {
                    "holofoil": {
                        "directLow": 9.44,
                        "high": 39.99,
                        "low": 5.89,
                        "market": 19.11,
                        "mid": 12.9
                    }
                },
                "updatedAt": "2021/08/22",
                "url": "https://prices.pokemontcg.io/tcgplayer/base1-9"
            },
            "types": [
                "Lightning"
            ],
            "weaknesses": [
                {
                    "type": "Fighting",
                    "value": "×2"
                }
            ]
        }
    ],
    "pokemongo_id": "0444444400000000000",
    "success": true,
    "verified": false
```

</details>

#### POST /user/create

- General

  - creates a new user
  - requires `post:user` permission

- Request Body

  - name: string, required
  - pokemongo_id: string, required

- Sample Request
  - `https://online-poke-binder.herokuapp.com/user/create`
  - Request Body
    ```
       {
           "name": "ffff",
           "pokemongo_id": "ffff"
       }
    ```

<details>
<summary>Sample Response</summary>

```
{
    "success": true
}
```

</details>

#### PATCH /user/<int:id>

- General

  - updates user info
  - requires `patch:user` permission

- Request Body (at least one of the following fields required)

  - name: string, required
  - pokemongo_id: string, required

- Sample Request
  - `https://online-poke-binder.herokuapp.com/user/2`
  - Request Body
    ```
       {
           "name": "new",
           "pokemongo_id": "39393993"
       }
    ```

<details>
<summary>Sample Response</summary>

```
    {
        "success": true,
        "updated pokemonGO id": "39393993",
        "updated username": "new"
    }

```

</details>

#### DELETE /binder

- General

  - deletes the pokemon card from binder
  - requires `delete:card` permission

- Sample Request
  - `https://online-poke-binder.herokuapp.com/binder`

<details>
<summary>Sample Response</summary>

```
{
    "deleted": 1,
    "success": true
}
```

</details>

#### POST /binder

- General

  - adds card to binder
  - requires `post:add-card` permission

- Request Body (at least one of the following fields required)

  - pokemon_id: string, required
  - user_id: string, required

- Sample Request
  - `https://online-poke-binder.herokuapp.com/binder/`
  - Request Body
    ```
       {
           "pokemon_id": "base1-2",
           "user_id": "2"
       }
    ```

<details>
<summary>Sample Response</summary>

```
{
    "pokemon added": "base1-2",
    "pokemon card added to user id": "2",
    "success": true
}
```

## Testing

For testing the backend, run the following commands (in the exact order):

```
createdb poketrack_test
psql poketrack_test < poketrack.psql
python test_app.py
```

In order to set enviorment varibles for test cases create a .test.env and update with your information
a .test.env file has been included with valid tokens for testing purposes
ie

```
DATABASE_URL=postgresql://@localhost:5432/poketrack_test
API_AUDIENCE=pokemon
ADMIN_TOKEN=
USER_TOKEN=
```

all postman endpoints have been exported to git hub with auth tokens included .
