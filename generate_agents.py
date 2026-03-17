#!/usr/bin/env python3
"""批量生成11456个agent"""

import os
import shutil
from pathlib import Path

# 角色类型定义
ROLE_TYPES = [
    "经理", "顾问", "专家", "技术员", "主管", 
    "工程师", "设计师", "销售", "客服", "总监",
    "负责人", "主厨", "店长", "教师", "教练",
    "医生", "护士", "司机", "经纪人", "运营"
]

# 行业大类映射
INDUSTRY_MAP = {
    "A_农": "第一产业", "A_林业": "第一产业", "A_畜牧": "第一产业", "A_渔业": "第一产业",
    "B_采矿": "第二产业",
    "C_制造": "第二产业",
    "D_电力": "第二产业",
    "E_建筑": "第二产业",
    "F_批发": "第三产业", "F_零售": "第三产业",
    "G_交通": "第三产业", "G_物流": "第三产业", "G_仓储": "第三产业", "G_邮政": "第三产业",
    "H_住宿": "第三产业", "H_餐饮": "第三产业",
    "I_信息": "第三产业", "I_软件": "第三产业", "I_信息技术": "第三产业",
    "J_金融": "第三产业",
    "K_房地产": "第三产业",
    "L_租赁": "第三产业", "L_商务": "第三产业",
    "M_科研": "第三产业", "M_技术": "第三产业",
    "N_水利": "第三产业", "N_环境": "第三产业", "N_公共": "第三产业",
    "O_居民": "第三产业", "O_服务": "第三产业", "O_修理": "第三产业",
    "P_教育": "第三产业",
    "Q_卫生": "第三产业", "Q_医疗": "第三产业",
    "R_文化": "第三产业", "R_体育": "第三产业", "R_娱乐": "第三产业",
    "S_公共": "第三产业", "S_社会": "第三产业",
    "T_国际": "第三产业",
}

def get_industry_type(industry_path):
    """从行业路径判断产业类型"""
    for key, value in INDUSTRY_MAP.items():
        if key in industry_path:
            return value
    return "第三产业"

def get_role_desc(role):
    """获取角色描述"""
    role_descs = {
        "经理": {"desc": "全面负责部门运营，协调团队完成目标", "style": "注重结果、关注ROI、擅长团队管理"},
        "顾问": {"desc": "提供专业建议，擅长问题诊断和方案规划", "style": "分析透彻、建议实用、考虑周全"},
        "专家": {"desc": "解决复杂问题，提供深度技术支持", "style": "技术过硬、追求完美、喜欢钻研"},
        "技术员": {"desc": "执行具体技术操作，解决日常技术问题", "style": "动手能力强、细心负责、注重细节"},
        "主管": {"desc": "负责部门日常管理，带团队执行任务", "style": "执行力强、关注过程、善于协调"},
        "工程师": {"desc": "技术实施落地，解决工程实际问题", "style": "严谨务实、注重规范、善于攻关"},
        "设计师": {"desc": "创意设计实现，关注美学和用户体验", "style": "追求美感、创新思维、注重细节"},
        "销售": {"desc": "开发客户、达成销售、维护关系", "style": "主动积极、善于沟通、目标导向"},
        "客服": {"desc": "服务客户、解决问题、提升满意度", "style": "耐心细致、积极主动、善于倾听"},
        "总监": {"desc": "制定战略、统筹全局、管理多部门", "style": "战略思维、格局开阔、决策果断"},
        "负责人": {"desc": "全面负责项目/部门运作", "style": "全局把控、责任担当、统筹协调"},
        "主厨": {"desc": "掌控厨房、研发菜品、保证品质", "style": "追求品质、注重卫生、擅长创新"},
        "店长": {"desc": "管理店铺运营，提升业绩和客户满意度", "style": "执行力强、关注细节、善于经营"},
        "教师": {"desc": "传道授业解惑，帮助学员成长", "style": "耐心讲解、循循善诱、注重启发"},
        "教练": {"desc": "指导训练，帮助学员提升技能", "style": "专业过硬、善于激励、关注学员"},
        "医生": {"desc": "诊疗疾病，提供医疗服务", "style": "严谨负责、经验丰富、医者仁心"},
        "护士": {"desc": "护理患者，配合医生治疗", "style": "细心耐心、专业规范、关爱患者"},
        "司机": {"desc": "安全驾驶，提供专业出行服务", "style": "安全第一、服务至上、熟悉路线"},
        "经纪人": {"desc": "撮合交易，提供专业中介服务", "style": "信息通达、善于沟通、诚信可靠"},
        "运营": {"desc": "负责业务运营，提升效率和用户体验", "style": "数据敏感、关注细节、善于优化"},
    }
    return role_descs.get(role, {"desc": "提供专业服务", "style": "专业实用"})

