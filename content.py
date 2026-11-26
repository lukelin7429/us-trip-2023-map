# ---------------- days ----------------
DAYS=[
 (0,'8/22','TUE · 週二','台北 → 舊金山 → 芝加哥','Taipei → San Francisco → Chicago',
  '早上到舊金山，再飛芝加哥，在 O\'Hare 機場過夜轉機。','A morning arrival in San Francisco, then on to Chicago for an overnight connection at O\'Hare.'),
 (0,'8/23','WED · 週三','芝加哥 → Albany','Chicago → Albany',
  '早班機飛紐約州首府 Albany，下午在 Colonie 的公園散步。接下來兩天待在 Albany 一帶。','An early flight to Albany, the capital of New York State, and an afternoon walk in a park in Colonie. The next two days were spent around Albany.'),
 (1,'8/25','FRI · 週五','開車南下紐約市','The drive down to New York City',
  '沿 87 號州際公路往南開大約 240 公里，傍晚在 Yonkers 的韓國超市買到台南關廟麵。在紐約這幾天住在 Bronx（不標位置）。','About 240 kilometers south on I-87, with a stop at a Korean supermarket in Yonkers that sells noodles from Guanmiao, Tainan. The base for the New York days was the Bronx (location not marked).'),
 (1,'8/26','SAT · 週六','華盛頓大橋、中央公園','The George Washington Bridge and Central Park',
  '從哥倫布圓環走進中央公園，看 Bow Bridge 和草莓園，傍晚到東河邊。','Into Central Park from Columbus Circle, past Bow Bridge and Strawberry Fields, and over to the East River in the evening.'),
 (1,'8/27','SUN · 週日','紐澤西、東河渡輪、世貿遺址、史坦頓島渡輪','New Jersey, the East River ferry, the 9/11 Memorial, and the Staten Island Ferry',
  '早上過華盛頓大橋到紐澤西 Cranford，回曼哈頓後搭渡輪沿東河南下，走華爾街到世貿遺址，傍晚來回史坦頓島渡輪看自由女神。','Across the George Washington Bridge to Cranford, New Jersey, then back to Manhattan for a ferry down the East River, a walk along Wall Street to the 9/11 Memorial, and a round trip on the Staten Island Ferry past the Statue of Liberty.'),
 (1,'8/28','MON · 週一','中央車站、哈林、洋基球場、布魯克林、康尼島、時代廣場','Grand Central, Harlem, Yankee Stadium, Brooklyn, Coney Island, Times Square',
  '一天跑遍四個區：哈林的阿波羅劇院、Bronx 的洋基球場、皇后區的河岸、布魯克林大橋下和康尼島，最後回到中城。','Four boroughs in one day: the Apollo in Harlem, Yankee Stadium in the Bronx, the Queens waterfront, Brooklyn Bridge Park and Coney Island, and back to Midtown.'),
 (1,'8/29','TUE · 週二','帝國大廈、自由女神遊船、唐人街、世貿一號大樓','Empire State Building, a harbor cruise, Chinatown, One World Observatory',
  '早上上帝國大廈，中午從南街海港搭船繞自由女神，下午逛唐人街，傍晚上世貿一號大樓的觀景台。','The Empire State Building in the morning, a boat around the Statue of Liberty from South Street Seaport at midday, Chinatown in the afternoon, and One World Observatory in the evening.'),
 (1,'8/30','WED · 週三','古根漢美術館、中央公園、自然史博物館','The Guggenheim, Central Park, and the Museum of Natural History',
  '博物館大道上的古根漢，穿過中央公園，到對面的美國自然史博物館看恐龍和藍鯨。','The Guggenheim on Museum Mile, across Central Park, and the dinosaurs and the blue whale at the American Museum of Natural History.'),
 (2,'8/31','THU · 週四','紐約 → Albany → Worcester → 波士頓','New York → Albany → Worcester → Boston',
  '8/31 先開回 Albany，9/1 再往東經過 Worcester 到劍橋。在波士頓這幾天住在劍橋（不標位置）。','Back to Albany on 8/31, then east through Worcester to Cambridge on 9/1. The base for the Boston days was Cambridge (location not marked).'),
 (2,'9/2','SAT · 週六','安角：Rockport 與 Gloucester','Cape Ann: Rockport and Gloucester',
  '往北開到海邊的安角，看 Halibut Point 的採石場和大西洋，再到 Gloucester 的漁人紀念碑。','North to Cape Ann for the old granite quarry and the Atlantic at Halibut Point, then the Fishermen\'s Memorial in Gloucester.'),
 (2,'9/3','SUN · 週日','哈佛、Charles 河、科學博物館','Harvard, the Charles River, and the Museum of Science',
  '早上走哈佛園區，下午沿 Charles 河走，最後到科學博物館。','Harvard Yard in the morning, a walk along the Charles in the afternoon, and the Museum of Science.'),
 (2,'9/4','MON · 週一','MIT、哈佛商學院、波士頓公園、自由之路','MIT, Harvard Business School, the Public Garden, and the Freedom Trail',
  '勞動節。從 MIT 走到哈佛商學院和哈佛廣場，下午到 Brookline 的 Larz Anderson 公園，傍晚走波士頓公園、老市政廳、昆西市場，在港邊看夕陽。','Labor Day. From MIT to Harvard Business School and Harvard Square, Larz Anderson Park in Brookline in the afternoon, then the Public Garden, Old City Hall, Quincy Market, and sunset on the harbor.'),
 (2,'9/5','TUE · 週二','波士頓市中心、Back Bay','Downtown Boston and Back Bay',
  '從南站走到市中心，經過波士頓公園的新雕塑《The Embrace》，沿 Newbury 街到 Copley 廣場和波士頓公共圖書館。','From South Station through downtown, past the new sculpture The Embrace on the Common, and along Newbury Street to Copley Square and the Boston Public Library.'),
 (2,'9/6','WED · 週三','Malden','Malden',
  '到波士頓北邊的 Malden，華夏文化協會在這裡。','North of Boston to Malden, home of the Chinese Culture Connection.'),
 (2,'9/7','THU · 週四','Medford','Medford',
  '9/7 傍晚在 Medford 的河邊散步；9/8 留在劍橋。','An evening walk by the river in Medford on 9/7; 9/8 was a quiet day in Cambridge.'),
 (3,'9/9','SAT · 週六','波士頓 → Albany：帝國州廣場、州立博物館','Boston → Albany: Empire State Plaza and the State Museum',
  '開回 Albany，在 Latham 吃午飯，下午逛帝國州廣場和紐約州立博物館。','Back to Albany, lunch in Latham, and an afternoon at Empire State Plaza and the New York State Museum.'),
 (3,'9/10','SUN · 週日','Albany → 紐約 → 舊金山','Albany → New York → San Francisco',
  '開車南下，從 Newark 機場飛舊金山，半夜落地。','South by car, and a flight from Newark to San Francisco that landed after midnight.'),
 (3,'9/11','MON · 週一','舊金山 → 台北','San Francisco → Taipei',
  '在舊金山國際航廈轉機，搭聯合航空回台灣，9/12 到家。','A connection in the International Terminal at SFO and a United flight home, arriving 9/12.'),
]

