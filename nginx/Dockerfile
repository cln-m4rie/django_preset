FROM nginx:alpine

RUN apk --no-cache update && \
    apk --no-cache upgrade

RUN mkdir -p /var/www/html
RUN chown -R www-data:www-data /var/www/html