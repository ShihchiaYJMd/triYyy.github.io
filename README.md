# 彩色水粉风个人主页

这个目录已经是一个可直接部署的静态主页：

- `index.html`
- `styles.css`

## 本地预览

在当前目录执行：

```bash
python3 -m http.server 8080
```

打开 `http://localhost:8080`。

## 部署到 GitHub Pages（推荐）

1. 在 GitHub 新建仓库（例如：`yourname.github.io`）。
2. 把当前目录文件推送到仓库默认分支：

```bash
git init
git add .
git commit -m "init homepage"
git branch -M main
git remote add origin git@github.com:yourname/yourname.github.io.git
git push -u origin main
```

3. 到仓库 `Settings -> Pages`，`Build and deployment` 选择：
   - Source: `Deploy from a branch`
   - Branch: `main` + `/ (root)`
4. 等待 1-3 分钟后访问：`https://yourname.github.io`

## Notion 方案（更快但自定义弱）

1. 在 Notion 新建页面，粘贴你的头像、简介、项目卡片、联系方式。
2. 点击页面右上角 `Share`，开启 `Publish`。
3. 可直接使用 Notion 链接，或绑定工具：
   - [Super](https://super.so)
   - [Potion](https://potion.so)
4. 这两个工具可把 Notion 页面套上更好看的主题和自定义域名。

## 你需要改的内容

- `index.html` 里的名字、文案、链接（Email/GitHub/Notion）。
- 项目区 `Project A/B/C` 改成你的真实项目。
- 想换配色可在 `styles.css` 顶部 `:root` 调整颜色变量。
