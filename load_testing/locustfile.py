from locust import HttpUser, task, between


class N11User(HttpUser):
    wait_time = between(1, 3)

    default_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive"
    }

    def on_start(self):
        with self.client.get("/", headers=self.default_headers, catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Homepage failed")

    # -------------------------
    # Popular Search
    # -------------------------
    @task(5)
    def search_laptop(self):
        self.perform_search("laptop")

    # -------------------------
    # Pagination Test
    # -------------------------
    @task(2)
    def search_pagination(self):
        with self.client.get(
            "/arama",
            params={"q": "laptop", "pg": 2},
            headers=self.default_headers,
            catch_response=True
        ) as response:

            if response.status_code != 200:
                response.failure("Pagination failed")

    # -------------------------
    # Deep Pagination
    # -------------------------
    @task(1)
    def search_deep_pagination(self):
        with self.client.get(
            "/arama",
            params={"q": "laptop", "pg": 5},
            headers=self.default_headers,
            catch_response=True
        ) as response:

            if response.status_code != 200:
                response.failure("Deep pagination failed")

    # -------------------------
    # Long Query Test
    # -------------------------
    @task(1)
    def search_long_query(self):
        long_query = "laptop gaming intel i7 16gb ram 1tb ssd nvidia rtx"
        self.perform_search(long_query)

    # -------------------------
    # Numeric Query
    # -------------------------
    @task(1)
    def search_numeric_query(self):
        self.perform_search("123456")

    # -------------------------
    # Case Sensitivity
    # -------------------------
    @task(1)
    def search_uppercase(self):
        self.perform_search("LAPTOP")

    # -------------------------
    # Burst Search (rapid repeated)
    # -------------------------
    @task(1)
    def burst_search(self):
        for _ in range(3):
            self.perform_search("laptop")

    # -------------------------
    # Special Characters
    # -------------------------
    @task(1)
    def search_special_characters(self):
        self.perform_search("!@")

    # -------------------------
    # Search Without Input
    # -------------------------
    @task(1)
    def search_without_input(self):
        with self.client.get(
            "/arama?promotions=2060476",
            headers=self.default_headers,
            catch_response=True
        ) as response:

            if response.status_code != 200:
                response.failure("Search without input failed")

    # -------------------------
    # Helper Method
    # -------------------------
    def perform_search(self, query):
        with self.client.get(
            "/arama",
            params={"q": query},
            headers=self.default_headers,
            catch_response=True
        ) as response:

            if response.status_code != 200:
                response.failure(f"Search failed for query: {query}")