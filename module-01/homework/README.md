## Question 1. Understanding Docker images
What's the version of pip in the image?
- 25.3
- 24.3.1
- 24.2.1
- 23.3.1

**Ans**: 25.3
```
docker run -it --entrypoint bash python:3.13
root@4a682835d322:/# pip --version
pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)

```

## Question 2: Understanding Docker Networking and docker-compose
Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?
```
services:
  db:
    container_name: postgres
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: 'postgres'
      POSTGRES_PASSWORD: 'postgres'
      POSTGRES_DB: 'ny_taxi'
    ports:
      - '5433:5432'
    volumes:
      - vol-pgdata:/var/lib/postgresql/data

  pgadmin:
    container_name: pgadmin
    image: dpage/pgadmin4:latest
    environment:
      PGADMIN_DEFAULT_EMAIL: "pgadmin@pgadmin.com"
      PGADMIN_DEFAULT_PASSWORD: "pgadmin"
    ports:
      - "8080:80"
    volumes:
      - vol-pgadmin_data:/var/lib/pgadmin

volumes:
  vol-pgdata:
    name: vol-pgdata
  vol-pgadmin_data:
    name: vol-pgadmin_data
```
- postgres:5433
- localhost:5432
- db:5433
- postgres:5432
- db:5432

**Ans**: postgres:5432


## Question 3. Counting short trips
For the trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive of the upper bound), how many trips had a trip_distance of less than or equal to 1 mile?
- 7,853
- 8,007
- 8,254
- 8,421

**Ans**: 8007

#### SQL Query:
```SQL
SELECT COUNT(*) as num_of_trips
FROM green_trip
WHERE trip_distance <= 1.0
AND lpep_pickup_datetime >= '2025-11-01'
AND lpep_pickup_datetime < '2025-12-01';
```

## Question 4. Longest trip for each day
Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles (to exclude data errors).

Use the pick up time for your calculations.
- 2025-11-14
- 2025-11-20
- 2025-11-23
- 2025-11-25

**Ans**: 2025-11-14

#### SQL Query:
```SQL
SELECT DATE(lpep_pickup_datetime), trip_distance
FROM green_trip
WHERE trip_distance <100.0
ORDER BY trip_distance DESC
LIMIT 1;
```

## Question 5. Biggest pickup zone
Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?
- East Harlem North
- East Harlem South
- Morningside Heights
- Forest Hills

**Ans**: East Harlem North

#### SQL Query:
```SQL
SELECT 
tz.Zone,SUM(gt.total_amount) as total
FROM green_trip AS gt
INNER JOIN taxi_zone_lookup AS tz
ON gt.pulocationid = tz.locationid
AND DATE(gt.lpep_pickup_datetime) = '2025-11-18'
GROUP BY tz.zone
ORDER BY SUM(gt.total_amount) DESC
LIMIT 1;
```

## Question 6. Largest tip
For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?
- JFK Airport
- Yorkville West
- East Harlem North
- LaGuardia Airport

**Ans**: Yorkville West

#### SQL Query:
```SQL
SELECT
ptz.zone as pickup_zone,
dtz.zone as dropoff_zone,
gt.tip_amount as large_total_tip
FROM green_trip AS gt
INNER JOIN taxi_zone_lookup AS ptz
ON gt.pulocationid = ptz.locationid
INNER JOIN taxi_zone_lookup AS dtz
ON gt.dolocationid = dtz.locationid
WHERE EXTRACT(MONTH FROM gt.lpep_pickup_datetime) = 11
AND EXTRACT(YEAR FROM gt.lpep_pickup_datetime) = 2025
AND ptz.zone = 'East Harlem North'
ORDER BY gt.tip_amount DESC
LIMIT 1;
```

## Question 7. Terraform Workflow
Which of the following sequences, respectively, describes the workflow for:
1. Downloading the provider plugins and setting up backend,
2. Generating proposed changes and auto-executing the plan
3. Remove all resources managed by terraform`

Answers:
- terraform import, terraform apply -y, terraform destroy
- teraform init, terraform plan -auto-apply, terraform rm
- terraform init, terraform run -auto-approve, terraform destroy
- terraform init, terraform apply -auto-approve, terraform destroy
- terraform import, terraform apply -y, terraform rm

**Ans**: terraform init, terraform apply -auto-approve, terraform destroy