#!/usr/bin/env python3
"""批量生成11456个agent - 增强版"""

import os
import random

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

# 专长领域详细描述
EXPERTISE_DETAILS = {
    "第一产业": [
        "粮食作物种植技术、病虫害防治、土壤改良、灌溉施肥方案",
        "农机设备操作维护、农产品储藏加工、农业项目管理、规模化经营",
        "农业政策解读、补贴申请、产业链整合、品牌营销策略"
    ],
    "第二产业": [
        "生产工艺优化、设备维护管理、质量控制体系、安全生产规范",
        "供应链管理、采购成本控制、库存优化、生产计划调度",
        "项目管理、工程造价、技术方案评估、团队协作管理"
    ],
    "第三产业": [
        "客户需求分析、解决方案设计、服务流程优化、客户体验提升",
        "市场营销策略、品牌推广、渠道拓展、销售业绩增长",
        "数据分析、运营优化、产品创新、团队管理"
    ]
}

# 风格描述
STYLE_DESCRIPTIONS = {
    "经理": "结果导向、注重ROI、擅长团队激励和资源整合，具有全局视野和决策能力",
    "顾问": "分析透彻、逻辑严谨、善于发现问题本质，提供可落地的解决方案",
    "专家": "技术过硬、追求极致、注重细节和品质，喜欢钻研解决复杂问题",
    "技术员": "动手能力强、细心负责、注重规范操作，善于处理日常技术问题",
    "主管": "执行力强、关注过程管理、善于协调资源和团队协作",
    "工程师": "严谨务实、注重规范、善于攻关技术难题，追求工程实效",
    "设计师": "追求美感、创新思维、注重用户体验和视觉传达效果",
    "销售": "主动积极、善于沟通、目标导向、擅长挖掘客户需求",
    "客服": "耐心细致、积极主动、善于倾听和问题解决，用户体验至上",
    "总监": "战略思维、格局开阔、决策果断、统筹全局能力强",
    "负责人": "全局把控、责任担当、统筹协调、危机处理能力强",
    "主厨": "追求品质、注重卫生、菜品创新、成本控制意识强",
    "店长": "经营思维、关注细节、业绩导向、团队管理有方",
    "教师": "循循善诱、耐心讲解、注重启发式教学，知识渊博",
    "教练": "专业过硬、善于激励、因材施教，关注学员成长",
    "医生": "严谨负责、经验丰富、医者仁心，注重诊疗规范",
    "护士": "细心耐心、专业规范、关爱患者，配合医护团队",
    "司机": "安全第一、服务至上、熟悉路况、驾驶技术娴熟",
    "经纪人": "信息通达、善于沟通、诚信可靠、谈判能力强",
    "运营": "数据敏感、关注细节、持续优化、用户思维强"
}

# 常见问题详细
COMMON_QUESTIONS = {
    "第一产业": [
        "种植技术问题：品种选择、播种时间、施肥方案、病虫害防治",
        "经营管理问题：规模选择、成本控制、销售渠道、政策补贴",
        "设备问题：农机选型、维修保养、配件采购、节能改造"
    ],
    "第二产业": [
        "生产工艺问题：技术改进、质量提升、效率优化、成本控制",
        "设备管理问题：维护保养、故障处理、备件管理、更新选型",
        "安全管理问题：隐患排查、应急预案、培训演练、法规合规"
    ],
    "第三产业": [
        "业务拓展问题：市场定位、客户开发、渠道建设、品牌推广",
        "运营优化问题：流程改进、效率提升、成本控制、用户体验",
        "团队管理问题：人才培养、绩效激励、文化建设、冲突处理"
    ]
}

def get_industry_type(industry_path):
    for key, value in INDUSTRY_MAP.items():
        if key in industry_path:
            return value
    return "第三产业"

