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


# Comment Functionality in Django Blog

## Overview
This system allows users to comment on blog posts. Authenticated users can create, edit, and delete their comments.

## Adding a Comment
1. Navigate to the post's detail page.
2. Fill in the comment form and click "Post Comment."
3. Your comment will appear below the post.

## Editing a Comment
1. If you authored a comment, you can edit it.
2. Click the "Edit" link next to your comment, update your content, and submit.

## Deleting a Comment
1. If you authored a comment, you can delete it.
2. Click the "Delete" button next to your comment for removal.

## Permissions
- Only authenticated users can add comments.
- Only comment authors can edit or delete their comments.


# Tagging and Search Functionality in Django Blog

## Overview
This feature allows users to tag their blog posts and search for content easily, enhancing navigation.

## Adding Tags to Posts
- When creating or editing a post, you can select existing tags or create new ones.
- Tags are displayed on the post detail page and are linked to a filtered view of related posts.

## Searching for Posts
- Use the search bar at the top of the page to search for posts by title, content, or tags.
- The results will display all matching posts.

## Viewing Posts by Tag
- Clicking on a tag will redirect you to a list of all posts that share that tag.