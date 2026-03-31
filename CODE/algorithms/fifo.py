from .base import PageReplacementAlgorithm


class FIFO(PageReplacementAlgorithm):
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
                    frames.pop(0)
                    frames.append(page)

            results.append({
                "step": step,
                "page": page,
                "frames": frames.copy(),
                "fault": fault
            })

        return results
    
    #chịu trách nhiệm nhận dữ liệu đầu vài, xử lý mô phỏng thay trang và trả ra output 