# HCRS@WWW 2027 网站改造说明（交接文档）

> **给执行方**：本文档说明如何基于 2026 年站点改造出 2027 年（第 3 届）workshop 官网。
> 站点与仓库已由组织者建好，**本文档只涉及页面内容与页面实现**，不涉及仓库创建、Pages 配置等部署事项。
> 文档内容自足，不需要额外阅读 proposal。凡标注「**需确认**」的地方，请先找组织者确认，**不要自行编造**。
> 改完请对照配套的《自查清单》逐项核对。
> 最后更新：2026-09-21

---

## 0. 任务概览

| 项 | 内容 |
|---|---|
| 站点地址 | https://hcrs2027.github.io/ （**URL 不可更改**，已写进提交给会议的 proposal） |
| 页面模板 | 以 2026 年第 2 届站点为模板：https://hcrec.github.io/ ，页面文件可从 https://github.com/HCRec/HCRec.github.io 取得（纯静态 HTML） |
| 会议 | The Web Conference 2027（ACM Web 2027），2027-05-03 ~ 05-07，爱尔兰都柏林 |
| Workshop 形态 | **全日（full-day）、线下（in-person）** |
| 沿用板块 | 与 2026 一致，共 6 个页面：Home / CfP / Committee / Program / Accepted Papers / Keynote（+ 导航 Previous 下拉） |
| 保留设计 | 2026 的版式、配色（`#2d4a6b` 深蓝 + `#C6743B` 橙）、`css/` `js/` `fonts/` 全部沿用 |

### 时间线：页面内容该在什么时候变成什么样

| 时间 | 里程碑 | 页面要做什么 |
|---|---|---|
| 2026-10-12 | proposal 结果通知 | 收到接收通知后：去掉 `noindex`、放上三个投稿 deadline、首页横幅切成 "Call for Papers" |
| 2027-01-04 | 论文投稿截止 | 首页横幅切换为 "Submission closed / under review" |
| 2027-02-01 | 论文录用通知 | 填充 Accepted Papers 页；Keynote 页补 title/abstract；公布 Best Paper |
| 2027-02-16 | Camera-ready 截止 | 更新（如有） |
| 2027-05-03 ~ 05-07 | 会议 | Program 定稿（具体日期、时段、oral 顺序） |

> ⚠️ **接收前（10-12 之前）**：如果站点已经公开可访问，建议先加 `<meta name="robots" content="noindex">`，并且**先不要写三个投稿 deadline**。proposal 结果 10-12 才出，接收之前公开宣传截止日期有风险。

---

## 1. 全站统一替换（最容易漏，先做这一步）

2026 站是 6 个独立 HTML 文件，**导航栏和 footer 在每个文件里各复制了一份**，同一个字符串全站出现十几处。手工改必漏，建议先写脚本批量替换，再逐页人工检查。

### 必须替换的字符串

| 2026 站上的内容 | 2027 改成 |
|---|---|
| `The 2nd Workshop on Human-Centered Recommender Systems` | `The 3rd Workshop on Human-Centered Recommender Systems` |
| `HCRS@TheWebConf 2026`（navbar brand、footer、`<meta name="author">`） | `HCRS@WWW 2027` |
| `@TheWebConf 2026` | `@The Web Conference 2027` |
| `half-day session` / `half-day` | `full-day session` |
| `held online` / `meeting link to be announced` | `held in person` / 删除 |
| `Tuesday, June 30, 2026, 10:00–13:30` | 见第 4.4 节（**具体日期未定，不要编**） |
| `GST (UTC+4)` / `Gulf Standard Time` | `IST (Irish Standard Time, UTC+1)` |
| `January 14, 2026`（notification） | `February 1, 2027` |
| `February 2, 2026`（camera-ready） | `February 16, 2027` |
| `January 4, 2026`（submission） | `January 4, 2027`（只改年份，日期不变） |
| `ACM WWW 2026 template` | `ACM Web Conference 2027 template` |
| `Two 30-minute keynote talks` | `Four 30-minute keynote talks` |
| `https://openreview.net/group?id=ACM.org/TheWebConf/2026/Workshop/HCRS` | 2027 的 OpenReview group（**可能尚未建立，先写 TBA**，绝对不要留 2026 链接） |
| hero 图 `https://www2026.thewebconf.org/images/Large-DubaiSkyline_BurjKhalifa_DET.jpg` | 自托管的都柏林/爱尔兰相关图片（见第 6.3 节） |

