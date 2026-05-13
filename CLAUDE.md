# CLAUDE.md — Claude Workspace

## Tổng quan
Workspace này dùng để làm BTVN khóa học SEONGON, sử dụng Claude Code với Sub Agents và Custom Skills.

## Sub Agents có sẵn

- **research-analyst**: Nghiên cứu + phân tích chủ đề → dùng `/research` và `/slides`
- **ui-content-creator**: Thiết kế UI/UX + tạo nội dung → dùng `/ui-ux-pro-max` và `/slides`

## Custom Skills (Slash Commands)

- `/research [chủ đề]` — Nghiên cứu có hệ thống, xuất file `.md`
- `/slides [topic] [số trang]` — Tạo HTML presentation
- `/ui-ux-pro-max` — Thiết kế UI theo 50+ styles, 161 màu sắc

## Nguyên tắc làm việc

1. Giao nhiệm vụ lớn → Claude Code tự phân bổ cho agent phù hợp
2. Mỗi agent dùng đúng skill của mình
3. Output luôn có file `.md` (research) hoặc `.html` (slides/UI)

## Dự án chính

Ladle Crane Training: `https://github.com/hongvan22-work/ladle-crane-training`
