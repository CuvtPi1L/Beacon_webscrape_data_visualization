FROM node:20-alpine3.18 

WORKDIR /app
COPY package.json .
RUN npm i 
COPY . .
EXPOSE 8080
CMD [ "npm","run" ,"dev"]






