up: 
	docker compose up --detach
	bash health_populate.sh

stop:
	docker compose stop

start:
	docker compose start

down:
	docker compose down

re  : prune up

clean:
	@docker stop $$(docker ps -qa) || true
	@docker rm -f $$(docker ps -qa) || true
	@docker rmi -f $$(docker images -qa) || true
	@docker volume rm -f $$(docker volume ls -q) || true
	@docker network rm $$(docker network ls -q) || true

prune: clean
	@docker system prune -a --volumes -f