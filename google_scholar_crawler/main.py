from scholarly import scholarly, MaxTriesExceededException
import json
from datetime import datetime
import os
import time
from requests.exceptions import Timeout, ConnectionError  # 捕获网络异常

# 配置参数（可通过环境变量调整，灵活控制爬取行为）
MAX_RETRIES = 3  # 最大重试次数
RETRY_DELAY = 5  # 重试间隔（秒）
TIMEOUT = 15  # 单请求超时时间（秒）
MAX_PUBLICATIONS = 50  # 最多保留的出版物数量（避免数据量过大）

def setup_scholarly_timeout():
    """为scholarly底层请求设置超时（覆盖默认无超时的问题）"""
    import requests
    session = requests.Session()
    session.timeout = TIMEOUT  # 全局超时
    scholarly.set_retries(MAX_RETRIES)  # 设置scholarly内置重试次数
    scholarly._SESSION = session  # 替换scholarly的会话对象

def fetch_author_data(author_id):
    """获取作者数据，包含重试和异常处理"""
    for attempt in range(MAX_RETRIES + 1):
        try:
            print(f"[{datetime.now()}] 第{attempt+1}次尝试获取作者数据...")
            # 1. 搜索作者ID
            start_time = time.time()
            author = scholarly.search_author_id(author_id)
            print(f"[{datetime.now()}] 搜索作者ID耗时: {time.time()-start_time:.2f}秒")
            
            # 2. 填充详细信息（只获取必要字段，减少请求量）
            start_time = time.time()
            # 移除'publications'可大幅提速，若需要则保留并限制数量
            sections = ['basics', 'indices', 'counts']  # 基础信息+引用数据（不含出版物）
            # 如需出版物，解开下面一行（会增加耗时）
            # sections = ['basics', 'indices', 'counts', 'publications']
            scholarly.fill(author, sections=sections)
            print(f"[{datetime.now()}] 填充作者信息耗时: {time.time()-start_time:.2f}秒")
            
            return author  # 成功获取则返回
        
        except (MaxTriesExceededException, Timeout, ConnectionError) as e:
            print(f"[{datetime.now()}] 尝试{attempt+1}失败: {str(e)}")
            if attempt == MAX_RETRIES:
                print(f"[{datetime.now()}] 已达最大重试次数，终止获取")
                raise  # 抛出异常让工作流捕获
            time.sleep(RETRY_DELAY * (attempt + 1))  # 指数退避重试

def main():
    try:
        # 1. 初始化超时配置
        setup_scholarly_timeout()
        
        # 2. 获取作者数据
        author_id = "W-rloDsAAAAJ"
        author = fetch_author_data(author_id)
        if not author:
            print("未获取到作者数据，终止脚本")
            return
        
        # 3. 处理数据（精简出版物，避免体积过大）
        author['name'] = author.get('name', 'unknown')
        author['updated'] = str(datetime.now())
        
        # 若包含出版物，限制数量并格式化
        if 'publications' in author:
            # 截断出版物列表（只保留最新的MAX_PUBLICATIONS条）
            author['publications'] = author['publications'][:MAX_PUBLICATIONS]
            # 转为字典（原代码逻辑保留）
            author['publications'] = {v['author_pub_id']: v for v in author['publications']}
            print(f"[{datetime.now()}] 已处理{len(author['publications'])}条出版物")
        
        # 4. 保存主数据
        output_dir = '../assets/results'
        os.makedirs(output_dir, exist_ok=True)
        main_output_path = os.path.join(output_dir, 'gs_data.json')
        with open(main_output_path, 'w') as f:
            json.dump(author, f, ensure_ascii=False, indent=2)
        print(f"[{datetime.now()}] 主数据已保存至 {main_output_path}")
        
        # 5. 生成shield.io徽章数据（处理可能的引用数缺失）
        citedby = author.get('citedby', 'unknown')
        shieldio_data = {
            "schemaVersion": 1,
            "label": "citations",
            "message": f"{citedby}",
            "color": "green" if citedby != 'unknown' else "red"  # 状态颜色标识
        }
        shield_output_path = os.path.join(output_dir, 'gs_data_shieldsio.json')
        with open(shield_output_path, 'w') as f:
            json.dump(shieldio_data, f, ensure_ascii=False)
        print(f"[{datetime.now()}] 徽章数据已保存至 {shield_output_path}")
        
        print(f"[{datetime.now()}] 脚本执行完成")
        
    except Exception as e:
        print(f"[{datetime.now()}] 脚本执行失败: {str(e)}")
        exit(1)  # 非0退出码让GitHub Actions识别为失败

if __name__ == "__main__":
    main()