### ⚠️ 连带注意

- **4 个日期里只有 3 个换月**：submission 是 1 月 4 日不变、只改年；notification 从 1 月 14 日变 2 月 1 日；camera-ready 从 2 月 2 日变 2 月 16 日。
- **不要写 "TheWebConf 2027"**：会议官方品牌是 `ACM Web 2027` / `The Web Conference 2027`。全站统一用简称 `HCRS@WWW 2027` + 全称 `The 3rd Workshop on Human-Centered Recommender Systems`。
- 主题名统一写法：`Agency` / `Alignment` / `Long-term Value`（第三个词 `Value` 首字母大写）。
- 改完后必须跑关键词校验（见配套《自查清单》A 节）。

---

## 2. 必须删除的 2026 残留

| # | 位置 | 内容 | 处理 |
|---|---|---|---|
| 1 | 首页顶部横幅 + `papers.html` | `🎉 Accepted Papers Announced!`、`6 oral / 7 poster`、Best Paper 得主 **"RecoWorld: Building Simulated Environments for Agentic Recommender Systems"** 及其颁奖词 | **全部删除**。2027 尚无结果。首页横幅改为 Call for Papers 招募（见第 4.7 节） |
| 2 | 所有页面 `<head>` | `<meta name="google-site-verification" content="-BynJeLAbljne-NSEGWSpl2dwG65n6AZ9O-2TKPtAuo">` | 删除。这是 hcrec.github.io 的验证码，对新域名无效 |
| 3 | 所有页面 `<head>` | `<!--[if lt IE 9]><script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->` | 删除（http 混合内容 + 服务已停） |
| 4 | 首页 | 注释掉的 `<div class="row">` 里那块 "📢 Reviewer Nomination Open!" 横幅，含一个 2026 的 Google Form 链接 | 连同注释一起删除 |
| 5 | 首页 | 注释掉的 `<!-- Reviewer Nomination -->` 内容区块（同一个 Google Form） | 连同注释一起删除 |
| 6 | `papers.html` | 2026 的 13 篇论文（6 oral + 7 poster）及其 OpenReview / PDF 链接 | 全部清空，改成一句"待 2027-02-01 通知后公布" |
| 7 | `program.html` | `Oral Presentation Order` 表（2026 的 6 篇 oral 及时间） | 删除或改成占位（2027 论文未定） |
| 8 | `committee.html` / 首页 | Julian McAuley、Lina Yao、Du Su、Yue Feng 四人 | 删除（都不是 2027 组织者） |
| 9 | `committee.html` / 首页 | `Student Organizers` 整块（Shixuan Zhang、Kaike Zhang、Jiakai Tang） | **删除该分类**（2027 没有这个类别；Jiakai Tang 改列到 Organizing Committee） |
| 10 | `keynote.html` | 两位 2026 keynote：Li Chen、Zhaochun Ren | 删除。**注意：这两位 2027 是组织者，不是 keynote**，不要顺手沿用 |

---

## 3. 逐页修改说明

### 3.1 Home（`index.html`）

2026 首页结构：Hero → 顶部横幅 → Overview → Important Dates → Workshop Objectives → Call for Papers → Best Paper Award 框 → Submission Guidelines → Program Highlights → Organizing Committee → Student Organizers。

