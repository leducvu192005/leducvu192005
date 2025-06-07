 ## BÁO CÁO ĐỒ ÁN CUỐI KỲ
Đề tài: Xây dựng ứng dụng nghe nhạc Spotify Clone
    -Thành viên : 1
        Họ và tên: Lê Đức Vũ
        MSSV: 23010608@st.phenikaa-uni.edu.vn
    -Thành viên : 2
        Họ và tên: Đô Bảo Long
        MSSV: 23010561@st.phenikaa-uni.edu.vn
I. Mục tiêu và lý do chọn đề tài
    -Ngày nay, các nền tảng phát nhạc trực tuyến đóng vai trò quan trọng trong đời sống giải trí số, trong đó nổi bật là Spotify. Việc xây dựng một ứng dụng Spotify Clone giúp em vừa tiếp cận thực tế về kiến trúc và tính năng của các hệ thống hiện đại, vừa rèn luyện kỹ năng lập trình từ frontend (giao diện người dùng) đến backend (API, xử lý dữ liệu).

Mục tiêu đề tài:

    -Thiết kế giao diện người dùng đẹp, trực quan, mô phỏng Spotify.

    -Xây dựng kiến trúc MVVM (Model – View – ViewModel) để tách biệt logic và UI.

    -Sử dụng Flutter và Riverpod cho ứng dụng mobile.

    -Xây dựng API backend bằng FastAPI để xử lý người dùng, bài hát, playlist,...

    -Áp dụng các kỹ thuật: đăng nhập bằng JWT, phát nhạc (audio streaming), upload file MP3, lưu playlist,...

II. Công nghệ sử dụng
Frontend (Flutter)

    - Flutter 3.19.5: Framework đa nền tảng (mobile, web, desktop)

    - Riverpod 2.5: Quản lý trạng thái và ViewModel

    - Dio: Gửi request đến API

    - GoRouter: Điều hướng màn hình

    - AudioPlayers: Phát nhạc mp3 trực tuyến

    - CachedNetworkImage: Tối ưu ảnh đại diện, bìa album

    - Backend (Python - FastAPI)

    - FastAPI: Framework web tốc độ cao, hỗ trợ async

    - Pydantic: Kiểm tra dữ liệu đầu vào (validation)

    - SQLAlchemy: ORM để thao tác CSDL

    - SQLite: CSDL nhẹ dùng cho bản thử nghiệm

    - JWT (JSON Web Token): Đăng nhập và bảo mật

III. Kiến trúc hệ thống
Dự án tuân theo mô hình Client-Server với sự phân tách rõ ràng giữa frontend và backend. Giao tiếp giữa hai phía thông qua các API RESTful. Dữ liệu được truyền bằng JSON.

    -Frontend (ứng dụng Flutter) hoạt động theo kiến trúc MVVM:

        + Model: Các lớp dữ liệu, định nghĩa bài hát, người dùng,...

        + ViewModel: Điều phối dữ liệu giữa model và view, xử lý logic, gọi API

        + View: Giao diện người dùng (UI), phản hồi theo thay đổi từ ViewModel

    - Backend chia thành các phần:

        + api/: Router định nghĩa các endpoint

        + auth/: Đăng nhập, đăng ký, xác thực JWT

        + db/: Các models (User, Song, Playlist)

        + core/: Cấu hình, tiện ích

        + main.py: Điểm khởi chạy chính với Uvicorn

IV. Các tính năng đã hoàn thành
    1. Đăng ký & Đăng nhập
    Người dùng có thể tạo tài khoản mới, đăng nhập để truy cập các chức năng nâng cao. Dữ liệu được mã hóa và bảo vệ bằng JWT.

    2. Trình phát nhạc (Player)
    Giao diện giống Spotify cơ bản, có thể:

        - Phát/Ngừng bài hát

        - Chuyển bài (Next/Previous)

        - Tua nhanh (Seek)

        - Hiển thị thông tin bài hát đang phát

    3. Danh sách bài hát & tìm kiếm
        - Hiển thị danh sách các bài hát trong hệ thống

        - Người dùng có thể tìm kiếm theo tên bài hát

    4. Playlist cá nhân
Tạo playlist mới

        - Thêm/xoá bài hát khỏi playlist

        - Lưu danh sách bài hát yêu thích

    5. Upload và streaming bài hát
        - Admin có thể upload file mp3 lên server, backend hỗ trợ phát trực tiếp thông qua streaming API.

V. Kết quả đạt được
Xây dựng thành công giao diện mô phỏng Spotify (dùng Flutter)

    - Backend ổn định, phản hồi nhanh, hỗ trợ xác thực JWT

    - Có thể đăng nhập, phát nhạc, quản lý playlist cá nhân

    - Giao diện thân thiện, responsive tốt với nhiều thiết bị:

    - Giao diện Home

    - Trình phát nhạc

    - Giao diện Playlist

    - API mẫu trong Swagger UI

VI. Hạn chế và hướng phát triển
    - Hạn chế:
        + Chưa hỗ trợ nghe offline

        + Chưa có hệ thống bình luận, chia sẻ bài hát

        + Bảo mật chưa áp dụng nâng cao (chưa có refresh token, giới hạn rate...)

    - Hướng phát triển:
        + Tích hợp Firebase cho lưu trữ và xác thực

        + Thêm tính năng like, comment, đề xuất nhạc

        + Tối ưu player chạy nền (background playback)

        + Hỗ trợ nền tảng Web/Desktop từ cùng một codebase Flutter

VII. Kết luận
    Đề tài "Spotify Clone sử dụng Flutter và FastAPI" đã giúp em củng cố kiến thức lập trình cả frontend và backend, hiểu sâu hơn về cách xây dựng hệ thống có kiến trúc rõ ràng và quản lý dữ liệu hiệu quả. Dự án có tiềm năng mở rộng thành một ứng dụng thực tế với các tính năng nâng cao hơn.

    Em xin cảm ơn thầy/cô đã hướng dẫn, góp ý trong quá trình thực hiện đồ án này.

    - Tài liệu tham khảo
        + Flutter.dev

        + FastAPI Docs

        + Riverpod.dev

        + AudioPlayers plugin

        + YouTube:https://www.youtube.com/watch?v=9gpAtzQhYkY&t=17418s

        