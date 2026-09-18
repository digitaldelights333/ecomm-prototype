import base64, os

SCRATCHPAD = "/private/tmp/claude-501/-Users-kerrynguyen-Library-Application-Support-Claude-scratch-workspaces-45a82dc2-899c-4111-89db-636e9dd5611c-c755861b-73af-42ff-b9a8-6def8014fe7a-scratch-2026-09-17-3e4ab8/5d677bf4-01ce-4ae3-89ae-74814a6bca11/scratchpad"
IMGDIR = os.path.join(SCRATCHPAD, "imgs")
OUTFILE = os.path.join(SCRATCHPAD, "cat-level2.html")

def b64img(name, ext="webp"):
    path = os.path.join(IMGDIR, name + "." + ext)
    mime = "image/" + ext
    with open(path, "rb") as f:
        return "data:" + mime + ";base64," + base64.b64encode(f.read()).decode()

LOGO = b64img("logo")

# Real product images from parts.cat.com Drivetrain (model=320, serialNumber=ZBN60173)
PI = {k: b64img(k) for k in ["p01","p02","p03","p04","p05","p06","p07","p08","p09","p10","p11","p12","p13","p14","p15","p16","p17","p18","p19","p20"]}
MACH = b64img("mach")  # 320 Excavator machine photo

AI_RING = "M146.9441,80.4873s-19.4829,30.9684-24.8493,39.4806c-.728,1.1547-2.3036,1.3963-3.3499.5197l-3.2698-2.7397c-.8644-.7243-1.0606-1.9759-.4593-2.9299l23.8364-38.2222c1.2222-2.116,1.4882-5.5896.2659-7.7065l-25.2972-42.2833c-1.6225-2.6259-4.1195-4.1863-7.1818-4.1863h-49.4686c-2.4434,0-4.6662.8747-6.563,3.833l-25.3649,43.3431c-1.2068,2.0903-1.2068,4.7189.0154,6.836l23.6882,38.1261c.6002.966.3868,2.2278-.4976,2.9427l-3.2926,2.6617c-1.053.8513-2.6099.5948-3.3263-.5542-5.263-8.4418-24.1294-38.8138-24.1294-38.8138-4.392-7.3564-4.392-8.8554,0-15.5869l25.6013-43.7464c4.5256-7.2145,6.0802-7.7666,13.4843-7.7666h50.6373c7.5399,0,9.48,1.3059,13.4987,7.7934l26.2343,43.4116c3.8162,6.0758,3.8868,8.7377-.2122,15.5878ZM162.2935,62.9806l-32.1653-53.5232c-3.3669-5.8331-9.6427-9.4574-16.3787-9.4574h-63.2298c-6.7349,0-13.0107,3.6233-16.3797,9.4574L2.5256,62.9806c-3.367,5.832-3.368,13.0788,0,18.9127l28.2883,46.6271c.6972,1.1489,2.2475,1.4194,3.2927.5745l3.7953-3.0682c1.1111-.8982,1.3866-2.4798.6446-3.7008l-27.5376-45.3298c-1.6238-2.8129-1.6238-6.3066-.001-9.1185L42.6223,14.3554c1.6247-2.813,4.6509-4.5592,7.8974-4.5592h62.0707c3.8633,0,7.7265,2.2257,9.5084,5.3119l31.5381,52.7697c1.3222,2.2578,1.3075,6.6256-.2811,9.1185l-28.17,45.4216c-.7443,1.206-.4906,2.7755.5957,3.6857l3.7147,3.1125c1.0344.8667,2.5963.6159,3.3066-.5316,5.7475-9.2843,28.4382-45.0842,29.4556-46.7325.0269-.0435.0491-.081.0745-.1254,3.3285-5.8225,3.3147-13.0362-.0395-18.846ZM112.1395,111.86l20.5967-33.2474c2.7793-4.1012,3.025-8.0552.2349-11.8367l-20.5471-34.3182c-2.9432-4.9527-4.5764-6.0687-10.3635-6.0687h-39.7693c-5.3322,0-6.9432.328-10.3665,6.0758,0,0-20.5405,34.9936-20.5608,35.026-2.8827,4.6124-3.2416,5.9807-.0064,11.9361.0267.0491.0547.1004.0842.1478l20.1842,32.4066c.6495,1.0426,2.0652,1.2811,3.0205.5089l1.7346-1.4022c.8033-.6494.996-1.796.4491-2.6723,0,0-19.9878-32.0644-20.0374-32.1498-1.4254-2.4578-.8244-4.2267.0669-5.7315l20.2119-34.4388c1.2871-2.326,3.2387-3.4297,5.7357-3.4297h38.821c2.012,0,4.3815,1.1694,5.6413,3.3912l19.8992,33.2572c1.0266,1.8081,1.1054,4.5671.1082,6.1993l-20.1049,32.963c-.5378.8645-.3575,1.993.4229,2.647l1.4959,1.2233c.9528.7984,2.3917.5687,3.0486-.4866ZM62.8749,105.8346l.6085-.4919c.8649-.6992.9872-2.0168.3925-2.9565l-16.6255-26.6169c-.7804-1.3868-.7804-3.1105.0072-4.5098l15.887-27.2159c.7619-1.357,2.1736-2.1993,3.682-2.1993h30.8556c1.5086,0,2.9201.8423,3.681,2.1974l16.3854,27.3383c.7804,1.387.1456,2.5276-.6339,3.9144l-17.0732,27.0234c-.5859.9273-.3957,2.1449.445,2.8494l.6115.5124c1.0173.8524,2.5528.6116,3.2604-.5112l17.1937-27.2856c.0283-.045.0565-.0935.0816-.1403,2.0266-3.7809,2.6406-5.2507.597-8.8809l-16.3853-27.3383c-2.3115-3.5931-3.6542-4.8188-8.1632-4.8188h-30.8556c-4.1894,0-5.9065.943-8.1692,4.8311,0,0-15.9067,27.2396-15.9361,27.2865-2.1306,3.398-2.5072,4.9471.05,9.4681l16.7927,26.9294c.7,1.1082,2.2915,1.4392,3.3108.6151Z"
AI_TRI = "M126.5512,139.2276l-89.9464.0002c-2.0988-.0002-3.0319-2.6383-1.3999-3.9577l45.778-37.0079c.8273-.6697,2.013-.6591,2.8285.0243l44.1698,37.0089c1.5933,1.3352.6489,3.9322-1.43,3.9323Z"
MACHINE_ICON = "M22.6941 14.5245V9.75192C22.6941 9.44133 22.5131 9.16181 22.2417 9.03758L20.9049 8.44747V5.77646C20.9049 5.35199 20.5631 5 20.151 5H13.5874C13.2054 5 12.8838 5.28988 12.8436 5.68328L12.5018 8.61311H10.8936V7.4329C10.8936 7.22584 10.8132 7.02914 10.6724 6.87385L9.86833 6.06633C9.56678 5.7661 9.09436 5.7661 8.80287 6.06633C8.51138 6.37692 8.51138 6.8635 8.80287 7.16373L9.3758 7.74348V8.60276H8.21988C7.80777 8.60276 7.46602 8.95475 7.46602 9.37922V12.1538L6.95339 11.7189L4.44051 8.84087C4.24954 8.62347 3.95804 8.53029 3.6766 8.61311C3.39516 8.69594 3.19413 8.9237 3.14387 9.22393L2.02815 15.477L1.08331 17.3715C0.942589 17.6511 0.982795 17.9824 1.18382 18.2205C1.32455 18.3965 1.54568 18.5 1.75676 18.5C1.82712 18.5 1.90753 18.4896 1.97789 18.4689L5.9985 17.1852H7.30519C7.58664 17.9824 8.26009 18.5 9.04411 18.5H20.6435C21.5482 18.5 22.3322 17.9513 22.7443 17.0403C23.1062 16.2224 23.076 15.2906 22.7041 14.5245H22.6941ZM5.20443 15.8186L3.23433 16.4398L3.41526 16.0775C3.44541 16.0153 3.47557 15.9429 3.48562 15.86L4.34 11.0564L5.63664 12.5472L5.20443 15.8083V15.8186ZM8.97374 10.1764H13.1652C13.5472 10.1764 13.8688 9.8865 13.909 9.4931L14.2508 6.56327H19.3972V8.95475C19.3972 9.26534 19.5781 9.54486 19.8495 9.6691L21.1863 10.2592V12.5989L19.9198 11.0978C18.9448 9.93827 17.4371 9.61733 16.1606 10.2903L8.96369 14.1001V10.1867L8.97374 10.1764ZM6.9936 13.7895L7.43586 14.1622C7.43586 14.1622 7.45597 14.1622 7.45597 14.1725V15.1871C7.45597 15.1871 7.45597 15.2078 7.45597 15.2182C7.37555 15.3424 7.31525 15.4873 7.27504 15.6323H6.74231L6.98355 13.7791L6.9936 13.7895ZM21.4678 15.9739C21.4477 16.1292 21.4175 16.2742 21.3673 16.4087C21.2969 16.5744 21.0758 16.9678 20.6435 16.9678H9.04411C8.81292 16.9678 8.72246 16.6986 8.6923 16.5847C8.64204 16.388 8.6722 16.1396 8.80287 15.9843C8.84308 15.9429 8.87323 15.9015 8.92349 15.8704L11.6474 14.4314L16.8441 11.6775C17.0652 11.5636 17.3064 11.5015 17.5376 11.5015C17.9899 11.5015 18.4322 11.7189 18.774 12.1227L20.7139 14.4314L21.1964 15.0008C21.4376 15.2906 21.4979 15.653 21.4678 15.9843V15.9739Z"