| 位置 | 需要做什么 |
|---|---|
| Hero | 换图；标题改 `The 3rd Workshop<br>on Human-Centered Recommender Systems` + `@The Web Conference 2027` |
| 顶部横幅 | 改成 CfP 招募横幅（接收后启用，见第 4.7 节文案） |
| Overview | 整段重写，用第 4.1 节英文原文 |
| Important Dates | 用第 4.4 节内容 |
| Workshop Objectives | 用第 4.5 节内容 |
| **Call for Papers（四项主题）** | **最大改动**：2026 的 Human Understanding / Human Involvement / Human Impact / Emerging Cross-Domain **整段删除**，换成第 4.2 节的三主题 Agency / Alignment / Long-term Value |
| Best Paper Award 框 | 删掉得主信息，或改成一句 "A Best Paper Award will be presented at the workshop." |
| Submission Guidelines | 用第 4.6 节内容（注意长度表述与投稿政策的注意事项） |
| Program Highlights | 改成 full-day + four keynotes + paper sessions + **poster session** + panel discussion |
| Organizing Committee | 换成 2027 的 9 人（第 4.8 节）。**建议首页只放缩略或一个链接指向 Committee 页**，避免两处维护不一致 |
| Student Organizers | 删除 |
| 新增 | 联系方式（footer）、可选 "Previous editions" 入口、可选 D&I 说明段 |
| `<head>` | `description` 目前是空的 → 必须填；补 `og:title` / `og:description` / `og:image`，方便微信/Twitter 分享 |

### 3.2 CfP（`cfp.html`）

1. **Topics of Interest 整段重写**（第 4.2 节）。
2. ⚠️ **删除这句**（2026 有，2027 不能有）：
   > We encourage in-person participation, but remote presentation options will be available for authors who cannot attend in person.
   WWW 2027 官方明文 "Workshops are in-person events"，照抄会与会议政策冲突。
3. ⚠️ **不要照抄 2026 的出版政策**。2026 写的是"已发表工作也欢迎投稿，只是不进 companion proceedings"；WWW 2027 官方口径更严：
   > Papers accepted by a workshop can be included in the Companion Proceedings of the Web Conference 2027, subject to meeting the camera-ready timeline. Workshop papers that have been previously published or are under review for another journal, conference or workshop should not be considered for publication but can be presented in a non-archival workshop.
   处理方式：按上面官方口径重写，或**先不写该段**，等 workshop chair 确认。见第 5.2 节。
4. Paper Format 里 `\setcopyright{none}`、CCS/关键词可选可保留，模板年份改 2027。
5. 长度表述统一成：`4–8 pages, with unlimited pages allowed for references`（2026 那句 "up to 4 additional pages for references and appendix…" 与 proposal 口径不同，替换掉）。
6. Important Dates 换 2027（第 4.4 节）。
7. OpenReview 链接改 2027 group 或写 TBA。
8. 页脚 / 页面里所有 "2nd"、"2026" 清干净。

### 3.3 Committee（`committee.html`）

1. **Organizing Committee 从 7 人换成 9 人**（第 4.8 节）。照片裁成 200×200 圆形（2026 CSS 已固定 `border-radius:50%` + `object-fit:cover`，照抄即可）。
2. **新增 `Program Committee` 区块**。proposal 里有 17 人名单（第 4.9 节），但 **2026 站从来没有这个分类**，需要新建。
3. **删除 `Student Organizers` 分类**。
4. ⚠️ 名单纪律：
   - 只列**同意公开姓名**的人，未确认的不要列；
   - PC 建议只列姓名 + 单位，**不要放邮箱**；
   - proposal 里 PC 名单**没有单位**，需先向组织者收集齐，否则页面上会是一列光秃秃的名字；
   - 组织者链接请核实是否有效，**不要留 2026 的死链**；找不到主页的人宁可不加 `<a>`。

### 3.4 Program（`program.html`）

1. 页面顶部描述改：`full-day session`、`in person`、会期 `May 10–14, 2027, Dublin, Ireland`，**具体日期和时段标注 TBA / Tentative**。
2. 时区标签从 `GST (UTC+4)` 改为 `IST (Irish Standard Time, UTC+1)`。⚠️ **"IST" 有三个国家共用，必须写成 "IST (Irish Standard Time, UTC+1)"**，不要裸写 IST。
3. 排期表换成第 4.10 节的 12 行。
4. **删掉 2026 的 `Oral Presentation Order` 表**，或改成占位。
5. 新增 `Poster Session`（workshop 已向会议申请 **10 块 poster board**）。
6. ⚠️ **排期内部有矛盾需确认**：proposal 的三个 paper session 合计 2 小时 20 分钟（约 11–12 个 oral 槽），但 proposal 同时写"预期 12–18 篇录用"。页面上先按 "oral + poster 分流" 的口径表述，不要写死每篇多少分钟；具体需向 co-chair 确认。

