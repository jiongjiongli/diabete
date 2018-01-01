#!/usr/bin/python
#coding=utf-8

import pdb
import datetime



def set_default_value(part):
        if part == '':
            part = '\N'
        return part

class Train_Info(object):

    def __init__(self):
        super(Train_Info, self).__init__()
        self.id = None # 
        self.sex = None # 性别    
        self.age = None # 年龄  
        self.exam_date = None # 体检日期

        self.AST = None # 天门冬氨酸氨基转换酶
        self.ALT = None # 丙氨酸氨基转换酶
        self.ALP = None # 碱性磷酸酶
        self.r_GT = None # *r-谷氨酰基转换酶

        self.total_protein = None # 总蛋白
        self.albumino = None # 白蛋白
        self.globulin = None # *球蛋白
        self.aga = None # 白球比例
        self.triglyceride = None # 甘油三酯
        self.total_cholesterol = None # 总胆固醇
        self.hdl_c = None # 高密度脂蛋白胆固醇
        self.ldl_c = None # 低密度脂蛋白胆固醇
        self.urea = None # 尿素  
        self.creatinine = None # 肌酐 
        self.ua = None # 尿酸 
        self.HBsAg = None # 乙肝表面抗原 
        self.HbsAb = None # 乙肝表面抗体 
        self.HbeAg = None # 乙肝e抗原 
        self.HbeAb = None # 乙肝e抗体 
        self.HbcAb = None # 乙肝核心抗体 
        self.WBC = None # 白细胞计数  
        self.RBC = None # 红细胞计数  
        self.HGB = None # 血红蛋白  
        self.HCT = None #  红细胞压积  
        self.mcv = None # 红细胞平均体积 
        self.mch = None # 红细胞平均血红蛋白量 
        self.MCHC = None # 红细胞平均血红蛋白浓度
        self.RDW = None # 红细胞体积分布宽度  
        self.PLT = None # 血小板计数  
        self.MPV = None # 血小板平均体积 
        self.pdw = None # 血小板体积分布宽度  
        self.pct = None # 血小板比积  
        self.GRA = None # 中性粒细胞% 
        self.LYM = None # 淋巴细胞%  
        self.MO = None # 单核细胞%  
        self.EO = None # 嗜酸细胞%  
        self.BA = None # 嗜碱细胞%   

        self.glucose = None # 血糖

    def set_values(self, parts):
        curr_index = 0
        self.id = set_default_value(parts[curr_index]) #
        curr_index += 1 
        self.sex = set_default_value(parts[curr_index]) # 性别    
        curr_index += 1
        self.age = set_default_value(parts[curr_index]) # 年龄  
        curr_index += 1
        self.exam_date = set_default_value(parts[curr_index]) # 体检日期
        curr_index += 1

        self.AST = set_default_value(parts[curr_index]) # 天门冬氨酸氨基转换酶
        curr_index += 1
        self.ALT = set_default_value(parts[curr_index]) # 丙氨酸氨基转换酶
        curr_index += 1
        self.ALP = set_default_value(parts[curr_index]) # 碱性磷酸酶
        curr_index += 1
        self.r_GT = set_default_value(parts[curr_index]) # *r-谷氨酰基转换酶
        curr_index += 1
        self.total_protein = set_default_value(parts[curr_index]) # 总蛋白
        curr_index += 1
        self.albumino = set_default_value(parts[curr_index]) # 白蛋白
        curr_index += 1
        self.globulin = set_default_value(parts[curr_index]) # *球蛋白
        curr_index += 1
        self.aga = set_default_value(parts[curr_index]) # 白球比例
        curr_index += 1
        self.triglyceride = set_default_value(parts[curr_index]) # 甘油三酯
        curr_index += 1
        self.total_cholesterol = set_default_value(parts[curr_index]) # 总胆固醇
        curr_index += 1
        self.hdl_c = set_default_value(parts[curr_index]) # 高密度脂蛋白胆固醇
        curr_index += 1
        self.ldl_c = set_default_value(parts[curr_index]) # 低密度脂蛋白胆固醇
        curr_index += 1
        self.urea = set_default_value(parts[curr_index]) # 尿素  
        curr_index += 1
        self.creatinine = set_default_value(parts[curr_index]) # 肌酐 
        curr_index += 1
        self.ua = set_default_value(parts[curr_index]) # 尿酸 
        curr_index += 1
        self.HBsAg = set_default_value(parts[curr_index]) # 乙肝表面抗原 
        curr_index += 1
        self.HbsAb = set_default_value(parts[curr_index]) # 乙肝表面抗体 
        curr_index += 1
        self.HbeAg = set_default_value(parts[curr_index]) # 乙肝e抗原 
        curr_index += 1
        self.HbeAb = set_default_value(parts[curr_index]) # 乙肝e抗体 
        curr_index += 1
        self.HbcAb = set_default_value(parts[curr_index]) # 乙肝核心抗体 
        curr_index += 1
        self.WBC = set_default_value(parts[curr_index]) # 白细胞计数  
        curr_index += 1
        self.RBC = set_default_value(parts[curr_index]) # 红细胞计数  
        curr_index += 1
        self.HGB = set_default_value(parts[curr_index]) # 血红蛋白  
        curr_index += 1
        self.HCT = set_default_value(parts[curr_index]) #  红细胞压积  
        curr_index += 1
        self.mcv = set_default_value(parts[curr_index]) # 红细胞平均体积 
        curr_index += 1
        self.mch = set_default_value(parts[curr_index]) # 红细胞平均血红蛋白量 
        curr_index += 1
        self.MCHC = set_default_value(parts[curr_index]) # 红细胞平均血红蛋白浓度
        curr_index += 1
        self.RDW = set_default_value(parts[curr_index]) # 红细胞体积分布宽度  
        curr_index += 1
        self.PLT = set_default_value(parts[curr_index]) # 血小板计数  
        curr_index += 1
        self.MPV = set_default_value(parts[curr_index]) # 血小板平均体积 
        curr_index += 1
        self.pdw = set_default_value(parts[curr_index]) # 血小板体积分布宽度  
        curr_index += 1
        self.pct = set_default_value(parts[curr_index]) # 血小板比积  
        curr_index += 1
        self.GRA = set_default_value(parts[curr_index]) # 中性粒细胞% 
        curr_index += 1
        self.LYM = set_default_value(parts[curr_index]) # 淋巴细胞%  
        curr_index += 1
        self.MO = set_default_value(parts[curr_index]) # 单核细胞%  
        curr_index += 1
        self.EO = set_default_value(parts[curr_index]) # 嗜酸细胞%  
        curr_index += 1
        self.BA = set_default_value(parts[curr_index]) # 嗜碱细胞%   
        curr_index += 1

        self.glucose = set_default_value(parts[curr_index]) # 血糖
        curr_index += 1

    def update_values(self):
        # pdb.set_trace()
        self.sex = '' 
        if self.sex.decode('gb2312') == '男'.decode('utf-8'):
            self.sex = '1'
        if self.sex.decode('gb2312') == '女'.decode('utf-8'):
            self.sex = '0'
        self.exam_date = self.format_date_str(self.exam_date)

    def format_date_str(self, date_str):
        date_value = datetime.datetime.strptime(date_str, '%d/%m/%Y')
        return date_value.strftime('%Y-%m-%d %H:%M')

    @classmethod
    def deserialize(cls, parts):
        ti = Train_Info()
        ti.set_values(parts)
        ti.update_values()
        return ti

    def serialize(self):
        return '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (
            self.id, 
            self.sex, # 性别
            self.age, # 年龄  
            self.exam_date, # 体检日期
            self.AST, # 天门冬氨酸氨基转换酶
            self.ALT, # 丙氨酸氨基转换酶
            self.ALP, # 碱性磷酸酶
            self.r_GT, # *r-谷氨酰基转换酶 
            self.total_protein, # 总蛋白
            self.albumino, # 白蛋白
            self.globulin, # *球蛋白
            self.aga, # 白球比例
            self.triglyceride, # 甘油三酯
            self.total_cholesterol, # 总胆固醇
            self.hdl_c, # 高密度脂蛋白胆固醇
            self.ldl_c, # 低密度脂蛋白胆固醇
            self.urea, # 尿素  
            self.creatinine, # 肌酐 
            self.ua, # 尿酸 
            self.HBsAg, # 乙肝表面抗原 
            self.HbsAb, # 乙肝表面抗体 
            self.HbeAg, # 乙肝e抗原 
            self.HbeAb, # 乙肝e抗体 
            self.HbcAb, # 乙肝核心抗体 
            self.WBC, # 白细胞计数  
            self.RBC, # 红细胞计数  
            self.HGB, # 血红蛋白  
            self.HCT, #  红细胞压积  
            self.mcv, # 红细胞平均体积 
            self.mch, # 红细胞平均血红蛋白量 
            self.MCHC, # 红细胞平均血红蛋白浓度
            self.RDW, # 红细胞体积分布宽度  
            self.PLT, # 血小板计数  
            self.MPV, # 血小板平均体积 
            self.pdw, # 血小板体积分布宽度  
            self.pct, # 血小板比积  
            self.GRA, # 中性粒细胞% 
            self.LYM, # 淋巴细胞%  
            self.MO, # 单核细胞%  
            self.EO, # 嗜酸细胞%  
            self.BA, # 嗜碱细胞%   
            self.glucose) # 血糖


def load_file():
    file_path = '/home/epcc/proj/diabete/data/input/d_train.csv'
    out_file_path = '/home/epcc/proj/diabete/data/output/d_train.csv'
    elems_len = 42
    line_number = 0
    first_line = True
    infos = []
    # max_width = 0

    with open(file_path, 'r') as file_content, \
    open(out_file_path, 'w') as output_file:
        for line in file_content:
            line_number += 1
            if first_line:
                first_line = False
            else:
                line = line.rstrip('\r\n')
                parts = line.split(',')
                assert len(parts) == elems_len
                info = Train_Info.deserialize(parts)
                infos.append(info)
                s = info.serialize()
                output_file.write(s)
                # for part in parts:
                    # max_width = max(max_width, len(part))

    # print 'max_width: %d' % (max_width)

if __name__ == '__main__':
    load_file()



