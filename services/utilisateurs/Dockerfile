FROM php:7.4-apache
RUN docker-php-ext-install mysqli
RUN if ! pecl list | grep -q redis; then \
    pecl install redis && docker-php-ext-enable redis; \
    fi
COPY index.php /var/www/html/
EXPOSE 80