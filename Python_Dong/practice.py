# 作者 ：D_wh
# 时间 ：2023/3/13 14:21
# 格式化 ：Ctrl+Alt+L
# 清除不用代码 ：Ctrl+Alt+O
# 智能导入 ：Alt+Enter
def main(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

print(main(5)) # 输出 120

# import fedml
#
# fedml.run_simulation()

