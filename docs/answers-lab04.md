# Câu hỏi thảo luận Lab 04

## 1. Vì sao không merge release/* ngược vào master?

Nhánh `release/*` giữ mốc phát hành và là nơi bảo trì phiên bản đã phát hành. Trong khi đó, `master` tiếp tục nhận tính năng mới. Merge toàn bộ nhánh phát hành ngược lại có thể đưa thay đổi riêng của phiên bản cũ, chẳng hạn số phiên bản hoặc ghi chú bản vá, vào dòng phát triển mới. Khi một bản sửa cần có ở cả hai nơi, có thể đưa riêng bản sửa qua một PR phù hợp hoặc dùng `cherry-pick` để giữ dấu vết.

## 2. Quy trình của học phần khác GitFlow thế nào?

Trong GitFlow, nhánh release thường tách từ `develop` để ổn định bản phát hành. Khi hoàn tất, thay đổi phát hành được hợp nhất vào nhánh chính và đưa trở lại `develop` để giữ các bản sửa. Trong quy trình của học phần, `release/*` tách từ `master` để chốt bản nộp và bảo trì. Bản sửa cần cho dòng phát triển được tích hợp riêng.

## 3. Vì sao chọn 1.0.0 thay vì 0.4.0?

Các bản `0.x` là các mốc phát triển ban đầu. Bản `1.0.0` đánh dấu mốc ổn định đầu tiên đã được nhóm chốt và kiểm tra. Đây là quyết định về mức độ ổn định của phiên bản theo SemVer. Việc chọn `0.4.0` sẽ tiếp tục đánh dấu dự án ở giai đoạn trước bản ổn định đầu tiên.
