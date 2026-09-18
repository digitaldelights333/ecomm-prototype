import base64, os, math

SCRATCHPAD = "/private/tmp/claude-501/-Users-kerrynguyen-Library-Application-Support-Claude-scratch-workspaces-45a82dc2-899c-4111-89db-636e9dd5611c-c755861b-73af-42ff-b9a8-6def8014fe7a-scratch-2026-09-17-3e4ab8/5d677bf4-01ce-4ae3-89ae-74814a6bca11/scratchpad"
IMGDIR = os.path.join(SCRATCHPAD, "imgs")
OUTFILE = "/Users/kerrynguyen/prototype.parts.cat/cat-parts.html"

def b64img(name, ext="webp"):
    path = os.path.join(IMGDIR, name + "." + ext)
    with open(path, "rb") as f:
        return "data:image/" + ext + ";base64," + base64.b64encode(f.read()).decode()

# ── Images ───────────────────────────────────────────────────────────────────
L1_KEYS = ["attachments","cabs","drivetrain","electrical","engine","equip_upgrades",
           "filters","ground_engaging","hardware","hoses","hydraulics",
           "structures","undercarriage","upgrade_repair","workshop"]
LOGO   = b64img("logo")
MACH   = b64img("mach")
NO_IMG = b64img("no-image")
PROD_HERO = b64img("prod_567-4399")
CAT_I  = {k: b64img(k) for k in L1_KEYS}

_REAL_IMG_PARTS = ["567-4399","148-4636","122-9608","4B-9880","174-4874","561-7005",
                   "296-6220","2D-6642","523-0574","3D-2891","333-2998","593-5616",
                   "517-4512","378-9517"]
PI = {p: b64img("prod_" + p) for p in _REAL_IMG_PARTS}

# ── SVG constants ─────────────────────────────────────────────────────────────
AI_RING = "M146.9441,80.4873s-19.4829,30.9684-24.8493,39.4806c-.728,1.1547-2.3036,1.3963-3.3499.5197l-3.2698-2.7397c-.8644-.7243-1.0606-1.9759-.4593-2.9299l23.8364-38.2222c1.2222-2.116,1.4882-5.5896.2659-7.7065l-25.2972-42.2833c-1.6225-2.6259-4.1195-4.1863-7.1818-4.1863h-49.4686c-2.4434,0-4.6662.8747-6.563,3.833l-25.3649,43.3431c-1.2068,2.0903-1.2068,4.7189.0154,6.836l23.6882,38.1261c.6002.966.3868,2.2278-.4976,2.9427l-3.2926,2.6617c-1.053.8513-2.6099.5948-3.3263-.5542-5.263-8.4418-24.1294-38.8138-24.1294-38.8138-4.392-7.3564-4.392-8.8554,0-15.5869l25.6013-43.7464c4.5256-7.2145,6.0802-7.7666,13.4843-7.7666h50.6373c7.5399,0,9.48,1.3059,13.4987,7.7934l26.2343,43.4116c3.8162,6.0758,3.8868,8.7377-.2122,15.5878ZM162.2935,62.9806l-32.1653-53.5232c-3.3669-5.8331-9.6427-9.4574-16.3787-9.4574h-63.2298c-6.7349,0-13.0107,3.6233-16.3797,9.4574L2.5256,62.9806c-3.367,5.832-3.368,13.0788,0,18.9127l28.2883,46.6271c.6972,1.1489,2.2475,1.4194,3.2927.5745l3.7953-3.0682c1.1111-.8982,1.3866-2.4798.6446-3.7008l-27.5376-45.3298c-1.6238-2.8129-1.6238-6.3066-.001-9.1185L42.6223,14.3554c1.6247-2.813,4.6509-4.5592,7.8974-4.5592h62.0707c3.8633,0,7.7265,2.2257,9.5084,5.3119l31.5381,52.7697c1.3222,2.2578,1.3075,6.6256-.2811,9.1185l-28.17,45.4216c-.7443,1.206-.4906,2.7755.5957,3.6857l3.7147,3.1125c1.0344.8667,2.5963.6159,3.3066-.5316,5.7475-9.2843,28.4382-45.0842,29.4556-46.7325.0269-.0435.0491-.081.0745-.1254,3.3285-5.8225,3.3147-13.0362-.0395-18.846ZM112.1395,111.86l20.5967-33.2474c2.7793-4.1012,3.025-8.0552.2349-11.8367l-20.5471-34.3182c-2.9432-4.9527-4.5764-6.0687-10.3635-6.0687h-39.7693c-5.3322,0-6.9432.328-10.3665,6.0758,0,0-20.5405,34.9936-20.5608,35.026-2.8827,4.6124-3.2416,5.9807-.0064,11.9361.0267.0491.0547.1004.0842.1478l20.1842,32.4066c.6495,1.0426,2.0652,1.2811,3.0205.5089l1.7346-1.4022c.8033-.6494.996-1.796.4491-2.6723,0,0-19.9878-32.0644-20.0374-32.1498-1.4254-2.4578-.8244-4.2267.0669-5.7315l20.2119-34.4388c1.2871-2.326,3.2387-3.4297,5.7357-3.4297h38.821c2.012,0,4.3815,1.1694,5.6413,3.3912l19.8992,33.2572c1.0266,1.8081,1.1054,4.5671.1082,6.1993l-20.1049,32.963c-.5378.8645-.3575,1.993.4229,2.647l1.4959,1.2233c.9528.7984,2.3917.5687,3.0486-.4866ZM62.8749,105.8346l.6085-.4919c.8649-.6992.9872-2.0168.3925-2.9565l-16.6255-26.6169c-.7804-1.3868-.7804-3.1105.0072-4.5098l15.887-27.2159c.7619-1.357,2.1736-2.1993,3.682-2.1993h30.8556c1.5086,0,2.9201.8423,3.681,2.1974l16.3854,27.3383c.7804,1.387.1456,2.5276-.6339,3.9144l-17.0732,27.0234c-.5859.9273-.3957,2.1449.445,2.8494l.6115.5124c1.0173.8524,2.5528.6116,3.2604-.5112l17.1937-27.2856c.0283-.045.0565-.0935.0816-.1403,2.0266-3.7809,2.6406-5.2507.597-8.8809l-16.3853-27.3383c-2.3115-3.5931-3.6542-4.8188-8.1632-4.8188h-30.8556c-4.1894,0-5.9065.943-8.1692,4.8311,0,0-15.9067,27.2396-15.9361,27.2865-2.1306,3.398-2.5072,4.9471.05,9.4681l16.7927,26.9294c.7,1.1082,2.2915,1.4392,3.3108.6151Z"
AI_TRI = "M126.5512,139.2276l-89.9464.0002c-2.0988-.0002-3.0319-2.6383-1.3999-3.9577l45.778-37.0079c.8273-.6697,2.013-.6591,2.8285.0243l44.1698,37.0089c1.5933,1.3352.6489,3.9322-1.43,3.9323Z"
MACHINE_ICON = "M22.6941 14.5245V9.75192C22.6941 9.44133 22.5131 9.16181 22.2417 9.03758L20.9049 8.44747V5.77646C20.9049 5.35199 20.5631 5 20.151 5H13.5874C13.2054 5 12.8838 5.28988 12.8436 5.68328L12.5018 8.61311H10.8936V7.4329C10.8936 7.22584 10.8132 7.02914 10.6724 6.87385L9.86833 6.06633C9.56678 5.7661 9.09436 5.7661 8.80287 6.06633C8.51138 6.37692 8.51138 6.8635 8.80287 7.16373L9.3758 7.74348V8.60276H8.21988C7.80777 8.60276 7.46602 8.95475 7.46602 9.37922V12.1538L6.95339 11.7189L4.44051 8.84087C4.24954 8.62347 3.95804 8.53029 3.6766 8.61311C3.39516 8.69594 3.19413 8.9237 3.14387 9.22393L2.02815 15.477L1.08331 17.3715C0.942589 17.6511 0.982795 17.9824 1.18382 18.2205C1.32455 18.3965 1.54568 18.5 1.75676 18.5C1.82712 18.5 1.90753 18.4896 1.97789 18.4689L5.9985 17.1852H7.30519C7.58664 17.9824 8.26009 18.5 9.04411 18.5H20.6435C21.5482 18.5 22.3322 17.9513 22.7443 17.0403C23.1062 16.2224 23.076 15.2906 22.7041 14.5245H22.6941ZM5.20443 15.8186L3.23433 16.4398L3.41526 16.0775C3.44541 16.0153 3.47557 15.9429 3.48562 15.86L4.34 11.0564L5.63664 12.5472L5.20443 15.8083V15.8186ZM8.97374 10.1764H13.1652C13.5472 10.1764 13.8688 9.8865 13.909 9.4931L14.2508 6.56327H19.3972V8.95475C19.3972 9.26534 19.5781 9.54486 19.8495 9.6691L21.1863 10.2592V12.5989L19.9198 11.0978C18.9448 9.93827 17.4371 9.61733 16.1606 10.2903L8.96369 14.1001V10.1867L8.97374 10.1764ZM6.9936 13.7895L7.43586 14.1622C7.43586 14.1622 7.45597 14.1622 7.45597 14.1725V15.1871C7.45597 15.1871 7.45597 15.2078 7.45597 15.2182C7.37555 15.3424 7.31525 15.4873 7.27504 15.6323H6.74231L6.98355 13.7791L6.9936 13.7895ZM21.4678 15.9739C21.4477 16.1292 21.4175 16.2742 21.3673 16.4087C21.2969 16.5744 21.0758 16.9678 20.6435 16.9678H9.04411C8.81292 16.9678 8.72246 16.6986 8.6923 16.5847C8.64204 16.388 8.6722 16.1396 8.80287 15.9843C8.84308 15.9429 8.87323 15.9015 8.92349 15.8704L11.6474 14.4314L16.8441 11.6775C17.0652 11.5636 17.3064 11.5015 17.5376 11.5015C17.9899 11.5015 18.4322 11.7189 18.774 12.1227L20.7139 14.4314L21.1964 15.0008C21.4376 15.2906 21.4979 15.653 21.4678 15.9843V15.9739Z"