LANGS = ["United States English","العربية","বাংলা","Български","简体中文","繁體中文","Čeština","Dansk","Nederlands","Suomi","Français","Deutsch","Ελληνικά","עברית","हिंदी","Bahasa Indonesia","Italiano","日本語","ಕನ್ನಡ","한국어","Norsk","Polski","Português Do Brasil","Română","Русский","Español (Latino)","Svenska","தமிழ்","తెలుగు","ไทย","Türkçe","Українська Мова","Tiếng Việt"]
lang_items = "\n".join('<a href="#" onclick="return false;">' + l + '</a>' for l in LANGS)

CAT_APPS = ["Caterpillar HOME","Buy Parts","Explore Products","Find Used Products","Rent Products","Shop Machines","Buy Merchandise"]
HELP_ICON = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true" style="flex-shrink:0;"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>'
cat_app_links = ['<a href="#" onclick="return false;" class="cat-app-home">' + CAT_APPS[0] + '</a>']
cat_app_links += ['<a href="#" onclick="return false;">' + i + '</a>' for i in CAT_APPS[1:]]
cat_app_links += ['<a href="#" onclick="return false;" class="cat-app-help" style="display:flex;align-items:center;gap:8px;border-top:1px solid #eee;color:#555;">' + HELP_ICON + 'Help Center</a>']
cat_app_html = "\n".join(cat_app_links)

CATS = [
    "Brakes &amp; Components",
    "Clutches &amp; Sprockets",
    "Differentials",
    "Drive Chains &amp; Sprockets",
    "Drivetrain Repair &amp; Service Kits",
    "Final Drive",
    "Gears",
    "Other Drivetrain Components",
]

