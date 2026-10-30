# Chuck 的个人主页 · 水墨风

纯静态页面，无构建步骤，可直接部署：

- `index.html`：主页（首屏、近作、关于、联系）+ 三个项目的「画卷」弹窗
- `styles.css`：全部样式；顶部 `:root` 是配色变量（宣纸 / 墨 / 朱砂 / 黛青）
- `404.html`：Notion 链接暂时指向这里；GitHub Pages 也会把它当作站点 404
- `assets/`：项目截图
  - `matchedge-1-assistant.png` / `matchedge-2-analysis.png` / `matchedge-3-dashboard.png`：足彩分析 Agent
  - `kezhan-downloader.png`：课栈 · 小鹅通下载器

视觉效果全部用 CSS + 内联 SVG 滤镜实现（`#bleed` 墨迹晕染、`#rough` 印章残边、`#ridge` 远山轮廓），
字体来自 Google Fonts（Ma Shan Zheng / Noto Serif SC / Cormorant Garamond）。

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

## 常改的地方

- Notion 页面上线后：把 `index.html` 联系区里的 `./404.html` 换成真实链接。
- 新增项目：复制 `.works` 里的一个 `<article class="work">`，再复制一个对应的 `<dialog class="scroll">`，
  两者用 `data-open="dlg-xxx"` / `id="dlg-xxx"` 关联。
- 换配色：改 `styles.css` 顶部 `:root` 变量。
