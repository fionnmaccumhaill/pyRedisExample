# Set the base image to Ubuntu
FROM        redis:latest

# File Author / Maintainer
MAINTAINER Edward Foley

COPY redis.conf /usr/local/etc/redis/redis.conf
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]

# Expose Redis port 6379
EXPOSE      6379