# Spec filters: (label, [(us_label, metric_label), ...] or None for checkbox-only)
SPECS = [
    ("Diameter", [
        ('Under 4"', "Under 102mm"),
        ('4" – 10"', "102 – 254mm"),
        ('10" – 20"', "254 – 508mm"),
        ('20"+', "508mm+"),
    ]),
    ("Thickness", [
        ('Under 0.1"', "Under 2.5mm"),
        ('0.1" – 0.5"', "2.5 – 12.7mm"),
        ('0.5"+', "12.7mm+"),
    ]),
    ("Material", ["Carbon Steel", "Alloy Steel", "Silicone Rubber", "Bronze"]),
    ("Drive Type", ["Universal Joint", "Slip Joint", "Planetary Gear", "Duo Cone Seal"]),
]

# Products: (img_key, part_num, name, description, fit)
# fit = "fits" (green Fits 320 Excavator) or "unverified" (orange Verify fit)
# Order: factory fit + image → factory fit + no image → not fit + image → not fit + no image
PRODUCTS = [
    # --- Factory fit + real image ---
    ("p01","595-3692","Engine Cylinder Piston","Cat® Engine Cylinder Piston converts combustion energy into mechanical motion, driving the crankshaft to power the equipment.","fits"),
    ("p03","226-2826","874.5mm Outer Diameter Brake Friction Disc","Cat® Friction Disc (Brake).","fits"),
    ("p04","2A-6946","Link Group-Steering","Cat® Steering Link Group.","fits"),
    ("p05","8R-7036","Universal Joint Bearing Spider","Cat® part 8R-7036 universal joint bearing spider transmits rotational motion between two intersecting shafts.","fits"),
    ("p06","106-0933","Universal Joint Assembly","Cat® Universal Joint Assembly (10C).","fits"),
    ("p07","150-8355","Universal Joint Assembly","Cat® Universal Joint Assembly (14.5C Interlock).","fits"),
    ("p08","436-2594","101.62mm Inner Diameter Roller Bearing","Shop Cat® cylindrical roller bearing for off-highway truck final drive. 436-2594 is for low to medium-speed and high-load applications.","fits"),
    ("p10","0R-9043","Wheel Arrangement","Cat Reman wheel arrangement. Best-built Cat® parts with full warranty when and where you need them, at a fraction of the price.","fits"),
    ("p12","365-4922","538.62mm Outer Diameter Duo Cone Seal","Cat® parts duo cone seal maintains a tight seal and avoids oil leakage. Shop this part for machines compatible with 365-4922.","fits"),
    ("p15","303-2504","Joint Group-Slip","Cat® Joint Group-Slip for drivetrain assemblies requiring a precision slip joint connection.","fits"),
    ("p16","163-9366","2.413mm Thick Outer Plate","Cat® 2.413mm Thick Outer Plate for Service and Parking Brake. Carbon steel construction for durability.","fits"),
    ("p17","363-1924","Joint Group-Slip","Cat® Slip Joint Group (15.5C) for smooth drivetrain power transmission.","fits"),
    # --- Factory fit + no image (default CAT logo) ---
    ("p14","8W-0212","2.413mm Thick Outer Plate","Cat® 2.413mm Thick Outer Plate for Service and Parking Brake.","fits"),
    # --- Not factory fit + real image ---
    ("p09","384-4562","Bearing Assembly","Find premium bearing assembly and more with Cat. Reliable heavy-duty components for your needs.","unverified"),
    ("p11","290-4140","190.27mm Transmission Steel Planet Gear","Cat® Planet Gear (Final Drive).","unverified"),
    ("p13","255-0902","Drive Shaft Spider Bearing","Cat® 255-0902 drive shaft spider bearing supports and aligns the bearings for smooth power transmission.","unverified"),
    ("p18","563-8599","Duo Seal Group","Shop Cat® duo cone seal group to protect against particle intrusion for machines compatible with 563-8599.","unverified"),
    ("p19","118-6606","170mm ID Fan Type Outer Plate","Shop Cat® final drive plate brake parts for machines compatible with Cat part 118-6606.","unverified"),
    ("p20","179-0745","Final Drive Spindle","Cat® Final Drive Spindle is responsible for transmitting power from the differential to the wheels.","unverified"),
    # --- Not factory fit + no image ---
    ("p02","8X-9620","295mm Long Ball Stud","Shop Cat® 295mm long ball stud used in steering cylinder rod end mounting and steering tie rod linkage for machines compatible with 8X-9620.","unverified"),
]

INFO_SVG = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#AAA" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>'

CHAR_LIMIT = 100

def prod_card(img_key, num, name, desc, fit='fits'):
    img_src = PI[img_key]
    if len(desc) > CHAR_LIMIT:
        cutoff = desc[:CHAR_LIMIT].rsplit(' ', 1)[0]
        desc_html = cutoff + '... <a href="#" class="more-link" onclick="return false;">More</a>'
    else:
        desc_html = desc
    if fit == 'fits':
        badge = (
            '<div class="fit-badge fits" data-fit="badge">'
            '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>'
            ' Fits 320 Excavator'
            '</div>'
        )
    else:
        badge = (
            '<div class="fit-badge unverified" data-fit="badge">'
            '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>'
            ' Verify fit'
            '</div>'
        )
    return (
        '<div class="prod-card">'
        '<div class="prod-img">'
        '<img src="' + img_src + '" alt="' + name + '" width="140" height="140">'
        '</div>'
        '<div class="prod-info">'
        '<span class="prod-num">' + num + '</span>'
        '<p class="prod-name">' + name + '</p>'
        '<p class="prod-desc">' + desc_html + '</p>'
        '<div class="prod-bottom">'
        + badge +
        '<button class="add-cart-btn" type="button" onclick="return false;">Add to Cart</button>'
        '</div>'
        '</div>'
        '</div>'
    )

parts = []
parts.append('<title>CAT Parts — Drivetrain</title>')
parts.append('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Roboto+Mono:wght@500&display=swap">')

