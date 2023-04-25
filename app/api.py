from rq import Queue
from redis import Redis
from fastapi import FastAPI, HTTPException
from jobs import process_order
from pydantic import BaseModel

class Dish(BaseModel):
    dish_name: str


app = FastAPI()

redis_conn = Redis(host='rq_redis')
order_queue = Queue('order_queue', connection=redis_conn)

@app.get("/")
def index():
    return {
        'message': 'Welcome to RQ restaurant!'
    }

@app.post("/order")
def submit_order(dish: Dish):
    job = order_queue.enqueue(process_order, dish.dish_name)
    return {
        'order_id': job.id,
    }


@app.get("/order/{order_id}")
def get_order_status(order_id: str):
    job = order_queue.fetch_job(order_id)
    if not job:
        raise HTTPException(status_code=404, detail="Order not found")

    if job.get_status() == 'failed':
        raise HTTPException(status_code=500, detail="Job failed")

    if job.get_status() != 'finished':
        return {
            'status': job.get_status()
        }

    return {
        'status': job.get_status(),
        'result': job.result
    }

