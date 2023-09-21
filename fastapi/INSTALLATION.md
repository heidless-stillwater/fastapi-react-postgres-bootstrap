# gcloud sql instance create
https://cloud.google.com/sdk/gcloud/reference/sql/instances/create

--root-password=ROOT_PASSWORD] [--[no-]storage-auto-increase]

# local
uvicorn app.main:app --reload

uvicorn main:app --reload

# db
```
# ensure correct project
gcloud config set project cloud-run-install
```

```
# initialise DB Instance (takes some time  - take a break and let it process)
gcloud sql instances create bootstrap-instance-0 \
    --project cloud-run-install \
    --database-version POSTGRES_15 \
    --tier db-f1-micro \
    --region europe-west2

postgres
havana11

Created [https://sqladmin.googleapis.com/sql/v1beta4/projects/cloud-run-install/instances/bootstrap-instance-0].
NAME                  DATABASE_VERSION  LOCATION        TIER         PRIMARY_ADDRESS  PRIVATE_ADDRESS  STATUS
bootstrap-instance-0  POSTGRES_15       europe-west2-c  db-f1-micro  35.242.140.91    -                RUNNABLE

gcloud sql databases create bootstrap-db-0 \
    --instance bootstrap-instance-0

gcloud sql users create bootstrap-user-0 \
    --instance bootstrap-instance-0 \
    --password GJaUUsg_%RYnXVCB
```

## db url
postgres://bootstrap-user-0:GJaUUsg_%RYnXVCB@//cloudsql/cloud-run-install:europe-west2:bootstrap-instance-0/bootstrap-db-0

## service account(s)
```
PROJECT: cloud-run-install
ID: cloud-run-install

'IAM & ADMIN'->Service Accounts
bootstrap-svc@cloud-run-install.iam.gserviceaccount.com
-
edit principal
-

# add ROLES to allow access to DB & 'secrets'
--
Cloud SQL Admin
--
```

generate & install KEY file
```
'IAM & ADMIN'->Service Accounts->'3 dots'->Manage Keys
'ADD KEY'->JSON
# Download & install json file
' copy to local project/app directory'
/home/heidless/LIVE/pfolio/WORKING/backend-LIVE-WORKING/app/config
```
# pgadmin4
tut:
https://cshiva.medium.com/connecting-to-gcps-cloud-sql-postgressql-from-pgadmin-3-simple-steps-2f4530488a4c

use local pgadmin4
http://localhost/pgadmin4

```
INSTANCE
bootstrap-instance-0
PWD:
havana11

USER
postgres
havana11

bootstrap-user-0
GJaUUsg_%RYnXVCB
```