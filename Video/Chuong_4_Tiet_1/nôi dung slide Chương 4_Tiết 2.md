**PHẦN 1: HẬU QUẢ CỦA RỦI RO & PHÂN TÍCH TÌNH HUỐNG (SLIDE 1 - 5)**

**Slide 1: Tiêu đề Tiết học**
*   **Tiêu đề chính:** CHƯƠNG IV: AN TOÀN THÔNG TIN TRONG THƯƠNG MẠI ĐIỆN TỬ
*   **Tiêu đề phụ:** Tiết 2: Hậu quả khôn lường & Nền tảng phòng thủ
*   **Thông tin:** Giảng viên: [Tên giảng viên] | Lớp: BA24M
*   **Hình ảnh minh họa:** Hình ảnh đồ họa thể hiện sự gián đoạn của một hệ thống thương mại điện tử hoặc một lá chắn bảo vệ dữ liệu.

**Slide 2: Mục tiêu Tiết 2**
*   **Tiêu đề:** Mục tiêu Tiết học
*   **Nội dung hiển thị:**
    *   Đánh giá toàn diện các mức độ thiệt hại do rủi ro an ninh mạng gây ra đối với doanh nghiệp TMĐT và người tiêu dùng.
    *   Phân tích sâu bài học quản trị rủi ro từ các cuộc tấn công thực tế (Case Study).
    *   Nắm vững mô hình Đảm bảo thông tin (Information Assurance) và Tam giác bảo mật CIA làm nền tảng xây dựng hệ thống phòng thủ.

**Slide 3: 4.3 Ảnh hưởng của rủi ro trong TMĐT - Bức tranh thiệt hại**
*   **Tiêu đề:** Cái giá của sự chủ quan: Thiệt hại đa chiều
*   **Nội dung hiển thị:**
    *   **Tổn thất Tài chính & Vận hành:** Chi phí trung bình cho mỗi vụ tội phạm mạng đối với doanh nghiệp lên tới hàng triệu USD mỗi năm. Bao gồm mất doanh thu do gián đoạn dịch vụ (Downtime), chi phí khắc phục hệ thống và tiền bồi thường.
    *   **Suy giảm Uy tín (Tài sản vô hình):** Đánh mất niềm tin của khách hàng - yếu tố sống còn để duy trì hoạt động Thương mại điện tử.
    *   **Rủi ro Pháp lý:** Đối mặt với các vụ kiện tụng từ khách hàng hoặc án phạt từ cơ quan quản lý do vi phạm bảo mật dữ liệu.
    *   **Thiệt hại đối với Người tiêu dùng:** Bị đánh cắp danh tính (Identity Theft), mất cắp tài sản và dữ liệu cá nhân nhạy cảm.

**Slide 4: Case Study Chuyên sâu - Sự cố Bệnh viện Tim Kansas (2016)**
*   **Tiêu đề:** Phân tích Tình huống: Cơn ác mộng Ransomware
*   **Nội dung hiển thị:**
    *   **Sự cố:** Bệnh viện Tim Kansas bị tin tặc tấn công bằng mã độc tống tiền (Ransomware), khiến toàn bộ dữ liệu và hồ sơ bệnh án bị khóa/mã hóa hoàn toàn,.
    *   **Phản ứng:** Hacker yêu cầu trả tiền chuộc bằng Bitcoin để tránh bị truy vết,. Bệnh viện đã quyết định trả tiền chuộc lần 1 để lấy lại quyền truy cập,.
    *   **Hậu quả:** Hacker không mở khóa toàn bộ dữ liệu mà tiếp tục tống tiền thêm, cho thấy việc nhượng bộ tội phạm không mang lại kết quả đảm bảo,.

**Slide 5: Bài học Quản trị từ Case Study Kansas**
*   **Tiêu đề:** Lỗ hổng Quản trị & Chiến lược Ứng phó
*   **Nội dung hiển thị:**
    *   **Lỗ hổng hệ thống (Root Causes):**
        *   *Thất bại trong khâu Sao lưu (Backup):* Bệnh viện không có hệ thống sao lưu dữ liệu độc lập/offline đủ mạnh để phục hồi khi hệ thống chính bị vô hiệu hóa.
        *   *Nhận thức nhân sự:* Các vụ lây nhiễm Ransomware thường bắt nguồn từ những email giả mạo (Phishing) do nhân viên thiếu cảnh giác click vào.
    *   **Chiến lược ứng phó chuẩn mực:**
        *   **Không trả tiền chuộc:** Việc trả tiền không đảm bảo lấy lại được dữ liệu và chỉ tạo tiền lệ khuyến khích tội phạm tiếp tục tấn công.
        *   **Phòng vệ chủ động:** Đầu tư vào đào tạo nhân sự và xây dựng Kế hoạch liên tục kinh doanh (Business Continuity Plan),.

---

### **PHẦN 2: NỀN TẢNG LÝ THUYẾT & CHIẾN LƯỢC PHÒNG THỦ CHIỀU SÂU (SLIDE 6 - 10)**

