-- SOURCE /home/epcc/proj/diabete/data/sql/data_operation.sql


-- mysql -u root --show-warnings -p

-- CREATE DATABASE diabete;

USE diabete

SELECT 'Creating tables' AS '';
CREATE TABLE d_train(
id INT, 
sex BIT(1), -- 性别
age INT, -- 年龄  
exam_date DATETIME, -- 体检日期
AST FLOAT(10,6), -- 天门冬氨酸氨基转换酶
ALT FLOAT(10,6), -- 丙氨酸氨基转换酶
ALP FLOAT(10,6), -- 碱性磷酸酶
r_GT FLOAT(10,6), -- *r-谷氨酰基转换酶 
total_protein FLOAT(10,6), -- 总蛋白
albumino FLOAT(10,6), -- 白蛋白
globulin FLOAT(10,6), -- *球蛋白
aga FLOAT(10,6), -- 白球比例
triglyceride FLOAT(10,6), -- 甘油三酯
total_cholesterol FLOAT(10,6), -- 总胆固醇
hdl_c FLOAT(10,6), -- 高密度脂蛋白胆固醇
ldl_c FLOAT(10,6), -- 低密度脂蛋白胆固醇
urea FLOAT(10,6), -- 尿素  
creatinine FLOAT(10,6), -- 肌酐 
ua FLOAT(10,6), -- 尿酸 
HBsAg FLOAT(10,6), -- 乙肝表面抗原 
HbsAb FLOAT(10,6), -- 乙肝表面抗体 
HbeAg FLOAT(10,6), -- 乙肝e抗原 
HbeAb FLOAT(10,6), -- 乙肝e抗体 
HbcAb FLOAT(10,6), -- 乙肝核心抗体 
WBC FLOAT(10,6), -- 白细胞计数  
RBC FLOAT(10,6), -- 红细胞计数  
HGB FLOAT(10,6), -- 血红蛋白  
HCT FLOAT(10,6), --  红细胞压积  
mcv FLOAT(10,6), -- 红细胞平均体积 
mch FLOAT(10,6), -- 红细胞平均血红蛋白量 
MCHC FLOAT(10,6), -- 红细胞平均血红蛋白浓度
RDW FLOAT(10,6), -- 红细胞体积分布宽度  
PLT FLOAT(10,6), -- 血小板计数  
MPV FLOAT(10,6), -- 血小板平均体积 
pdw FLOAT(10,6), -- 血小板体积分布宽度  
pct FLOAT(10,6), -- 血小板比积  
GRA FLOAT(10,6), -- 中性粒细胞% 
LYM FLOAT(10,6), -- 淋巴细胞%  
MO FLOAT(10,6), -- 单核细胞%  
EO FLOAT(10,6), -- 嗜酸细胞%  
BA FLOAT(10,6), -- 嗜碱细胞%   
glucose FLOAT(10,6), -- 血糖
PRIMARY KEY(id));

-- system cd /home/epcc/proj/diabete/data/output

SELECT 'Insert d_train' AS '';
LOAD DATA LOCAL INFILE '/home/epcc/proj/diabete/data/output/d_train.csv' INTO TABLE d_train;


-- DROP TABLE d_train;

SELECT COUNT(*) FROM d_train;

-- 5642



