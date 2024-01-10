from typing import Optional

from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.params import *

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


my_posts = [{"title": "New Post", "content": "This is a new post", "id": 1}]


@app.get("/")
async def root():
    return "API built on top of FastAPI"


@app.post("/create-post")
def create_post(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = len(my_posts) + 1
    my_posts.append(post_dict)
    return {"message": "Post created succesffuly", "post": post_dict}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.get("/posts/{id}")
def get_posts_by_id():
    return {"message": f"This is a list of posts {id}"}
