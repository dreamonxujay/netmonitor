from django.db import models

#

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Hosts(models.Model):
	ID = models.AutoField(blank=False, primary_key=True)  
	IPADDR = models.GenericIPAddressField(protocol='IPv4', unpack_ipv4=False)
	PROJ_AREA = models.CharField(max_length=40)
	OPERATOR = models.CharField(max_length=40)
	PROJ_NAME = models.CharField(max_length=200)
	PRODUCT_NAME = models.CharField(max_length=200)
	PROVINCE_NAME = models.CharField(max_length=20)
	IDC_NAME = models.CharField(max_length=200)
	PROJ_MANAGER = models.CharField(max_length=40)
	PROJ_PERSON_IN_CHARGE = models.CharField(max_length=40)
	PROJ_PERSON_IN_CHARGE_TEL = models.IntegerField(max_length=11)
	PROJ_PERSON_IN_CHARGE_WECHAT = models.CharField(max_length=20)
	EQPT_STATUS = models.CharField(max_length=20)
	EQPT_DESC = models.CharField(max_length=300)

class Ports(models.Model):
	ID = models.AutoField(blank=False, primary_key=True)  
	# HOSTS_ID = models.ForeignKey(Hosts, on_delete=models.CASCADE)
	POSTS = models.IntegerField(max_length=5)
	POSTS_DESC = models.CharField(max_length=2000)
	RULE_ID = models.CharField(max_length=300)  


class History(models.Model):
	DATE = models.DateTimeField(auto_now = True) # 字段保存时会自动保存当前时间
	HOSTS_ID = models.CharField(max_length=40)
	PROTS_ID  = models.CharField(max_length=40)
	SCAN_TYPE = models.CharField(max_length=40)
	STATUS = models.CharField(max_length=40)
	DETAILS = models.CharField(max_length=40)

class Alerts(models.Model):
	ID = models.AutoField(blank=False, primary_key=True)  
	DATE = models.DateTimeField(auto_now = True) # 字段保存时会自动保存当前时间
	HOSTS_ID = models.CharField(max_length=40)
	POSTS_ID = models.CharField(max_length=40)
	STATUS = models.CharField(max_length=40)
	DETAILS = models.CharField(max_length=40)

class Rules(models.Model):
	ID = models.AutoField(blank=False, primary_key=True)  
	DESC = models.CharField(max_length=40)
	RULE = models.CharField(max_length=40)

class Alert_logs(models.Model):
	ID = models.AutoField(blank=False, primary_key=True)  
	AL_ID = models.CharField(max_length=40)
	STATUS = models.CharField(max_length=40)
	DATE = models.DateTimeField(auto_now = True) # 字段保存时会自动保存当前时间
	DETAILS = models.CharField(max_length=40)
