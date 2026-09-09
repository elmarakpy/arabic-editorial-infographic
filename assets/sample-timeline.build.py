#!/usr/bin/env python3
import subprocess, os
from PIL import Image
SC = "/private/tmp/claude-502/-Users-apple-Mutlaq-Studio-Toot/62f4849e-8858-42eb-a14f-8fad76f467d2/scratchpad"

CSS = """
:root{--navy:#0E2A4A;--navy2:#0A2140;--deep:#071730;--orange:#E9812A;--orange2:#F59A3C;--cream:#F3EAD3;}
*{margin:0;padding:0;box-sizing:border-box;font-family:"SF Arabic","Geeza Pro","Damascus",sans-serif}
.stage{position:absolute;left:0;width:1080px;height:1920px;direction:rtl;color:#fff;overflow:hidden;
 background:
  linear-gradient(135deg,rgba(30,70,120,.35) 0 22%,transparent 22% 40%,rgba(12,40,74,.5) 40% 60%,transparent 60% 78%,rgba(30,70,120,.30) 78%),
  linear-gradient(215deg,rgba(20,55,100,.30) 0 30%,transparent 30% 62%,rgba(10,30,60,.5) 62%),
  linear-gradient(180deg,var(--navy) 0%, var(--navy2) 55%, var(--deep) 100%);}
.logo{position:absolute;top:56px;left:0;right:0;text-align:center;z-index:3}
.logo .tri{width:70px;height:60px;margin:0 auto 8px;clip-path:polygon(50% 0,100% 100%,0 100%);
 background:linear-gradient(180deg,#fff,#ccd6e2);opacity:.92}
.logo b{display:block;font-size:22px;letter-spacing:3px;color:#e6edf6;font-family:Georgia,serif}
.logo small{display:block;font-size:18px;color:#b9c6d8;letter-spacing:1px}
.head{position:absolute;top:250px;right:70px;left:70px;z-index:3;display:flex;justify-content:center;align-items:center;gap:6px}
.head .three{font-size:330px;font-weight:800;line-height:.8;color:var(--orange);
 text-shadow:0 8px 40px rgba(233,129,42,.35)}
.htext{position:relative;font-size:76px;font-weight:800;line-height:1.12;color:#fff;text-align:right}
.htext .kick{position:absolute;top:-6px;right:6px;font-size:40px;font-weight:700;color:var(--orange2)}
.htext .pad{display:block;height:44px}
.grid{position:absolute;top:648px;right:98px;left:52px;z-index:3;display:flex;gap:22px}
.col{flex:1;display:flex;flex-direction:column;gap:44px}
.ev .yr{font-size:48px;font-weight:800;color:var(--orange);position:relative;padding-left:28px}
.ev .yr:after{content:"\\25C2";position:absolute;left:0;top:8px;font-size:30px;color:var(--orange)}
.ev .tx{font-size:31px;font-weight:600;line-height:1.34;color:#eaf1fb;margin-top:8px}
/* scene */
.obelisk{position:absolute;bottom:250px;right:180px;width:118px;height:560px;z-index:2;
 background:linear-gradient(180deg,#caa46a,#8f6a37);clip-path:polygon(38% 0,62% 0,72% 8%,60% 100%,40% 100%,28% 8%);
 box-shadow:0 0 60px rgba(233,160,80,.35)}
.obelisk:before{content:"";position:absolute;inset:0;opacity:.4;background:repeating-linear-gradient(0deg,rgba(60,40,10,.5) 0 6px,transparent 6px 22px)}
.facade{position:absolute;bottom:0;left:0;right:0;height:440px;z-index:1;
 background:linear-gradient(180deg,transparent,rgba(4,10,22,.4) 40%, #04080f 100%);}
.facade:before{content:"";position:absolute;bottom:120px;left:-4%;width:64%;height:360px;transform:skewX(-8deg);
 background:repeating-linear-gradient(58deg,#3a2a12 0 10px,#caa050 10px 16px,#7a5a24 16px 40px);
 clip-path:polygon(0 100%,100% 40%,100% 100%);opacity:.9;filter:brightness(1.05)}
.facade:after{content:"";position:absolute;bottom:0;left:0;right:0;height:110px;background:#04080f}
.credit,.tag{}
.src{position:absolute;top:1180px;right:20px;z-index:5;writing-mode:vertical-rl;font-size:30px;font-weight:700;color:#dbe4f0;letter-spacing:2px}
.credit{position:absolute;bottom:96px;left:0;right:0;z-index:6;text-align:center}
.credit .rule{width:120px;height:3px;background:var(--orange);margin:0 auto 14px;border-radius:2px}
.credit b{font-size:32px;font-weight:700;color:#fff;letter-spacing:1px}
.tag{position:absolute;bottom:48px;left:0;right:0;text-align:center;z-index:6;color:#8fa2bd;opacity:.6;font-size:20px}
"""

