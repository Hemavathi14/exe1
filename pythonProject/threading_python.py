import threading
import time

def update_db():
    print("updating db....")
    time.sleep(5)
    print("updated db")#updating db taking so much time so next func execution takes time ,so we use another thread to simultaneously
                       #run the another func
def display_nums(num):
    for i in range(1,num+1):
        print(i)
#update_db()
thread_db = threading.Thread(target=update_db)
thread_db.start()
display_nums(100)

print(threading.active_count())
print(threading.enumerate())# this func shows which thread is running
thread_db.join()# if any thread running it doen't print bye after finishing thread_db bye will print
print("bye")