parts.append("""<style>
:root{color-scheme:light;--yellow:#FFCD11;--bg:#fff;--card-bg:#F7F7F7;--border:#E0E0E0;--text:#111;--muted:#666;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html,body{height:100%;}
body{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:var(--bg);color:var(--text);font-size:14px;line-height:1.5;display:flex;flex-direction:column;}
main{flex:1;}
a{color:inherit;text-decoration:none;}
/* HEADER */
.site-header{background:#000;position:sticky;top:env(safe-area-inset-top,0px);z-index:100;}
.hdr-inner{max-width:1280px;margin:0 auto;padding:0 16px;height:54px;display:flex;align-items:center;gap:10px;}
.hdr-left{display:flex;align-items:center;gap:8px;flex-shrink:0;}
.hdr-center{flex:1;display:flex;justify-content:center;min-width:0;}
.hdr-right{display:flex;align-items:center;gap:2px;flex-shrink:0;}
.cat-wrap{position:relative;}
.cat-logo{text-decoration:none;display:flex;align-items:center;gap:4px;line-height:0;cursor:pointer;}
.cat-logo img{height:32px;width:auto;display:block;}
@keyframes logoSpin{from{transform:rotate(0deg);}to{transform:rotate(1080deg);}}
.cat-app-menu{display:none;position:absolute;top:calc(100% + 8px);left:0;background:#fff;border:1px solid #ddd;min-width:230px;box-shadow:0 4px 20px rgba(0,0,0,.16);z-index:300;}
.cat-app-menu.open{display:block;}
.cat-app-menu a{display:block;padding:12px 16px;font-size:13px;color:#333;text-decoration:none;border-bottom:1px solid #f0f0f0;transition:background .1s;}
.cat-app-menu a:last-child{border-bottom:none;}
.cat-app-menu a:hover{background:#f5f5f5;}
.cat-app-menu a.cat-app-home{font-weight:600;color:#111;}
.store-btn{background:none;border:none;color:#fff;cursor:pointer;display:flex;align-items:center;gap:5px;font-size:12px;font-family:inherit;padding:6px 10px;white-space:nowrap;border-radius:2px;transition:background .12s;}
.store-btn:hover{background:rgba(255,255,255,.09);}
/* Search bar — same pill design as Level 1 */
.search-area{width:100%;max-width:520px;display:flex;background:#fff;overflow:hidden;border-radius:22px;}
.add-equip-btn{display:flex;align-items:center;gap:5px;background:var(--yellow);border:none;border-right:1px solid #D0D0D0;padding:0 12px;cursor:pointer;white-space:nowrap;flex-shrink:0;font-size:12px;color:#111;font-family:inherit;font-weight:500;transition:background .12s;}
.add-equip-btn:hover{background:#e6b800;}
.search-area input{flex:1;height:36px;padding:0 10px;border:none;font-size:13px;font-family:inherit;background:#fff;color:#111;outline:none;min-width:0;-webkit-appearance:none;}
.search-area input::placeholder{color:#999;}
.search-submit{width:42px;height:36px;background:#fff;border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.search-submit:hover{background:#f5f5f5;}
.hbtn{background:none;border:none;color:#fff;cursor:pointer;display:flex;align-items:center;gap:5px;font-size:12px;font-family:inherit;padding:8px 9px;white-space:nowrap;border-radius:2px;transition:background .12s;flex-shrink:0;}
.hbtn:hover{background:rgba(255,255,255,.09);}
.lang-wrap{position:relative;}
.lang-menu{display:none;position:absolute;top:calc(100% + 6px);right:0;background:#fff;border:1px solid #ddd;box-shadow:0 4px 16px rgba(0,0,0,.15);z-index:300;width:480px;padding:14px;}
.lang-menu.open{display:block;}
.lang-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2px 8px;}
.lang-grid a{display:block;padding:7px 8px;font-size:12px;color:#111;text-decoration:none;border-radius:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.lang-grid a:first-child{font-weight:700;}
.lang-grid a:hover{background:#f5f5f5;}
.acct-wrap{position:relative;}
.acct-menu{display:none;position:absolute;top:calc(100% + 6px);right:0;background:#fff;border:1px solid #ddd;min-width:210px;box-shadow:0 4px 16px rgba(0,0,0,.13);z-index:200;}
.acct-menu.open{display:block;}
.acct-menu a{display:block;padding:11px 16px;font-size:13px;color:#111;text-decoration:none;border-bottom:1px solid #f0f0f0;}
.acct-menu a.acct-signout{border-bottom:none;color:#888;font-size:12px;border-top:1px solid #eee;padding-top:10px;}
.acct-menu a:hover{background:#f8f8f8;}
/* LAYOUT */
.wrap{max-width:1280px;margin:0 auto;padding:0 20px;}
.breadcrumb{padding:14px 0 0;font-size:12px;color:var(--muted);display:flex;gap:6px;align-items:center;}
.breadcrumb a{color:var(--muted);}
.breadcrumb a:hover{text-decoration:underline;}
.page-title{padding:12px 0 18px;}
.page-title h1{font-size:24px;font-weight:700;display:inline-block;padding-bottom:7px;border-bottom:3px solid var(--yellow);}
.page-layout{display:flex;gap:28px;align-items:flex-start;padding-bottom:48px;}
/* SIDEBAR */
.sidebar{width:220px;flex-shrink:0;position:sticky;top:70px;}
.sidebar-section{margin-bottom:24px;}
.sidebar-section-title{font-size:15px;font-weight:700;color:#111;padding:0 0 10px;border-bottom:2px solid var(--border);margin-bottom:8px;letter-spacing:-.01em;}
.sidebar-links{list-style:none;}
.sidebar-links li a{display:block;padding:7px 0;font-size:13px;color:var(--text);border-bottom:1px solid #F5F5F5;transition:color .1s;}
.sidebar-links li a:hover{color:#000;text-decoration:underline;}
/* Unit toggle pill */
.unit-toggle{display:flex;background:#E8E8E8;border-radius:20px;padding:2px;margin-bottom:12px;}
.unit-btn{flex:1;border:none;background:none;padding:4px 10px;border-radius:18px;font-size:12px;font-family:inherit;cursor:pointer;color:#666;font-weight:500;transition:background .12s,color .12s;}
.unit-btn.active{background:#fff;color:#111;font-weight:600;box-shadow:0 1px 3px rgba(0,0,0,.12);}
/* Spec accordion */
.spec-filter{border-bottom:1px solid var(--border);}
.spec-filter summary{padding:9px 0;font-size:13px;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;user-select:none;}
.spec-filter summary::-webkit-details-marker{display:none;}
.spec-filter summary::after{content:"";width:8px;height:8px;border-right:2px solid #888;border-bottom:2px solid #888;transform:rotate(45deg);flex-shrink:0;margin-top:-4px;}
.spec-filter[open] summary::after{transform:rotate(-135deg);margin-top:2px;}
.spec-options{padding:4px 0 10px;}
.spec-option{display:flex;align-items:center;gap:7px;padding:4px 0;font-size:12px;color:var(--text);}
.spec-option input[type="checkbox"]{width:14px;height:14px;cursor:pointer;accent-color:#000;flex-shrink:0;}
.spec-option label{cursor:pointer;line-height:1.3;}
/* Equipment context button in search bar (L2/L3) */
.equip-context-btn{display:flex;align-items:center;gap:6px;background:var(--yellow);border:none;border-right:1px solid #D0D0D0;padding:0 14px;cursor:pointer;white-space:nowrap;flex-shrink:0;font-size:13px;font-weight:700;color:#111;font-family:inherit;height:36px;transition:background .12s;}
.equip-context-btn:hover{background:#e6b800;}
/* MAIN */
.main-content{flex:1;min-width:0;}
.sort-bar{display:flex;justify-content:flex-end;align-items:center;gap:10px;margin-bottom:16px;}
.sort-label{font-size:13px;color:var(--muted);}
.sort-select{font-size:13px;font-family:inherit;padding:5px 28px 5px 10px;border:1px solid var(--border);border-radius:4px;background:#fff;color:var(--text);cursor:default;-webkit-appearance:none;appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6' viewBox='0 0 10 6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%23666'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 8px center;}
/* PRODUCT GRID — CSS Grid stretch gives uniform row heights */
.prod-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;}
/* EQUIPMENT CARD */
.equip-card{background:#fff;border:2px solid var(--yellow);border-radius:10px;padding:18px;display:flex;flex-direction:column;}
.equip-mach-img{width:100%;height:100px;object-fit:contain;border-radius:6px;background:#F7F7F7;flex-shrink:0;margin-bottom:8px;}
.equip-card-title{font-size:13px;font-weight:700;display:flex;align-items:center;gap:7px;margin-bottom:12px;}
/* Confirmed state — Change button pushed to bottom matching Add to Cart row */
.equip-confirmed{display:flex;flex-direction:column;align-items:center;flex:1;text-align:center;gap:6px;}
.equip-conf-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:#888;}
.equip-conf-model{font-size:15px;font-weight:700;color:var(--text);}
.equip-conf-serial{font-size:11px;color:var(--muted);}
.equip-change-btn{background:none;border:1px solid #CCC;border-radius:22px;padding:8px 14px;font-size:12px;font-weight:600;font-family:inherit;cursor:pointer;color:var(--muted);margin-top:auto;width:100%;transition:border-color .12s,color .12s;}
.equip-change-btn:hover{border-color:#999;color:#333;}
/* Edit state */
.equip-edit{display:none;flex-direction:column;flex:1;gap:9px;}
.equip-input-wrap{position:relative;}
.equip-input-wrap input{width:100%;padding:8px 30px 8px 10px;border:1px solid #D0D0D0;border-radius:6px;font-size:12px;font-family:inherit;color:var(--text);background:#fff;outline:none;transition:border-color .15s;}
.equip-input-wrap input::placeholder{color:#AAA;}
.equip-input-wrap input:focus{border-color:#FFCD11;box-shadow:0 0 0 2px rgba(255,205,17,.2);}
.equip-input-info{position:absolute;right:8px;top:50%;transform:translateY(-50%);pointer-events:none;}
.equip-submit-btn{width:100%;background:var(--yellow);border:none;padding:8px;border-radius:6px;font-size:12px;font-weight:600;font-family:inherit;cursor:pointer;transition:background .12s;}
.equip-submit-btn:hover{background:#e6b800;}
.equip-cancel-btn{width:100%;background:none;border:1px solid #D0D0D0;padding:7px;border-radius:6px;font-size:11px;font-family:inherit;cursor:pointer;color:var(--muted);transition:border-color .12s;}
.equip-cancel-btn:hover{border-color:#999;color:#333;}
/* PRODUCT CARDS */
.prod-card{background:var(--card-bg);border:1px solid var(--border);border-radius:10px;overflow:hidden;display:flex;flex-direction:column;transition:border-color .15s;}
.prod-card:hover{border-color:#bbb;}
.prod-img{width:100%;height:160px;background:#fff;display:flex;align-items:center;justify-content:center;overflow:hidden;flex-shrink:0;}
.prod-img img{width:140px;height:140px;object-fit:contain;mix-blend-mode:multiply;}
.prod-info{padding:10px 12px 12px;display:flex;flex-direction:column;flex:1;}
.prod-num{font-family:"Roboto Mono",monospace;font-size:11px;font-weight:500;color:#555;letter-spacing:.02em;margin-bottom:4px;}
.prod-name{font-size:13px;font-weight:600;line-height:1.3;color:var(--text);margin-bottom:4px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;}
.prod-desc{font-size:11px;color:var(--muted);line-height:1.45;flex:1;margin-bottom:10px;}
.more-link{color:#555;font-weight:600;font-size:11px;white-space:nowrap;}
.more-link:hover{color:#000;text-decoration:underline;}
.prod-bottom{margin-top:auto;display:flex;flex-direction:column;gap:7px;}
.fit-badge{display:inline-flex;align-items:center;gap:5px;padding:4px 10px;border-radius:20px;font-size:11px;font-weight:600;width:fit-content;transition:background .2s,color .2s;}
.fit-badge.unverified{background:#FFF3E0;color:#E65100;}
.fit-badge.fits{background:#E8F5E9;color:#2E7D32;}
.add-cart-btn{width:100%;background:var(--yellow);border:none;padding:8px;border-radius:22px;font-size:12px;font-weight:600;font-family:inherit;cursor:pointer;transition:background .12s;}
.add-cart-btn:hover{background:#e6b800;}
/* PAGINATION */
.pagination{display:flex;align-items:center;justify-content:center;gap:14px;padding:28px 0 8px;margin-top:12px;}
.pg-btn{padding:8px 20px;border:1px solid var(--border);border-radius:22px;background:#fff;font-size:13px;font-family:inherit;cursor:pointer;color:var(--text);transition:background .12s,border-color .12s;}
.pg-btn:hover:not(:disabled){background:#f0f0f0;border-color:#bbb;}
.pg-btn:disabled{color:#bbb;cursor:default;}
.pg-info{font-size:13px;color:var(--muted);}
/* FOOTER */
.site-footer{background:var(--yellow);padding:26px 16px 16px;text-align:center;}
.social-row{display:flex;justify-content:center;align-items:center;gap:12px;margin-bottom:18px;}
.soc-icon{width:34px;height:34px;border-radius:50%;background:#000;display:flex;align-items:center;justify-content:center;color:var(--yellow);text-decoration:none;flex-shrink:0;transition:opacity .13s;}
.soc-icon:hover{opacity:.78;}
.footer-legal{font-size:11px;color:#333;line-height:2;margin-bottom:7px;}
.footer-legal .pipe{margin:0 5px;color:#666;}
.footer-copy{font-size:11px;color:#333;font-weight:600;}
/* AI BTN */
.ai-btn{position:fixed;bottom:26px;right:26px;width:54px;height:54px;border-radius:50%;background:#000;border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 18px rgba(0,0,0,.4);z-index:999;padding:10px;transition:transform .15s;}
.ai-btn:hover{transform:scale(1.06);}
.ai-icon{position:relative;width:100%;height:100%;}
.ai-ring{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;transform-origin:center center;will-change:transform;z-index:1;}
.ai-tri-fixed{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;z-index:2;pointer-events:none;}
.ai-ring svg,.ai-tri-fixed svg{width:100%;height:100%;}
@keyframes ringLoad{from{transform:rotate(0deg);}to{transform:rotate(1080deg);}}
@keyframes ringHover{from{transform:rotate(0deg);}to{transform:rotate(360deg);}}
@media(prefers-reduced-motion:reduce){.ai-ring,.cat-logo img{animation:none!important;}}
@media(max-width:900px){.sidebar{display:none;}.prod-grid{grid-template-columns:repeat(2,1fr);}}
@media(max-width:600px){.prod-grid{grid-template-columns:1fr;}.lang-menu{width:280px;}}
</style>""")

