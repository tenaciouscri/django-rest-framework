# Lesson on Django Rest Framework

This repository consists of two projects:

- *provider*
- *consumer*

These are independent from each other and don't necessarily need to be both Django projects to interact with each other.

PROVIDER = Build, expose and operate APIs.

CONSUMER = Read APIs.
__________________________________________________________________

## Important files to consult per project

PROVIDER:

- `users/serializers.py` -> Serializers (with notes)
- `users/views.py` -> Viewsets (with notes)
- `users/urls.py` -> Browsable APIs, Routers (with notes)
- `provider/settings.py` -> DRF Pagination, DRF Auth Token

CONSUMER:

- `manage.py` -> Setting port to 7000
- `users/views.py` -> Asynchronous View, Rendering APIs, Auth Token
- `users/templates/users/index.html` -> Template for API Rendering