### 3.5 Accepted Papers（`papers.html`）

1. 清空 2026 全部内容，只留一句：
   > The list of accepted papers will be announced after the notification deadline (February 1, 2027).
2. 保留 Oral / Poster 分区结构 + OpenReview 链接 + PDF 链接 + Best Paper 徽章这套版式，2 月后直接填数据。
3. 顶部描述里的 `half-day`、`June 30, 2026`、`online` 全部改掉。
4. 建议把论文列表做成数据文件（如 `papers.json`）渲染，避免像 2026 那样手写 13 段导致格式不一致。

### 3.6 Keynote（`keynote.html`）

1. 2026 是 2 位，2027 **计划 4 位**。
2. ⚠️ **proposal 里目前只有 2 位是 "tentative, initial interest expressed; still under application" 状态，另 2 位仍是待定**。
   **绝对不要把 "tentative / still under application" 这类字眼或未确认的人名放到公开网页上。** 做法：先搭 4 张空卡片（照片位 + 单位 + 时间 + "Title & abstract coming soon"），确认一位填一位；不合适就写 `To be announced`。
3. 可复用的版式：2026 的 keynote 卡片布局。但**照片不要用 Li Chen / Zhaochun Ren**（他们今年是组织者）。

### 3.7 导航栏 Previous 下拉（6 个文件里都有）

| 显示文本 | 链接 |
|---|---|
| 2nd HCRS@WWW 2026 | https://hcrec.github.io/ |
| 1st HCRS@WWW 2025 | https://human-centeredrec.github.io/ |

⚠️ 这个下拉**出现在全部 6 个 HTML 文件里**，六处都要加（2026 只有 1 条，2027 要有 2 条，新的在前）。
建议顺手在 2026 站（hcrec.github.io）加一个指向 hcrs2027.github.io 的链接，否则从老站进来的流量找不到新站。

---

## 4. 可直接使用的英文文案

> 以下内容基于 proposal 整理，**其中的英文段落可以逐字粘贴**。带「需确认」标记的不要直接发布。

### 4.1 首页 Overview

> Recommender systems now shape what people know, choose, and experience. In the generative AI era, recommendation is becoming an ongoing relationship among people, agents, and platforms. User-facing agents can interpret goals, maintain memory, use tools, and act across multiple steps, while agentic workflows can revise, evaluate, and deploy recommendation models. These capabilities promise more adaptive support, but they may also shift control over how preferences are represented, decisions are executed, and systems evolve. Human-centered recommendation must therefore ask whose goals agents serve, how people can inspect and correct their behavior, and whether their effects remain beneficial over time. Organized around **agency, alignment, and long-term value**, the 3rd Workshop on Human-Centered Recommender Systems (HCRS@WWW 2027) brings together recommender systems, information retrieval, human-computer interaction, responsible AI, and social computing to develop methods, evaluations, and safeguards that keep agent-mediated recommendation accountable to people.

### 4.2 CfP — Topics of Interest（**逐字使用**）

