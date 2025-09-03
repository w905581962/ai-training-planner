# 🚴‍♂️ AI驱动的自行车训练计划生成器

一个智能的自行车训练计划生成器，使用AI技术为骑行者创建个性化的训练计划，并自动上传到intervals.icu平台。

## ✨ 特性

- 🤖 **AI驱动**: 使用GPT-4生成科学、个性化的训练计划
- 📅 **自动上传**: 直接上传到intervals.icu日历
- 📊 **智能分析**: 根据当前FTP自动调整功率区间
- 🏆 **多目标支持**: 支持FTP提升、耐力建设、比赛准备等目标
- 🎯 **周期化训练**: 遵循科学的训练周期化原理
- 💻 **现代界面**: 响应式Web界面，支持移动设备
- 🔒 **安全可靠**: 使用HTTPS加密，API密钥安全存储

## 🏗️ 技术架构

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React前端     │────│   FastAPI后端   │────│   OpenAI GPT-4  │
│  (TypeScript)   │    │    (Python)     │    │      (LLM)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       
         │              ┌─────────────────┐              
         └──────────────│   Intervals.icu │              
                        │      API        │              
                        └─────────────────┘              
```

### 核心技术栈

- **前端**: React 18 + TypeScript + Chakra UI + Vite
- **后端**: FastAPI + Python 3.11 + Pydantic
- **AI**: OpenAI GPT-4 (通过LiteLLM)
- **部署**: Docker + Docker Compose + Traefik
- **集成**: Intervals.icu API

## 🚀 快速开始

### 方法1: 一键部署 (推荐)

```bash
# 下载快速部署脚本
wget https://raw.githubusercontent.com/your-repo/ai-training-planner/main/setup.sh

# 给予执行权限并运行
chmod +x setup.sh
./setup.sh
```

### 方法2: 手动部署

1. **克隆项目**
```bash
git clone https://github.com/your-repo/ai-training-planner.git
cd ai-training-planner
```

2. **配置环境变量**
```bash
cp .env.template .env
nano .env  # 编辑配置
```

3. **启动服务**
```bash
docker-compose up -d
```

4. **测试部署**
```bash
chmod +x test_deployment.sh
./test_deployment.sh
```

### 环境变量配置

在`.env`文件中设置以下变量：

```env
# 必需配置
OPENAI_API_KEY=sk-your-openai-api-key-here
DOMAIN=yourdomain.com
EMAIL=your-email@example.com

# 可选配置
LITELLM_MODEL=openai/gpt-4o
```

## 📖 使用指南

### 1. 获取API密钥

**OpenAI API密钥**:
1. 访问 [OpenAI Platform](https://platform.openai.com/)
2. 创建账户并获取API密钥
3. 确保账户有足够的使用额度

**Intervals.icu API密钥**:
1. 登录您的intervals.icu账户
2. 前往 Settings → Developer
3. 生成新的API密钥

### 2. 生成训练计划

1. 访问您的部署网站
2. 输入intervals.icu运动员ID和API密钥
3. 选择训练目标（FTP提升、耐力等）
4. 设置训练参数（周数、天数、时间）
5. 点击"生成并上传计划"

### 3. 查看结果

- 生成的计划会自动显示在网页上
- 同时上传到您的intervals.icu日历
- 可以在Zwift等软件中直接使用.zwo文件

## 🛠️ 开发指南

### 开发环境设置

```bash
# 启动开发环境
docker-compose -f docker-compose.dev.yml up

# 或者本地开发
cd backend && pip install -r requirements.txt
cd frontend && npm install

# 分别启动前后端
uvicorn app.main:app --reload  # 后端
npm run dev                    # 前端
```

### 项目结构

```
ai-training-planner/
├── backend/                 # FastAPI后端
│   ├── app/
│   │   ├── main.py         # 应用入口
│   │   ├── models/         # 数据模型
│   │   ├── services/       # 业务逻辑
│   │   └── api/            # API端点
│   └── Dockerfile
├── frontend/               # React前端
│   ├── src/
│   │   ├── components/     # React组件
│   │   └── App.tsx        # 主应用
│   └── Dockerfile
├── docker-compose.yml     # 生产环境
├── docker-compose.dev.yml # 开发环境
└── docs/                  # 文档
```

### API端点

- `GET /` - 健康检查
- `POST /api/v1/generate-and-upload` - 生成并上传训练计划
- `GET /api/docs` - API文档 (Swagger UI)

## 🔧 运维指南

### 查看日志
```bash
# 查看所有服务日志
docker-compose logs -f

# 查看特定服务
docker-compose logs backend
docker-compose logs frontend
```

### 更新应用
```bash
# 拉取最新代码
git pull

# 重新构建并部署
docker-compose down
docker-compose up -d --build
```

### 备份配置
```bash
# 备份环境配置
cp .env .env.backup-$(date +%Y%m%d)

# 备份SSL证书
tar -czf ssl-backup-$(date +%Y%m%d).tar.gz letsencrypt/
```

### 监控和故障排除

1. **服务状态检查**
```bash
docker-compose ps
```

2. **端口检查**
```bash
netstat -tlnp | grep -E "(80|443|8000)"
```

3. **磁盘空间**
```bash
df -h
docker system df
```

4. **性能监控**
```bash
docker stats
htop
```

## 🔒 安全说明

- ✅ HTTPS加密传输
- ✅ API密钥安全存储
- ✅ CORS跨域保护
- ✅ 输入数据验证
- ⚠️ 生产环境请限制Traefik仪表板访问
- ⚠️ 定期更新依赖包和基础镜像

## 🤝 贡献指南

欢迎贡献！请遵循以下流程：

1. Fork项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

### 代码规范

- Python: 遵循PEP 8
- TypeScript: 使用ESLint配置
- 提交信息: 使用常规提交格式

## 📝 更新日志

### v1.0.0 (2024-09-03)
- ✨ 初始版本发布
- 🤖 AI训练计划生成
- 📅 Intervals.icu集成
- 🐳 Docker部署支持

### 计划功能
- [ ] 支持更多LLM提供商 (Claude, Gemini)
- [ ] 训练历史分析
- [ ] 社区分享功能
- [ ] 移动应用
- [ ] 多语言支持

## 📄 许可证

本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件

## 🆘 支持

如遇问题，请通过以下方式获取帮助：

- 📧 邮件: support@example.com
- 🐛 Bug报告: [GitHub Issues](https://github.com/your-repo/ai-training-planner/issues)
- 💬 讨论: [GitHub Discussions](https://github.com/your-repo/ai-training-planner/discussions)

## ⭐ 致谢

感谢以下开源项目：
- [FastAPI](https://fastapi.tiangolo.com/) - 现代Python API框架
- [React](https://reactjs.org/) - 用户界面库
- [Chakra UI](https://chakra-ui.com/) - 简洁的组件库
- [LiteLLM](https://litellm.ai/) - 统一的LLM API接口
- [Traefik](https://traefik.io/) - 现代反向代理

---

<p align="center">
  <b>🚴‍♂️ 让AI成为您的专属骑行教练！</b>
</p>
