from my_celery import app, add
import time

results = []

# Submit jobs for execution
for i in range(10):
    async_result = add.delay(0,i) 
    results.append(async_result)


# print status of the tasks
for res in results:
    print(res.id, res.status, res.result)
print('\n')

# Wait for completion of tasks
while not all(map(lambda res: res.ready(), results)):
    print('waiting for tasks to complete')
    time.sleep(2)
print('\n')

# print status of tasks
for res in results:
    print(res.id, res.status, res.result)