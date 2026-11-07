# Câu hỏi thảo luận Lab 05

## Upstream first và release first khác nhau thế nào?

Với upstream first, nhóm sửa trên nhánh phát triển chính rồi chuyển bản sửa xuống từng nhánh phát hành bị ảnh hưởng. Cách này giảm nguy cơ quên sửa trên dòng phát triển chính, nhưng bản sửa có thể phụ thuộc vào mã mới chưa có trong phiên bản cũ.

Với release first, nhóm bắt đầu từ đúng nhánh có lỗi đang ảnh hưởng người dùng. Nhờ vậy, bản vá có thể được kiểm thử và phát hành trên dòng cũ trước. Nhóm cần theo dõi việc chuyển riêng commit sửa lỗi sang master và các nhánh phát hành khác để tránh tái xuất hiện lỗi.

## Làm sao phát hiện bản sửa chưa được đưa vào release/lab05?

Chạy lại phép tìm từ khóa `lion` trên `release/lab05` hoặc tag `v1.1.0`. Kết quả rỗng cho thấy bản sửa chưa có, còn kết quả chứa `The Lion King` xác nhận hành vi đã đúng. Có thể dùng `git log` để tìm dòng `cherry picked from commit` trỏ đến SHA gốc. Kiểm tra hành vi vẫn cần thiết vì các bản cherry-pick có SHA khác nhau.