# HEADER — search bar includes equipment chip (320 Excavator, with "Change" link)
parts.append("""<header class="site-header">
  <div class="hdr-inner">
    <div class="hdr-left">
      <div class="cat-wrap">
        <a href="javascript:history.back()" class="cat-logo" aria-label="Cat Applications">
          <img src="{logo}" alt="Caterpillar" width="64" height="35">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" aria-hidden="true" style="margin-left:4px;flex-shrink:0;"><polyline points="6 9 12 15 18 9"/></svg>
        </a>
        <div class="cat-app-menu">{apps}</div>
      </div>
      <button class="store-btn" type="button">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle cx="12" cy="9" r="2.5"/></svg>
        <span>Select Store</span>
      </button>
    </div>
    <div class="hdr-center">
      <div class="search-area" role="search">
        <button class="equip-context-btn" type="button" id="hdrEquipBtn" aria-label="Equipment: 320 Excavator" onclick="document.getElementById('equipCard').scrollIntoView({behavior:'smooth',block:'center'});return false;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="{machine}"/></svg>
          <span id="hdrEquipNum">320</span>
        </button>
        <input type="search" placeholder="Search for part number or name" aria-label="Search parts">
        <button class="search-submit" type="button" aria-label="Search">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><line x1="16.5" y1="16.5" x2="22" y2="22"/></svg>
        </button>
      </div>
    </div>
    <div class="hdr-right">
      <div class="lang-wrap">
        <button class="hbtn" type="button" aria-label="Select language">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          <span>EN</span>
          <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="lang-menu"><div class="lang-grid">{langs}</div></div>
      </div>
      <div class="acct-wrap">
        <button class="hbtn" type="button">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          <span>Account</span>
          <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="acct-menu">
          <a href="#" onclick="return false;">Manage My Equipment</a>
          <a href="#" onclick="return false;">Order History</a>
          <a href="#" onclick="return false;">View Finance Solutions</a>
          <a href="#" onclick="return false;">Cat&reg; Rewards</a>
          <a href="#" class="acct-signout" onclick="return false;">Sign Out</a>
        </div>
      </div>
      <button class="hbtn" type="button" aria-label="Cart">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
      </button>
    </div>
  </div>
</header>""".replace("{logo}", LOGO).replace("{apps}", cat_app_html).replace("{langs}", lang_items).replace("{machine}", MACHINE_ICON))

