
# **api_documentation.md**

## **API 1 — JSONPlaceholder**
**Base URL:**  
`https://jsonplaceholder.typicode.com`

**Authentication:**  
None — fully open test API.

---

### **Endpoints Tested**

#### **1. GET /users**  
**Method:** GET  
**Path:** `/users`  
**Description:** Returns a collection of 10 user objects.  
**Example Response Shape:**  
```json
[
  {
    "id": 1,
    "name": "Leanne Graham",
    "email": "Sincere@april.biz",
    "address": { ... }
  },
  ...
]
```

---

#### **2. GET /posts?userId=5**  
**Method:** GET  
**Path:** `/posts?userId=5`  
**Description:** Returns posts filtered by the `userId` query parameter.  
**Example Response Shape:**  
```json
[
  {
    "userId": 5,
    "id": 41,
    "title": "non est facere",
    "body": "molestias id nostrum..."
  }
]
```

---

#### **3. POST /posts**  
**Method:** POST  
**Path:** `/posts`  
**Description:** Creates a new post (simulated). Always returns `id: 101`.  
**Example Response Shape:**  
```json
{
  "title": "My first API post",
  "body": "Learning how POST requests work",
  "userId": 1,
  "id": 101
}
```

---

### **Rate Limits Observed**  
None — JSONPlaceholder does not enforce rate limits for typical testing.

### **One Thing That Surprised Me**  
POST requests always return the same ID (`101`) because the API simulates creation rather than storing data.

---

---

## **API 2 — PokeAPI**
**Base URL:**  
`https://pokeapi.co/api/v2`

**Authentication:**  
None — fully open public API.

---

### **Endpoints Tested**

#### **1. GET /pokemon/1**  
**Method:** GET  
**Path:** `/pokemon/1`  
**Description:** Returns full details for Bulbasaur.  
**Example Response Shape:**  
```json
{
  "id": 1,
  "name": "bulbasaur",
  "height": 7,
  "weight": 69,
  "abilities": [
    { "ability": { "name": "overgrow" } },
    { "ability": { "name": "chlorophyll" } }
  ],
  "types": [
    { "type": { "name": "grass", "url": "..." } }
  ]
}
```

---

#### **2. GET /pokemon/25**  
**Method:** GET  
**Path:** `/pokemon/25`  
**Description:** Returns full details for Pikachu.  
**Example Response Shape:**  
```json
{
  "id": 25,
  "name": "pikachu",
  "height": 4,
  "weight": 60,
  "abilities": [ ... ],
  "species": { "url": "..." }
}
```

---

#### **3. GET (nested) — Pokémon Type URL**  
**Method:** GET  
**Path:** `/type/<typeId>` (URL extracted from Pokémon JSON)  
**Description:** Returns a list of Pokémon belonging to a specific type.  
**Example Response Shape:**  
```json
{
  "name": "electric",
  "pokemon": [
    { "pokemon": { "name": "pikachu", "url": "..." } },
    ...
  ]
}
```

---

#### **4. GET (nested) — Pokémon Species URL**  
**Method:** GET  
**Path:** `/pokemon-species/<id>`  
**Description:** Returns species-level data such as habitat and legendary status.  
**Example Response Shape:**  
```json
{
  "name": "pikachu",
  "habitat": { "name": "forest" },
  "is_legendary": false
}
```

---

### **Rate Limits Observed**  
PokeAPI occasionally slows down or returns 503 if hit rapidly, but no formal rate limit was encountered during testing.

### **One Thing That Surprised Me**  
The nested URLs (type, species) make the API feel like a relational database — you can “follow” links to deeper resources.

---

---

## **API 3 — REST Countries (Mirror API)**
**Base URL:**  
`https://restcountries.com/v3.1`

**Authentication:**  
None — fully open public API.

---

### **Endpoints Tested**

#### **1. GET /name/japan?fullText=true**  
**Method:** GET  
**Path:** `/name/japan?fullText=true`  
**Description:** Returns detailed information for Japan.  
**Example Response Shape:**  
```json
[
  {
    "name": { "official": "Japan" },
    "capital": ["Tokyo"],
    "population": 125836021,
    "region": "Asia"
  }
]
```

---

#### **2. GET /region/europe**  
**Method:** GET  
**Path:** `/region/europe`  
**Description:** Returns all countries in Europe.  
**Example Response Shape:**  
```json
[
  { "name": { "common": "France" } },
  { "name": { "common": "Germany" } },
  ...
]
```

---

#### **3. GET /name/notacountry**  
**Method:** GET  
**Path:** `/name/notacountry`  
**Description:** Intentional error test — returns a deprecation proxy or empty list.  
**Example Response Shape:**  
```json
{
  "success": false,
  "data": null,
  "errors": [
    { "message": "No matching country found" }
  ]
}
```

---

### **Rate Limits Observed**  
None — but deprecated endpoints sometimes return proxy error objects instead of real data.

### **One Thing That Surprised Me**  
The official v3.1 and v5 endpoints are deprecated and often return proxy error JSON, but the mirror endpoints still work reliably.