FIT_CHECK_SM = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="#2E7D32"/><polyline points="20 6 9 17 4 12" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>'
FIT_CHECK_LG = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="#2E7D32"/><polyline points="20 6 9 17 4 12" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>'
REMAN_SVG    = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>'
NO_RETURN_SVG= '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/></svg>'
KIT_SVG      = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>'
REPLACED_SVG = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>'
CHEVRON_SVG  = '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#999" stroke-width="2" stroke-linecap="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>'
INFO_SVG     = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#AAA" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>'
HELP_ICON    = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true" style="flex-shrink:0;"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>'

# ── Header helpers ────────────────────────────────────────────────────────────
LANGS = ["United States English","العربية","বাংলা","Български","简体中文","繁體中文","Čeština","Dansk","Nederlands","Suomi","Français","Deutsch","Ελληνικά","עברית","हिंदी","Bahasa Indonesia","Italiano","日本語","ಕನ್ನಡ","한국어","Norsk","Polski","Português Do Brasil","Română","Русский","Español (Latino)","Svenska","தமிழ்","తెలుగు","ไทย","Türkçe","Українська Мова","Tiếng Việt"]
lang_items = "\n".join('<a href="#" onclick="return false;">' + l + '</a>' for l in LANGS)

CAT_APPS = ["Caterpillar HOME","Buy Parts","Explore Products","Find Used Products","Rent Products","Shop Machines","Buy Merchandise"]
cat_app_links  = ['<a href="#" onclick="return false;" class="cat-app-home">' + CAT_APPS[0] + '</a>']
cat_app_links += ['<a href="#" onclick="return false;">' + i + '</a>' for i in CAT_APPS[1:]]
cat_app_links += ['<a href="#" onclick="return false;" class="cat-app-help" style="display:flex;align-items:center;gap:8px;border-top:1px solid #eee;color:#555;">' + HELP_ICON + 'Help Center</a>']
cat_app_html = "\n".join(cat_app_links)

# ── L1 data ───────────────────────────────────────────────────────────────────
L1_CARDS = [
    ("attachments","Attachments"),("cabs","Cabs"),("drivetrain","Drivetrain"),
    ("electrical","Electrical &amp; Electronics"),("engine","Engine"),
    ("equip_upgrades","Equipment Upgrades"),("filters","Filters &amp; Fluids"),
    ("ground_engaging","Ground Engaging Tools"),("hardware","Hardware, Seals, &amp; Consumables"),
    ("hoses","Hoses &amp; Tubes"),("hydraulics","Hydraulics"),
    ("structures","Structures &amp; Other Systems Components"),
    ("undercarriage","Undercarriage"),("upgrade_repair","Upgrade &amp; Repair Kits"),
    ("workshop","Workshop Supplies"),
]

def l1_card(key, label):
    if key == "drivetrain":
        return (
            '<div class="cat-card active" id="drivetrain-card" role="button" tabindex="0"'
            ' onclick="showLevel(2)" aria-label="Browse Drivetrain">'
            '<div class="card-img"><img src="' + CAT_I[key] + '" alt="" width="110" height="110"></div>'
            '<div class="card-body" style="flex-direction:column;align-items:flex-start;justify-content:center;gap:6px;">'
            '<span class="card-label">' + label + '</span>'
            '<span style="font-size:11px;color:#555;font-weight:400;">&#x25BA; Select to advance prototype</span>'
            '</div></div>'
        )
    return (
        '<div class="cat-card inert">'
        '<div class="card-img"><img src="' + CAT_I[key] + '" alt="" width="110" height="110"></div>'
        '<div class="card-body"><span class="card-label">' + label + '</span></div>'
        '</div>'
    )

l1_grid_html = "\n".join(l1_card(k, l) for k, l in L1_CARDS)

# ── L2 data ───────────────────────────────────────────────────────────────────
CATS = [
    ("Brakes &amp; Components", 6),("Clutches &amp; Components", 1),("Differentials", 6),
    ("Driveshafts &amp; Joints", 3),("Final Drive", 26),("Gears", 18),
    ("Other Drivetrain Components", 19),("Steering", 1),("Transmissions &amp; Components", 4),
]

SPECS = [
    ("Bore Diameter (in)",        [('Under 1"',"Under 25mm"),('1" – 3"',"25 – 76mm"),('3" – 6"',"76 – 152mm"),('6"+',"152mm+")]),
    ("Diameter (in)",             [('Under 5"',"Under 127mm"),('5" – 15"',"127 – 381mm"),('15" – 30"',"381 – 762mm"),('30"+',"762mm+")]),
    ("Inside Diameter (in)",      [('Under 5"',"Under 127mm"),('5" – 15"',"127 – 381mm"),('15" – 30"',"381 – 762mm"),('30"+',"762mm+")]),
    ("Outer Diameter (in)",       [('Under 5"',"Under 127mm"),('5" – 15"',"127 – 381mm"),('15" – 30"',"381 – 762mm"),('30"+',"762mm+")]),
    ("Outside Diameter (in)",     [('Under 10"',"Under 254mm"),('10" – 20"',"254 – 508mm"),('20" – 35"',"508 – 889mm"),('35"+',"889mm+")]),
    ("Number of Teeth",           ["16 – 30","31 – 50","51 – 80","81+"]),
    ("Seal Type",                 ["Duo Cone","Lip Seal","O-Ring","Mechanical Face"]),
    ("Type",                      ["Bearing","Disc","Gear","Seal","Assembly","Spider"]),
]

PRODUCTS = [
    ("567-4399","Swing Gear Bearing","Cat® Swing Gear Bearing","fits",True),
    ("122-9608","Right Hand Side Rubber Pedal","Cat® Right Hand Side Pilot Control Valve Rubber Pedal offers durability in demanding environments","fits",True),
    ("4B-9880","7.938mm Outer Diameter Check Ball","Cat® Check Ball for governor cutoff valve preventing backflow and contamination","fits",True),
    ("3D-2891","12.7mm Spherical Diameter Steel Ball","Cat® Ball Bearing (Loose ball only)","fits",True),
    ("593-5616","Planetary Gear","Cat® Planetary Gear","fits",True),
    ("517-4512","Control Group-Electronic","Electronic Control Group (A6N1 Yellow Key)","fits",True),
    ("567-7173","Single Row Tapered Roller Bearing","Cat® Single Row Tapered Roller Bearing, ID X OD X W: 254 X 315.9 X 34mm","fits",False),
    ("569-4288","90 Internal Teeth Ring Gear","Cat® Ring Gear, 90 Teeth","fits",False),
    ("569-4292","351.8mm Outer Diameter Duo Cone Seal","Cat® Duo Cone Seal (320), Steel and Rubber, Inside Diameter: 319mm","fits",False),
    ("569-4287","35 Tooth Planetary Gear","Planet Gear","fits",False),
    ("148-4636","34, 14 External Teeth Pinion Shaft","Cat® Pinion Shaft for transmitting power from the swing motor to the swing gear","unverified",True),
    ("174-4874","333.12mm Outside Diameter Duo Cone Seal","Cat® Duo Cone Seal","unverified",True),
    ("561-7005","Control Group-Pedal","Cat® Control Group-Pedal","unverified",True),
    ("296-6220","240mm Internal Diameter Ball Bearing","Cat® 310mm Outer Diameter Ball Bearing Used for Final Drive","unverified",True),
    ("2D-6642","6.35mm Spherical Diameter Steel Ball","Cat® Ball (Check)","unverified",True),
    ("523-0574","533.5mm Outer Diameter Final Drive","Cat® General Duty Small Excavator Final Drive","unverified",True),
    ("333-2998","533mm Outer Diameter Sprocket Housing","Cat® 533mm Outer Diameter Sprocket Ductile Iron Housing for Final Drive","unverified",True),
    ("378-9517","Drive Group-Swing","Cat® Swing Drive Group (Without Motor)","unverified",True),
    ("584-2564","Right Hand Final Drive","Cat® Final Drive transfers torque from the travel motor to the undercarriage","unverified",False),
    ("584-2563","Left Hand Final Drive","Cat® Final Drive transfers torque from the travel motor to the undercarriage","unverified",False),
]

def prod_card(num, name, desc, fit, has_img):
    img_src = PI[num] if has_img else NO_IMG
    desc_html = (desc[:97].rsplit(' ',1)[0] + '... <a href="#" class="more-link" onclick="return false;">More</a>' if len(desc) > 100 else desc)
    badge = ('<div class="fit-badge fits">' + FIT_CHECK_SM + ' Factory Fit 320 ZBN60173</div>' if fit == 'fits' else '')
    blend = ' style="mix-blend-mode:multiply;"' if has_img else ''
    img_cls = '' if has_img else ' class="no-img"'
    is_proto = (num == '567-4399')
    card_cls = 'prod-card proto-card' if is_proto else 'prod-card'
    card_id  = ' id="protoCard"' if is_proto else ''
    advance  = '<p class="advance-hint">&#x25BA; Select to advance prototype</p>' if is_proto else ''
    click    = ' onclick="showLevel(3)"' if is_proto else ''
    return (
        '<div class="' + card_cls + '"' + card_id + click + '>'
        '<div class="prod-img"><img src="' + img_src + '" alt="' + name + '" width="140" height="140"' + img_cls + blend + '></div>'
        '<div class="prod-info">'
        '<span class="prod-num">' + num + '</span>'
        '<p class="prod-name">' + name + '</p>'
        '<p class="prod-desc">' + desc_html + '</p>'
        '<div class="prod-bottom">' + badge + advance +
        ('<button class="add-cart-btn" type="button" '
         'onclick="openQtyModal(\'' + name.replace("'","\\'") + '\',\'' + num + '\',\'' + img_src[:60] + '...\',' + ('true' if has_img else 'false') + ');event.stopPropagation();">'
         'Add to Cart</button>') +
        '</div></div></div>'
    )

