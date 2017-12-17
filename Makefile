build-local:
	docker-compose -f docker-compose.yml -f docker-compose.override.yml -f docker-compose.local.yml build

local:
	docker-compose -f docker-compose.yml -f docker-compose.override.yml -f docker-compose.local.yml up

show_urls:
	docker-compose -f docker-compose.yml -f docker-compose.override.yml -f docker-compose.local.yml run --rm imaginarium python manage.py show_urls

manage:
	docker-compose -f docker-compose.yml -f docker-compose.override.yml -f docker-compose.local.yml run --rm imaginarium python manage.py $(command)
