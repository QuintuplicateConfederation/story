import random


def arpanet():
    print('"We\'re doing a network of computers. Making computers talk to each other." You give the same talk you\'ve '
          'given a million times.\n"How will the data be transmitted?" Norm asks.\n"Through telephone lines," you '
          'answer.\n"Why are you using 19th century technology to accomplish a 20th century purpose?" challenges '
          'Norm.\n"Because it works," you reply, "what do you guys use?"\n"Radio waves," he says.\n"How do you get '
          'line-of-sight through all these tall buildings, all these high mountains, all the thick vegetation?"\n'
          '"Repeaters," he says, "loads of them. Say, do you wanna know our ambition?" ')


def alohanet():
    print('"We wangled two frequencies, an inbound and an outbound one. The users send messages into the computer '
          'through the inbound channel, and they get a short acknowledgment back through the outbound channel'
          ' if there hasn\'t been a collision. If there has, they get no acknowledgment, and retransmit after '
          'waiting a random time. But do you know the other potential of the ALOHA system?" Norm tests you.\n"No," you '
          'admit.\n"Don\'t worry. We didn\'t, either. You guys use packet switching, where you can only go '
          'point-to-point on wires, right?"\n"Yes," you confess.\n"Well, we don\'t do packet switching; '
          'we do packet broadcasting."\n"What do you use to split data up into packets like our IMPs?"\n'
          '"Well, there are actually two equivalents, TCUs - terminal control unit - on the user side, MENEHUNE -'
          ' a dwarf people in Hawaiian mythology - on the computer side. Your IMPs store and forward; we don\'t exactly'
          ' have a precise equivalent, because we only have one central computer, not many like yours. Our TCUs, scan '
          'the headers of every packet transmitted on ALOHA, and ignore those which are not addressed to them. Can you '
          'see the advantages of that? How\'s that for efficiency? No need to wire any new TCUs in. The equipment\'s '
          'all you need. And with our 9600 bit per second connection, we can accommodate 200 teletypes entering data as'
          ' fast as you can type. So the inbound channel is also called the \'random access channel\', the outbound '
          'channel is also called the \'broadcasting channel\', and ALOHA is a \'random access protocol\', because the'
          ' TCUs send whenever they damn well please, and wait a random time before retransmitting if they don\'t get '
          'an acknowledgment. Simple, too, isn\'t it?')


print("NETWORKING IN PARADISE.\n\nAn ALOHAnet text adventure\n\n2021 Free to Use and Republish\n\nFor All My Readers")
a = int(input("Type 0 to begin: "))
if a == 0:
    print("You're on the 707 over the crystal-clear waters of the infinite Pacific Ocean. You've just concluded a "
          "three-week visit to Australia and are headed for Honolulu.\nThe plane's been flying for an hour, and its motion "
          "soon lulls you to sleep. You start dreaming of the fun you had and the work you did all these three weeks in Aus"
          "tralia. The 747 flight over, stopping in Hawaii to stretch your legs and refuel. Driving to Queensland and bac"
          "k with Tom.\nIt's early morning at Kingsford Smith Airport. Next to you is your brother, Clement, with his girlf"
          "riend, Helen, in his arms. Beside Helen is her brother, Tom. Clement is about to go back to Vietnam. "
          "Helen is sobbing. ")
    a = int(input("Do you comfort her? Yes (1), no (2) "))
if a == 1:
    print('"I\'m angry about the war," Helen says, "how they\'re drafting men off the streets to fight it. You should '
          'have taken the deal, Clem. That way I wouldn\'t have to watch you die."\n"There\'s no point, Helen," Clement'
          ' hugs her and walks away. "Come with me, Homer," Clement begs.')
    a = int(input('Do you follow Clement? Yes (3), no (4) '))
if a == 2:
    print('"You work for the Department of Defense, don\'t you?" Helen gets in your face. "Don\'t deny it!"')
    a = int(input('Apologize (5), defend yourself (6) '))
if a == 3:
    print('You follow Clement into the airport terminal. "Look at the hippie!" an airman shouts and points at you. '
          'You show him your Defense Department ID and watch his jaws drop.\n"I wanted to confess something," says '
          'Clement. \n"I feel angry at you because you \'dodged the draft\'. I know you\'re doing something important '
          'and I know it\'s not right for me to feel that way. But..."\n"You have every right to feel that way, Clem. '
          'I feel this too. I feel like I failed you."\n"You didn\'t fail me, Homer. I look up to you, and I love you."'
          ' You walk away.')
    a = 7
