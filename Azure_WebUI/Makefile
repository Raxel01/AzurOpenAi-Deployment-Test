COMPOSEFILE = /goinfre/abait-ta/AzurOpenAi-Deployment-Test/Azure_WebUI/docker-compose.yml


up: 
	docker compose -f ${COMPOSEFILE} up --detach

stop:
	docker compose -f ${COMPOSEFILE} stop

start:
	docker compose -f ${COMPOSEFILE} start

down:
	docker compose -f ${COMPOSEFILE} down

re  : prune up

clean:
	@docker stop $$(docker ps -qa) || true
	@docker rm -f $$(docker ps -qa) || true
	@docker rmi -f $$(docker images -qa) || true
	@docker volume rm -f $$(docker volume ls -q) || true
	@docker network rm $$(docker network ls -q) || true

prune: clean
	@docker system prune -a --volumes -f