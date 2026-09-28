import tkinter as tk
from tkinter import filedialog
from PIL import Image

def select_and_show_image():
    # 1. Khởi tạo giao diện Tkinter để dùng cửa sổ chọn file
    root = tk.Tk()
    root.withdraw()  # Ẩn cửa sổ chính của Tkinter, chỉ hiện cửa sổ chọn file

    # 2. Mở cửa sổ chọn file từ ổ cứng máy tính
    file_path = filedialog.askopenfilename(
        title="Chọn ảnh từ máy tính",
        filetypes=[
            ("Tất cả các file ảnh", "*.jpg *.jpeg *.png *.bmp *.webp *.tiff *.gif"),
            ("PNG files", "*.png"),
            ("JPEG files", "*.jpg *.jpeg"),
            ("Tất cả các file", "*.*")
        ]
    )

    # 3. Kiểm tra xem người dùng đã chọn file hay chưa
    if file_path:
        print(f"Đã chọn file: {file_path}")
        
        try:
            # 4. Đọc ảnh bằng thư viện Pillow (PIL)
            img = Image.open(file_path)
            
            # In thông tin cơ bản của ảnh
            print(f"Định dạng ảnh: {img.format}")
            print(f"Kích thước (Rộng x Cao): {img.size}")
            print(f"Chế độ màu: {img.mode}")
            
            # 5. Hiển thị ảnh bằng trình xem ảnh mặc định của hệ thống
            img.show()
            
        except Exception as e:
            print(f"Lỗi khi mở ảnh: {e}")
    else:
        print("Bạn đã hủy chọn file!")

if __name__ == "__main__":
    select_and_show_image()

#BÀI 2 Chuyển đổi ảnh từ hệ màu RGB sang hệ màu Grayscale và HSV
    import cv2
import tkinter as tk
from tkinter import filedialog

def convert_color_spaces():
    # 1. Mở giao diện chọn ảnh từ máy tính
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Chọn ảnh để chuyển đổi hệ màu",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp *.tiff")]
    )

    if not file_path:
        print("Bạn chưa chọn ảnh nào!")
        return

    # 2. Đọc ảnh bằng OpenCV (hệ màu BGR gốc)
    img_bgr = cv2.imread(file_path)

    if img_bgr is None:
        print("Không thể đọc được file ảnh!")
        return

    # 3. Chuyển đổi sang hệ màu Grayscale (Ảnh xám)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # 4. Chuyển đổi sang hệ màu HSV
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

    # 5. Hiển thị từng hệ màu trên các cửa sổ khác nhau
    cv2.imshow("1. Anh Goc (BGR)", img_bgr)
    cv2.imshow("2. Anh Xam (Grayscale)", img_gray)
    cv2.imshow("3. He mau HSV", img_hsv)

    # Chờ người dùng nhấn một phím bất kỳ để đóng tất cả các cửa sổ
    print("Nhấn phím bất kỳ khi đang chọn cửa sổ ảnh để đóng...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    convert_color_spaces()
    #Bài tập 3: Áp dụng phép toán Bitwise AND trên ảnh
    import cv2
import tkinter as tk
from tkinter import filedialog

def select_image(title_text):
    # Hàm mở cửa sổ chọn ảnh
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title=title_text,
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp *.tiff")]
    )
    return file_path