l2_grid_html = "\n".join(prod_card(*p) for p in PRODUCTS)

# sidebar categories
cat_links_html = "\n".join(
    '<li><a href="#" onclick="return false;">' + c + ' <span style="color:#999;font-weight:400;">(' + str(n) + ')</span></a></li>'
    for c, n in CATS
)

# spec filters (accordion-look, non-functional)
def spec_filter_html():
    out = '<div class="sidebar-section"><div class="sidebar-section-title">Filter by Specification</div>'
    out += '<div class="unit-toggle"><button class="unit-btn active" type="button">US</button><button class="unit-btn" type="button">Metric</button></div>'
    for label, opts in SPECS:
        out += '<div class="spec-filter-label">' + label + CHEVRON_SVG + '</div>'
    out += '</div>'
    return out

# ── L3 data ───────────────────────────────────────────────────────────────────
FBT_ITEMS = [
    ("570-5838","210mm Outer Diameter Lip Type Oil Seal"),
    ("570-5839","185mm Outer Diameter Ring Seal"),
    ("605-7780","105mm Inner Diameter Oil Seal"),
    ("4D-6695","329.79mm Inside Diameter Seal-O-Ring"),
    ("570-5840","Single Row Tapered Roller Bearing"),
]

DIAGRAMS = [
    ("6211633 GEAR & BEARING GP-SWING", [
        ("5K9243","ELBOW-FLARED"),("7Y1648","STRIP"),("8T4199","BOLT"),("0964902","DOWEL"),
        ("8T3282","WASHER-HARD"),("4685306","SPACER"),("1484689","TUBE AS"),("3B8489","ADAPTER"),
    ]),
    ("5772733 GEAR & BEARING GP-SWING", [
        ("3B8489","ADAPTER"),("5K9243","ELBOW-FLARED"),("7Y1647","GASKET"),("1484689","TUBE AS"),
        ("2276105","BOOT"),("1459278","BOLT"),("5Q3560","BOLT"),("4N9170","CLIP"),
    ]),
    ("5674399 GEAR & BEARING GP-SWING", [
        ("3527064","CAP"),("3B8489","ADAPTER"),("2276071","SEAL-DUST"),("1484685","SEAL"),
    ]),
]

def diag_svg_1():
    dots = ""
    for a in range(0, 360, 12):
        r = 148
        cx = int(240 + r * math.cos(math.radians(a)))
        cy = int(200 + r * math.sin(math.radians(a)))
        dots += '<circle cx="' + str(cx) + '" cy="' + str(cy) + '" r="5" fill="none" stroke="#3355cc" stroke-width="1.2"/>'
    return ('<svg viewBox="0 0 480 380" xmlns="http://www.w3.org/2000/svg" font-family="Arial,sans-serif">'
            '<rect width="480" height="380" fill="#fff"/>'
            '<circle cx="240" cy="200" r="148" fill="none" stroke="#3355cc" stroke-width="2.5"/>'
            '<circle cx="240" cy="200" r="130" fill="none" stroke="#3355cc" stroke-width="1.5" stroke-dasharray="4 3"/>'
            '<circle cx="240" cy="200" r="112" fill="none" stroke="#3355cc" stroke-width="2"/>'
            '<circle cx="240" cy="200" r="38" fill="none" stroke="#666" stroke-width="1"/>'
            '<circle cx="240" cy="200" r="22" fill="none" stroke="#666" stroke-width="1.5"/>'
            + dots +
            '<line x1="80" y1="200" x2="400" y2="200" stroke="#888" stroke-width="0.5" stroke-dasharray="6 4"/>'
            '<line x1="240" y1="40" x2="240" y2="360" stroke="#888" stroke-width="0.5" stroke-dasharray="6 4"/>'
            '<text x="240" y="375" text-anchor="middle" font-size="13" font-weight="bold" fill="#222">TOP VIEW</text>'
            '</svg>')

DIAG_SVGS = [
    diag_svg_1(),
    ('<svg viewBox="0 0 480 380" xmlns="http://www.w3.org/2000/svg" font-family="Arial,sans-serif">'
     '<rect width="480" height="380" fill="#fff"/>'
     '<text x="240" y="22" text-anchor="middle" font-size="11" font-weight="bold" fill="#222">5772733 GEAR &amp; BEARING GP-SWING</text>'
     '<ellipse cx="240" cy="200" rx="110" ry="55" fill="none" stroke="#3355cc" stroke-width="2.5"/>'
     '<ellipse cx="240" cy="185" rx="110" ry="55" fill="none" stroke="#3355cc" stroke-width="1.5" stroke-dasharray="3 2"/>'
     '<ellipse cx="240" cy="200" rx="38" ry="20" fill="none" stroke="#3355cc" stroke-width="2"/>'
     '<line x1="130" y1="200" x2="130" y2="185" stroke="#3355cc" stroke-width="2.5"/>'
     '<line x1="350" y1="200" x2="350" y2="185" stroke="#3355cc" stroke-width="2.5"/>'
     '<rect x="195" y="138" width="90" height="40" rx="4" fill="none" stroke="#666" stroke-width="1.5"/>'
     '<text x="240" y="162" text-anchor="middle" font-size="10" fill="#444">UPPER FRAME</text>'
     '<circle cx="175" cy="260" r="35" fill="none" stroke="#555" stroke-width="1.5"/>'
     '<circle cx="350" cy="285" r="25" fill="none" stroke="#555" stroke-width="1.5"/>'
     '<text x="100" y="345" font-size="9" fill="#333">FWD</text>'
     '<polygon points="88,340 100,345 88,350" fill="#333"/>'
     '</svg>'),
    ('<svg viewBox="0 0 480 380" xmlns="http://www.w3.org/2000/svg" font-family="Arial,sans-serif">'
     '<rect width="480" height="380" fill="#fff"/>'
     '<text x="240" y="22" text-anchor="middle" font-size="11" font-weight="bold" fill="#222">5674399 GEAR &amp; BEARING GP-SWING</text>'
     '<rect x="60" y="60" width="360" height="260" rx="8" fill="none" stroke="#bbb" stroke-width="1.5"/>'
     '<ellipse cx="240" cy="210" rx="105" ry="52" fill="none" stroke="#3355cc" stroke-width="2.5"/>'
     '<ellipse cx="240" cy="198" rx="105" ry="52" fill="none" stroke="#3355cc" stroke-width="1.5" stroke-dasharray="3 2"/>'
     '<ellipse cx="240" cy="210" rx="36" ry="18" fill="none" stroke="#3355cc" stroke-width="2"/>'
     '<line x1="135" y1="210" x2="135" y2="198" stroke="#3355cc" stroke-width="2.5"/>'
     '<line x1="345" y1="210" x2="345" y2="198" stroke="#3355cc" stroke-width="2.5"/>'
     '<text x="155" y="82" font-size="10" fill="#444">UNDERCARRIAGE</text>'
     '<text x="165" y="94" font-size="10" fill="#444">FRAME</text>'
     '<text x="370" y="345" font-size="9" fill="#333">FWD</text>'
     '<polygon points="358,340 370,345 358,350" fill="#333"/>'
     '</svg>'),
]

# ── Build HTML ────────────────────────────────────────────────────────────────
out = []
out.append('<title>CAT Parts Store</title>')
out.append('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Roboto+Mono:wght@500&display=swap">')

