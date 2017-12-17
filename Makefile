build-local:
	docker-compose -f docker-compose.yml -f docker-compose.override.yml -f docker-compose.local.yml build

local:
	docker-compose -f docker-compose.yml -f docker-compose.override.yml -f docker-compose.local.yml up