if a == 4:
    print('Clem looks over his shoulder but finds no one behind him. He walks away, slouching a bit more than before.')
    a = 7
if a == 5:
    print('"I\'m sorry," you say. \n"Sorry\'s not enough!" responds Helen. "You\'re aiding and abetting the war'
          ' by working for it."\n"Come on, Helen," says Tom. "Neither of us is very happy about the war. It\'s his brot'
          'her too!"\nThe drive home is frosty.')
    a = 7
if a == 6:
    print('"I don\'t work for the DOD," you say. "They just pay me to help my research because it\'ll contribute to the'
          'national defense."\n"So you are \'contributing to the national defense\'," Helen points at your nose, '
          '"and doing their dirty work though not actively participating."\n"Come on, Helen," says Tom. "Neither of us '
          'is very happy about the war. It\'s his brother too!"\nThe drive home is frosty.')
    a = 7
if a == 7:
    print('\n"Dinner is served, sir," the Pan Am stewardess rouses you gently. You get a metal fork and knife and a tra'
          'y with a one-pound steak, a quart of milk, and ice cream. You eat heartily.\nFrom your window seat you can '
          'see the curtain of night being drawn over the Pacific Ocean, stage of the greatest dramas and scenes of '
          'world history. Right now a great conflict is going on, but that doesn\'t mean there aren\'t side plots. '
          'The cloudless sky is endless as the sea below. Stars appear one by one against a dignified, regal blue '
          'backdrop.\nAfter your finished tray is taken away, you drift back into sleep. This time your sleep is dream'
          'less.\n\nYou feel something heavy below you. You realize that the plane has landed in Honolulu.\nYou '
          'disembark, go to the terminal, go through Immigration, get your passport stamped, are welcomed to the United'
          ' States of America by a dour immigration agent. Now comes the hard part. Customs.')
    b = random.choice([0, 0, 0, 0, 1])
    if b == 1:
        print('"Sir? Sir? What\'s this? Would you come with me, sir." The customs agent is holding something. You look'
              ' at it. It\'s the blue box Ada gave you, signed with her name and number.\n\nGAME OVER.')
        quit()
    else:
        print('Customs is uneventful. Which is just as good for you and your blue box. You have to look for a Norman '
              'Abramson. You see him holding up a sign reading "HOMER CARLSON". You walk to him. Norm\'s a Caucasian '
              'man with a whitening beard and a healthy copper tan. You go together to the parking lot, and you drive'
              ' down H-1 through the bustling city of Honolulu to the campus of the University of Hawaii at Manoa.')
        a = int(input("Ask him what he's doing (8),  tell him what you're doing (9) "))
if a == 8:
    print('"I dare to assume you know that Hawaii is an archipelago," Norm begins. "Although they say Hawaii has eight '
          'islands, one is uninhabited, one is forbidden to visit, and two others have population in the four digits. '
          'The main campus of the University of Hawaii - the one we\'re going to now is on Oahu, where we have three'
          ' community colleges. On the Island of Hawaii - the biggest island, which we call the Big Island - we have a '
          'second campus and another community college. Kauai and Maui have one community college apiece.\n'
          '"The difference between us and the Mainland is that, unlike you guys, the University of Hawaii controls the '
          'community colleges as well as the four-year \'teaching\' and graduate \'research\' universities. Here lies '
          'the problem. Legally and functionally, we are not a group of colleges - we\'re one university with buildings'
          ' spread out over 200 miles of water. As you can see, the unique geographical circumstances of the Hawaiian'
          ' Islands mean that telephone lines aren\'t really practical for transmitting data, whereas a radio-based '
          'transmission system is much more extensible. So what are you guys up to?"')
    arpanet()
    a = int(input("Yes (10), no (11) "))
if a == 9:
    arpanet()
    a = int(input("Yes (10), no (11) "))
if a == 10:
    print('"Space. It\'s the Space Age after all. What can be sent between land-based transceivers can be sent via'
          ' a satellite in geostationary orbit thereby expanding its range to an entire section of the globe. And we '
          'have that satellite; NASA\'s ATS-1 - makes Sputnik look like the Hindenburg with what it can do. Just one '
          'voice-quality line could serve over a hundred. We could link with you guys. And Australia. And Japan. '
          'All without having to lay a single mile of cable. NASA and the University of Alaska are working with us '
          'on this."\n"NASA\'s obvious, but why Alaska?"\n"They have the same problem as we do. Only public university'
          ' in the whole state. Only it\'s not just water separating their campuses - there\'s glaciers, forests, '
          'and the highest mountains in all of North America! So they had to look up to geosynchronous equatorial '
          'orbit to find a way they could do what we did. And when we link up, you\'re gonna be sorry you put us '
          'together in the corner of the map.')
    a = 13
