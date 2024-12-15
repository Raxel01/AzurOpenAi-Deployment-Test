COMPOSEFILE = /goinfre/abait-ta/AzurOpenAi-Deployment-Test/docker-compose.yml


up: 
	docker compose -f ${COMPOSEFILE} up --detach

stop:
	docker compose -f ${COMPOSEFILE} stop

start:
	docker compose -f ${COMPOSEFILE} start

down:
	docker compose -f ${COMPOSEFILE} down
rm:
	docker rm Litellm