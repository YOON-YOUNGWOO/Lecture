from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Member, Lecture, Member_Lecture
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
import os
# Create your views here.

# 첫페이지
def home(req):
    if req.session.get('id'):
        if req.session.get('id') == "root":
            return render(req, 'homepage.html',{'session_root':'root','session_ok':'ok'})
        return render(req, 'homepage.html',{'session_ok':'ok'})
    else:
        return render(req, 'homepage.html')

# 로그인페이지
def login(req):
    return render(req, 'login.html')

# 로그인 체크
def login_check(req):
    logged_member = Member.objects.filter(memberid=req.POST.get('id'), memberpw = req.POST.get('pw'))
    
    if logged_member:
        req.session["id"] = req.POST.get('id')#eeee
        # print(req.session.get('id'))
        return redirect('../home/')
    else:
        return redirect('../login/')

# 로그아웃
def logout(req):
    if req.session.pop('id'):
        return redirect('../home/')
    else:
        return render(req, 'homepage.html',{'session_login':'로그아웃으로 세션 x'})

# 장바구니 페이지
def cart(req):
    return render(req, 'cart.html')

# 회원가입 페이지
def signup(req):
    return render(req, 'signup.html')

# 회원가입 체크
def signupcheck(req):
    if req.method == "POST":
        userid = req.POST.get('id')
        username = req.POST.get('name')
        password = req.POST.get('password')
        password_check = req.POST.get('password_check')
        useremail = req.POST.get('email')
        usergender = req.POST.get('gender')

        if not (userid and username and password and password_check and useremail and usergender):
            return render(req, 'signup.html',{'err':'모든 값을 입력해주셔야 합니다.'})
        else:
            logged_member = Member.objects.filter(memberid=userid)
            if logged_member:
                return render(req,'signup.html',{'err2':'아이디가 중복되었습니다.'})
            elif password_check != password:
                return render(req,'signup.html',{'err3':'패스워드가 동일하지 않습니다.'})
            elif usergender == "nopick":
                return render(req,'signup.html',{'err4':'성별 선택하세요'})
            else:
                new_member = Member(memberid=userid, membername=username, memberpw=password, gender=usergender, memberemail = useremail)
                new_member.save()
                messages.info(req,'회원가입 성공')
                return redirect('../login/',messages.info)
    else:
        return render(req, 'signup.html')

# 회원가입 아이디 중복체크
def id_ck(req):
    id_ck = Member.objects.filter(memberid = req.POST.get('id'))
    if id_ck:
        return HttpResponse("중복")
    elif req.POST.get('id').strip() == '':
        return HttpResponse("빈칸")
    else:
        return HttpResponse("통과")

#  회원정보 수정 페이지
def editinfo(req):
    session_ck = req.session.get('id')
    try:
        logged_member =Member.objects.get(memberid=session_ck)
        if session_ck:
            if req.session.get('id') == "root":
                return render(req, 'editinfo.html',{'memberinfo':logged_member,'session_root':'root','session_ok':'ok'})
            return render(req, 'editinfo.html',{'memberinfo':logged_member,'session_ok':'ok'})
        else:
            return redirect('../login/')
    except Member.DoesNotExist:
        return redirect("../login/")

#  회원정보 수정 체크
def profile_edit(req):
    session_ok = req.session.get('id')
    pw1 = req.POST.get('pw_1')
    pw2 = req.POST.get('pw_2')
    member_profile = req.POST.get('memberprofile')
    member_email = req.POST.get('memberemail')
    
    try:
        logged_member = Member.objects.get(memberid=session_ok)
        if logged_member:
            if pw1 != pw2:
                if req.session.get('id') == "root":
                    return render(req, 'editinfo.html',{'err':'비밀번호가 틀립니다.', 'memberinfo':logged_member,'session_root':'root','session_ok':'ok'})
                return render(req, 'editinfo.html',{'err':'비밀번호가 틀립니다.', 'memberinfo':logged_member,'session_ok':'ok'})
            else:
                logged_member.memberpw = pw1
                logged_member.memberemail = member_email
                logged_member.memberprofile = member_profile
                logged_member.save()
                return redirect('../profile/')
        else:
            return redirect('../editinfo/')
    except Member.DoesNotExist:
        return redirect('../profile/')

