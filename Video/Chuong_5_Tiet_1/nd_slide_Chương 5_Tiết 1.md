**SLIDE 1: TIÊU ĐỀ TIẾT HỌC**
*   **Tiêu đề chính:** CHƯƠNG V: ỨNG DỤNG THƯƠNG MẠI ĐIỆN TỬ TRONG DOANH NGHIỆP
*   **Tiêu đề phụ:** Tiết 1 - Khái niệm và Phát triển hệ thống TMĐT Doanh nghiệp.
*   **Thông tin:** Giảng viên: Trần Thành Thắng | Lớp: Quản trị kinh doanh BA24M.
*   **🎤 Gợi ý diễn giảng:** Chúng ta đã học về các mô hình và chiến lược marketing. Hôm nay, chúng ta sẽ bước vào phần "bếp núc" của doanh nghiệp: Làm thế nào để thực sự xây dựng và vận hành một cỗ máy TMĐT hoàn chỉnh từ con số không.

**SLIDE 2: MỤC TIÊU TIẾT 1**
*   **Nội dung hiển thị:**
    *   Hiểu rõ kiến trúc và các thành phần của một hệ thống TMĐT.
    *   Tóm tắt được những vấn đề liên quan đến phát triển hệ thống TMĐT.
    *   Phân tích ưu/nhược điểm của các phương pháp xây dựng hệ thống: Tự phát triển (In-house) vs. Thuê dịch vụ (SaaS).

**SLIDE 3: KHỞI ĐỘNG - TÌNH HUỐNG "XÂY NHÀ HAY THUÊ NHÀ?"**
*   **Nội dung hiển thị:** 
    *   Để mở một nền tảng bán hàng, bạn sẽ thuê một đội ngũ IT về viết code từ đầu (In-house), hay trả 29$/tháng để dùng nền tảng có sẵn như Shopify (SaaS)?
    *   *Thảo luận nhanh 3 phút.*
*   **🎤 Gợi ý diễn giảng:** Mỗi lựa chọn đều có cái giá của nó. Bài học hôm nay sẽ cung cấp cho các nhà quản trị tương lai khung tư duy để đưa ra quyết định công nghệ chính xác nhất.

**SLIDE 4: 5.1 KHÁI NIỆM HỆ THỐNG TMĐT DOANH NGHIỆP**
*   **Nội dung hiển thị:**
    *   Hệ thống TMĐT là các ứng dụng sử dụng công nghệ thông tin để hỗ trợ, xử lý và duy trì các quá trình trao đổi dịch vụ, thông tin và hàng hóa.
    *   Không chỉ là một website giao diện, nó đòi hỏi sự tích hợp sâu sắc giữa mạng viễn thông, phần cứng, phần mềm và cơ sở dữ liệu để luồng công việc diễn ra trơn tru.
    *   **Mục tiêu:** Tránh tình trạng "phân mảnh ứng dụng" (silo) khiến dữ liệu marketing, bán hàng và tài chính bị cô lập, gây tốn kém chi phí hỗ trợ và nâng cấp.

**SLIDE 5: KIẾN TRÚC TỔNG THỂ CỦA HỆ THỐNG (DIGITAL BUSINESS ARCHITECTURE)**
*   **Nội dung hiển thị:** Hệ thống TMĐT vận hành dựa trên nguyên lý **Client-Server (Khách - Chủ)**.
    *   **Phía Client (Khách):** Thiết bị của người dùng (PC, Smartphone, Tablet). Có thể là *Thin Client* (chỉ hiển thị, cấu hình thấp) hoặc *Fat Client* (xử lý và quản lý dữ liệu trực tiếp).
    *   **Phía Server (Máy chủ):** Nơi xử lý cốt lõi, bao gồm:
        *   *Web Server:* Xử lý giao diện và yêu cầu HTTP,.
        *   *Application Server:* Xử lý logic nghiệp vụ, giỏ hàng.
        *   *Database Server:* Lưu trữ dữ liệu khách hàng, sản phẩm.
    *   **Back-end Systems:** Tích hợp với hệ thống CRM, ERP, Kế toán và Mua sắm nội bộ.

**SLIDE 6: PHƯƠNG PHÁP 1 - SỬ DỤNG DỊCH VỤ PHẦN MỀM (SAAS & CLOUD)**
*   **Nội dung hiển thị:**
    *   **SaaS (Software as a Service):** Ứng dụng được lưu trữ và quản lý bởi bên thứ ba, trả phí theo dạng đăng ký (Subscription) hoặc theo mức sử dụng.
    *   **Ưu điểm:** Tiết kiệm chi phí cài đặt/bảo trì máy chủ cục bộ, linh hoạt đáp ứng các đợt tăng vọt lưu lượng truy cập (spikes),. 
    *   **Nhược điểm:** Phụ thuộc vào bên thứ 3 (nguy cơ thời gian chết - downtime), hiệu suất có thể chậm hơn cơ sở dữ liệu nội bộ, rủi ro rò rỉ dữ liệu bảo mật.

**SLIDE 7: KIẾN TRÚC SAAS: SINGLE-TENANT VS MULTI-TENANT**
*   **Nội dung hiển thị:**
    *   **Single-tenancy (Đơn khách thuê):** Một phiên bản ứng dụng và cơ sở dữ liệu độc lập dành riêng cho một doanh nghiệp. Tài nguyên không bị chia sẻ.
    *   **Multi-tenancy (Đa khách thuê):** Một phiên bản ứng dụng duy nhất được dùng chung cho nhiều khách hàng trên một máy chủ (VD: Shopify). Tiết kiệm chi phí (ưu thế chi phí 16:1) nhưng phải chia sẻ băng thông và bộ xử lý,.

