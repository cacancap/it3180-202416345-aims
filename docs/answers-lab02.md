# Câu hỏi thảo luận Lab 02

## 1. Vì sao cần đồng bộ với `master` trước khi gửi PR?

* Đồng bộ giúp nhánh công việc nhận được những thay đổi mới nhất trên master. Nhờ đó, lập trình viên có thể phát hiện xung đột, kiểm tra khả năng tích hợp và sửa lỗi trước khi yêu cầu review. Đây cũng là quy trình được yêu cầu trong bài thực hành.

## 2. Khi nào không được rebase?

Theo quy tắc của bài, không rebase các commit đã được push hoặc chia sẻ, đặc biệt trên master và các nhánh release. Rebase tạo lại commit với mã SHA mới, nên có thể làm lịch sử trên máy của những người cùng làm việc không còn khớp nhau.

## 3. Nhánh `feature/*` khác `topic/*` như thế nào?
* Nhánh feature/* dùng để phát triển tính năng, chẳng hạn in giỏ hàng hoặc tìm kiếm theo tiêu đề.

* Nhánh topic/* dùng cho một chủ đề công việc riêng, có phạm vi rộng hơn. Trong bài này, các ví dụ là tạo mẫu Pull Request và viết tài liệu use case.

* Đây là quy ước đặt tên để thể hiện mục đích công việc; Git không tự áp dụng cơ chế khác nhau cho hai loại nhánh.