parts.append('<main>')
parts.append('<div class="wrap">')
# Breadcrumb — All Categories links back to Level 1
parts.append('<nav class="breadcrumb" aria-label="Breadcrumb"><a href="https://claude.ai/artifact/JkHPcq3EZBPeG4jNBuitvd">Home</a><span>/</span><a href="https://claude.ai/artifact/JkHPcq3EZBPeG4jNBuitvd">All Categories</a><span>/</span><span aria-current="page">Drivetrain</span></nav>')
parts.append('<div class="page-title"><h1>Drivetrain</h1></div>')
parts.append('<div class="page-layout">')

# SIDEBAR
cat_links = "\n".join(
    '<li><a href="#" onclick="return false;">' + c + '</a></li>'
    for c in CATS
)

def spec_filter_html(label, options):
    if options is None:
        return '<details class="spec-filter"><summary>' + label + '</summary></details>'
    inner = '<div class="spec-options">'
    for i, opt in enumerate(options):
        uid = 'sf_' + label.replace(' ','_').lower() + '_' + str(i)
        if isinstance(opt, tuple):
            # Has US/Metric variants
            us_v, met_v = opt
            val_html = '<span class="val-us">' + us_v + '</span><span class="val-metric" hidden>' + met_v + '</span>'
        else:
            val_html = opt
        inner += '<div class="spec-option"><input type="checkbox" id="' + uid + '"><label for="' + uid + '">' + val_html + '</label></div>'
    inner += '</div>'
    return '<details class="spec-filter" open><summary>' + label + '</summary>' + inner + '</details>'

