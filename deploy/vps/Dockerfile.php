# Marketing site PHP for contact form (reCAPTCHA verify + SMTP).
FROM php:8.2-fpm-alpine

RUN apk add --no-cache curl-dev \
    && docker-php-ext-install curl \
    && apk del curl-dev \
    && printf 'display_errors=Off\nlog_errors=On\nerror_reporting=E_ALL & ~E_DEPRECATED & ~E_STRICT\n' \
      > /usr/local/etc/php/conf.d/zz-contact.ini

# Rate-limit storage under assets/php/storage
RUN mkdir -p /usr/share/nginx/html/assets/php/storage/rate-limit \
    && chown -R www-data:www-data /usr/share/nginx/html/assets/php/storage

WORKDIR /usr/share/nginx/html