**Slide 6: 4.4 Mô hình Đảm bảo Thông tin (Information Assurance - IA)**
*   **Tiêu đề:** Nền tảng Phòng thủ: Mô hình Đảm bảo Thông tin
*   **Nội dung hiển thị:**
    *   **Khái niệm:** Các biện pháp toàn diện nhằm bảo vệ hệ thống thông tin và quy trình chống lại mọi rủi ro tiềm ẩn.
    *   **Cốt lõi - Tam giác CIA (CIA Triad),:**
        *   *Confidentiality (Tính bảo mật):* Đảm bảo dữ liệu (như thông tin thẻ tín dụng) chỉ được tiết lộ cho những người có thẩm quyền.
        *   *Integrity (Tính toàn vẹn):* Đảm bảo dữ liệu chính xác, không bị cắt xén hay chỉnh sửa trái phép trên đường truyền.
        *   *Availability (Tính sẵn sàng):* Hệ thống, website và thông tin luôn khả dụng mọi lúc mọi nơi khi khách hàng cần.

**Slide 7: Các Yếu tố Bảo mật Mở rộng trong TMĐT**
*   **Tiêu đề:** Mở rộng Tam giác CIA: Xác thực & Chống chối bỏ
*   **Nội dung hiển thị:**
    *   **Xác thực (Authentication):** Quá trình xác minh danh tính thực sự của một cá nhân, phần mềm hoặc website (VD: Đăng nhập bằng mật khẩu, vân tay).
    *   **Ủy quyền (Authorization):** Cấp quyền truy cập vào các tài nguyên cụ thể sau khi đã xác thực thành công.
    *   **Chống chối bỏ (Non-repudiation):** Sự đảm bảo rằng người mua hoặc người bán không thể phủ nhận (chối bỏ) việc họ đã tham gia vào một giao dịch hợp lệ. Thường được hiện thực hóa bằng Chữ ký số (Digital Signatures),.

**Slide 8: Chiến lược Phòng thủ Chiều sâu (Defense-in-Depth)**
*   **Tiêu đề:** Xây dựng Thành trì: Chiến lược Phòng thủ Đa lớp
*   **Nội dung hiển thị:**
    Bảo mật không phụ thuộc vào một công cụ duy nhất mà là sự kết hợp của nhiều rào chắn bảo vệ:
    *   **Lớp 1 - Kiểm soát Truy cập & Mã hóa:** Ngăn chặn ở cửa ngõ bằng xác thực danh tính và mã hóa dữ liệu (Encryption & PKI).
    *   **Lớp 2 - Bảo vệ Mạng lưới:** Sử dụng Tường lửa (Firewall) và Mạng riêng ảo (VPN) để cô lập mạng nội bộ khỏi Internet công cộng,,.
    *   **Lớp 3 - Kiểm soát Quản trị (Administrative Controls):** Xây dựng chính sách, quy trình, và đào tạo nhận thức an ninh cho nhân sự,.

**Slide 9: Hệ thống Giám sát & Phát hiện Xâm nhập (IDS)**
*   **Tiêu đề:** Lính gác Không ngủ: Hệ thống IDS (Intrusion Detection Systems)
*   **Nội dung hiển thị:**
    *   **Khái niệm:** Thiết bị hoặc phần mềm chuyên dụng được thiết kế để theo dõi liên tục các hoạt động trên mạng và hệ thống máy chủ.
    *   **Chức năng chính:**
        *   Phát hiện các dấu hiệu truy cập trái phép, thao túng dữ liệu hoặc các hành vi độc hại.
        *   Giúp nhận diện sớm các luồng dữ liệu bất thường của cuộc tấn công Từ chối dịch vụ (DoS/DDoS) để có biện pháp ngăn chặn kịp thời.

**Slide 10: Quản trị Quyền truy cập & Công nghệ Sinh trắc học**
*   **Tiêu đề:** Kiểm soát Truy cập & Ứng dụng Sinh trắc học (Biometrics)
*   **Nội dung hiển thị:**
    *   **Kiểm soát truy cập (Access Control):** Xác định rõ ai (người dùng, chương trình) được phép sử dụng các tài nguyên nào của doanh nghiệp, vào thời điểm nào và thao tác ra sao.
    *   **Công nghệ Sinh trắc học (Biometrics):**
        *   Sử dụng các đặc điểm sinh học độc nhất để xác thực danh tính mức độ cao, thay thế/bổ sung cho mật khẩu truyền thống.
        *   *Ví dụ ứng dụng:* Máy quét vân tay, nhận diện khuôn mặt (Face ID), quét mống mắt hoặc nhận diện giọng nói trong các giao dịch và thanh toán điện tử.


---

### **PHẦN 3: CÔNG CỤ PHÒNG VỆ CHIỀU SÂU & KẾ HOẠCH DỰ PHÒNG (SLIDE 11 - 15)**