spec_html = "\n".join(spec_filter_html(label, opts) for label, opts in SPECS)

parts.append("""<aside class="sidebar">
  <div class="sidebar-section">
    <div class="sidebar-section-title">Categories</div>
    <ul class="sidebar-links">""" + cat_links + """</ul>
  </div>
  <div class="sidebar-section">
    <div class="sidebar-section-title">Specifications</div>
    <div class="unit-toggle" role="group" aria-label="Unit system">
      <button class="unit-btn active" id="unitUS" type="button" onclick="setUnit('us')">US</button>
      <button class="unit-btn" id="unitMetric" type="button" onclick="setUnit('metric')">Metric</button>
    </div>""" + spec_html + """
  </div>
</aside>""")

parts.append('<div class="main-content">')
parts.append("""<div class="sort-bar">
  <span class="sort-label">Sort by</span>
  <select class="sort-select" disabled aria-label="Sort by">
    <option>Relevance</option>
    <option>Price: Low to High</option>
    <option>Price: High to Low</option>
    <option>Part Number</option>
  </select>
</div>""")

parts.append('<div class="prod-grid">')

# Equipment card — starts in CONFIRMED state (equipment pre-selected from URL params)
parts.append("""<div class="equip-card" id="equipCard">
  <div class="equip-card-title">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="{machine}"/></svg>
    My Equipment
  </div>

  <!-- Confirmed state (default) -->
  <div class="equip-confirmed" id="equipConfirmed">
    <img class="equip-mach-img" src="{mach}" alt="320 Excavator">
    <div class="equip-conf-label">Shopping for</div>
    <div class="equip-conf-model" id="confirmedModel">320 Excavator</div>
    <div class="equip-conf-serial" id="confirmedSerial">ZBN60173</div>
    <button class="equip-change-btn" type="button" id="equipChange">Change equipment</button>
  </div>

  <!-- Edit state (shown when changing equipment) -->
  <div class="equip-edit" id="equipEdit">
    <div class="equip-input-wrap">
      <input type="text" id="serialNum" placeholder="Serial number, e.g. ZBN60173" autocomplete="off">
      <span class="equip-input-info">{info}</span>
    </div>
    <div class="equip-input-wrap">
      <input type="text" id="modelName" placeholder="Model name, e.g. 320 Excavator" autocomplete="off">
      <span class="equip-input-info">{info}</span>
    </div>
    <button class="equip-submit-btn" type="button" id="equipSubmit">Find Compatible Parts</button>
    <button class="equip-cancel-btn" type="button" id="equipCancel">Cancel</button>
  </div>
</div>""".replace("{machine}", MACHINE_ICON).replace("{mach}", MACH).replace("{info}", INFO_SVG))

# 20 product cards
for img_key, num, name, desc, fit in PRODUCTS:
    parts.append(prod_card(img_key, num, name, desc, fit))

parts.append('</div>') # prod-grid

# Pagination
parts.append("""<div class="pagination" aria-label="Page navigation">
  <button class="pg-btn pg-prev" type="button" disabled aria-label="Previous page">&larr; Previous</button>
  <span class="pg-info">Page 1 of 5 &nbsp;&middot;&nbsp; 84 results</span>
  <button class="pg-btn pg-next" type="button" onclick="return false;" aria-label="Next page">Next &rarr;</button>
</div>""")

parts.append('</div>') # main-content
parts.append('</div>') # page-layout
parts.append('</div>') # wrap
parts.append('</main>')

parts.append("""<footer class="site-footer">
  <div class="social-row">
    <a href="#" class="soc-icon" aria-label="Facebook" onclick="return false;"><svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
    <a href="#" class="soc-icon" aria-label="X" onclick="return false;"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>
    <a href="#" class="soc-icon" aria-label="LinkedIn" onclick="return false;"><svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg></a>
    <a href="#" class="soc-icon" aria-label="YouTube" onclick="return false;"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.95-1.96C18.88 4 12 4 12 4s-6.88 0-8.59.46a2.78 2.78 0 0 0-1.95 1.96A29 29 0 0 0 1 12a29 29 0 0 0 .46 5.58A2.78 2.78 0 0 0 3.41 19.6C5.12 20 12 20 12 20s6.88 0 8.59-.46a2.78 2.78 0 0 0 1.95-1.95A29 29 0 0 0 23 12a29 29 0 0 0-.46-5.58z"/><polygon points="9.75 15.02 15.5 12 9.75 8.98 9.75 15.02" fill="#FFCD11"/></svg></a>
    <a href="#" class="soc-icon" aria-label="Instagram" onclick="return false;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.5" fill="currentColor" stroke="none"/></svg></a>
  </div>
  <p class="footer-legal">About Cat<span class="pipe">|</span>Site Map<span class="pipe">|</span>Cookie Settings<span class="pipe">|</span>Do Not Sell or Share My Personal Information<span class="pipe">|</span>Legal Terms<span class="pipe">|</span>Privacy</p>
  <p class="footer-copy">&copy; 2026 Caterpillar. All Rights Reserved.</p>
</footer>""")