BODY = """
<div class="logo"><div class="tri"></div><b>GRAND EGYPTIAN MUSEUM</b><small>المتحف المصري الكبير</small></div>
<div class="head">
  <div class="three">3</div>
  <div class="htext"><span class="kick">رحلة</span><span class="pad"></span>عقود لبناء<br>المتحف المصري<br>الكبير</div>
</div>
<div class="grid">
  <div class="col">
    <div class="ev"><div class="yr">1992</div><div class="tx">تخصيص مساحة شمال منطقة الأهرام</div></div>
    <div class="ev"><div class="yr">2005</div><div class="tx">بدء المرحلة الأولى</div></div>
  </div>
  <div class="col">
    <div class="ev"><div class="yr">2002</div><div class="tx">وضع حجر أساس المتحف الكبير</div></div>
    <div class="ev"><div class="yr">2010</div><div class="tx">افتتاح مركز الحفظ الأثري</div></div>
    <div class="ev"><div class="yr">2018</div><div class="tx">نقل تمثال رمسيس الثاني إلى بهو المتحف</div></div>
    <div class="ev"><div class="yr">2021</div><div class="tx">إنهاء 90 % من البنية التحتية الرقمية</div></div>
    <div class="ev"><div class="yr">2024</div><div class="tx">افتتاح المتحف جزئيا أمام الزائرين</div></div>
  </div>
  <div class="col">
    <div class="ev"><div class="yr">2003</div><div class="tx">وضع التصميمات الهندسية</div></div>
    <div class="ev"><div class="yr">2015</div><div class="tx">بدء المرحلتين الثانية والثالثة</div></div>
    <div class="ev"><div class="yr">2020</div><div class="tx">إنهاء 97 % من أعمال الإنشاء</div></div>
    <div class="ev"><div class="yr">2023</div><div class="tx">إكمال تجهيز الدرج العظيم</div></div>
    <div class="ev"><div class="yr">1 نوفمبر 2025</div><div class="tx">الإفتتاح الرسمي</div></div>
  </div>
</div>
<div class="facade"></div>
<div class="obelisk"></div>
<div class="src">المصدر: وكالات</div>
<div class="credit"><div class="rule"></div><b>نمط تحريري · عيّنة</b></div>
<div class="tag">sample · arabic-editorial-infographic</div>
"""

# Single pass: fit the 1080x1920 design into a SQUARE 1080 page via scale(0.5625),
# render at -s1920 (device 1.7778x) so the design rasterizes at native res, then crop.
S=0.5625; LEFT=int(round((1080-1080*S)/2))  # =236
PAGE=f"""<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>
html,body{{margin:0;width:1080px;height:1080px;overflow:hidden;background:#071730}}{CSS}
.stage{{top:0;left:{LEFT}px;transform:scale({S});transform-origin:top left}}
</style></head><body><div class="stage">{BODY}</div></body></html>"""
f=os.path.join(SC,"gem_full.html"); open(f,"w").write(PAGE)
png=os.path.join(SC,"gem_full.html.png")
if os.path.exists(png): os.remove(png)
subprocess.run(["qlmanage","-t","-s","1920","-o",SC,f],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
img=Image.open(png).convert("RGB")
if img.size!=(1920,1920): img=img.resize((1920,1920))
x0=int(round(LEFT/1080*1920))  # =420
out=os.path.join(SC,"gem.png"); img.crop((x0,0,x0+1080,1920)).save(out); print("saved",out,(1080,1920))
