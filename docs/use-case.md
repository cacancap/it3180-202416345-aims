# Use case AIMS-mini

**Tác nhân chính:** Người dùng tìm DVD và quản lý giỏ hàng.

```mermaid
flowchart LR
    User["Người dùng"]
    subgraph AIMS["AIMS-mini"]
        Find(["Tìm DVD theo tiêu đề"])
        Add(["Thêm DVD vào giỏ"])
        Remove(["Xóa DVD khỏi giỏ"])
        Print(["In giỏ hàng"])
    end
    User --- Find
    User --- Add
    User --- Remove
    User --- Print
```

| Use case | Thao tác của người dùng | Kết quả |
| --- | --- | --- |
| Tìm DVD theo tiêu đề | Nhập từ khóa để tìm trong danh sách DVD. | Trả về các DVD có tiêu đề chứa từ khóa, phân biệt chữ hoa và chữ thường. |
| Thêm DVD vào giỏ | Chọn DVD muốn thêm. | Nếu thêm thành công, DVD xuất hiện trong giỏ. |
| Xóa DVD khỏi giỏ | Chọn DVD muốn xóa. | DVD được xóa nếu có trong giỏ. Nếu không tìm thấy, chương trình báo `The disc is not in the cart`. |
| In giỏ hàng | Yêu cầu xem nội dung giỏ. | In số thứ tự, tiêu đề, giá từng DVD và tổng tiền. Nếu giỏ trống, in `The cart is empty`. |

`main.py` minh họa luồng thêm ba DVD rồi in giỏ. Các thao tác xóa và tìm kiếm được cung cấp qua các hàm Python.

## Kiểm tra chức năng in giỏ hàng

Chạy các lệnh dưới đây từ thư mục gốc của dự án.

### Giỏ có DVD

```bash
python main.py
```

Sau các thông báo thêm DVD, chương trình in nội dung giỏ và tổng tiền.

```text
Cart contents:
1. The Lion King - 19.95 $
2. Star Wars - 24.95 $
3. Aladdin - 18.99 $
Total cost: 63.89 $
```

### Giỏ trống

```bash
python -c "from aims.cart import Cart; Cart().print_cart()"
```

Lệnh tạo một giỏ mới và gọi `print_cart()`. Kết quả mong đợi là dòng sau.

```text
The cart is empty
```
