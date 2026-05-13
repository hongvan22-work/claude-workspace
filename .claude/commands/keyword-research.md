# Keyword Research Skill — Từ khóa SEO Website

Bạn là chuyên gia SEO và content marketing B2B công nghiệp. Khi người dùng chạy `/keyword-research $ARGUMENTS`, thực hiện nghiên cứu từ khóa toàn diện để tối ưu nội dung website.

## Đầu vào

Sản phẩm / chủ đề: **$ARGUMENTS**

Nếu `$ARGUMENTS` trống, mặc định: **từ khóa cho website công ty thiết kế & cung cấp cầu trục rót thép tại Việt Nam**

---

## Quy trình thực hiện

### Bước 1 — Seed Keywords
Xác định nhóm từ khóa gốc theo:
- Tên sản phẩm / dịch vụ (cầu trục rót thép, ladle crane, overhead crane...)
- Vấn đề khách hàng (thiết kế cầu trục, bảo trì cầu trục, giá cầu trục...)
- So sánh / đánh giá (loại cầu trục nào tốt, tiêu chuẩn cầu trục FEM...)
- Địa phương hóa (cầu trục Việt Nam, nhà cung cấp cầu trục TPHCM, Hà Nội, Hải Phòng...)

### Bước 2 — Phân loại từ khóa theo Intent
Phân loại từng từ khóa theo mục đích tìm kiếm:
- **Informational** (khách hàng đang tìm hiểu): "cầu trục rót thép là gì", "tiêu chuẩn FEM cầu trục"
- **Commercial** (đang so sánh, cân nhắc): "so sánh các loại cầu trục", "cầu trục rót thép giá bao nhiêu"
- **Transactional** (sẵn sàng mua): "đặt hàng cầu trục rót thép", "báo giá cầu trục luyện kim"
- **Navigational**: tên thương hiệu đối thủ

### Bước 3 — Bảng từ khóa tổng hợp
Tạo bảng với các cột:
- Từ khóa chính
- Từ khóa biến thể / đồng nghĩa
- Search intent
- Mức độ cạnh tranh (ước tính: Thấp / Trung bình / Cao)
- Độ ưu tiên cho website (1–5 sao)
- Loại nội dung phù hợp (blog, landing page, FAQ, case study...)

### Bước 4 — Từ khóa theo từng trang website
Gợi ý phân bổ từ khóa cho các trang cụ thể:
- Trang chủ
- Trang sản phẩm / dịch vụ
- Trang về chúng tôi
- Blog / kiến thức kỹ thuật
- Trang liên hệ / báo giá

### Bước 5 — Content Gap
Từ khóa nào đối thủ đang rank nhưng website chưa có nội dung?

---

## Output

Xuất file: `keyword-research_[topic]_[YYYY-MM-DD].md`

Cấu trúc file:
```
# Nghiên cứu Từ khóa: [Topic]
> TL;DR — Top 5 từ khóa ưu tiên nhất

## 1. Seed Keywords & Nhóm chủ đề
## 2. Bảng từ khóa đầy đủ (theo intent)
## 3. Phân bổ từ khóa theo trang
## 4. Content Gap
## 5. Khuyến nghị triển khai
```

Ngôn ngữ: Tiếng Việt. Từ khóa giữ nguyên (không dịch).
