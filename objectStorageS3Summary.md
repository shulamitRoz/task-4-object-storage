# Object Storage and S3

## Question 1: Differences between distributed storage types

There are three main types of data storage: **Object Storage**, **File Storage**, and **Block Storage**.

* **Object Storage:**

  * Stores each item as an "object" with **data + metadata + unique identifier**.
  * No folder hierarchy, making it easier to store and retrieve very large amounts of data.
  * **Advantages:** Suitable for cloud and distributed systems, scalable, no single point of failure.
  * **Disadvantages:** Less efficient for random access to very small files or frequent updates.

* **File Storage:**

  * Works with a hierarchical structure of **folders and subfolders**.
  * **Advantages:** Convenient for users and applications expecting a classic file structure.
  * **Disadvantages:** Less suitable for distributed systems, protocol limitations, and scalability challenges.

* **Block Storage:**

  * Data is stored in **separate blocks**, each with its own identifier.
  * **Advantages:** High performance for frequent read/write operations, suitable for ERP systems and databases.
  * **Disadvantages:** Less convenient for direct management, lacks rich metadata.

## Question 2: What is S3?

S3 is a service by AWS for object storage. It allows storing data efficiently and securely, with each file saved as an object with a unique identifier and metadata. The service provides management of **permissions**, **data availability**, and security, and is especially suitable for distributed systems and cloud usage.

## Question 3: What is a Bucket?

A bucket is the container where objects are stored in S3. Every object must be inside a bucket. The bucket helps organize data, manage permissions, and control data availability. It can be thought of as a main folder, but there is no true hierarchy.

## Question 4: Are there folders in S3?

S3 does not have a true folder hierarchy. What appears as folders is actually part of the object's name (key) or metadata that simulates a folder structure. Each object is stored independently, and folders are only a visual illusion.

## Question 5: Size limitations compared to a file system

In S3, each object can reach up to **5TB**, allowing efficient storage of very large amounts of data. Traditional file systems have folder and hierarchy limitations, which restrict storage and make scaling more difficult in distributed environments.

## Question 6: S3 implementations

S3 is a standard for object storage, and there are several implementations and services that follow it:

* AWS S3 – the original service from Amazon.
* MinIO – an open-source solution that can run on Docker or a local server.
* Ceph Object Storage – an open-source distributed system.
* DigitalOcean Spaces, Wasabi, Backblaze B2, Google Cloud Storage – other providers implementing the S3 standard.

All of these implementations allow distributed object storage with management of permissions, versioning, availability, and security.