if a == 12:
    print('"I suppose you didn\'t come here to learn about ambitions. Let\'s just talk about how Additive Links '
          'On-Line Hawaii Area - the ALOHA System, ALOHAnet works.')
    a = 13
if a == 13:
    print('"Usually, we use both radio and telephone to transmit voice messages, right?" compares Norm. \n"Yes," you '
          'agree.\n"And you\'ll concede that transmitting data is very different from transmitting sound?" contrasts N'
          'orm.\n"Don\'t see how this is open to dispute," you confess.\n"So what\'s your solution to the problem of'
          ' transmitting data on a system designed to transmit sound?"\n"We split our messages up into packets," you '
          'say. "These packets have a header, kind of like an envelope, saying where they need to be. And every server'
          ' that gets a packet stores and forwards it to a closer one to the destination."\n"The ideal, though wasteful'
          ', solution, would be a channel for every member of our network," says Norm. "This was what we proposed to'
          ' the FCC, but the rat bastards denied it. So, necessity became the mother of invention. We got a single exp'
          'erimental frequency, and we needed to find some way for our 8 nodes to share it.\n"There are two traditional'
          ' ways multiple points can share one frequency. One is subdividing the frequency we have so that each'
          ' pair of receivers gets a channel they can use all the time. Another is allocating all of the frequency to '
          'a given pair of receivers at a set time. Both of these solutions provide exclusivity, and exclusivity is '
          'really not what we need, is it? Computers are intermittent - what we call \'bursty\'. They need exclusivity'
          ' for a split second, just to send one command and wait for its response. And they might send a command at '
          'any time. So the need for exclusivity is brief, but unpredictable.\n"It really hit me while I was surfing '
          'one day at Waikiki. I was watching the waves hit the beach. You know about superposition. Sometimes two '
          'waves would combine to form a bigger one, other times the crest of one wave would superpose with the trough'
          ' of another and level out. But they were few and far between. Most of the time, waves retained their '
          'amplitude until they crashed into the shore.\n"I realized that the problem frequency and time division were'
          ' intended to solve - interference - wasn\'t really that much of a big deal within the context of our'
          ' problem. As long as users sent what they wanted to send again after a collision, and as long as messages '
          'didn\'t take too long to get to Honolulu, the messages were going to get through eventually.')
    a = int(input("Doubt (14), accept (15) "))
if a == 14:
    print('"Won\'t that just replicate the collision?" you wonder.\n"That\'s the magic of the matter," Norm says, "they'
          ' don\'t all wait the same time to resend. It\'s a randomly selected time. So they\'ll resend at different '
          'times.')
    alohanet()
    a = 16
if a == 15:
    print('"The magic of the matter is they don\'t all wait the same time to resend. They wait a randomly selected '
          'time and resend at different times.')
    alohanet()
    a = 16
if a == 16:
    print('"So what\'s ALOHAnet good for?"\n"You wanna know?" boasted Norm. "How about the first satellite-delivered'
          ' lecture in world history? Students in Honolulu and Hilo, over 200 miles away, sat in on the same lecture'
          ', together, and participated in activities together."\nYou\'re agape.\n\nAbove you clouds are massing, '
          'billowing back and forth, nearly black on the bottom, white on the top, a menacing army ravishing the blue'
          ' sky. The army begins to bomb the ground below. Fat raindrops land on the windshield, growing more and more'
          ' dense by the second. The rain is drenching, warm, and - exuberantly tropical. Norm turns on the headlamps.'
          ' You drive through the rain, which seems to have taken on a personality of its own - trying to get into any'
          ' exposed space, soaking anything out in the open, blocking the view with drops which have now turned long '
          'and needle-like. Norm seems to be almost feeling his way through now with his puny headlights. Finally you '
          'come to the University Avenue exit; Norm executes a swift, flawless right turn, goes down to University '
          'Avenue, U-turns, and turns right onto Dole Street in almost blinding rain. "Way to welcome us,"'
          ' quips Norm. But just then you see the sky lighten up, a beam of sunlight penetrating the formerly uniform'
          'ly dark sky. The drops die away as sunshine reconquers the land. The only signs it ever rained are puddles '
          'in all the low ground that will quickly dry - and a splendid double rainbow crowning the Engineering Complex'
          'like a hood.\n"It\'s beautiful," you exclaim, as Norm steers the car into a staff-only parking lot.\n'
          '"Let\'s go surfing," invites Norm.')