# ── CSS ───────────────────────────────────────────────────────────────────────
out.append("""<style>
:root{color-scheme:light;--yellow:#FFCD11;--bg:#fff;--card-bg:#F7F7F7;--border:#E0E0E0;--text:#111;--muted:#666;--green:#2E7D32;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html,body{min-height:100%;}
body{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:var(--bg);color:var(--text);font-size:14px;line-height:1.5;padding-top:54px;display:flex;flex-direction:column;}
a{color:inherit;text-decoration:none;}
/* LEVELS */
.level{display:block;flex:1;}
.level.hidden{display:none;}
/* HEADER */
.site-header{background:#000;position:fixed;top:0;left:0;right:0;z-index:100;}
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
.cat-app-menu a{display:block;padding:12px 16px;font-size:13px;color:#333;border-bottom:1px solid #f0f0f0;transition:background .1s;}
.cat-app-menu a:last-child{border-bottom:none;}
.cat-app-menu a:hover{background:#f5f5f5;}
.cat-app-menu a.cat-app-home{font-weight:600;color:#111;}
.store-btn{background:none;border:none;color:#fff;cursor:pointer;display:flex;align-items:center;gap:5px;font-size:12px;font-family:inherit;padding:6px 10px;white-space:nowrap;border-radius:2px;transition:background .12s;}
.store-btn:hover{background:rgba(255,255,255,.09);}
.search-area{width:100%;max-width:520px;display:flex;background:#fff;overflow:hidden;border-radius:22px;}
/* L1 equip button — "Add Equipment" */
.add-equip-btn{display:flex;align-items:center;gap:5px;background:var(--yellow);border:none;border-right:1px solid #D0D0D0;padding:0 12px;cursor:pointer;white-space:nowrap;flex-shrink:0;font-size:12px;color:#111;font-family:inherit;font-weight:600;height:36px;transition:background .12s;min-width:126px;}
.add-equip-btn:hover{background:#e6b800;}
/* L2/L3 equip button — "320" context */
.equip-context-btn{display:none;align-items:center;gap:6px;background:var(--yellow);border:none;border-right:1px solid #D0D0D0;padding:0 14px;cursor:pointer;white-space:nowrap;flex-shrink:0;font-size:13px;font-weight:700;color:#111;font-family:inherit;height:36px;transition:background .12s;min-width:126px;}
.equip-context-btn:hover{background:#e6b800;}
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
.lang-grid a{display:block;padding:7px 8px;font-size:12px;color:#111;border-radius:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.lang-grid a:first-child{font-weight:700;}
.lang-grid a:hover{background:#f5f5f5;}
.acct-wrap{position:relative;}
.acct-menu{display:none;position:absolute;top:calc(100% + 6px);right:0;background:#fff;border:1px solid #ddd;min-width:220px;box-shadow:0 4px 16px rgba(0,0,0,.13);z-index:200;}
.acct-menu.open{display:block;}
.acct-menu a{display:block;padding:11px 16px;font-size:13px;color:#111;border-bottom:1px solid #f0f0f0;}
.acct-menu a.acct-sub-item{padding-left:28px;font-size:12px;color:#666;background:#FAFAFA;}
.acct-menu a.acct-signout{border-bottom:none;color:#888;font-size:12px;border-top:1px solid #eee;padding-top:10px;}
.acct-menu a:hover{background:#f0f0f0;}
.cart-btn-wrap{position:relative;display:inline-flex;}
.cart-badge{background:var(--yellow);color:#111;border-radius:50%;width:16px;height:16px;font-size:9px;font-weight:700;display:none;align-items:center;justify-content:center;position:absolute;top:-2px;right:0;pointer-events:none;}
.cart-badge.visible{display:flex;}
/* Add Equipment Dropdown (L1 only — position:fixed within iframe) */
.equip-dropdown{display:none;position:fixed;top:54px;background:#fff;border:1px solid #D0D0D0;border-top:2px solid var(--yellow);border-radius:0 0 10px 10px;box-shadow:0 4px 16px rgba(0,0,0,.12);padding:12px 14px;z-index:99;}
.equip-dropdown.open{display:block;}
.equip-drop-inner{display:flex;gap:10px;align-items:center;}
.equip-drop-fields{flex:1;display:flex;flex-direction:column;gap:8px;}
.equip-drop-input{width:100%;padding:8px 12px;border:1px solid #D0D0D0;border-radius:6px;font-size:12px;font-family:inherit;background:#fff;color:#111;outline:none;}
.equip-drop-input:focus{border-color:var(--yellow);box-shadow:0 0 0 2px rgba(255,205,17,.2);}
.equip-drop-add{background:var(--yellow);border:none;padding:10px 18px;border-radius:6px;font-size:12px;font-weight:700;font-family:inherit;cursor:pointer;flex-shrink:0;transition:background .12s;}
.equip-drop-add:hover{background:#e6b800;}
/* SHARED LAYOUT */
.wrap{max-width:1280px;margin:0 auto;padding:0 20px;}
.breadcrumb{padding:14px 0 0;font-size:12px;color:var(--muted);display:flex;gap:6px;align-items:center;flex-wrap:wrap;}
.breadcrumb a{color:var(--muted);cursor:pointer;}
.breadcrumb a:hover{text-decoration:underline;}
.page-title{padding:16px 0 20px;}
.page-title h1{font-size:24px;font-weight:700;display:inline-block;padding-bottom:7px;border-bottom:3px solid var(--yellow);}
/* L1 GRID */
.cat-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;padding-bottom:48px;}
.cat-card{background:var(--card-bg);border:1px solid var(--border);border-radius:10px;display:flex;align-items:stretch;text-decoration:none;color:var(--text);min-height:130px;transition:box-shadow .15s,border-color .15s;overflow:hidden;}
.cat-card.inert{cursor:default;}
.cat-card.inert:hover{border-color:#000;box-shadow:0 2px 10px rgba(0,0,0,.1);}
.cat-card.active{cursor:pointer;}
#drivetrain-card:hover{border-color:var(--yellow);box-shadow:0 2px 10px rgba(255,205,17,.25);}
.card-img{width:140px;flex-shrink:0;display:flex;align-items:center;justify-content:center;padding:12px;}
.card-img img{width:110px;height:110px;object-fit:contain;mix-blend-mode:multiply;}
.card-body{flex:1;padding:0 18px;display:flex;align-items:center;}
.card-label{font-size:17px;font-weight:600;line-height:1.4;}
/* NEW EXP BANNER (L1 only) */
.new-exp-banner{background:#1A1A1A;color:#fff;display:flex;align-items:center;justify-content:center;padding:10px 48px 10px 20px;font-size:13px;line-height:1.4;position:relative;}
.new-exp-banner a{color:var(--yellow);text-decoration:underline;text-underline-offset:2px;}
.banner-close{position:absolute;right:14px;top:50%;transform:translateY(-50%);background:none;border:none;color:#fff;cursor:pointer;font-size:20px;line-height:1;padding:4px 8px;border-radius:2px;}
/* L2 LAYOUT */
.page-layout{display:flex;gap:28px;align-items:flex-start;padding-bottom:48px;}
.sidebar{width:220px;flex-shrink:0;position:sticky;top:70px;}
.sidebar-section{margin-bottom:24px;}
.sidebar-section-title{font-size:15px;font-weight:700;color:#111;padding:0 0 10px;border-bottom:2px solid var(--border);margin-bottom:8px;}
.sidebar-links{list-style:none;}
.sidebar-links li a{display:block;padding:7px 0;font-size:13px;color:var(--text);border-bottom:1px solid #F5F5F5;}
.sidebar-links li a:hover{color:#000;text-decoration:underline;}
.unit-toggle{display:flex;background:#E8E8E8;border-radius:20px;padding:2px;margin-bottom:12px;}
.unit-btn{flex:1;border:none;background:none;padding:4px 10px;border-radius:18px;font-size:12px;font-family:inherit;cursor:pointer;color:#666;font-weight:500;transition:background .12s,color .12s;}
.unit-btn.active{background:#fff;color:#111;font-weight:600;box-shadow:0 1px 3px rgba(0,0,0,.12);}
.spec-filter-label{padding:9px 0;font-size:13px;border-bottom:1px solid var(--border);color:var(--text);display:flex;align-items:center;justify-content:space-between;cursor:default;user-select:none;}
.main-content{flex:1;min-width:0;}
.filter-sort-bar{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:16px;flex-wrap:wrap;}
.type-filter-row{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}
.type-chip{display:inline-flex;align-items:center;gap:5px;padding:5px 12px;border:1px solid var(--border);border-radius:22px;font-size:12px;font-weight:500;font-family:inherit;background:#fff;color:var(--text);cursor:pointer;transition:background .12s,border-color .12s,color .12s;white-space:nowrap;}
.type-chip:hover{border-color:#888;}
.type-chip.active{background:#111;border-color:#111;color:#fff;}
.sort-bar{display:flex;align-items:center;gap:10px;flex-shrink:0;}
.sort-label{font-size:13px;color:var(--muted);}
.sort-select{font-size:13px;font-family:inherit;padding:5px 28px 5px 10px;border:1px solid var(--border);border-radius:4px;background:#fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6' viewBox='0 0 10 6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%23666'/%3E%3C/svg%3E") no-repeat right 8px center;color:var(--text);cursor:default;-webkit-appearance:none;}
/* FIT BANNER */
.fit-banner-wrap{margin-bottom:16px;}
.fit-banner-full{background:#fff;border:1px solid #e0e0e0;border-left:3px solid #2E7D32;border-radius:8px;padding:16px 20px 14px;display:flex;gap:24px;position:relative;}
.fit-banner-left{flex:1;min-width:0;}
.fit-banner-title{display:flex;align-items:center;gap:8px;font-size:15px;font-weight:700;color:#1a5c1a;margin-bottom:8px;}
.fit-banner-subtitle{font-size:13px;font-weight:600;color:#111;margin-bottom:6px;line-height:1.4;}
.fit-banner-body{font-size:12px;color:#555;line-height:1.55;}
.fit-banner-close{position:absolute;top:8px;right:10px;background:none;border:none;cursor:pointer;color:#bbb;font-size:22px;line-height:1;padding:1px 5px;border-radius:3px;font-family:inherit;}
.fit-banner-close:hover{color:#333;}
/* PRODUCT GRID */
.prod-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;}
.equip-card{background:#fff;border:2px solid var(--yellow);border-radius:10px;padding:18px 18px 56px;display:flex;flex-direction:column;position:relative;}
.equip-mach-img{width:100%;height:100px;object-fit:contain;border-radius:6px;background:#F7F7F7;margin-bottom:8px;}
.equip-card-title{font-size:13px;font-weight:700;display:flex;align-items:center;gap:7px;margin-bottom:12px;}
.equip-confirmed{display:flex;flex-direction:column;align-items:center;flex:1;text-align:center;gap:6px;justify-content:center;}
.equip-conf-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:#888;}
.equip-conf-model{font-size:15px;font-weight:700;}
.equip-conf-serial{font-size:11px;color:var(--muted);}
.equip-change-btn{background:none;border:1px solid #CCC;border-radius:22px;padding:8px 14px;font-size:12px;font-weight:600;font-family:inherit;cursor:pointer;color:var(--muted);position:absolute;bottom:12px;left:18px;right:18px;transition:border-color .12s;}
.equip-change-btn:hover{border-color:#999;color:#333;}
.prod-card{background:var(--card-bg);border:1px solid var(--border);border-radius:10px;overflow:hidden;display:flex;flex-direction:column;transition:border-color .15s;}
.prod-card:hover{border-color:#000;box-shadow:0 2px 10px rgba(0,0,0,.1);}
.prod-img{width:100%;height:160px;background:#fff;display:flex;align-items:center;justify-content:center;overflow:hidden;flex-shrink:0;}
.prod-img img{width:110px;height:110px;object-fit:contain;}
.prod-img img.no-img{width:140px;height:140px;}
.prod-info{padding:10px 12px 12px;display:flex;flex-direction:column;flex:1;}
.prod-num{font-family:"Roboto Mono",monospace;font-size:11px;font-weight:500;color:#555;letter-spacing:.02em;margin-bottom:4px;}
.prod-name{font-size:13px;font-weight:600;line-height:1.3;color:var(--text);margin-bottom:4px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;}
.prod-desc{font-size:11px;color:var(--muted);line-height:1.45;flex:1;margin-bottom:10px;}
.more-link{color:#555;font-weight:600;font-size:11px;}
.more-link:hover{color:#000;text-decoration:underline;}
.prod-bottom{margin-top:auto;display:flex;flex-direction:column;gap:7px;}
.fit-badge{display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:600;}
.fit-badge.fits{color:#2E7D32;}
.add-cart-btn{width:100%;background:var(--yellow);border:none;padding:8px;border-radius:22px;font-size:12px;font-weight:600;font-family:inherit;cursor:pointer;transition:background .12s;}
.add-cart-btn:hover{background:#e6b800;}
.proto-card{cursor:pointer;}
.advance-hint{font-size:10px;color:#888;font-weight:500;text-align:center;padding:3px 0 0;letter-spacing:.02em;}
.pagination{display:flex;align-items:center;justify-content:center;gap:14px;padding:28px 0 8px;margin-top:12px;}
.pg-btn{padding:8px 20px;border:1px solid var(--border);border-radius:22px;background:#fff;font-size:13px;font-family:inherit;cursor:pointer;color:var(--text);transition:background .12s;}
.pg-btn:hover:not(:disabled){background:#f0f0f0;}
.pg-btn:disabled{color:#bbb;cursor:default;}
.pg-info{font-size:13px;color:var(--muted);}
/* QTY MODAL */
.qty-modal-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:500;align-items:center;justify-content:center;}
.qty-modal-overlay.open{display:flex;}
.qty-modal{background:var(--card-bg);border:1px solid var(--border);border-radius:10px;min-width:260px;max-width:340px;width:90vw;position:relative;box-shadow:0 8px 40px rgba(0,0,0,.25);overflow:hidden;}
.qty-modal-img-area{width:100%;height:150px;background:#fff;display:flex;align-items:center;justify-content:center;border-bottom:1px solid var(--border);}
.qty-modal-img-area img{width:110px;height:110px;object-fit:contain;}
.qty-modal-body{padding:12px 14px 14px;}
.qty-modal-close{position:absolute;top:8px;right:10px;background:rgba(255,255,255,.85);border:none;cursor:pointer;font-size:18px;color:#555;padding:1px 6px;line-height:1;font-family:inherit;border-radius:4px;z-index:2;}
.qty-modal-num{font-family:"Roboto Mono",monospace;font-size:11px;font-weight:500;color:#555;display:block;margin-bottom:3px;}
.qty-modal-name{font-size:13px;font-weight:600;color:var(--text);line-height:1.3;margin-bottom:12px;}
.qty-input-row{display:flex;align-items:center;gap:10px;margin-bottom:12px;}
.qty-input-row label{font-size:13px;font-weight:600;flex-shrink:0;}
.qty-input{width:72px;padding:7px 10px;border:1px solid #D0D0D0;border-radius:6px;font-size:14px;font-family:inherit;text-align:center;font-weight:600;background:#fff;color:#111;outline:none;}
.qty-input:focus{border-color:var(--yellow);box-shadow:0 0 0 2px rgba(255,205,17,.2);}
.qty-modal-actions{display:flex;gap:10px;}
.qty-cancel-btn{flex:1;background:#fff;border:1px solid #CCC;padding:9px;border-radius:22px;font-size:12px;font-weight:600;font-family:inherit;cursor:pointer;color:var(--muted);}
.qty-cancel-btn:hover{border-color:#999;color:#333;}
.qty-confirm-btn{flex:2;background:var(--yellow);border:none;padding:9px;border-radius:22px;font-size:12px;font-weight:700;font-family:inherit;cursor:pointer;}
.qty-confirm-btn:hover{background:#e6b800;}
/* L3 LAYOUT */
.product-section{display:grid;grid-template-columns:200px 340px 1fr;gap:28px;padding:20px 0 36px;align-items:start;}
.fbt-sidebar{position:sticky;top:70px;}
.fbt-title{font-size:13px;font-weight:700;padding-bottom:10px;border-bottom:2px solid var(--border);margin-bottom:10px;}
.fbt-item{display:flex;gap:8px;padding:10px 0;border-bottom:1px solid #F0F0F0;}
.fbt-item.this-part{background:#FFFDE7;border-radius:6px;padding:10px 8px;margin-bottom:4px;border-bottom:none;}
.fbt-img{width:44px;height:44px;flex-shrink:0;background:#fff;border:1px solid var(--border);border-radius:4px;display:flex;align-items:center;justify-content:center;overflow:hidden;}
.fbt-img img{width:36px;height:36px;object-fit:contain;}
.fbt-info{flex:1;min-width:0;}
.fbt-num{font-family:"Roboto Mono",monospace;font-size:10px;font-weight:500;color:#555;display:block;margin-bottom:2px;}
.fbt-name{font-size:11px;color:var(--text);line-height:1.3;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;}
.fbt-fit{display:flex;align-items:center;gap:4px;font-size:10px;font-weight:600;color:var(--green);margin-top:4px;}
.main-img-wrap{width:100%;aspect-ratio:1;background:#fff;border:1px solid var(--border);border-radius:8px;display:flex;align-items:center;justify-content:center;overflow:hidden;margin-bottom:10px;}
.main-img-wrap img{width:260px;height:260px;object-fit:contain;mix-blend-mode:multiply;}
.thumb-row{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;}
.thumb{aspect-ratio:1;background:#fff;border:1px solid var(--border);border-radius:5px;display:flex;align-items:center;justify-content:center;overflow:hidden;cursor:pointer;transition:border-color .12s;}
.thumb.active{border-color:#000;border-width:2px;}
.thumb:hover{border-color:#888;}
.thumb img{width:48px;height:48px;object-fit:contain;mix-blend-mode:multiply;}
.pdp-partnum{font-family:"Roboto Mono",monospace;font-size:12px;font-weight:500;color:#555;display:block;margin-bottom:6px;}
.pdp-title{font-size:26px;font-weight:700;line-height:1.2;margin-bottom:8px;}
.pdp-underline{width:40px;height:3px;background:var(--yellow);margin-bottom:12px;}
.pdp-subtitle{font-size:14px;color:#333;margin-bottom:4px;}
.pdp-brand{font-size:13px;color:var(--muted);margin-bottom:14px;}
.pdp-fit-badge{display:flex;align-items:center;gap:6px;font-size:13px;font-weight:600;color:var(--green);margin-bottom:4px;}
.pdp-fit-machine{font-size:12px;color:var(--muted);margin-left:19px;margin-bottom:14px;}
.pdp-divider{border:none;border-top:1px solid var(--border);margin:18px 0;}
.pdp-section-title{font-size:16px;font-weight:700;margin-bottom:10px;}
.pdp-body-text{font-size:13px;color:#333;line-height:1.65;margin-bottom:10px;}
.pdp-attr-list{list-style:none;padding:0;margin-bottom:10px;}
.pdp-attr-list li{font-size:13px;color:#333;padding:2px 0 2px 12px;position:relative;line-height:1.5;}
.pdp-attr-list li::before{content:"•";position:absolute;left:0;color:#555;}
.pdp-warning{background:#FFF8E1;border:1px solid #FFE082;border-radius:6px;padding:10px 12px;font-size:11px;color:#5D4037;line-height:1.55;margin-top:12px;}
.pdp-spec-row{display:flex;gap:8px;font-size:13px;padding:6px 0;border-bottom:1px solid #F5F5F5;}
.pdp-spec-label{font-weight:700;flex-shrink:0;min-width:100px;}
.pdp-spec-value{color:#333;}
.pdp-compat-group{margin-bottom:10px;}
.pdp-compat-cat{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#666;margin-bottom:3px;}
.pdp-compat-models{font-size:13px;color:#333;line-height:1.6;}
.pdp-cta{margin-top:22px;display:flex;align-items:center;gap:12px;flex-wrap:wrap;}
.check-price-btn{background:#111;color:#fff;border:none;padding:11px 26px;border-radius:4px;font-size:14px;font-weight:700;font-family:inherit;cursor:pointer;transition:background .12s;}
.check-price-btn:hover{background:#333;}
.login-link{font-size:13px;color:#0052a5;text-decoration:underline;cursor:pointer;}
.pdp-links{margin-top:14px;display:flex;gap:0;align-items:center;}
.pdp-links a{font-size:12px;color:#0052a5;text-decoration:underline;padding-right:12px;margin-right:12px;border-right:1px solid #CCC;cursor:pointer;}
.pdp-links a:last-child{border-right:none;margin-right:0;padding-right:0;}
/* DIAGRAMS */
.diagram-section{border-top:2px solid var(--border);padding:28px 0 48px;}
.diagram-section-hdr{display:flex;align-items:baseline;gap:10px;margin-bottom:18px;}
.diagram-section-hdr h2{font-size:20px;font-weight:700;}
.diagram-count{font-size:14px;color:var(--muted);}
.diagram-window{display:flex;position:relative;border:1px solid var(--border);border-radius:8px;overflow:hidden;height:420px;}
.diagram-nav{position:absolute;top:50%;transform:translateY(-50%);z-index:10;width:36px;height:64px;background:#fff;border:1px solid #CCC;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:20px;color:#333;transition:background .12s;}
.diagram-nav:hover{background:var(--yellow);color:#000;border-color:var(--yellow);}
.diagram-nav-prev{left:0;border-radius:0 8px 8px 0;border-left:none;}
.diagram-nav-next{right:0;border-radius:8px 0 0 8px;border-right:none;}
.diagram-nav:disabled{color:#CCC;cursor:default;}
.diagram-nav:disabled:hover{background:#fff;color:#CCC;border-color:#CCC;}
.diagram-slide{display:none;width:100%;}
.diagram-slide.active{display:flex;}
.diagram-img-area{flex:3;border-right:1px solid var(--border);overflow:hidden;display:flex;align-items:center;justify-content:center;background:#fff;}
.diagram-img-area svg{max-width:100%;max-height:100%;}
.diagram-parts-list{flex:2;overflow-y:auto;padding:14px 0;}
.diagram-parts-title{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#888;padding:0 14px 10px;border-bottom:1px solid #F0F0F0;}
.diagram-part-row{display:flex;align-items:center;gap:10px;padding:9px 14px;border-bottom:1px solid #F8F8F8;transition:background .1s;}
.diagram-part-row:hover{background:#F7F7F7;}
.dpr-num{font-size:12px;font-weight:700;color:#888;width:18px;flex-shrink:0;}
.dpr-thumb{width:28px;height:28px;flex-shrink:0;background:#EFEFEF;border:1px solid #DDD;border-radius:3px;display:flex;align-items:center;justify-content:center;overflow:hidden;}
.dpr-thumb img{width:24px;height:24px;object-fit:contain;}
.dpr-partnum{font-family:"Roboto Mono",monospace;font-size:10px;font-weight:500;color:#555;display:block;}
.dpr-partname{font-size:11px;font-weight:500;}
.diagram-indicator{display:flex;justify-content:center;gap:8px;margin-top:12px;}
.diag-dot{width:8px;height:8px;border-radius:50%;background:#DDD;cursor:pointer;border:none;transition:background .12s;}
.diag-dot.active{background:#111;}
/* FOOTER */
.site-footer{background:var(--yellow);padding:26px 16px 16px;text-align:center;}
.social-row{display:flex;justify-content:center;align-items:center;gap:12px;margin-bottom:10px;}
.soc-icon{width:34px;height:34px;border-radius:50%;background:#000;display:flex;align-items:center;justify-content:center;color:var(--yellow);text-decoration:none;flex-shrink:0;transition:opacity .13s;}
.soc-icon:hover{opacity:.78;}
.footer-copy{font-size:11px;color:#333;font-weight:600;margin-bottom:8px;}
.footer-legal{font-size:11px;color:#333;line-height:2;}
.footer-legal .pipe{margin:0 5px;color:#666;}
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
@media(max-width:1000px){.product-section{grid-template-columns:180px 1fr;}.fbt-sidebar{display:none;}}
@media(max-width:900px){.sidebar{display:none;}.prod-grid{grid-template-columns:repeat(2,1fr);}}
@media(max-width:860px){.cat-grid{grid-template-columns:repeat(2,1fr);}.lang-menu{width:320px;}.lang-grid{grid-template-columns:repeat(2,1fr);}}
@media(max-width:700px){.product-section{grid-template-columns:1fr;}.fbt-sidebar{display:none;}.diagram-window{height:auto;flex-direction:column;}.diagram-img-area{height:280px;}.diagram-parts-list{height:220px;}}
@media(max-width:640px){.cat-grid{grid-template-columns:1fr;}.lang-menu{right:-40px;width:280px;}.lang-grid{grid-template-columns:1fr;}.filter-sort-bar{flex-direction:column;align-items:flex-start;}.prod-grid{grid-template-columns:1fr;}}
</style>""")

