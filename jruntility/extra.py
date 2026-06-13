"""extra.py —— 远程自定义规则（可热更新，无需重新打包客户端）。

客户端会拉取本文件并执行，调用其中的 is_accessible(flow, config)。
返回值：
  True  → 放行
  False → 拦截（替换为 block.html）
  None  → 不表态，交回客户端默认的黑/白名单逻辑（api.py）

参数：
  flow   —— mitmproxy.http.HTTPFlow，可读 flow.request.url / .pretty_host / .path 等
  config —— 远程规则 dict（来自 config.json）

⚠️ 本文件会在所有客户端上执行，等同远程代码执行——
   务必保护好仓库写权限，只放可信代码。
"""


def is_accessible(flow, config):
    # 示例：拦截任意 URL 路径中包含 /ads/ 的请求；其余交给默认黑/白名单逻辑
    if "/ads/" in flow.request.path:
        return False
    return None