> **Scope and Topics**
>
> The workshop provides an interdisciplinary forum for human-centered recommendation in the generative AI era. By fostering dialogue among recommender systems, HCI, information retrieval, AI safety, and social computing, it aims to connect technical advances with meaningful human outcomes. While the underlying agent architectures continue to evolve rapidly, our emphasis is on their consequences for people: the evaluation frameworks, safeguards, and governance mechanisms needed to keep them accountable.
>
> We welcome empirical, theoretical, and position papers, as well as systems, datasets, benchmarks, and user studies addressing the following themes:
>
> - **Agency: Human control over goals and delegation.** Extending human capabilities while preserving meaningful control over preference representation, memory, tools, permissions, and consequential actions. Topics include:
>   - Personal agents for discovery and decision support.
>   - Goal expression, revision, and mixed-initiative interaction.
>   - User control of memory, tools, data, and permissions.
>   - Consent, contestability, correction, and human override.
>   - Recommendations interpreted jointly by people and agents.
>   - Platform access, competition, and user choice.
> - **Alignment: Systems aligned with human intentions and values.** Keeping user-facing agents and self-evolving recommendation systems responsive to human intentions through feedback, verification, and accountable oversight. Topics include:
>   - Preference elicitation under ambiguity, conflict, and drift.
>   - Human and agent feedback, rubrics, and reward models.
>   - Verified agent harnesses for development and deployment.
>   - Memory provenance, revision, deletion, and contamination.
>   - Safe tool use, reflection, coordination, and self-improvement.
>   - Reward hacking, capability drift, and failed exploration.
>   - Reproducibility, privacy, fairness, and accountable audits.
> - **Long-term Value: Benefits for people and ecosystems over time.** Moving beyond one-step relevance and short-term engagement to assess cumulative effects on users, creators, communities, and platforms. Topics include:
>   - Long-horizon user modeling and preference formation.
>   - Satisfaction, learning, well-being, and autonomy.
>   - Continual adaptation and delayed feedback.
>   - Value for users, creators, and communities.
>   - Simulation-based and longitudinal evaluation.
>   - Process evaluation, attribution, and red teaming.
>   - Manipulation, dependency, filter bubbles, and harm.

⚠️ **不要保留** 2026 的四个主题名：`Human Understanding`、`Human Involvement`、`Human Impact`、`Emerging Cross-Domain Topics`。

### 4.3 Keywords（首页/CfP 关键词行，可选）

> Human-Centered Recommendation, Generative AI, Human Agency, Human–AI Alignment, Long-term Value

### 4.4 Important Dates（接收后启用）

- **Workshop paper submission:** January 4, 2027
- **Paper acceptance notification:** February 1, 2027
- **Camera-ready submission:** February 16, 2027
- **Workshop date:** during **May 10–14, 2027**, Dublin, Ireland — full-day, in person（**具体日期与时段待定 / TBA**）

Timezone note:
> TIMEZONE: Anywhere On Earth (UTC-12) for paper deadlines; session times will be announced in IST (Irish Standard Time, UTC+1).

（以上三个 paper deadline 已与 WWW 2027 官方 "Workshop Proposals & Papers" 时间表核对一致，可放心发布。）

### 4.5 Workshop Objectives

> This workshop encourages new theoretical frameworks, interdisciplinary approaches, and perspectives for human-centered recommender systems in the generative AI era. We advocate rigorous evaluation through user studies, simulation-based protocols, and off-policy metrics that move beyond engagement to capture satisfaction, trust, and long-term welfare. Participants will explore how large language models and autonomous agents can strengthen, rather than undermine, meaningful human control over recommendation. Rather than centering on agent architectures and system capabilities, the workshop foregrounds the human stakes of this transition: whose goals are served, who retains oversight, and who bears the consequences.

### 4.6 Submission Guidelines

- Format: single PDF, **ACM Web Conference 2027 template**
- Length: **4–8 pages, with unlimited pages allowed for references**
- Review: **single-blind**
- Evaluation criteria: relevance to the workshop, scientific novelty, and technical quality
- **Best Paper Award** will be presented
- Submission portal: **TBA**（OpenReview group 待建立；⚠️ 不要留 2026 的链接）
- 出版政策段：见第 3.2 节第 3 条，**按官方口径写或先留空**

### 4.7 首页顶部横幅（各阶段文案）

**阶段一（接收后 ~ 2027-01-04，投稿开放）**

> **📢 Call for Papers — HCRS@WWW 2027**
> The 3rd Workshop on Human-Centered Recommender Systems invites submissions on agency, alignment, and long-term value in the generative AI era. **Submission deadline: January 4, 2027 (AoE).**
> [Read the Call for Papers →](cfp.html)

**阶段二（2027-01-04 之后）**

> **Submissions are now closed.** Thank you to all authors! Review is in progress; notifications will be sent by February 1, 2027.

