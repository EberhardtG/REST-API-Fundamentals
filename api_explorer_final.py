

import requests

BASE_URLS = {
    "jsonplaceholder": "https://jsonplaceholder.typicode.com",
    "pokeapi": "https://pokeapi.co/api/v2",
    "restcountries": "https://restcountries.com/v3.1",
}

# ============================================================
# API 1: JSONPlaceholder
# ============================================================

def explore_jsonplaceholder():
    # WHY:
    # This function is the "exploration" phase of the project.
    # Before building a reusable API client class (Part 2), we
    # manually interact with JSONPlaceholder to understand:
    #   • How GET requests retrieve collections and filtered data
    #   • How POST requests send JSON bodies
    #   • How responses come back as JSON and map to Python objects
    #
    # DESIGN:
    # We follow a consistent pattern for each API call:
    #   1. Build the full URL using BASE_URLS
    #   2. Make the request with requests.get() or requests.post()
    #   3. Parse JSON using .json()
    #   4. Extract meaningful fields and print them

    print("\n=== API 1: JSONPlaceholder ===")

    # ------------------------------------------------------------
    # TODO 1: GET all users
    # ------------------------------------------------------------
    # WHY:
# The /users endpoint returns a full collection of user resources.
# This demonstrates how REST APIs expose entire datasets through
# a single GET request. It also shows how JSONPlaceholder structures
# user objects, including nested fields like name, email, and address.
#
# DESIGN:
# 1. Build the full URL using the base + /users.
# 2. Perform a GET request because we are retrieving a collection.
# 3. Print the HTTP method, URI, status code, reason, and Content-Type
#    to reinforce how REST responses are structured.
# 4. Parse the JSON into Python objects and summarize the results by
#    printing the total number of users and key fields from each user.
#    This avoids dumping raw JSON and keeps the output readable.

    url = BASE_URLS["jsonplaceholder"] + "/users"
    print("\nGET", url)
    response = requests.get(url)
    print("Status:", response.status_code, response.reason)
    print("Content-Type:", response.headers.get("Content-Type"))

    users = response.json()
    print("Summary: Retrieved", len(users), "users.")
    for user in users:
        print(" -", user["name"], "-", user["email"])

    # ------------------------------------------------------------
    # TODO 2: GET posts by a specific user
    # ------------------------------------------------------------
    # WHY:
# This endpoint demonstrates how REST APIs support server‑side filtering
# using query parameters. By calling /posts?userId=5, we retrieve only
# the posts authored by user 5 instead of the full posts collection.
# This reinforces how REST exposes filtered views of a resource without
# requiring additional endpoints.
#
# DESIGN:
# 1. Build the URL with the query parameter ?userId=5.
# 2. Perform a GET request because we are retrieving filtered data.
# 3. Print method, URI, status code, reason, and Content-Type to show
#    the structure of the HTTP response.
# 4. Parse the JSON list and summarize the results by printing the
#    number of posts and the title of the first one.
#    This keeps the output readable and avoids dumping raw JSON.

    url = BASE_URLS["jsonplaceholder"] + "/posts?userId=5"
    print("\nGET", url)
    response = requests.get(url)
    print("Status:", response.status_code, response.reason)
    print("Content-Type:", response.headers.get("Content-Type"))

    posts = response.json()
    print("Summary: Retrieved", len(posts), "posts for user 5.")
    print("First title:", posts[0]["title"])

    # ------------------------------------------------------------
    # TODO 3: POST a new post
    # ------------------------------------------------------------
    # WHY:
# POST requests create new resources on the server. JSONPlaceholder
# simulates this behavior by accepting a JSON body and returning a
# predictable response with a new id. This teaches how REST APIs
# handle resource creation, how clients send JSON payloads, and how
# servers acknowledge successful creation with status 201.
#
# DESIGN:
# 1. Build the URL for the /posts endpoint.
# 2. Use requests.post() with json=payload so the body is automatically
#    serialized and the Content-Type header is set correctly.
# 3. Print method, URI, status code, reason, and Content-Type to show
#    the structure of a POST response.
# 4. Parse the returned JSON and summarize the result by printing the
#    new post ID, demonstrating successful resource creation.

    url = BASE_URLS["jsonplaceholder"] + "/posts"
    payload = {
        "title": "My first API post",
        "body": "Learning how POST requests work",
        "userId": 1
    }

    print("\nPOST", url)
    response = requests.post(url, json=payload)
    print("Status:", response.status_code, response.reason)
    print("Content-Type:", response.headers.get("Content-Type"))

    new_post = response.json()
    print("Summary: Created new post with ID:", new_post["id"])
    print("REST Concept: Status 201 means the resource was created.")


# ============================================================
# API 2: PokeAPI
# ============================================================

