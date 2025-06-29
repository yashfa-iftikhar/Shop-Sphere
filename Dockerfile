# Stage 1: Build
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

ENV NODE_OPTIONS=--max-old-space-size=2048
RUN npm run build

# Stage 2: Serve
FROM node:20-alpine

RUN npm install -g serve

WORKDIR /app

COPY --from=builder /app/dist ./dist

ENV PORT=5000
EXPOSE 5000

CMD ["serve", "-s", "dist", "-l", "5000"]