**阶段三（2027-02-01 之后）**：换成 accepted papers 公告（含 oral / poster 数量 + View Papers 按钮），版式沿用 2026 那块渐变横幅即可。

### 4.8 Organizing Committee（2027 共 9 人）

| 姓名 | 单位（英文写法照此） | 照片状态 | 链接状态 |
|---|---|---|---|
| Jiakai Tang | Renmin University of China, China | 可复用 2026 仓库的 `tjk.png` | 2026 站有 Scholar 链接，**需核对** |
| Weixin Chen | Kuaishou, China | ❌ **需新照片** | **需补** |
| Yuanhao Liu | Institute of Computing Technology, CAS, China | ❌ **需新照片** | **需补** |
| Qi Cao | Institute of Computing Technology, CAS, China | 可复用 `cq2.png` | `https://caoqi92.github.io/` |
| Shuchang Liu | Kuaishou, China | 可复用 `lsc.jpg` | 2026 站有 Scholar 链接，**需核对** |
| Tun Lu | Fudan University, China | ❌ **需新照片** | **需补** |
| Zhaochun Ren | Leiden University, Netherlands | 可复用 `renzhaochun.png` | 2026 站有 Scholar 链接，**需核对** |
| Li Chen | Hong Kong Baptist University, Hong Kong, China | 可复用 `chenli.jpeg` | 2026 站有 Scholar 链接，**需核对** |
| Fei Sun | University of Chinese Academy of Sciences, China | 可复用 `ofey.png`（3 MB，建议压缩） | `https://ofey.me/` |

→ **只缺 3 张照片**：Weixin Chen、Yuanhao Liu、Tun Lu。
→ 展示顺序建议按 proposal 的顺序（即上表顺序）。
→ 可在页面上加一句（可选）：
> Five of the nine organizers co-organized one or both previous editions of HCRS@WWW (2025, 2026), ensuring continuity in vision and logistics.

### 4.9 Program Committee（17 人，**需先补单位并确认公开意愿**）

名单（按 proposal 原文顺序）：Tarun Raheja, Jingyuan Huang, Xiaonan Song, Yunfan Wu, Aarush Sinha, Baruch Epstein, Erica Coppolillo, Rajarshee Dhar, Bodhisatta Maiti, Jiacheng Lin, Yasuhiro Yoshida, Huizhong Guo, Xiao Lin, Xue Li, Manoj Yadav, Sushant Mehta, Mingming Li。

### 4.10 Program Schedule（proposal 版，全日）

| Time | Event |
|---|---|
| 10:00–10:10 | Opening Remarks from Co-Chairs |
| 10:10–10:40 | Keynote Talk #1 + Q&A |
| 10:40–11:30 | Paper Session #1 |
| 11:30–12:00 | Keynote Talk #2 + Q&A |
| 12:00–12:30 | Paper Session #2 |
| 12:30–14:00 | Lunch Break |
| 14:00–14:30 | Keynote Talk #3 + Q&A |
| 14:30–15:20 | Paper Session #3 |
| 15:20–15:50 | Keynote Talk #4 + Q&A |
| 15:50–16:10 | Tea Break |
| 16:10–16:50 | Poster Session |
| 16:50–17:30 | Panel Discussion & Closing Remarks |

⚠️ 上线时整表标注 **Tentative**，并注明具体日期/时段待会议统一排期后公布。不要写死"某月某日"。

### 4.11 可选亮点：本届产出

> As a third-edition workshop with an established community, we aim to produce lasting value beyond the event itself: a community research roadmap synthesizing open challenges and future directions in human-centered recommendation, a workshop report published in ACM SIGIR Forum, and — where available — the coordinated release of community resources such as benchmarks or datasets contributed by participating organizations.

⚠️ **绝对不要发布 TORS special issue 相关内容**（proposal 里仍是 `[TODO: Confirm]` 待确认状态）。

---

## 5. 内容红线（Red Lines）

### 5.1 不要照抄 2026 的内容

