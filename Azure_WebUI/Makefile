COMPOSEFILE = /goinfre/abait-ta/AzurOpenAi-Deployment-Test/Azure_WebUI/docker-compose.yml


up: 
	docker compose -f ${COMPOSEFILE} up --detach

stop:
	docker compose -f ${COMPOSEFILE} stop

start:
	docker compose -f ${COMPOSEFILE} start

down:
	docker compose -f ${COMPOSEFILE} down

re  : stop rm up

rm:
	docker rm azureWebUI
	docker rmi azure:abait-ta