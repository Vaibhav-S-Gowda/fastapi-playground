from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [
    {"id": 1, "title": "Title of post 1", "content": "Content of post 1"},
    {"id": 2, "title": "Favorite foods", "content": "I like pizza"}
]

@app.get("/posts")
def get_posts():
    return my_posts

@app.post("/posts")
def create_post(post: Post):
    new_post = post.dict()
    new_post["id"] = randrange(0, 1000000)
    my_posts.append(new_post)
    return new_post