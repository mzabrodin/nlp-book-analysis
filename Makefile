.PHONY: start stop

NAME = udpipe

start:
	docker start $(NAME)

stop:
	docker stop $(NAME)
