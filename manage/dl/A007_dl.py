# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) wxmall.janedao.cn
# Author：QQ173782910
#QQ group:528289471
##############################################################################
""" manage/dl/A007_dl.py"""

from imp import reload
from basic.publicw import DEBUG
if DEBUG == '1':
    import manage.dl.BASE_DL
    reload(manage.dl.BASE_DL)
from manage.dl.BASE_DL  import cBASE_DL

class cA007_dl(cBASE_DL):
    def init_data(self):
        self.GNL = ['','用户名称','手机号码','反馈类型','反馈内容','状态']


    #在子类中重新定义         
    def myInit(self):
        self.src = 'A007'
        pass

    def mRight(self):
            
        sql = u"""
            select w.id
                ,u.cname
                ,w.phone
                ,w.type
                ,w.text
                ,w.status_str
               
            from feedback w
            left join wechat_mall_user  u on u.id=w.wechat_user_id
            where  COALESCE(w.del_flag,0)=0 and w.usr_id =%s
        """%self.usr_id_p

        
        L,iTotal_length,iTotal_Page,pageNo,select_size=self.db.select_for_grid(sql,self.pageNo)
        PL=[pageNo,iTotal_Page,iTotal_length,select_size]
        return PL,L

    def get_local_data(self , pk):
        """获取 local 表单的数据
        """
        L = {}
        sql = u"""
                    select w.id
                        ,wu.cname
                        ,case when w.is_default=1 then '是' else '否' end is_default
                        ,w.address
                        ,w.cname
                        ,w.phone
                        ,w.ctime 
                        ,w.utime
                    from wechat_address w
                    left join wechat_mall_user  wu on wu.id=w.wechat_user_id
                    where  COALESCE(w.del_flag,0)=0 and w.usr_id =%s and w.id
                """
        if pk != '':
            L = self.db.fetch( sql,[self.usr_id_p,pk] )

        return L
    
    # def local_add_save(self):
    #
    #
    #     """
    #     <p>这里是local 表单 ，add 模式下的保存处理</p>
    #     """
    #
    #     #这些是操作权限
    #     dR={'R':'','MSG':'申请单 保存成功','B':'1','isadd':'','furl':''}
    #     pk = self.pk
    #     #dR={'R':'','MSG':'','isadd':''}
    #     dR={'R':'','MSG':''}
    #     save_flag = self.REQUEST.get("save_flag").strip()
    #     save_flag2 = self.cookie.getcookie("__flag")
    #
    #
    #     #获取表单参数
    #     danhao=self.GP('danhao')#单号
    #     sp_name=self.GP('sp_name')#商品名
    #     sp_bh=self.GP('sp_bh')#商品编号
    #     sp_type=self.GP('sp_type')#商品类型
    #     candi=self.GP('candi')#产地
    #     num=self.GP('num')#数量
    #     dw=self.GP('dw')#单位
    #     gys_id = self.GP('gys_id')  # 供应商ID
    #     money=self.GP('money')#进货价格
    #     in_date=self.GP('in_date')#进货时间
    #     beizhu=self.GP('beizhu')#备注
    #
    #
    #
    #     if not (save_flag == save_flag2):
    #         #为FALSE时,当前请求为重刷新
    #         return dR
    #
    #     # if danhao == '':
    #     #     dR['R'] = '1'
    #     #     dR['MSG'] = '请输入角色名字'
    #
    #     data = {
    #             'danhao':danhao
    #             ,'sp_name':sp_name
    #             ,'sp_bh':sp_bh
    #             ,'sp_type':sp_type
    #             ,'candi':candi
    #             ,'num':num
    #             ,'dw':dw
    #             ,'gys_id':gys_id
    #             ,'money':money
    #             ,'in_date':in_date
    #             ,'beizhu':beizhu,
    #             'cid': self.usr_id,
    #             'ctime': self.getToday(6),
    #             'uid': self.usr_id,
    #             'utime': self.getToday(6)
    #     }
    #
    #
    #     if pk != '':  #update
    #         #如果是更新，就去掉cid，ctime 的处理.
    #         data.pop('cid')
    #         data.pop('ctime')
    #         #data.pop('random')
    #
    #         self.db.update('cggl_cg' , data , " id = %s " % pk)
    #
    #     else:  #insert
    #         #如果是插入 就去掉 uid，utime 的处理
    #         data.pop('uid')
    #         data.pop('utime')
    #
    #         self.db.insert('cggl_cg' , data)
    #         pk = self.db.insertid('cggl_cg_id')#这个的格式是表名_自增字段
    #         dR['isadd'] = 1
    #     #self.listdata_save(pk,danhao)
    #     dR['pk'] = pk
    #
    #     return dR
    # def delete_data(self):
    #     pk = self.pk
    #     dR = {'R':'', 'MSG':''}
    #
    #     self.db.query("update wechat_address set del_flag=1,del_time=now() where id= %s" % pk)
    #     return dR
