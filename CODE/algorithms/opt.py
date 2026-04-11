from .base import PageReplacementAlgorithm



class OPT(PageReplacementAlgorithm):

    def simulate(self, ref_list, frame_count):
        frames = []
        results = []

        for step, page in enumerate(ref_list):
            fault = False

            if page not in frames:
                fault = True
                
                if len(frames) < frame_count:
                    frames.append(page)
                else:
                    def distance_to_next_use(p):
                        future_list = ref_list[step + 1:]
                        return future_list.index(p) if p in future_list else float('inf')
                    page_to_replace = max(frames, key=distance_to_next_use)               
                    frames[frames.index(page_to_replace)] = page

            results.append({
                "step": step,
                "page": page,
                "frames": frames.copy(),
                "fault": fault
            })
        return results
    
# OPT - Optimal: Chọn thay thế trang mà khoảng thời gian tới lần sử dụng tiếp theo là lớn nhất.
# Khuyết điểm: Không thể cài đặt thực tế vì hệ điều hành không thể biết trước tương lai tiến trình cần trang nào.