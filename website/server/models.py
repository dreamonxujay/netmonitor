from django.db import models

#
class Hosts(models.Model):
	ID = models.AutoField(blank=False, primary_key=True)  
	IPADDR = models.GenericIPAddressField(protocol='IPv4', unpack_ipv4=False, null=True, blank=True)
	PROJ_AREA = models.CharField(max_length=40, null=True, blank=True)
	OPERATOR = models.CharField(max_length=40, null=True, blank=True)
	PROJ_NAME = models.TextField(max_length=200, null=True, blank=True)
	PRODUCT_NAME = models.TextField(max_length=200, null=True, blank=True)
	PROVINCE_NAME = models.CharField(max_length=20, null=True, blank=True)
	IDC_NAME = models.CharField(max_length=200, null=True, blank=True)
	PROJ_MANAGER = models.CharField(max_length=40, null=True, blank=True)
	PROJ_PERSON_IN_CHARGE = models.CharField(max_length=40, null=True, blank=True)
	PROJ_PERSON_IN_CHARGE_TEL = models.IntegerField(null=True, blank=True)
	PROJ_PERSON_IN_CHARGE_WECHAT = models.CharField(max_length=20, null=True, blank=True)
	EQPT_STATUS = models.CharField(max_length=20, null=True, blank=True)
	EQPT_DESC = models.TextField(max_length=300, null=True, blank=True)

class Ports(models.Model):
	ID = models.AutoField(blank=False, primary_key=True)  
	# HOSTS_ID = models.ForeignKey(Hosts, on_delete=models.CASCADE)
	POSTS = models.IntegerField(null=True, blank=True)
	POSTS_DESC = models.TextField(max_length=2000, null=True, blank=True)
	RULE_ID = models.CharField(max_length=300, null=True, blank=True)  


class History(models.Model):
	DATE = models.DateTimeField(auto_now = True, null=True, blank=True) # 字段保存时会自动保存当前时间
	HOSTS_ID = models.CharField(max_length=40, null=True, blank=True)
	PROTS_ID  = models.CharField(max_length=40, null=True, blank=True)
	SCAN_TYPE = models.CharField(max_length=40, null=True, blank=True)
	STATUS = models.CharField(max_length=40, null=True, blank=True)
	DETAILS = models.CharField(max_length=40, null=True, blank=True)

class Alerts(models.Model):
	ID = models.AutoField(blank=False, primary_key=True)  
	DATE = models.DateTimeField(auto_now = True, null=True, blank=True) # 字段保存时会自动保存当前时间
	HOSTS_ID = models.CharField(max_length=40, null=True, blank=True)
	POSTS_ID = models.CharField(max_length=40, null=True, blank=True)
	STATUS = models.CharField(max_length=40, null=True, blank=True)
	DETAILS = models.CharField(max_length=40, null=True, blank=True)

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
