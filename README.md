# Claude Workspace

Không gian làm việc với Claude Code: Sub Agents + Custom Skills.

## Thông tin

| Mục | Chi tiết |
|-----|---------|
| **Tác giả** | hongvan22-work |
| **Công cụ** | Claude Code |
| **Ngày tạo** | 13/05/2026 |

## Cấu trúc `.claude/`

```
.claude/
├── agents/
│   ├── research-analyst.md      # Agent nghiên cứu & phân tích
│   └── ui-content-creator.md    # Agent thiết kế UI & tạo nội dung
├── commands/                    # Custom slash commands (Skills)
│   ├── research.md              # /research [topic]
│   ├── slides.md                # /slides [topic] [n]
│   └── ui-ux-pro-max.md         # /ui-ux-pro-max
└── skills/                      # Assets cho các skills
```

## Sub Agents

### 1. Research Analyst (`research-analyst`)
Chuyên nghiên cứu chuyên sâu và trình bày kết quả.
- **Skill 1:** `/research` — nghiên cứu có hệ thống, output `.md`
- **Skill 2:** `/slides` — chuyển kết quả thành HTML presentation

### 2. UI Content Creator (`ui-content-creator`)
Chuyên thiết kế UI/UX và tạo nội dung trực quan.
- **Skill 1:** `/ui-ux-pro-max` — thiết kế UI 50+ styles
- **Skill 2:** `/slides` — presentation về quyết định thiết kế

## Cách dùng

### Bước 1 — Clone repo

```bash
git clone https://github.com/hongvan22-work/claude-workspace.git
cd claude-workspace
```

### Bước 2 — Mở bằng Claude Code

```bash
claude .
```

Folder `.claude/` sẽ được tự động nhận diện — agents và skills sẵn sàng dùng ngay.

### Bước 3 — Dùng Skills (Slash Commands)

```
/research [chủ đề]         # Nghiên cứu → xuất file .md
/slides [topic] [số trang]  # Tạo HTML presentation
/ui-ux-pro-max              # Thiết kế UI component
```

### Bước 4 — Giao nhiệm vụ cho Agents

```
"Dùng research-analyst để nghiên cứu về [chủ đề]"
"Dùng ui-content-creator để thiết kế [màn hình]"
```

Hoặc giao 1 nhiệm vụ lớn, Claude Code sẽ tự phân bổ cho agent phù hợp.

## Files Output

| File | Mô tả |
|------|-------|
| `research_*.md` | Kết quả nghiên cứu từ Research Analyst |
| `slides_*.html` | Slide presentations |
| `ui_*.html` | UI components từ UI Content Creator |
