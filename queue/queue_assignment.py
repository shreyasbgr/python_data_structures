import queue
import threading
import time
t=time.time()
food_orders = queue.Queue()

def place_order(arr):
    for elem in arr:
        time.sleep(0.5)
        print(f"Placing order: {elem}. Time elapsed = {time.time()-t}")
        food_orders.enqueue(elem)
        

def serve_order():
    while True:
        time.sleep(2)
        print(f"Order completed: {food_orders.dequeue()}. Time elapsed = {time.time()-t}")

if __name__ == '__main__':
    all_orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_order,args=[all_orders])
    t2 = threading.Thread(target=serve_order,args=[])

    t1.start()
    time.sleep(1)
    t2.start()

    t1.join()
    t2.join()
    print(f"Time taken for finishing all orders = {time.time()-t}")