def main():
    # 1. Chọn Ảnh 1
    print("Vui lòng chọn Ảnh thứ nhất...")
    path1 = select_image("Chọn Ảnh Thứ Nhất")
    if not path1:
        print("Bạn chưa chọn Ảnh 1!")
        return

    # 2. Chọn Ảnh 2
    print("Vui lòng chọn Ảnh thứ hai...")
    path2 = select_image("Chọn Ảnh Thứ Hai")
    if not path2:
        print("Bạn chưa chọn Ảnh 2!")
        return

    # 3. Đọc 2 ảnh bằng OpenCV
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)

    if img1 is None or img2 is None:
        print("Không thể đọc được file ảnh!")
        return

    # 4. Resize Ảnh 2 cho bằng kích thước Ảnh 1 (Bắt buộc)
    height, width = img1.shape[:2]
    img2_resized = cv2.resize(img2, (width, height))

    # 5. Áp dụng phép toán Bitwise AND
    bitwise_and_result = cv2.bitwise_and(img1, img2_resized)

    # 6. Hiển thị kết quả lên các cửa sổ khác nhau
    cv2.imshow("1. Anh Thu Nhat", img1)
    cv2.imshow("2. Anh Thu Hai (Da Resize)", img2_resized)
    cv2.imshow("3. Ket Qua Bitwise AND", bitwise_and_result)

    # Chờ nhấn phím bất kỳ để đóng cửa sổ
    print("Nhấn phím bất kỳ trên cửa sổ ảnh để đóng...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
#Bai4 
import cv2
import os
import tkinter as tk
from tkinter import filedialog

def bai_tap_4():
    # 1. Mở cửa sổ chọn file ảnh từ máy tính
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename(
        title="Chọn ảnh để lưu sang nhiều định dạng",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp *.tiff")]
    )

    if not file_path:
        print("Bạn chưa chọn ảnh!")
        return

    # 2. Đọc ảnh từ ổ cứng
    img = cv2.imread(file_path)

    if img is None:
        print("Lỗi: Không đọc được file ảnh!")
        return

    # 3. Lấy đường dẫn thư mục chứa ảnh vừa chọn
    folder_path = os.path.dirname(file_path)

    # 4. Lưu ảnh dưới các định dạng PNG, JPEG, và BMP
    path_png = os.path.join(folder_path, "ketqua.png")
    path_jpg = os.path.join(folder_path, "ketqua.jpg")
    path_bmp = os.path.join(folder_path, "ketqua.bmp")

    cv2.imwrite(path_png, img)
    cv2.imwrite(path_jpg, img)
    cv2.imwrite(path_bmp, img)

    print("--- LƯU ẢNH THÀNH CÔNG ---")
    print(f"1. Định dạng PNG  -> {path_png}")
    print(f"2. Định dạng JPEG -> {path_jpg}")
    print(f"3. Định dạng BMP  -> {path_bmp}")

    # 5. Hiển thị ảnh vừa đọc
    cv2.imshow("Anh Goc", img)
    print("\n[LƯU Ý]: Nhấp vào cửa sổ ảnh 'Anh Goc' rồi nhấn phím bất kỳ để thoát!")
    cv2.waitKey(3000)  # Tự động đóng cửa sổ ảnh sau 3 giây (3000ms)
cv2.destroyAllWindows()


if __name__ == "__main__":
    bai_tap_4()

#bai5
Python


import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

def increase_brightness():
    # 1. Mở giao diện chọn ảnh từ máy tính
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Chọn ảnh để tăng độ sáng",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp *.tiff")]
    )
    root.destroy()  # Giải phóng giao diện Tkinter

    if not file_path:
        print("Bạn chưa chọn ảnh nào!")
        return

    # 2. Đọc ảnh từ ổ cứng
    img = cv2.imread(file_path)

    if img is None:
        print("Không thể đọc được file ảnh!")
        return

    # 3. Tạo một mảng cùng kích thước chứa giá trị độ sáng cần tăng
    # Ví dụ: tăng thêm 50 đơn vị cho mỗi kênh màu (B, G, R)
    value_to_add = 50
    matrix = np.full(img.shape, value_to_add, dtype=np.uint8)

    # 4. Tăng độ sáng bằng cv2.add()
    # (cv2.add sẽ tự động giới hạn giá trị max là 255, tránh bị tràn số)
    brightened_img = cv2.add(img, matrix)

    # 5. Hiển thị ảnh gốc và ảnh đã tăng độ sáng
    cv2.imshow("1. Anh Goc", img)
    cv2.imshow("2. Anh Da Tang Do Sang (+50)", brightened_img)

    print("--- Hoàn tất! Nhấp chuột vào cửa sổ ảnh rồi nhấn phím bất kỳ để thoát ---")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    increase_brightness()

#bai6
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

def increase_brightness():
    # 1. Mở giao diện chọn ảnh từ máy tính
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Chọn ảnh để tăng độ sáng",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp *.tiff")]
    )
    root.destroy()  # Giải phóng giao diện Tkinter

    if not file_path:
        print("Bạn chưa chọn ảnh nào!")
        return

    # 2. Đọc ảnh từ ổ cứng
    img = cv2.imread(file_path)

    if img is None:
        print("Không thể đọc được file ảnh!")
        return

    # 3. Tạo một mảng cùng kích thước chứa giá trị độ sáng cần tăng
    # Ví dụ: tăng thêm 50 đơn vị cho mỗi kênh màu (B, G, R)
    value_to_add = 50
    matrix = np.full(img.shape, value_to_add, dtype=np.uint8)

    # 4. Tăng độ sáng bằng cv2.add()
    # (cv2.add sẽ tự động giới hạn giá trị max là 255, tránh bị tràn số)
    brightened_img = cv2.add(img, matrix)

    # 5. Hiển thị ảnh gốc và ảnh đã tăng độ sáng
    cv2.imshow("1. Anh Goc", img)
    cv2.imshow("2. Anh Da Tang Do Sang (+50)", brightened_img)

    print("--- Hoàn tất! Nhấp chuột vào cửa sổ ảnh rồi nhấn phím bất kỳ để thoát ---")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    increase_brightness()
    #bai6
    import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

def geometric_transformations():
    # 1. Chọn ảnh từ máy tính
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Chọn ảnh để biến đổi hình học",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp *.tiff")]
    )
    root.destroy()

    if not file_path:
        print("Bạn chưa chọn ảnh nào!")
        return

    # 2. Đọc ảnh bằng OpenCV
    img = cv2.imread(file_path)
    if img is None:
        print("Không thể đọc file ảnh!")
        return

    h, w = img.shape[:2]

    # --- 1. Xoay ảnh 90 độ (theo chiều kim đồng hồ) ---
    img_rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # --- 2. Dịch chuyển ảnh sang phải 50 pixel ---
    # Ma trận biến đổi Affine T = [[1, 0, tx], [0, 1, ty]]
    # Ở đây tx = 50 (dịch phải 50px), ty = 0 (không dịch dọc)
    M_translation = np.float32([
        [1, 0, 50],
        [0, 1, 0]
    ])
    img_translated = cv2.warpAffine(img, M_translation, (w, h))

    # --- 3. Thu phóng (ph phóng) ảnh với tỉ lệ 1.5 lần ---
    img_resized = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

    # 3. Hiển thị kết quả lên các cửa sổ
    cv2.imshow("1. Anh Goc", img)
    cv2.imshow("2. Xoay 90 do (cv2.rotate)", img_rotated)
    cv2.imshow("3. Dich sang phai 50px (cv2.warpAffine)", img_translated)
    cv2.imshow("4. Phong to 1.5 lan (cv2.resize)", img_resized)

    print("--- Hoàn tất! Nhấp vào cửa sổ ảnh rồi nhấn phím bất kỳ để đóng ---")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    geometric_transformations()