# ---------------- stops ----------------
S=[
 (0,'tpe','','桃園機場','Taoyuan Airport',None,[],'從桃園出發飛舊金山。','Departure from Taoyuan for San Francisco.'),
 (0,'sfo','08:00','舊金山國際機場','San Francisco International (SFO)','sfo',[(0,'抵達舊金山','Arriving in San Francisco')],
  '跨過太平洋，落地時還是 8 月 22 日早上。在這裡轉國內線。','Across the Pacific and still the morning of August 22. A domestic connection here.'),
 (0,'ord','8/23 00:06','芝加哥 O\'Hare 機場','Chicago O\'Hare (ORD)','ord',[(1,'深夜的登機口','The gate after midnight'),(2,'空蕩的候機區','An empty waiting area')],
  '半夜到芝加哥，在機場等早班機。','Chicago after midnight, waiting for the morning flight.'),
 (1,'alb','07:04–10:42','Albany 國際機場','Albany International (ALB)','alb',[(3,'機上','On board'),(4,'雲上','Above the clouds'),(8,'快到 Albany','Almost to Albany'),(10,'機場的 I ♥ NY 看板','The I ♥ NY sign at the airport')],
  '早上十點半落地 Albany。','Wheels down in Albany at 10:30 a.m.'),
 (1,'lunch','13:22–13:36','Albany 午餐','Lunch in Albany','lunch823',[(14,'中餐館的午餐','Lunch at a Chinese restaurant')],
  '中午在 Albany 吃中餐。','A Chinese lunch in Albany.'),
 (1,'crossings','16:31–16:57','The Crossings 公園','The Crossings of Colonie','crossings',[(22,'公園入口','The park entrance'),(24,'林間步道','A path through the woods'),(28,'涼亭和草地','The pavilion and lawn'),(34,'退伍軍人紀念牆','The veterans memorial wall'),(35,'紀念牆的流水','Water along the memorial')],
  'Colonie 鎮上的大公園，有步道、涼亭和紀念牆。','A large town park in Colonie with trails, a pavilion, and a memorial wall.'),
 (2,'hmart','19:33–19:45','Yonkers 的 H Mart','H Mart, Yonkers','hmart',[(50,'H Mart','H Mart'),(51,'台南關廟麵','Guanmiao noodles from Tainan'),(53,'關廟陽春麵','Guanmiao plain noodles')],
  '進紐約市之前，在 Yonkers 的韓國超市看到台南關廟麵。','Just outside the city, noodles from Guanmiao, Tainan, on the shelf of a Korean supermarket in Yonkers.'),
 (3,'gwb','12:56','華盛頓大橋','George Washington Bridge','gwb',[(58,'車窗外的華盛頓大橋','The bridge from the car')],
  '沿 Hudson 河岸南下，經過華盛頓大橋。','Down the Hudson, past the George Washington Bridge.'),
 (3,'colcircle','14:00–14:19','哥倫布圓環','Columbus Circle','colcircle',[(64,'哥倫布圓環','Columbus Circle'),(67,'地球儀雕塑','The globe sculpture'),(65,'圓環周圍的大樓','Towers around the circle')],
  '中央公園的西南角。','The southwest corner of Central Park.'),
 (3,'cpark','14:12–16:45','中央公園','Central Park','cpark1',[(69,'公園步道','A park path'),(72,'溜冰場','The rink'),(77,'San Remo 雙塔','The San Remo towers'),(79,'Bow Bridge','Bow Bridge'),(81,'湖邊','By the Lake'),(82,'草莓園','Strawberry Fields'),(84,'公園西邊的老公寓','Old apartment houses on Central Park West')],
  '從南邊走到湖邊的 Bow Bridge，再到紀念約翰藍儂的草莓園。','North to Bow Bridge over the Lake, then Strawberry Fields, the John Lennon memorial.'),
 (3,'eastriver','17:38–17:47','東河邊','The East River','river826',[(88,'東河','The East River'),(90,'對岸的羅斯福島和皇后區','Roosevelt Island and Queens across the water')],
  '傍晚到上東城的河邊步道。','The riverside walk on the Upper East Side in the evening.'),
 (4,'gwb2','08:33','過華盛頓大橋','Across the George Washington Bridge','gwb2',[(98,'橋上','On the bridge')],
  '一早開車過橋到紐澤西。','Over the bridge to New Jersey first thing in the morning.'),
 (4,'cranford','09:10–10:25','紐澤西 Cranford','Cranford, New Jersey','cranford',[(104,'一箱箱的童書','Boxes of children\'s books'),(105,'書箱','More boxes of books'),(108,'倉庫裡','Inside the warehouse')],
  '在 Cranford 的一間倉庫，裡面堆滿一箱箱的書。','A warehouse in Cranford stacked with boxes of books.'),
 (4,'lincoln','11:33–11:48','從紐澤西看曼哈頓','Manhattan from New Jersey','lincoln',[(116,'曼哈頓天際線','The Manhattan skyline')],
  '經過 Secaucus 和 Weehawken，從林肯隧道回曼哈頓。','Through Secaucus and Weehawken, and back into Manhattan through the Lincoln Tunnel.'),
 (4,'e90','13:36–13:37','東 90 街渡輪碼頭','East 90th Street ferry landing','e90',[(122,'渡輪碼頭','The ferry landing'),(123,'等船','Waiting for the boat')],
  '在 Carl Schurz 公園旁的碼頭搭 NYC Ferry。','The NYC Ferry from the landing by Carl Schurz Park.'),
 (4,'ferry','13:47–14:30','東河渡輪','The East River ferry','ferry',[(124,'羅斯福島','Roosevelt Island'),(128,'聯合國總部','United Nations Headquarters'),(135,'皇后區大橋下','Under the Queensboro Bridge'),(137,'布魯克林大橋','The Brooklyn Bridge'),(138,'NYC Ferry','The NYC Ferry'),(140,'下船','Off the boat')],
  '沿東河一路南下，經過聯合國、皇后區大橋，在華爾街碼頭下船。','Down the East River past the United Nations and the Queensboro Bridge, off at the Wall Street pier.'),
 (4,'wallst','14:37–14:40','華爾街','Wall Street','wallst',[(145,'華爾街一帶','Around Wall Street'),(149,'窄街裡的老大樓','Old towers on narrow streets')],
  '金融區的窄街和老大樓。','Narrow streets and old towers in the Financial District.'),
 (4,'trinity','15:09–15:13','三一教堂','Trinity Church','trinity',[(152,'三一教堂','Trinity Church'),(155,'哥倫比亞大學發源地的牌子','A plaque marking where Columbia University began')],
  '百老匯大道上的哥德式教堂。','The Gothic church on Broadway.'),
 (4,'wtc','15:20–15:46','911 紀念廣場','9/11 Memorial','wtc',[(157,'世貿一號大樓','One World Trade Center'),(161,'大樓前','In front of the tower'),(164,'紀念池','A memorial pool'),(166,'刻在池邊的名字','Names on the parapet'),(170,'911 紀念館的旗子','A 9/11 Memorial & Museum banner')],
  '雙子星原址的兩座紀念池，池邊刻著罹難者的名字。','Two memorial pools in the footprints of the Twin Towers, with the names of the victims around the edges.'),
 (4,'siferry','16:24–17:54','史坦頓島渡輪','Staten Island Ferry','siferry',[(175,'Whitehall 渡輪站','Whitehall Terminal'),(183,'經過自由女神','Passing the Statue of Liberty'),(184,'自由女神','The Statue of Liberty'),(185,'澤西市','Jersey City'),(191,'回程看曼哈頓下城','Lower Manhattan on the way back')],
  '免費的橘色渡輪，來回各二十五分鐘，從船上就看得到自由女神。','The free orange ferry, about twenty-five minutes each way, with the Statue of Liberty in view.'),
 (5,'gct','07:41–07:55','中央車站','Grand Central Terminal','gct',[(196,'中央大廳','The Main Concourse'),(194,'通往大廳的長廊','A passage to the concourse')],
  '從 Bronx 搭北方線火車進城，在中央車站下車。','The Metro-North train into the city, arriving at Grand Central.'),
 (5,'apollo','09:08–09:12','哈林的阿波羅劇院','The Apollo Theater, Harlem','apollo',[(198,'阿波羅劇院','The Apollo Theater'),(201,'人行道上的 Stevie Wonder 名牌','Stevie Wonder\'s plaque on the sidewalk')],
  '125 街上的阿波羅劇院，門口人行道上有歷年巨星的名牌。','The Apollo on 125th Street, with plaques for its legends set in the sidewalk.'),
 (5,'yankee','09:37–09:46','洋基球場','Yankee Stadium','yankee',[(205,'洋基球場','Yankee Stadium'),(208,'球場外','Outside the stadium')],
  '到 Bronx 的洋基球場外面看看。','A look at Yankee Stadium in the Bronx.'),
 (5,'gantry','11:39','Gantry Plaza 州立公園','Gantry Plaza State Park','gantry',[(210,'Long Island 舊吊車','The old Long Island gantries'),(211,'對岸的曼哈頓','Manhattan across the river')],
  '皇后區長島市的河岸公園，對面就是聯合國和中城。','A riverfront park in Long Island City, Queens, facing the United Nations and Midtown.'),
 (5,'dumbo','13:00–13:06','布魯克林大橋公園','Brooklyn Bridge Park','dumbo',[(212,'Jane 的旋轉木馬','Jane\'s Carousel'),(213,'布魯克林大橋和下城','The Brooklyn Bridge and Lower Manhattan'),(215,'曼哈頓大橋','The Manhattan Bridge')],
  '布魯克林大橋和曼哈頓大橋之間的河岸，玻璃屋裡有一座老旋轉木馬。','The waterfront between the Brooklyn and Manhattan Bridges, with an old carousel in a glass pavilion.'),
 (5,'coney','14:09–14:15','康尼島','Coney Island','coney',[(216,'海灘','The beach'),(218,'康尼島海灘','On Coney Island beach')],
  '搭地鐵到布魯克林最南端的海灘和遊樂園。','The subway to the beach and amusement park at the southern tip of Brooklyn.'),
 (5,'teco','16:37–16:42','駐紐約台北經濟文化辦事處','Taipei Economic and Cultural Office in New York','teco',[(219,'中城的老大樓','An old building in Midtown'),(220,'辦事處門口','The office entrance'),(221,'門口的牌子','The sign at the door'),(223,'辦事處裡的花布牆','A floral wall inside the office')],
  '回到中城，到台北經濟文化辦事處。','Back in Midtown, a stop at the Taipei Economic and Cultural Office.'),
 (5,'times','17:00–17:15','時代廣場','Times Square','times',[(226,'時代廣場','Times Square'),(227,'看板','The billboards'),(233,'人潮裡','In the crowd')],
  '傍晚的時代廣場。','Times Square in the early evening.'),
 (5,'nypl','17:41','紐約公共圖書館','New York Public Library','nypl',[(236,'門口的石獅','A stone lion at the entrance')],
  '第五大道上的總館，門口有兩隻石獅。','The main branch on Fifth Avenue, guarded by two stone lions.'),
 (6,'ktown','08:44–08:54','韓國城','Koreatown','ktown',[(242,'32 街 Korea Way','Korea Way on 32nd Street'),(243,'韓國城的店','Shops in Koreatown')],
  '帝國大廈旁邊的 32 街。','West 32nd Street, next to the Empire State Building.'),
 (6,'esb','09:03–09:43','帝國大廈','Empire State Building','esb',[(248,'觀景台的牌子','The observatory plaque'),(251,'86 樓窗邊','At an 86th-floor window'),(254,'往南看下城','South toward Lower Manhattan'),(258,'往北看中城','North over Midtown'),(262,'中城的高樓','The towers of Midtown')],
  '上 86 樓的觀景台，往南看得到下城和自由女神，往北是中城和中央公園。','Up to the 86th-floor observatory, with Lower Manhattan and the Statue of Liberty to the south and Midtown and Central Park to the north.'),
 (6,'msg','10:24','麥迪遜廣場花園','Madison Square Garden','msg',[(268,'麥迪遜廣場花園','Madison Square Garden')],
  '賓州車站上面的體育館。','The arena above Penn Station.'),
 (6,'pier16','11:10–11:15','南街海港','South Street Seaport','pier16',[(271,'海港和老帆船','The seaport and its tall ships'),(273,'布魯克林大橋','The Brooklyn Bridge')],
  '從 16 號碼頭上船。','Boarding at Pier 16.'),
 (6,'cruise','11:35–12:16','自由女神遊船','Harbor cruise to the Statue of Liberty','cruise',[(277,'下城天際線','The Lower Manhattan skyline'),(283,'自由女神','The Statue of Liberty'),(285,'船上','On the boat'),(289,'自由女神前','With the Statue of Liberty'),(293,'回程的布魯克林大橋','The Brooklyn Bridge on the way back')],
  '繞過下城南端，在自由島前停下來，再從東河回來。','Around the tip of Manhattan, a pause off Liberty Island, and back up the East River.'),
 (6,'chinatown','13:53–16:43','唐人街','Chinatown','chinatown',[(296,'Kimlau 紀念門','The Kimlau Memorial Arch'),(297,'店招和國旗','Shop signs and flags'),(299,'中華公所','The Chinese Consolidated Benevolent Association'),(301,'廟','A temple'),(302,'曼哈頓大橋的拱門','The Manhattan Bridge arch'),(309,'唐人街的街口','A Chinatown corner')],
  '從勿街一帶走到曼哈頓大橋橋頭，街上看得到中華民國國旗和中文學校。','From the area around Mott Street to the foot of the Manhattan Bridge, with Republic of China flags and Chinese schools along the way.'),
 (6,'owo','17:21–18:02','世貿一號大樓觀景台','One World Observatory','owo',[(316,'從 100 樓往下看','Down from the 100th floor'),(317,'遠方的自由女神','The Statue of Liberty in the distance'),(318,'東河上的三座橋','Three bridges over the East River'),(321,'下城和港口','Lower Manhattan and the harbor')],
  '西半球最高的大樓，從 100 樓看港口和東河。','The tallest building in the Western Hemisphere, with the harbor and the East River below.'),
 (6,'oculus','18:16–18:20','Oculus 車站','The Oculus','oculus2',[(325,'Oculus 的地下長廊','The underground concourse'),(326,'白色的肋骨','The white ribs')],
  '世貿遺址旁的交通樞紐，像一副白色的翅膀。','The transit hub beside the World Trade Center site, shaped like white wings.'),
 (7,'gugg','12:09–13:56','古根漢美術館','Guggenheim Museum','gugg',[(327,'螺旋形的外觀','The spiral building'),(331,'中庭的螺旋坡道','The spiral ramp'),(332,'天窗','The skylight'),(360,'盧梭的畫','A painting by Henri Rousseau'),(361,'梵谷的山景','A mountain landscape by Van Gogh')],
  '萊特設計的螺旋美術館，沿著坡道一路往上看展。','Frank Lloyd Wright\'s spiral museum, seen by walking up the ramp.'),
 (7,'met','14:19–14:20','大都會博物館','The Metropolitan Museum of Art','met',[(366,'門前的噴泉','The fountain out front'),(367,'大都會博物館','The Met')],
  '沿博物館大道走到大都會博物館門口。','Down Museum Mile to the steps of the Met.'),
 (7,'cpark2','14:16–14:40','中央公園','Central Park','cpark2',[(369,'埃及方尖碑','Cleopatra\'s Needle'),(370,'大草坪','The Great Lawn'),(372,'公園裡','In the park'),(375,'眺望台城堡','Belvedere Castle')],
  '穿過公園中段，經過埃及方尖碑和大草坪。','Through the middle of the park, past Cleopatra\'s Needle and the Great Lawn.'),
 (7,'amnh','15:35–17:08','美國自然史博物館','American Museum of Natural History','amnh',[(377,'天文館的海報','A planetarium poster'),(380,'暴龍','Tyrannosaurus rex'),(381,'恐龍廳','The dinosaur hall'),(393,'非洲哺乳類展廳','The Hall of African Mammals'),(417,'藍鯨下','Under the blue whale'),(426,'海象','Walruses')],
  '恐龍廳、非洲哺乳類的立體造景，最後是海洋生物廳天花板上的藍鯨。','The dinosaur halls, the African mammal dioramas, and the blue whale hanging in the Hall of Ocean Life.'),
 (8,'mcphs','9/1 13:27–13:36','Worcester','Worcester','mcphs',[(431,'大樓裡的樓層指引','A building directory')],
  '9/1 往波士頓的路上，在 Worcester 的麻州藥學與健康科學大學停了一下。','On the way to Boston on 9/1, a stop at the Massachusetts College of Pharmacy and Health Sciences in Worcester.'),
 (9,'halibut','13:41–14:36','Halibut Point 州立公園','Halibut Point State Park','halibut',[(466,'舊採石場','The old quarry'),(472,'採石場邊','By the quarry'),(473,'禁止游泳的石碑','A No Swimming stone'),(479,'大西洋','The Atlantic'),(481,'海邊疊石','Stacked stones by the sea'),(486,'州立公園說明牌','The park sign')],
  'Rockport 北端的海岬，以前是花崗岩採石場，現在積滿雨水。','The northern tip of Rockport, once a granite quarry, now filled with rainwater.'),
 (9,'gloucester','15:52–16:27','Gloucester 漁人紀念碑','Gloucester Fishermen\'s Memorial','glou',[(488,'Pavilion 海灘','Pavilion Beach'),(491,'海邊的花','Flowers by the sea'),(494,'漁人妻子紀念碑','The Fishermen\'s Wives Memorial'),(495,'開合橋','The drawbridge'),(500,'刻著罹難漁民名字的碑','Tablets with the names of lost fishermen')],
  '美國最老的漁港之一，海邊的紀念碑刻著四百年來在海上喪生的漁民。','One of the oldest fishing ports in America. The memorial by the harbor lists fishermen lost at sea over four centuries.'),
 (9,'stagefort','18:04','Stage Fort 公園','Stage Fort Park','stagefort',[(503,'公園看出去的海','The sea from the park'),(505,'傍晚','Early evening')],
  '回程前在港邊公園看海。','A last look at the sea before heading back.'),
 (10,'harvard','11:36–12:01','哈佛大學','Harvard University','harvard',[(512,'校園裡的教堂','A church on campus'),(514,'哈佛藝術博物館','Harvard Art Museums'),(516,'哈佛園','Harvard Yard'),(520,'紅磚老樓前','By an old brick hall'),(521,'Widener 圖書館','Widener Library')],
  '哈佛園和周邊的老建築。','Harvard Yard and the old buildings around it.'),
 (10,'boathouse','14:16–14:52','Charles 河邊的船屋','A boathouse on the Charles','boathouse',[(528,'河邊','By the river'),(529,'河邊','On the riverbank'),(532,'划船練習機','Rowing machines'),(534,'船架','Racks of shells'),(536,'船屋','The boathouse')],
  '沿 Charles 河走到划船隊的船屋。','Along the Charles to a rowing boathouse.'),
 (10,'bubridge','15:51–15:58','Charles 河','The Charles River','longfellow',[(542,'帆船','Sailboats'),(544,'波士頓天際線','The Boston skyline'),(545,'橋上','On the bridge')],
  '從河上的橋看波士頓。','Boston from a bridge over the river.'),
 (10,'mos','16:18–16:20','波士頓科學博物館','Museum of Science, Boston','mos',[(549,'館內','Inside the museum'),(550,'火星地形的展示','A display on Mars landforms'),(552,'地球：水的行星','Earth, a planet of water')],
  'Charles 河口的科學博物館。','The Museum of Science at the mouth of the Charles.'),
 (11,'mit','11:07–11:18','MIT','MIT','mit',[(560,'Stata 中心','The Stata Center'),(561,'Simmons Hall','Simmons Hall'),(563,'像海綿的宿舍','The sponge-like dorm')],
  '蓋瑞設計的 Stata 中心和像海綿的 Simmons 宿舍。','Frank Gehry\'s Stata Center and the sponge-like Simmons Hall.'),
 (11,'weeks','11:26–11:28','Weeks 人行橋','Weeks Footbridge','weeks',[(570,'Charles 河','The Charles River'),(572,'河上的獨木舟','A kayak on the river')],
  '走過 Charles 河上的人行橋。','Across the footbridge over the Charles.'),
 (11,'hbs','11:31–11:41','哈佛商學院','Harvard Business School','hbs',[(576,'學生宿舍','Student housing'),(582,'校園','On campus'),(589,'Baker 圖書館','Baker Library'),(591,'校園裡的鐘','A bell on campus')],
  '河的南岸是哈佛商學院。','Harvard Business School on the south bank of the river.'),
 (11,'hsq','11:47–12:20','哈佛廣場','Harvard Square','hsq',[(606,'哈佛廣場','Harvard Square'),(614,'哈佛園的鐵門','A gate into Harvard Yard'),(618,'Coop 書店','The Coop'),(621,'約翰哈佛像','The John Harvard statue'),(622,'Widener 圖書館','Widener Library')],
  '從哈佛廣場走進哈佛園，看約翰哈佛像。','From Harvard Square into Harvard Yard to see the John Harvard statue.'),
 (11,'larz','15:05–15:43','Larz Anderson 公園','Larz Anderson Park','larz',[(657,'社區菜園','Community gardens'),(664,'池塘','The pond'),(668,'池邊的小亭子','A small temple by the pond'),(670,'柳樹','Willows')],
  'Brookline 山丘上的公園，有池塘和社區菜園。','A hilltop park in Brookline with a pond and community gardens.'),
 (11,'pubgarden','17:03–17:16','波士頓公共花園','Boston Public Garden','pubgarden',[(676,'湖邊','By the lagoon'),(680,'老樹','An old tree'),(684,'華盛頓騎馬像','The George Washington statue'),(683,'花壇','Flower beds')],
  '美國第一座公共植物園。','The first public botanical garden in the United States.'),
 (11,'freedom','17:22–17:40','自由之路：老市政廳一帶','The Freedom Trail around Old City Hall','oldcity',[(692,'州議會大廈的金頂','The gold dome of the State House'),(693,'老市政廳','Old City Hall'),(704,'舊州議會大樓','The Old State House'),(705,'1795 年的 Bell in Hand 酒館','The Bell in Hand Tavern, 1795'),(707,'酒館前','In front of the tavern')],
  '沿著自由之路，從州議會走到老市政廳和舊州議會大樓。','Along the Freedom Trail from the State House to Old City Hall and the Old State House.'),
 (11,'quincy','17:59','昆西市場','Quincy Market','quincy',[(708,'昆西市場','Quincy Market')],
  '法尼爾廳旁的老市場。','The old market next to Faneuil Hall.'),
 (11,'wharf','19:13–19:51','波士頓港邊','The Boston waterfront','wharf',[(712,'長碼頭','Long Wharf'),(717,'港邊的浮標牆','A wall of buoys on the wharf'),(721,'港灣的帆船','Sailboats in the harbor'),(725,'入夜的港口','The harbor after dark')],
  '在長碼頭一帶看太陽下山。','Sunset around Long Wharf.'),
 (11,'cityhall','20:28–20:49','波士頓市政廳','Boston City Hall','cityhall',[(727,'保羅．李維爾故居的牌子','The Paul Revere House sign'),(728,'夜裡的市政廳','City Hall at night')],
  '經過北區的保羅．李維爾故居，回到政府中心。','Past the Paul Revere House in the North End and back to Government Center.'),
 (12,'southst','10:37','南站','South Station','southst',[(736,'南站大廳','The South Station concourse')],
  '從南站開始走。','Starting out at South Station.'),
 (12,'dtx','10:44–11:01','市中心與劇院區','Downtown Crossing and the Theatre District','dtx',[(740,'市中心','Downtown Crossing'),(742,'BOSTON 壁畫','A BOSTON mural'),(743,'波士頓歌劇院','The Boston Opera House')],
  '市中心的商店街和老劇院。','The shopping streets and old theaters of downtown.'),
 (12,'embrace','12:34–12:38','《The Embrace》雕塑','The Embrace','embrace',[(749,'The Embrace','The Embrace'),(752,'雕塑和公園','The sculpture and the Common')],
  '2023 年初揭幕，紀念金恩博士夫婦在波士頓相遇。','Unveiled earlier in 2023 to honor Martin Luther King Jr. and Coretta Scott King, who met in Boston.'),
 (12,'pubg2','12:47–12:52','波士頓公共花園','Boston Public Garden','pubg2',[(755,'公共花園大門','The Public Garden gate'),(760,'湖','The lagoon')],
  '再走一次公共花園。','Another walk through the Public Garden.'),
 (12,'newbury','13:02–13:07','Newbury 街','Newbury Street','newbury',[(763,'中央公理會教堂','Central Congregational Church'),(766,'Back Bay 的紅磚排屋','Brick row houses in Back Bay')],
  'Back Bay 的商店街和紅磚排屋。','The shops and brick row houses of Back Bay.'),
 (12,'copley','13:12–13:29','Copley 廣場與公共圖書館','Copley Square and the Boston Public Library','copley',[(768,'三一教堂','Trinity Church'),(769,'老南教堂','Old South Church'),(772,'圖書館中庭','The library courtyard'),(776,'圖書館新館','The library\'s newer wing')],
  '廣場兩邊是三一教堂和美國最早的大型公共圖書館。','Trinity Church on one side of the square and the first large free public library in America on the other.'),
 (13,'malden','12:39–16:01','Malden 市中心','Malden Center','malden',[(780,'Malden 市中心','Malden Center'),(781,'市政府大廳','The City Hall lobby'),(790,'街上的老銀行','An old bank building'),(794,'「華夏文化協會」字幅','The Chinese Culture Connection scroll')],
  '下午都在 Malden。','The afternoon in Malden.'),
 (14,'medford','17:02–18:10','Medford 的河邊公園','A riverside park in Medford','medford',[(847,'柳樹','A willow'),(849,'河邊','By the river'),(851,'傍晚的河岸','The riverbank in the evening'),(853,'夕陽下的河','The river at sunset')],
  '傍晚在 Medford 的河邊公園散步。','An evening walk in a riverside park in Medford.'),
 (15,'latham','12:03–12:59','Latham 午餐','Lunch in Latham','latham99',[(859,'餐館','The restaurant'),(861,'午餐','Lunch')],
  '回到 Albany 一帶，先在 Latham 吃午飯。','Back in the Albany area, lunch in Latham first.'),
 (15,'esp','15:40–16:09','帝國州廣場','Empire State Plaza','esp',[(862,'「蛋」表演廳','The Egg'),(870,'州議會大廈','The State Capitol'),(876,'I ♥ NY','I ♥ NY'),(877,'倒影池','The reflecting pool'),(880,'紀念雕塑','A memorial sculpture')],
  '州政府大廣場和議會大廈。2025 年再來時，進了議會大廈參觀。','The state government plaza and the Capitol. On the 2025 trip, I went inside the Capitol.'),
 (15,'nysm','15:57–16:38','紐約州立博物館','New York State Museum','nysm',[(882,'老消防馬車','An old horse-drawn fire engine'),(883,'911 當天的紐約消防救護車','An FDNY ambulance from September 11'),(885,'老教室','An old classroom'),(887,'自由女神的老版畫','An old print of the Statue of Liberty'),(893,'老計程車','An old taxi'),(896,'老地鐵站','An old subway entrance')],
  '免費的州立博物館，有 911 世貿的展區，也有紐約的老街景。','The free state museum, with a World Trade Center gallery and scenes from old New York.'),
 (16,'ewr','','Newark 機場','Newark Liberty International (EWR)','ewr',[],
  '從 Newark 機場搭聯合航空飛舊金山。','A United flight from Newark to San Francisco.'),
 (17,'sfo2','01:11–11:18','舊金山國際機場','San Francisco International (SFO)','sfo2',[(899,'半夜到舊金山','San Francisco after midnight'),(900,'要飛回台灣的飛機','The plane home to Taiwan')],
  '半夜一點落地，等到中午轉機回台灣。','Landed at 1 a.m. and waited until midday for the flight home.'),
]
TIME_FIX=set(range(888,897))  # these camera times were saved in Taipei time; shift back 12 hours

