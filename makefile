build:
	docker build -t bastor/bundesliga-api .

push:
	docker push bastor/bundesliga-api

run_dev:
	docker run \
		--env-file=debug.env \
		-e DEBUG=false \
		--restart=always \
		--name=bundesliga-api \
		-d \
		-p 80:8000 \
		bastor/bundesliga-api

run_prod:
	docker run \
		--env-file=prod-deploy-dir/prod.env \
		--restart=always \
		--name=bundesliga-api \
		-d \
		-p 80:8000 \
		bastor/bundesliga-api

restart:
	docker restart bundesliga-api

clean:
	docker stop bundesliga-api; docker rm bundesliga-api