# profile page
def profile(req):
    session_ck = req.session.get('id')
    try:
        logged_member =Member.objects.get(memberid=session_ck) # 현재 로그인 되어있는 세션값 = id 1개 
        membered_lecture = Member_Lecture.objects.filter(member_id= session_ck) # 여러개
        lecture = Lecture.objects.all()
        
        a = {}
        a['memberinfo'] = logged_member
        a['session_ok'] = 'dfrerewrew'
        a['session_root'] = 'root'
        a['lecture'] = lecture
        a['member_lecture'] = membered_lecture

        index = []
        for plus in membered_lecture:
            index.append(plus.lecture_id.lectureid)
        print(index)
        a['index'] = index

        if session_ck:
            return render(req, 'profile.html',a)
        else:
            return redirect('../login/')
    except Member.DoesNotExist:
        return redirect('../login/')
    except IndexError:
        messages.error(req, '강의를 등록하세요')
        return redirect('../product/')

# 회원 탈퇴
def memberleave(req):
    try:
        withdraw_member= Member.objects.get(memberid = req.session.get('id'), memberpw=req.POST.get('password'))
        if withdraw_member:
            if withdraw_member.memberid == req.session.get('id'):
                req.session.pop('id')
                withdraw_member.delete()
                return HttpResponse("탈퇴 완료")
                messages.info(req,'탈퇴 완료')
                return redirect('../home/',messages.info)
            else:
                return HttpResponse("Passwords do not match")
        else:
            return HttpResponse("Passwords do not match")
    except Exception as err:
        print(err)
        return HttpResponse("Passwords do not match")

# product page
def product(req):
    session_ck = req.session.get('id')
    try:
        lecture = Lecture.objects.all()
        if session_ck:
            if req.session.get('id') == "root":
                return render(req, 'product.html',{'lectureinfo':lecture,'session_root':'root','session_ok':'ok'})
            return render(req, 'product.html',{'lectureinfo':lecture,'session_ok':'ok'})
        else:
            return redirect('../login/')
    except Member.DoesNotExist:
        return redirect("../login/")
   
# start onclick
def class_plus(req):
    try:
        session_ck = req.session.get('id') # qq
        product_id = req.POST.get('pid') # 1
        member = Member.objects.get(memberid = session_ck)
        product = Lecture.objects.get(lectureid = product_id)
        #new_member = Member(memberid=userid, membername=username, memberpw=password, gender=usergender, memberemail = useremail)
        if Member_Lecture.objects.filter(member_id = session_ck, lecture_id = product_id):
            messages.error(req, '이미 등록된 강의입니다.')
            return redirect('../product')
        else:
            print(member.memberid) # qq
            print(product.lectureid) # 1
            ml_plus = Member_Lecture(member_id=member,lecture_id=product)
            ml_plus.save()
            messages.info(req, '신청 완료')
            return redirect('../product/')
    except Exception as err:
        print(err)
        return redirect('../product/')

def upload_file(req):
    if req.method == 'POST':
        print(req.FILES['my_file'])
        with open(os.path.abspath('./member/static/'+req.FILES['my_file'].name), 'wb+') as dest:
            for chunk in req.FILES['my_file'].chunks():
                dest.write(chunk)
        return render(req, 'homepage.html')
    else:
        return render(req, 'test2.html')

def test(req):
    return render(req, 'test.html')

def test2(req):
    return render(req, 'test2.html')

def ck_box(req):
    list = req.POST.getlist("dkdk")
    return render(req, 'checkbox2.html',{'list':list})

def ck_box2(req):
    return render(req, 'checkbox.html')

# 강의 삭제
def delete_lecture(req):
    lectureid = int(req.POST.get('lectureid'))
    sessionid = req.session.get('id')
    print(lectureid)
    print(sessionid)
    try:
        mem_lec = Member_Lecture.objects.get(member_id = sessionid,lecture_id = lectureid)
        print(mem_lec)
        if mem_lec:
            mem_lec.delete()
            return HttpResponse('삭제 완료')
    except Exception as err:
        print(err)
        return HttpResponse('삭제 실패')

# 강의 추가
def lecture_add(req):
    return render(req, 'lecture_add.html')