AIR={'TPE':(25.0797,121.2342),'SFO':(37.6152,-122.3900),'ORD':(41.9786,-87.9048),'ALB':(42.7483,-73.8017),'EWR':(40.6895,-74.1745)}
def flight(a,b): pts,km=gc(AIR[a],AIR[b],48); return pts,round(km)
L=[]
def car(day,after,key,i0,i1,zh,en):
    r=R[key]
    L.append((day,after,'car',r['coords'] if i0 is None else None,zh,en,r['km'] if i0 is None else sum(r['legs'][i0:i1]),key,i0,i1))
def straight(day,after,mode,pts,zh,en):
    km=sum(math.dist(P(*a),P(*b)) for a,b in zip(pts,pts[1:]))/K
    L.append((day,after,mode,pts,zh,en,round(km,1),None,None,None))
def fl(day,after,a,b,zh,en):
    pts,km=flight(a,b); L.append((day,after,'flight' if a!='TPE' and b!='TPE' else 'intl',pts,zh,en,km,None,None,None))
W=lambda *ks:[ll(k) if isinstance(k,str) else k for k in ks]

fl(0,'tpe','TPE','SFO','桃園 → 舊金山','Taipei → San Francisco')
fl(0,'sfo','SFO','ORD','舊金山 → 芝加哥','San Francisco → Chicago')
fl(1,'start','ORD','ALB','芝加哥 → Albany','Chicago → Albany')
car(1,'alb','d1',0,1,'機場 → 午餐','Airport → lunch')
car(1,'lunch','d1',1,2,'→ The Crossings','To The Crossings')
car(2,'start','d2',0,1,'I-87 南下，Albany → Yonkers','South on I-87, Albany → Yonkers')
car(2,'hmart','d2',1,2,'Yonkers → Bronx','Yonkers → the Bronx')
car(3,'start','d3',None,None,'Bronx → 華盛頓大橋','The Bronx → George Washington Bridge')
straight(3,'gwb','move',W('gwb','colcircle'),'→ 哥倫布圓環','To Columbus Circle')
straight(3,'colcircle','walk',W('colcircle','cpark1'),'走進中央公園','Into Central Park')
straight(3,'cpark','move',W('cpark1','river826'),'→ 東河','To the East River')
car(4,'gwb2','d4a',None,None,'過華盛頓大橋到 Cranford','Across the bridge to Cranford')
car(4,'cranford','d4b',0,1,'Cranford → Weehawken','Cranford → Weehawken')
car(4,'lincoln','d4b',1,2,'林肯隧道回曼哈頓','Through the Lincoln Tunnel')
straight(4,'lincoln','move',W('dewitt','e90'),'→ 上東城','To the Upper East Side')
straight(4,'e90','boat',W('e90',(40.7700,-73.9440),(40.7590,-73.9580),(40.7440,-73.9700),(40.7300,-73.9720),(40.7100,-73.9780),(40.7030,-73.9950),(40.7033,-74.0060)),'NYC Ferry 東河南下','NYC Ferry down the East River')
straight(4,'ferry','walk',W((40.7033,-74.0060),'wallst','trinity'),'華爾街 → 三一教堂','Wall Street → Trinity Church')
straight(4,'trinity','walk',W('trinity','wtc'),'→ 911 紀念廣場','To the 9/11 Memorial')
straight(4,'wtc','walk',W('wtc','whitehall'),'→ Whitehall 渡輪站','To Whitehall Terminal')
straight(4,'siferry','boat',W('whitehall',(40.6900,-74.0250),(40.6650,-74.0480),(40.6437,-74.0735),(40.6650,-74.0430),(40.6920,-74.0200),'whitehall'),'史坦頓島渡輪來回','Staten Island Ferry, round trip')
straight(5,'gct','move',W('gct','apollo'),'→ 哈林','To Harlem')
straight(5,'apollo','move',W('apollo','yankee'),'→ 洋基球場','To Yankee Stadium')
straight(5,'yankee','move',W('yankee','gantry'),'→ 長島市','To Long Island City')
straight(5,'gantry','move',W('gantry','dumbo'),'→ 布魯克林','To Brooklyn')
straight(5,'dumbo','move',W('dumbo','coney'),'→ 康尼島','To Coney Island')
straight(5,'coney','move',W('coney','teco'),'→ 中城','Back to Midtown')
straight(5,'teco','walk',W('teco','times','nypl'),'→ 時代廣場 → 圖書館','To Times Square and the library')
straight(6,'ktown','walk',W('ktown','esb'),'→ 帝國大廈','To the Empire State Building')
straight(6,'esb','walk',W('esb','msg'),'→ 麥迪遜廣場花園','To Madison Square Garden')
straight(6,'msg','move',W('msg','pier16'),'→ 南街海港','To South Street Seaport')
straight(6,'pier16','boat',W('pier16',(40.7000,-74.0130),(40.6950,-74.0260),(40.6920,-74.0420),(40.6990,-74.0180),(40.7030,-73.9970),(40.7048,-74.0020)),'自由女神遊船','Harbor cruise')
straight(6,'cruise','move',W('pier16','chinatown'),'→ 唐人街','To Chinatown')
straight(6,'chinatown','move',W('chinatown','owo'),'→ 世貿中心','To the World Trade Center')
car(8,'start','d8',None,None,'8/31 開回 Albany','Back to Albany on 8/31')
car(8,'start','d9',0,1,'9/1 往東到 Worcester','East to Worcester on 9/1')
car(8,'mcphs','d9',1,2,'Worcester → 劍橋','Worcester → Cambridge')
car(9,'start','d10',0,1,'劍橋 → Rockport','Cambridge → Rockport')
car(9,'halibut','d10',1,2,'→ Gloucester','To Gloucester')
car(9,'gloucester','d10',2,3,'→ Stage Fort 公園','To Stage Fort Park')
car(9,'stagefort','d10',3,4,'回劍橋','Back to Cambridge')
straight(10,'harvard','walk',W('harvard','boathouse'),'→ Charles 河','To the Charles')
straight(10,'boathouse','walk',W('boathouse','longfellow'),'沿河走','Along the river')
straight(10,'bubridge','move',W('longfellow','mos'),'→ 科學博物館','To the Museum of Science')
straight(11,'mit','walk',W('mit','weeks','hbs','hsq'),'MIT → 哈佛','MIT to Harvard')
straight(11,'hsq','move',W('hsq','larz'),'→ Brookline','To Brookline')
straight(11,'larz','move',W('larz','pubgarden'),'→ 波士頓市區','Into Boston')
straight(11,'pubgarden','walk',W('pubgarden','common','oldcity','bellinhand','quincy'),'自由之路','The Freedom Trail')
straight(11,'quincy','walk',W('quincy','wharf'),'→ 港邊','To the waterfront')
straight(11,'wharf','walk',W('wharf','revere','cityhall'),'→ 北區 → 市政廳','North End to City Hall')
straight(12,'southst','walk',W('southst','dtx','embrace','pubg2','newbury','copley'),'南站 → Copley 廣場','South Station to Copley Square')
car(13,'start','d13',None,None,'劍橋 → Malden','Cambridge → Malden')
car(15,'start','d16',0,1,'I-90 西行，劍橋 → Latham','West on I-90, Cambridge → Latham')
car(15,'latham','d16',1,2,'→ Albany 市中心','To downtown Albany')
straight(15,'esp','walk',W('esp','nysm'),'→ 州立博物館','To the State Museum')
car(16,'start','d17',None,None,'Albany → Newark 機場','Albany → Newark Airport')
fl(16,'ewr','EWR','SFO','Newark → 舊金山','Newark → San Francisco')
fl(17,'sfo2','SFO','TPE','聯合航空 舊金山 → 桃園','United, San Francisco → Taipei')

LAB=[('紐約州',43.1,-75.6,'big',90000,7000),('麻州',42.25,-72.2,'big',90000,7000),('加州',37.2,-119.6,'big',90000,7000),('伊利諾州',40.2,-89.3,'big',90000,7000),('紐澤西',40.1,-74.6,'big',90000,5000),
 ('太平洋',31.0,-122.5,'sea',90000,3000),('大西洋',39.6,-71.5,'sea',90000,3000),
 ('舊金山',37.95,-122.42,'',90000,3000),('芝加哥',42.15,-87.63,'',90000,3000),('Albany',42.90,-73.76,'',90000,2500),('波士頓',42.15,-71.06,'',90000,2500),('紐約市',40.45,-73.95,'',90000,2500),
 ('Albany',42.6526,-73.7562,'',2400,100),('Troy',42.7284,-73.6918,'',2400,100),('Colonie',42.7179,-73.8335,'',1200,60),('Latham',42.7470,-73.7590,'',900,60),
 ('曼哈頓',40.7831,-73.9712,'',2400,150),('Bronx',40.8448,-73.8648,'',2400,150),('布魯克林',40.6500,-73.9500,'',2400,150),('皇后區',40.7282,-73.8000,'',2400,150),('史坦頓島',40.5795,-74.1502,'',2400,150),('澤西市',40.7178,-74.0731,'',1400,100),('Yonkers',40.9312,-73.8988,'',2400,150),('Cranford',40.6584,-74.2999,'',1400,100),('Hudson 河',40.8200,-73.9640,'sea',700,80),('東河',40.7600,-73.9560,'sea',500,60),('上紐約灣',40.6700,-74.0450,'sea',1200,150),
 ('波士頓',42.3601,-71.0589,'',2400,100),('劍橋',42.3736,-71.1097,'',1500,100),('Brookline',42.3318,-71.1212,'',1500,100),('Malden',42.4251,-71.0662,'',1500,100),('Medford',42.4184,-71.1062,'',1500,100),('Rockport',42.6556,-70.6203,'',2400,100),('Gloucester',42.6159,-70.6620,'',2400,100),('麻薩諸塞灣',42.40,-70.80,'sea',2400,200),('Worcester',42.2626,-71.8023,'',2400,100)]
SEG_STATS={'days':21,'photos':1418}