def explore_pokeapi():
    print("\n=== API 2: PokeAPI ===")

    # ------------------------------------------------------------
    # GET Bulbasaur
    # ------------------------------------------------------------
    url = BASE_URLS["pokeapi"] + "/pokemon/1"
    print("\nGET", url)
    response = requests.get(url)
    print("Status:", response.status_code, response.reason)
    print("Content-Type:", response.headers.get("Content-Type"))

    pokemon = response.json()
    print("Summary: Bulbasaur info:")
    print("Name:", pokemon["name"])
    print("Height:", pokemon["height"])
    print("Weight:", pokemon["weight"])
    print("Abilities:", [a["ability"]["name"] for a in pokemon["abilities"]])
# WHY:
# Starting with a known Pokémon (Bulbasaur, ID 1) provides a stable
# baseline for understanding how PokeAPI structures its responses.
# This endpoint demonstrates how REST APIs expose detailed resource
# representations, including nested fields like abilities and stats.
#
# DESIGN:
# 1. Build the URL using the base + /pokemon/1.
# 2. Perform a GET request to retrieve a single Pokémon resource.
# 3. Print method, URI, status code, reason, and Content-Type to
#    reinforce how REST responses are structured.
# 4. Parse the JSON and summarize key fields (name, height, weight,
#    abilities) to avoid dumping raw JSON and keep output readable.


    # ------------------------------------------------------------
    # GET Pikachu
    # ------------------------------------------------------------
    # WHY:
# This call demonstrates how REST endpoints can be parameterized.
# Instead of hardcoding a specific Pokémon, we dynamically request
# Pokémon 25 (Pikachu). This reinforces how REST APIs expose uniform
# resource structures across different IDs.
#
# DESIGN:
# 1. Build the URL using a variable Pokémon ID.
# 2. Perform a GET request to retrieve the resource.
# 3. Print method, URI, status code, reason, and Content-Type to
#    show the structure of the HTTP response.
# 4. Parse the JSON and summarize key fields, mirroring the Bulbasaur
#    example to highlight consistency across resources.

    pokemon_id = 25
    url = BASE_URLS["pokeapi"] + f"/pokemon/{pokemon_id}"
    print("\nGET", url)
    response = requests.get(url)
    print("Status:", response.status_code, response.reason)
    print("Content-Type:", response.headers.get("Content-Type"))

    pokemon = response.json()
    print("Summary: Pikachu info:")
    print("Name:", pokemon["name"])
    print("Height:", pokemon["height"])
    print("Weight:", pokemon["weight"])
    print("Abilities:", [a["ability"]["name"] for a in pokemon["abilities"]])

    # ------------------------------------------------------------
    # Nested Resource: Pokémon → Type → Pokémon list
    # ------------------------------------------------------------
  # WHY:
# This section demonstrates how REST APIs link resources together.
# The Pokémon object contains a nested URL pointing to its type
# resource. Following this URL shows how clients can navigate
# relationships between resources, similar to foreign keys in a
# database. It also reinforces the importance of defensive coding
# when dealing with nested JSON structures.
#
# DESIGN:
# 1. Validate the Pokémon response and ensure it contains type data.
# 2. Extract the first type URL and perform a GET request.
# 3. Print method, URI, status code, reason, and Content-Type.
# 4. Parse the JSON and summarize the first five Pokémon of that type,
#    demonstrating how type resources expose collections.


    print("\nNested Resource: Pokémon → Type → Pokémon list")

    url = BASE_URLS["pokeapi"] + f"/pokemon/{pokemon_id}"
    print("GET", url)
    response = requests.get(url)
    print("Status:", response.status_code, response.reason)
    print("Content-Type:", response.headers.get("Content-Type"))

    if response.status_code != 200:
        print("Error: Pokémon not found.")
    else:
        pokemon = response.json()

        if "types" not in pokemon or not pokemon["types"]:
            print("Error: No type information.")
        else:
            try:
                type_url = pokemon["types"][0]["type"]["url"]
                print("GET", type_url)
                type_response = requests.get(type_url)
                print("Status:", type_response.status_code, type_response.reason)
                print("Content-Type:", type_response.headers.get("Content-Type"))

                type_data = type_response.json()
                first_five = type_data["pokemon"][:5]
                names = [p["pokemon"]["name"] for p in first_five]

                print("Summary: First 5 Pokémon of this type:")
                for n in names:
                    print(" -", n)

            except Exception:
                print("Error: Pokémon type structure is malformed.")

    # ------------------------------------------------------------
    # Nested Resource: Pokémon → Species
    # ------------------------------------------------------------
    # WHY:
