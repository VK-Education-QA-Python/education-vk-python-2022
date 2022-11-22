FROM centos:7

RUN yum update -y
RUN yum install epel-release -y
RUN yum install nginx -y

ADD nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]