**Slide 11: Lá chắn Dữ liệu - Mã hóa (Encryption) & Giao thức SSL**
*   **Tiêu đề:** Mã hóa Dữ liệu & Môi trường truyền dẫn an toàn
*   **Nội dung hiển thị:**
    *   **Mã hóa (Encryption):** Quá trình biến đổi dữ liệu gốc (Plaintext) thành dạng mã hóa (Ciphertext) không thể đọc được nếu thiếu khóa giải mã, giúp bảo vệ dữ liệu nhạy cảm.
    *   **Phân loại Hệ thống Khóa:**
        *   *Mã hóa đối xứng (Symmetric):* Dùng chung 1 khóa bí mật để cả mã hóa và giải mã.
        *   *Mã hóa bất đối xứng (Asymmetric/PKI):* Dùng Khóa công khai (Public Key) để mã hóa và Khóa bí mật (Private Key) để giải mã.
    *   **Secure Sockets Layer (SSL/TLS):** Giao thức bảo mật tiêu chuẩn tạo đường truyền an toàn cho TMĐT. Nhận diện dễ dàng qua biểu tượng ổ khóa và tiền tố "https://".

**Slide 12: Xác thực & Chống chối bỏ - PKI và Chữ ký số**
*   **Tiêu đề:** Định danh trên không gian mạng: Chữ ký số & CA
*   **Nội dung hiển thị:**
    *   **Chữ ký số (Digital Signatures):** Tương đương với chữ ký tay, giúp xác thực danh tính người gửi thông điệp và đảm bảo tính "chống chối bỏ" (Non-repudiation).
    *   **Hạ tầng khóa công khai (PKI):** Khung bảo mật toàn diện kết hợp khóa công khai, khóa bí mật và chữ ký số.
    *   **Cơ quan Chứng thực (Certificate Authority - CA):** Tổ chức bên thứ ba độc lập cấp phát Chứng thư số (Digital Certificates) để xác minh chủ sở hữu đích thực của Khóa công khai.
    *   *Ví dụ thực tiễn:* VeriSign, VNPT-CA, Viettel-CA.

**Slide 13: Thiết lập Biên giới - Tường lửa & VPN**
*   **Tiêu đề:** Rào cản Mạng lưới: Tường lửa (Firewall) & VPN
*   **Nội dung hiển thị:**
    *   **Tường lửa (Firewall):** Đóng vai trò kiểm soát an ninh, tạo rào cản giữa mạng nội bộ riêng tư (Intranet) và mạng Internet công cộng nhằm ngăn chặn các truy cập trái phép.
    *   **Kiến trúc DMZ (Demilitarized Zone):** Đặt các máy chủ công cộng (như Web Server) vào một "vùng phi quân sự" giữa hai lớp tường lửa để tăng cường bảo vệ mạng nội bộ.
    *   **Mạng riêng ảo (VPN - Virtual Private Network):** Kỹ thuật "tạo đường hầm" (tunnelling) mã hóa qua Internet công cộng, cho phép nhân viên làm việc từ xa hoặc đối tác B2B trao đổi thông tin nội bộ an toàn.

**Slide 14: Kế hoạch Liên tục Kinh doanh & Phục hồi thảm họa**
*   **Tiêu đề:** "Phòng bệnh hơn chữa bệnh": Kế hoạch BCP & Backup
*   **Nội dung hiển thị:**
    *   **Thực trạng:** Tấn công mạng (như Ransomware) hoặc thảm họa thiên nhiên có thể làm tê liệt hệ thống bất cứ lúc nào.
    *   **Kế hoạch Liên tục Kinh doanh (Business Continuity Plan - BCP):** Kế hoạch chi tiết giúp doanh nghiệp tiếp tục vận hành và phục hồi nhanh chóng sau sự cố.
    *   **Các biện pháp chủ động:**
        *   *Sao lưu dữ liệu (Backup):* Lưu trữ dữ liệu thường xuyên ở môi trường độc lập (offline/cloud) để sẵn sàng khôi phục khi bị tống tiền.
        *   *Kiểm tra xâm nhập (Penetration Testing):* Thuê chuyên gia đóng giả hacker tấn công vào hệ thống để chủ động tìm và vá lỗ hổng.

**Slide 15: Tổng kết Tiết 2 & Chuẩn bị Tiết 3**
*   **Tiêu đề:** Tổng kết & Bước đệm cho Quản trị Rủi ro
*   **Nội dung hiển thị:**
    *   **Key Takeaways:**
        *   Thiệt hại do rủi ro an ninh mạng không chỉ là tiền bạc mà còn là uy tín thương hiệu và rủi ro pháp lý khôn lường.
        *   Mô hình Đảm bảo Thông tin (IA) với Tam giác CIA (Confidentiality - Integrity - Availability) là tiêu chuẩn vàng cho mọi chiến lược bảo mật.
        *   Doanh nghiệp bắt buộc phải xây dựng chiến lược phòng thủ đa lớp (Defense-in-depth): Từ Mã hóa dữ liệu, Tường lửa, Sinh trắc học đến Sao lưu dự phòng.
    *   **Nhiệm vụ Tiết sau (Tiết 3):** Áp dụng kiến thức nền tảng để giải quyết các Bài tập tình huống thực tế về quản lý và ứng phó khủng hoảng an ninh mạng trong doanh nghiệp TMĐT.