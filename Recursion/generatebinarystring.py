def solve(binary: str,idx: int,temp: str,ans: list):
    if idx == len(binary):
        ans.append(temp)
        return
    if binary[idx] =='?':
        solve(binary,idx+1,temp+'0',ans)
        solve(binary,idx+1,temp+'1',ans)
    else:
        solve(binary,idx+1,temp+binary[idx],ans)