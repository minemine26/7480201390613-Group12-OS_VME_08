from .base import PageReplacementAlgorithm


class LRU(PageReplacementAlgorithm):
    def simulate(self, ref_list, frame_count):
        frames = []
        results = []

        for step, page in enumerate(ref_list):
            fault = False

            if page in frames:
                frames.remove(page)
                frames.append(page)
            else:
                fault = True

                if len(frames) < frame_count:
                    frames.append(page)
                else:
                    frames.pop(0)
                    frames.append(page)

            results.append({
                "step": step,
                "page": page,
                "frames": frames.copy(),
                "fault": fault
            })

        return results
    
#LRU - least recently used : cái nào lâu không sd => xóa 
# LRU dựa trên nguyên lý : quá khứ gần -> dự đoán tương lai 