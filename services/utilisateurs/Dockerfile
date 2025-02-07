FROM php:7.4-apache
COPY index.php /var/www/html/
RUN docker-php-ext-install mysqli
RUN pecl install redis && docker-php-ext-enable redis
EXPOSE 80