**SLIDE 8: PHƯƠNG PHÁP 2 - TỰ PHÁT TRIỂN & MÃ NGUỒN MỞ (OPEN-SOURCE)**
*   **Nội dung hiển thị:**
    *   Sử dụng mã nguồn mở (như LAMP: Linux, Apache, MySQL, PHP) được phát triển cộng tác bởi cộng đồng,.
    *   **Ưu điểm:** Miễn phí mua bản quyền ban đầu. Tăng tính linh hoạt vì doanh nghiệp có thể tự do chỉnh sửa mã nguồn để phù hợp chính xác với nghiệp vụ.
    *   **Nhược điểm:** Đòi hỏi đội ngũ IT nội bộ cực giỏi để tự vá lỗi (support). Chi phí chuyển đổi và đào tạo nhân sự cao,.

**SLIDE 9: BƯỚC VÀO VÒNG ĐỜI PHÁT TRIỂN HỆ THỐNG (SDLC)**
*   **Nội dung hiển thị:**
    *   Quy trình chuẩn để phát triển nền tảng TMĐT bao gồm: (1) Phân tích kiến trúc -> (2) Tích hợp ứng dụng -> (3) Chọn hạ tầng lưu trữ -> (4) Kiểm thử & Giám sát mức dịch vụ.

**SLIDE 10: BƯỚC 1 - TÍCH HỢP HỆ THỐNG BẰNG API & WEB SERVICES**
*   **Nội dung hiển thị:**
    *   Trong kỷ nguyên Internet, chiến lược giữ kín thông tin độc quyền cục bộ đã lỗi thời. Các nền tảng cần giao tiếp với nhau.
    *   **API (Application Programming Interfaces):** Giao diện lập trình ứng dụng giúp hệ thống TMĐT "nói chuyện" với hệ thống khác (VD: Gắn bản đồ Google Maps, Cổng thanh toán, Tracking vận chuyển),.
    *   Lợi ích: Tăng cường giá trị dịch vụ và mở rộng phạm vi tiếp cận khách hàng.

**SLIDE 11: BƯỚC 2 - LỰA CHỌN NHÀ CUNG CẤP LƯU TRỮ (HOSTING PROVIDER)**
*   **Nội dung hiển thị:**
    *   **Hosting Provider:** Đơn vị quản lý máy chủ lưu trữ website và kết nối nó với mạng Internet. 
    *   **Dedicated Server (Máy chủ riêng):** Chi phí cao gấp 5-10 lần nhưng đảm bảo hiệu suất độc lập.
    *   **Co-located/Shared Server (Máy chủ dùng chung):** Phù hợp với doanh nghiệp SME nhưng dễ bị ảnh hưởng nếu các website dùng chung bị quá tải.

**SLIDE 12: BƯỚC 3 - QUẢN TRỊ TỐC ĐỘ VÀ SỰ KHẢ DỤNG (AVAILABILITY)**
*   **Nội dung hiển thị:**
    *   **Tốc độ tải trang:** Nội dung web cần tải dưới **4 giây**, nếu không trải nghiệm người dùng sẽ sụt giảm. 64% khách hàng sẽ không quay lại nếu trang web quá chậm.
    *   Tổn thất doanh thu khổng lồ (hàng tỷ USD) xảy ra do hiện tượng "Bailout" – khách hàng thoát trang vì không muốn chờ đợi.

**SLIDE 13: BƯỚC 4 - THIẾT LẬP THỎA THUẬN MỨC DỊCH VỤ (SLA)**
*   **Nội dung hiển thị:**
    *   **SLA (Service Level Agreement):** Văn bản cam kết với nhà cung cấp Hosting về tiêu chuẩn thời gian hoạt động (Uptime - thường là 99.9%) và tốc độ phản hồi.
    *   SLA cũng phải quy định rõ việc bồi thường nếu thời gian chết (downtime) xảy ra, lý do gián đoạn và thời gian dự kiến khôi phục hệ thống.

**SLIDE 14: LỜI CẢNH BÁO TỪ THỰC TẾ: "NHỮNG CHIẾC GIỎ HÀNG LUNG LAY"**
*   **Nội dung hiển thị:**
    *   Nghiên cứu cho thấy 20% giỏ hàng điện tử không hoạt động từ 12 giờ trở lên mỗi tháng, và 75% website trượt bài kiểm tra tiêu chuẩn sẵn sàng 99.9%.
    *   *Bài học:* Việc khách hàng không thể thanh toán khi đã quyết định mua là hành động "tự sát thương mại". Doanh nghiệp phải giám sát hệ thống 24/7 cho từng hành trình của khách (checkout, thêm vào giỏ, kiểm tra đơn),.

**SLIDE 15: TỔNG KẾT TIẾT 1**
*   **Nội dung hiển thị:**
    *   Phát triển hệ thống TMĐT là bài toán giải quyết sự cân bằng giữa Tự xây dựng (In-house/Open source) linh hoạt nhưng tốn công, và Thuê ngoài (SaaS/Cloud) tiện lợi nhưng phụ thuộc.
    *   Tốc độ tải trang, thời gian Uptime, và sự tích hợp liền mạch giữa Front-end và Back-end là xương sống của một nền tảng TMĐT thành công.
*   **🎤 Dẫn dắt sang Tiết 2:** Nền móng công nghệ đã có, ở tiết sau chúng ta sẽ học cách đặt nền móng kinh doanh thông qua việc Lập kế hoạch kinh doanh điện tử.