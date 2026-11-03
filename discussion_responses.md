## 1. Câu hỏi nhanh: Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?

* **Nơi lưu `--global`:** Lưu tại tệp `~/.gitconfig` (thư mục người dùng hiện tại).
* **Khác biệt giữa `--global` và `--local`:**
  * `--global`: Áp dụng cho **mọi repository** của người dùng trên máy.
  * `--local`: Lưu trong `.git/config` của repo hiện tại, chỉ áp dụng cho **riêng repo đó** và có độ ưu tiên cao hơn `--global` (ghi đè `--global`).

---

## 2. Câu hỏi thảo luận

### a. Vì sao dùng `git mv`?
* **Tiện lợi:** Thực hiện đồng thời việc di chuyển tệp trên ổ đĩa và đưa thay đổi vào vùng Staging (không cần `git rm` và `git add` thủ công).
* **Giữ lịch sử (History tracking):** Giúp Git và PR nhận diện đây là thao tác đổi tên/di chuyển (`renamed`) thay vì xóa cũ thêm mới, nhờ đó bảo toàn lịch sử commit của tệp (xem được qua `git log --follow`).

### b. `release/lab01` có phải baseline không?
* **Có.** Vì đây là phiên bản đã hoàn thiện và thống nhất tại mốc nộp bài Lab 01. Nó được đóng băng làm mốc chuẩn; mọi thay đổi sau đó (nếu có) không được sửa trực tiếp mà phải đi qua quy trình kiểm soát thay đổi (`hotfix/*` và Pull Request).

### c. Vì sao không commit thẳng vào `master` dù làm một mình?
* **Bảo vệ nhánh chính:** Cô lập các thay đổi đang làm dở ở nhánh riêng, giữ cho `master` luôn ở trạng thái ổn định và chạy được.
* **Kiểm soát chất lượng:** Tạo Pull Request giúp tự rà soát lại toàn bộ code (`Files changed`), mô tả rõ mục đích và kết quả kiểm thử trước khi gộp vào `master`.
* **Dễ hoàn tác & tuân thủ quy trình:** Dễ dàng hủy bỏ nhánh nếu làm sai hoặc `revert` theo cụm tính năng, đồng thời tạo thói quen chuẩn bị cho việc làm việc nhóm và tích hợp CI/CD ở các bài sau.