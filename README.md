# DecentWorkWeb
Project for creating profiles, register work, get job.

## Prerequisites

```
python 3.6
node v10.0
npm v6.4.1
```

## Installation

### VirtualEnv
```
source env/bin/activate
pip install -r requirements/local.txt
```

### Install JavaScript packages:
```
npm install
```

### Build JavaScript
```
npm run build
```

### Watch
```
npm run watch
```

### Database
Copy `decentwork/settings/db.py.base` to `decentwork/settings/db.py` and
```
./manage.py migrate
```

### Google Sign In
To install Google sign in you have to find google_credentials.json in decentwork/fixtures and
enter your client id and secret key from Google OAuth client API and then do
```
./manage.py loaddata decentwork/fixtures/google_credentials.json
```

### Other fixtures
Installing other fixtures needed for application to work
```
./manage.py loaddata cities professions
```