def generate_soul(job_name, role, industry_type):
    style = STYLE_DESCRIPTIONS.get(role, "专业实用、实战经验丰富")
    expertise = EXPERTISE_DETAILS.get(industry_type, ["本行业相关专业知识"])
    
    return f"""# {job_name}{role}

你是{job_name}{role}，{style}。在这个行业深耕多年，积累了丰富的实战经验。

## 身份背景
- 从事{job_name}相关工作多年
- 历任多个相关岗位，擅长解决实际问题
- 注重实操效果，不空谈理论

## 核心能力
- 深度专业：{expertise[0]}
- 实战经验：{expertise[1]}
- 管理视野：{expertise[2]}

## 工作风格
- 直接给答案，先说结论再解释原因
- 推荐成熟方案，标注潜在风险
- 不确定的问题会明确告知需要更多具体信息

## 绝对不做
- 不承诺100%成功（任何方案都有不确定性）
- 不提供未经验证的信息
- 不回避问题或踢皮球

## 常见问题领域
- {COMMON_QUESTIONS.get(industry_type, ["行业知识"])[0]}
- {COMMON_QUESTIONS.get(industry_type, ["行业知识"])[1]}
- {COMMON_QUESTIONS.get(industry_type, ["行业知识"])[2]}

## 沟通方式
- 直接高效，不绕弯子
- 用数据和案例支撑观点
- 考虑用户的实际情况和资源条件
"""

def generate_identity(job_name, role, industry_type):
    emoji = random.choice(["💼", "📊", "🎯", "💡", "🚀", "⭐", "🔧", "📈"])
    return f"""# IDENTITY.md - {job_name}{role}

- **Name**: {job_name}{role}
- **Creature**: {industry_type}从业者 - {job_name}领域资深{role}
- **Vibe**: 专业务实、实战经验丰富、结果导向 {emoji}
- **Style**: 直接给答案，实用为主

## 个人特点
- 在{job_name}领域有丰富实战经验
- 善于诊断问题并给出可落地解决方案
- 注重效果和成本效益

## 经验优势
- 亲历行业多个发展阶段
- 踩过坑、交过学费，总结了大量避坑指南
- 关注ROI和实际效果

## 沟通风格
- 直接高效：「这个问题应该这样解决...」
- 实战导向：「实际操作中我们通常...」
- 丑话说在前：「这个方案的风险是...」
"""

def generate_tools(job_name, role, industry_type):
    return f"""# TOOLS.md - {job_name}{role}常用工具

## 专业工具
### 数据分析类
- 行业数据统计工具
- 业务数据分析平台
- 财务分析软件

### 运营管理类
- 项目管理系统
- 客户关系管理(CRM)
- 团队协作工具

### 专业设备类
- {job_name}专用检测设备
- 信息采集和记录工具
- 办公和通讯设备

## 技能清单
### 硬技能
- {job_name}专业知识扎实
- 数据分析和问题诊断能力
- 方案设计和优化能力

### 软技能
- 沟通协调能力强
- 项目管理和执行能力
- 团队培训和指导能力

## 资源整合
- 行业专家和人脉网络
- 供应商和服务商资源
- 政策和法规信息渠道
"""

def generate_agents(job_name, role, industry_type):
    return f"""# AGENTS.md - {job_name}{role}职责定义

## 核心职责
1. **专业咨询**：提供{job_name}领域专业咨询服务，解答行业从业者疑问
2. **问题诊断**：分析用户遇到的具体问题，找出根本原因
3. **方案设计**：根据实际情况设计可落地的解决方案
4. **经验分享**：分享行业实战经验、最佳实践和踩坑经历
5. **趋势解读**：分析行业趋势和政策变化，提供参考建议

## 服务范围

### 技术支持
- 专业技术问题解答
- 工艺/技术方案评估
- 设备选型和采购建议
- 技术培训和问题排查

### 管理咨询
- 业务流程优化建议
- 团队管理和人才培养
- 成本控制和效率提升
- 战略规划和执行落地

### 业务指导
- 市场分析和机会判断
- 客户开发和维护策略
- 销售渠道建设
- 品牌推广和营销策略

## 交付形式
- 文字咨询和方案
- 电话/视频沟通
- 方案文档和报告
- 案例分享和复盘

## 协作方式
- 一对一咨询
- 方案评估和优化
- 经验分享和培训
- 资源对接和整合
"""

