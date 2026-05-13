# Claude Workspace — SEONGON BTVN Buổi 4

Không gian làm việc nâng cao với Claude Code: Sub Agents + Custom Skills.

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

## Cách sử dụng Agents

Giao 1 nhiệm vụ lớn cho Claude Code, nó sẽ tự phân bổ cho agent phù hợp:

```
Nhiệm vụ: Tạo tài liệu hoàn chỉnh cho dự án Ladle Crane Training
→ Research Analyst: nghiên cứu + slides về AI trong đào tạo công nghiệp
→ UI Content Creator: thiết kế Admin Dashboard mới + slides design
```

## Files Output

| File | Mô tả |
|------|-------|
| `lich_su_tro_chuyen.txt` | Lịch sử trò chuyện xuất từ `/export` |
| `research_*.md` | Kết quả nghiên cứu từ Research Analyst |
| `slides_*.html` | Slide presentations |
| `ui_*.html` | UI components từ UI Content Creator |

## Dự án liên quan

- **Ladle Crane Training:** [github.com/hongvan22-work/ladle-crane-training](https://github.com/hongvan22-work/ladle-crane-training)
