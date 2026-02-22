from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    
@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}

'''@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": [f"title is {payLoad['title']}, content = {payLoad['content']}"]}
# title str, content str'''

@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post)
    print(new_post.dict())
    return {"data": new_post}