# ── HEADER ────────────────────────────────────────────────────────────────────
MACH_SVG = '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="' + MACHINE_ICON + '"/></svg>'
out.append(
    '<header class="site-header">'
    '<div class="hdr-inner">'
    '<div class="hdr-left">'
    '<div class="cat-wrap">'
    '<a href="#" class="cat-logo" aria-label="Cat Applications" onclick="return false;">'
    '<img src="' + LOGO + '" alt="Caterpillar" width="64" height="35">'
    '<svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" aria-hidden="true" style="margin-left:4px;flex-shrink:0;"><polyline points="6 9 12 15 18 9"/></svg>'
    '</a>'
    '<div class="cat-app-menu">' + cat_app_html + '</div>'
    '</div>'
    '<button class="store-btn" type="button">'
    '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle cx="12" cy="9" r="2.5"/></svg>'
    '<span>Select Store</span>'
    '</button>'
    '</div>'
    '<div class="hdr-center">'
    '<div class="search-area" role="search">'
    '<button class="add-equip-btn" id="addEquipBtn" type="button" aria-label="Add equipment">'
    + MACH_SVG +
    '<span>Add Equipment</span>'
    '</button>'
    '<button class="equip-context-btn" id="equipContextBtn" type="button" aria-label="Equipment: 320 Excavator">'
    + MACH_SVG +
    '<span>320</span>'
    '</button>'
    '<input type="search" placeholder="Search for part number or name" aria-label="Search parts">'
    '<button class="search-submit" type="button" aria-label="Search">'
    '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><line x1="16.5" y1="16.5" x2="22" y2="22"/></svg>'
    '</button>'
    '</div>'
    '</div>'
    '<div class="hdr-right">'
    '<div class="lang-wrap">'
    '<button class="hbtn" type="button" aria-label="Select language">'
    '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>'
    '<span>EN</span>'
    '<svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>'
    '</button>'
    '<div class="lang-menu"><div class="lang-grid">' + lang_items + '</div></div>'
    '</div>'
    '<div class="acct-wrap">'
    '<button class="hbtn" type="button">'
    '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>'
    '<span>Account</span>'
    '<svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>'
    '</button>'
    '<div class="acct-menu">'
    '<a href="#" onclick="return false;">Manage My Equipment</a>'
    '<a href="#" onclick="return false;" class="acct-sub-item">&#8627; Parts Diagram</a>'
    '<a href="#" onclick="return false;">Order History</a>'
    '<a href="#" onclick="return false;">View Finance Solutions</a>'
    '<a href="#" onclick="return false;">Cat&reg; Rewards</a>'
    '<a href="#" onclick="return false;">Service Information System (SIS)</a>'
    '<a href="#" class="acct-signout" onclick="return false;">Sign Out</a>'
    '</div>'
    '</div>'
    '<div class="cart-btn-wrap">'
    '<button class="hbtn" id="cartBtn" type="button" aria-label="Cart">'
    '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>'
    '</button>'
    '<span class="cart-badge" id="cartBadge"></span>'
    '</div>'
    '</div>'
    '</div>'
    '</header>'
)

