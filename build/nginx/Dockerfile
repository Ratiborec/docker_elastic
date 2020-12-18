FROM nginx:latest
RUN rm /etc/nginx/conf.d/default.conf
COPY kibana.conf /etc/nginx/conf.d/kibana.conf
RUN sed -i 's/localhost:5601/'"$KIBANA_HOST"'/' /etc/nginx/conf.d/kibana.conf
