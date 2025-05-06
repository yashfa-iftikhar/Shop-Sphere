FROM node:20
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN npm install -g serve
COPY . .
RUN npm run build
ENV PORT=5000
EXPOSE 5000
CMD ["serve", "-s", "dist", "-l", "5000"]