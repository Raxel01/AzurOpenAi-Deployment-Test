up: 
	docker compose up --detach

stop:
	docker compose stop

start:
	docker compose start

down:
	docker compose down

clear:
	@clear
re  : clear prune clear up

clean:
	@docker stop $$(docker ps -qa) || true
	@docker rm -f $$(docker ps -qa) || true
	@docker rmi -f $$(docker images -qa) || true
	@docker volume rm -f $$(docker volume ls -q) || true
	@docker network rm $$(docker network ls -q) || true

prune: clean
	@docker system prune -a --volumes -f