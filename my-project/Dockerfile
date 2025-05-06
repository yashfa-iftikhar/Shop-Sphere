# Frontend Dockerfile for Vite on port 5000
FROM node:18

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 5000

ENV VITE_BACKEND_URL=http://server:3000

CMD ["npm", "run", "dev", "--", "--host", "--port", "5000"]
