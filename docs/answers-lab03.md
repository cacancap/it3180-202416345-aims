# Câu hỏi thảo luận Lab 03

## 1. Merge base là gì?

Merge base là commit tổ tiên chung phù hợp nhất của hai nhánh. Git dùng mốc này để xác định mỗi nhánh đã thay đổi gì kể từ khi tách ra. Trong bài thực hành, Dev 1 và Dev 2 xuất phát từ cùng một mốc rồi sửa cùng dòng thông báo theo hai cách khác nhau, nên Git yêu cầu người dùng giải quyết xung đột khi hợp nhất.

## 2. Vì sao dùng revert trên master và release/*?

Đây là các nhánh dùng chung. `git revert` tạo một commit mới để đảo ngược thay đổi, giữ lịch sử mà những người khác đã đồng bộ và để lại dấu vết về việc hoàn tác. Trong bài này, revert PR #14 đưa thông báo thêm DVD về phiên bản của Dev 1. Với một commit merge, `-m 1` chọn phía master trước khi merge làm mốc.