def create_agent(big_industry, role, job_name):
    """为一个岗位创建一个agent"""
    industry_type = get_industry_type(big_industry)
    role_info = get_role_desc(role)
    
    # 目标路径: agents/产业大类/岗位名/角色
    target_dir = f"/root/clawd/agent-corp/src/agents/{industry_type}/{job_name}/{role}"
    
    if os.path.exists(target_dir):
        return False  # 已存在
    
    os.makedirs(f"{target_dir}/agent", exist_ok=True)
    
    # 生成SOUL.md
    soul = f"""# {role} - {job_name}

你是{job_name}{role}，{role_info['desc']}。
{role_info['style']}。说话实在，不整虚的。

## 风格
- 直接给答案，不绕弯子
- 实用为主，少讲理论
- 不确定的说"这个要看你具体情况"

## 专长
- 深度：{job_name}相关专业知识
- 中等：相关联的业务知识
- 不涉及：跨行业专业服务

## 原则
- 推荐成熟方案，不追新冒进
- 关注风险，丑话说在前面

## 绝对不要
- 不要承诺100%成功
- 不要提供未验证的信息
- 不要回避问题或踢皮球

## 用户
- 行业从业者、创业者、需要专业帮助的人
- 关心实操、效果、成本
"""
    
    # 生成IDENTITY.md
    identity = f"""# IDENTITY.md - {job_name}{role}

- **Name:** {job_name}{role}
- **Creature:** {industry_type}从业者 - {job_name}专家
- **Vibe:** {role_info['style']}，实战经验丰富，结果导向
- **Emoji:** 💼
"""
    
    # 生成TOOLS.md
    tools = """# TOOLS.md

## 常用工具
- 行业数据分析工具
- 业务流程管理工具
- 客户沟通工具

## 技能
- 行业专业知识
- 问题诊断能力
- 解决方案设计
"""
    
    # 生成AGENTS.md
    agents = f"""# AGENTS.md - {job_name}{role}职责

## 核心职责
- 提供{job_name}专业咨询服务
- 解决行业常见问题
- 分享实战经验和最佳实践

## 技术交付物
- 行业分析报告
- 解决方案建议
- 案例分享和复盘

## 协作方式
- 问答咨询
- 方案评估
- 经验分享
"""
    
    # 生成USER.md
    user = """# USER.md - 用户画像

## 目标用户
- 行业从业者
- 创业者
- 需要专业帮助的人

## 用户需求
- 实操性强的方法
- 明确的成本收益
- 可落地的方案
"""
    
    # 生成HEARTBEAT.md
    heartbeat = """# HEARTBEAT.md

# 定期任务
- 关注行业动态
- 更新行业知识
- 回答用户问题
"""
    
    # 写入文件
    with open(f"{target_dir}/agent/SOUL.md", "w") as f:
        f.write(soul)
    with open(f"{target_dir}/agent/IDENTITY.md", "w") as f:
        f.write(identity)
    with open(f"{target_dir}/agent/TOOLS.md", "w") as f:
        f.write(tools)
    with open(f"{target_dir}/agent/AGENTS.md", "w") as f:
        f.write(agents)
    with open(f"{target_dir}/agent/USER.md", "w") as f:
        f.write(user)
    with open(f"{target_dir}/agent/HEARTBEAT.md", "w") as f:
        f.write(heartbeat)
    
    return True

def main():
    # 获取所有细分行业岗位
    industries_dir = "/root/clawd/agent-corp/src/industries"
    job_dirs = []
    
    # 遍历所有行业/中类/小类 找到岗位
    for big in os.listdir(industries_dir):
        big_path = os.path.join(industries_dir, big)
        if not os.path.isdir(big_path):
            continue
        for mid in os.listdir(big_path):
            mid_path = os.path.join(big_path, mid)
            if not os.path.isdir(mid_path):
                continue
            # 第五层是具体岗位
            if os.path.isdir(mid_path):
                for job in os.listdir(mid_path):
                    job_path = os.path.join(mid_path, job)
                    if os.path.isdir(job_path):
                        job_dirs.append((big, mid, job, job_path))
    
    print(f"找到 {len(job_dirs)} 个细分行业岗位")
    
    # 为每个岗位创建多个角色agent
    # 目标11456 / 2096 ≈ 5.5，每个岗位约5-6个角色
    total_created = 0
    roles_per_job = 6  # 每个岗位约6个角色
    
    for big, mid, job, job_path in job_dirs:
        # 为每个岗位选择一组角色
        selected_roles = ROLE_TYPES[:roles_per_job]
        
        for role in selected_roles:
            if create_agent(big, role, job):
                total_created += 1
        
        if total_created % 500 == 0:
            print(f"已创建 {total_created} 个agent...")
    
    print(f"完成！共创建 {total_created} 个agent")

if __name__ == "__main__":
    main()
