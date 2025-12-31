from minio import Minio
import random
import string
from io import BytesIO

#התחברות ללקוח
client = Minio(
    "localhost:9000",
    access_key="admin",
    secret_key="password123",
    secure=False
)
#יצירת דלי
bucket_name = "mybucket"

if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)
    print(f"Bucket '{bucket_name}' created.")
else:
    print(f"Bucket '{bucket_name}' already exists.")

#יצירת אוביקט אקראי עם תוכן אקראי
object_name = ''.join(random.choices(string.ascii_lowercase, k=8)) + ".txt"
data = ''.join(random.choices(string.ascii_letters + string.digits, k=20)).encode('utf-8')

client.put_object(
    bucket_name,
    object_name,
    BytesIO(data),
    length=len(data)    # אורך התוכן
)
print(f"Created object: {object_name}")

print(f"Objects in bucket '{bucket_name}':")
for obj in client.list_objects(bucket_name):
    print(obj.object_name)

    #פונקציה שקוראת את התוכן של האוביקט האחרון שנוצר
def read_last_object(client, bucket_name):
    objects = list(client.list_objects(bucket_name))
    
    if not objects:
        print("No objects found in the bucket.")
        return
    
    last_object = objects[-1].object_name
    
    response = client.get_object(bucket_name, last_object)
    data = response.read().decode('utf-8')
    response.close()
    response.release_conn()
    
    print(f"Data in the last object '{last_object}': {data}")
    return data

#read_last_object(client,bucket_name)

#פונקציה שמוחקת את האוביקט האחרון שנוצר
def delete_last_object(client, bucket_name):
    objects = list(client.list_objects(bucket_name))

    if not objects:
        print("No objects to delete.")
        return

    last_object = objects[-1].object_name

    client.remove_object(bucket_name, last_object)
    print(f"Deleted object: {last_object}")

delete_last_object(client,bucket_name)

def update_last_object(client, bucket_name):
    objects = list(client.list_objects(bucket_name))

    if not objects:
        print("No objects to update.")
        return

    last_object = objects[-1].object_name

    new_data = b"Updated content of the object"

    client.put_object(
        bucket_name,
        last_object,
        BytesIO(new_data),
        length=len(new_data)
    )

    print(f"Updated object: {last_object}")

#update_last_object(client, bucket_name)
#read_last_object(client,bucket_name)
