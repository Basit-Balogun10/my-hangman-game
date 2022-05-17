# HANGMAN GAME
from random import choice
from os import system
import pickle
import json

exit_game = False
while not exit_game:
    exit_game_option = input('EXIT GAME?   ')
    if exit_game_option in ['y', 'Y']:
        exit_game = True
        break
    Nouns = (
        '	fifth	scale arithmetic	finger	seashorebadge	flock	sidewalk frame	sleet furniture	smoke battle	bathtub beast	ghost	nose beggar	governor brain		stage bubble	hope	station bucket	income	throat plant	island	throne cannon	jeans	title 	judge	toothbrush jewellery	lamp	umbrella cloth	marble	underwear	month	vacation coast	north south  east west	crate	ocean	 cream	patch	riddle 	plane	scale	playground	visitor earthquake	 voyage riddle	year ')

    Adjectives = (
        'abundant	delightful	high nutritious	square adorable	dirty	hollow	obedient	steep agreeable	drab	hot	obnoxious	sticky alive	dry	hot	odd	straight angry	dusty	huge	old-fashioned	strong beautiful	eager	icy	orange	substantial better	early	immense	panicky	sweet bewildered	easy	important	petite	swift big	elegant	inexpensive	plain	tall bitter	embarrassed	itchy	powerful	tart black	empty	jealous	prickly	tasteless blue	faint	jolly	proud	teeny boiling	faithful	juicy	puny	teeny-tiny brave	famous	kind	purple	tender breeze	fancy	large	purring	thankful broad	fast	late	quaint	thoughtless broken	fat	lazy	quick	tiny bumpy	few	light	quiet	ugliest calm	fierce	little	rainy	ugly careful	filthy	lively	rapid	uneven chilly	flaky	long	red	uninterested chubby	flat	loose	relieved	unsightly clean	fluffy	loud	repulsive	uptight clever	freezing	low	rich	vast clumsy	fresh	lumpy	rotten	victorious cold	full	magnificent	round	warm colossal	gentle	mammoth	salty	weak cool	gifted	many	scary	wet creepy	gigantic	massive	scrawny	west crooked	glamorous	melted	screeching	whispering cuddly	gray	messy	shallow	white curly	greasy	miniature	short	wide curved	great	modern	shy	wide-eyed damaged	green	mushy	silly	witty damp	grumpy	mysterious	skinny	wooden dead	handsome	narrow	slow	worried deafening	happy	nervous	small	wrong deep	heavy	nice	soft	yellow defeated	helpful	noisy	sparkling	young delicious	helpless	numerous	sparse	yummy')

    Verbs = (
        'question	add	itch reach	allow	jog rinse	bake	jump run	bang	jump scatter	call	kick stay	chase	knit swim	damage	land talk	drop	lock turn	end	march untie	escape	mix use	fasten	name vanish	fix	notice visit	gather	obey walk	grab	open work	hang	pass yawn	hug yell	imagine	promise return reject praise confuse convince pray play hail break clear drag elevate emerge fall fill great grant hype hope hire jilt knock kill love like prank pamper read ring stand save trick yield')

    Adverbs = (
        'actually	famously	jaggedly	perfectly	smoothly almost	far	jealously	playfully	softly always	fast	joyfully	politely	solidly angrily	fatally	justly	poorly	sometimes  annually	ferociously	keenly	positively	soon anxiously	foolishly	kindly	powerfully	speedily arrogantly	fortunately	knowingly	promptly	sternly awkwardly	frankly	lazily	properly	strictly badly	frantically	less	quicker	successfully bashfully	freely	lightly	quickly	suddenly beautifully	fully	likely	quietly	surprisingly blindly	furiously	limply	rapidly	suspiciously boldly	generally	lively	rarely	sweetly bravely	generously	loosely	readily	swiftly briefly	gently	loudly	really	sympathetically brightly	gladly	lovingly	reassuringly	tenderly briskly	gleefully	madly	recklessly	terribly busily	gracefully	merrily	regularly	thankfully calmly	gratefully	miserably	reluctantly	thoughtfully carefully	greatly	mockingly	repeatedly	tightly carelessly	greedily	monthly	rigidly	tomorrow certainly	happily	more	roughly	too cheerfully	hastily	mortally	rudely	truly clearly	healthily	mostly	sadly	truthfully cleverly	heavily	naturally	safely	upbeat closely	helpfully	nearly	searchingly	upward coolly	helplessly	neatly	sedately	urgently courageously	highly	nervously	seemingly	vainly cruelly	honestly	never	seldom	vastly curiously	hopelessly	nicely	selfishly	very daintily	hourly	noisily	separately	viciously deeply	hungrily	normally	seriously	violently delightfully	immediately	not	shakily	warmly dimly	innocently	oddly	sharply	weakly dreamily	instantly	often	sheepishly	well easily	intensely	only	shrilly	wetly excitedly	intently	openly	shyly	wildly extremely	interestingly	painfully	silently	wisely fairly	inwardly	partially	sleepily	worriedly faithfully	irritably	patiently	slowly	wrongly')

    Food_Fruits = (
        'almond appetizer apple apricot avocado bacon banana barbecue barley basil beans beef berry biscuit bitter blackberry blueberry boysenberry bread brisket breakfast broccoli brownie buns butter bean cake candy caramel carrot cashew cassava calorie cauliflower cheese cheesecake cherry chicken chili chips chocolate chutney citrus clam coconut coffee cod cornflakes cornmeal corn cookie crab crackers cream crepe crisp cucumber cupcake curry custard dairy dessert carbohydrate protein fat oil mineral vitamin roughage fibre dairy dates dessert diet digest digestive digestivesystem dough lunch dinner doughnut egg fast eat fast feast feed fig flour foodstuff fork freezer refrigerator fry frenchfries garlic ginger gingerbread grain legume cereal grape grapefruit greentea greenbean guava gyro hamburger hash herbs honey honeydew hot hotdog hotsauce hunger hungry ice icecream icedtea icing jam jelly jackfruit juice junk kebab ketchup kettle kitchen kiwi knife kettle lard legumes lemon lemonade lentils lettuce liver loaf lollipop lobster lunchbox macaroni maize mango margarine marshmallow mayonnaise meat meatloaf melon menu meringue milk milkshake millet nutrient mint molasses mushroom mug mussels mustard mutton napkin nectar nectarine nibble noddles nourish nourishment  omelet nut nutmeg nutrient nutrition nutritious oats oatmeal okra olive onion orange order oregano oyster pan pancake pawpaw pasta pastry confectionery pea peach peanut pear pepper pepperoni pickle picnic pie pineapple pizza plate plum pomegranate pop popcorn pork pot potato pudding pumpkin quiche quinoa radish raspberry ravioli recipe  refreshment restaurant rice roast roll rye salad saffron salmon salsa salt sandwich sauce scrambled seeds shrimp slice smoked snack soda sorghum soup sour soursop  soy soybeans spaghetti spicy spinach spoon sprouts squid stew stomach stove straw strawberry sugar supper sweet potato sweetpotato tangerine tapioca tart tea thyme toast toffee tomato tuber turkey turmeric turkey utensils vegetable vinegar vanilla waffle wafer walnut water wheat yam yeast yogurt yolk zucchini beancake beefcake eggroll watermelon chestnut')
    Food_scrape = ('digestivesystem greentea greenbean hotdog hotsauce icecream icedtea lunchbox sweetpotato')

    Sports = (
        'Ability  Accuracy  Activity  Advantage  Aggressive  Agility  Amateur  Appearances  Arena Assistance  Assistant  Athlete  Average  Awards  Awesome Balance  Ban  Beat  Beaten  Blindside  Boot  Bounceback  Broadcast  Brutal Call  Caution  Celebrate  Center  Challenge  Champion  Chances  Character  Charisma  Co-captain  Coach Comeback  Commentator  Commitment  Communication  Competition  Conference  Confidence  Confrontation  Consistent consistency Control  Cooperation  Cornerkick  Crossbar  Crowd Dangerous  Daunting  Debut  Defeat  Defender  Defense  Gamedelay  Determination  Diligent  Direction  Disappointment  Discipline  Dislocation  Dive  Division  Dominate dominant  Dramatic  Dribble  Dynamic Effective  Eligible  Encouragement  Energetic  Enthusiasm  Equipment  Esteem  Ethical  Euphoria  Exemplary  Exercise  Exhibitiongames  Experience  Fair  Fans  Field  FIFA  Fitness  Flair  Football   Foreign  Forward  Foul  Fracture  Freekick  Frenzy  Full-time  Fullback games  Gear  Goal Goalkeeper  Goalsgalore  Grudge  Half time  Hardwork  Hattrick  Header  Healthy  Hero  Hit  Improvement  Inbound  Indirectkick   Ineligible   Injuries  Instructions  Instructive  Intense  Intercepted   International Jerseys Jubilation  Jumping jump  play  Kick  Kickoff   Leadership  League  Leftwing Linesman  Lockers  Lose  Loss  Loyalty  Manager  Medication Men Mid-season  Midfielder  Motivate  Moves  Muscles  National  Negotiate  Offense  Offensive  Official  Offside  Opponent  Opportunity  Outstanding  Ovation Participation  Pass  Penalty  Penaltykick  Performance  Pitch  Players  Playoffs  Policy  Popular  Popularity  Position  Possession  Post  season  Practice  Pressure  Professional   Protection  Punctual  Pursue Qualify  Quality  Quarter  Ranking Record  Recruit  Redcard  Referee  Regulation  Retaliation Rivals   Rough Rules  Rushing  Safety  Sanction  Score  Scoring   Season  Shorts  Shot  Sideline  Skill Slide  Soccer  Spectator  Speed  Sportsmanship  Squad  Stadium  Staff  Stamina  Standards  Standings  Stands Strategy  Strength  Striker  Style  Substitute  Sweeper Tackle  Talent  Team  Teammate  Teamwork  Tenacious  Tiebreaker  Time lob  Title  Top-seed  Trainer  Training  Travel  TrophyUniforms United MostValuablePlayer Valuable Victory Warmup  Whistle  Winning  Women  Workout  WorldCup Yellowcard  aerobatics airracing gliding hanggliding parachuting paragliding archery badmintonball ball baldminton bribol bossaball fistball footvolley hooverball padel jianzi peteca pickleball rocball tabletennis tennis targetball teqball throwball volleyball wallyball basketball cestoball flickerball korfball netball ringball slamball baseball  batandtrap brannboll corkball cricket elle kickball kilikiti lapta matball oina palant punchball rounders stickball teeball vigoro wireball wiffleball skateboarding scootering skysurfing snowboarding streetluge surfing wakeboarding paddleboarding dodgeball Frisbee abselling iceclimbing aidclimbing mountaineering rockclimbing  canyoning canyoneering coasteering hiking ropeclimbing poleclimbing cycling skibobbing unicycling wrestling martialarts sumo sambo boxing karate kickboxing taekwondo kungfu pool snooker foosball horsepolo polo horseball angling casting noodling spearfishing discdog fricket discgolf Frisbee rugby golf gymnastics trampolining tumbling handball waterpolo hunting bandy icehockey hockey football soccer skating parasailing kitesurfing decathlon triathlon biathlon heptathlon icosathlon tetrathlon pentathlon aquathlon parkour marathon racketlon squash matkot miniten sprint athletics athlete sprint hurdling skyrunning sailing windsurfing kiteboarding speedskiing shooting  Olympic hurling lacrosse wallball canoeing kayaking rafting rowing swimming waboba backstroke beaststroke freestyle butterflystroke diving weightlifting autocross racing drifting folkrace rallying chess backgammon checkers draughts scrabble monopoly mahjong Sudoku running quidditch armwrestling bowling bocce boccia darts trugo woodsports aerobics axel arrow archer arean athlete ball base bat baton batter bicycle bike biking billiards boomerang boule curling s bow bowler medal bunt canoe catch champion championship club coach team competition compete competitor crew competitor cycle dartboard defense attack discus dive polevault longjump highjump dugout diver header pass epee equestrian equipment field exercise fencing fielder midfielder striker  defender goalie goalkeeper fitness forward game goal goldmedal bronzemedal golfer gym gymnasium gymnast halftime hammer helmet hitter hoop hometeam away stadium inning infield outfield outfielder infielder javelin jog jogger judo jumper jump kayaker kneepad league lose loser win winner mallet mat movement MVP move net offense offensive Ollie paddle paintball pingpong play pitch player playing playoff pole puck quarter quarterback quiver racer runner score scoreline scoreboard sculling shotput skate ski skier silvermedal snowboard sledder sledding somersault stroke surfer target throw tie throwing teammate triplejump umpire unicylclist vault vaulter vaulting volley waker weightlifter wicket winning worldcup wrestler ')
    Sport_scrape = ()
    Colours = (
        'amber amethystapricotaqua aquamarine auburn azure beige black blue bronze brown buffburnt umber cardinal carmine celadon cerise cerulean charcoal chartreuse chocolate cinnamon color complementary copper coral cream crimson cyan dark denim desertsand ebony ecru eggplant emerald forestgreen fuchsia gold golden rod gray green grey hotpink hue indigo ivory jade jet junglegreen kellygreen khaki lavender lemon light lilac lime magenta mahogany maroon mauve mustard navyblue ocher olive orange orchid pale pastel peach periwinkle persimmon pewter pink primary puce pumpkin purple rainbow red rose ruby russet rust saffron salmon sapphire scarlet seagreen secondary sepia shade shamrock sienna silver slate spectrum steelblue tan taupe teal terracotta thistle tint tomato topaz turquoise ultramarine umber vermilion violet viridian wheat white wisteria yellow')

    Schools = (
        '  answer arithmetic assignment atlas backpack ballpointpen binder blackboard book bookcase bookmark calculator calendar chalk chalkboard class clown classroom clipboard coloredpencils compass compositionbook computer constructionpaper crayons desk dictionary dividers dry-eraseboard easel encyclopedia English eraser exam examination experiment file folder flashcards gelpen geography globe glossary glue gluestick grades gym highlighter history holepunch homework ink intelligent keyboard language laptop learn lesson library loose leafpaper lunch lunchbox map markers math mathematics mechanicalpencil memopad memorize mortarboard notebook paper paperclip paperpunch paste pen pencil pencilpouch pencilsharpener physicaleducation portfolio poster paint principal printer project protractor pupil pushpinquestion quiz readingrecess rubberbands ruler science scissors sharpener smart spiralnotebook stapleremover stapler student tape teacher test thesaurus think thumbtack vocabulary watercolors whiteboard wordproblems wordprocessor worldmap writing yardstick')

    Professions = (
        'accountant actor actress actuary advisor aide ambassador animator archer artist astronaut astronomer athlete attorney auctioneer author babysitter baker ballerina banker barber baseballplayer basketballplayer bellhop biologist blacksmith bookkeeper bowler builder butcher butler cabdriver calligrapher captain cardiologist caregiver carpenter cartographer cartoonist cashier catcher caterer cellist chaplain chauffeur chef chemist clergyman clergywoman clerk coach cobbler composer concierge consultant contractor cook cop coroner courier cryptographer custodian dancer dentist deputy dermatologist designer detective dictator director discjockey diver doctor doorman driver drummer drycleaner ecologist economist editor educator electrician emperor empress engineer entertainer entomologist entrepreneu rexecutive explorer exporter exterminator extra falconer farmer financier firefighter fisherman flutist footballplayer foreman gamedesigner garbageman gardener gatherer gemcutter general geneticist geographer geologist golfer governor grocerguide hairdresser handyman harpist highwaypatrol hobo hunter illustrator importer instructor intern internist interpreter inventor investigator jailer janitor jester jeweler jockey journalist judge karateteacher laborer landlord landscaper laundress lawyer lecturer legalaide librarian librettist lifeguardlinguist lobbyist locksmith lyricist magician maid mailcarrier manager manufacturer mariner marketer mason mathematician mayor mechanic messenger midwife miner model monk muralist musician navigator negotiator notary novelist nun nurse oboist operator ophthalmologist optician oracle orderly ornithologist painter paleontologist paralegal parkranger pathologist pawnbroker peddler pediatrician percussionist performer pharmacist philanthropist philosopher photographer physician physicist pianist pilot pitcher plumber poet police policeman policewoman politician president prince princess principal private privatedetective producer professor programmer psychiatrist psychologist publisher quarterback quilter radiologist rancher ranger realestateagent receptionist referee registrar reporter representative researcher restaurateur retailer retiree sailor salesperson samurai saxophonist scholar scientist scouts  diver seamstress security guard senator sheriff singer smith socialite soldier spy star statistician stockbroker street sweeper surgeon surveyor swimmer tailor taxcollector taxidriver taxidermist teacher technician tennisplayer testpilot tiler toolmaker trader trainer translator trashcollector travelagent treasurer truckdriver tutor typist umpire undertaker usher valet veteran veterinarian violinist waiter waitress warden warrior watchmaker weaver welder woodcarver workman wrangler writer xylophonist yodeler zookeeper zoologist')

    Flowers = (
        "anemone appleblossom aster azalea baby'sbreath bachelorbutton begonia bellflower bellsofIreland bitterroot black-eyedSusan bluebells bluebonnet bougainvillea ,bouquet buttercup butterflybush calendula Californiapoppy callalily camellia candytuft canna carnation carrionflower chicory chrysanthemum clover columbine cornflower corpseflower cosmos crocus daffodil dahlia daisy dandelion delphinium dianthus dogwood edelweiss floret florist forget-me-not foxglove freesia gardenia gerberadaisy gillyflower gladiolus goldenrod hawthorn heather hibiscus hollyhock honeysuckle hydrangea Indianblanket iris jasmine jessamine Johnny-jump-up jonquil kangaroopaw lady'sslipper lantanalarkspurlaurellavenderlilaclilylily-of-the-valley magnolia mallow marigold mayflower mimosa mistletoe mockorange morningglory mountainlaurel myrtle narcissus nasturtium oleander orangeblossom orchid pansy pasqueflower passionflower peachblossom peony petal phlox plumeria poinsettia poppy primrose pussywillow QueenAnne'slace ranunculus rhododendron rose safflower segolily sepal snapdragon stock sunflower sweetpea thistle tickseed tigerlily trillium tulip Venusflytrap veronica vetch violet wallflower wildprairierose wildflowers wisteria wolfsbane yucca flower zinnia")

    Musics = (
        "accordion acousticguitar Aeolianharp Alphorn altosaxophone anvil babygrandpiano bagpipe bandoneon bandura banjo baritonehorn bass bassclarinet bassdrum bassguitar bassoon bell bongodrum bouzouki bow brass bugle calliope carillon castanets celesta cello Celticharp chimes cimbalom clarinet classicalguitar clavichord clavier concertina conch congadrum contrabass cornet cowbell cymbals didgeridoo doublebass drum drumsticks dulcimer electricguitar electricorgan Englishhorn euphonium fiddle fife flugelhorn flute Frenchhorn glockenspiel gong grandpiano guitar hammereddulcimer harmonica harmonium harp harpsichord helicon horn hurdy-gurdy instrument jawharp Jew'sharp kazoo kettledrum keyboard lutelyre mallets mandolin maracas marimba mellophone melodeon Moogsynthesizer musicalinstruments musicalsaw mute oboe ocarina organ panpipes pennywhistle percussion piano piccolo pipa pipeorgan playerpiano pumporgan rainstick rattle recorder reed saw saxophone sitar slidewhistle snaredrum sousaphone spinet spoons steeldrum steelguitar stringbass stringinstruments strings synthesizer tabla tambourine theremin thumbpiano timpani tinwhistle tom-tomdrum triangle trombone trumpet tuba tubularbells ukulele uprightpiano valve vibraphone viola violin violoncello vuvuzela Wagnertuba washboard whistle windchime windinstruments woodwindinstruments xylophone zither")

    Bodies = (
        "abdomen Adam'sapple adenoids adrenalgland anatomy ankle anus appendix arch arm artery back belly bellybutton bigtoe bladder blood bloodvessels body bone brain breast buttocks calf capillary carpal cartilage cell cervicalvertebrae cheek chest chin circulatorysystem clavicle coccyx collarbone diaphragm digestivesystem ear earlobe elbow endocrinesystem esophagus eye eyebrow eyelashes eyelid face fallopiantubes feet femur fibula filling finger fingernail follicle foot forehead gallbladder glands groin gums hair hand head heart heel hip humerus immunesystem indexfinger instep intestines iris jaw kidney knee larynx leg ligament lip liver lobe lumbarvertebrae lungs lymphnode mandible metacarpal metatarsal molar mouth muscle nail navel neck nerves nipple nose nostril organs ovary palm pancreas patella pelvis phalanges pharynx pinky pituitary pore pupil radius rectum redbloodcells respiratorysystem ribs sacrum scalp scapula senses shin shoulder shoulderblade skeleton skin skull sole spinalcolumn spinalcord spine spleen sternum stomach tarsal teeth tendon testes thigh thorax throat thumb thyroid tibia tissue toe toenail tongue tonsils tooth torso trachea ulna ureter urethra urinarysystem uterus uvula vein vertebra waist whitebloodcells wrist")

    Beaches = (
        "barnacle bathingsuit bay beach beachball bikini boardwalk boat boogieboard cape catamaran clam clambake coast conch cooler coral cove crab currents dive dock dune dunebuggy ebbtide family fins fish fishing Frisbee gull hangfive hat hermitcrab hightide ice cream intertidalzone island jellyfish kayak kelp lagoon lake lakeshore lifejacket lifepreserver lifeguard limpet longboard lowtide mangrove mussels neaptide ocean paddleboat palmtree pelican pier popsicle reef relax rest ripcurrent sail sailboat saltwater saltwatertaffy sand sanddollar sandals sandbar sandcastle scuba sea seastar seagull seashell seashore shark shell ship shore shorebirds snacks snorkel spray starfish sun sunhat sunbathe sunburn sunglasses sunscreen suntan surf surfboard swim swimfins swimmingcap taffy tan tide tidepool towel trip trunks tsunami umbrella undertow underwater vacation volleyball water waterbottle waves weekend wet wharf whitecaps yacht zoris")

    Calendars_Times = (
        'gregorian lunar day year lunisolar month julian solar schedule date islamic roman week date hebrew  docket intercalation hijri dates monthly weekly daily chronology holidays timeline millennium semester bronzeage timekeeping yearly events easter leapyear lunation era twelvemonth bimonthly itinerary diary scheduling fortnight fortnightly preceding deadline deadlines yesteryear yesternight lastweek lastmonth  timetables timetable midweek weekend sunrise beginning end sunset timescale coincide coincidence period night millennial century  centuries cycle cycles update  trimonthly annual biannual biennial perennial thursday decade Monday Tuesday Wednesday Friday Saturday Sunday morning evemig dawn forever early late earlier latest  onwards earliest  shorten periodical daytime coinciding regime countdown equinox tomorrow current present past future January February March April may June July August September October November December midday semimonthly yester today tonight workday expiration previous next egyptian quinquennium luster lustre lustrum history clock wallclock annually biennially perennially biannually once twice thrice seconds minutes hour hours minute millisecond milliseconds ancient modern moon ironage bronzeage babylonian forenoon someday afternoon timezone daybook midafternoon midnight noon day workweek preholiday classical hellenistic eve newyear newday Leapyear twelfthtide uptime downtime yeartime morningtide ethiopian sidereal wristwatch watch summer autumn spring winter newyear new day autumnal birthday timetabling birth date leap day decan autumnally fullmoon ')

    Families = (
        ' age old young aged adoption adoptivefather adoptivemother ancestor aunt bachelor birthmother bloodrelative bride bridegroom brother brother-in-law brotherhood brotherly care-giver child childhood children clan close-knit connection cousin closely-knit dad daddy daughter daughter-in-law descendant devoted divorce eligible engaged engagement estranged ex exhusband exwife extendedfamily faithful familytree father father-in-law fiancee firstborn firstcousin folks foster fosterchild fosterfather fostermother fosterparent fraternal fraternaltwin friend faimilyfriend genealogy gene granny gramps grandchild grandchildren granddaughter grandfather grandma grandmother grandpa grandparent grandson granny great-aunt great-granddaughter great-grandfather great-grandmother great-grandparent great-grandson great-uncle groom grownup half-brother halfsister heir heiress helpmate hereditary heritage history home household husband identical twin in-law infancy infant inherit inheritance juvenile kin  kinfolk kinship kith lineage love loyalty ma maiden name mama marriage mate maternal matriarch matrimony Miss mom mommy monogamy mother mother-in-law Mr. Mrs. Ms. nana natal nephew nest newlywed niece nuclearfamily nuptial nurture offspring orphan papa pa parent partner paternal patriarch pop posterity progenitor progeny quadruplets quads quints quintuplets related relations relative secondborn secondcousin senior separation sibling single sister sister-in-law sisterhood sisterly son son-in-law spouse stepbrother stepchild stepchildren stepdad stepdaughter stepfather stepmom stepmother stepsister stepson support surrogatemother tribe triplets trust trustworthy twinbrother twinsister twins uncle value wed wedding wedlock wife youngster youth')

    Countries_Cities = (
        ' oslo Palermo paris perm prague riga rome Rotterdam saint-petersburg samara Saratov Seville sofia stockholm Stuttgart Tolyatti turin ufa Ulyanovsk Valencia Vienna Volgograd Voronezh warsaw Wroclaw yaroslavl Zagreb zaporizhia zaragoza  Abkhazia Afghanistan Albania Algeria Andorra argentina ammenia artsakh Australia Austria Azerbaijan Bahamas Bahrain Bangladesh Barbados Belarus Belgium belize benin Bhutan Bolivia bosniaandherzegovina  Botswana brazil brunei bulgaria Burkina Burundi Cambodia Cameroon Canada cape central chad chile china Colombia Comoros costarica ivorycoast cotedivoire Croatia cuba Czech Denmark democratic republicofcongo Djibouti east Egypt Estonia eswatini Ethiopia finland france gabon georgia germany Ghana Greece guineabissau hungary Iceland india Indonesian iran Iraq Ireland Israel Italy Jamaica japan Jordan Kazakhstan Kenya northkorea southkorea Kosovo Kyrgyzstan laos Latvia Lebanon Lesotho Lithuania luxermbourg Madagascar Malawi Malaysia Maldives Mauritania mexico moldova morocco Montenegro myanamar Netherlands Nepal newzealand northmacedonia Norway oman Pakistan palau Palestine peru Philippines Poland Portugal puertorico congo Romania Russia Rwanda Saudi arabia serbia singapore slovakia slovenia southafrica srilanka sudan sudan suriname Sweden switzerland Taiwan Tanzania thailand transnistria TrinidadandTobago tunisia turkey Tuvalu Ukraine united arab emirates united kingdom united states Vanuatu Vietnam Zambia Zimbabwe Amsterdam Athens Barcelona Belgrade berlin Birmingham Bucharest Budapest Chisinau cologne Copenhagen dnipro Donetsk dusseldorf Frankfort Glasgow hamburg Helsinki Istanbul Izhevsk kazan kharkiv Kuwait kiev Krakow Krasnodar kryvyi-rih leeds lodz London Manchester lviv Madrid Makhachkala Marseille Milan minsk Moscow munich naples nizhny odessa  oslo Palermo paris perm prague riga rome Rostov-on-don Rotterdam saint-petersburg samara Saratov Seville sofia stockholm Stuttgart Tolyatti turin ufa Ulyanovsk Valencia Vienna Volgograd Voronezh warsaw Wroclaw yaroslavl Zagreb zaporizhia zaragoza')

    Noun = Nouns.split()
    Verb = Verbs.split()
    Adverb = Adverbs.split()
    Adjective = Adjectives.split()
    Sport = Sports.split()
    Food_Fruit = Food_Fruits.split()
    # Animal= Animal.split()
    Country_City = Countries_Cities.split()
    School = Schools.split()
    Body = Bodies.split()
    Calendar_Time = Calendars_Times.split()
    Profession = Professions.split()
    Music = Musics.split()
    Beach = Beaches.split()
    Family = Families.split()
    Flower = Flowers.split()
    Colour = Colours.split()
    Word_collection = Noun + Verb + Adjective + Adverb + Sport + Food_Fruit + Country_City + School + Body + Calendar_Time + Profession + Music + Beach + Family + Flower + Colour


    def difficulty_level(object):
        print('EASY--> A \nHARD--> B')
        global max_trial
        object.game_difficulty = input('Select game difficulty level: ')
        if object.game_difficulty.upper() == 'A':
            object.game_max_trial = 9
            print('MAXIMUM NUMBER OF ENTRY IS ', object.game_max_trial)
        elif object.game_difficulty.upper() == 'B':
            object.game_max_trial = 6
            print('MAXIMUM NUMBER OF ENTRY IS ', object.game_max_trial)
        else:
            print('INVALID ENTRY! \nMAXIMUM NUMBER OF ENTRY IS SET TO DEFAULT(9)')
            object.game_max_trial = 9


    class Player:
        def __init__(self, name=None, game_difficulty=None, game_max_trial=None, game_level=None,
                     game_Level_WordLength_dict=None, game_division=None, game_division_dict=None,
                     game_division_rating=None, game_rounds=None, wins=None, losses=None, streak=None, coins=None,
                     game_word=None, word_gap=None, gap_str=None, tries=None, game_revival_coins=None):
            self.name = name
            self.game_difficulty = game_difficulty
            self.game_max_trial = game_max_trial
            self.game_level = game_level
            self.game_Level_WordLength_dict = game_Level_WordLength_dict
            self.game_division = game_division
            self.game_division_dict = game_division_dict
            self.game_rounds = game_rounds
            self.wins = wins
            self.losses = losses
            self.streak = streak
            self.coins = coins
            self.game_word = game_word
            self.word_gap = word_gap
            self.gap_str = gap_str
            self.tries = tries
            self.game_revival_coins = game_revival_coins
            self.state_file = 'game_state.txt'

        def save_game(self):
            global player
            with open(self.state_file, 'wb') as save_state:
                pickle.dump(player, save_state)

        def load_game(self):
            global player
            with open(self.state_file, 'rb') as load_state:
                player = pickle.load(load_state)

        def __str__(self):
            return '{} is playing game at {} difficulty level; level {}, division{} round {} with {} wins, {} losses, {}streaks, and {}coins; Used trials on current word: {}'.format(
                self.name, self.game_difficulty, self.game_level, self.game_division, self.game_rounds, self.wins,
                self.losses, self.streak, self.coins, self.tries)


    class SinglePlayer(Player):
        def __init__(self, game_rounds=None, game_difficulty=None, game_max_trial=None, wins=None, losses=None,
                     streak=None, coins=None, category_selection=None,
                     game_word=None, word_gap=None, gap_str=None, tries=None, game_revival_coins=None):
            super().__init__(game_difficulty, game_max_trial, wins, losses, streak, coins, game_word, word_gap, gap_str,
                             tries, game_revival_coins)
            self.game_rounds = game_rounds
            self.category_selection = category_selection

        def save_game(self, description):
            global RS_player, CS_player
            if description == 'random':
                self.object = RS_player
                self.state_file = 'RSP_game_state.txt'
            elif description == 'category':
                self.object = CS_player
                self.state_file = 'CSP_game_state.txt'
            with open(self.state_file, 'wb') as save_state:
                pickle.dump(self.object, save_state)

        def load_game(self, description):
            global RS_player, CS_player
            if description == 'random':
                self.object = RS_player
                self.state_file = 'RSP_game_state.txt'
            elif description == 'category':
                self.object = CS_player
                self.state_file = 'CSP_game_state.txt'
            with open(self.state_file, 'rb') as load_state:
                self.object = pickle.load(load_state)
                if description is 'random':
                    RS_player = self.object
                else:
                    CS_player = self.object

        def __str__(self):
            return 'Game has been resumed at round {}, difficulty level {}. Player has {} wins, {} losses, {}streaks, and {}coins; Used trials on current word: {}'.format(
                self.game_rounds,
                self.game_difficulty, self.wins, self.losses, self.streak, self.coins, self.tries)


    class MultiPlayer(Player):
        def __init__(self, name=None, game_rounds=None, game_difficulty=None, game_max_trial=None,
                     count=None, streak=None, coins=None, game_word=None, word_gap=None, gap_str=None, tries=None,
                     name2=None, count2=None, streak2=None, coins2=None,
                     counts=None, counts_neutral=None, names=None, names_neutral=None, coins_list=None,
                     coins_neutral=None, streaks=None, streaks_neutral=None, category_selection=None):
            global PVP_MP, RM_player, CM_player
            super().__init__(name, game_difficulty, game_max_trial, streak, coins, game_word, word_gap,
                             gap_str, tries)
            self.count = count
            self.counts = counts
            self.counts_neutral = counts_neutral
            self.names = names
            self.names_neutral = names_neutral
            self.coins_list = coins_list
            self.coins_neutral = coins_neutral
            self.streaks = streaks
            self.streaks_neutral = streaks_neutral
            self.game_rounds = game_rounds
            self.category_selection = category_selection
            self.name2 = name2
            self.count2 = count2
            self.streak2 = streak2
            self.coins2 = coins2

        def save_game(self, description):
            global PVP_MP, RM_player, CM_player
            if description == 'pvp':
                self.object = PVP_MP
                self.state_file = 'PVP_MP_game_state.txt'
            elif description == 'random':
                self.object = RM_player
                self.state_file = 'RMP_game_state.txt'
            elif description == 'category':
                self.object = 'CM_player'
                self.state_file = 'CMP_game_state.txt'
            with open(self.state_file, 'wb') as save_state:
                pickle.dump(self.object, save_state)

        def load_game(self, description):
            global PVP_MP, RM_player, CM_player
            if description == 'pvp':
                self.object = PVP_MP
                self.state_file = 'PVP_MP_game_state.txt'
            elif description == 'random':
                self.object = RM_player
                self.state_file = 'RMP_game_state.txt'
            elif description == 'category':
                self.object = 'CM_player'
                self.state_file = 'CMP_game_state.txt'
            with open(self.state_file, 'rb') as load_state:
                self.object = pickle.load(load_state)
                if description is 'random':
                    RM_player = self.object
                elif description is 'category':
                    CM_player = self.object
                elif description is 'pvp':
                    PVP_MP = self.object
            print(RM_player)

        def __str__(self):
            return (
                'Game has been resumed at at round {}, difficulty level {}:\n{}(P1) has {} points, {}streaks, and {}coins '
                '\n{}(P2) has {} points, {}streaks, and {}coins; Used trials on current word: {}'.format(self.game_rounds,
                                                                         self.game_difficulty, self.name,
                                                                         self.count, self.streak,
                                                                         self.coins, self.name2,
                                                                         self.count2, self.streak2, self.coins2, self.tries))


    home = False
    while not home:
        play_button = input('PLAY?  ')
        if play_button in ['y', 'Y']:
            # settings_button = input('SETTINGS?  ')
            menu_1 = False
            while not menu_1:
                print('PLEASE SELECT GAME MODE...')
                mode = input('A- QUICK PLAY B- CAREER MODE')
                if mode in ['a', 'A']:
                    print('PLEASE SELECT GAME MODE...')
                    mode2 = input('A- SINGLE PLAYER  B- MULTI-PLAYER:  ')
                    if mode2 in ['a', 'A']:
                        selection = input('A- RANDOM MODE \nB-CATEGORY MODE')
                        if selection in ['a', 'A']:
                            RS_player = SinglePlayer()
                            # FUNCTION 1 STARTS
                            load_request = input('A- NEW GAME \nB- LOAD GAME')
                            if load_request.upper() == 'B':
                                try:
                                    RS_player.load_game('random')
                                    print('SAVED STATE LOADED')
                                    game_state_loaded = True
                                    print(RS_player)
                                except FileNotFoundError as f:
                                    print('SAVED STATE FILE NOT FOUND')
                                    game_state_loaded = False
                                    difficulty_level(RS_player)
                                    RS_player.revival_coins, RS_player.streak, RS_player.wins, RS_player.losses, RS_player.game_rounds, RS_player.coins = 20, 0, 0, 0, 1, 0
                                    RS_player.save_game('random')
                            elif load_request.upper() == 'A':
                                game_state_loaded = False
                                try:
                                    with open('RSP_game_state.txt', 'w'):
                                        pass
                                except:
                                    pass
                                difficulty_level(RS_player)
                                RS_player.revival_coins, RS_player.streak, RS_player.wins, RS_player.losses, RS_player.game_rounds, RS_player.coins = 20, 0, 0, 0, 1, 0
                                RS_player.save_game('random')


                            def get_hint():
                                help = choice(word_list)
                                while help in RS_player.gap_str:
                                    help = choice(word_list)
                                for letter in word_list:
                                    index = ([pos for pos, letter in enumerate(word_list) if letter == help])
                                    for element in index:
                                        RS_player.word_gap[element] = help


                            def end_game():
                                print('GAME OVER!')
                                score = ('SCORE:  %d / %d' % (RS_player.wins, RS_player.game_rounds))
                                print(score)


                            # FUNCTION 1 ENDS

                            Quit = False
                            while True:
                                # GO AND REMOVE THE FOREVER WHILE LOOP USING YOUR LAPTOP
                                while not Quit:
                                    if game_state_loaded is False:
                                        RS_player.game_word = choice(Word_collection).upper()
                                    else:
                                        pass
                                    # RS_player.game_word= 'DAISY'
                                    Description_Dict = {'NOUN': Noun, 'VERB': Verb, 'ADJECTIVE': Adjective,
                                                        'ADVERB': Adverb,
                                                        'SPORT': Sport,
                                                        'FOOD/FRUIT': Food_Fruit, 'COUNNTRY/CITY': Country_City,
                                                        'SCHOOL': School,
                                                        'BODY': Body,
                                                        'CALENDER/TIME': Calendar_Time,
                                                        'PROFESSION': Profession, 'MUSIC': Music, 'BEACH': Beach,
                                                        'FAMILY': Family,
                                                        'FLOWER': Flower, 'COLOUR': Colour}
                                    if game_state_loaded is False:
                                        word_list = list(RS_player.game_word)
                                    else:
                                        pass
                                    if game_state_loaded is False:
                                        RS_player.word_gap = ('_' * len(RS_player.game_word))
                                    else:
                                        pass
                                    if game_state_loaded is False:
                                        RS_player.gap_str = '   '.join(RS_player.word_gap)
                                    else:
                                        pass
                                    if game_state_loaded is False:
                                        RS_player.word_gap = list(RS_player.word_gap)
                                    else:
                                        pass
                                    if game_state_loaded is False:
                                        RS_player.tries = 0
                                    else:
                                        pass
                                    if game_state_loaded is False:
                                        RS_player.save_game('random')
                                    else:
                                        pass

                                    # FUNCTION 8 STARTS
                                    print('ROUND %d>>>' % RS_player.game_rounds)
                                    while RS_player.tries < RS_player.game_max_trial:
                                        RS_player.save_game('random')


                                        def obt_key(val):
                                            for key, value in Description_Dict.items():
                                                if val == value:
                                                    return key


                                        for item in Description_Dict.values():
                                            if RS_player.game_word.lower() in item or RS_player.game_word.capitalize() in item:
                                                print('WORD DESCRIPTION:  ', obt_key(item))
                                        print(RS_player.gap_str)
                                        print()
                                        RS_player.save_game('random')
                                        # FUNCITON 8 ENDS

                                        # FUNCTION 2 STARTS
                                        hint = input(
                                            "GET HINT? \nENTER 'Y' OR 'y' TO CONFIRM OTHERWISE, PRESS ANY KEY:   ")
                                        if hint == 'y' or hint == 'Y':
                                            if RS_player.coins >= 10:
                                                get_hint()
                                                RS_player.gap_str = '   '.join(RS_player.word_gap)
                                                RS_player.coins -= 10
                                                print('COINS LEFT:  ', RS_player.coins)
                                                RS_player.save_game('random')

                                                if '_' not in RS_player.gap_str:
                                                    print(RS_player.gap_str)
                                                    win_comment = ['BRILLIANT!', 'AWESOME!', 'BRAVO!', 'GREAT!',
                                                                   'ASTONISHING!',
                                                                   'EYE-WATERING!',
                                                                   'FANTASTIC!', 'WOW!', 'OUTSTANDING!', 'OUTRAGEOUS!',
                                                                   'EXTRAORDINARY!',
                                                                   'WHOA!',
                                                                   'CONGRATULATIONS!']
                                                    print(choice(win_comment))
                                                    RS_player.wins += 1
                                                    print('WINS:  ', RS_player.wins)
                                                    RS_player.streak += 1
                                                    print('STREAK: ', RS_player.streak)
                                                    RS_player.save_game('random')
                                                    if RS_player.streak % 5 == 0:
                                                        streak_comment = ['%d IN A ROW!' % RS_player.streak,
                                                                          '%d IN %d!' % (
                                                                              RS_player.streak, RS_player.streak),
                                                                          'CONSECUTIVE %d WINS!' % RS_player.streak,
                                                                          '%d AT ONCE!' % RS_player.streak]
                                                        print(choice(streak_comment))
                                                        RS_player.coins += 5
                                                        print('YOU EARNED 5 COINS!\t COINS:  ', RS_player.coins)
                                                    else:
                                                        RS_player.coins += 1
                                                        print('YOU EARNED A COIN!\t COINS:  ', RS_player.coins)
                                                    RS_player.save_game('random')
                                                    Exit = input(
                                                        'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                                                    if Exit == '1':
                                                        end_game()
                                                        Quit = True
                                                        game_state_loaded = False
                                                        RS_player.save_game('random')
                                                        break
                                                    else:
                                                        score = ('SCORE:  %d / %d' % (
                                                            RS_player.wins, RS_player.game_rounds))
                                                        print('SCORE:  ', score)
                                                        RS_player.game_rounds += 1
                                                        game_state_loaded = False
                                                        RS_player.save_game('random')
                                                        break
                                            else:
                                                print('INSUFFICIENT COINS!')
                                                RS_player.save_game('random')
                                                pass

                                        else:
                                            guess = (input('Your guess?  ')).upper()
                                            RS_player.save_game('random')
                                            if guess in RS_player.game_word:
                                                index = ([pos for pos, letter in enumerate(RS_player.game_word) if
                                                          letter == guess])
                                                for element in index:
                                                    RS_player.word_gap[element] = guess
                                                RS_player.gap_str = '   '.join(RS_player.word_gap)
                                                RS_player.save_game('random')
                                                if '_' not in RS_player.gap_str:
                                                    print(RS_player.gap_str)
                                                    win_comment = ['BRILLIANT!', 'AWESOME!', 'BRAVO!', 'GREAT!',
                                                                   'ASTONISHING!',
                                                                   'EYE-WATERING!', 'FANTASTIC!', 'WOW!',
                                                                   'OUTSTANDING!', 'OUTRAGEOUS!',
                                                                   'EXTRAORDINARY!', 'WHOA!', 'CONGRATULATIONS!']
                                                    print(choice(win_comment))
                                                    RS_player.wins += 1
                                                    print('WINS:  ', RS_player.wins)
                                                    RS_player.streak += 1
                                                    print('STREAK: ', RS_player.streak)
                                                    RS_player.save_game('random')
                                                    if RS_player.streak % 5 == 0:
                                                        streak_comment = ['%d IN A ROW!' % RS_player.streak,
                                                                          '%d IN %d!' % (
                                                                              RS_player.streak, RS_player.streak),
                                                                          'CONSECUTIVE %d WINS!' % RS_player.streak,
                                                                          '%d AT ONCE!' % RS_player.streak]
                                                        print(choice(streak_comment))
                                                        RS_player.coins += 5
                                                        print('YOU EARNED 5 COINS!\t COINS:  ', RS_player.coins)
                                                    else:
                                                        RS_player.coins += 1
                                                        print('YOU EARNED A COIN!\t COINS:  ', RS_player.coins)
                                                    print(RS_player.gap_str)
                                                    RS_player.save_game('random')

                                                    Exit = input(
                                                        'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                                                    if Exit == '1':
                                                        end_game()
                                                        Quit = True
                                                        game_state_loaded = False
                                                        RS_player.save_game('random')
                                                        break
                                                    else:
                                                        score = ('SCORE:  %d / %d' % (
                                                            RS_player.wins, RS_player.game_rounds))
                                                        print('SCORE:  ', score)
                                                        RS_player.game_rounds += 1
                                                        game_state_loaded = False
                                                        RS_player.save_game('random')
                                                        break

                                            else:
                                                RS_player.tries += 1
                                                print(guess, 'is not in the word')
                                                RS_player.save_game('random')

                                    else:
                                        print('MAN HANGED!!!')
                                        print(
                                            'You\'re out of tries \nGAME OVER! \nThe word is \'%s\'' % RS_player.game_word)
                                        revival = input(
                                            "REVIVE MAN? \nEnter 'y' or 'Y' to confirm otherwise, press any key:  ")
                                        RS_player.save_game('random')
                                        if revival in ['y', 'Y']:
                                            if RS_player.coins >= RS_player.revival_coins:
                                                print('MAN REVIVED!!!')
                                                RS_player.tries -= RS_player.game_max_trial
                                                RS_player.coins -= RS_player.revival_coins
                                                RS_player.revival_coins += 10
                                                print('REMAINING COINS:  ', RS_player.coins)
                                                RS_player.save_game('random')
                                                continue
                                            else:
                                                print('INSUFFICIENT COINS!')
                                                RS_player.losses += 1
                                                RS_player.save_game('random')
                                                if RS_player.streak > 0:
                                                    RS_player.streak = 0
                                                    print('STREAK ENDS!')
                                                    print('LOSES: ', RS_player.losses)
                                                    RS_player.save_game('random')
                                                Exit = input(
                                                    'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                                                if Exit == '1':
                                                    end_game()
                                                    Quit = True
                                                    game_state_loaded = False
                                                    RS_player.save_game('random')
                                                    break
                                                else:
                                                    score = ('%d/%d' % (RS_player.wins, RS_player.game_rounds))
                                                    print('SCORE:  ', score)
                                                    RS_player.game_rounds += 1
                                                    game_state_loaded = False
                                                    RS_player.save_game('random')
                                                    continue


                                        else:
                                            RS_player.losses += 1
                                            RS_player.save_game('random')
                                            if RS_player.streak > 0:
                                                RS_player.streak = 0
                                                print('STREAK ENDS!')
                                                print('LOSES: ', RS_player.losses)
                                                RS_player.save_game('random')

                                            Exit = input(
                                                'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                                            if Exit == '1':
                                                end_game()
                                                Quit = True
                                                game_state_loaded = False
                                                RS_player.save_game('random')
                                                break
                                            else:
                                                score = ('%d/%d' % (RS_player.wins, RS_player.game_rounds))
                                                print('SCORE:  ', score)
                                                RS_player.game_rounds += 1
                                                game_state_loaded = False
                                                RS_player.save_game('random')
                                        # FUNCTION 2 ENDS
                        elif selection in ['b', 'B']:
                            # FUNCTION 1 STARTS
                            CS_player = SinglePlayer()
                            load_request = input('A- NEW GAME \nB- LOAD GAME')
                            if load_request.upper() == 'B':
                                try:
                                    CS_player.load_game('category')
                                    print('SAVED STATE LOADED')
                                    game_state_loaded = True
                                    print(CS_player)
                                except FileNotFoundError as f:
                                    print('SAVED STATE FILE NOT FOUND')
                                    game_state_loaded = False
                                    difficulty_level(CS_player)
                                    CS_player.revival_coins, CS_player.streak, CS_player.wins, CS_player.losses, CS_player.game_rounds, CS_player.coins = 20, 0, 0, 0, 1, 0
                                    CS_player.save_game('category')
                            elif load_request.upper() == 'A':
                                game_state_loaded = False
                                try:
                                    with open('CSP_game_state.txt','w'):
                                        pass
                                except FileNotFoundError:
                                    pass
                                difficulty_level(CS_player)
                                CS_player.revival_coins, CS_player.streak, CS_player.wins, CS_player.losses, CS_player.game_rounds, CS_player.coins = 20, 0, 0, 0, 1, 0
                                CS_player.save_game('category')


                            def get_hint():
                                help = choice(word_list)
                                while help in CS_player.gap_str:
                                    help = choice(word_list)
                                for letter in word_list:
                                    index = ([pos for pos, letter in enumerate(word_list) if letter == help])
                                    for element in index:
                                        CS_player.word_gap[element] = help


                            def end_game():
                                print('GAME OVER!')
                                score = ('SCORE:  %d / %d' % (CS_player.wins, CS_player.game_rounds))
                                print(score)


                            # FUNCTION 1 ENDS

                            # FUNCTION 7 STARTS
                            Description_Dict = {'A1': ['Adjective', Adjective], 'A2': ['Adverb', Adverb],
                                                'B1': ['Beach', Beach],
                                                'B2': ['Body', Body],
                                                'C1': ['Calendar_Time', Calendar_Time], 'C2': ['Colour', Colour],
                                                'C3': ['Country_City', Country_City],
                                                'F1': ['Family', Family], 'F2': ['Flower', Flower],
                                                'F3': ['Food_Fruit', Food_Fruit],
                                                'M': ['Music', Music],
                                                'N': ['Noun', Noun], 'P': ['Profession', Profession],
                                                'S1': ['School', School],
                                                'S2': ['Sport', Sport], 'V': ['Verb', Verb]}
                            for keys, values in Description_Dict.items():
                                print(keys, '=', values[0])
                            if game_state_loaded is False:
                                CS_player.category_selection = input(
                                    "Please enter the corresponding value of the words category you'd like to play: ").upper()
                            else:
                                pass
                            # FUNCTION 7 ENDS
                            Quit = False
                            while not Quit:
                                for keys, values in Description_Dict.items():
                                    if CS_player.category_selection in keys:
                                        word_description = values[0]
                                        if game_state_loaded is False:
                                            CS_player.game_word = choice(values[1]).upper()
                                        else:
                                            pass
                                        if game_state_loaded is False:
                                            word_list = list(CS_player.game_word)
                                        else:
                                            pass
                                        if game_state_loaded is False:
                                            CS_player.word_gap = ('_' * len(CS_player.game_word))
                                        else:
                                            pass
                                        if game_state_loaded is False:
                                            CS_player.gap_str = '   '.join(CS_player.word_gap)
                                        else:
                                            pass
                                        if game_state_loaded is False:
                                            CS_player.word_gap = list(CS_player.word_gap)
                                        else:
                                            pass
                                        if game_state_loaded is False:
                                            CS_player.tries = 0
                                        else:
                                            pass
                                        if game_state_loaded is False:
                                            CS_player.save_game('category')
                                        else:
                                            pass
                                print('ROUND %d>>>' % CS_player.game_rounds)
                                while CS_player.tries < CS_player.game_max_trial:
                                    CS_player.save_game('category')
                                    print('WORD DESCRIPTION:  ', word_description)
                                    print(CS_player.gap_str)
                                    print()
                                    CS_player.save_game('category')
                                    # FUNCTION 2 STARTS
                                    hint = input("GET HINT? \nENTER 'Y' OR 'y' TO CONFIRM OTHERWISE, PRESS ANY KEY:   ")
                                    if hint == 'y' or hint == 'Y':
                                        if CS_player.coins >= 10:
                                            get_hint()
                                            CS_player.gap_str = '   '.join(CS_player.word_gap)
                                            CS_player.coins -= 10
                                            print('COINS LEFT:  ', CS_player.coins)
                                            CS_player.save_game('category')

                                            if '_' not in CS_player.gap_str:
                                                print(CS_player.gap_str)
                                                win_comment = ['BRILLIANT!', 'AWESOME!', 'BRAVO!', 'GREAT!',
                                                               'ASTONISHING!',
                                                               'EYE-WATERING!',
                                                               'FANTASTIC!', 'WOW!', 'OUTSTANDING!', 'OUTRAGEOUS!',
                                                               'EXTRAORDINARY!',
                                                               'WHOA!',
                                                               'CONGRATULATIONS!']
                                                print(choice(win_comment))
                                                CS_player.wins += 1
                                                print('WINS:  ', CS_player.wins)
                                                CS_player.streak += 1
                                                print('STREAK: ', CS_player.streak)
                                                CS_player.save_game('category')
                                                if CS_player.streak % 5 == 0:
                                                    streak_comment = ['%d IN A ROW!' % CS_player.streak,
                                                                      '%d IN %d!' % (
                                                                          CS_player.streak, CS_player.streak),
                                                                      'CONSECUTIVE %d WINS!' % CS_player.streak,
                                                                      '%d AT ONCE!' % CS_player.streak]
                                                    print(choice(streak_comment))
                                                    CS_player.coins += 5
                                                    print('YOU EARNED 5 COINS!\t COINS:  ', CS_player.coins)
                                                else:
                                                    CS_player.coins += 1
                                                    print('YOU EARNED A COIN!\t COINS:  ', CS_player.coins)

                                                CS_player.save_game('category')
                                                Exit = input(
                                                    'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                                                if Exit == '1':
                                                    end_game()
                                                    Quit = True
                                                    game_state_loaded = False
                                                    CS_player.save_game('category')
                                                    break
                                                else:
                                                    score = ('SCORE:  %d / %d' % (
                                                    CS_player.wins, CS_player.game_rounds))
                                                    print('SCORE:  ', score)
                                                    CS_player.game_rounds += 1
                                                    CS_player.save_game('category')
                                                    game_state_loaded = False
                                                    break
                                        else:
                                            print('INSUFFICIENT COINS!')
                                            CS_player.save_game('category')
                                            pass

                                    else:
                                        guess = (input('Your guess?  ')).upper()
                                        CS_player.save_game('category')
                                        if guess in CS_player.game_word:
                                            index = (
                                            [pos for pos, letter in enumerate(CS_player.game_word) if letter == guess])
                                            for element in index:
                                                CS_player.word_gap[element] = guess
                                            CS_player.gap_str = '   '.join(CS_player.word_gap)
                                            CS_player.save_game('category')
                                            if '_' not in CS_player.gap_str:
                                                print(CS_player.gap_str)
                                                win_comment = ['BRILLIANT!', 'AWESOME!', 'BRAVO!', 'GREAT!',
                                                               'ASTONISHING!',
                                                               'EYE-WATERING!', 'FANTASTIC!', 'WOW!', 'OUTSTANDING!',
                                                               'OUTRAGEOUS!',
                                                               'EXTRAORDINARY!', 'WHOA!', 'CONGRATULATIONS!']
                                                print(choice(win_comment))
                                                CS_player.wins += 1
                                                print('WINS:  ', CS_player.wins)
                                                CS_player.streak += 1
                                                print('STREAK: ', CS_player.streak)
                                                CS_player.save_game('category')
                                                if CS_player.streak % 5 == 0:
                                                    streak_comment = ['%d IN A ROW!' % CS_player.streak,
                                                                      '%d IN %d!' % (
                                                                          CS_player.streak, CS_player.streak),
                                                                      'CONSECUTIVE %d CS_player.wins!' % CS_player.streak,
                                                                      '%d AT ONCE!' % CS_player.streak]
                                                    print(choice(streak_comment))
                                                    CS_player.coins += 5
                                                    print('YOU EARNED 5 COINS!\t COINS:  ', CS_player.coins)
                                                else:
                                                    CS_player.coins += 1
                                                    print('YOU EARNED A COIN!\t COINS:  ', CS_player.coins)
                                                print(CS_player.gap_str)
                                                CS_player.save_game('category')

                                                Exit = input(
                                                    'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                                                if Exit == '1':
                                                    end_game()
                                                    Quit = True
                                                    game_state_loaded = False
                                                    CS_player.save_game('category')
                                                    break
                                                else:
                                                    score = ('SCORE:  %d / %d' % (
                                                    CS_player.wins, CS_player.game_rounds))
                                                    print('SCORE:  ', score)
                                                    CS_player.game_rounds += 1
                                                    game_state_loaded = False
                                                    CS_player.save_game('category')
                                                    break

                                        else:
                                            CS_player.tries += 1
                                            print(guess, 'is not in the word')
                                            CS_player.save_game('category')

                                else:
                                    print('MAN HANGED!!!')
                                    print(
                                        'You\'re out of tries \nGAME OVER! \nThe word is \'%s\'' % CS_player.game_word)
                                    revival = input(
                                        "REVIVE MAN? \nEnter 'y' or 'Y' to confirm otherwise, press any key:  ")
                                    CS_player.save_game('category')
                                    if revival in ['y', 'Y']:
                                        if CS_player.coins >= CS_player.revival_coins:
                                            print('MAN REVIVED!!!')
                                            CS_player.tries -= CS_player.game_max_trial
                                            CS_player.coins -= CS_player.revival_coins
                                            print('REMAINING COINS:  ', CS_player.coins)
                                            CS_player.save_game('category')
                                            continue
                                        else:
                                            print('INSUFFICIENT COINS!')
                                            CS_player.losses += 1
                                            CS_player.save_game('category')
                                            if CS_player.streak > 0:
                                                CS_player.streak = 0
                                                print('STREAK ENDS!')
                                                print('LOSES: ', CS_player.losses)
                                                CS_player.save_game('category')

                                            Exit = input(
                                                'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                                            if Exit == '1':
                                                end_game()
                                                Quit = True
                                                game_state_loaded = False
                                                CS_player.save_game('category')
                                                break
                                            else:
                                                score = ('%d/%d' % (CS_player.wins, CS_player.game_rounds))
                                                print('SCORE:  ', score)
                                                CS_player.game_rounds += 1
                                                game_state_loaded = False
                                                CS_player.save_game('category')
                                                continue


                                    else:
                                        CS_player.losses += 1
                                        CS_player.save_game('category')
                                        if CS_player.streak > 0:
                                            CS_player.streak = 0
                                            print('STREAK ENDS!')
                                            print('LOSSES: ', CS_player.losses)
                                            CS_player.save_game('category')

                                        Exit = input(
                                            'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                                        if Exit == '1':
                                            end_game()
                                            Quit = True
                                            game_state_loaded = False
                                            CS_player.save_game('category')
                                            break
                                        else:
                                            score = ('%d/%d' % (CS_player.wins, CS_player.game_rounds))
                                            print('SCORE:  ', score)
                                            CS_player.game_rounds += 1
                                            game_state_loaded = False
                                            CS_player.save_game('category')
                                    # FUNCTION 2 ENDS



                    elif mode2 in ['b', 'B']:
                        selection = (input('A- PLAYER VS PLAYER \nB- PLAYER<--CPU-->PLAYER:  '))
                        if selection in ['a', 'A']:
                            # FUNCTION 3 STARTS
                            Player1 = input('PLAYER1-->Please enter your name:  ').upper()
                            print('WLECOME %s!' % Player1.upper())
                            Player2 = input('PLAYER2-->Please enter your name:  ').upper()
                            print('WLECOME %s!' % Player2.upper())
                            Players = [Player1, Player2]
                            count1 = 0
                            count2 = 0
                            streak1 = 0
                            streak2 = 0
                            coins1 = 0
                            coins2 = 0
                            rounds = 1
                            coins = [coins1, coins2]
                            streaks = [streak1, streak2]
                            counts = [count1, count2]


                            def get_hint():
                                help = choice(word_list)
                                while help in gap_str:
                                    help = choice(word_list)
                                for letter in word_list:
                                    index = ([pos for pos, letter in enumerate(word_list) if letter == help])
                                    for element in index:
                                        gap[element] = help


                            def end_game():
                                print('GAME OVER!')
                                score = ("(%s)%d : (%s)%d" % (Players[0], counts[0], Players[1], counts[1]))
                                print('SCORE:  ', score)


                            # FUNCTION 3 ENDS

                            quit = False
                            while not quit:
                                # TRY DEFINING A FUNCTION HERE
                                cycle = 1
                                recycle = False
                                while not recycle:
                                    if True:
                                        # FUNCTION 4 STARTS
                                        Continue = False
                                        Players_neutral = Players[1]
                                        Players[1] = Players[0]
                                        Players[0] = Players_neutral
                                        coins_neutral = coins[1]
                                        coins[1] = coins[0]
                                        coins[0] = coins_neutral
                                        streaks_neutral = streaks[1]
                                        streaks[1] = streaks[0]
                                        streaks[0] = streaks_neutral
                                        counts_neutral = counts[1]
                                        counts[1] = counts[0]
                                        counts[0] = counts_neutral
                                    # FUNCTION 4 ENDS

                                    word = input('%s, Please enter your word:  ' % Players[1]).upper()
                                    word_description = input("%s, Give the word description(OPTIONAL):  " % Players[1])
                                    system('clear')
                                    # FUNCTION 5 STARTS
                                    word_list = list(word)
                                    gap = ('_' * len(word))
                                    gap_str = '   '.join(gap)
                                    gap = list(gap)

                                    tries = 0
                                    # FUNCTION 5 ENDS
                                    print('%s TURN....' % Players[0])
                                    while tries < 9:
                                        print(
                                            'WORD DESCRIPTION:  %s' % word_description) if word_description is not '' else print(
                                            'WORD DESCRIPTION:  NOT PROVIDED')
                                        print(gap_str)
                                        # FUNCTION 6 STARTS
                                        hint = input(
                                            "GET HINT? \nENTER 'Y' OR 'y' TO CONFIRM OTHERWISE, PRESS ANY KEY:   ")
                                        if hint == 'y' or hint == 'Y':
                                            if coins[0] >= 3:
                                                get_hint()
                                                gap_str = '   '.join(gap)
                                                coins[0] -= 3
                                                print('%s, YOUR COINS LEFT:  %d' % (Players[1], coins[1]))
                                                if '_' not in gap_str:
                                                    print(gap_str)
                                                    win_comment = ['BRILLIANT!', 'AWESOME!', 'BRAVO!', 'GREAT!',
                                                                   'ASTONISHING!',
                                                                   'EYE-WATERING!',
                                                                   'FANTASTIC!', 'WOW!', 'OUTSTANDING!', 'OUTRAGEOUS!',
                                                                   'EXTRAORDINARY!',
                                                                   'WHOA!',
                                                                   'CONGRATULATIONS!']
                                                    print(choice(win_comment))
                                                    counts[0] += 1
                                                    print('POINTS:  ', counts[0])
                                                    streaks[0] += 1
                                                    print("%s STREAK:  %d" % (Players[0], streaks[0]))
                                                    if streaks[0] % 5 == 0:
                                                        streak_comment = ['%d IN A ROW!' % streaks[0],
                                                                          '%d IN %d!' % (streaks[0], streaks[0]),
                                                                          'CONSECUTIVE %d WINS!' % streaks[0],
                                                                          '%d AT ONCE!' % streaks[0]]
                                                        print(choice(streak_comment))
                                                        coins[0] += 5
                                                        print('%s EARNED 5 COINS!\tCOINS:  %d' % (Players[0], coins[0]))
                                                        tries = 10
                                                        Continue = True
                                                        break
                                                    else:
                                                        coins[0] += 1
                                                        print('%s EARNED A COIN!\tCOINS:  %d' % (Players[0], coins[0]))
                                                        tries = 10
                                                        Continue = True
                                                        break
                                            else:
                                                print('INSUFFICIENT COINS!')
                                        else:
                                            guess = input('Your guess, %s?:  ' % Players[0]).upper()
                                            if guess in word:
                                                index = ([pos for pos, letter in enumerate(word) if letter == guess])
                                                for element in index:
                                                    gap[element] = guess
                                                    gap_str = '   '.join(gap)
                                                    if '_' not in gap_str:
                                                        print(gap_str)
                                                        win_comment = ['BRILLIANT!', 'AWESOME!', 'BRAVO!', 'GREAT!',
                                                                       'ASTONISHING!',
                                                                       'EYE-WATERING!',
                                                                       'FANTASTIC!', 'WOW!', 'OUTSTANDING!',
                                                                       'OUTRAGEOUS!',
                                                                       'EXTRAORDINARY!', 'WHOA!',
                                                                       'CONGRATULATIONS!']
                                                        print(choice(win_comment))
                                                        counts[0] += 1
                                                        streaks[0] += 1
                                                        print("%s STREAK:  %d" % (Players[0], streaks[0]))
                                                        if streaks[0] % 5 == 0:
                                                            streak_comment = ['%d IN A ROW!' % streaks[0],
                                                                              '%d IN %d!' % (streaks[0], streaks[0]),
                                                                              'CONSECUTIVE %d WINS!' % streaks[0],
                                                                              '%d AT ONCE!' % streaks[0]]
                                                            print(choice(streak_comment))
                                                            coins[0] += 5
                                                            print('%s EARNED 5 COINS!\tCOINS:  %d' % (
                                                                Players[0], coins[0]))
                                                            tries = 10
                                                            Continue = True
                                                            break
                                                        else:
                                                            coins[0] += 1
                                                            print('%s EARNED A COIN!\tCOINS:  %d' % (
                                                                Players[0], coins[0]))
                                                            tries = 10
                                                            Continue = True
                                                            break

                                            else:
                                                tries += 1
                                                print(guess, 'is not in the word')
                                    else:
                                        if Continue == False:
                                            print('MAN HANGED!!!')
                                            print('You\'re out of tries \nYOU LOST! \nThe hidden word is \'%s\'' % word)
                                    if cycle % 2 == 0:
                                        Exit = input(
                                            'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                                        if Exit == '1':
                                            end_game()
                                            quit = True
                                            break
                                        else:
                                            score = ("(%s)%d : (%s)%d" % (Players[0], counts[0], Players[1], counts[1]))
                                            print('SCORE:  ', score)
                                            rounds += 1
                                            print('ROUND %d>>>' % rounds)

                                            break
                                    cycle += 1
                                    # FUNCTION 6 ENDS


                        elif selection in ['b', 'B']:
                            selection2 = input('A- RANDOM MODE \nB- CATEGORY MODE  ')
                            if selection2 in ['a', 'A']:
                                RM_player = MultiPlayer()
                                # FUNCTION 3 STARTS
                                load_request = input('A- NEW GAME \nB- LOAD GAME')
                                if load_request.upper() == 'B':
                                    try:
                                        RM_player.load_game('random')
                                        print('SAVED STATE LOADED')
                                        game_state_loaded = True
                                        print(RM_player)
                                    except FileNotFoundError as f:
                                        print('SAVED STATE FILE NOT FOUND')
                                        game_state_loaded = False
                                        difficulty_level(RM_player)
                                        RM_player.names = [RM_player.name, RM_player.name2]
                                        RM_player.count = 0
                                        RM_player.count2 = 0
                                        RM_player.streak = 0
                                        RM_player.streak2 = 0
                                        RM_player.coins = 0
                                        RM_player.coins2 = 0
                                        RM_player.game_rounds = 1
                                        RM_player.coins_list = [RM_player.coins, RM_player.coins2]
                                        RM_player.streaks = [RM_player.streak, RM_player.streak2]
                                        RM_player.counts = [RM_player.count, RM_player.count2]
                                        RM_player.save_game('random')
                                elif load_request.upper() == 'A':
                                    game_state_loaded = False
                                    try:
                                        with open('RMP_game_state.txt', 'w'):
                                            pass
                                    except FileNotFoundError:
                                        pass
                                    difficulty_level(RM_player)
                                    RM_player.names = [RM_player.name, RM_player.name2]
                                    RM_player.count = 0
                                    RM_player.count2 = 0
                                    RM_player.streak = 0
                                    RM_player.streak2 = 0
                                    RM_player.coins = 0
                                    RM_player.coins2 = 0
                                    RM_player.game_rounds = 1
                                    RM_player.coins_list = [RM_player.coins, RM_player.coins2]
                                    RM_player.streaks = [RM_player.streak, RM_player.streak2]
                                    RM_player.counts = [RM_player.count, RM_player.count2]
                                    RM_player.save_game('random')
                                if game_state_loaded is False:
                                    RM_player.name = input('PLAYER1-->Please enter your name:  ').upper()
                                    print('WELCOME %s!' % RM_player.name.upper())
                                    RM_player.name2 = input('PLAYER2-->Please enter your name:  ').upper()
                                    print('WELCOME %s!' % RM_player.name2.upper())
                                    if RM_player.name is '':
                                        RM_player.name = 'Player1'
                                    if RM_player.name2 is '':
                                        RM_player.name2 = 'Player2'
                                    RM_player.names[0] = RM_player.name
                                    RM_player.names[1] = RM_player.name2
                                else:
                                    pass


                                def get_hint():
                                    help = choice(word_list)
                                    while help in RM_player.gap_str:
                                        help = choice(word_list)
                                    for letter in word_list:
                                        index = ([pos for pos, letter in enumerate(word_list) if letter == help])
                                        for element in index:
                                            RM_player.word_gap[element] = help


                                def end_game():
                                    print('GAME OVER!')
                                    score = ("(%s)%d : (%s)%d" % (
                                    RM_player.names[0], RM_player.counts[0], RM_player.names[1], RM_player.counts[1]))
                                    print('SCORE:  ', score)


                                # FUNCTION 3 ENDS
                                quit = False
                                while not quit:
                                    cycle = 1
                                    recycle = False
                                    while not recycle:
                                        if True:
                                            # FUNCTION 4 STARTS
                                            Continue = False
                                            if game_state_loaded is False:
                                                RM_player.names_neutral = RM_player.names[1]
                                                RM_player.names[1] = RM_player.names[0]
                                                RM_player.names[0] = RM_player.names_neutral
                                                RM_player.coins_neutral = RM_player.coins_list[1]
                                                RM_player.coins_list[1] = RM_player.coins_list[0]
                                                RM_player.coins_list[0] = RM_player.coins_neutral
                                                RM_player.streaks_neutral = RM_player.streaks[1]
                                                RM_player.streaks[1] = RM_player.streaks[0]
                                                RM_player.streaks[0] = RM_player.streaks_neutral
                                                RM_player.counts_neutral = RM_player.counts[1]
                                                RM_player.counts[1] = RM_player.counts[0]
                                                RM_player.counts[0] = RM_player.counts_neutral
                                        # FUNCTION 4 ENDS
                                        if game_state_loaded is False:
                                            RM_player.game_word = choice(Word_collection).upper()
                                        else:
                                            pass
                                        Description_Dict = {'NOUN': Noun, 'VERB': Verb, 'ADJECTIVE': Adjective,
                                                            'ADVERB': Adverb,
                                                            'SPORT': Sport,
                                                            'FOOD/FRUIT': Food_Fruit, 'COUNNTRY/CITY': Country_City,
                                                            'SCHOOL': School,
                                                            'BODY': Body,
                                                            'CALENDER/TIME': Calendar_Time,
                                                            'PROFESSION': Profession, 'MUSIC': Music, 'BEACH': Beach,
                                                            'FAMILY': Family,
                                                            'FLOWER': Flower, 'COLOUR': Colour}

                                        # FUNCTION 5 STARTS
                                        if game_state_loaded is False:
                                            word_list = list(RM_player.game_word)
                                        else:
                                            pass
                                        if game_state_loaded is False:
                                            RM_player.word_gap = ('_' * len(RM_player.game_word))
                                        else:
                                            pass
                                        if game_state_loaded is False:
                                            RM_player.gap_str = '   '.join(RM_player.word_gap)
                                        else:
                                            pass
                                        if game_state_loaded is False:
                                            RM_player.word_gap = list(RM_player.word_gap)
                                        else:
                                            pass
                                        if game_state_loaded is False:
                                            RM_player.tries = 0
                                        else:
                                            pass
                                        if game_state_loaded is False:
                                            RM_player.save_game('random')
                                        else:
                                            pass

                                        RM_player.tries = 0
                                        # FUNCTION 5 ENDS
                                        print('%s TURN....' % RM_player.names[1])
                                        print('ROUND %d>>>' % RM_player.game_rounds)
                                        while RM_player.tries < RM_player.game_max_trial:
                                            RM_player.save_game('random')


                                            def obt_key(val):
                                                for key, value in Description_Dict.items():
                                                    if val == value:
                                                        return key


                                            for item in Description_Dict.values():
                                                if RM_player.game_word.lower() in item or RM_player.game_word.capitalize() in item:
                                                    print('WORD DESCRIPTION:  ', obt_key(item))
                                            print(RM_player.gap_str)
                                            print()
                                            RM_player.save_game('random')
                                            # FUNCTION 6 STARTS
                                            hint = input(
                                                "GET HINT? \nENTER 'Y' OR 'y' TO CONFIRM OTHERWISE, PRESS ANY KEY:   ")
                                            if hint == 'y' or hint == 'Y':
                                                if RM_player.coins_list[1] >= 3:
                                                    get_hint()
                                                    RM_player.gap_str = '   '.join(RM_player.word_gap)
                                                    RM_player.coins_list[1] -= 3
                                                    print('%s, YOUR COINS LEFT:  %d' % (
                                                    RM_player.names[1], RM_player.coins_list[1]))
                                                    RM_player.save_game('random')
                                                    if '_' not in RM_player.gap_str:
                                                        print(RM_player.gap_str)
                                                        win_comment = ['BRILLIANT!', 'AWESOME!', 'BRAVO!', 'GREAT!',
                                                                       'ASTONISHING!',
                                                                       'EYE-WATERING!',
                                                                       'FANTASTIC!', 'WOW!', 'OUTSTANDING!',
                                                                       'OUTRAGEOUS!',
                                                                       'EXTRAORDINARY!',
                                                                       'WHOA!',
                                                                       'CONGRATULATIONS!']
                                                        print(choice(win_comment))
                                                        RM_player.counts[1] += 1
                                                        print('POINTS:  ', RM_player.counts[1])
                                                        RM_player.streaks[1] += 1
                                                        print("%s STREAK:  %d" % (
                                                        RM_player.names[1], RM_player.streaks[1]))
                                                        RM_player.save_game('random')
                                                        if RM_player.streaks[1] % 5 == 0:
                                                            streak_comment = ['%d IN A ROW!' % RM_player.streaks[1],
                                                                              '%d IN %d!' % (RM_player.streaks[1],
                                                                                             RM_player.streaks[1]),
                                                                              'CONSECUTIVE %d WINS!' %
                                                                              RM_player.streaks[1],
                                                                              '%d AT ONCE!' % RM_player.streaks[1]]
                                                            print(choice(streak_comment))
                                                            RM_player.coins_list[1] += 5
                                                            print('%s EARNED 5 COINS!\tCOINS:  %d' % (
                                                            RM_player.names[1], RM_player.coins_list[1]))
                                                            RM_player.tries = 10
                                                            Continue = True
                                                            break
                                                        else:
                                                            RM_player.coins_list[1] += 1
                                                            print('%s EARNED A COIN!\tCOINS:  %d' % (
                                                            RM_player.names[1], RM_player.coins_list[1]))
                                                            RM_player.tries = 10
                                                            Continue = True
                                                            break
                                                        RM_player.save_game('random')
                                                else:
                                                    print('INSUFFICIENT COINS!')
                                                    RM_player.save_game('random')
                                            else:
                                                guess = input('Your guess, %s?:  ' % RM_player.names[1]).upper()
                                                RM_player.save_game('random')
                                                if guess in RM_player.game_word:
                                                    index = ([pos for pos, letter in enumerate(RM_player.game_word) if
                                                              letter == guess])
                                                    for element in index:
                                                        RM_player.word_gap[element] = guess
                                                        RM_player.gap_str = '   '.join(RM_player.word_gap)
                                                        RM_player.save_game('random')
                                                        if '_' not in RM_player.gap_str:
                                                            print(RM_player.gap_str)
                                                            win_comment = ['BRILLIANT!', 'AWESOME!', 'BRAVO!', 'GREAT!',
                                                                           'ASTONISHING!',
                                                                           'EYE-WATERING!',
                                                                           'FANTASTIC!', 'WOW!', 'OUTSTANDING!',
                                                                           'OUTRAGEOUS!',
                                                                           'EXTRAORDINARY!', 'WHOA!',
                                                                           'CONGRATULATIONS!']
                                                            print(choice(win_comment))
                                                            RM_player.counts[1] += 1
                                                            RM_player.streaks[1] += 1
                                                            print("%s STREAK:  %d" % (
                                                            RM_player.names[1], RM_player.streaks[1]))
                                                            RM_player.save_game('random')
                                                            if RM_player.streaks[1] % 5 == 0:
                                                                streak_comment = ['%d IN A ROW!' % RM_player.streaks[1],
                                                                                  '%d IN %d!' % (RM_player.streaks[1],
                                                                                                 RM_player.streaks[1]),
                                                                                  'CONSECUTIVE %d WINS!' %
                                                                                  RM_player.streaks[1],
                                                                                  '%d AT ONCE!' % RM_player.streaks[1]]
                                                                print(choice(streak_comment))
                                                                RM_player.coins_list[1] += 5
                                                                print('%s EARNED 5 COINS!\tCOINS:  %d' % (
                                                                    RM_player.names[1], RM_player.coins_list[1]))
                                                                RM_player.tries = 10
                                                                Continue = True
                                                                break
                                                            else:
                                                                RM_player.coins_list[1] += 1
                                                                print('%s EARNED A COIN!\tCOINS:  %d' % (
                                                                    RM_player.names[1], RM_player.coins_list[1]))
                                                                RM_player.tries = 10
                                                                Continue = True
                                                                break
                                                            RM_player.save_game('random')

                                                else:
                                                    RM_player.tries += 1
                                                    print(guess, 'is not in the word')
                                                    RM_player.save_game('random')
                                        else:
                                            if Continue == False:
                                                print('MAN HANGED!!!')
                                                print(
                                                    'You\'re out of tries \nYOU LOST! \nThe hidden word is \'%s\'' % RM_player.game_word)
                                                RM_player.save_game('random')
                                        if cycle % 2 == 0:
                                            RM_player.name2 = RM_player.names[1]
                                            RM_player.coins2 = RM_player.coins_list[1]
                                            RM_player.count2 = RM_player.counts[1]
                                            RM_player.streak2 = RM_player.streaks[1]
                                            Exit = input(
                                                'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                                            if Exit == '1':
                                                end_game()
                                                quit = True
                                                game_state_loaded = False
                                                RM_player.save_game('random')
                                                break
                                            else:
                                                score = ("(%s)%d : (%s)%d" % (
                                                RM_player.names[0], RM_player.counts[0], RM_player.names[1],
                                                RM_player.counts[1]))
                                                print('SCORE:  ', score)
                                                RM_player.game_rounds += 1
                                                game_state_loaded = False
                                                RM_player.save_game('random')
                                                break
                                        else:
                                            RM_player.name = RM_player.names[1]
                                            RM_player.coins = RM_player.coins_list[1]
                                            RM_player.count = RM_player.counts[1]
                                            RM_player.streak = RM_player.streaks[1]
                                            cycle += 1
                                            game_state_loaded = False
                                            RM_player.save_game('random')
                                        # FUNCTION 6 ENDS

                            elif selection2 in ['b', 'B']:
                                difficulty_level('player')
                                # FUNCTION 3 STARTS--> B
                                Player1 = input('PLAYER1-->Please enter your name:  ').upper()
                                print('WLECOME %s!' % Player1.upper())
                                Player2 = input('PLAYER2-->Please enter your name:  ').upper()
                                print('WLECOME %s!' % Player2.upper())
                                Players = [Player1, Player2]
                                count1 = 0
                                count2 = 0
                                streak1 = 0
                                streak2 = 0
                                coins1 = 0
                                coins2 = 0
                                rounds = 1
                                coins = [coins1, coins2]
                                streaks = [streak1, streak2]
                                counts = [count1, count2]


                                def get_hint():
                                    help = choice(word_list)
                                    while help in gap_str:
                                        help = choice(word_list)
                                    for letter in word_list:
                                        index = ([pos for pos, letter in enumerate(word_list) if letter == help])
                                        for element in index:
                                            gap[element] = help


                                def end_game():
                                    print('GAME OVER!')
                                    score = ("(%s)%d : (%s)%d" % (Players[0], counts[0], Players[1], counts[1]))
                                    print('SCORE:  ', score)


                                # FUNCTION 3 ENDS--> B

                                # FUNCTION 7 STARTS
                                Description_Dict = {'A1': ['Adjective', Adjective], 'A2': ['Adverb', Adverb],
                                                    'B1': ['Beach', Beach],
                                                    'B2': ['Body', Body],
                                                    'C1': ['Calendar_Time', Calendar_Time], 'C2': ['Colour', Colour],
                                                    'C3': ['Country_City', Country_City],
                                                    'F1': ['Family', Family], 'F2': ['Flower', Flower],
                                                    'F3': ['Food_Fruit', Food_Fruit],
                                                    'M': ['Music', Music],
                                                    'N': ['Noun', Noun], 'P': ['Profession', Profession],
                                                    'S1': ['School', School],
                                                    'S2': ['Sport', Sport], 'V': ['Verb', Verb]}
                                for keys, values in Description_Dict.items():
                                    print(keys, '=', values[0])
                                selection = input(
                                    "Please enter the corresponding value of the words category you'd like to play: ").upper()
                                # FUNCTION 7 ENDS
                                quit = False
                                while not quit:
                                    # FUNCTION 4 STARTS ---> B
                                    Continue = False
                                    cycle = 1
                                    Players_neutral = Players[1]
                                    Players[1] = Players[0]
                                    Players[0] = Players_neutral
                                    coins_neutral = coins[1]
                                    coins[1] = coins[0]
                                    coins[0] = coins_neutral
                                    streaks_neutral = streaks[1]
                                    streaks[1] = streaks[0]
                                    streaks[0] = streaks_neutral
                                    counts_neutral = counts[1]
                                    counts[1] = counts[0]
                                    counts[0] = counts_neutral
                                    # FUNCTION 4 ENDS---> B
                                    for keys, values in Description_Dict.items():
                                        if selection in keys:
                                            word_description = values[0]
                                            word = choice(values[1]).upper()
                                            # FUNCTION 5 STARTS--->B
                                            word_list = list(word)
                                            gap = ('_' * len(word))
                                            gap_str = '   '.join(gap)
                                            gap = list(gap)
                                            tries = 0
                                            # FUNCTION 5 ENDS--->B
                                    print('%s TURN....' % Players[1])
                                    while tries < max_trial:
                                        print('WORD DESCRIPTION:  ', word_description)
                                        print(gap_str)
                                        hint = input(
                                            "GET HINT? \nENTER 'Y' OR 'y' TO CONFIRM OTHERWISE, PRESS ANY KEY:   ")
                                        if hint == 'y' or hint == 'Y':
                                            if coins[1] >= 3:
                                                get_hint()
                                                gap_str = '   '.join(gap)
                                                coins[1] -= 3
                                                print('%s, YOUR COINS LEFT:  %d' % (Players[1], coins[1]))
                                                if '_' not in gap_str:
                                                    print(gap_str)
                                                    win_comment = ['BRILLIANT!', 'AWESOME!', 'BRAVO!', 'GREAT!',
                                                                   'ASTONISHING!',
                                                                   'EYE-WATERING!',
                                                                   'FANTASTIC!', 'WOW!', 'OUTSTANDING!', 'OUTRAGEOUS!',
                                                                   'EXTRAORDINARY!',
                                                                   'WHOA!',
                                                                   'CONGRATULATIONS!']
                                                    print(choice(win_comment))
                                                    counts[1] += 1
                                                    print('POINTS:  ', counts[1])
                                                    streaks[1] += 1
                                                    print("%s STREAK:  %d" % (Players[1], streaks[1]))
                                                    if streaks[1] % 5 == 0:
                                                        streak_comment = ['%d IN A ROW!' % streaks[1],
                                                                          '%d IN %d!' % (streaks[1], streaks[1]),
                                                                          'CONSECUTIVE %d WINS!' % streaks[1],
                                                                          '%d AT ONCE!' % streaks[1]]
                                                        print(choice(streak_comment))
                                                        coins[1] += 5
                                                        print('%s EARNED 5 COINS!\tCOINS:  %d' % (Players[1], coins[1]))
                                                        tries = 10
                                                        Continue = True
                                                        break
                                                    else:
                                                        coins[1] += 1
                                                        print('%s EARNED A COIN!\tCOINS:  %d' % (Players[1], coins[1]))
                                                        tries = 10
                                                        Continue = True
                                                        break
                                            else:
                                                print('INSUFFICIENT COINS!')
                                        else:
                                            guess = input('Your guess, %s?:  ' % Players[1]).upper()
                                            if guess in word:
                                                index = ([pos for pos, letter in enumerate(word) if letter == guess])
                                                for element in index:
                                                    gap[element] = guess
                                                    gap_str = '   '.join(gap)
                                                    if '_' not in gap_str:
                                                        print(gap_str)
                                                        win_comment = ['BRILLIANT!', 'AWESOME!', 'BRAVO!', 'GREAT!',
                                                                       'ASTONISHING!',
                                                                       'EYE-WATERING!',
                                                                       'FANTASTIC!', 'WOW!', 'OUTSTANDING!',
                                                                       'OUTRAGEOUS!',
                                                                       'EXTRAORDINARY!',
                                                                       'WHOA!',
                                                                       'CONGRATULATIONS!']
                                                        print(choice(win_comment))
                                                        counts[1] += 1
                                                        streaks[1] += 1
                                                        print("%s STREAK:  %d" % (Players[1], streaks[1]))
                                                        if streaks[1] % 5 == 0:
                                                            streak_comment = ['%d IN A ROW!' % streaks[1],
                                                                              '%d IN %d!' % (streaks[1], streaks[1]),
                                                                              'CONSECUTIVE %d WINS!' % streaks[1],
                                                                              '%d AT ONCE!' % streaks[1]]
                                                            print(choice(streak_comment))
                                                            coins[1] += 5
                                                            print('%s EARNED 5 COINS!\tCOINS:  %d' % (
                                                            Players[1], coins[1]))
                                                            tries = 10
                                                            Continue = True
                                                            break
                                                        else:
                                                            coins[1] += 1
                                                            print('%s EARNED A COIN!\tCOINS:  %d' % (
                                                            Players[1], coins[1]))
                                                            tries = 10
                                                            Continue = True
                                                            break

                                            else:
                                                tries += 1
                                                print(guess, 'is not in the word')
                                    else:
                                        if Continue == False:
                                            print('MAN HANGED!!!')
                                            print('You\'re out of tries \nYOU LOST! \nThe hidden word is \'%s\'' % word)
                                    if Players[1] == Player2:
                                        Exit = input(
                                            'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                                        if Exit == '1':
                                            end_game()
                                            quit = True
                                            break
                                        else:
                                            score = ("(%s)%d : (%s)%d" % (Players[0], counts[0], Players[1], counts[1]))
                                            print('SCORE:  ', score)
                                            rounds += 1
                                            print('ROUND %d>>>' % rounds)
                                            # TRY CONNECTING FUNCTION 6  INTO THIS PLACE
                                    cycle += 1

                elif mode in ['b', 'B']:
                    player = Player()
                    try:
                        player.load_game()
                        game_state_loaded = True
                        print(player)
                    except FileNotFoundError as f:
                        game_state_loaded = False
                        print('PLEASE CREATE PLAYER PROFILE')
                        player.name = input('Please enter player name:  ').upper()
                        print('WELCOME TO THE HANGMAN WORLD, %s!' % player.name)
                        difficulty_level(player)
                        player.game_revival_coins = 20
                        player.streak = 0
                        player.game_rounds = 1
                        player.wins = 0
                        player.losses = 0
                        player.coins = 5000
                        player.save_game()


                    def get_hint():
                        help = choice(word_list)
                        while help in player.gap_str:
                            help = choice(word_list)
                        for letter in word_list:
                            index = ([pos for pos, letter in enumerate(word_list) if letter == help])
                            for element in index:
                                player.word_gap = list(player.word_gap)
                                player.word_gap[element] = help


                    def end_game():
                        print('GAME OVER!')
                        score = ('SCORE:  %d / %d' % (player.wins, player.game_rounds))
                        print(score)
                        GameOn = True
                        ExitForLoop = True
                        ExitForLoop2 = True
                        Quit = True
                        return


                    game_Level_WordLength_dict = {1: ['UNLOCKED', [20, 14, 15, 16, 2, 4]], 2: ['LOCKED', [5, 6, 11]],
                                                  3: ['LOCKED', [5, 6, 11]],
                                                  4: ['LOCKED', [7, 8, 12, 13, 18, 19]],
                                                  5: ['LOCKED', [7, 8, 12, 13, 18, 19]], 6: ['LOCKED', [9, 10]]}
                    player.game_division_dict = {1: ['UNLOCKED', 'rating1', 'NOT PLAYED'],
                                                 2: ['LOCKED', 'rating2', 'NOT PLAYED'],
                                                 3: ['LOCKED', 'rating3', 'NOT PLAYED'],
                                                 4: ['LOCKED', 'rating4', 'NOT PLAYED'],
                                                 5: ['LOCKED', 'rating5', 'NOT PLAYED'],
                                                 6: ['LOCKED', 'rating6', 'NOT PLAYED'],
                                                 7: ['LOCKED', 'rating7', 'NOT PLAYED'],
                                                 8: ['LOCKED', 'rating8', 'NOT PLAYED'],
                                                 9: ['LOCKED', 'rating9', 'NOT PLAYED'],
                                                 10: ['LOCKED', 'rating10', 'NOT PLAYED'],
                                                 11: ['LOCKED', 'rating11', 'NOT PLAYED'],
                                                 12: ['LOCKED', 'rating12', 'NOT PLAYED'],
                                                 13: ['LOCKED', 'rating13', 'NOT PLAYED'],
                                                 14: ['LOCKED', 'rating14', 'NOT PLAYED'],
                                                 15: ['LOCKED', 'rating15', 'NOT PLAYED'],
                                                 16: ['LOCKED', 'rating16', 'NOT PLAYED'],
                                                 17: ['LOCKED', 'rating17', 'NOT PLAYED'],
                                                 18: ['LOCKED', 'rating18', 'NOT PLAYED'],
                                                 19: ['LOCKED', 'rating19', 'NOT PLAYED'],
                                                 20: ['LOCKED', 'rating20', 'NOT PLAYED'],
                                                 21: ['LOCKED', 'rating21', 'NOT PLAYED'],
                                                 22: ['LOCKED', 'rating22', 'NOT PLAYED'],
                                                 23: ['LOCKED', 'rating23', 'NOT PLAYED'],
                                                 24: ['LOCKED', 'rating24', 'NOT PLAYED'],
                                                 25: ['LOCKED', 'rating25', 'NOT PLAYED'],
                                                 26: ['LOCKED', 'rating26', 'NOT PLAYED'],
                                                 27: ['LOCKED', 'rating27', 'NOT PLAYED'],
                                                 28: ['LOCKED', 'rating28', 'NOT PLAYED'],
                                                 29: ['LOCKED', 'rating29', 'NOT PLAYED'],
                                                 30: ['LOCKED', 'rating30', 'NOT PLAYED'],
                                                 31: ['LOCKED', 'rating31', 'NOT PLAYED'],
                                                 32: ['LOCKED', 'rating32', 'NOT PLAYED'],
                                                 33: ['LOCKED', 'rating33', 'NOT PLAYED'],
                                                 34: ['LOCKED', 'rating34', 'NOT PLAYED'],
                                                 35: ['LOCKED', 'rating35', 'NOT PLAYED'],
                                                 36: ['LOCKED', 'rating36', 'NOT PLAYED'],
                                                 37: ['LOCKED', 'rating37', 'NOT PLAYED'],
                                                 38: ['LOCKED', 'rating38', 'NOT PLAYED'],
                                                 39: ['LOCKED', 'rating39', 'NOT PLAYED'],
                                                 40: ['LOCKED', 'rating40', 'NOT PLAYED'],
                                                 41: ['LOCKED', 'rating41', 'NOT PLAYED'],
                                                 42: ['LOCKED', 'rating42', 'NOT PLAYED'],
                                                 43: ['LOCKED', 'rating43', 'NOT PLAYED'],
                                                 44: ['LOCKED', 'rating44', 'NOT PLAYED'],
                                                 45: ['LOCKED', 'rating45', 'NOT PLAYED'],
                                                 46: ['LOCKED', 'rating46', 'NOT PLAYED'],
                                                 47: ['LOCKED', 'rating47', 'NOT PLAYED'],
                                                 48: ['LOCKED', 'rating48', 'NOT PLAYED'],
                                                 49: ['LOCKED', 'rating49', 'NOT PLAYED'],
                                                 50: ['LOCKED', 'rating50', 'NOT PLAYED']}


                    def level_security():
                        if player.game_difficulty.upper() in ['A', 'B', '']:
                            # for key, values in (pair for pair in game_Level_WordLength_dict.items() if
                            # not pair == (1, ['unlocked', [20, 14, 15, 16, 2, 4]])):
                            global stop_game
                            stop_game = False
                            if stop_game2 == False:
                                for key, values in game_Level_WordLength_dict.items():
                                    # print('welcome ooo')
                                    if player.game_level == key:
                                        while values[0] == 'LOCKED':
                                            stop_game = True
                                            print('LEVEL LOCKED! \nUNLOCK PREVIOUS LEVEL FIRST')
                                            return
                                        else:
                                            stop_game = None
                                            return
                            else:
                                for key, values in player.game_division_dict.items():
                                    if player.game_division == key:
                                        while values[0] == 'LOCKED':
                                            stop_game = True
                                            print('DIVISION LOCKED! \nUNLOCK PREVIOUS DIVISION FIRST')
                                            break


                    level_button = False
                    while not level_button:
                        print('LEVEL1 \nLEVEL2 \nLEVEL3 \nLEVEL4 \nLEVEL5 \nLEVEL6')
                        GameOn = False
                        while not GameOn:
                            if game_state_loaded is True:
                                pass
                            else:
                                player.game_level = int(input('ENTER LEVEL NUMBER TO SELECT THE LEVEL:  '))
                                stop_game2 = False
                                level_security()
                                if stop_game == True:
                                    continue
                            player.save_game()
                            print('LEVEL %d>>>' % player.game_level)
                            while player.game_level <= 6:
                                for num in range(1, 7):
                                    for num2 in range(1, 51):
                                        if player.game_level == num:
                                            print('DIVISION %d' % num2, end=' ')
                                print()
                                stop_game2 = True
                                if game_state_loaded is True:
                                    pass
                                else:
                                    player.game_division = int(input('ENTER DIVISION NUMBER TO SELECT THE DIVISION:  '))
                                    level_security()
                                    if stop_game == True:
                                        continue
                                player.save_game()
                                # player.game_division =1
                                ExitForLoop = False
                                for num in range(1, 51):
                                    if ExitForLoop == True:
                                        break
                                    for num in range(1, 51):
                                        if player.game_division == num:
                                            print('LEVEL %d; DIVISION %d BEGINS>>>' % (
                                                player.game_level, num)) if game_state_loaded != True else print(
                                                'CONTINUING FROM LAST MEMORY... \nLEVEL %d; DIVISION %d>>>' % (
                                                    player.game_level, num))
                                            player.save_game()
                                    ExitForLoop2 = False
                                    for key, value in game_Level_WordLength_dict.items():
                                        if ExitForLoop2 == True:
                                            break
                                        # SEEMS LIKE A PART HERE IS REPEATED
                                        if player.game_level == key:
                                            if game_state_loaded is True and '_' in player.gap_str:
                                                player.game_word
                                            else:
                                                player.game_word = choice(Word_collection).upper()
                                            player.save_game()
                                            while len(player.game_word) not in value[1]:
                                                if game_state_loaded is True and '_' in player.gap_str:
                                                    player.game_word
                                                else:
                                                    player.game_word = choice(Word_collection).upper()
                                                player.save_game()
                                            else:
                                                Quit = False
                                                while not Quit:
                                                    # while player.game_rounds <= 10
                                                    for round in range(11 - player.game_rounds):
                                                        print('ROUND %d>>>' % player.game_rounds)
                                                        for key, value in game_Level_WordLength_dict.items():
                                                            # SEEMS LIKE THERE'S A REPITION HERE
                                                            if player.game_level == key:
                                                                if game_state_loaded is True and '_' in player.gap_str:
                                                                    player.game_word
                                                                else:
                                                                    player.game_word = choice(Word_collection).upper()
                                                                player.save_game()
                                                                while len(player.game_word) not in value[1]:
                                                                    if game_state_loaded is True and '_' in player.gap_str:
                                                                        player.game_word
                                                                    else:
                                                                        player.game_word = choice(
                                                                            Word_collection).upper()
                                                                    player.save_game()
                                                        Description_Dict = {'NOUN': Noun, 'VERB': Verb,
                                                                            'ADJECTIVE': Adjective, 'ADVERB': Adverb,
                                                                            'SPORT': Sport,
                                                                            'FOOD/FRUIT': Food_Fruit,
                                                                            'COUNNTRY/CITY': Country_City,
                                                                            'SCHOOL': School,
                                                                            'BODY': Body,
                                                                            'CALENDER/TIME': Calendar_Time,
                                                                            'PROFESSION': Profession, 'MUSIC': Music,
                                                                            'BEACH': Beach, 'FAMILY': Family,
                                                                            'FLOWER': Flower, 'COLOUR': Colour}
                                                        # FUNCTION 5 STARTS---> C
                                                        word_list = list(player.game_word)
                                                        if game_state_loaded is True and '_' in player.gap_str:
                                                            player.word_gap
                                                        else:
                                                            # try:
                                                            #     if '_' not in player.gap_str:
                                                            #         player.game_rounds = player.wins + player.losses
                                                            # except TypeError:
                                                            #     pass
                                                            player.word_gap = ('_' * len(player.game_word))
                                                        if game_state_loaded is True and '_' in player.gap_str:
                                                            player.gap_str
                                                        else:
                                                            player.gap_str = '   '.join(player.word_gap)
                                                        if game_state_loaded is True and '_' in player.gap_str:
                                                            player.word_gap
                                                        else:
                                                            player.word_gap = list(player.word_gap)
                                                        if game_state_loaded is True and '_' in player.gap_str:
                                                            player.tries
                                                        else:
                                                            player.tries = 0
                                                        # FUNCTION 5 ENDS---> C

                                                        # FUNCTION 8 STARTS
                                                        player.save_game()
                                                        while player.tries < player.game_max_trial:
                                                            def obt_key(val):
                                                                for key, value in Description_Dict.items():
                                                                    if val == value:
                                                                        return key


                                                            for item in Description_Dict.values():
                                                                if player.game_word.lower() in item or player.game_word.capitalize() in item:
                                                                    print('WORD DESCRIPTION:  ', obt_key(item))
                                                            print(player.gap_str)
                                                            player.save_game()
                                                            print()
                                                            # FUNCITON 8 ENDS

                                                            # FUNCTION 2 STARTS---> B
                                                            hint = input(
                                                                "GET HINT? \nENTER 'Y' OR 'y' TO CONFIRM OTHERWISE, PRESS ANY KEY:   ")
                                                            if hint == 'y' or hint == 'Y':
                                                                if player.coins >= 10:
                                                                    get_hint()
                                                                    player.gap_str = '   '.join(player.word_gap)
                                                                    player.coins -= 10
                                                                    player.save_game()
                                                                    print('COINS LEFT:  ', player.coins)

                                                                    if '_' not in player.gap_str:
                                                                        print(player.gap_str)
                                                                        player.save_game()
                                                                        win_comment = ['BRILLIANT!', 'AWESOME!',
                                                                                       'BRAVO!', 'GREAT!',
                                                                                       'ASTONISHING!',
                                                                                       'EYE-WATERING!',
                                                                                       'FANTASTIC!', 'WOW!',
                                                                                       'OUTSTANDING!', 'OUTRAGEOUS!',
                                                                                       'EXTRAORDINARY!',
                                                                                       'WHOA!',
                                                                                       'CONGRATULATIONS!']
                                                                        print(choice(win_comment))
                                                                        player.wins += 1
                                                                        # player.game_rounds += 1
                                                                        player.save_game()
                                                                        print('WINS:  ', player.wins)
                                                                        player.streak += 1
                                                                        player.save_game()
                                                                        print('STREAK: ', player.streak)
                                                                        if player.streak % 5 == 0:
                                                                            streak_comment = [
                                                                                '%d IN A ROW!' % player.streak,
                                                                                '%d IN %d!' % (
                                                                                    player.streak, player.streak),
                                                                                'CONSECUTIVE %d WINS!' % player.streak,
                                                                                '%d AT ONCE!' % player.streak]
                                                                            print(choice(streak_comment))
                                                                            if player.game_division_dict[
                                                                                player.game_division][
                                                                                2] == 'NOT PLAYED':
                                                                                player.coins += 5
                                                                                print('YOU EARNED 5 COINS!\t COINS:  ',
                                                                                      player.coins)
                                                                            else:
                                                                                pass
                                                                            player.save_game()
                                                                        else:
                                                                            if player.game_division_dict[
                                                                                player.game_division][
                                                                                2] == 'NOT PLAYED':
                                                                                player.coins += 1
                                                                                print('YOU EARNED A COIN!\t COINS:  ',
                                                                                      player.coins)
                                                                            else:
                                                                                pass
                                                                            player.save_game()

                                                                        Exit = input(
                                                                            'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                                                                        if Exit == '1':
                                                                            end_game()
                                                                            game_state_loaded = False
                                                                            player.save_game()
                                                                            break
                                                                        else:
                                                                            score = ('SCORE:  %d / %d' % (
                                                                                player.wins, player.game_rounds))
                                                                            print('SCORE:  ', score)
                                                                            player.game_rounds += 1
                                                                            game_state_loaded = False
                                                                            player.save_game()
                                                                            break
                                                                else:
                                                                    print('INSUFFICIENT COINS!')
                                                                    player.save_game()
                                                                    pass

                                                            else:
                                                                guess = (input('Your guess?  ')).upper()
                                                                player.save_game()
                                                                if guess in player.game_word:
                                                                    index = (
                                                                        [pos for pos, letter in
                                                                         enumerate(player.game_word)
                                                                         if letter == guess])
                                                                    for element in index:
                                                                        player.word_gap[element] = guess
                                                                        player.save_game()
                                                                    player.gap_str = '   '.join(player.word_gap)
                                                                    player.save_game()
                                                                    if '_' not in player.gap_str:
                                                                        print(player.gap_str)
                                                                        player.save_game()
                                                                        win_comment = ['BRILLIANT!', 'AWESOME!',
                                                                                       'BRAVO!', 'GREAT!',
                                                                                       'ASTONISHING!',
                                                                                       'EYE-WATERING!', 'FANTASTIC!',
                                                                                       'WOW!', 'OUTSTANDING!',
                                                                                       'OUTRAGEOUS!',
                                                                                       'EXTRAORDINARY!', 'WHOA!',
                                                                                       'CONGRATULATIONS!']
                                                                        print(choice(win_comment))
                                                                        player.wins += 1
                                                                        # player.game_rounds += 1
                                                                        player.save_game()
                                                                        print('WINS:  ', player.wins)
                                                                        player.streak += 1
                                                                        player.save_game()
                                                                        print('STREAK: ', player.streak)
                                                                        if player.streak % 5 == 0:
                                                                            streak_comment = [
                                                                                '%d IN A ROW!' % player.streak,
                                                                                '%d IN %d!' % (
                                                                                    player.streak, player.streak),
                                                                                'CONSECUTIVE %d WINS!' % player.streak,
                                                                                '%d AT ONCE!' % player.streak]
                                                                            print(choice(streak_comment))
                                                                            if player.game_division_dict[
                                                                                player.game_division][
                                                                                2] == 'NOT PLAYED':
                                                                                player.coins += 5
                                                                                print('YOU EARNED 5 COINS!\t COINS:  ',
                                                                                      player.coins)
                                                                            else:
                                                                                pass
                                                                            player.save_game()
                                                                        else:
                                                                            if player.game_division_dict[
                                                                                player.game_division][
                                                                                2] == 'NOT PLAYED':
                                                                                player.coins += 1
                                                                                print('YOU EARNED A COIN!\t COINS:  ',
                                                                                      player.coins)
                                                                            else:
                                                                                pass
                                                                            player.save_game()
                                                                        print(player.gap_str)

                                                                        Exit = input(
                                                                            'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                                                                        if Exit == '1':
                                                                            end_game()
                                                                            game_state_loaded = False
                                                                            player.save_game()
                                                                            GameOn = True
                                                                            ExitForLoop = True
                                                                            ExitForLoop2 = True
                                                                            Quit = True
                                                                            player.save_game()
                                                                            break
                                                                        else:
                                                                            score = ('SCORE:  %d / %d' % (
                                                                                player.wins, player.game_rounds))
                                                                            print('SCORE:  ', score)
                                                                            player.game_rounds += 1
                                                                            game_state_loaded = False
                                                                            player.save_game()
                                                                            break

                                                                else:
                                                                    player.tries += 1
                                                                    player.save_game()
                                                                    print(guess, 'is not in the word')

                                                        else:
                                                            print('MAN HANGED!!!')
                                                            print(
                                                                'You\'re out of tries \nGAME OVER! \nThe word is \'%s\'' % player.game_word)
                                                            revival = input(
                                                                "REVIVE MAN? \nEnter 'y' or 'Y' to confirm otherwise, press any key:  ")
                                                            if revival in ['y', 'Y']:
                                                                if player.coins >= player.game_revival_coins:
                                                                    print('MAN REVIVED!!!')
                                                                    player.tries -= player.game_max_trial
                                                                    player.save_game()
                                                                    player.coins -= player.game_revival_coins
                                                                    player.save_game()
                                                                    player.game_revival_coins += 10
                                                                    player.save_game()
                                                                    print('REMAINING COINS:  ', player.coins)
                                                                    continue
                                                                else:
                                                                    print('INSUFFICIENT COINS!')
                                                                    player.losses += 1
                                                                    # player.game_rounds += 1
                                                                    player.save_game()
                                                                    if player.streak > 0:
                                                                        player.streak = 0
                                                                        player.save_game()
                                                                        print('STREAK ENDS!')
                                                                        print('LOSES: ', player.losses)

                                                                    Exit = input(
                                                                        'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS ANY KEY TO CONTINUE:')
                                                                    if Exit == '1':
                                                                        option_made = True
                                                                        end_game()
                                                                        GameOn = True
                                                                        ExitForLoop = True
                                                                        ExitForLoop2 = True
                                                                        Quit = True
                                                                        game_state_loaded = False
                                                                        player.save_game()
                                                                        break
                                                                    else:
                                                                        option_made = True
                                                                        score = ('%d/%d' % (
                                                                            player.wins, player.game_rounds))
                                                                        print('SCORE:  ', score)
                                                                        player.game_rounds += 1
                                                                        game_state_loaded = False
                                                                        player.save_game()
                                                                        continue


                                                            else:
                                                                player.losses += 1
                                                                player.save_game()
                                                                if player.streak > 0:
                                                                    player.streak = 0
                                                                    player.save_game()
                                                                    print('STREAK ENDS!')
                                                                    print('LOSES: ', player.losses)

                                                                Exit = input(
                                                                    'END GAME? PRESS 1 TO CONFIRM, OTHERWISE PRESS '
                                                                    'ANY KEY TO CONTINUE:')
                                                                if Exit == '1':
                                                                    end_game()
                                                                    GameOn = True
                                                                    ExitForLoop = True
                                                                    ExitForLoop2 = True
                                                                    Quit = True
                                                                    game_state_loaded = False
                                                                    player.save_game()
                                                                    break
                                                                else:
                                                                    score = ('%d/%d' % (
                                                                        player.wins, player.game_rounds))
                                                                    print('SCORE:  ', score)
                                                                    player.game_rounds += 1
                                                                    game_state_loaded = False
                                                                    player.save_game()

                                                    else:
                                                        if player.wins in [5, 6]:
                                                            division_rating = 1
                                                            print('YOU WON THIS DIVISION WITH 1 STAR')
                                                        elif player.wins in [7, 8, 9]:
                                                            division_rating = 2
                                                            print('YOU WON THIS DIVISION WITH 2 STARS')
                                                        elif player.wins in [10]:
                                                            division_rating = 3
                                                            print('YOU WON THIS DIVISION WITH 3 STARS')
                                                        else:
                                                            print(
                                                                'YOU CAN\'T CONTINUE TO THE NEXT DIVISION AS THE MINIMUM WIN REQUIRED IS 5')
                                                            player.streak = 0
                                                            player.wins = 0
                                                            player.losses = 0
                                                            player.game_rounds = 1
                                                            ExitForLoop = True
                                                            ExitForLoop2 = True
                                                            Quit = True
                                                            game_state_loaded = False
                                                            player.save_game()
                                                            break
                                                        player.game_division_dict[player.game_division][2] = 'PLAYED'
                                                        game_state_loaded = False
                                                        player.save_game()
                                                        player.game_division_dict[player.game_division][
                                                            1] = division_rating
                                                        player.game_division += 1
                                                        player.game_division_dict[player.game_division][0] = 'UNLOCKED'
                                                        player.save_game()
                                                        if player.game_division > 50:
                                                            print(
                                                                'LEVEL %d IS FINISHED! \nNEXT LEVEL>>>' % player.game_level) if player.game_level != 6 else print(
                                                                'CONGRATUTLATIONS! \nYOU\'VE REACHED THE END OF THE HANGMAN GAME\'S CAREER MODE...')
                                                            player.streak = 0
                                                            player.wins = 0
                                                            player.losses = 0
                                                            player.coins += 7
                                                            print('YOU EARNED 7 COOL COINS!')
                                                            player.game_rounds = 1
                                                            player.game_level += 1
                                                            player.save_game()
                                                            for key, values in game_Level_WordLength_dict.items():
                                                                if player.game_level == key:
                                                                    values[0] = 'UNLOCKED'
                                                            if player.game_level <= 6:
                                                                print('LEVEL %d IS UNLOCKED' % player.game_level)
                                                            else:
                                                                pass
                                                            player.save_game()
                                                            ExitForLoop = True
                                                            ExitForLoop2 = True
                                                            Quit = True
                                                            player.save_game()
                                                            break

                                                        else:
                                                            print('DIVISION %d IS UNLOCKED' % player.game_division)
                                                            player.streak = 0
                                                            player.wins = 0
                                                            player.losses = 0
                                                            player.coins += 5
                                                            print('YOU EARNED 5 COOL COINS! \nCOINS:  ', player.coins)
                                                            player.game_rounds = 1
                                                            game_state_loaded = False
                                                            player.save_game()
                                                            break