# Add Equipment dropdown
out.append(
    '<div class="equip-dropdown" id="equipDropdown" aria-label="Add equipment">'
    '<div class="equip-drop-inner">'
    '<div class="equip-drop-fields">'
    '<input type="text" class="equip-drop-input" id="dropSerial" placeholder="Serial number, e.g. ZBN60173" autocomplete="off">'
    '<input type="text" class="equip-drop-input" id="dropModel" placeholder="Model name, e.g. 320 Excavator" autocomplete="off">'
    '</div>'
    '<button type="button" class="equip-drop-add" id="dropAddBtn">Add</button>'
    '</div>'
    '</div>'
)

# ── LEVEL 1 ───────────────────────────────────────────────────────────────────
out.append('<div id="l1" class="level">')
out.append(
    '<div class="new-exp-banner" id="newExpBanner">'
    'You&#8217;re navigating a redesigned experience.&nbsp;'
    '<a href="#" onclick="return false;">Return to the legacy website</a>'
    '<button class="banner-close" type="button" aria-label="Dismiss" onclick="this.parentElement.hidden=true;">&#215;</button>'
    '</div>'
)
out.append(
    '<main>'
    '<div class="wrap">'
    '<nav class="breadcrumb"><span>Home</span><span>/</span><span aria-current="page">All Categories</span></nav>'
    '<div class="page-title"><h1>Shop By Category</h1></div>'
    '<div class="cat-grid">'
    + l1_grid_html +
    '</div>'
    '</div>'
    '</main>'
)
out.append('</div>') # l1

# ── LEVEL 2 ───────────────────────────────────────────────────────────────────
fit_banner = (
    '<div class="fit-banner-wrap" id="fitBannerWrap">'
    '<div class="fit-banner-full">'
    '<div class="fit-banner-left">'
    '<div class="fit-banner-title">' + FIT_CHECK_LG + ' Factory Fit</div>'
    '<p class="fit-banner-subtitle">This part is designed to fit your Cat equipment based on the manufacturer\'s specifications.</p>'
    '<p class="fit-banner-body">Any changes to the manufacturer\'s configuration might result in the product not fitting your Cat equipment. Please consult your Cat Dealer before purchasing to ensure that this part is appropriate for your Cat equipment in its current condition and assumed configuration.</p>'
    '</div>'
    '<button class="fit-banner-close" id="fitBannerClose" type="button" aria-label="Close">&times;</button>'
    '</div>'
    '</div>'
)

type_chips = (
    '<div class="type-filter-row">'
    '<button class="type-chip active" type="button">All</button>'
    '<button class="type-chip" type="button">' + FIT_CHECK_SM + ' Factory Fit</button>'
    '<button class="type-chip" type="button">' + REMAN_SVG + ' Remanufactured</button>'
    '<button class="type-chip" type="button">' + NO_RETURN_SVG + ' Non-Returnable</button>'
    '<button class="type-chip" type="button">' + KIT_SVG + ' Kit</button>'
    '<button class="type-chip" type="button">' + REPLACED_SVG + ' Replaced</button>'
    '</div>'
)

equip_card = (
    '<div class="equip-card" id="equipCard">'
    '<img class="equip-mach-img" src="' + MACH + '" alt="320 Excavator">'
    '<div class="equip-card-title">'
    + FIT_CHECK_SM +
    '<span>Equipment Confirmed</span>'
    '</div>'
    '<div class="equip-confirmed">'
    '<span class="equip-conf-label">Your Machine</span>'
    '<span class="equip-conf-model">320 Excavator</span>'
    '<span class="equip-conf-serial">S/N: ZBN60173</span>'
    '</div>'
    '<button class="equip-change-btn" type="button">Change equipment</button>'
    '</div>'
)

