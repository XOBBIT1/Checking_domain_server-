FROM node:14.17.3 as base

WORKDIR /domain_ping/front

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN npm install

EXPOSE 3000

COPY ./front/my-react-app ./

CMD ["npm", "start"]