# The species endpoint provides deeper biological and lore-related
# information that is not included in the main Pokémon resource.
# Following this nested URL demonstrates how REST APIs separate
# concerns across multiple endpoints and how clients can safely
# traverse linked resources.
#
# DESIGN:
# 1. Extract the species URL from the Pokémon JSON.
# 2. Perform a GET request and print method, URI, status code,
#    reason, and Content-Type.
# 3. Parse the JSON and handle nullable fields like habitat.
# 4. Summarize key species attributes (name, habitat, legendary
#    status) to provide meaningful output without dumping raw JSON.

    print("\nNested Resource: Pokémon → Species")

    try:
        species_url = pokemon["species"]["url"]
        print("GET", species_url)
        species_response = requests.get(species_url)
        print("Status:", species_response.status_code, species_response.reason)
        print("Content-Type:", species_response.headers.get("Content-Type"))

        species_data = species_response.json()

        habitat_name = (
            species_data["habitat"]["name"]
            if species_data.get("habitat") and species_data["habitat"].get("name")
            else "None"
        )

        print("Summary: Species info:")
        print("Name:", species_data.get("name", "N/A"))
        print("Habitat:", habitat_name)
        print("Legendary:", species_data.get("is_legendary", False))

    except Exception:
        print("Error: Could not retrieve species data.")


# ============================================================
# API 3: REST Countries (Mirror API)
# ============================================================

def explore_restcountries_v3_1():
    print("\n=== API 3: REST Countries (Mirror API) ===")

    # ============================================================
    # TODO 7 — WHY:
    # The original assignment expected us to use the v3.1 endpoint
    # /name/<country>. However, both v3.1 and v5 are deprecated on
    # this network and return only a deprecation error object.
    #
    # To still complete the learning objective, we use the mirror
    # endpoint /v3.1/name/japan?fullText=true, which still returns
    # valid country data.
    #
    # DESIGN:
    # 1. GET Japan using the mirror endpoint.
    # 2. Parse JSON safely.
    # 3. If the response is malformed, print an error but DO NOT
    #    exit the function — continue to TODO 8 and TODO 9.
    # ============================================================

    url = "https://restcountries.com/v3.1/name/japan?fullText=true"
    print("\nGET", url)
    response = requests.get(url)
    print("Status:", response.status_code, response.reason)
    print("Content-Type:", response.headers.get("Content-Type"))

    try:
        countries = response.json()
    except ValueError:
        print("Error: Could not parse JSON.")
        countries = None

    if isinstance(countries, list) and countries:
        country = countries[0]
        print("Official Name:", country.get("name", {}).get("official", "N/A"))
        print("Capital:", country.get("capital", ["N/A"])[0])
        print("Population:", country.get("population", "N/A"))
        print("Region:", country.get("region", "N/A"))
    else:
        print("Error: Unexpected response format for Japan.")
        print("Raw JSON:", countries)

    # ============================================================
    # TODO 8 — WHY:
    # The assignment originally required /region/<region>, but
    # v3.1 and v5 region endpoints are deprecated on this network.
    #
    # The mirror endpoint /v3.1/region/europe still works, so we
    # use it to complete the learning objective: retrieving a list
    # of countries, counting them, and printing the first 10.
    #
    # DESIGN:
    # 1. GET Europe region data.
    # 2. Parse JSON safely.
    # 3. If the response is malformed, print an error but DO NOT
    #    exit — continue to TODO 9.
    # ============================================================

    url = "https://restcountries.com/v3.1/region/europe"
    print("\nGET", url)
    response = requests.get(url)
    print("Status:", response.status_code, response.reason)
    print("Content-Type:", response.headers.get("Content-Type"))

    try:
        europe = response.json()
    except ValueError:
        print("Error: Could not parse JSON.")
        europe = None

    if isinstance(europe, list):
        print("Count:", len(europe))
        names = sorted([c.get("name", {}).get("common", "N/A") for c in europe])
        print("First 10 countries alphabetically:", names[:10])
    else:
        print("Error: Unexpected response format for Europe.")
        print("Raw JSON:", europe)

    # ============================================================
    # TODO 9 — WHY:
    # We intentionally request a country that does not exist to
    # demonstrate safe error handling. Because the API is
    # deprecated on this network, invalid requests return the same
    # deprecation proxy JSON.
    #
    # DESIGN:
    # 1. GET an invalid country name.
    # 2. Parse JSON safely.
    # 3. Detect deprecation proxy errors.
    # 4. Print a friendly message instead of crashing.
    # ============================================================

    url = "https://restcountries.com/v3.1/name/notacountry"
    print("\nGET", url)
    response = requests.get(url)
    print("Status:", response.status_code, response.reason)
    print("Content-Type:", response.headers.get("Content-Type"))

    try:
        data = response.json()
    except ValueError:
        print("Error: Could not parse JSON.")
        data = None

    if isinstance(data, dict) and "errors" in data:
        print("API Error:", data["errors"][0]["message"])
    elif isinstance(data, list) and len(data) == 0:
        print("Summary: Country not found (empty list).")
    else:
        print("Unexpected response format:")
        print(data)


# ============================================================
# Run all explorations
# ============================================================

if __name__ == "__main__":
    explore_jsonplaceholder()
    explore_pokeapi()
    explore_restcountries_v3_1()
    print("\n=== Exploration complete! ===")
