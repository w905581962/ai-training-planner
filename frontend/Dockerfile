# 阶段 1: 构建 React 应用
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# 阶段 2: 使用 Nginx 托管静态文件
FROM nginx:stable-alpine
# 从构建阶段复制优化后的静态文件到 Nginx 的 Web 根目录
COPY --from=build /app/dist /usr/share/nginx/html
# 如果需要，可以复制自定义的 nginx 配置
# COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]