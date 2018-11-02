# DecentWorkWeb
Project for creating profiles, register work, get job.

## Installation

### Prerequisites

```
python 3.6
node v10.0
npm v6.4.1
```

### VirtualEnv
```
source env/bin/activate
pip install -r requirements/local.txt
```

### JavaScript
```
npm install
```

### Database

Copy `decentwork/settings/db.py.base` to `decentwork/settings/db.py` and
```
./manage.py migrate
```