| 不要抄 | 原因 |
|---|---|
| 四项主题（Human Understanding / Involvement / Impact / Emerging Cross-Domain） | 2027 重写为 Agency / Alignment / Long-term Value，与 proposal 不一致会被评审/chairs 质疑 |
| Best Paper 得主（RecoWorld…） | 是 2026 的结果 |
| 2026 的 13 篇 accepted papers | 同上 |
| two keynote talks / half-day / online / GST | 与 2027 形态矛盾 |
| 2026 的 Organizing Committee（含 Julian McAuley、Lina Yao、Du Su、Yue Feng）和 Student Organizers | 人员已换 |
| 2026 的 hero 图（Dubai skyline） | 换城市 |
| 2026 的 OpenReview 链接 | 会 404 / 指错 venue |
| `google-site-verification` token | 属于旧域名 |
| 2026 的 Reviewer Nomination Google Form（含注释块） | 表单已作废 |

### 5.2 不要凭猜测发布的内容

1. **未确认的 keynote 姓名** —— proposal 里两位是 "still under application"，两位仍是 TODO。
2. **TORS special issue 细节** —— proposal 里是 `[TODO: Confirm]`。
3. **workshop 的具体日期和时段** —— proposal 只给了会期区间 5/3–5/7，具体哪天由会议排期决定。
4. **投稿/出版政策中 proposal 未提及的部分** —— 尤其是"已发表或在审论文能否投"这条，按 WWW 2027 官方 workshop 政策口径（见第 3.2 节第 3 条）或等 chair 确认。
5. **预期投稿数/录用数/参会人数** —— proposal 里写 25–35 投稿、12–18 录用、50–70 人到场，那是给评审看的，**不适合当宣传语**。
6. **Program Committee 单位** —— proposal 里没有，需收集。
7. **联系邮箱** —— proposal 未给团队邮箱。如需在 footer 放联系方式，请向组织者索取（不要自行使用组织者个人邮箱，除非本人同意）。

### 5.3 与会议政策相关的硬约束（写文案时要遵守）

- 会议明文：`Workshops are in-person events. At least one organiser commits to register and attend in person.` → 网站上不要再承诺"线上参会/远程报告"。
- 会议明文：`Each accepted workshop will have a summary included in the Companion Proceedings of the Web Conference 2027.`
- 会议明文：`Workshops with fewer than 15 expected registrants may be merged with other workshops` → 不要写"已确认举办"之类的措辞，接收前一律用 "proposed / to be held"。
- 会议要求：`They must maintain an up-to-date website for their workshop that will be referenced from The Web Conference 2027 website.` → 页面要保持更新，会议官网会链过来。

---

## 6. 页面实现注意事项

### 6.1 代码结构

2026 的做法是 6 个 HTML 各复制一份 nav/footer，导致同一个字符串散落十几处，极易漏改。低成本改进（任选其一，也可都不做只靠人工校验）：

- 把 nav / footer / 年份常量抽到 `js/site.js`，各页只留一个占位容器；
- 或写一个替换脚本：改完统一跑一遍批量替换 + 校验。

批量替换示例（PowerShell，在页面目录执行，先备份或先 commit 再跑）：

```powershell
Get-ChildItem *.html | ForEach-Object {
  $p = $_.FullName
  $t = Get-Content $p -Raw
  $t = $t -replace 'The 2nd Workshop', 'The 3rd Workshop'
  $t = $t -replace 'HCRS@TheWebConf 2026', 'HCRS@WWW 2027'
  $t = $t -replace '@TheWebConf 2026', '@The Web Conference 2027'
  $t = $t -replace 'half-day session', 'full-day session'
  Set-Content $p -Value $t -Encoding utf8NoBOM -NoNewline
}
```

⚠️ **注意保留文件编码与换行符**（原文件是 UTF-8，含中文/特殊字符的页面改完请打开确认没有乱码）。

### 6.2 `<head>` 必做项

- `<title>`：每页不同，且都含 `HCRS@WWW 2027`，例如 `Call for Papers - HCRS@WWW 2027`
- `<meta name="description">`：2026 是空的，**必须填**一句话（含 3rd Workshop、WWW 2027、Dublin、agency/alignment/long-term value）
- `<meta name="author">`：`HCRS@WWW 2027`
- 补 `og:title` / `og:description` / `og:image`（分享卡片）
- 补 `favicon.ico`（2026 没有）
- **接收前（10-12 之前）**保留 `<meta name="robots" content="noindex">`，收到接收通知后删除

