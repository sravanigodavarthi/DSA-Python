class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        # Initialize history_records as a list of lists
        self.history_records = [[(0, 0)] for _ in range(length)]  # (snap_id, value)

    def set_val(self, index: int, val: int) -> None:
        # Append a new tuple (current snapshot id, value) to the history of the index
        self.history_records[index].append((self.id, val))

    def snap(self) -> int:
        # Return the current snapshot id and increment it
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        # Binary search for the snap_id in the history of the index
        history = self.history_records[index]
        l, r = 0, len(history) - 1
        while l <= r:
            mid = (l + r) // 2
            if history[mid][0] <= snap_id:
                l = mid + 1
            else:
                r = mid - 1
        return history[r][1] 


# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(3)
obj.set_val(0,5)
param_2 = obj.snap()
obj.set_val(0,4)
param_2 = obj.snap()
param_3 = obj.get(0,0)
print(param_3)