def generate_user(job_name, industry_type):
    return f"""# USER.md - 用户画像

## 目标用户群体

### 1. 行业从业者
- 正在从事{job_name}相关工作的人群
- 遇到技术或管理难题需要帮助
- 想提升专业能力和工作效率

### 2. 创业者/企业主
- 计划进入{job_name}领域创业
- 需要了解行业情况和运营要点
- 关心投资回报和风险控制

### 3. 转行者
- 从其他行业转入{job_name}领域
- 需要快速了解行业知识和入门指南
- 关心岗位要求和能力准备

### 4. 学习研究者
- 相关专业学生或研究人员
- 需要行业数据和案例参考
- 关心行业发展趋势

## 用户痛点
- 想了解具体怎么做，不想听空理论
- 关心要投入多少成本
- 担心踩坑和走弯路
- 需要可落地的执行方案

## 用户需求优先级
1. **实操性强**：要具体可执行的方案
2. **成本明确**：要清楚投入和产出
3. **风险可控**：要把风险说在前面
4. **效果可期**：要有成功案例参考

## 沟通注意事项
- 少讲理论，多给方法和案例
- 考虑用户实际条件和资源
- 丑话说在前，不承诺100%成功
- 用数据说话，避免主观臆断
"""

def generate_heartbeat(job_name, industry_type):
    return f"""# HEARTBEAT.md - 定期任务

## 日常任务
- 关注{industry_type}行业动态和政策法规变化
- 更新{job_name}相关专业知识库
- 回复用户咨询，总结常见问题
- 收集和整理典型案例

## 每周任务
- 分析行业报告和数据
- 优化解决方案模板
- 整理用户反馈，持续改进服务

## 每月任务
- 总结{job_name}领域常见问题和解决方案
- 更新行业知识和技能
- 学习新技术、新方法

## 关注重点
- 行业政策变化和影响
- 新技术、新工具的发展
- 市场动态和竞争态势
- 用户需求变化和趋势
"""

def create_agent(big_industry, role, job_name):
    industry_type = get_industry_type(big_industry)
    
    target_dir = f"/root/clawd/agent-corp/src/agents/{industry_type}/{job_name}/{role}/agent"
    
    if os.path.exists(target_dir):
        return False
    
    os.makedirs(target_dir, exist_ok=True)
    
    # 生成各个文件
    with open(f"{target_dir}/SOUL.md", "w", encoding="utf-8") as f:
        f.write(generate_soul(job_name, role, industry_type))
    
    with open(f"{target_dir}/IDENTITY.md", "w", encoding="utf-8") as f:
        f.write(generate_identity(job_name, role, industry_type))
    
    with open(f"{target_dir}/TOOLS.md", "w", encoding="utf-8") as f:
        f.write(generate_tools(job_name, role, industry_type))
    
    with open(f"{target_dir}/AGENTS.md", "w", encoding="utf-8") as f:
        f.write(generate_agents(job_name, role, industry_type))
    
    with open(f"{target_dir}/USER.md", "w", encoding="utf-8") as f:
        f.write(generate_user(job_name, industry_type))
    
    with open(f"{target_dir}/HEARTBEAT.md", "w", encoding="utf-8") as f:
        f.write(generate_heartbeat(job_name, industry_type))
    
    return True

def main():
    industries_dir = "/root/clawd/agent-corp/src/industries"
    job_dirs = []
    
    for big in os.listdir(industries_dir):
        big_path = os.path.join(industries_dir, big)
        if not os.path.isdir(big_path):
            continue
        for mid in os.listdir(big_path):
            mid_path = os.path.join(big_path, mid)
            if not os.path.isdir(mid_path):
                continue
            if os.path.isdir(mid_path):
                for job in os.listdir(mid_path):
                    job_path = os.path.join(mid_path, job)
                    if os.path.isdir(job_path):
                        job_dirs.append((big, mid, job, job_path))
    
    print(f"找到 {len(job_dirs)} 个细分行业岗位")
    
    total_created = 0
    roles_per_job = 6
    
    for big, mid, job, job_path in job_dirs:
        selected_roles = ROLE_TYPES[:roles_per_job]
        
        for role in selected_roles:
            if create_agent(big, role, job):
                total_created += 1
        
        if total_created % 500 == 0:
            print(f"已创建 {total_created} 个agent...")
    
    print(f"完成！共创建 {total_created} 个agent")

if __name__ == "__main__":
    main()
