# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) wxmall.janedao.cn
# Author：QQ173782910
#QQ group:528289471
##############################################################################
"""manage/vi/C003.py"""

from imp import reload
from basic.publicw import DEBUG
if DEBUG == '1':
    import manage.vi.BASE_TPL
    reload(manage.vi.BASE_TPL)
from manage.vi.BASE_TPL             import cBASE_TPL



class cC003(cBASE_TPL):
    
    def setClassName(self):
        self.dl_name = 'C003_dl'
        self.inframe = 1
    def specialinit(self):
        pass

    def goPartList(self):
      
        self.assign('NL',self.dl.GNL)
        self.navTitle = ''
        self.getBreadcrumb() #获取面包屑
        PL,L = self.dl.mRight()
        self.assign('dataList',L)

        self.getPagination(PL)
        s = self.runApp('C003_list.html')
        return s
    
    def initPagiUrl(self):
        lb_code = self.REQUEST.get('lb_code','')
        brand_id = self.REQUEST.get('brand_id','')
        status = self.REQUEST.get('status','')
        ctype = self.REQUEST.get('ctype','')
        qqid = self.REQUEST.get('qqid','')
        url = self.sUrl
        if qqid:
            url += "&qqid=%s" % qqid
        if lb_code:
            url += "&lb_code=%s" % lb_code
        if brand_id:
            url += "&brand_id=%s" % brand_id
        if status:
            url += "&status=%s" % status
        if ctype:
            url += "&ctype=%s" % ctype
        return url
    
    def goPartLocalfrm(self):
        self.navTitle = ''

        self.need_editor = 1
        self.getBreadcrumb() #获取面包屑
        self.initHiddenLocal()#初始隐藏域
       
        self.getBackBtn()

        self.item = self.dl.get_local_data()
        self.assign('item', self.item)
        self.itemc = self.dl.get_sec_data()
        self.assign('itemc', self.itemc)
        
        s = self.runApp('C003_local.html')
        return s


    def goPartAjax_update(self):
        dR=self.dl.ajax_update_data()
        return self.jsons(dR)

    def goPartSave_brand(self):#增加品牌
        dR=self.dl.save_brand()
        return self.jsons(dR)

    def goPartedit_brand(self):#修改品牌
        dR=self.dl.edit_brand()
        return self.jsons(dR)


        
 