### 6.3 图片

- **不要 hotlink 会议官网图片**（2026 直接引用了 `www2026.thewebconf.org` 的迪拜图，外站改路径/防盗链就会挂）。
- 换成都柏林/爱尔兰相关图片，**下载到本地 `img/` 目录自托管**，并注意版权与出处标注。可向 WWW 2027 官网/web chair 索取官方 banner 素材（会议官网现有 banner：`https://www2027.thewebconf.org/wp-content/uploads/2026/09/WebBanner-1-scaled.jpg`）。
- 组织者照片统一 **200×200 圆形**（沿用 2026 CSS）；`ofey.png` 有 3 MB，上线前压缩。
- 保留 2026 的兜底写法 `onerror="this.src='img/avatar.png'"`。

### 6.4 可访问性与细节

- hero 文字压在图片上，换图后**检查对比度**，必要时加深色遮罩（2026 有 `.hero-overlay`）。
- 所有 `<img>` 保留有意义的 `alt`。
- 手机端检查：导航折叠菜单、排期表在小屏是否溢出（2026 的表格较宽）。

---

## 7. 素材清单：2026 仓库里能用的与不能用的

按下表取用（来源：`https://github.com/HCRec/HCRec.github.io`）：

| 文件 | 用途 |
|---|---|
| `tjk.png` | Jiakai Tang |
| `cq2.png` | Qi Cao |
| `lsc.jpg` | Shuchang Liu |
| `ofey.png` | Fei Sun（建议压缩） |
| `renzhaochun.png` | Zhaochun Ren |
| `chenli.jpeg` | Li Chen |
| `img/avatar.png` | 头像加载失败兜底 |
| `css/`、`js/`、`fonts/` | 整套样式与脚本，原样搬 |
| ❌ `sudo.jpg`、`mc.jpg`、`yln.jpg`、`fy2.png`、`zsx.png`、`kkz.png` | 这些人不是 2027 组织者，**不要用** |
| ❌ hero 迪拜图、2026 的 papers/program 内容 | 不要用 |

---

## 8. 建议的执行顺序

1. **2026-10-12 之前**：取 2026 页面文件作模板 → 建六个页面骨架 → 全站年份替换（第 1 节）→ CfP 换三主题（第 4.2 节）→ Committee 换 9 人并新建 PC 区块（第 4.8 / 4.9 节，同时向 3 位新组织者要照片、向 17 位 PC 收集单位）→ Program 换 full-day 表并标 Tentative（第 4.10 节）→ Keynote 页搭 4 张空卡片（第 3.6 节）→ 删除全部 2026 残留（第 2 节）→ 跑《自查清单》。
2. **2026-10-12 收到接收通知后**：去掉 `noindex` → 首页横幅换 "Call for Papers" → 上三个 deadline 与投稿入口（或 TBA）。
3. **2027-01-04 后**：横幅换 "Submissions closed"。
4. **2027-02-01 后**：填 Accepted Papers（oral/poster）、Keynote 补 title/abstract、公布 Best Paper。
5. **2027-04 月**：Program 定稿（具体日期、时段、oral 顺序）。
6. **持续**：会议官网会链接本站，页面需保持与实际进展一致。

---

## 附：配套文件与信息源

**配套文件**

- 《HCRS@WWW 2027 网站自查清单》：改完逐项核对用
- `HCRS_www27.txt`：proposal 全文纯文本（英文），本文档第 4 节文案的原始出处
- `HCRS_www27_topics.md`：主题范围新旧对照 + 新版逐字原文

**信息源（供核实）**

- WWW 2027 workshop 征稿与政策：https://www2027.thewebconf.org/workshops/
- WWW 2027 重要日期：https://www2027.thewebconf.org/important-dates/
- 2026 站：https://hcrec.github.io/ ｜ 2025 站：https://human-centeredrec.github.io/
