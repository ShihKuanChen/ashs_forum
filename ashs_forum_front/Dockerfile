FROM node:25 AS base

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .


FROM base AS dev
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]


FROM base AS build-stage
RUN npm run build


FROM nginx:1.29 AS production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]