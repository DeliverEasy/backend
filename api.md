**Backend REST Documentation**
----

* **URL**

        /api/v1/token-auth/

* **Method:**
  
  `POST`

* **Data Params**

  **Required:**
 
   `username=[string], password=[string]`

* **Success Response:**
  
  * **Code:** 200 <br />
  
  * **Content:** <br />
    <pre><code>{
        "token": "XXXXX",
        "user": {
            "username": "XXXXX"
        }
    }</pre></code>

* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** 
    <pre><code>{ 
        "non_field_errors": ["Unable to log in with provided credentials."]
    }</pre></code>

* **Sample Call:**

        fetch("/echo/json/", {
            headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json' },
            method: "POST",
            body: JSON.stringify({username: "admin", password: "admin1234"})
        });

    