Generate a django application that meets the following specs

Sample application should have a

- use bult-in auth
- use adrf
- use tokens from https://github.com/jazzband/django-rest-knox for auth
- use uvicorn
- use uvloop

- have CRUD endpoints for a Post type

```py
class Post
    text: str
    author: User
```

- have CRUD endpoints for a Comment type

```py
class Comment
    text: str
    post: Post
    author: User
```

- use serializers with sensible validation
- only auth users can post and comment

TODO:

- add k6 load test