# AI BUTTON
parts.append('<button class="ai-btn" type="button" aria-label="Open AI assistant" id="aiBtn">')
parts.append('  <div class="ai-icon">')
parts.append('    <div class="ai-ring" id="aiRing" aria-hidden="true">')
parts.append('      <svg viewBox="0 0 164.8193 139.2278" xmlns="http://www.w3.org/2000/svg">')
parts.append('        <path fill="#ffffff" d="' + AI_RING + '"/>')
parts.append('      </svg>')
parts.append('    </div>')
parts.append('    <div class="ai-tri-fixed" aria-hidden="true">')
parts.append('      <svg viewBox="0 0 164.8193 139.2278" xmlns="http://www.w3.org/2000/svg">')
parts.append('        <path fill="#FFCD11" d="' + AI_TRI + '"/>')
parts.append('      </svg>')
parts.append('    </div>')
parts.append('  </div>')
parts.append('</button>')

parts.append("""<script>
(function(){
  function dropdown(wrapSel,menuSel){
    var wrap=document.querySelector(wrapSel),menu=document.querySelector(menuSel);
    if(!wrap||!menu)return;
    var t;
    function show(){clearTimeout(t);menu.classList.add('open');}
    function hide(){t=setTimeout(function(){menu.classList.remove('open');},150);}
    wrap.addEventListener('mouseenter',show);
    wrap.addEventListener('mouseleave',hide);
    menu.addEventListener('mouseenter',show);
    menu.addEventListener('mouseleave',hide);
  }
  dropdown('.cat-wrap','.cat-app-menu');
  dropdown('.lang-wrap','.lang-menu');
  dropdown('.acct-wrap','.acct-menu');

  var logo=document.querySelector('.cat-logo img');
  if(logo){
    var done=false;
    function spinLogo(){logo.style.animation='none';void logo.offsetWidth;done=false;logo.style.animation='logoSpin 1.2s linear forwards';}
    logo.addEventListener('animationend',function(){done=true;});
    logo.addEventListener('mouseenter',function(){if(done)spinLogo();});
    spinLogo();
  }

  var btn=document.getElementById('aiBtn'),ring=document.getElementById('aiRing');
  if(btn&&ring){
    var hovering=false,adone=false;
    ring.style.animation='ringLoad 1.2s linear forwards';
    ring.addEventListener('animationend',function h(){
      ring.removeEventListener('animationend',h);
      ring.style.animation='none';ring.style.transform='rotate(0deg)';adone=true;
      if(hovering)ring.style.animation='ringHover 0.8s linear infinite';
    });
    btn.addEventListener('mouseenter',function(){hovering=true;if(adone)ring.style.animation='ringHover 0.8s linear infinite';});
    btn.addEventListener('mouseleave',function(){hovering=false;if(adone){ring.style.animation='none';ring.style.transform='rotate(0deg)';}});
  }

  var equipChange=document.getElementById('equipChange');
  var equipCancel=document.getElementById('equipCancel');
  var equipSubmit=document.getElementById('equipSubmit');
  var equipConfirmed=document.getElementById('equipConfirmed');
  var equipEdit=document.getElementById('equipEdit');
  var confirmedModel=document.getElementById('confirmedModel');
  var confirmedSerial=document.getElementById('confirmedSerial');
  var serialInput=document.getElementById('serialNum');
  var modelInput=document.getElementById('modelName');
  var badges=document.querySelectorAll('[data-fit="badge"]');
  var hdrEquipNum=document.getElementById('hdrEquipNum');

  function showEdit(){
    equipConfirmed.style.display='none';
    equipEdit.style.display='flex';
  }
  function showConfirmed(model,serial){
    equipEdit.style.display='none';
    equipConfirmed.style.display='flex';
    if(model){
      confirmedModel.textContent=model;
      confirmedSerial.textContent=serial||'';
      if(hdrEquipNum)hdrEquipNum.textContent=model.split(' ')[0]||model;
      badges.forEach(function(b){
        b.classList.remove('unverified');
        b.classList.add('fits');
        b.innerHTML='<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg> Fits '+model;
      });
    }
  }

  if(equipChange)equipChange.addEventListener('click',showEdit);
  if(equipCancel)equipCancel.addEventListener('click',function(){showConfirmed(null,null);});
  if(equipSubmit)equipSubmit.addEventListener('click',function(){
    var serial=serialInput.value.trim();
    var model=modelInput.value.trim();
    if(!model&&!serial)return;
    showConfirmed(model||serial,serial);
  });
  [serialInput,modelInput].forEach(function(inp){
    if(inp)inp.addEventListener('keydown',function(e){
      if(e.key==='Enter'){
        var serial=serialInput.value.trim();
        var model=modelInput.value.trim();
        if(model||serial)showConfirmed(model||serial,serial);
      }
    });
  });
})();

function setUnit(u){
  document.querySelectorAll('.val-us').forEach(function(e){e.hidden=u!=='us';});
  document.querySelectorAll('.val-metric').forEach(function(e){e.hidden=u!=='metric';});
  var btnUS=document.getElementById('unitUS');
  var btnMet=document.getElementById('unitMetric');
  if(btnUS)btnUS.classList.toggle('active',u==='us');
  if(btnMet)btnMet.classList.toggle('active',u==='metric');
}
</script>""")

html = "\n".join(parts)
with open(OUTFILE,'w') as f:
    f.write(html)
print("Written: {}KB".format(len(html)//1024))
