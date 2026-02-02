FROM node:25 AS base

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .


FROM base AS dev
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "80"]


FROM base AS build-stage
ARG VITE_GOOGLE_CLIENT_ID
ARG VITE_HD
ENV VITE_GOOGLE_CLIENT_ID=$VITE_GOOGLE_CLIENT_ID
ENV VITE_HD=$VITE_HD

RUN echo "VITE_API_URL is: ${VITE_GOOGLE_CLIENT_ID}"

RUN npm run build


FROM nginx:1.29 AS production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]