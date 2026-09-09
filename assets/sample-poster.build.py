#!/usr/bin/env python3
import subprocess, os
from PIL import Image

SC = "/private/tmp/claude-502/-Users-apple-Mutlaq-Studio-Toot/62f4849e-8858-42eb-a14f-8fad76f467d2/scratchpad"
W, H = 1080, 1920

CSS = """
:root{--navy:#0A1B33;--navy2:#06122A;--green:#33C46E;--green2:#7DE6A0;--cyan:#CFE8FF;--ink:#0d2240;}
*{margin:0;padding:0;box-sizing:border-box;font-family:"SF Arabic","Geeza Pro","Damascus",sans-serif}
.stage{position:absolute;left:0;width:1080px;height:1920px;direction:rtl;color:#fff;overflow:hidden;
 background:radial-gradient(140% 55% at 50% -8%, #12633f 0%, #0d3a4a 26%, var(--navy) 55%, var(--navy2) 100%);}
.flag{position:absolute;top:0;left:0;right:0;height:340px;opacity:.5;
 background:linear-gradient(115deg,rgba(23,140,86,.85) 0%,rgba(20,110,80,.35) 40%,rgba(10,40,60,0) 72%);
 -webkit-mask:linear-gradient(180deg,#000 30%,transparent);}
.flag:after{content:"";position:absolute;inset:0;opacity:.25;
 background:repeating-linear-gradient(112deg,#0e5a3a 0 60px,transparent 60px 130px);-webkit-mask:linear-gradient(180deg,#000,transparent)}
.wrap{position:relative;z-index:2;padding:0 70px}
.h1{margin-top:210px;font-size:104px;font-weight:800;line-height:1.04;letter-spacing:-2px;text-align:center;color:#fff;text-shadow:0 4px 30px rgba(0,0,0,.4)}
.h1 .g{color:var(--green2)}
.h2{margin-top:16px;font-size:62px;font-weight:800;text-align:center;color:#fff}
.h2 .y{color:var(--green2)}
.rows{position:relative;z-index:2;margin-top:52px;display:flex;flex-direction:column;gap:30px;padding:0 55px}
.row{display:flex;align-items:center;gap:30px;background:linear-gradient(90deg,rgba(255,255,255,.05),rgba(255,255,255,.02));
 border:1px solid rgba(255,255,255,.06);border-radius:26px;padding:26px 30px;min-height:286px}
.num{flex:0 0 240px;text-align:center}
.num b{font-size:180px;font-weight:800;line-height:.9;
 background:linear-gradient(180deg,var(--green2),var(--green));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
 filter:drop-shadow(0 6px 26px rgba(51,196,110,.35))}
.num span{display:block;font-size:52px;font-weight:800;color:var(--green2);margin-top:6px}
.labels{flex:1;display:flex;flex-direction:column;gap:26px;justify-content:center}
.lab{position:relative;padding-right:34px;font-size:42px;font-weight:700;line-height:1.32;color:#eaf3ff}
.lab:before{content:"\\25C2";position:absolute;right:0;top:2px;color:var(--green2);font-size:30px}
.pic{flex:0 0 196px;height:214px;border-radius:20px;position:relative;overflow:hidden;
 background:radial-gradient(120% 120% at 30% 20%, #17324f, #0a1a2e 70%);
 box-shadow:inset 0 0 60px rgba(0,0,0,.5)}
.pic:before{content:"";position:absolute;inset:0;opacity:.5;
 background:repeating-linear-gradient(60deg,rgba(90,150,220,.18) 0 2px,transparent 2px 26px),
 radial-gradient(circle at 60% 55%, rgba(120,180,255,.35), transparent 45%)}
.pic:after{content:"AI";position:absolute;bottom:16px;left:18px;font-size:26px;font-weight:800;color:#6fb3ff;letter-spacing:2px;opacity:.8}
.foot{position:absolute;bottom:56px;left:0;right:0;z-index:2;display:flex;align-items:center;justify-content:center;gap:34px;opacity:.92}
.foot .brand{font-size:44px;font-weight:700;letter-spacing:1px;color:#eaf3ff;font-family:Georgia,serif}
.foot .sep{width:2px;height:52px;background:rgba(255,255,255,.35)}
.foot .sd{display:flex;flex-direction:column;line-height:1.05}
.foot .sd b{font-size:40px;font-weight:800;letter-spacing:3px}
.foot .sd small{font-size:20px;opacity:.7}
.tag{position:absolute;bottom:18px;left:0;right:0;text-align:center;z-index:2;color:#9fb6d6;opacity:.6;font-size:22px}
"""

BODY = """
<div class="flag"></div>
<div class="wrap">
  <div class="h1">المملكة <span class="g">تتقدم</span><br>في الذكاء الاصطناعي</div>
  <div class="h2">وفقاً لمؤشر <span class="y">ستانفورد 2025</span></div>
</div>
<div class="rows">
  <div class="row">
    <div class="num"><b>3</b><span>عالميًا</span></div>
    <div class="labels"><div class="lab">في نماذج الذكاء الاصطناعي الرائدة</div>
      <div class="lab">في نسبة نمو الوظائف بمجال الذكاء الاصطناعي</div></div>
    <div class="pic"></div>
  </div>
  <div class="row">
    <div class="num"><b>7</b><span>عالميًا</span></div>
    <div class="labels"><div class="lab">في استقطاب كفاءات الذكاء الاصطناعي</div></div>
    <div class="pic"></div>
  </div>
  <div class="row">
    <div class="num"><b>8</b><span>عالميًا</span></div>
    <div class="labels"><div class="lab">في الوعي العام بالذكاء الاصطناعي</div>
      <div class="lab">في الاستشهادات العلمية بالذكاء الاصطناعي</div></div>
    <div class="pic"></div>
  </div>
</div>
<div class="foot"><span class="brand">Stanford</span><span class="sep"></span>
  <span class="sd"><b>SDAIA</b><small>الهيئة السعودية للبيانات والذكاء الاصطناعي</small></span></div>
<div class="tag">sample · arabic-editorial-infographic</div>
"""

def page(offset):
    return f"""<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>
    html,body{{margin:0;width:1080px;height:1080px;overflow:hidden;background:#06122A}}
    {CSS}
    .stage{{top:{offset}px}}
    </style></head><body><div class="stage">{BODY}</div></body></html>"""

tiles = []
for i, off in enumerate([0, -840]):   # top square, then bottom (shifted up 840)
    f = os.path.join(SC, f"tile{i}.html")
    open(f, "w").write(page(off))
    png = os.path.join(SC, f"tile{i}.html.png")
    if os.path.exists(png): os.remove(png)
    subprocess.run(["qlmanage","-t","-s","1080","-o",SC,f], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    tiles.append(Image.open(png).convert("RGB").resize((1080,1080)))

# stack: top full 1080 + bottom rows 240..1080 (design 1080..1920)
canvas = Image.new("RGB",(1080,1920))
canvas.paste(tiles[0].crop((0,0,1080,1080)),(0,0))
canvas.paste(tiles[1].crop((0,240,1080,1080)),(0,1080))
out = os.path.join(SC,"sdaia.png")
canvas.save(out)
print("saved", out, canvas.size)
