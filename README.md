```
1. Mục tiêu
•	Hiểu và triển khai các thuật toán tìm kiếm không có thông tin và có thông tin.
•	Áp dụng các thuật toán này vào bài toán trò chơi 8 ô chữ (8-puzzle).
•	So sánh hiệu suất của các thuật toán dựa trên thời gian, bộ nhớ, và số bước để tìm lời giải.
•	Trình bày kết quả dưới dạng trực quan (hình ảnh, biểu đồ, GIF) và đưa ra nhận xét.

2. Nội dung
2.1. Các thuật toán tìm kiếm không có thông tin (Uninformed Search)
Các thành phần chính của bài toán tìm kiếm:
•	Trạng thái (State): Một cấu hình của trò chơi 8 ô chữ, ví dụ: vị trí của các ô số và ô trống.
•	Trạng thái ban đầu (Initial State): Cấu hình ban đầu của bảng 8 ô chữ.
•	Trạng thái mục tiêu (Goal State): Cấu hình mong muốn (ví dụ: các số từ 1-8 được sắp xếp đúng).
•	Hành động (Actions): Di chuyển ô trống lên, xuống, trái, phải.
•	Hàm chuyển trạng thái (Transition Function): Quy định cách trạng thái thay đổi khi thực hiện hành động.
•	Hàm chi phí (Cost Function): Chi phí của mỗi bước di chuyển (thường là 1 trong 8-puzzle).
•	Không gian trạng thái (State Space): Tập hợp tất cả các cấu hình có thể có.
Solution (Lời giải): Một chuỗi các hành động đưa từ trạng thái ban đầu đến trạng thái mục tiêu.

2.1.Các thuật toán tìm kiếm không có thông tin (Uninformed Search)
2.1.1.Breadth-First Search (BFS):
Mô tả
•	Cơ chế hoạt động: 
o	BFS là thuật toán tìm kiếm không có thông tin (uninformed search), khám phá tất cả trạng thái ở mức hiện tại trước khi chuyển sang mức sâu hơn, đảm bảo tìm đường đi ngắn nhất.
o	Bắt đầu từ trạng thái ban đầu của 8-puzzle, BFS mở rộng các trạng thái hàng xóm theo thứ tự mức (level by level).
o	Sử dụng hàng đợi (queue) để lưu trữ các trạng thái, lấy trạng thái đầu tiên để mở rộng.
o	Với 8-puzzle: 
	Trạng thái: Bảng 3x3 (ví dụ: [[1,2,3], [4,0,5], [7,8,6]], 0 là ô trống).
	Hàng xóm: Cấu hình sau di chuyển ô trống (lên, xuống, trái, phải).
	BFS duyệt theo mức, hướng tới mục tiêu ([[1,2,3], [4,5,6], [7,8,0]]).
o	Quy trình: 
1.	Thêm trạng thái ban đầu vào hàng đợi, đánh dấu đã thăm.
2.	Lặp lại: 
	Lấy trạng thái đầu tiên từ hàng đợi.
	Nếu là trạng thái mục tiêu, dừng và trả về lời giải.
	Tạo tất cả trạng thái hàng xóm, thêm vào hàng đợi nếu chưa thăm.
3.	Tiếp tục cho đến khi tìm thấy mục tiêu hoặc hàng đợi rỗng.
o	Đặc điểm: BFS đảm bảo tối ưu (đường đi ngắn nhất) và hoàn chỉnh trong không gian hữu hạn.
Ưu điểm
•	Tối ưu: Tìm đường đi ngắn nhất trong 8-puzzle dựa trên số bước di chuyển.
•	Hoàn chỉnh: Tìm lời giải nếu tồn tại trong không gian hữu hạn (~362,880 trạng thái).
•	Ứng dụng: Phù hợp cho 8-puzzle hoặc bài toán tìm đường khi cần đường đi tối ưu.
•	Đơn giản: Dễ triển khai, không cần heuristic.
Nhược điểm
•	Tốn tài nguyên: Hàng đợi cần lưu nhiều trạng thái, nhiều hơn DFS/IDS.
•	Chậm hơn Informed Search: Không dùng heuristic, khám phá nhiều trạng thái hơn A* hoặc Greedy.
•	Không hiệu quả trong không gian lớn: Khám phá tất cả trạng thái ở các mức nông trước, chậm với bài toán phức tạp.
o	GIF minh họa
```
![bfs](https://github.com/user-attachments/assets/096e550a-e0bd-4fdf-a2a7-066d8b396d17)
```
oNgoài ra còn có nút Detail để xem chi tiết các trạng thái dẫn đến solution:
```
![image](https://github.com/user-attachments/assets/c48fcdae-2536-46c3-a4bf-d0443d2497c5)
```
 
2.1.2.Depth-First Search (DFS):
Mô tả
•	Cơ chế hoạt động: 
o	DFS là thuật toán tìm kiếm không có thông tin (uninformed search), ưu tiên duyệt sâu vào một nhánh của cây tìm kiếm trước khi quay lui khám phá các nhánh khác.
o	Bắt đầu từ trạng thái ban đầu của 8-puzzle, DFS chọn một hành động và đi sâu nhất có thể, chỉ quay lui khi gặp ngõ cụt.
o	Sử dụng ngăn xếp (thường qua đệ quy hoặc stack rõ ràng) để lưu trữ các trạng thái, lấy trạng thái mới nhất để mở rộng.
o	Với 8-puzzle: 
	Trạng thái: Bảng 3x3 (ví dụ: [[1,2,3], [4,0,5], [7,8,6]], 0 là ô trống).
	Hàng xóm: Cấu hình sau di chuyển ô trống (lên, xuống, trái, phải).
	DFS duyệt sâu từng nhánh, hướng tới mục tiêu ([[1,2,3], [4,5,6], [7,8,0]]).
o	Quy trình: 
1.	Thêm trạng thái ban đầu vào ngăn xếp, đánh dấu đã thăm.
2.	Lặp lại: 
	Lấy trạng thái trên cùng từ ngăn xếp.
	Nếu là trạng thái mục tiêu, dừng và trả về lời giải.
	Tạo tất cả trạng thái hàng xóm, thêm vào ngăn xếp nếu chưa thăm.
3.	Tiếp tục cho đến khi tìm thấy mục tiêu hoặc ngăn xếp rỗng.
o	Đặc điểm: DFS nhanh nhưng không đảm bảo tối ưu, vì có thể khám phá các nhánh sâu không cần thiết.
Ưu điểm
•	Nhanh: Duyệt sâu một nhánh, giảm số trạng thái cần kiểm tra ở các mức nông.
•	Tiết kiệm tài nguyên: Chỉ lưu trạng thái trên nhánh hiện tại, ít hơn BFS/UCS.
•	Hoàn chỉnh trong không gian hữu hạn: Tìm lời giải nếu tồn tại trong không gian hữu hạn (~362,880 trạng thái), với điều kiện tránh lặp.
•	Ứng dụng: Phù hợp cho bài toán cần tìm lời giải nhanh hoặc khi tài nguyên hạn chế.
Nhược điểm
•	Không tối ưu: Có thể tìm đường đi dài hơn tối ưu do duyệt sâu không cần thiết.
•	Nguy cơ lặp vô hạn: Cần kiểm tra trạng thái đã thăm để tránh vòng lặp trong 8-puzzle.
•	Không hiệu quả bằng Informed Search: Không dùng heuristic, khám phá nhiều trạng thái hơn A* hoặc Greedy.
•	Hạn chế: Kém hiệu quả trong 8-puzzle khi cần đường đi ngắn nhất.
Chi tiết bổ sung
•	Thời gian: O(b^m), với b là số nhánh, m là độ sâu tối đa, nhanh nếu mục tiêu gần.
•	Không gian: O(bm), chỉ lưu nhánh hiện tại.
•	So sánh: 
o	BFS/UCS: Tối ưu, tốn tài nguyên hơn.
o	IDS: Tối ưu, chậm hơn, tiết kiệm tài nguyên.
o	Greedy/A*: Hiệu quả hơn, tối ưu (A*).
•	Hiệu suất: Nhanh nhưng không tối ưu, phụ thuộc vào cấu trúc cây.
Nhận xét trên 8-puzzle
•	Hiệu quả: Phù hợp khi ưu tiên tốc độ và tài nguyên thấp, nhưng không đảm bảo đường đi ngắn nhất.
•	Thực tiễn: Ít áp dụng cho 8-puzzle, vì A* hoặc IDS vượt trội hơn.
•	Hạn chế: Có thể chọn nhánh dài, không lý tưởng khi cần tính tối ưu.
o	GIF minh họa
```
![dfs](https://github.com/user-attachments/assets/5e6d395b-2167-4627-83a2-390e69d2dccc)
```


2.1.3.UCS:
Mô tả
•	Cơ chế hoạt động: 
o	UCS là thuật toán tìm kiếm không có thông tin (uninformed search), mở rộng trạng thái có chi phí đường đi thấp nhất từ trạng thái ban đầu, đảm bảo tìm đường đi tối ưu.
o	Bắt đầu từ trạng thái ban đầu của 8-puzzle, UCS sử dụng chi phí đường đi g(n) (số bước di chuyển) để ưu tiên trạng thái.
o	Sử dụng hàng đợi ưu tiên (priority queue) để lưu trữ các trạng thái, sắp xếp theo g(n) tăng dần. Trạng thái có g(n) thấp nhất được xử lý trước.
o	Với 8-puzzle: 
	Trạng thái: Bảng 3x3 (ví dụ: [[1,2,3], [4,0,5], [7,8,6]], 0 là ô trống).
	Hàng xóm: Cấu hình sau di chuyển ô trống (lên, xuống, trái, phải).
	Chi phí: Mỗi di chuyển có chi phí 1 (đồng đều).
	UCS mở rộng trạng thái theo g(n), hướng tới mục tiêu ([[1,2,3], [4,5,6], [7,8,0]]).
o	Quy trình: 
1.	Thêm trạng thái ban đầu vào hàng đợi ưu tiên với g(n) = 0.
2.	Lặp lại: 
	Lấy trạng thái có g(n) thấp nhất từ hàng đợi.
	Nếu là trạng thái mục tiêu, dừng và trả về lời giải.
	Tạo tất cả trạng thái hàng xóm, tính g(n) (tăng chi phí thêm 1), thêm vào hàng đợi nếu chưa thăm hoặc có g(n) thấp hơn.
3.	Tiếp tục cho đến khi tìm thấy mục tiêu hoặc hàng đợi rỗng.
o	Đặc điểm: UCS đảm bảo tối ưu trong 8-puzzle (đường đi ngắn nhất) và hoàn chỉnh trong không gian hữu hạn.
Ưu điểm
•	Tối ưu: Tìm đường đi ngắn nhất trong 8-puzzle dựa trên chi phí đường đi.
•	Hoàn chỉnh: Tìm lời giải nếu tồn tại trong không gian hữu hạn (~362,880 trạng thái).
•	Ứng dụng: Phù hợp cho bài toán tìm đường hoặc 8-puzzle khi cần đường đi tối ưu mà không có heuristic.
•	Đơn giản: Dễ triển khai, chỉ dựa trên chi phí đường đi.
Nhược điểm
•	Tốn tài nguyên: Hàng đợi ưu tiên cần lưu nhiều trạng thái, nhiều hơn DFS/IDS.
•	Chậm hơn Informed Search: Không dùng heuristic, khám phá nhiều trạng thái hơn A* hoặc Greedy.
•	Không hiệu quả trong không gian lớn: Khám phá tất cả trạng thái ở mức chi phí thấp trước, làm chậm với bài toán phức tạp.
•	Hạn chế: Kém hơn A* trong 8-puzzle khi có heuristic tốt.
Chi tiết bổ sung
•	Thời gian: O(b^d), với b là số nhánh, d là độ sâu, chậm hơn A*.
•	Không gian: O(b^d), lưu hàng đợi ưu tiên.
•	So sánh: 
o	BFS: Tương tự UCS trong 8-puzzle (chi phí đồng đều), tốn tài nguyên.
o	DFS: Nhanh, không tối ưu.
o	IDS: Tối ưu, tiết kiệm tài nguyên hơn.
o	Greedy/A*: Nhanh hơn, hiệu quả hơn với heuristic.
•	Hiệu suất: Tối ưu nhưng chậm hơn A*.
Nhận xét trên 8-puzzle
•	Hiệu quả: Tốt khi cần đường đi ngắn nhất mà không có heuristic, nhưng không nhanh bằng A*.
•	Thực tiễn: Phù hợp cho 8-puzzle khi thiếu heuristic, nhưng A* vượt trội hơn.
•	Hạn chế: Tốn tài nguyên, không lý tưởng cho không gian trạng thái lớn.
```
![ucs](https://github.com/user-attachments/assets/a96d5a07-2352-4bdd-9249-21729c0c0623)
```
2.1.4.Iterative Deepening DFS (IDS):
Mô tả
•	Cơ chế hoạt động: 
o	IDS là thuật toán tìm kiếm không có thông tin (uninformed search), kết hợp ưu điểm của Breadth-First Search (BFS) và Depth-First Search (DFS) bằng cách thực hiện DFS nhiều lần với giới hạn độ sâu tăng dần.
o	Bắt đầu từ trạng thái ban đầu của 8-puzzle, IDS duyệt sâu từng nhánh với giới hạn độ sâu, tăng giới hạn nếu không tìm thấy mục tiêu.
o	Sử dụng ngăn xếp (thường qua đệ quy) để thực hiện DFS, chỉ lưu trạng thái trên nhánh hiện tại.
o	Với 8-puzzle: 
	Trạng thái: Bảng 3x3 (ví dụ: [[1,2,3], [4,0,5], [7,8,6]], 0 là ô trống).
	Hàng xóm: Cấu hình sau di chuyển ô trống (lên, xuống, trái, phải).
	IDS duyệt sâu từng nhánh, hướng tới mục tiêu ([[1,2,3], [4,5,6], [7,8,0]]).
o	Quy trình: 
1.	Bắt đầu với độ sâu giới hạn = 0.
2.	Thực hiện DFS với giới hạn độ sâu: 
	Thêm trạng thái ban đầu vào ngăn xếp, đánh dấu đã thăm.
	Lấy trạng thái trên cùng, nếu là mục tiêu thì dừng.
	Nếu độ sâu hiện tại < giới hạn, tạo hàng xóm, thêm vào ngăn xếp nếu chưa thăm.
3.	Nếu không tìm thấy mục tiêu, tăng độ sâu và lặp lại.
4.	Tiếp tục cho đến khi tìm thấy mục tiêu hoặc hết trạng thái.
o	Đặc điểm: IDS đảm bảo tìm đường đi ngắn nhất như BFS, nhưng tiết kiệm tài nguyên hơn.
Ưu điểm
•	Tối ưu: Tìm đường đi ngắn nhất trong 8-puzzle, tương tự BFS.
•	Tiết kiệm tài nguyên: Chỉ lưu nhánh hiện tại, ít hơn BFS/UCS.
•	Hoàn chỉnh: Tìm lời giải nếu tồn tại trong không gian hữu hạn (~362,880 trạng thái).
•	Ứng dụng: Phù hợp cho 8-puzzle khi cần đường đi ngắn nhất và tài nguyên hạn chế.
Nhược điểm
•	Chậm hơn BFS: Lặp lại các mức nông làm tăng số trạng thái duyệt.
•	Không hiệu quả bằng Informed Search: Không dùng heuristic, khám phá nhiều trạng thái hơn A* hoặc Greedy.
•	Tốn tài nguyên cho trạng thái lặp: Tái khám phá các mức nông làm giảm hiệu suất.
•	Hạn chế: Không phù hợp cho không gian trạng thái rất lớn (như 15-puzzle).
Chi tiết bổ sung
•	Thời gian: O(b^d), hằng số cao hơn BFS do lặp lại, với b là số nhánh, d là độ sâu.
•	Không gian: O(bd), chỉ lưu nhánh hiện tại.
•	So sánh: 
o	BFS/UCS: Tối ưu, nhanh hơn, tốn tài nguyên hơn.
o	DFS: Nhanh, không tối ưu.
o	Greedy: Nhanh hơn, không tối ưu.
o	A*: Hiệu quả hơn, tối ưu.
•	Hiệu suất: Tối ưu, tiết kiệm tài nguyên nhưng chậm hơn A*.
Nhận xét trên 8-puzzle
•	Hiệu quả: Tốt khi cần tối ưu và tiết kiệm tài nguyên, nhưng không nhanh bằng A*.
•	Thực tiễn: Phù hợp cho 8-puzzle khi tài nguyên hạn chế, nhưng kém A*.
•	Hạn chế: Tốn thời gian do lặp lại, không lý tưởng cho không gian lớn.
```
![ids](https://github.com/user-attachments/assets/63d982ef-6c47-4fa3-93c5-e268840dbdff)
```


2.2.Các thuật toán tìm kiếm có thông tin (Informed Search)
2.2.1.Greedy Search:
Mô tả
•	Cơ chế hoạt động: 
o	Greedy Search là thuật toán tìm kiếm có thông tin (informed search), sử dụng hàm heuristic để ưu tiên trạng thái được ước tính gần trạng thái mục tiêu nhất.
o	Bắt đầu từ trạng thái ban đầu của 8-puzzle, Greedy Search chọn trạng thái hàng xóm có giá trị heuristic thấp nhất (không xem xét chi phí đường đi từ trạng thái ban đầu).
o	Sử dụng hàng đợi ưu tiên (priority queue) để lưu trữ các trạng thái, sắp xếp theo giá trị heuristic tăng dần. Trạng thái có heuristic thấp nhất được xử lý trước.
o	Với 8-puzzle: 
	Trạng thái: Bảng 3x3 (ví dụ: [[1,2,3], [4,0,5], [7,8,6]], 0 là ô trống).
	Hàng xóm: Cấu hình sau di chuyển ô trống (lên, xuống, trái, phải).
	Hàm heuristic: Thường là Manhattan Distance (tổng khoảng cách mỗi ô đến vị trí mục tiêu) hoặc số ô sai vị trí.
	Greedy Search mở rộng trạng thái dựa trên heuristic, hướng tới mục tiêu ([[1,2,3], [4,5,6], [7,8,0]]).
o	Quy trình: 
1.	Thêm trạng thái ban đầu vào hàng đợi ưu tiên với giá trị heuristic.
2.	Lặp lại: 
	Lấy trạng thái có heuristic thấp nhất từ hàng đợi.
	Nếu là trạng thái mục tiêu, dừng và trả về lời giải.
	Tạo tất cả trạng thái hàng xóm, tính heuristic, thêm vào hàng đợi nếu chưa thăm.
3.	Tiếp tục cho đến khi tìm thấy mục tiêu hoặc hàng đợi rỗng.
o	Đặc điểm: Greedy Search nhanh nhưng không đảm bảo tối ưu, vì chỉ dựa vào heuristic mà không tính chi phí đường đi.
Ưu điểm
•	Nhanh: Ưu tiên trạng thái gần mục tiêu theo heuristic, giảm số trạng thái cần duyệt.
•	Hiệu quả với heuristic tốt: Manhattan Distance giúp tìm lời giải nhanh trong 8-puzzle.
•	Ứng dụng: Phù hợp khi cần tốc độ hơn tính tối ưu, như 8-puzzle hoặc tìm đường đơn giản.
•	Đơn giản: Dễ triển khai với hàm heuristic phù hợp.
Nhược điểm
•	Không tối ưu: Có thể tìm đường đi dài hơn tối ưu do không xem xét chi phí đường đi.
•	Không hoàn chỉnh: Có thể kẹt trong nhánh không có mục tiêu, dù hiếm trong 8-puzzle (~362,880 trạng thái hữu hạn).
•	Phụ thuộc heuristic: Hiệu suất phụ thuộc vào chất lượng heuristic; heuristic kém làm giảm hiệu quả.
•	Hạn chế: Kém hơn A* (kết hợp heuristic và chi phí đường đi) về tính tối ưu và hiệu suất.
Chi tiết bổ sung
•	Thời gian: O(b^m), với b là số nhánh, m là độ sâu cây, nhanh hơn BFS.
•	Không gian: O(bm), lưu hàng đợi ưu tiên.
•	So sánh: 
o	BFS/UCS: Tối ưu, chậm hơn.
o	DFS: Nhanh, không tối ưu.
o	IDS: Tối ưu, chậm hơn.
o	A*: Tối ưu, hiệu quả hơn.
•	Hiệu suất: Nhanh nhưng không tối ưu.
Nhận xét trên 8-puzzle
•	Hiệu quả: Phù hợp khi ưu tiên tốc độ, nhưng không đảm bảo đường đi ngắn nhất.
•	Thực tiễn: Tốt cho 8-puzzle khi tài nguyên hạn chế và chấp nhận lời giải không tối ưu.
•	Hạn chế: Kém A* về tính tối ưu và độ tin cậy.
```
![greedy](https://github.com/user-attachments/assets/9c704523-028e-4563-a605-58a314907bcc)
```


2.2.2.A:*
Mô tả
•	Cơ chế hoạt động: 
o	A* là thuật toán tìm kiếm có thông tin (informed search), kết hợp chi phí đường đi (từ trạng thái ban đầu) và hàm heuristic (ước lượng chi phí đến mục tiêu) để tìm đường đi tối ưu.
o	Bắt đầu từ trạng thái ban đầu của 8-puzzle, A* chọn trạng thái có tổng chi phí f(n) = g(n) + h(n) thấp nhất, trong đó: 
	g(n): Chi phí đường đi từ trạng thái ban đầu đến trạng thái hiện tại (số bước di chuyển).
	h(n): Giá trị heuristic (thường là Manhattan Distance hoặc số ô sai vị trí).
o	Sử dụng hàng đợi ưu tiên (priority queue) để lưu trữ các trạng thái, sắp xếp theo f(n) tăng dần. Trạng thái có f(n) thấp nhất được xử lý trước.
o	Với 8-puzzle: 
	Trạng thái: Bảng 3x3 (ví dụ: [[1,2,3], [4,0,5], [7,8,6]], 0 là ô trống).
	Hàng xóm: Cấu hình sau di chuyển ô trống (lên, xuống, trái, phải).
	Hàm heuristic: Manhattan Distance (tổng khoảng cách mỗi ô đến vị trí mục tiêu).
	A* mở rộng trạng thái theo f(n), hướng tới mục tiêu ([[1,2,3], [4,5,6], [7,8,0]]).
o	Quy trình: 
1.	Thêm trạng thái ban đầu vào hàng đợi ưu tiên với f(n) = g(n) + h(n).
2.	Lặp lại: 
	Lấy trạng thái có f(n) thấp nhất từ hàng đợi.
	Nếu là trạng thái mục tiêu, dừng và trả về lời giải.
	Tạo tất cả trạng thái hàng xóm, tính f(n) = g(n) + h(n), thêm vào hàng đợi nếu chưa thăm hoặc có f(n) thấp hơn.
3.	Tiếp tục cho đến khi tìm thấy mục tiêu hoặc hàng đợi rỗng.
o	Đặc điểm: A* đảm bảo tối ưu nếu heuristic là admissible (không vượt quá chi phí thực tế, như Manhattan Distance) và hoàn chỉnh trong không gian hữu hạn.
Ưu điểm
•	Tối ưu: Tìm đường đi ngắn nhất trong 8-puzzle nếu heuristic admissible.
•	Hiệu quả: Nhờ heuristic như Manhattan Distance, khám phá ít trạng thái hơn BFS/UCS.
•	Ứng dụng: Lý tưởng cho 8-puzzle, tìm đường, lập kế hoạch, hoặc tối ưu hóa lộ trình.
•	Cân bằng: Kết hợp chi phí đường đi và heuristic để đạt hiệu suất cao.
Nhược điểm
•	Tốn tài nguyên: Hàng đợi ưu tiên cần lưu nhiều trạng thái, không tiết kiệm như DFS/IDS.
•	Phụ thuộc heuristic: Hiệu suất giảm nếu heuristic kém (như số ô sai vị trí).
•	Chậm hơn Greedy: Xem xét cả chi phí đường đi làm chậm hơn Greedy Search.
•	Hạn chế: Không phù hợp cho không gian trạng thái cực lớn nếu heuristic không được tối ưu hóa.
Chi tiết bổ sung
•	Thời gian: O(b^d), thực tế nhanh hơn nhờ heuristic.
•	Không gian: O(b^d), lưu hàng đợi ưu tiên.
•	So sánh: 
o	BFS/UCS: Tối ưu, khám phá nhiều trạng thái hơn.
o	DFS: Nhanh, không tối ưu.
o	IDS: Tối ưu, chậm hơn.
o	Greedy: Nhanh hơn, không tối ưu.
•	Hiệu suất: Tối ưu, hiệu quả hơn uninformed search.
Nhận xét trên 8-puzzle
•	Hiệu quả: Lựa chọn tốt nhất cho 8-puzzle, cân bằng tính tối ưu và hiệu suất.
•	Thực tiễn: Phù hợp khi cần đường đi ngắn nhất với tài nguyên vừa phải.
•	Hạn chế: Tốn tài nguyên hơn DFS/IDS, không lý tưởng cho không gian cực lớn.
```
![astart](https://github.com/user-attachments/assets/3c03f081-1abf-4887-8829-3a0f291bc331)
```


2.2.3.Iterative Deepening A* (IDA*)
Mô tả
•	Cơ chế hoạt động: 
o	IDA* là thuật toán tìm kiếm có thông tin (informed search), kết hợp A* với Iterative Deepening để giảm yêu cầu bộ nhớ.
o	Bắt đầu từ trạng thái ban đầu của 8-puzzle, IDA* sử dụng hàm đánh giá f(n) = g(n) + h(n) (g(n): chi phí đường đi, h(n): heuristic) và duyệt theo chiều sâu với giới hạn f(n) tăng dần.
o	Sử dụng ngăn xếp (thường qua đệ quy) để thực hiện tìm kiếm chiều sâu, chỉ giữ trạng thái trên nhánh hiện tại.
o	Với 8-puzzle: 
	Trạng thái: Bảng 3x3 (ví dụ: [[1,2,3], [4,0,5], [7,8,6]], 0 là ô trống).
	Hàng xóm: Cấu hình sau di chuyển ô trống (lên, xuống, trái, phải).
	Hàm heuristic: Manhattan Distance (tổng khoảng cách mỗi ô đến vị trí mục tiêu).
	IDA* mở rộng trạng thái theo f(n), hướng tới mục tiêu ([[1,2,3], [4,5,6], [7,8,0]]).
o	Quy trình: 
1.	Thêm trạng thái ban đầu vào ngăn xếp với ngưỡng f(n) = h(n).
2.	Thực hiện tìm kiếm chiều sâu: 
	Lấy trạng thái trên cùng, nếu là mục tiêu thì dừng.
	Nếu f(n) ≤ ngưỡng, tạo hàng xóm, thêm vào ngăn xếp.
	Nếu vượt ngưỡng, bỏ qua trạng thái.
3.	Nếu không tìm thấy mục tiêu, tăng ngưỡng (dựa trên f(n) nhỏ nhất vượt ngưỡng) và lặp lại.
4.	Tiếp tục cho đến khi tìm thấy mục tiêu hoặc hết trạng thái.
o	Đặc điểm: IDA* đảm bảo tối ưu như A* nếu heuristic admissible, nhưng tiết kiệm bộ nhớ hơn bằng cách tránh hàng đợi ưu tiên lớn.
Ưu điểm
•	Tối ưu: Tìm đường đi ngắn nhất trong 8-puzzle nếu heuristic admissible.
•	Tiết kiệm tài nguyên: Chỉ lưu trạng thái trên nhánh hiện tại, ít hơn A*.
•	Hiệu quả với heuristic tốt: Manhattan Distance giúp khám phá ít trạng thái hơn uninformed search.
•	Ứng dụng: Phù hợp cho 8-puzzle khi cần tính tối ưu và tài nguyên hạn chế.
Nhược điểm
•	Chậm hơn A:* Lặp lại tìm kiếm chiều sâu làm tăng số trạng thái duyệt.
•	Phụ thuộc heuristic: Hiệu suất giảm nếu heuristic kém (như số ô sai vị trí).
•	Không hoàn chỉnh trong trường hợp xấu: Có thể kẹt nếu heuristic dẫn đến nhánh sâu vô hạn, dù hiếm trong 8-puzzle (~362,880 trạng thái).
•	Hạn chế: Chậm hơn Greedy Search và không hiệu quả bằng A* cho không gian lớn.
Chi tiết bổ sung
•	Thời gian: O(b^d), nhanh hơn uninformed search nhờ heuristic.
•	Không gian: O(bd), chỉ lưu nhánh hiện tại.
•	So sánh: 
o	BFS/UCS: Tối ưu, khám phá nhiều trạng thái hơn.
o	DFS: Nhanh, không tối ưu.
o	IDS: Tối ưu, chậm hơn.
o	Greedy: Nhanh hơn, không tối ưu.
o	A*: Tối ưu, nhanh hơn, tốn tài nguyên hơn.
•	Hiệu suất: Tối ưu, tiết kiệm tài nguyên nhưng chậm hơn A*.
Nhận xét trên 8-puzzle
•	Hiệu quả: Tốt khi cần tối ưu và tiết kiệm tài nguyên, nhưng không nhanh bằng A*.
•	Thực tiễn: Phù hợp cho 8-puzzle khi tài nguyên hạn chế.
•	Hạn chế: Tốn thời gian hơn A*, không lý tưởng cho không gian cực lớn.
```
![ida](https://github.com/user-attachments/assets/f41b8560-f5c4-4821-8ad0-586ff38e64c7)
```


2.3. Tìm kiếm trong môi trường phức tạp
2.3.1.And Or Search:
Mô tả
•	Cơ chế hoạt động: 
o	AND-OR Search là thuật toán tìm kiếm chuyên biệt (specialized search), được thiết kế cho các bài toán có cây tìm kiếm phân cấp với các nút OR (lựa chọn một nhánh) và nút AND (yêu cầu tất cả nhánh con).
o	Bắt đầu từ trạng thái ban đầu của 8-puzzle, AND-OR Search xây dựng một cây AND-OR, trong đó: 
	Nút OR: Đại diện cho một trạng thái, có các lựa chọn (hành động di chuyển ô trống).
	Nút AND: Đại diện cho tập hợp các trạng thái con cần thỏa mãn để đạt mục tiêu.
o	Sử dụng tìm kiếm đệ quy để khám phá cây, đánh giá các nhánh OR và đảm bảo tất cả nhánh con trong nút AND dẫn đến lời giải.
o	Với 8-puzzle: 
	Trạng thái: Bảng 3x3 (ví dụ: [[1,2,3], [4,0,5], [7,8,6]], 0 là ô trống).
	Hàng xóm: Cấu hình sau di chuyển ô trống (lên, xuống, trái, phải).
	AND-OR Search mô hình hóa 8-puzzle như một bài toán phân cấp: mỗi trạng thái (nút OR) dẫn đến các hành động, và tất cả hành động cần phối hợp để đạt mục tiêu ([[1,2,3], [4,5,6], [7,8,0]]).
o	Quy trình: 
1.	Bắt đầu từ trạng thái ban đầu, xây dựng nút OR.
2.	Với mỗi nút OR: 
	Nếu là trạng thái mục tiêu, trả về lời giải.
	Tạo các nút AND cho tất cả hành động (di chuyển ô trống).
3.	Với mỗi nút AND: 
	Đệ quy khám phá tất cả nhánh con (trạng thái hàng xóm).
	Nếu tất cả nhánh con dẫn đến lời giải, đánh dấu nút AND là thành công.
4.	Quay lui nếu nhánh thất bại, tiếp tục cho đến khi tìm thấy lời giải hoặc hết trạng thái.
o	Đặc điểm: AND-OR Search phù hợp cho bài toán có mục tiêu phân cấp, nhưng phức tạp khi áp dụng cho 8-puzzle do không gian trạng thái không có cấu trúc AND rõ ràng.
Ưu điểm
•	Xử lý bài toán phân cấp: Hiệu quả cho các bài toán có mục tiêu phụ cần thỏa mãn đồng thời (dù 8-puzzle không phải trường hợp điển hình).
•	Hoàn chỉnh: Tìm được lời giải nếu tồn tại trong không gian hữu hạn (~362,880 trạng thái trong 8-puzzle).
•	Linh hoạt: Có thể kết hợp heuristic để ưu tiên nhánh OR, cải thiện hiệu suất.
•	Ứng dụng: Phù hợp cho bài toán lập kế hoạch, phân tích logic, hoặc các trò chơi có mục tiêu phụ, ít áp dụng trực tiếp cho 8-puzzle.
Nhược điểm
•	Phức tạp: Cần xây dựng cây AND-OR, không tự nhiên cho 8-puzzle vì bài toán không có cấu trúc AND rõ ràng.
•	Thời gian chạy cao: Khám phá nhiều nhánh OR và AND làm tăng số trạng thái duyệt so với A* hoặc Greedy Search.
•	Không tối ưu: Không đảm bảo đường đi ngắn nhất trong 8-puzzle, vì không sử dụng chi phí đường đi như A*.
•	Hạn chế: Ít hiệu quả cho 8-puzzle so với Informed Search (A*, IDA*) hoặc Uninformed Search (BFS, IDS).
Chi tiết bổ sung
•	Thời gian: O(b^m), với b~3, m là độ sâu cây, chậm hơn do khám phá nhánh AND-OR.
•	Không gian: O(bm), lưu nhánh hiện tại, tương tự DFS/IDA*.
•	So sánh: 
o	BFS/UCS: Tối ưu, khám phá nhiều trạng thái hơn.
o	DFS: Nhanh, không tối ưu, tiết kiệm bộ nhớ.
o	IDS: Tối ưu, chậm hơn, tiết kiệm bộ nhớ.
o	Greedy: Nhanh, không tối ưu.
o	A*/IDA*: Tối ưu, hiệu quả hơn nhiều.
•	Hiệu suất: Không tối ưu, chậm hơn A*/IDA* do cấu trúc phức tạp.
Nhận xét trên 8-puzzle
•	Hiệu quả: Không phải lựa chọn tốt cho 8-puzzle do cấu trúc AND-OR không tự nhiên.
•	Thực tiễn: Ít áp dụng, A* hoặc IDA* vượt trội hơn về hiệu suất và đơn giản.
•	Hạn chế: Phức tạp và không tận dụng được đặc điểm không gian trạng thái 8-puzzle.
```
![andorsearch](https://github.com/user-attachments/assets/8e6c6982-07eb-49e3-a90c-51238ab0e905)
```


2.3.2. Breadth-First Search trong môi trường Partially Observable
Mô tả
•	Cơ chế hoạt động: 
o	BFS là thuật toán tìm kiếm không có thông tin (uninformed search), nhưng trong môi trường quan sát một phần, nó được điều chỉnh để xử lý tập hợp trạng thái niềm tin (belief states) thay vì trạng thái đơn lẻ.
o	Trong 8-puzzle với quan sát một phần, tác nhân không biết toàn bộ cấu hình bảng 3x3 (ví dụ: chỉ thấy vị trí ô trống hoặc một số ô nhất định). Mỗi hành động (di chuyển ô trống) dẫn đến một tập hợp các trạng thái có thể xảy ra.
o	BFS sử dụng hàng đợi (queue) để lưu trữ các tập hợp trạng thái niềm tin, khám phá tất cả tập hợp ở mức hiện tại trước khi chuyển sang mức sâu hơn.
o	Với 8-puzzle: 
	Trạng thái niềm tin: Tập hợp các cấu hình bảng 3x3 khả thi dựa trên quan sát (ví dụ: ô trống ở [1,1], nhưng các ô khác chưa biết).
	Hàng xóm: Các tập hợp trạng thái niềm tin mới sau khi thực hiện hành động (di chuyển ô trống lên, xuống, trái, phải).
	BFS mở rộng cây tìm kiếm trên không gian niềm tin, hướng tới tập hợp trạng thái chứa mục tiêu ([[1,2,3], [4,5,6], [7,8,0]]).
o	Quy trình: 
1.	Thêm tập hợp trạng thái niềm tin ban đầu vào hàng đợi, đánh dấu đã thăm.
2.	Lặp lại: 
	Lấy tập hợp trạng thái đầu tiên từ hàng đợi.
	Nếu tập hợp chứa trạng thái mục tiêu (dựa trên quan sát), dừng và trả về lời giải.
	Tạo tất cả tập hợp trạng thái niềm tin hàng xóm (thực hiện hành động trên mỗi trạng thái trong tập hợp), thêm vào hàng đợi nếu chưa thăm.
3.	Tiếp tục cho đến khi tìm thấy mục tiêu hoặc hàng đợi rỗng.
o	Đặc điểm: BFS trong môi trường quan sát một phần đảm bảo tìm đường đi ngắn nhất trên không gian niềm tin, nhưng phức tạp hơn do quản lý tập hợp trạng thái.
Ưu điểm
•	Tối ưu: Tìm đường đi ngắn nhất trên không gian trạng thái niềm tin trong 8-puzzle, nếu mục tiêu có thể xác định qua quan sát.
•	Hoàn chỉnh: Tìm lời giải nếu tồn tại trong không gian hữu hạn (~362,880 trạng thái trong 8-puzzle).
•	Đơn giản: Dễ điều chỉnh từ BFS chuẩn, không cần heuristic, phù hợp khi không có thông tin bổ sung.
•	Ứng dụng: Hữu ích trong các bài toán quan sát một phần như robot điều hướng hoặc trò chơi với thông tin ẩn.
Nhược điểm
•	Phức tạp: Quản lý tập hợp trạng thái niềm tin làm tăng số trạng thái cần khám phá so với BFS chuẩn.
•	Không hiệu quả: Không sử dụng heuristic, dẫn đến duyệt nhiều tập hợp trạng thái hơn so với Informed Search (như A*).
•	Khó áp dụng cho 8-puzzle: Quan sát một phần không tự nhiên trong 8-puzzle (thường giả định biết toàn bộ bảng), làm BFS trở nên cồng kềnh.
•	Hạn chế: Kém hiệu quả so với các phương pháp chuyên biệt (như Belief State Search hoặc POMDP) trong môi trường quan sát một phần.
Chi tiết bổ sung
•	Thời gian: O(b^d), với b là số nhánh trung bình, d là độ sâu, nhưng phức tạp hơn do tập hợp trạng thái lớn.
•	Không gian: O(b^d), lưu trữ các tập hợp trạng thái niềm tin trong hàng đợi.
•	So sánh: 
o	BFS chuẩn: Tối ưu, đơn giản hơn, nhưng chỉ áp dụng khi biết toàn bộ trạng thái.
o	DFS: Nhanh, không tối ưu, tiết kiệm bộ nhớ hơn.
o	IDS: Tối ưu, tiết kiệm bộ nhớ, nhưng chậm hơn.
o	Greedy/A*/IDA*: Hiệu quả hơn nếu có heuristic tốt.
•	Hiệu suất: Tối ưu nhưng không hiệu quả do không gian trạng thái niềm tin lớn.
Nhận xét trên 8-puzzle
•	Hiệu quả: Không phải lựa chọn tốt cho 8-puzzle trong môi trường quan sát một phần do phức tạp và thiếu heuristic.
•	Thực tiễn: Ít áp dụng, vì 8-puzzle thường giả định quan sát đầy đủ; A* hoặc Belief State Search phù hợp hơn.
•	Hạn chế: Phù hợp hơn cho bài toán có cấu trúc quan sát một phần rõ ràng (như robot với cảm biến hạn chế).
```
![partialbfs](https://github.com/user-attachments/assets/d63403aa-ca71-490c-bde3-c641316a3fea)
```
2.3.3.Unknown Environmen (Môi trường ẩn với thuật toán BFS):
Mô tả
•	Cơ chế hoạt động: 
o	BFS là thuật toán tìm kiếm không có thông tin (uninformed search), nhưng trong môi trường ẩn, nó được điều chỉnh để xử lý thiếu thông tin về không gian trạng thái (ví dụ: không biết trước các trạng thái hàng xóm hoặc hiệu ứng của hành động).
o	Trong 8-puzzle với môi trường ẩn, tác nhân không biết trước các quy tắc di chuyển ô trống (ví dụ: không biết ô trống có thể di chuyển lên/xuống/trái/phải ở một số trạng thái) và phải học qua thử nghiệm.
o	BFS sử dụng hàng đợi (queue) để lưu trữ các trạng thái hoặc tập hợp trạng thái dự đoán, khám phá tất cả trạng thái ở mức hiện tại trước khi chuyển sang mức sâu hơn, đồng thời cập nhật kiến thức về môi trường qua các hành động.
o	Với 8-puzzle: 
	Trạng thái: Bảng 3x3 (ví dụ: [[1,2,3], [4,0,5], [7,8,6]], 0 là ô trống).
	Hàng xóm: Không biết trước, chỉ được phát hiện khi thử di chuyển ô trống.
	BFS xây dựng cây tìm kiếm, thử các hành động khả thi và học cách di chuyển, hướng tới mục tiêu ([[1,2,3], [4,5,6], [7,8,0]]).
o	Quy trình: 
1.	Thêm trạng thái ban đầu vào hàng đợi, đánh dấu đã thăm.
2.	Lặp lại: 
	Lấy trạng thái đầu tiên từ hàng đợi.
	Nếu là trạng thái mục tiêu, dừng và trả về lời giải.
	Thử tất cả hành động khả thi (di chuyển ô trống), cập nhật kiến thức về hàng xóm, thêm trạng thái mới vào hàng đợi nếu chưa thăm.
3.	Tiếp tục cho đến khi tìm thấy mục tiêu hoặc hàng đợi rỗng.
o	Đặc điểm: BFS trong môi trường ẩn đảm bảo tìm đường đi ngắn nhất nếu môi trường được học đầy đủ, nhưng phức tạp do cần khám phá và cập nhật kiến thức.
Ưu điểm
•	Tối ưu: Tìm đường đi ngắn nhất trong 8-puzzle nếu môi trường được khám phá đầy đủ.
•	Hoàn chỉnh: Tìm lời giải nếu tồn tại trong không gian hữu hạn (~362,880 trạng thái).
•	Đơn giản: Không cần heuristic, dễ điều chỉnh từ BFS chuẩn cho môi trường ẩn.
•	Ứng dụng: Phù hợp cho bài toán như robot học môi trường hoặc trò chơi với quy tắc ẩn.
Nhược điểm
•	Phức tạp: Cần lưu trữ và cập nhật kiến thức về môi trường, làm tăng số trạng thái cần duyệt.
•	Không hiệu quả: Khám phá mù nhiều trạng thái hơn so với Informed Search (như A*) nếu môi trường chưa được học.
•	Khó áp dụng cho 8-puzzle: Môi trường ẩn không tự nhiên trong 8-puzzle (thường giả định biết quy tắc di chuyển), làm BFS trở nên không thực tiễn.
•	Hạn chế: Kém hiệu quả so với các phương pháp chuyên biệt (như Reinforcement Learning hoặc Online Search) trong môi trường ẩn.
Chi tiết bổ sung
•	Thời gian: O(b^d), với b là số nhánh trung bình, d là độ sâu, chậm hơn do cần học môi trường.
•	Không gian: O(b^d), lưu trữ các trạng thái trong hàng đợi.
•	So sánh: 
o	BFS chuẩn: Tối ưu, đơn giản hơn, áp dụng khi biết môi trường.
o	DFS: Nhanh, không tối ưu, tiết kiệm bộ nhớ hơn.
o	IDS: Tối ưu, tiết kiệm bộ nhớ, nhưng chậm hơn.
o	Greedy/A*/IDA*: Hiệu quả hơn nếu có heuristic.
•	Hiệu suất: Tối ưu nhưng không hiệu quả do khám phá môi trường ẩn.
Nhận xét trên 8-puzzle
•	Hiệu quả: Không phải lựa chọn tốt cho 8-puzzle trong môi trường ẩn do phức tạp và thiếu heuristic.
•	Thực tiễn: Ít áp dụng, vì 8-puzzle thường giả định biết quy tắc; A* hoặc Q-Learning phù hợp hơn.
•	Hạn chế: Phù hợp hơn cho bài toán với môi trường thực sự ẩn (như điều hướng robot).
```
![beliefstatebfs](https://github.com/user-attachments/assets/6828e049-dc52-49ad-b2a0-7320f566d34a)
```

2.4.Tìm kiếm trong môi trường có ràng buộc (áp dụng trên Sudoku)
2.4.1.Backtracking Search
Mô tả
•	Cơ chế hoạt động: 
o	Backtracking Search là thuật toán giải bài toán CSP, thử gán giá trị cho các biến (ô trong 8-puzzle) và quay lui nếu gán không thỏa mãn ràng buộc.
o	Trong 8-puzzle, bài toán được mô hình hóa như CSP: 
	Biến: Mỗi ô trong bảng 3x3 (9 ô).
	Miền giá trị: Các số {0, 1, 2, ..., 8}, với 0 là ô trống.
	Ràng buộc: Mỗi số chỉ xuất hiện một lần; ô trống có thể di chuyển đến vị trí hợp lệ (lên, xuống, trái, phải); trạng thái cuối phải là [[1,2,3], [4,5,6], [7,8,0]].
o	Backtracking Search thử gán số cho từng ô, kiểm tra ràng buộc, và quay lui nếu gán dẫn đến trạng thái không hợp lệ.
o	Sử dụng tìm kiếm đệ quy để khám phá các gán giá trị, ưu tiên thử tất cả giá trị khả thi cho một ô trước khi chuyển sang ô tiếp theo.
o	Với 8-puzzle: 
	Trạng thái: Bảng 3x3 (ví dụ: [[1,2,3], [4,0,5], [7,8,6]], 0 là ô trống).
	Hành động: Gán số cho ô, đảm bảo tính duy nhất và khả năng di chuyển ô trống.
	Backtracking xây dựng trạng thái từ trạng thái ban đầu, hướng tới mục tiêu.
o	Quy trình: 
1.	Chọn một ô chưa gán giá trị.
2.	Thử gán một giá trị từ miền (0-8), kiểm tra ràng buộc (duy nhất, di chuyển hợp lệ).
3.	Nếu hợp lệ, chuyển sang ô tiếp theo và lặp lại.
4.	Nếu không hợp lệ hoặc không tìm được lời giải, quay lui, thử giá trị khác.
5.	Tiếp tục cho đến khi tất cả ô được gán đúng hoặc hết giá trị khả thi.
o	Đặc điểm: Backtracking đảm bảo tìm lời giải nếu tồn tại, nhưng không tối ưu về số bước di chuyển trong 8-puzzle.
Ưu điểm
•	Đơn giản: Dễ triển khai, chỉ cần kiểm tra ràng buộc và quay lui.
•	Hoàn chỉnh: Đảm bảo tìm lời giải nếu tồn tại trong không gian hữu hạn (~362,880 trạng thái trong 8-puzzle).
•	Linh hoạt: Có thể áp dụng cho bất kỳ bài toán CSP nào, dù 8-puzzle không phải trường hợp lý tưởng.
•	Ứng dụng: Hữu ích cho các bài toán CSP như Sudoku, 8-puzzle (khi mô hình hóa như CSP), hoặc bài toán tô màu đồ thị.
Nhược điểm
•	Không tối ưu: Không đảm bảo đường đi ngắn nhất trong 8-puzzle, vì chỉ tìm trạng thái thỏa mãn chứ không xem xét chi phí di chuyển.
•	Chậm với không gian lớn: Khám phá nhiều gán giá trị không cần thiết, đặc biệt nếu không có tối ưu hóa.
•	Phức tạp cho 8-puzzle: Mô hình hóa 8-puzzle như CSP (gán số cho ô) không tự nhiên, kém hiệu quả hơn tìm kiếm trạng thái (như A*).
•	Hạn chế: Kém hơn A* hoặc BFS trong 8-puzzle do không tận dụng cấu trúc không gian trạng thái.
Chi tiết bổ sung
•	Thời gian: O(b^d), với b là số giá trị trong miền, d là số biến, chậm hơn do thử nhiều gán.
•	Không gian: O(d), lưu trạng thái gán hiện tại, tiết kiệm hơn BFS.
•	So sánh: 
o	BFS/UCS: Tối ưu, khám phá nhiều trạng thái hơn.
o	DFS: Nhanh, không tối ưu, tiết kiệm bộ nhớ.
o	IDS: Tối ưu, chậm hơn, tiết kiệm bộ nhớ.
o	Greedy/A*/IDA*: Hiệu quả hơn, tối ưu cho 8-puzzle.
•	Hiệu suất: Hoàn chỉnh nhưng không hiệu quả cho 8-puzzle.
Nhận xét trên 8-puzzle
•	Hiệu quả: Không phải lựa chọn tốt cho 8-puzzle do mô hình CSP phức tạp và không tối ưu.
•	Thực tiễn: Ít áp dụng, A* hoặc IDA* hiệu quả hơn nhiều.
•	Hạn chế: Phù hợp hơn cho bài toán CSP rõ ràng như Sudoku.
```
![backtracking](https://github.com/user-attachments/assets/cf5320cf-17d3-40eb-b2d4-cfc18850d13f)
```

2.4.2.Forward Checking:
Mô tả
•	Cơ chế hoạt động: 
o	Forward Checking là một kỹ thuật tối ưu hóa cho Backtracking Search trong bài toán CSP, sử dụng DFS để gán giá trị cho các biến và kiểm tra ràng buộc trước để loại bỏ các giá trị không khả thi trong miền của các biến liên quan.
o	Trong 8-puzzle, bài toán được mô hình hóa như CSP: 
	Biến: Mỗi ô trong bảng 3x3 (9 ô).
	Miền giá trị: Các số {0, 1, 2, ..., 8}, với 0 là ô trống.
	Ràng buộc: Mỗi số xuất hiện duy nhất; ô trống phải di chuyển hợp lệ (lên, xuống, trái, phải); trạng thái cuối là [[1,2,3], [4,5,6], [7,8,0]].
o	Forward Checking kết hợp DFS để gán số cho ô, sau mỗi lần gán, cập nhật miền giá trị của các ô liên quan (ô lân cận hoặc ô chưa gán) và quay lui nếu miền của ô nào đó rỗng.
o	Sử dụng tìm kiếm đệ quy để thử gán giá trị, ưu tiên đi sâu vào một nhánh và kiểm tra ràng buộc trước.
o	Với 8-puzzle: 
	Trạng thái: Bảng 3x3 (ví dụ: [[1,2,3], [4,0,5], [7,8,6]], 0 là ô trống).
	Hành động: Gán số cho ô, kiểm tra tính duy nhất và khả năng di chuyển.
	Forward Checking giảm miền giá trị để hướng tới mục tiêu.
o	Quy trình: 
1.	Chọn một ô chưa gán, thử một giá trị từ miền.
2.	Kiểm tra ràng buộc, gán giá trị, và cập nhật miền của các ô liên quan (loại bỏ giá trị không khả thi).
3.	Nếu miền của ô nào đó rỗng, quay lui và thử giá trị khác.
4.	Nếu hợp lệ, chuyển sang ô tiếp theo và lặp lại.
5.	Tiếp tục cho đến khi tất cả ô được gán đúng hoặc hết giá trị khả thi.
o	Đặc điểm: Forward Checking với DFS giảm không gian tìm kiếm so với Backtracking đơn thuần, nhưng không đảm bảo tối ưu về số bước di chuyển trong 8-puzzle.
Ưu điểm
•	Nhanh hơn Backtracking: Kiểm tra ràng buộc trước giúp loại bỏ sớm các nhánh không khả thi, giảm số trạng thái cần duyệt.
•	Hoàn chỉnh: Đảm bảo tìm lời giải nếu tồn tại trong không gian hữu hạn (~362,880 trạng thái).
•	Hiệu quả hơn Backtracking: Giảm miền giá trị sớm, đặc biệt khi ràng buộc chặt (như tính duy nhất trong 8-puzzle).
•	Ứng dụng: Hữu ích cho bài toán CSP như Sudoku, 8-puzzle (khi mô hình hóa như CSP), hoặc lập lịch.
Nhược điểm
•	Không tối ưu: Không đảm bảo đường đi ngắn nhất trong 8-puzzle, vì chỉ tìm trạng thái thỏa mãn ràng buộc.
•	Vẫn chậm với bài toán khó: Nếu miền giá trị lớn hoặc ràng buộc phức tạp, Forward Checking vẫn phải quay lui nhiều lần.
•	Phức tạp cho 8-puzzle: Mô hình CSP không tự nhiên cho 8-puzzle, kém hiệu quả hơn tìm kiếm trạng thái (như A*).
•	Hạn chế: Kém hơn A* hoặc BFS trong 8-puzzle do không tận dụng cấu trúc không gian trạng thái.
Chi tiết bổ sung
•	Thời gian: O(b^d), với b là số giá trị trong miền, d là số biến, nhanh hơn Backtracking nhưng chậm hơn A*.
•	Không gian: O(d), lưu trạng thái gán hiện tại, tiết kiệm hơn BFS.
•	So sánh: 
o	Backtracking: Chậm hơn, khám phá nhiều trạng thái hơn.
o	BFS/UCS: Tối ưu, tốn nhiều tài nguyên hơn.
o	DFS: Nhanh, không tối ưu.
o	IDS: Tối ưu, chậm hơn.
o	Greedy/A*/IDA*: Hiệu quả hơn, tối ưu cho 8-puzzle.
•	Hiệu suất: Hoàn chỉnh, nhanh hơn Backtracking nhưng không hiệu quả cho 8-puzzle.
Nhận xét trên 8-puzzle
•	Hiệu quả: Không phải lựa chọn tốt cho 8-puzzle do mô hình CSP phức tạp và không tối ưu.
•	Thực tiễn: Ít áp dụng, A* hoặc IDA* vượt trội hơn.
•	Hạn chế: Phù hợp hơn cho bài toán CSP rõ ràng như Sudoku.
```
![dfsfc](https://github.com/user-attachments/assets/21458673-da06-45ad-acf2-c56168e7f234)
```

2.4.3.AC-3 (Arc Consistency):
Mô tả
•	Cơ chế hoạt động: 
o	AC-3 là một thuật toán duy trì tính nhất quán cung (arc consistency) trong bài toán CSP, kết hợp với DFS để tìm lời giải bằng cách gán giá trị cho các biến.
o	Trong 8-puzzle, bài toán được mô hình hóa như CSP: 
	Biến: Mỗi ô trong bảng 3x3 (9 ô).
	Miền giá trị: Các số {0, 1, 2, ..., 8}, với 0 là ô trống.
	Ràng buộc: Mỗi số xuất hiện duy nhất; ô trống phải di chuyển hợp lệ (lên, xuống, trái, phải); trạng thái cuối là [[1,2,3], [4,5,6], [7,8,0]].
o	AC-3 đảm bảo rằng mỗi cung (ràng buộc giữa hai ô) là nhất quán bằng cách loại bỏ các giá trị trong miền không thỏa mãn ràng buộc, trước khi DFS gán giá trị.
o	DFS sử dụng tìm kiếm đệ quy để thử gán giá trị, quay lui nếu không tìm được lời giải, tận dụng miền giá trị đã được AC-3 thu hẹp.
o	Với 8-puzzle: 
	Trạng thái: Bảng 3x3 (ví dụ: [[1,2,3], [4,0,5], [7,8,6]], 0 là ô trống).
	Hành động: Gán số cho ô, kiểm tra tính duy nhất và khả năng di chuyển.
	AC-3 thu hẹp miền, DFS tìm trạng thái mục tiêu.
o	Quy trình: 
1.	Chạy AC-3: Kiểm tra tất cả cung (ràng buộc), loại bỏ giá trị không thỏa mãn từ miền của các ô liên quan. Nếu miền rỗng, bài toán vô nghiệm.
2.	Dùng DFS: 
	Chọn ô chưa gán, thử một giá trị từ miền đã thu hẹp.
	Gán giá trị, chạy AC-3 để cập nhật miền của ô liên quan.
	Nếu hợp lệ, chuyển sang ô tiếp theo; nếu không, quay lui.
3.	Tiếp tục cho đến khi tất cả ô được gán đúng hoặc hết giá trị khả thi.
o	Đặc điểm: AC-3 với DFS giảm không gian tìm kiếm hơn Backtracking và Forward Checking, nhưng không đảm bảo tối ưu về số bước di chuyển trong 8-puzzle.
Ưu điểm
•	Hiệu quả hơn Backtracking/Forward Checking: AC-3 thu hẹp miền giá trị trước, giảm số lần quay lui trong DFS.
•	Hoàn chỉnh: Đảm bảo tìm lời giải nếu tồn tại trong không gian hữu hạn (~362,880 trạng thái).
•	Tối ưu hóa miền: Loại bỏ sớm các giá trị không khả thi, đặc biệt hiệu quả với ràng buộc chặt (như tính duy nhất).
•	Ứng dụng: Hữu ích cho bài toán CSP như Sudoku, 8-puzzle (khi mô hình hóa như CSP), hoặc bài toán lập lịch.
Nhược điểm
•	Không tối ưu: Không đảm bảo đường đi ngắn nhất trong 8-puzzle, vì chỉ tìm trạng thái thỏa mãn ràng buộc.
•	Phức tạp hơn: AC-3 yêu cầu quản lý cung và miền, tốn tài nguyên hơn Backtracking đơn thuần.
•	Không tự nhiên cho 8-puzzle: Mô hình CSP phức tạp, kém hiệu quả hơn tìm kiếm trạng thái (như A*).
•	Hạn chế: Kém hơn A* hoặc IDA* trong 8-puzzle do không tận dụng cấu trúc không gian trạng thái.
Chi tiết bổ sung
•	Thời gian: O(b^d), với b là số giá trị trong miền, d là số biến, nhanh hơn Backtracking nhưng chậm hơn A*.
•	Không gian: O(d), lưu trạng thái gán và miền, tiết kiệm hơn BFS.
•	So sánh: 
o	Backtracking: Chậm hơn, khám phá nhiều trạng thái hơn.
o	Forward Checking: Hiệu quả hơn Backtracking, nhưng kém AC-3.
o	BFS/UCS: Tối ưu, tốn nhiều tài nguyên hơn.
o	DFS: Nhanh, không tối ưu.
o	Greedy/A*/IDA*: Hiệu quả hơn, tối ưu cho 8-puzzle.
•	Hiệu suất: Hoàn chỉnh, nhanh hơn Forward Checking nhưng không hiệu quả cho 8-puzzle.
Nhận xét trên 8-puzzle
•	Hiệu quả: Không phải lựa chọn tốt cho 8-puzzle do mô hình CSP phức tạp và không tối ưu.
•	Thực tiễn: Ít áp dụng, A* hoặc IDA* vượt trội hơn.
•	Hạn chế: Phù hợp hơn cho bài toán CSP rõ ràng như Sudoku.
```
![dfsac3](https://github.com/user-attachments/assets/ebe53b93-248f-47c5-9ce7-6617f2578db7)
```

2.5. Tìm kiếm cục bộ
2.5.1.Beam Search
Mô tả
•	Cơ chế hoạt động: 
o	Beam Search là thuật toán tìm kiếm cục bộ (local search), kết hợp ý tưởng của Breadth-First Search (BFS) và tìm kiếm heuristic, nhưng chỉ giữ một số lượng giới hạn (beam width) các trạng thái tốt nhất ở mỗi mức.
o	Trong 8-puzzle, Beam Search bắt đầu từ trạng thái ban đầu, mở rộng các trạng thái hàng xóm và chỉ giữ lại k trạng thái có giá trị heuristic thấp nhất (k là beam width).
o	Sử dụng hàng đợi ưu tiên (priority queue) để lưu trữ và sắp xếp các trạng thái dựa trên hàm heuristic (thường là Manhattan Distance).
o	Với 8-puzzle: 
	Trạng thái: Bảng 3x3 (ví dụ: [[1,2,3], [4,0,5], [7,8,6]], 0 là ô trống).
	Hàng xóm: Cấu hình sau di chuyển ô trống (lên, xuống, trái, phải).
	Hàm heuristic: Manhattan Distance (tổng khoảng cách mỗi ô đến vị trí mục tiêu).
	Beam Search hướng tới mục tiêu ([[1,2,3], [4,5,6], [7,8,0]]) bằng cách giới hạn không gian tìm kiếm.
o	Quy trình: 
1.	Thêm trạng thái ban đầu vào hàng đợi.
2.	Lặp lại: 
	Lấy tất cả trạng thái trong hàng đợi, tạo các trạng thái hàng xóm.
	Tính heuristic cho các hàng xóm, chọn k trạng thái có heuristic thấp nhất.
	Nếu một trạng thái là mục tiêu, dừng và trả về lời giải.
	Cập nhật hàng đợi với k trạng thái được chọn.
3.	Tiếp tục cho đến khi tìm thấy mục tiêu hoặc không còn trạng thái khả thi.
o	Đặc điểm: Beam Search nhanh nhưng không đảm bảo tối ưu hoặc hoàn chỉnh, vì giới hạn số trạng thái được khám phá.
Ưu điểm
•	Nhanh: Giới hạn beam width giảm số trạng thái cần duyệt so với BFS hoặc A*.
•	Hiệu quả với heuristic tốt: Manhattan Distance giúp Beam Search tập trung vào các trạng thái tiềm năng.
•	Tiết kiệm tài nguyên: Chỉ lưu k trạng thái mỗi lần, phù hợp khi tài nguyên hạn chế.
•	Ứng dụng: Hữu ích trong bài toán tìm kiếm lớn (như dịch máy, nhận dạng giọng nói) hoặc 8-puzzle khi ưu tiên tốc độ.
Nhược điểm
•	Không tối ưu: Có thể tìm đường đi dài hơn tối ưu do loại bỏ các trạng thái tiềm năng sớm.
•	Không hoàn chỉnh: Có thể bỏ lỡ lời giải nếu beam width quá nhỏ, đặc biệt trong không gian trạng thái phức tạp.
•	Phụ thuộc beam width: Hiệu suất phụ thuộc vào lựa chọn k; k nhỏ làm mất lời giải, k lớn tăng chi phí tính toán.
•	Hạn chế: Kém hơn A* hoặc IDA* trong 8-puzzle về tính tối ưu và độ tin cậy.
Chi tiết bổ sung
•	Thời gian: O(bk), với b là số nhánh trung bình, k là beam width, nhanh hơn BFS nhưng phụ thuộc k.
•	Không gian: O(k), lưu k trạng thái, tiết kiệm hơn BFS/A*.
•	So sánh: 
o	BFS/UCS: Tối ưu, khám phá nhiều trạng thái hơn.
o	DFS: Nhanh, không tối ưu.
o	IDS: Tối ưu, chậm hơn.
o	Greedy: Nhanh, không tối ưu, tương tự nhưng không giới hạn trạng thái.
o	A*/IDA*: Tối ưu, hiệu quả hơn.
•	Hiệu suất: Nhanh nhưng không tối ưu, phụ thuộc vào beam width.
Nhận xét trên 8-puzzle
•	Hiệu quả: Phù hợp khi ưu tiên tốc độ và chấp nhận lời giải không tối ưu.
•	Thực tiễn: Ít áp dụng cho 8-puzzle, vì A* hoặc IDA* hiệu quả hơn.
•	Hạn chế: Nguy cơ bỏ lỡ lời giải nếu beam width không phù hợp.
```
![beamsearch](https://github.com/user-attachments/assets/34313cbf-e7dd-497d-a4c7-b51bf8f311ee)
```
2.5.2	Simple Hill Climbing (HC):
Mô tả
•	Cơ chế hoạt động: 
o	Simple Hill Climbing là thuật toán tìm kiếm cục bộ (local search), bắt đầu từ trạng thái ban đầu và chọn trạng thái hàng xóm đầu tiên có giá trị hàm mục tiêu (heuristic) tốt hơn để cải thiện dần.
o	Trong 8-puzzle, nó sử dụng hàm heuristic (thường là Manhattan Distance hoặc số ô sai vị trí) để đánh giá trạng thái.
o	Không sử dụng hàng đợi, chỉ theo dõi trạng thái hiện tại và chuyển sang hàng xóm tốt hơn đầu tiên.
o	Với 8-puzzle: 
	Trạng thái: Bảng 3x3 (ví dụ: [[1,2,3], [4,0,5], [7,8,6]], 0 là ô trống).
	Hàng xóm: Cấu hình sau di chuyển ô trống (lên, xuống, trái, phải).
	Hàm heuristic: Manhattan Distance (tổng khoảng cách mỗi ô đến vị trí mục tiêu).
	Simple Hill Climbing hướng tới mục tiêu ([[1,2,3], [4,5,6], [7,8,0]]) bằng cách giảm heuristic.
o	Quy trình: 
1.	Bắt đầu từ trạng thái ban đầu, tính heuristic.
2.	Tạo các trạng thái hàng xóm, chọn trạng thái đầu tiên có heuristic thấp hơn hiện tại.
3.	Nếu không có hàng xóm nào tốt hơn, dừng (đạt cực đại cục bộ).
4.	Nếu trạng thái là mục tiêu, trả về lời giải; nếu không, chuyển sang hàng xóm và lặp lại.
o	Đặc điểm: Simple Hill Climbing nhanh nhưng dễ kẹt ở cực đại cục bộ, không đảm bảo tối ưu hoặc hoàn chỉnh.
Ưu điểm
•	Nhanh: Chỉ kiểm tra một số ít trạng thái hàng xóm, giảm chi phí tính toán.
•	Đơn giản: Dễ triển khai, không cần lưu trữ nhiều trạng thái.
•	Tiết kiệm tài nguyên: Chỉ theo dõi trạng thái hiện tại, phù hợp khi tài nguyên hạn chế.
•	Ứng dụng: Hữu ích trong bài toán tối ưu hóa đơn giản hoặc khi chấp nhận lời giải gần đúng.
Nhược điểm
•	Không tối ưu: Thường không tìm được đường đi ngắn nhất, vì chỉ chọn cải thiện cục bộ.
•	Không hoàn chỉnh: Dễ kẹt ở cực đại cục bộ, bỏ lỡ mục tiêu trong 8-puzzle.
•	Phụ thuộc heuristic: Hiệu suất phụ thuộc vào chất lượng heuristic; heuristic kém làm giảm hiệu quả.
•	Hạn chế: Kém hơn A* hoặc IDA* trong 8-puzzle về tính tối ưu và độ tin cậy.
Chi tiết bổ sung
•	Thời gian: O(bd), với b là số nhánh trung bình, d là số bước, rất nhanh nếu sớm đạt cực đại.
•	Không gian: O(1), chỉ lưu trạng thái hiện tại.
•	So sánh: 
o	BFS/UCS: Tối ưu, khám phá nhiều trạng thái hơn.
o	DFS: Nhanh, không tối ưu.
o	IDS: Tối ưu, chậm hơn.
o	Greedy/A*/IDA*: Hiệu quả hơn, tối ưu.
o	Beam Search: Linh hoạt hơn, nhưng vẫn không tối ưu.
•	Hiệu suất: Nhanh nhưng không đáng tin cậy trong 8-puzzle.
Nhận xét trên 8-puzzle
•	Hiệu quả: Phù hợp khi ưu tiên tốc độ và chấp nhận lời giải không tối ưu, nhưng hiếm khi đạt mục tiêu.
•	Thực tiễn: Ít áp dụng cho 8-puzzle, vì A* hoặc IDA* vượt trội hơn.
•	Hạn chế: Dễ kẹt ở cực đại cục bộ, không lý tưởng cho không gian trạng thái phức tạp.
```
![shc](https://github.com/user-attachments/assets/1bc80d35-1ae7-47f5-9ba1-26e79bd97167)
```
2.5.3.Stochastic Hill Climbing (SHC):
Mô tả
•	Cơ chế hoạt động: 
o	Stochastic Hill Climbing là thuật toán tìm kiếm cục bộ (local search), cải tiến từ Simple Hill Climbing bằng cách chọn ngẫu nhiên một trạng thái hàng xóm có giá trị hàm mục tiêu (heuristic) tốt hơn, thay vì chọn trạng thái đầu tiên.
o	Trong 8-puzzle, SHC sử dụng hàm heuristic (thường là Manhattan Distance) để đánh giá trạng thái và chọn ngẫu nhiên trong số các hàng xóm cải thiện heuristic.
o	Không sử dụng hàng đợi, chỉ theo dõi trạng thái hiện tại và chuyển sang hàng xóm được chọn ngẫu nhiên.
o	Với 8-puzzle: 
	Trạng thái: Bảng 3x3 (ví dụ: [[1,2,3], [4,0,5], [7,8,6]], 0 là ô trống).
	Hàng xóm: Cấu hình sau di chuyển ô trống (lên, xuống, trái, phải).
	Hàm heuristic: Manhattan Distance (tổng khoảng cách mỗi ô đến vị trí mục tiêu).
	SHC hướng tới mục tiêu ([[1,2,3], [4,5,6], [7,8,0]]) bằng cách giảm heuristic ngẫu nhiên.
o	Quy trình: 
1.	Bắt đầu từ trạng thái ban đầu, tính heuristic.
2.	Tạo các trạng thái hàng xóm, xác định các trạng thái có heuristic thấp hơn hiện tại.
3.	Chọn ngẫu nhiên một trạng thái từ các hàng xóm tốt hơn; nếu không có, dừng (đạt cực đại cục bộ).
4.	Nếu trạng thái là mục tiêu, trả về lời giải; nếu không, chuyển sang hàng xóm và lặp lại.
o	Đặc điểm: SHC nhanh, giảm nguy cơ kẹt ở cực đại cục bộ so với Simple Hill Climbing, nhưng không đảm bảo tối ưu hoặc hoàn chỉnh.
Ưu điểm
•	Nhanh: Chỉ kiểm tra một số ít trạng thái hàng xóm, giảm chi phí tính toán.
•	Giảm kẹt cục bộ: Lựa chọn ngẫu nhiên giúp thoát khỏi một số cực đại cục bộ, cải thiện so với Simple Hill Climbing.
•	Đơn giản: Dễ triển khai, không cần lưu trữ nhiều trạng thái.
•	Ứng dụng: Hữu ích trong bài toán tối ưu hóa hoặc khi chấp nhận lời giải gần đúng.
Nhược điểm
•	Không tối ưu: Không tìm được đường đi ngắn nhất trong 8-puzzle, vì chỉ cải thiện cục bộ.
•	Không hoàn chỉnh: Có thể bỏ lỡ mục tiêu do kẹt ở cực đại cục bộ hoặc lựa chọn ngẫu nhiên không hiệu quả.
•	Phụ thuộc heuristic: Hiệu suất phụ thuộc vào chất lượng heuristic; heuristic kém làm giảm hiệu quả.
•	Hạn chế: Kém hơn A* hoặc IDA* trong 8-puzzle về tính tối ưu và độ tin cậy.
Chi tiết bổ sung
•	Thời gian: O(bd), với b là số nhánh trung bình, d là số bước, nhanh nếu sớm đạt mục tiêu.
•	Không gian: O(1), chỉ lưu trạng thái hiện tại.
•	So sánh: 
o	BFS/UCS: Tối ưu, khám phá nhiều trạng thái hơn.
o	DFS: Nhanh, không tối ưu.
o	IDS: Tối ưu, chậm hơn.
o	Simple Hill Climbing: Dễ kẹt cục bộ hơn.
o	Greedy/A*/IDA*: Hiệu quả hơn, tối ưu.
•	Hiệu suất: Nhanh nhưng không đáng tin cậy trong 8-puzzle.
Nhận xét trên 8-puzzle
•	Hiệu quả: Phù hợp khi ưu tiên tốc độ và chấp nhận lời giải không tối ưu, nhưng hiếm khi đạt mục tiêu.
•	Thực tiễn: Ít áp dụng cho 8-puzzle, vì A* hoặc IDA* vượt trội hơn.
•	Hạn chế: Vẫn dễ kẹt ở cực đại cục bộ, không lý tưởng cho không gian trạng thái phức tạp.
```
![stochatichc](https://github.com/user-attachments/assets/b5f1ec17-f862-479e-b6d6-55cf7b61729c)
```
2.5.4.Simulated Annealing (SA):
Mô tả
•	Cơ chế hoạt động: 
o	Stochastic Hill Climbing là thuật toán tìm kiếm cục bộ (local search), cải tiến từ Simple Hill Climbing bằng cách chọn ngẫu nhiên một trạng thái hàng xóm có giá trị hàm mục tiêu (heuristic) tốt hơn, thay vì chọn trạng thái đầu tiên.
o	Trong 8-puzzle, SHC sử dụng hàm heuristic (thường là Manhattan Distance) để đánh giá trạng thái và chọn ngẫu nhiên trong số các hàng xóm cải thiện heuristic.
o	Không sử dụng hàng đợi, chỉ theo dõi trạng thái hiện tại và chuyển sang hàng xóm được chọn ngẫu nhiên.
o	Với 8-puzzle: 
	Trạng thái: Bảng 3x3 (ví dụ: [[1,2,3], [4,0,5], [7,8,6]], 0 là ô trống).
	Hàng xóm: Cấu hình sau di chuyển ô trống (lên, xuống, trái, phải).
	Hàm heuristic: Manhattan Distance (tổng khoảng cách mỗi ô đến vị trí mục tiêu).
	SHC hướng tới mục tiêu ([[1,2,3], [4,5,6], [7,8,0]]) bằng cách giảm heuristic ngẫu nhiên.
o	Quy trình: 
1.	Bắt đầu từ trạng thái ban đầu, tính heuristic.
2.	Tạo các trạng thái hàng xóm, xác định các trạng thái có heuristic thấp hơn hiện tại.
3.	Chọn ngẫu nhiên một trạng thái từ các hàng xóm tốt hơn; nếu không có, dừng (đạt cực đại cục bộ).
4.	Nếu trạng thái là mục tiêu, trả về lời giải; nếu không, chuyển sang hàng xóm và lặp lại.
o	Đặc điểm: SHC nhanh, giảm nguy cơ kẹt ở cực đại cục bộ so với Simple Hill Climbing, nhưng không đảm bảo tối ưu hoặc hoàn chỉnh.
Ưu điểm
•	Nhanh: Chỉ kiểm tra một số ít trạng thái hàng xóm, giảm chi phí tính toán.
•	Giảm kẹt cục bộ: Lựa chọn ngẫu nhiên giúp thoát khỏi một số cực đại cục bộ, cải thiện so với Simple Hill Climbing.
•	Đơn giản: Dễ triển khai, không cần lưu trữ nhiều trạng thái.
•	Ứng dụng: Hữu ích trong bài toán tối ưu hóa hoặc khi chấp nhận lời giải gần đúng.
Nhược điểm
•	Không tối ưu: Không tìm được đường đi ngắn nhất trong 8-puzzle, vì chỉ cải thiện cục bộ.
•	Không hoàn chỉnh: Có thể bỏ lỡ mục tiêu do kẹt ở cực đại cục bộ hoặc lựa chọn ngẫu nhiên không hiệu quả.
•	Phụ thuộc heuristic: Hiệu suất phụ thuộc vào chất lượng heuristic; heuristic kém làm giảm hiệu quả.
•	Hạn chế: Kém hơn A* hoặc IDA* trong 8-puzzle về tính tối ưu và độ tin cậy.
Chi tiết bổ sung
•	Thời gian: O(bd), với b là số nhánh trung bình, d là số bước, nhanh nếu sớm đạt mục tiêu.
•	Không gian: O(1), chỉ lưu trạng thái hiện tại.
•	So sánh: 
o	BFS/UCS: Tối ưu, khám phá nhiều trạng thái hơn.
o	DFS: Nhanh, không tối ưu.
o	IDS: Tối ưu, chậm hơn.
o	Simple Hill Climbing: Dễ kẹt cục bộ hơn.
o	Greedy/A*/IDA*: Hiệu quả hơn, tối ưu.
•	Hiệu suất: Nhanh nhưng không đáng tin cậy trong 8-puzzle.
Nhận xét trên 8-puzzle
•	Hiệu quả: Phù hợp khi ưu tiên tốc độ và chấp nhận lời giải không tối ưu, nhưng hiếm khi đạt mục tiêu.
•	Thực tiễn: Ít áp dụng cho 8-puzzle, vì A* hoặc IDA* vượt trội hơn.
•	Hạn chế: Vẫn dễ kẹt ở cực đại cục bộ, không lý tưởng cho không gian trạng thái phức tạp.
```
![simulateanneling](https://github.com/user-attachments/assets/09700b48-6b40-48c7-a77e-e3ea2c165173)
```
2.5.5. Genetic Algorithms
Mô tả
•	Cơ chế hoạt động: 
o	Genetic Algorithms là thuật toán tìm kiếm cục bộ (local search), lấy cảm hứng từ tiến hóa sinh học, sử dụng quần thể (population) các lời giải tiềm năng, tiến hóa qua các thế hệ bằng cách áp dụng chọn lọc, lai ghép (crossover), và đột biến (mutation).
o	Trong 8-puzzle, mỗi cá thể (individual) trong quần thể là một chuỗi di chuyển hoặc một trạng thái bảng 3x3, được đánh giá bằng hàm thích nghi (fitness function) (thường dựa trên Manhattan Distance hoặc số ô đúng vị trí).
o	GA tiến hóa quần thể để tìm trạng thái gần với mục tiêu.
o	Với 8-puzzle: 
	Trạng thái: Bảng 3x3 (ví dụ: [[1,2,3], [4,0,5], [7,8,6]], 0 là ô trống) hoặc chuỗi di chuyển.
	Hàng xóm: Không trực tiếp dùng; thay vào đó, tạo cá thể mới qua lai ghép và đột biến.
	Hàm thích nghi: Nghịch đảo của Manhattan Distance (giá trị càng cao càng tốt).
	GA hướng tới mục tiêu ([[1,2,3], [4,5,6], [7,8,0]]) qua các thế hệ.
o	Quy trình: 
1.	Khởi tạo quần thể ngẫu nhiên (các trạng thái hoặc chuỗi di chuyển).
2.	Đánh giá hàm thích nghi cho mỗi cá thể.
3.	Lặp lại: 
	Chọn lọc: Chọn các cá thể tốt (fitness cao) bằng phương pháp như roulette wheel.
	Lai ghép: Kết hợp hai cá thể để tạo cá thể mới (ví dụ: nối hai chuỗi di chuyển).
	Đột biến: Thay đổi ngẫu nhiên một phần cá thể (ví dụ: đổi một di chuyển).
4.	Cập nhật quần thể, kiểm tra nếu cá thể tốt nhất là mục tiêu thì dừng.
5.	Lặp lại cho đến khi đạt mục tiêu hoặc số thế hệ tối đa.
o	Đặc điểm: GA tìm kiếm toàn cục, giảm nguy cơ kẹt ở cực đại cục bộ, nhưng không đảm bảo tối ưu hoặc hoàn chỉnh.
Ưu điểm
•	Tìm kiếm toàn cục: Khám phá nhiều vùng trong không gian trạng thái, giảm kẹt ở cực đại cục bộ so với Hill Climbing.
•	Linh hoạt: Có thể áp dụng cho nhiều bài toán tối ưu hóa mà không cần hiểu rõ cấu trúc vấn đề.
•	Khả năng tiến hóa: Tạo ra lời giải tốt dần qua các thế hệ, đặc biệt khi quần thể đa dạng.
•	Ứng dụng: Hữu ích trong bài toán tối ưu hóa phức tạp, như 8-puzzle, lập lịch, hoặc thiết kế.
Nhược điểm
•	Không tối ưu: Không đảm bảo đường đi ngắn nhất trong 8-puzzle, vì phụ thuộc vào ngẫu nhiên.
•	Không hoàn chỉnh: Có thể không tìm được mục tiêu nếu quần thể không đa dạng hoặc dừng sớm.
•	Phụ thuộc tham số: Hiệu suất phụ thuộc vào kích thước quần thể, tỷ lệ lai ghép, đột biến, và hàm thích nghi.
•	Hạn chế: Kém hơn A* hoặc IDA* trong 8-puzzle về tính tối ưu và hiệu quả.
Chi tiết bổ sung
•	Thời gian: O(gb), với g là số thế hệ, b là kích thước quần thể, phụ thuộc vào tham số.
•	Không gian: O(b), lưu quần thể hiện tại.
•	So sánh: 
o	BFS/UCS: Tối ưu, khám phá nhiều trạng thái hơn.
o	DFS: Nhanh, không tối ưu.
o	IDS: Tối ưu, chậm hơn.
o	Hill Climbing/Simulated Annealing: Dễ kẹt cục bộ hơn hoặc ít toàn cục.
o	Greedy/A*/IDA*: Hiệu quả hơn, tối ưu.
•	Hiệu suất: Linh hoạt nhưng không đáng tin cậy trong 8-puzzle.
Nhận xét trên 8-puzzle
•	Hiệu quả: Phù hợp khi cần khám phá toàn cục và chấp nhận lời giải không tối ưu.
•	Thực tiễn: Ít áp dụng cho 8-puzzle, vì A* hoặc IDA* vượt trội hơn.
•	Hạn chế: Phụ thuộc vào tham số, không lý tưởng cho không gian trạng thái nhỏ như 8-puzzle.
```
![geneticalgorithms](https://github.com/user-attachments/assets/8c9a9835-71ba-4396-9f51-699ecfd9f83a)
```
2.6. Reinforcement Learning (Q-Learning)
Mô tả
•	Cơ chế hoạt động: 
o	Reinforcement Learning là phương pháp học dựa trên thử và sai, trong đó tác nhân học cách chọn hành động tối ưu thông qua phần thưởng (reward) từ môi trường. Q-Learning là một thuật toán RL phổ biến được áp dụng cho 8-puzzle.
o	Trong 8-puzzle, tác nhân học chính sách di chuyển ô trống để đạt trạng thái mục tiêu bằng cách cập nhật bảng Q (Q-table) lưu giá trị hành động-trạng thái.
o	Với 8-puzzle: 
	Trạng thái: Bảng 3x3 (ví dụ: [[1,2,3], [4,0,5], [7,8,6]], 0 là ô trống).
	Hành động: Di chuyển ô trống (lên, xuống, trái, phải).
	Phần thưởng: Thường là -1 cho mỗi bước di chuyển, +100 nếu đạt mục tiêu ([[1,2,3], [4,5,6], [7,8,0]]).
	Hàm giá trị Q: Ước lượng phần thưởng dài hạn cho mỗi cặp trạng thái-hành động.
o	Q-Learning cập nhật bảng Q dựa trên công thức
o	Quy trình: 
1.	Khởi tạo bảng Q với giá trị ngẫu nhiên hoặc 0.
2.	Lặp lại qua nhiều tập (episode): 
	Từ trạng thái ban đầu, chọn hành động theo chính sách (thường <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>ϵ</mi></mrow><annotation encoding="application/x-tex">\epsilon</annotation></semantics></math>ϵ-greedy: khai thác hoặc khám phá ngẫu nhiên).
	Thực hiện hành động, nhận phần thưởng và trạng thái mới.
	Cập nhật giá trị Q dựa trên phần thưởng và trạng thái mới.
3.	Tiếp tục cho đến khi Q hội tụ hoặc đạt số tập tối đa.
4.	Sử dụng bảng Q để chọn đường đi từ trạng thái ban đầu đến mục tiêu.
o	Đặc điểm: RL (Q-Learning) học chính sách tối ưu qua thử nghiệm, nhưng không đảm bảo tối ưu nhanh trong 8-puzzle do không gian trạng thái lớn.
Ưu điểm
•	Học từ môi trường: Không cần mô hình môi trường, phù hợp cho bài toán phức tạp hoặc môi trường ẩn.
•	Tìm kiếm toàn cục: Khám phá nhiều trạng thái, giảm nguy cơ kẹt ở cực đại cục bộ so với Hill Climbing.
•	Linh hoạt: Có thể áp dụng cho nhiều bài toán ngoài 8-puzzle, như điều khiển robot hoặc trò chơi.
•	Ứng dụng: Hữu ích trong bài toán cần học chính sách dài hạn, như 8-puzzle hoặc các trò chơi chiến lược.
Nhược điểm
•	Không tối ưu nhanh: Cần nhiều tập để học chính sách tốt trong 8-puzzle, chậm hơn A*.
•	Không hoàn chỉnh: Có thể không tìm được mục tiêu nếu không đủ tập hoặc tham số không tối ưu.
•	Phụ thuộc tham số: Hiệu suất phụ thuộc vào tốc độ học , hệ số chiết khấu, và chính sách khám phá.
•	Hạn chế: Kém hơn A* hoặc IDA* trong 8-puzzle do không gian trạng thái lớn (~362,880 trạng thái) và không sử dụng heuristic trực tiếp.
Chi tiết bổ sung
•	Thời gian: O(n), với n là số tập, phụ thuộc vào số trạng thái và hành động.
•	Không gian: O(|S||A|), lưu bảng Q cho mọi trạng thái-hành động.
•	So sánh: 
o	BFS/UCS: Tối ưu, khám phá nhiều trạng thái hơn.
o	DFS: Nhanh, không tối ưu.
o	IDS: Tối ưu, chậm hơn.
o	Hill Climbing/Simulated Annealing: Dễ kẹt cục bộ hơn.
o	Genetic Algorithms: Tương tự về tìm kiếm toàn cục, nhưng khác cơ chế.
o	Greedy/A*/IDA*: Hiệu quả hơn, tối ưu.
•	Hiệu suất: Linh hoạt nhưng chậm trong 8-puzzle so với Informed Search.
Nhận xét trên 8-puzzle
•	Hiệu quả: Phù hợp khi cần học chính sách trong môi trường không rõ, nhưng không hiệu quả bằng A*.
```
![rl](https://github.com/user-attachments/assets/5c91b4a7-8b2d-4f30-9b3d-639d24435a77)
```
Khi bấm nút compare, sẽ thấy biểu đồ cột thể hiện về memory và bấm vào time sẽ xuất biểu đồ cột theo thời gian.
```
![Screenshot 2025-05-18 094908](https://github.com/user-attachments/assets/14e0429c-0495-430a-b0cd-d282fdf16a79)
```
Hiệu quả cao: Thuật toán như Greedy Search, IDA*, Beam Search, và A Start* cho thấy thời gian thấp, phù hợp khi ưu tiên tốc độ, nhưng không phải lúc nào cũng tối ưu (trừ A*).
Hiệu quả tối ưu: BFS, UCS, và IDS đảm bảo đường đi ngắn nhất, nhưng tốn thời gian do khám phá nhiều trạng thái.
Học và tiến hóa: RL và Genetic Algorithms tiêu tốn thời gian hơn do học qua nhiều tập hoặc thế hệ, không lý tưởng cho 8-puzzle.
Tìm kiếm cục bộ: Simulated Annealing và SHC có thời gian trung bình, tốt hơn Simple Hill Climbing nhưng vẫn phụ thuộc tham số.
Phù hợp với 8-puzzle: A* (nếu A* Start là bước khởi đầu của A*) và IDA* nổi bật nhờ kết hợp heuristic và hiệu suất, vượt trội hơn các thuật toán uninformed (BFS, UCS, IDS) hoặc học (RL, GA).
•	Thực tiễn: Ít áp dụng cho 8-puzzle, vì A* hoặc IDA* vượt trội hơn.
•	Hạn chế: Yêu cầu nhiều tập học, không lý tưởng cho không gian trạng thái nhỏ như 8-puzzle.
```
![Screenshot 2025-05-18 094737](https://github.com/user-attachments/assets/7deac620-9fa2-48f6-ab86-77653f8d6ca6)
```
•  Informed Search (A, IDA, Greedy Search):** Vượt trội trong 8-puzzle nhờ heuristic (Manhattan Distance), trong đó A* và IDA* là lựa chọn tối ưu nhất về hiệu suất và độ tin cậy. 
•  Uninformed Search (BFS, UCS, IDS, DFS): BFS, UCS, IDS đảm bảo tối ưu nhưng chậm và tốn tài nguyên; DFS nhanh nhưng không tối ưu. 
•  Local Search (Beam Search, Hill Climbing, Simulated Annealing): Nhanh, tiết kiệm tài nguyên, nhưng không tối ưu và dễ bỏ lỡ mục tiêu. 
•  Learning-Based (RL, Genetic Algorithms): Phù hợp cho bài toán học dài hạn, nhưng không hiệu quả cho 8-puzzle do không gian trạng thái nhỏ. 
•  Specialized Search (AND-OR, Partially Observable/Unknown Environment): Không tự nhiên cho 8-puzzle, chậm và phức tạp. 
•  CSP (Backtracking, Forward Checking, AC-3): Phù hợp hơn cho bài toán như Sudoku, không hiệu quả khi áp dụng cho 8-puzzle.
	
Kết luận
•	Lựa chọn tốt nhất cho 8-puzzle: A* (hiệu suất tốt, tối ưu) hoặc IDA* (tiết kiệm tài nguyên, tối ưu).
•	Khi ưu tiên tốc độ: Greedy Search hoặc Beam Search.
•	Khi cần tối ưu mà không có heuristic: IDS (tiết kiệm tài nguyên hơn BFS/UCS).
•	Không khuyến nghị: RL, Genetic Algorithms, AND-OR Search, và CSP-based (Backtracking, Forward Checking, AC-3) do không phù hợp hoặc quá phức tạp.
3.Kết quả đạt được khi thực hiện project
3.1.Xây dựng và so sánh hiệu quả của các thuật toán tìm kiếm: 
o	Project đã triển khai thành công nhiều thuật toán tìm kiếm, bao gồm cả Uninformed Search (BFS, DFS, UCS, IDS) và Informed Search (Greedy Search, A*, IDA*), cùng với các phương pháp Local Search (Beam Search, Hill Climbing, Stochastic Hill Climbing, Simulated Annealing) và Learning-Based (Genetic Algorithms, Reinforcement Learning). Mỗi thuật toán được áp dụng và đánh giá trên bài toán 8-puzzle, giúp hiểu rõ cách chúng hoạt động trong không gian trạng thái hữu hạn (~362,880 trạng thái).
o	Kết quả so sánh cho thấy sự khác biệt rõ rệt về hiệu suất, từ đó xác định được thuật toán nào phù hợp nhất với từng yêu cầu (tối ưu, tốc độ, hoặc tiết kiệm tài nguyên).
3.2.Phát triển mô hình hóa bài toán 8-puzzle: 
o	Dự án đã mô hình hóa 8-puzzle như một bài toán tìm kiếm trạng thái, với trạng thái ban đầu và mục tiêu được biểu diễn dưới dạng bảng 3x3. Các hành động (di chuyển ô trống lên, xuống, trái, phải) và hàm heuristic (như Manhattan Distance) được tích hợp, cho phép áp dụng các thuật toán một cách hiệu quả.
o	Ngoài ra, một số phương pháp như AND-OR Search, Backtracking, Forward Checking, và AC-3 đã được thử nghiệm để mô phỏng 8-puzzle như bài toán CSP, mặc dù không tối ưu, vẫn mang lại hiểu biết về tính linh hoạt của các phương pháp.
3.3.Tích hợp công cụ trực quan hóa: 
o	Project đã thành công trong việc tạo ra các hình ảnh động (GIF) bằng Pygame, minh họa quá trình hoạt động của từng thuật toán trên 8-puzzle (ví dụ: BFS duyệt theo mức, A* chọn trạng thái theo f(n), Simulated Annealing chấp nhận trạng thái xấu). Điều này giúp trực quan hóa cách các thuật toán khám phá không gian trạng thái.
o	Biểu đồ so sánh thời gian và tài nguyên sử dụng (dựa trên dữ liệu giả định từ hình ảnh) đã được xây dựng bằng Matplotlib, cung cấp cái nhìn tổng quan về hiệu suất của từng phương pháp.
3.4.Đánh giá và rút ra bài học: 
o	Kết quả cho thấy A* và IDA* là các thuật toán hiệu quả nhất cho 8-puzzle, cân bằng giữa tính tối ưu (đường đi ngắn nhất) và hiệu suất, nhờ sử dụng heuristic như Manhattan Distance. Điều này xác nhận vai trò quan trọng của thông tin trong tìm kiếm.
o	Các phương pháp Local Search (như Greedy Search, Beam Search) phù hợp khi ưu tiên tốc độ, trong khi Uninformed Search (BFS, UCS, IDS) tốt hơn khi không có heuristic. Ngược lại, các phương pháp học (RL, Genetic Algorithms) và CSP (Backtracking, AC-3) ít hiệu quả do không gian trạng thái nhỏ và cấu trúc không phù hợp.
o	Dự án cũng chỉ ra hạn chế của một số thuật toán (như DFS dễ kẹt nhánh sâu, UCS tốn tài nguyên) và gợi ý cải tiến, chẳng hạn kết hợp heuristic hoặc tối ưu hóa tham số.
3.5.Ứng dụng thực tiễn và mở rộng: 
o	Thành quả của project có thể được áp dụng để giải các bài toán tìm đường hoặc tối ưu hóa tương tự (như 15-puzzle, Sudoku. Các GIF và biểu đồ cũng hỗ trợ giảng dạy hoặc trình bày về các thuật toán tìm kiếm.
o	Dự án mở ra hướng nghiên cứu thêm, như cải tiến heuristic, áp dụng cho môi trường quan sát một phần, hoặc tích hợp học sâu (Deep RL) để xử lý không gian trạng thái lớn hơn.

