from .base import PageReplacementAlgorithm


class LRU(PageReplacementAlgorithm):
    def simulate(self, ref_list, frame_count):
        frames = []
        results = []

        # 🔥 lưu thời điểm truy cập cuối
        last_used = {}

        for step, page in enumerate(ref_list):
            fault = False

            if page in frames:
                # update thời gian truy cập
                last_used[page] = step

            else:
                fault = True

                if len(frames) < frame_count:
                    frames.append(page)
                else:
                    # 🔥 tìm page ít được dùng gần đây nhất
                    lru_page = min(frames, key=lambda p: last_used[p])

                    idx = frames.index(lru_page)
                    frames[idx] = page

                    # xóa page cũ
                    del last_used[lru_page]

                # thêm page mới
                last_used[page] = step

            results.append({
                "step": step,
                "page": page,
                "frames": frames.copy(),
                "fault": fault
            })

        return results