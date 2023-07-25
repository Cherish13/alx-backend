## 0x00. Pagination

### Pagination:
Pagination refers to the process of dividing a large set of data or content into smaller, more manageable parts or pages. This technique is commonly used in various applications, such as websites, mobile apps, and databases, to present information in a user-friendly manner and improve performance.

In web applications, pagination is often utilized to display search results or a list of items, such as articles, products, or user profiles. Instead of showing all the data on a single page, it is divided into several pages, with each page containing a specific number of items. The user can then navigate through the pages using pagination controls, typically consisting of previous and next buttons, as well as page numbers.

### HATEOAS:


ChatGPT
HATEOAS stands for "Hypermedia as the Engine of Application State." It is a key constraint and concept of the REST (Representational State Transfer) architectural style, which is commonly used in designing web APIs. HATEOAS aims to make APIs more discoverable, self-descriptive, and flexible by including hypermedia links in the API responses.

In traditional APIs, the client and server need to have a pre-defined contract or knowledge about the endpoints and data formats to interact successfully. This tight coupling between the client and server can make the API less adaptable to changes and can result in brittle clients that break easily if the API evolves.

HATEOAS addresses this issue by providing hypermedia links within API responses. These links are references to related resources or actions that the client can perform next. By providing hypermedia links, the server guides the client on how to interact with the API dynamically, without requiring prior knowledge about the API structure.

### Tasks
0. Simple helper function: Write a function named index_range that takes two integer arguments page and page_size.

1. Simple pagination: Copy index_range from the previous task and the following class into your code.

2. Hypermedia pagination: Replicate code from the previous task.
Implement a get_hyper method that takes the same arguments (and defaults) as get_page and returns a dictionary containing the following key-value pairs:

* page_size: the length of the returned dataset page
* page: the current page number
* data: the dataset page (equivalent to return from previous task)
* next_page: number of the next page, None if no next page
* prev_page: number of the previous page, None if no previous page
* total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.

You can use the math module if necessary.

3. Deletion-resilient hypermedia pagination
The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.

Start 3-hypermedia_del_pagination.py with this code: