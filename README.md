# Django Caching Project with Redis

This project demonstrates how to implement caching in a Django REST API using Redis.

## **Setup Instructions**

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd caching_api
   ```

2. Create a virtual environment and activate it:
   ```bash
   uv venv
   source .vnv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   uv sync
   ```
   OR
   ```bash
   uv pip install -r pyproject.toml
   ```

4. Start the Redis server:
   ```bash
   redis-server
   ```

5. Run migration:
   ```bash
   python manage.py migrate
   ```

6. Load test data:
   ```bash
   python manage.py load_posts --count 10000
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Access the API at:
   ```
   http://127.0.0.1:8000/api/posts/
   ```

## **API Endpoints**

- `GET /api/posts/`: Fetch all posts (cached for 1 minute).

## **Performance**

The project logs the time taken for cache hits and misses to the console.

* Hitting API very first time takes **200ms - 300ms**
* After first time it takes **50ms - 80ms** 
* we can clearly see the adavantage using caching, we have improved performace by approax **X4 reduce in latency**

## **Key Points About Caching**

### **1. What is Caching?**
Caching is a technique used to store copies of frequently accessed data in a temporary storage location (cache) so that future requests for that data can be served faster without querying the main data source (e.g., a database). Caching improves performance by reducing latency and load on backend systems.

### **2. Types of Caching**
1. **In-Memory Caching**:  
   Stores data in the server’s memory for quick access (e.g., Redis, Memcached).  
   - Pros: Very fast access, low latency.  
   - Cons: Limited by server memory, may require eviction policies for large datasets.
   
2. **Database Query Caching**:  
   Caches the result of expensive database queries.  
   - Pros: Reduces database load significantly.  
   - Cons: May serve stale data if not invalidated properly.

3. **Page Caching**:  
   Stores the entire rendered HTML page for faster delivery.  
   - Pros: Great for static content, reduces server-side rendering time.  
   - Cons: Not suitable for highly dynamic content.

4. **Fragment Caching**:  
   Caches specific parts of a web page or response.  
   - Pros: Useful for pages with both dynamic and static content.  
   - Cons: More complex to manage compared to page caching.

### **3. When to Use Caching**
- **High Read-to-Write Ratio**: When data is read frequently but updated infrequently (e.g., blog posts, product catalogs).
- **Expensive Computations**: When the data requires complex computations or aggregation (e.g., reports, analytics).
- **Reducing Backend Load**: To minimize the load on the database or API by serving precomputed responses.
- **Improving Latency**: When low latency is critical (e.g., real-time systems, high-traffic APIs).

### **4. When NOT to Use Caching**
- **Highly Dynamic Data**: If data changes frequently and must always reflect the latest state (e.g., financial transactions, live scores).
- **Low Read-to-Write Ratio**: When the cost of maintaining the cache exceeds the benefits (e.g., frequently updated user profiles).
- **Small Datasets**: If the dataset is small and can be quickly queried from the database without performance issues.
- **Complex Invalidation**: When cache invalidation logic is too complex or prone to errors, leading to potential data inconsistency.

### **5. Cache Invalidation**
One of the hardest problems in caching is invalidating outdated data. Common strategies include:
- **Time-Based Expiry**: Setting a timeout after which the cache is invalidated automatically.
- **Manual Invalidation**: Explicitly clearing the cache when the underlying data changes.
- **Write-Through Caching**: Updating both the cache and the database simultaneously during write operations.

### **6. Performance Benefits of Caching**
- **Reduced Latency**: Since cached data is served from memory or a faster storage medium, it reduces the response time significantly.
- **Lower Backend Load**: By reducing the number of database queries or API calls, caching helps scale backend systems.
- **Improved Scalability**: Cached data can be distributed across multiple servers, enabling the application to handle more users simultaneously.

### **7. Potential Issues with Caching**
- **Stale Data**: Cached data may become outdated if not properly invalidated.
- **Memory Usage**: In-memory caches can consume significant memory, leading to higher operational costs.
- **Complexity**: Managing cache consistency, invalidation, and eviction policies can increase system complexity.
- **Cache Stampede**: When multiple requests attempt to refresh the cache simultaneously, it can overwhelm the backend. Solutions include locking and pre-warming the cache.

### **8. Tools and Libraries for Caching**
- **Redis**: A popular in-memory data structure store, often used for caching in web applications.
- **Memcached**: Another in-memory caching system, known for simplicity and high performance.
- **Django-Redis**: A Django library that integrates Redis as a caching backend.
- **Celery**: Can be combined with caching to pre-generate and refresh expensive computations asynchronously.

### **9. Best Practices for Caching**
1. **Choose the Right Cache Timeout**: Balance between serving stale data and reducing backend load.
2. **Monitor Cache Performance**: Use logging and metrics to monitor cache hits, misses, and evictions.
3. **Avoid Over-Caching**: Cache only what’s necessary to avoid excessive memory usage.
4. **Test with Real Data**: Simulate real-world scenarios and data volumes when implementing caching.
5. **Plan Cache Invalidation**: Ensure that your cache invalidation strategy is well-defined and tested.
