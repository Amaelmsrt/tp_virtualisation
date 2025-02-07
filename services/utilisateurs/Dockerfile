FROM php:7.4-apache
RUN docker-php-ext-install mysqli
RUN pecl install redis && docker-php-ext-enable redis
COPY index.php /var/www/html/
EXPOSE 80