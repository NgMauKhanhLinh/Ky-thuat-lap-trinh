import numpy as np

# Nhập kích thước ma trận từ người dùng
n = int(input("Nhập số dòng của ma trận: "))
m = int(input("Nhập số cột của ma trận: "))

# Tạo ma trận ngẫu nhiên với giá trị từ -100 đến 100
ma_tran = np.random.randint(-100, 101, (n, m))


def tinh_dinh_thuc(ma_tran):
    """Tính định thức của ma trận (chỉ tính nếu là ma trận vuông)."""
    if ma_tran.shape[0] != ma_tran.shape[1]:
        return "Ma trận không vuông, không thể tính định thức."
    return round(np.linalg.det(ma_tran), 2)


def find_inverse(ma_tran):
    """Tìm ma trận nghịch đảo nếu có"""
    if ma_tran.shape[0] != ma_tran.shape[1]:
        return "Ma trận không vuông, không thể tìm nghịch đảo."
    try:
        return np.linalg.inv(ma_tran)
    except np.linalg.LinAlgError:
        return "Ma trận suy biến, không có nghịch đảo."


def sort_ma_tran_rows(ma_tran):
    """Sắp xếp ma trận theo hàng"""
    return np.sort(ma_tran, axis=1)


def sort_ma_tran_columns(ma_tran):
    """Sắp xếp ma trận theo cột"""
    return np.sort(ma_tran, axis=0)


def sort_ma_tran_by_row_mean(ma_tran):
    """Sắp xếp ma trận theo giá trị trung bình của hàng"""
    row_means = np.mean(ma_tran, axis=1)
    sorted_indices = np.argsort(row_means)
    return ma_tran[sorted_indices]


def update_element(ma_tran, row, col, new_value):
    """Thay đổi giá trị của một phần tử trong ma trận"""
    if 0 <= row < ma_tran.shape[0] and 0 <= col < ma_tran.shape[1]:
        ma_tran[row, col] = new_value
        return ma_tran
    else:
        return "Lỗi: Vị trí dòng hoặc cột không hợp lệ!"


def update_elements_condition(ma_tran, condition_value):
    """Tăng giá trị lên 2 nếu phần tử bằng condition_value"""
    ma_tran[ma_tran == condition_value] += 2
    return ma_tran


# Hiển thị ma trận ban đầu
print("\nMa trận ngẫu nhiên:\n", ma_tran)

# Tính định thức
print("\n1. Định thức ma trận:", tinh_dinh_thuc(ma_tran))

# Tìm ma trận nghịch đảo
print("\n2. Ma trận nghịch đảo:\n", find_inverse(ma_tran))

# Sắp xếp ma trận theo hàng
print("\n3. Ma trận sắp xếp theo hàng:\n", sort_ma_tran_rows(ma_tran))

# Sắp xếp ma trận theo cột
print("\n4. Ma trận sắp xếp theo cột:\n", sort_ma_tran_columns(ma_tran))

# Sắp xếp ma trận theo giá trị trung bình của hàng
print("\n5. Ma trận sắp xếp theo giá trị trung bình của hàng:\n", sort_ma_tran_by_row_mean(ma_tran))

# Thay đổi giá trị của một phần tử
a = int(input("\nNhập dòng của phần tử cần thay đổi: "))
b = int(input("Nhập cột của phần tử cần thay đổi: "))
new_value = int(input("Nhập giá trị mới: "))
updated_matrix = update_element(ma_tran, a, b, new_value)
print("\nMa trận sau khi cập nhật phần tử:\n", updated_matrix)

# Thay đổi giá trị theo điều kiện
condition_value = int(input("\nNhập giá trị muốn tìm để tăng thêm 2: "))
print("\nMa trận sau khi cập nhật theo điều kiện:\n", update_elements_condition(ma_tran, condition_value))

# Cộng thêm vector vào từng hàng của ma trận
vector = np.random.randint(-10, 11, m)  # Tạo vector ngẫu nhiên có số phần tử bằng số cột
print("\nVector cần cộng vào từng hàng:\n", vector)

ma_tran = ma_tran + vector  # Cộng từng hàng với vector
print("\n8. Ma trận sau khi cộng vector vào từng hàng:\n", ma_tran)

# Tính hạng của ma trận
rank = np.linalg.matrix_rank(ma_tran)
print(f"\n9. Hạng của ma trận là: {rank}")

# Phân tích SVD
U, S, Vt = np.linalg.svd(ma_tran)
print("\n10. Ma trận U:\n", U)
print("Giá trị kỳ dị (S):\n", S)
print("Ma trận V^T:\n", Vt)
