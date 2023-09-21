
# local
uvicorn main:app --reload

# gcloud
gcloud init

## db
```
#### ensure correct project
gcloud config set project cloud-run-install

##### initialise DB Instance (takes some time  - take a break and let it process)
gcloud sql instances create api-instance-0 \
    --project cloud-run-install \
    --database-version POSTGRES_13 \
    --tier db-f1-micro \
    --region europe-west2

Created [https://sqladmin.googleapis.com/sql/v1beta4/projects/cloud-run-install/instances/api-instance-0].
NAME            DATABASE_VERSION  LOCATION        TIER         PRIMARY_ADDRESS  PRIVATE_ADDRESS  STATUS
api-instance-0  POSTGRES_13       europe-west2-c  db-f1-micro  34.147.176.203   -                RUNNABLE

gcloud sql databases create api-db-0 \
    --instance api-instance-0
	
gcloud sql users create api-user-0 \
    --instance api-instance-0 \
    --password GJaUUsg_%RYnXVCB

#### check status of instance
gcloud sql instances describe --project cloud-run-install api-instance-0
```
## DB URL
```
# assemble link from the above info
postgres://<USER>:<PWD>@//cloudsql/<PROJECT ID>:<REGION>:<INSTANCE>/<DB>
--
postgres://api-user-0:GJaUUsg_%RYnXVCB@//cloudsql/cloud-run-install:europe-west2:api-instance-0/api-db-0
--
```

## storage bucket
```
# PROJECT: pfolio-
gcloud config set project cloud-run-install

# initialise BUCKET
gsutil mb -l europe-west2 gs://api-bucket-0
```

## service account(s)
```
PROJECT: cloud-run-install
ID: cloud-run-install

'IAM & ADMIN'->Service Accounts
api-svc@cloud-run-install.iam.gserviceaccount.com
-
edit principal
-

# add ROLES to allow access to DB & 'secrets'
--
Secret Manager Secret Accessor
Cloud SQL Admin
Storage Admin
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


## secrets setup
```
# setup local environment - TEMPORARILY
cd config

echo DATABASE_URL=postgres://api-user-0:GJaUUsg_%RYnXVCB@//cloudsql/cloud-run-install:europe-west2:api-instance-0/api-db-0 >> .env

echo SECRET_KEY=$(cat /dev/urandom | LC_ALL=C tr -dc '[:alpha:]'| fold -w 50 | head -n1) >> .env

echo GS_BUCKET_NAME=api-bucket-0 >> .env

echo FRONTEND_URL=https://frontend-live-ceclcnqauq-nw.a.run.app/ >> .env

# store in secret manager
# enable secretmanager.googleapis.com if asked
gcloud secrets create api_settings --data-file .env

gcloud secrets describe api_settings

# Grant access to the secret to the App Engine standard service account
gcloud secrets add-iam-policy-binding django_settings \
    --member serviceAccount:api-svc@cloud-run-install.iam.gserviceaccount.com \
    --role roles/secretmanager.secretAccessor
		
# test - retrieve content of 'django_settings'
gcloud secrets versions access latest --secret api_settings && echo ""

###############################
# when reseting - delete SECRET
gcloud secrets delete api_settings
-
enable Secret Mgr API if asked
-
```

