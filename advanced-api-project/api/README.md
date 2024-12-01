# Advanced API Project

## Advanced Query Capabilities

This API supports advanced query capabilities for the Book model:

### Filtering
You can filter books based on various attributes using the following query parameters:
- **title**: Filter books by title (e.g., `?title=My Book`).
- **author**: Filter books by author's ID (e.g., `?author=1`).
- **publication_year**: Filter books by publication year (e.g., `?publication_year=2023`).

### Searching
To search books by title or author, use the `search` query parameter. For example:
- Search for books with 'Django':


### Ordering
You can order the results by any of the following fields:
- **title**: Order by title (e.g., `?ordering=title`).
- **publication_year**: Order by publication year (e.g., `?ordering=publication_year`).

### Combined Queries
You can combine these parameters to refine your queries:
- Example: Filter for books published in 2023, ordered by title:
