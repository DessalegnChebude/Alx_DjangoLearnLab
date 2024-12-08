# Django Blog Project

## Blog Post Management Features

### Overview
This project allows users to create, read, update, and delete blog posts. Only authenticated users can create new posts. Each post is associated with its author, and only the author may edit or delete their post.

### Features
- **Create Post**: Authenticated users can create new blog posts.
- **View Posts**: All users can view a list of blog posts and detailed information for each post.
- **Edit Post**: Only post authors can edit their posts.
- **Delete Post**: Only post authors can delete their posts.

### URL Patterns
- `/posts/`: List all posts
- `/posts/new/`: Create a new post
- `/posts/<int:pk>/`: View a specific post
- `/posts/<int:pk>/edit/`: Edit a specific post
- `/posts/<int:pk>/delete/`: Delete a specific post

### Permissions
- Only authenticated users can create posts.
- Only the author of a post can edit or delete it.