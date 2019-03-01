#! /user/bin/evn python
# coding:utf-8

import sys
import os
sys.path.append(os.path.abspath('%s../../' % sys.path[0]))
from common.config import *

url_Login = host + "/api/auth/login"   #用户登录接口
url_RefreshToken = host + "/api/auth/refresh"   #令牌刷新
url_ResetPassword = host + "/api/auth/reset"   #重置密码
url_HomepageAuthItems = host + "/api/supervisor/auth/items"  #首页授权项目
url_HomepageAnalysisData = host + "/api/supervisor/analysis/data"    #首页关键数据
url_HomepageRankList = host + "/api/supervisor/rank/list"  #首页排行榜
url_ProjectList = host + "/api/supervisor/project/list"  #主管项目列表
url_ClienteleSearchItems = host + "/api/supervisor/clientele/search_items"  #客户管理-筛选因子
url_ClienteleList = host + "/api/supervisor/clientele/list"   #客户管理-列表