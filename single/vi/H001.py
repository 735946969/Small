# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) wxmall.janedao.cn
# Author：QQ173782910
#QQ group:528289471
##############################################################################
"""single/vi/H001.py"""

from imp import reload
from basic.publicw import DEBUG
if DEBUG == '1':
    import single.vi.BASE_TPL
    reload(single.vi.BASE_TPL)
from single.vi.BASE_TPL             import cBASE_TPL

class cH001(cBASE_TPL):
    
    def setClassName(self):
        self.dl_name = 'H001_dl'

    def specialinit(self):
        pass

    def goPartList(self):
        self.initHiddenLocal()  # 初始隐藏域
        self.navTitle = '个人账号管理'
        self.getBreadcrumb() #获取面包屑
        info = self.dl.getInfo()
        self.assign('info',info)
        return self.runApp('H001_list.html')

    def goPartSearch(self):
        dR = self.dl.Search_data()
        return self.jsons(dR)
    
    
    
    
        
 