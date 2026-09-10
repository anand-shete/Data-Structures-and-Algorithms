## Binary Search

1. Binary search can be applied in 2 ways:
   - `low <= high` with boundary `high = mid - 1` and `low = mid + 1` and return `ans` (`mid`)
   - `low < high` with boundary `high = mid` and `low = mid + 1` and return `low`

2. Binary search on answers: Koko Eating Bananas
   - If Koko can eat banana in `h` hrs, he can eat all bananas in `h+1` hrs, `h+2` hrs,...
   - To find minimum, use `ans=mid` and `high=mid-1` else to find maximum set `ans=mid` inside `low=mid+1` block