out.append('<div id="l2" class="level hidden">')
out.append(
    '<main>'
    '<div class="wrap">'
    '<nav class="breadcrumb">'
    '<a onclick="showLevel(1)">Home</a><span>/</span>'
    '<span>Drivetrain</span><span>/</span>'
    '<span aria-current="page">Other Drivetrain Components</span>'
    '</nav>'
    '<div class="page-title"><h1>Other Drivetrain Components</h1></div>'
    + fit_banner +
    '<div class="page-layout">'
    '<aside class="sidebar">'
    '<div class="sidebar-section">'
    '<div class="sidebar-section-title">Categories</div>'
    '<ul class="sidebar-links">' + cat_links_html + '</ul>'
    '</div>'
    + spec_filter_html() +
    '</aside>'
    '<div class="main-content">'
    '<div class="filter-sort-bar">'
    + type_chips +
    '<div class="sort-bar">'
    '<span class="sort-label">Sort by:</span>'
    '<select class="sort-select" aria-label="Sort by"><option>Relevance</option><option>Name</option><option>Part Number</option></select>'
    '</div>'
    '</div>'
    '<div class="prod-grid">'
    + equip_card
    + l2_grid_html +
    '</div>'
    '<div class="pagination"><button class="pg-btn" disabled>&#8592; Previous</button><span class="pg-info">Page 1 of 3</span><button class="pg-btn">Next &#8594;</button></div>'
    '</div>'
    '</div>'
    '</div>'
    '</main>'
)
out.append('</div>') # l2

# ── LEVEL 3 ───────────────────────────────────────────────────────────────────
fbt_sidebar_html = (
    '<aside class="fbt-sidebar">'
    '<div class="fbt-title">Frequently Bought Together</div>'
    '<div class="fbt-item this-part">'
    '<div class="fbt-img"><img src="' + PROD_HERO + '" alt="Swing Gear Bearing" width="36" height="36" style="mix-blend-mode:multiply;"></div>'
    '<div class="fbt-info"><span class="fbt-num">567-4399</span><span class="fbt-name">Swing Gear bearing</span>'
    '<div class="fbt-fit">' + FIT_CHECK_SM + ' Factory Fit</div></div>'
    '</div>'
    + "".join(
        '<div class="fbt-item"><div class="fbt-img"><img src="' + NO_IMG + '" alt="' + nm + '" width="36" height="36"></div>'
        '<div class="fbt-info"><span class="fbt-num">' + pn + '</span><span class="fbt-name">' + nm + '</span>'
        '<div class="fbt-fit">' + FIT_CHECK_SM + ' Factory Fit</div></div></div>'
        for pn, nm in FBT_ITEMS
    ) +
    '</aside>'
)

prod_images_html = (
    '<div class="prod-images">'
    '<div class="main-img-wrap"><img src="' + PROD_HERO + '" alt="567-4399 Swing Gear Bearing" width="260" height="260"></div>'
    '<div class="thumb-row">'
    + "".join('<div class="thumb' + (' active' if i == 0 else '') + '"><img src="' + PROD_HERO + '" alt="" width="48" height="48"></div>' for i in range(4)) +
    '</div>'
    '</div>'
)

prod_info_html = (
    '<div class="prod-info-col">'
    '<span class="pdp-partnum">567-4399</span>'
    '<h1 class="pdp-title">Swing Gear Bearing</h1>'
    '<div class="pdp-underline"></div>'
    '<p class="pdp-subtitle">Cat&reg; Swing Gear Bearing</p>'
    '<p class="pdp-brand">Brand: Cat</p>'
    '<div class="pdp-fit-badge">' + FIT_CHECK_LG + ' Factory Fit</div>'
    '<p class="pdp-fit-machine">320 Excavator ZBN60173</p>'
    '<hr class="pdp-divider">'
    '<div class="pdp-section-title">Description</div>'
    '<p class="pdp-body-text">A Swing Gear bearing is an important component used in different mechanical systems, particularly in heavy machinery equipment. These bearings are designed to support and facilitate the smooth rotation of the swing gear, which allows for the controlled movement of the machinery.</p>'
    '<ul class="pdp-attr-list"><li>Designed to be durable, robust, and capable of handling heavy loads.</li><li>High Strength.</li><li>Corrosion resistance.</li></ul>'
    '<p class="pdp-body-text"><strong>Applications:</strong> A Swing Gear bearing enables the machinery to rotate horizontally or swing from side to side, providing important mobility and maneuverability.</p>'
    '<div class="pdp-warning"><strong>&#9888; WARNING:</strong> This product can expose you to chemicals including Carbon black (airborne, unbound particles of respirable size), which is known to the State of California to cause cancer. For more information go to <a href="#" onclick="return false;" style="color:#5D4037;">www.P65Warnings.ca.gov</a>.</div>'
    '<hr class="pdp-divider">'
    '<div class="pdp-section-title">Specifications</div>'
    '<div class="pdp-spec-row"><span class="pdp-spec-label">Material</span><span class="pdp-spec-value">Grease (Lanolin, Silicone) Fluid</span></div>'
    '<hr class="pdp-divider">'
    '<div class="pdp-section-title">Compatible Models</div>'
    '<div class="pdp-compat-group"><p class="pdp-compat-cat">Forestry Products</p><p class="pdp-compat-models">FM528, FM528 LL</p></div>'
    '<div class="pdp-compat-group"><p class="pdp-compat-cat">Excavator</p><p class="pdp-compat-models">320, 320D L, 320D, 323 GC, 323GC, 323</p></div>'
    '<hr class="pdp-divider">'
    '<div class="pdp-cta">'
    '<button class="check-price-btn" type="button">Check Price</button>'
    '<a href="#" class="login-link" onclick="return false;">Login to view your customer price</a>'
    '</div>'
    '<div class="pdp-links"><a href="#" onclick="return false;">Warranty Information</a><a href="#" onclick="return false;">Return Policy</a></div>'
    '</div>'
)

# diagrams section
diag_slides_html = ""
for i, (label, parts_list) in enumerate(DIAGRAMS):
    active = ' active' if i == 0 else ''
    slide = '<div class="diagram-slide' + active + '">'
    slide += '<div class="diagram-img-area">' + DIAG_SVGS[i] + '</div>'
    slide += '<div class="diagram-parts-list"><div class="diagram-parts-title">' + label + '</div>'
    for j, (pn, nm) in enumerate(parts_list):
        slide += (
            '<div class="diagram-part-row">'
            '<span class="dpr-num">' + str(j+1) + '</span>'
            '<div class="dpr-thumb"><img src="' + NO_IMG + '" alt="" width="24" height="24"></div>'
            '<div class="dpr-info"><span class="dpr-partnum">' + pn + '</span><span class="dpr-partname">' + nm + '</span></div>'
            '</div>'
        )
    slide += '</div></div>'
    diag_slides_html += slide

diag_dots_html = "".join(
    '<button class="diag-dot' + (' active' if i == 0 else '') + '" data-dot="' + str(i) + '" type="button" aria-label="Diagram ' + str(i+1) + '"></button>'
    for i in range(len(DIAGRAMS))
)

out.append('<div id="l3" class="level hidden">')
out.append(
    '<main>'
    '<div class="wrap">'
    '<nav class="breadcrumb">'
    '<a onclick="showLevel(1)">Home</a><span>/</span>'
    '<a onclick="showLevel(2)">Drivetrain</a><span>/</span>'
    '<a onclick="showLevel(2)">Other Drivetrain Components</a><span>/</span>'
    '<span aria-current="page">567-4399: Swing Gear bearing</span>'
    '</nav>'
    '<div class="product-section">'
    + fbt_sidebar_html
    + prod_images_html
    + prod_info_html +
    '</div>'
    '<div class="diagram-section">'
    '<div class="diagram-section-hdr"><h2>Diagrams</h2><span class="diagram-count">(' + str(len(DIAGRAMS)) + ')</span></div>'
    '<div class="diagram-window" id="diagramWindow">'
    '<button class="diagram-nav diagram-nav-prev" id="diagPrev" type="button" aria-label="Previous">&#8249;</button>'
    '<div id="diagSlides" style="display:flex;flex:1;overflow:hidden;">' + diag_slides_html + '</div>'
    '<button class="diagram-nav diagram-nav-next" id="diagNext" type="button" aria-label="Next">&#8250;</button>'
    '</div>'
    '<div class="diagram-indicator">' + diag_dots_html + '</div>'
    '</div>'
    '</div>'
    '</main>'
)
out.append('</div>') # l3

# ── QTY MODAL ─────────────────────────────────────────────────────────────────
out.append(
    '<div class="qty-modal-overlay" id="qtyModal">'
    '<div class="qty-modal">'
    '<button class="qty-modal-close" id="qtyModalClose" type="button">&#215;</button>'
    '<div class="qty-modal-img-area"><img id="qtyModalImg" src="" alt="" width="110" height="110"></div>'
    '<div class="qty-modal-body">'
    '<span class="qty-modal-num" id="qtyModalNum"></span>'
    '<p class="qty-modal-name" id="qtyModalName"></p>'
    '<div class="qty-input-row"><label for="qtyInput">Qty:</label><input class="qty-input" id="qtyInput" type="number" min="1" value="1"></div>'
    '<div class="qty-modal-actions">'
    '<button class="qty-cancel-btn" id="qtyCancelBtn" type="button">Cancel</button>'
    '<button class="qty-confirm-btn" id="qtyConfirmBtn" type="button">Add to Cart</button>'
    '</div>'
    '</div>'
    '</div>'
    '</div>'
)

# ── FOOTER ────────────────────────────────────────────────────────────────────
out.append(
    '<footer class="site-footer">'
    '<div class="social-row" aria-label="Social media">'
    '<a href="#" class="soc-icon" aria-label="Facebook" onclick="return false;"><svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>'
    '<a href="#" class="soc-icon" aria-label="X" onclick="return false;"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>'
    '<a href="#" class="soc-icon" aria-label="LinkedIn" onclick="return false;"><svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg></a>'
    '<a href="#" class="soc-icon" aria-label="YouTube" onclick="return false;"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.95-1.96C18.88 4 12 4 12 4s-6.88 0-8.59.46a2.78 2.78 0 0 0-1.95 1.96A29 29 0 0 0 1 12a29 29 0 0 0 .46 5.58A2.78 2.78 0 0 0 3.41 19.6C5.12 20 12 20 12 20s6.88 0 8.59-.46a2.78 2.78 0 0 0 1.95-1.95A29 29 0 0 0 23 12a29 29 0 0 0-.46-5.58z"/><polygon points="9.75 15.02 15.5 12 9.75 8.98 9.75 15.02" fill="#FFCD11"/></svg></a>'
    '<a href="#" class="soc-icon" aria-label="Instagram" onclick="return false;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.5" fill="currentColor" stroke="none"/></svg></a>'
    '</div>'
    '<p class="footer-copy">&copy; 2026 Caterpillar. All Rights Reserved.</p>'
    '<p class="footer-legal">About Cat<span class="pipe">|</span>Site Map<span class="pipe">|</span>Cookie Settings<span class="pipe">|</span>Do Not Sell or Share My Personal Information<span class="pipe">|</span>Legal Terms<span class="pipe">|</span>Privacy</p>'
    '</footer>'
)

# ── AI BUTTON ─────────────────────────────────────────────────────────────────
out.append(
    '<button class="ai-btn" type="button" aria-label="Open AI assistant" id="aiBtn">'
    '<div class="ai-icon">'
    '<div class="ai-ring" id="aiRing" aria-hidden="true">'
    '<svg viewBox="0 0 164.8193 139.2278" xmlns="http://www.w3.org/2000/svg">'
    '<path fill="#ffffff" d="' + AI_RING + '"/>'
    '</svg>'
    '</div>'
    '<div class="ai-tri-fixed" aria-hidden="true">'
    '<svg viewBox="0 0 164.8193 139.2278" xmlns="http://www.w3.org/2000/svg">'
    '<path fill="#FFCD11" d="' + AI_TRI + '"/>'
    '</svg>'
    '</div>'
    '</div>'
    '</button>'
)

# ── JS ────────────────────────────────────────────────────────────────────────
out.append("""<script>
// ── Level navigation ──────────────────────────────────────────────────────
var addBtn = document.getElementById('addEquipBtn');
var ctxBtn = document.getElementById('equipContextBtn');
var levels = [document.getElementById('l1'), document.getElementById('l2'), document.getElementById('l3')];

function showLevel(n) {
  levels.forEach(function(el, i) {
    if (i + 1 === n) { el.classList.remove('hidden'); }
    else { el.classList.add('hidden'); }
  });
  if (n === 1) {
    addBtn.style.display = 'flex';
    ctxBtn.style.display = 'none';
    document.getElementById('equipDropdown').classList.remove('open');
  } else {
    addBtn.style.display = 'none';
    ctxBtn.style.display = 'flex';
  }
  window.scrollTo(0, 0);
}
// Start on L1
showLevel(1);

// ── Add Equipment dropdown ────────────────────────────────────────────────
(function(){
  var drop = document.getElementById('equipDropdown');
  var area = document.querySelector('.search-area');
  if (!addBtn || !drop) return;
  function positionDrop() {
    if (area) {
      var r = area.getBoundingClientRect();
      drop.style.left = r.left + 'px';
      drop.style.width = r.width + 'px';
    }
  }
  addBtn.addEventListener('click', function(e) {
    e.stopPropagation();
    var wasOpen = drop.classList.contains('open');
    drop.classList.toggle('open');
    if (!wasOpen) { positionDrop(); var s = document.getElementById('dropSerial'); if (s) s.focus(); }
  });
  document.addEventListener('click', function(e) {
    if (!drop.contains(e.target) && e.target !== addBtn) drop.classList.remove('open');
  });
  var addConfirm = document.getElementById('dropAddBtn');
  if (addConfirm) addConfirm.addEventListener('click', function() { drop.classList.remove('open'); });
  window.addEventListener('resize', function() { if (drop.classList.contains('open')) positionDrop(); });
})();

// ── Hover dropdowns (cat-app, lang, account) ──────────────────────────────
(function(){
  var allMenus = [];
  function dropdown(wrapSel, menuSel) {
    var wrap = document.querySelector(wrapSel), menu = document.querySelector(menuSel);
    if (!wrap || !menu) return;
    allMenus.push(menu);
    var t;
    function show() { clearTimeout(t); allMenus.forEach(function(m){if(m!==menu)m.classList.remove('open');}); menu.classList.add('open'); }
    function hide() { t = setTimeout(function(){ menu.classList.remove('open'); }, 0); }
    wrap.addEventListener('mouseenter', show); wrap.addEventListener('mouseleave', hide);
    menu.addEventListener('mouseenter', show); menu.addEventListener('mouseleave', hide);
  }
  dropdown('.cat-wrap', '.cat-app-menu');
  dropdown('.lang-wrap', '.lang-menu');
  dropdown('.acct-wrap', '.acct-menu');
})();

// ── Logo spin ─────────────────────────────────────────────────────────────
(function(){
  var logo = document.querySelector('.cat-logo img');
  if (!logo) return;
  var done = false;
  function spin() { logo.style.animation = 'none'; void logo.offsetWidth; done = false; logo.style.animation = 'logoSpin 1.2s linear forwards'; }
  logo.addEventListener('animationend', function() { done = true; });
  logo.addEventListener('mouseenter', function() { if (done) spin(); });
  spin();
})();

// ── AI button ─────────────────────────────────────────────────────────────
(function(){
  var btn = document.getElementById('aiBtn'), ring = document.getElementById('aiRing');
  if (!btn || !ring) return;
  var hov = false, ad = false;
  ring.style.animation = 'ringLoad 1.2s linear forwards';
  ring.addEventListener('animationend', function h() {
    ring.removeEventListener('animationend', h);
    ring.style.animation = 'none'; ring.style.transform = 'rotate(0deg)'; ad = true;
    if (hov) ring.style.animation = 'ringHover 0.8s linear infinite';
  });
  btn.addEventListener('mouseenter', function() { hov = true; if (ad) ring.style.animation = 'ringHover 0.8s linear infinite'; });
  btn.addEventListener('mouseleave', function() { hov = false; if (ad) { ring.style.animation = 'none'; ring.style.transform = 'rotate(0deg)'; } });
})();

// ── Fit banner dismiss ────────────────────────────────────────────────────
var fitBannerClose = document.getElementById('fitBannerClose');
if (fitBannerClose) fitBannerClose.addEventListener('click', function() {
  var w = document.getElementById('fitBannerWrap'); if (w) w.hidden = true;
});

// ── Type chips (visual only) ──────────────────────────────────────────────
document.querySelectorAll('.type-chip').forEach(function(chip) {
  chip.addEventListener('click', function() {
    document.querySelectorAll('.type-chip').forEach(function(c){ c.classList.remove('active'); });
    chip.classList.add('active');
  });
});

// ── Cart modal ────────────────────────────────────────────────────────────
var cartCount = 0;
function openQtyModal(name, num, imgSrc, isReal) {
  var modal = document.getElementById('qtyModal');
  var img = document.getElementById('qtyModalImg');
  document.getElementById('qtyModalNum').textContent = num;
  document.getElementById('qtyModalName').textContent = name;
  img.src = imgSrc;
  img.style.mixBlendMode = isReal ? 'multiply' : 'normal';
  document.getElementById('qtyInput').value = 1;
  modal.classList.add('open');
}
document.getElementById('qtyModalClose').addEventListener('click', function() {
  document.getElementById('qtyModal').classList.remove('open');
});
document.getElementById('qtyCancelBtn').addEventListener('click', function() {
  document.getElementById('qtyModal').classList.remove('open');
});
document.getElementById('qtyConfirmBtn').addEventListener('click', function() {
  var qty = parseInt(document.getElementById('qtyInput').value, 10) || 1;
  cartCount += qty;
  var badge = document.getElementById('cartBadge');
  badge.textContent = cartCount;
  badge.classList.add('visible');
  document.getElementById('qtyModal').classList.remove('open');
});
document.getElementById('qtyModal').addEventListener('click', function(e) {
  if (e.target === this) this.classList.remove('open');
});

// ── Diagram navigation ────────────────────────────────────────────────────
(function(){
  var slides = document.querySelectorAll('.diagram-slide');
  var dots = document.querySelectorAll('.diag-dot');
  var prev = document.getElementById('diagPrev');
  var next = document.getElementById('diagNext');
  var cur = 0, total = slides.length;
  function show(n) {
    slides.forEach(function(s,i){ s.classList.toggle('active', i===n); });
    dots.forEach(function(d,i){ d.classList.toggle('active', i===n); });
    if (prev) prev.disabled = (n===0);
    if (next) next.disabled = (n===total-1);
    cur = n;
  }
  show(0);
  if (prev) prev.addEventListener('click', function(){ if(cur>0) show(cur-1); });
  if (next) next.addEventListener('click', function(){ if(cur<total-1) show(cur+1); });
  dots.forEach(function(d){ d.addEventListener('click', function(){ show(parseInt(d.dataset.dot,10)); }); });
})();

// ── Thumb clicks ──────────────────────────────────────────────────────────
document.querySelectorAll('.thumb').forEach(function(t) {
  t.addEventListener('click', function() {
    document.querySelectorAll('.thumb').forEach(function(x){ x.classList.remove('active'); });
    t.classList.add('active');
  });
});
</script>""")

html = "\n".join(out)
with open(OUTFILE, 'w') as f:
    f.write(html)
print("Written: {}KB to {}".format(len(html)//1024, OUTFILE))
